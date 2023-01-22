# remirepo/fedora spec file for php-swiftmailer
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please preserve changelog entries
#
%global gh_commit    181b89f18a90f8925ef805f950d47a7190e9b950
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swiftmailer
%global gh_project   swiftmailer
%global with_tests   0%{!?_without_tests:1}
%global php_home     %{_datadir}/php

Name:           php-%{gh_project}
Version:        5.4.12
Release:        10%{?dist}
Summary:        Free Feature-rich PHP Mailer

License:        MIT
URL:            http://www.swiftmailer.org/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php-reflection
BuildRequires:  php-simplexml
BuildRequires:  php-bcmath
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-mhash
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  php-fedora-autoloader-devel
# From composer.json, "require-dev": {
#        "mockery/mockery": "~0.9.1",
#        "symfony/phpunit-bridge": "~3.2"
BuildRequires: (php-composer(mockery/mockery) >= 0.9.1      with php-composer(mockery/mockery) <  1)
# ignore minimal version as test suite passes with 2.8
BuildRequires:  php-composer(symfony/phpunit-bridge) <  4
%endif

# From composer.json, "require": {
#        "php": ">=5.3.3"
Requires:       php(language) >= 5.3.3
# from phpcompatinfo report on version 5.4.8
Requires:       php-reflection
Requires:       php-simplexml
Requires:       php-bcmath
Requires:       php-ctype
Requires:       php-date
Requires:       php-hash
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-mhash
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl

# Removed from official repo in Fedora 25
Obsoletes:      php-swift-Swift   <= 5.4.1
# Single package in this channel
Obsoletes:      php-channel-swift <= 1.3
Provides:       php-pear(pear.swiftmailer.org/Swift) = %{version}

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Swift Mailer integrates into any web app written in PHP, offering a 
flexible and elegant object-oriented approach to sending emails with 
a multitude of features.

Autoloader: %{php_home}/Swift/swift_required.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

# Install using the same layout than the old PEAR package
mv lib/swift_required_pear.php lib/swift_required.php
rm lib/swiftmailer_generate_mimes_config.php


%build
# Empty build section, most likely nothing required.


%install
mkdir -p                   %{buildroot}/%{php_home}/Swift
cp -p lib/*.php            %{buildroot}/%{php_home}/Swift/
cp -pr lib/classes/*       %{buildroot}/%{php_home}/Swift/
cp -pr lib/dependency_maps %{buildroot}/%{php_home}/Swift/


%check
%if %{with_tests}
: Use installed tree and autoloader
mkdir vendor
%{_bindir}/phpab --format fedora --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}/%{php_home}/Swift/swift_required.php';
require_once '%{php_home}/Mockery/autoload.php';
if (file_exists('%{php_home}/Symfony3/Bridge/PhpUnit')) {
  \Fedora\Autoloader\Autoload::addPsr4('Symfony\\Bridge\\PhpUnit\\', '%{php_home}/Symfony3/Bridge/PhpUnit');
} else {
  \Fedora\Autoloader\Autoload::addPsr4('Symfony\\Bridge\\PhpUnit\\', '%{php_home}/Symfony/Bridge/PhpUnit');
}
EOF

TMPDIR=$(mktemp -d $PWD/rpmtests-XXXXXXXX)
cat << EOF | tee tests/acceptance.conf.php
<?php
define('SWIFT_TMP_DIR', '$TMPDIR');
EOF

if [ $(php -r 'echo PHP_VERSION_ID;') -lt 70400 ]; then
  : Run upstream test suite
  ret=0
  for cmd in php php72 php73; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit --exclude smoke --verbose || ret=1
    fi
  done
  rm -r $TMPDIR
else
  : Skip test suite as mockery is broken for 7.4
fi
exit $ret
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGES README
%doc doc
%doc composer.json
%{php_home}/Swift


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb  4 2020 Remi Collet <remi@remirepo.net> - 5.4.12-4
- disable test suite with PHP 7.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 17 2018 Remi Collet <remi@remirepo.net> - 5.4.12-1
- update to 5.4.12

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Remi Collet <remi@remirepo.net> - 5.4.9-1
- Update to 5.4.9

* Tue Nov  7 2017 Remi Collet <remi@remirepo.net> - 5.4.8-4
- fix FTBFS from Koschei
- add version constraint for symfony/phpunit-bridge

* Wed Oct  4 2017 Remi Collet <remi@remirepo.net> - 5.4.8-3
- drop unneeded dependency on php-mcrypt

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Remi Collet <remi@remirepo.net> - 5.4.8-1
- Update to 5.4.8

* Fri Apr 21 2017 Remi Collet <remi@remirepo.net> - 5.4.7-1
- Update to 5.4.7

* Mon Feb 13 2017 Remi Collet <remi@fedoraproject.org> - 5.4.6-1
- update to 5.4.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Remi Collet <remi@fedoraproject.org> - 5.4.5-1
- update to 5.4.5
- fix Remote Code Execution CVE-2016-10074

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 5.4.4-1
- update to 5.4.4

* Fri Jul  8 2016 Remi Collet <remi@fedoraproject.org> - 5.4.3-1
- update to 5.4.2
- drop patch merged upstream

* Mon May  2 2016 Remi Collet <remi@fedoraproject.org> - 5.4.2-1
- update to 5.4.2

* Mon Mar 28 2016 Remi Collet <remi@fedoraproject.org> - 5.4.1-2
- obsolete php-swift-Swift, retired in F25

* Fri Oct 16 2015 Remi Collet <remi@fedoraproject.org> - 5.4.1-1
- initial rpm, version 5.4.1
- sources from github, pear channel is dead

