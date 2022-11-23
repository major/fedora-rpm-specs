# remirepo/Fedora spec file for php-laminas-paginator
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    7070769de9b3d94270154c4bf24d4884e65c29f3
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-paginator
%global zf_name      zend-paginator
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Paginator
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.15.1
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
BuildRequires:  php-json
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0.4   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-cache": "^3.6.0",
#        "laminas/laminas-cache-storage-adapter-memory": "^2.1.0",
#        "laminas/laminas-coding-standard": "^2.4.0",
#        "laminas/laminas-config": "^3.8.0",
#        "laminas/laminas-filter": "^2.23.0",
#        "laminas/laminas-servicemanager": "^3.19.0",
#        "laminas/laminas-view": "^2.24.0",
#        "phpunit/phpunit": "^9.5.25",
#        "psalm/plugin-phpunit": "^0.17.0",
#        "vimeo/psalm": "^4.29.0"
# ignore cache min version for now
BuildRequires: (php-autoloader(%{gh_owner}/laminas-cache)                >= 2.9.0   with php-autoloader(%{gh_owner}/laminas-cache)                <  3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 3.8     with php-autoloader(%{gh_owner}/laminas-config)               <  4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.23    with php-autoloader(%{gh_owner}/laminas-filter)               <  3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.19    with php-autoloader(%{gh_owner}/laminas-servicemanager)       <  4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.24    with php-autoloader(%{gh_owner}/laminas-view)                 <  3)
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "ext-json": "*",
#        "laminas/laminas-stdlib": "^3.10.1",
#        "laminas/laminas-zendframework-bridge": "^1.0.4"
Requires:       php(language) >= 8.0
Requires:       php-json
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0.4   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-cache": "Laminas\\Cache component to support cache features",
#        "laminas/laminas-filter": "Laminas\\Filter component",
#        "laminas/laminas-paginator-adapter-laminasdb": "Provides pagination adapters for Select statements and TableGateway instances",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component",
#        "laminas/laminas-view": "Laminas\\View component"
Suggests:       php-autoloader(%{gh_owner}/laminas-cache)
Suggests:       php-autoloader(%{gh_owner}/laminas-filter)
Suggests:       php-autoloader(%{gh_owner}/laminas-paginator-adapter-laminasdb)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-view)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.8.2
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.8.3
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Paginator is a flexible component for paginating
collections of data and presenting that data to users.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    [
        '%{php_home}/%{namespace}/Cache3/autoload.php',
        '%{php_home}/%{namespace}/Cache/autoload.php',
    ],
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/View/autoload.php',
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
    '%{php_home}/%{namespace}/Config3/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Factory") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --bootstrap vendor/autoload.php --verbose || ret=1
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
* Mon Nov 21 2022 Remi Collet <remi@remirepo.net> - 2.15.1-1
- update to 2.15.1

* Mon Oct 24 2022 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0
- raise dependency on PHP 8.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency to laminas-stdlib 3.10.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Remi Collet <remi@remirepo.net> - 2.12.2-1
- update to 2.12.2

* Mon Dec 20 2021 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1
- raise dependency on PHP 7.4

* Fri Oct 15 2021 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency to laminas-stdlib 3.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 26 2021 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency to PHP 7.3
- raise dependency to laminas-stdlib 3.2.1
- raise dependency to laminas-zendframework-bridge 1.0.4
- switch to phpunit8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Remi Collet <remi@remirepo.net> - 2.8.3-1
- update to 2.8.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 2.8.2-1
- switch to Laminas

* Wed Aug 21 2019 Remi Collet <remi@remirepo.net> - 2.8.2-2
- update to 2.8.2
- use range dependencies

* Wed Jan 31 2018 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.8.0-2
- switch from zend-loader to fedora/autoloader

* Thu Nov  2 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Tue Apr 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Wed Feb 24 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
