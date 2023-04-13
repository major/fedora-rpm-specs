# remirepo/fedora spec file for php-nyholm-psr7
#
# Copyright (c) 2019-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
# github
%global gh_commit    bf4aebd170fadf5fd808c70b90535de327e81a50
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Nyholm
%global gh_project   psr7
# packagist
%global pk_vendor    nyholm
%global pk_project   %{gh_project}
%global major        %nil
# namespace
%global php_home     %{_datadir}/php
%global ns_vendor    Nyholm
%global ns_project   Psr7

%bcond_without       tests

# php-http/psr7-integration-tests 1.1.0
%global psr7_integration_tests_commit b63c2f50c114a474086c6801aea58c0aa96f9b27
%global psr7_integration_tests_short  %(c=%{psr7_integration_tests_commit}; echo ${c:0:7})
# http-interop/http-factory-tests 0.9.0
%global http_factory_tests_commit     642056c5360e8a74779cbf133afbc8aa2c174e15
%global http_factory_tests_short      %(c=%{http_factory_tests_commit}; echo ${c:0:7})

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.6.0
Release:        1%{?dist}
Summary:        A fast PHP7 implementation of PSR-7

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot for skip .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
# Only used for tests and no version released (dev-master required)
Source2:        https://github.com/php-http/psr7-integration-tests/archive/%{psr7_integration_tests_commit}/%{name}-integration-tests-%{psr7_integration_tests_short}.tar.gz
Source3:        https://github.com/http-interop/http-factory-tests/archive/%{http_factory_tests_commit}/%{name}-factory-tests-%{http_factory_tests_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-pcre
BuildRequires:  php-spl
%if %{with tests}
BuildRequires: (php-composer(psr/http-message)          >= 1.0 with php-composer(psr/http-message)         < 2)
BuildRequires: (php-composer(php-http/message-factory)  >= 1.0 with php-composer(php-http/message-factory) < 2)
BuildRequires: (php-composer(psr/http-factory)          >= 1.0 with php-composer(psr/http-factory)         < 2)
BuildRequires: (php-composer(symfony/error-handler)     >= 4.4 with php-composer(symfony/error-handler)    < 5)
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^7.5 || 8.5 || 9.4",
#        "php-http/psr7-integration-tests": "^1.0",
#        "http-interop/http-factory-tests": "^0.9",
#        "symfony/error-handler": "^4.4"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.4
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0

# from composer.json, "require": {
#        "php": ">=7.1",
#        "psr/http-message": "^1.0",
#        "php-http/message-factory": "^1.0",
#        "psr/http-factory": "^1.0"
Requires:       php(language) >= 7.1
Requires:      (php-composer(psr/http-message)          >= 1.0 with php-composer(psr/http-message)         < 2)
Requires:      (php-composer(php-http/message-factory)  >= 1.0 with php-composer(php-http/message-factory) < 2)
Requires:      (php-composer(psr/http-factory)          >= 1.0 with php-composer(psr/http-factory)         < 2)
# from phpcompatinfo report for version 1.1.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
Provides:       php-composer(psr/http-message-implementation) = 1.0
Provides:       php-composer(psr/http-factory-implementation) = 1.0


%description
A super lightweight PSR-7 implementation. Very strict and very fast..

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit} -a2 -a3


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
    '%{_datadir}/php/Http/Message/autoload.php',
    '%{_datadir}/php/Psr/Http/Message/http-factory-autoload.php',
]);
EOF

# Generate test Autoloader
phpab --template fedora --output test-autoload.php \
    psr7-integration-tests-%{psr7_integration_tests_commit} \
    http-factory-tests-%{http_factory_tests_commit}


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
require_once '%{php_home}/Symfony4/Component/ErrorHandler/autoload.php';
require_once dirname(__DIR__) . '/test-autoload.php';
EOF

: Fix path
sed -e 's:./vendor/http-interop/http-factory-tests:http-factory-tests-%{http_factory_tests_commit}:' \
    phpunit.xml.dist >phpunit.xml

: Run upstream test suite
: Ignore online tests
# TODO testCanDetachStream may fail on local build (extension conflicts ?)
# testIsNotSeekable|testIsNotWritable|testIsNotReadable|testRewindNotSeekable fail only in mock
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(testIsNotSeekable|testIsNotWritable|testIsNotReadable|testRewindNotSeekable|testCanDetachStream)).)*$' \
      --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/%{ns_vendor}


%changelog
* Tue Apr 11 2023 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Thu Feb  3 2022 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul  5 2021 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Wed Feb 24 2021 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0

* Fri Jan 29 2021 Remi Collet <remi@remirepo.net> - 1.3.2-2
- fix test path and FTBFS

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep  6 2019 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1 (no change)

* Fri Aug 23 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Remi Collet <remi@remirepo.net> - 1.1.0-2
- License is MIT

* Fri Jun 28 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- initial package, version 1.1.0
