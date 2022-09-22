# remirepo/Fedora spec file for php-laminas-test
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    ae49929c0060800f0e516cb984620674dfb74458
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-test
%global zf_name      zend-test
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Test
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.8.0
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-pcre
BuildRequires:  phpunit8 >= 8.5.14
BuildRequires:  phpunit9
BuildRequires: (php-autoloader(%{gh_owner}/laminas-console)              >= 2.6     with php-autoloader(%{gh_owner}/laminas-console)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.0     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15    with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.3     with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.5     with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.13.1  with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(symfony/css-selector)                       >= 4       with php-composer(symfony/css-selector)                       < 7)
BuildRequires: (php-composer(symfony/dom-crawler)                        >= 4       with php-composer(symfony/dom-crawler)                        < 7)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.3.0",
#        "laminas/laminas-i18n": "^2.6",
#        "laminas/laminas-log": "^2.7.1",
#        "laminas/laminas-modulemanager": "^2.7.1",
#        "laminas/laminas-mvc-console": "^1.1.8",
#        "laminas/laminas-mvc-plugin-flashmessenger": "^1.4.0",
#        "laminas/laminas-serializer": "^2.6.1",
#        "laminas/laminas-session": "^2.12.0",
#        "laminas/laminas-stdlib": "^3.6.0",
#        "laminas/laminas-validator": "^2.8",
#        "mikey179/vfsstream": "^1.6.8",
#        "psalm/plugin-phpunit": "^0.16.0",
#        "vimeo/psalm": "^4.7"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.6     with php-autoloader(%{gh_owner}/laminas-i18n)                < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-log)                  >= 2.7.1   with php-autoloader(%{gh_owner}/laminas-log)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-modulemanager)        >= 2.7.1   with php-autoloader(%{gh_owner}/laminas-modulemanager)       < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc-console)          >= 1.1.8   with php-autoloader(%{gh_owner}/laminas-mvc-console)         < 2)
BuildRequires:  php-autoloader(%{gh_owner}/laminas-mvc-plugin-flashmessenger) >= 1.4.0
BuildRequires: (php-autoloader(%{gh_owner}/laminas-serializer)           >= 2.6.1   with php-autoloader(%{gh_owner}/laminas-serializer)          < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.12    with php-autoloader(%{gh_owner}/laminas-session)             < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.8     with php-autoloader(%{gh_owner}/laminas-validator)           < 3)
BuildRequires: (php-composer(mikey179/vfsstream)                         >= 1.6.8   with php-composer(mikey179/vfsstream)                        < 2)
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0 || ~8.1.0",
#        "laminas/laminas-console": "^2.6",
#        "laminas/laminas-eventmanager": "^3.0",
#        "laminas/laminas-http": "^2.15.0",
#        "laminas/laminas-mvc": "^3.3",
#        "laminas/laminas-servicemanager": "^3.0.3",
#        "laminas/laminas-uri": "^2.5",
#        "laminas/laminas-view": "^2.13.1",
#        "phpunit/phpunit": "^8.5.14 || ^9.0",
#        "symfony/css-selector": "^5.4 || ^6.0",
#        "symfony/dom-crawler": "^5.4 || ^6.0"
Requires:       php(language) >= 7.3
# Maintained versions
Recommends:     phpunit9
Recommends:     phpunit8
Requires:      (php-autoloader(%{gh_owner}/laminas-console)              >= 2.6     with php-autoloader(%{gh_owner}/laminas-console)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.0     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15    with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.3     with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.5     with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.13.1  with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# ignore minimal version
Requires:      (php-composer(symfony/css-selector)                       >= 4       with php-composer(symfony/css-selector)                       < 7)
Requires:      (php-composer(symfony/dom-crawler)                        >= 4       with php-composer(symfony/dom-crawler)                        < 7)
# From composer.json, "suggest": {
#       "laminas/laminas-mvc-console": "^1.1.8, to test MVC <-> console integration"
Suggests:       php-autoloader(%{gh_owner}/laminas-mvc-console)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 3.3.0
Requires:       php-pcre

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.3.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{namespace}\Test component provides tools to facilitate integration
testing of your %{namespace} Framework applications. At this time, we offer
facilities to enable testing of your %{namespace} Framework MVC applications.

PHPUnit is the only library supported currently.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Console/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/Mvc/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Uri/autoload.php',
    '%{php_home}/%{namespace}/View/autoload.php',
    [
        '%{php_home}/Symfony6/Component/CssSelector/autoload.php',
        '%{php_home}/Symfony5/Component/CssSelector/autoload.php',
        '%{php_home}/Symfony4/Component/CssSelector/autoload.php',
    ], [
        '%{php_home}/Symfony6/Component/DomCrawler/autoload.php',
        '%{php_home}/Symfony5/Component/DomCrawler/autoload.php',
        '%{php_home}/Symfony4/Component/DomCrawler/autoload.php',
    ],
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Mvc/Console/autoload.php',
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
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/org/bovigo/vfs/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/Log/autoload.php',
    '%{php_home}/%{namespace}/ModuleManager/autoload.php',
    '%{php_home}/%{namespace}/Serializer/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/FlashMessenger/autoload.php',
    '%{php_home}/%{namespace}/Serializer/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Util\ModuleLoader") ? 0 : 1);
'

: upstream test suite
ret=0
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --verbose || ret=1
    fi
  done
fi
# TODO php81
if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php74 php80 php81; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --verbose || ret=1
    fi
  done
fi
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  8 2021 Remi Collet <remi@remirepo.net> - 3.8.0-1
- update to 3.8.0
- raise dependency on laminas-http 2.15
- raise dependency on laminas-mvc 3.3
- raise dependency on laminas-view 2.13.1
- drop dependency on laminas-stdlib

* Tue Dec  7 2021 Remi Collet <remi@remirepo.net> - 3.7.0-1
- update to 3.7.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Dec  3 2021 Remi Collet <remi@remirepo.net> - 3.6.0-1
- update to 3.6.0
- drop dependency on laminas-dom
- add dependency on symfony/css-selector
- add dependency on symfony/dom-crawler

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Remi Collet <remi@remirepo.net> - 3.5.1-1
- update to 3.5.1

* Thu Jun 10 2021 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0
- raise dependency on PHP 7.3
- raise dependency on laminas-dom 2.8
- raise dependency on laminas-http 2.13
- raise dependency on laminas-stdlib 3.3
- raise dependency on laminas-zendframework-bridge 1.1
- drop support for phpunit < 8

* Thu Mar 25 2021 Remi Collet <remi@remirepo.net> - 3.4.2-4
- drop phpunit6 build dependency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Remi Collet <remi@remirepo.net> - 3.4.2-1
- update to 3.4.2

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- allow phpunit9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 3.3.0-2
- only load phpunit-class-aliases if PHPUnit loaded

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 3.3.0-1
- switch to Laminas

* Wed Jun 12 2019 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0
- allow phpunit8

* Wed Jan  9 2019 Remi Collet <remi@remirepo.net> - 3.2.2-1
- update to 3.2.2
- raise dependency on zend-http >= 2.8.3

* Tue Dec 11 2018 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1
- use range dependencies

* Thu Apr 12 2018 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- allow phpunit7

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 3.1.1-2
- switch from zend-loader to fedora/autoloader

* Mon Oct 30 2017 Remi Collet <remi@remirepo.net> - 3.1.1-1
- Update to 3.1.1
- add autoloader for class aliases

* Sun Oct 29 2017 Remi Collet <remi@remirepo.net> - 3.1.0-3
- fix FTBFS from Koschei, add fix for recent PHPUnit from
  https://github.com/zendframework/zend-test/pull/55

* Tue May  2 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0
- run test suite against phpunit v5 and v6
- make dependency in phpunit optional (v5 or v6)

* Wed Sep  7 2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.1 for ZendFramework 3
- raise dependency on PHP 5.6
- raise dependency on zend-mvc >= 3.0

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-2
- allow sebastian/version 2.0

* Thu Mar  3 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1
- raise dependency on zend-mvc >= 2.7.1

* Wed Mar  2 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-console >= 2.6
- raise dependency on zend-dom >= 2.6
- raise dependency on zend-eventmanager >= 2.6.2
- raise dependency on zend-http >= 2.5.4
- raise dependency on zend-mvc >= 2.7
- raise dependency on zend-servicemanager >= 2.7.5
- raise dependency on zend-stdlib >= 2.7
- raise dependency on zend-view >= 2.6.3
- add dependency on sebastian/version

* Wed Dec  9 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on PHP >= 5.5
- allow PHPUnit 5

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-2
- ignore phpunit upstream recommended max version

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
