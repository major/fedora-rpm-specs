# remirepo/Fedora spec file for php-laminas-hydrator3
#
# Copyright (c) 2016-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# TODO: v2 pulled by php-ocramius-generated-hydrator
#          pulled by php-ocramius-proxy-manager

%global bootstrap    0
%global gh_commit    41aaccb9a0b8e25b1742f78427aa90504a6eb1cd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-hydrator
%global zf_name      zend-hydrator
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Hydrator
%global major        3
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}%{major}
Version:        3.2.1
Release:        4%{?dist}
Summary:        %{namespace} Framework %{library} component v%{major}

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-date
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-eventmanager": "^3.2.1",
#        "laminas/laminas-modulemanager": "^2.8",
#        "laminas/laminas-serializer": "^2.9",
#        "laminas/laminas-servicemanager": "^3.3.2",
#        "phpunit/phpunit": "~9.3.0",
#        "vimeo/psalm": "^3.16"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.2.1 with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-modulemanager)        >= 2.8   with php-autoloader(%{gh_owner}/laminas-modulemanager)        < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-serializer)           >= 2.9   with php-autoloader(%{gh_owner}/laminas-serializer)           < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3.2 with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.3
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0",
#        "laminas/laminas-stdlib": "^3.3",
Requires:       php(language) >= 7.3
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3    with php-autoloader(%{gh_owner}/laminas-stdlib)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-eventmanager": "^3.2, to support aggregate hydrator usage",
#        "laminas/laminas-serializer": "^2.9, to use the SerializableStrategy",
#        "laminas/laminas-servicemanager": "^3.3, to support hydrator plugin manager usage"
Suggests:       php-autoloader(%{gh_owner}/laminas-eventmanager)   >= 3.2
Suggests:       php-autoloader(%{gh_owner}/laminas-serializer)     >= 2.9
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager) >= 3.3
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.4.2
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl

Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Hydrator provides utilities for mapping arrays to objects,
and vice versa, including facilities for filtering which data
is mapped as well as providing mechanisms for mapping nested
structures.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/Serializer/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(__DIR__)) . '/%{namespace}/%{library}%{major}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}%{major}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}%{major}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}%{major}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}%{major}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ModuleManager/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}%{major}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Reflection") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} -d memory_limit=1G || ret=1
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
%{php_home}/Zend/%{library}%{major}
%{php_home}/%{namespace}/%{library}%{major}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Wed Feb 24 2021 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- raise dependency on PHP 7.3
- raise dependency on laminas-stdlib 3.3
- switch to phpunit9

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2
- rename to php-laminas-hydrator3
- install in /usr/share/php/Zend/Hydrator3
- raise dependency on PHP 7.2
- raise dependency on laminas-stdlib 3.2.1

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.4.2-1
- switch to Laminas

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 2.4.2-1
- update to 2.4.2

* Thu Nov 22 2018 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.3.1-2
- switch from zend-loader to fedora/autoloader

* Tue Oct  3 2017 Remi Collet <remi@remirepo.net> - 2.3.1-1
- Update to 2.3.1

* Thu Sep 21 2017 Remi Collet <remi@remirepo.net> - 2.3.0-1
- Update to 2.3.0

* Thu Sep 21 2017 Remi Collet <remi@remirepo.net> - 2.2.3-1
- Update to 2.2.3

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 2.2.2-1
- Update to 2.2.2
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- update to 2.2.1 for ZendFramework 3
- raise dependency on zend-stdlib >= 3.0

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- raise dependency on zend-stdlib >= 2.7

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- initial package
