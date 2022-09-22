# remirepo/Fedora spec file for php-laminas-servicemanager-di
#
# Copyright (c) 2016-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    abb2409f9dbf1b7c88f5dbe06bac726daa7c0325
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-servicemanager-di
%global zf_name      zend-servicemanager-di
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      ServiceManager
%global subproj      Di
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.2.1
Release:        9%{?dist}
Summary:        %{namespace} Framework %{library}-%{subproj} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.4"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-di)                   >= 2.6   with php-autoloader(%{gh_owner}/laminas-di)                   < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.12  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.4
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "container-interop/container-interop": "^1.1",
#        "laminas/laminas-di": "^2.6",
#        "laminas/laminas-servicemanager": "^3.0.3",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-di)                   >= 2.6   with php-autoloader(%{gh_owner}/laminas-di)                   < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.12  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From phpcompatinfo report for version 1.2.1
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.2.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Provides integration for laminas-di within laminas-servicemanager.

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
    '%{php_home}/%{namespace}/Di/autoload.php',
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
mkdir -p   %{buildroot}%{php_home}/%{namespace}/%{library}
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
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\DiFactory") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} --verbose || ret=1
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Remi Collet <remi@remirepo.net> - 1.2.1-8
- drop dependency on container-interop/container-interop
  replaced by servicemanager >= 3.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 1.2.1-2
- cleanup

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 1.2.1-1
- switch to Laminas

* Mon Oct 21 2019 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Wed Dec  6 2017 Remi Collet <remi@remirepo.net> - 1.1.1-2
- switch from zend-loader to fedora/autoloader

* Fri Sep 29 2017 Remi Collet <remi@remirepo.net> - 1.1.1-1
- Update to 1.1.1

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0 for ZendFramework 3

* Sun Jun 12 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- initial package

