# remirepo/Fedora spec file for php-laminas-mvc-i18n
#
# Copyright (c) 2016-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    6dc949c045d7a2c27652a3bb891d46ef5e1814e4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mvc-i18n
%global zf_name      zend-mvc-i18n
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mvc
%global subproj      I18n
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.4.0
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library}/%{subproj} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-intl
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.13.0 with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-router)               >= 3.5.0  with php-autoloader(%{gh_owner}/laminas-router)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.15.1 with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.19.0 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.2    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.3.0",
#        "phpspec/prophecy-phpunit": "^2.0",
#        "phpunit/phpunit": "^9.5",
#        "psalm/plugin-phpunit": "^0.17.0",
#        "vimeo/psalm": "^4.24.0"
BuildRequires: (php-composer(phpspec/prophecy-phpunit)                   >= 2.0    with php-composer(phpspec/prophecy-phpunit)                   < 3)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.4 || ~8.0.0 || ~8.1.0",
#        "container-interop/container-interop": "^1.1",
#        "laminas/laminas-i18n": "^2.13.0",
#        "laminas/laminas-router": "^3.5.0",
#        "laminas/laminas-servicemanager": "^3.15.1",
#        "laminas/laminas-stdlib": "^3.10.1",
#        "laminas/laminas-validator": "^2.19.0"
Requires:       php(language) >= 7.3
Requires:      (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.13   with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-router)               >= 3.5.0  with php-autoloader(%{gh_owner}/laminas-router)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.15.1 with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.19   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.2    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-cache": "To enable caching of translation strings"
Suggests:       php-autoloader(%{gh_owner}/laminas-cache)

# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.1.1
Requires:       php-intl
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.2.0
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} provides integration between:

* laminas-i18n
* laminas-mvc
* laminas-router

and replaces the i18n functionality found in the v2 releases of the latter
two components.

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
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/Router/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Cache/autoload.php',
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
    '%{php_home}/Prophecy/PhpUnit/autoload.php',
]);
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\Translator") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81 php82; do
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
%dir %{php_home}/Zend/%{library}
     %{php_home}/Zend/%{library}/%{subproj}
%dir %{php_home}/%{namespace}/%{library}
     %{php_home}/%{namespace}/%{library}/%{subproj}


%changelog
* Fri Jul 22 2022 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on PHP 7.4
- raise dependency on laminas-i18n 2.13.0
- raise dependency on laminas-router 3.5.0
- raise dependency on laminas-servicemanager 3.15.1
- raise dependency on laminas-stdlib 3.10.1
- raise dependency on laminas-validator 2.19.0

* Thu Jun 23 2022 Remi Collet <remi@remirepo.net> - 1.3.1-2
- drop dependency on container-interop/container-interop
  replaced by servicemanager >= 3.12

* Fri Feb 25 2022 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1 (no change)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  1 2021 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr  6 2021 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0 (no change)
- raise dependency on PHP 7.3
- raise dependency on laminas-i18n 2.11
- raise dependency on laminas-servicemanager 3.6
- raise dependency on laminas-stdlib 3.3
- raise dependency on laminas-validator 2.14
- raise dependency on laminas-zendframework-bridge 1.2
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 1.1.1-1
- switch to Laminas

* Fri Sep  6 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1 (no change)

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7
- raise dependency on zend-servicemanager 2.7.10

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 1.1.10-4
- switch from zend-loader to fedora/autoloader

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.1.10-1
- initial package

