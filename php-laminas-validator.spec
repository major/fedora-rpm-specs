# remirepo/Fedora spec file for php-laminas-validator
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# When buid without db, filter, http, session, uri
%global bootstrap    0
%global gh_commit    695bfa40b0a83dc1c5c58bdf74a03fdbeb516c39
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-validator
%global zf_name      zend-validator
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Validator
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        2.28.0
Release:        1%{?dist}
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
BuildRequires:  php-date
BuildRequires:  php-fileinfo
BuildRequires:  php-hash
BuildRequires:  php-intl
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.12.0 with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.13   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/http-message)                           >= 1.0.1  with php-composer(psr/http-message)                           < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "^2.4.0",
#        "laminas/laminas-db": "^2.15.0",
#        "laminas/laminas-filter": "^2.23.0",
#        "laminas/laminas-http": "^2.17.0",
#        "laminas/laminas-i18n": "^2.19",
#        "laminas/laminas-session": "^2.13.0",
#        "laminas/laminas-uri": "^2.10.0",
#        "phpunit/phpunit": "^9.5.25",
#        "psalm/plugin-phpunit": "^0.18.0",
#        "psr/http-client": "^1.0.1",
#        "psr/http-factory": "^1.0.1",
#        "vimeo/psalm": "^4.28"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.19   with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
%if ! %{bootstrap}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-db)                   >= 2.15   with php-autoloader(%{gh_owner}/laminas-db)                   < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.23   with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.17   with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.13   with php-autoloader(%{gh_owner}/laminas-session)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.10   with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
%endif
BuildRequires: (php-composer(psr/http-client)                            >= 1.0.1  with php-composer(psr/http-client)                            < 2)
BuildRequires: (php-composer(psr/http-factory)                           >= 1.0.1  with php-composer(psr/http-factory)                           < 2)
BuildRequires:  phpunit9 >= 9.5.25
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-servicemanager": "^3.12.0",
#        "laminas/laminas-stdlib": "^3.13",
#        "psr/http-message": "^1.0.1"
Requires:       php(language) >= 8.0
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.12.0 with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.13   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/http-message)                           >= 1.0.1  with php-composer(psr/http-message)                           < 2)
# From composer, "suggest": {
#        "laminas/laminas-db": "Laminas\\Db component, required by the (No)RecordExists validator",
#        "laminas/laminas-filter": "Laminas\\Filter component, required by the Digits validator",
#        "laminas/laminas-i18n": "Laminas\\I18n component to allow translation of validation error messages",
#        "laminas/laminas-i18n-resources": "Translations of validator messages",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component to allow using the ValidatorPluginManager and validator chains",
#        "laminas/laminas-session": "Laminas\\Session component, ^2.8; required by the Csrf validator",
#        "laminas/laminas-uri": "Laminas\\Uri component, required by the Uri and Sitemap\\Loc validators",
Suggests:       php-composer(%{gh_owner}/laminas-db)
Suggests:       php-composer(%{gh_owner}/laminas-filter)
Suggests:       php-composer(%{gh_owner}/laminas-i18n)
Suggests:       php-composer(%{gh_owner}/laminas-i18n-resources)
Suggests:       php-composer(%{gh_owner}/laminas-servicemanager)
Suggests:       php-composer(%{gh_owner}/laminas-session)
Suggests:       php-composer(%{gh_owner}/laminas-uri)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.13.0
Requires:       php-ctype
Requires:       php-date
Requires:       php-fileinfo
Requires:       php-hash
Requires:       php-intl
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.13.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{namespace}\Validator component provides a set of commonly needed validators.
It also provides a simple validator chaining mechanism by which multiple
validators may be applied to a single datum in a user-defined order.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/Psr/Http/Message/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Db/autoload.php',
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/I18n/Translator/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/%{namespace}/Uri/Translator/Resources.php',
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
# For BR without new autoloader
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Psr/Http/Client/autoload.php',
    '%{php_home}/Psr/Http/Message/http-factory-autoload.php',
    dirname(__DIR__) . '/test/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

%if  %{bootstrap}
rm -r test/Db/
rm -r test/Sitemap/
rm    test/BarcodeTest.php
rm    test/CreditCardTest.php
rm    test/CsrfTest.php 
rm    test/DigitsTest.php 
rm    test/NotEmptyTest.php
rm    test/UriTest.php
%endif

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Hex") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd -d memory_limit=1G %{_bindir}/phpunit9 --verbose || ret=1
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
* Mon Nov 14 2022 Remi Collet <remi@remirepo.net> - 2.28.0-1
- update to 2.28.0
- add mandatory dependency on psr/http-message

* Wed Oct 12 2022 Remi Collet <remi@remirepo.net> - 2.26.0-1
- update to 2.26.0
- raise dependency on PHP 8.0

* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 2.25.0-1
- update to 2.25.0
- raise dependency on zend-stdlib >= 3.13

* Thu Jul 28 2022 Remi Collet <remi@remirepo.net> - 2.23.0-1
- update to 2.23.0

* Mon Jul 25 2022 Remi Collet <remi@remirepo.net> - 2.22.0-1
- update to 2.22.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  1 2022 Remi Collet <remi@remirepo.net> - 2.20.1-1
- update to 2.20.1 (no change)

* Thu Jun 16 2022 Remi Collet <remi@remirepo.net> - 2.20.0-1
- update to 2.20.0
- raise dependency on PHP 7.4
- add dependency on laminas-servicemanager
- drop dependency on container-interop/container-interop
- drop weak dependency on laminas-math

* Fri Jun 10 2022 Remi Collet <remi@remirepo.net> - 2.19.0-1
- update to 2.19.0

* Thu Jun  9 2022 Remi Collet <remi@remirepo.net> - 2.18.0-1
- update to 2.18.0
- raise dependency on zend-stdlib >= 3.10

* Wed Mar  9 2022 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0

* Mon Jan 24 2022 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec  2 2021 Remi Collet <remi@remirepo.net> - 2.15.1-1
- update to 2.15.1

* Thu Sep  9 2021 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on zend-stdlib >= 3.6

* Fri Jul 30 2021 Remi Collet <remi@remirepo.net> - 2.14.5-3
- fix regression in Validator/Barcode/Royalmail using patch from
  https://github.com/laminas/laminas-validator/pull/106

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Remi Collet <remi@remirepo.net> - 2.14.5-1
- update to 2.14.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Remi Collet <remi@remirepo.net> - 2.14.4-1
- update to 2.14.4

* Fri Jan 22 2021 Remi Collet <remi@remirepo.net> - 2.14.2-1
- update to 2.14.2

* Fri Jan  8 2021 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0
- raise dependency on PHP 7.3
- raise dependency on zend-stdlib 3.3
- switch to phpunit9

* Thu Jan  7 2021 Remi Collet <remi@remirepo.net> - 2.13.5-1
- update to 2.13.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr  1 2020 Remi Collet <remi@remirepo.net> - 2.13.4-1
- update to 2.13.4

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.13.3-1
- update to 2.13.3 (no change)
- not bootstrap build

* Mon Mar 16 2020 Remi Collet <remi@remirepo.net> - 2.13.2-1
- update to 2.13.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1
- drop patch merged upstream
- switch to phpunit8

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- switch to Laminas
- boostrap build without config, db, filter, http, session and uri

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency on PHP 7.1
- add patch for PHP 7.4 from
  https://github.com/laminas/laminas-validator/pull/32

* Tue Oct 29 2019 Remi Collet <remi@remirepo.net> - 2.12.2-1
- update to 2.12.2

* Sun Oct 13 2019 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1

* Thu Jan 31 2019 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0
- raise dependency on zend-stdlib 3.2.1

* Fri Dec 14 2018 Remi Collet <remi@remirepo.net> - 2.11.0-2
- update to 2.11.0
- add weak dependency on psr/http-message
- use range dependencies

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 2.10.2-1
- Update to 2.10.2
- switch to phpunit6

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.10-1-3
- switch from zend-loader to fedora/autoloader

* Tue Oct 31 2017 Remi Collet <remi@remirepo.net> - 2.10.1-2
- fix FTBFS from Koschei, add patch for test with 7.2 from
  https://github.com/zendframework/zend-validator/pull/205

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 2.10.1-1
- Update to 2.10.1

* Tue Aug 15 2017 Remi Collet <remi@remirepo.net> - 2.10.0-1
- Update to 2.10.0

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 2.9.2-1
- Update to 2.9.2
- add patch for PHP 7.2 from
  https://github.com/zendframework/zend-validator/pull/190

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 2.9.1-1
- Update to 2.9.1

* Fri Mar 17 2017 Remi Collet <remi@remirepo.net> - 2.9.0-1
- Update to 2.9.0
- raise dependency on PHP 5.6
- raise dependency on zend-stdlib 2.7.6
- use phpunit6 on F26+

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2

* Tue Nov 15 2016 Remi Collet <remi@fedoraproject.org> - 2.8.1-2
- add patch for PHP 7.1 and timezone changes
- open https://github.com/zendframework/zend-validator/pull/136

* Thu Jun 23 2016 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Tue May 17 2016 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- Update to 2.7.2

* Wed Apr  6 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1

* Wed Apr  6 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Thu Feb 18 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0
- raise dependency on zend-stdlib ^2.7
- add dependency on container-interop/container-interop

* Fri Sep  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-2
- fix description

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package
