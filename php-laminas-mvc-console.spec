# remirepo/Fedora spec file for php-laminas-mvc-console
#
# Copyright (c) 2016-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    90338c7b61a5fa8445c0a41925a4ae351459fa79
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mvc-console
%global zf_name      zend-mvc-console
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mvc
%global subproj      Console
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.3.0
Release:        6%{?dist}
Summary:        %{namespace} Framework %{library}/%{subproj} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-filter": "^2.6.1",
#        "phpspec/prophecy": "^1.12.0",
#        "phpspec/prophecy-phpunit": "^2.0",
#        "phpunit/phpunit": "^9.3"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-console)              >= 2.6    with php-autoloader(%{gh_owner}/laminas-console)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.3    with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-modulemanager)        >= 2.7.1  with php-autoloader(%{gh_owner}/laminas-modulemanager)        < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0.3  with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-router)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-router)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.12   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-text)                 >= 2.6    with php-autoloader(%{gh_owner}/laminas-text)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.11.3 with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.6.1  with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-composer(phpspec/prophecy)                           >= 1.12.0 with php-composer(phpspec/prophecy)                           < 2)
BuildRequires: (php-composer(phpspec/prophecy-phpunit)                   >= 2.0    with php-composer(phpspec/prophecy-phpunit)                   < 3)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.3
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.",
#        "container-interop/container-interop": "^1.1",
#        "laminas/laminas-console": "^2.6",
#        "laminas/laminas-eventmanager": "^3.3",
#        "laminas/laminas-modulemanager": "^2.7.1",
#        "laminas/laminas-mvc": "^3.0.3",
#        "laminas/laminas-router": "^3.0",
#        "laminas/laminas-servicemanager": "^3.3",
#        "laminas/laminas-stdlib": "^3.3",
#        "laminas/laminas-text": "^2.6",
#        "laminas/laminas-view": "^2.11.3",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 7.3
Requires:      (php-autoloader(%{gh_owner}/laminas-console)              >= 2.6    with php-autoloader(%{gh_owner}/laminas-console)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.3    with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-modulemanager)        >= 2.7.1  with php-autoloader(%{gh_owner}/laminas-modulemanager)        < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0.3  with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-router)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-router)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.12   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-text)                 >= 2.6    with php-autoloader(%{gh_owner}/laminas-text)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.11.3 with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-filter": "^2.6.1, to filter rendered results"
Suggests:       php-composer(%{gh_owner}/laminas-filter)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.2.0
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.3.0
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} provides integration between:

* laminas-console
* laminas-mvc
* laminas-router
* laminas-view

and replaces the console functionality found in the v2 releases of the latter
three components.

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
    '%{php_home}/%{namespace}/Console/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/ModuleManager/autoload.php',
    '%{php_home}/%{namespace}/Mvc/autoload.php',
    '%{php_home}/%{namespace}/Router/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Text/autoload.php',
    '%{php_home}/%{namespace}/View/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Filter/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(__DIR__))) . '/%{namespace}/%{library}/%{subproj}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/%{library}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}/%{subproj}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\%{subproj}\\', dirname(__DIR__) . '/test');
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Prophecy/autoload.php',
    '%{php_home}/Prophecy/PhpUnit/autoload.php',
]);
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\ConfigProvider") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
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
%{php_home}/Zend/%{library}/%{subproj}
%{php_home}/%{namespace}/%{library}/%{subproj}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Remi Collet <remi@remirepo.net> - 1.3.0-4
- drop dependency on container-interop/container-interop
  replaced by servicemanager >= 3.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0
- raise dependency on PHP 7.3
- raise dependency on laminas-eventmanager 3.3
- raise dependency on laminas-servicemanager 3.3
- raise dependency on laminas-stdlib 3.3
- raise dependency on laminas-view 2.11.3
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 1.2.0-1
- switch to Laminas

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 1.1.11-4
- switch from zend-loader to fedora/autoloader

* Thu Dec 15 2016 Remi Collet <remi@fedoraproject.org> - 1.1.11-1
- update to 1.1.11
- raise dependency on zendframework/zend-mvc 3.0.3

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.1.10-1
- initial package

