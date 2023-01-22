# remirepo/Fedora spec file for php-laminas-http
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    76de9008f889bc7088f85a41d0d2b06c2b59c53d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-http
%global zf_name      zend-http
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Http
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.18.0
Release:        2%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-ctype
BuildRequires:  php-curl
BuildRequires:  php-date
BuildRequires:  php-fileinfo
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-zlib
BuildRequires: (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.8    with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.9.1  with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.15   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "ext-curl": "*",
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "phpunit/phpunit": "^9.5.25"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.25
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-loader": "^2.8",
#        "laminas/laminas-stdlib": "^3.6",
#        "laminas/laminas-uri": "^2.9.1",
#        "laminas/laminas-validator": "^2.15"
Requires:       php(language) >= 8.0
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.8    with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.9.1  with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.15   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.11.2
Requires:       php-ctype
Requires:       php-curl
Requires:       php-date
Requires:       php-fileinfo
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl
Requires:       php-zlib

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.11.3
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Http is a primary foundational component of %{namespace} Framework.
Since much of what PHP does is web-based, specifically HTTP,
it makes sense to have a performant, extensible, concise and
consistent API to do all things HTTP.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Loader/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Uri/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(__DIR__)) . '/%{namespace}/%{library}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Client") ? 0 : 1);
'

BIT=$(php -r 'echo PHP_INT_SIZE;')
if [ $BIT -lt 8 ]; then
FILTER='^((?!(testWriteCanHandleFloatHttpVersion|testWriteCanHandleStringHttpVersion|testStreamCompression|testChunkedResponsePerformance|testSetCookieSetExpiresWithStringDateBiggerThen2038)).)*$'
else
FILTER='^((?!(testWriteCanHandleFloatHttpVersion|testWriteCanHandleStringHttpVersion|testStreamCompression|testChunkedResponsePerformance)).)*$'
fi

: upstream test suite
# testStreamCompression: online test
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
       --filter $FILTER \
       || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Remi Collet <remi@remirepo.net> - 2.18.0-1
- update to 2.18.0

* Mon Nov 14 2022 Remi Collet <remi@remirepo.net> - 2.17.1-1
- update to 2.17.1

* Mon Oct 17 2022 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0
- raise dependency on PHP 8.0

* Thu Aug 18 2022 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec  3 2021 Remi Collet <remi@remirepo.net> - 2.15.1-1
- update to 2.15.1

* Fri Sep 10 2021 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on zend-loader >= 2.8
- raise dependency on zend-stdlib >= 3.6
- raise dependency on zend-uri >= 2.9.1
- raise dependency on zend-validator >= 2.15

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Remi Collet <remi@remirepo.net> - 2.14.3-1
- update to 2.14.3 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Remi Collet <remi@remirepo.net> - 2.14.2-1
- update to 2.14.2
- raise dependency on PHP 7.3
- switch to phpunit9

* Wed Aug 19 2020 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.11.2-2
- cleanup

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.11.2-1
- switch to Laminas

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 2.11.2-1
- update to 2.11.2

* Thu Dec  5 2019 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Tue Dec  3 2019 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0

* Tue Dec  3 2019 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Wed Jan 23 2019 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Wed Jan  9 2019 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on zend-stdlib 3.2.1

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 2.8.2-3
- skip 2 failing tests with recent PHP

* Fri Aug 17 2018 Remi Collet <remi@remirepo.net> - 2.8.2-1
- update to 2.8.2

* Thu Aug 02 2018 Shawn Iwinski <shawn@iwin.ski> - 2.8.1-1
- Update to 2.8.1 (ZF2018-01)

* Fri Apr 27 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.7.0-2
- switch from zend-loader to fedora/autoloader

* Thu Nov  2 2017 Remi Collet <remi@remirepo.net> - 2.7.0-1
- Update to 2.7.0
- use phpunit6 on F26+
- raise dependency on PHP 5.6
- raise dependency on zendframework/zend-loader 2.5.1
- raise dependency on zendframework/zend-stdlib 2.7.7
- raise dependency on zendframework/zend-uri 2.5.2
- raise dependency on zendframework/zend-validator 2.10.1

* Wed Feb  1 2017 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- version 2.6.0

* Mon Aug  8 2016 Remi Collet <remi@fedoraproject.org> - 2.5.5-1
- version 2.5.5

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- version 2.5.4

* Tue Sep 15 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- version 2.5.3

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- version 2.5.2

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
