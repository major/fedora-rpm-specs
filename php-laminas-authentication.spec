# remirepo/Fedora spec file for php-laminas-authentication
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    12bfb36b8b20052a5fee2ae69b0f12064ce16fa9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-authentication
%global zf_name      zend-authentication
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Authentication
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.13.0
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
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.12    with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "laminas/laminas-crypt": "^2.6.0 || ^3.9.0",
#        "laminas/laminas-db": "^2.15.0",
#        "laminas/laminas-http": "^2.17.0",
#        "laminas/laminas-ldap": "^2.15.0",
#        "laminas/laminas-session": "^2.13.0",
#        "laminas/laminas-uri": "^2.10.0",
#        "laminas/laminas-validator": "^2.26.0",
#        "phpunit/phpunit": "^9.5.25",
#        "psalm/plugin-phpunit": "^0.17.0",
#        "squizlabs/php_codesniffer": "^3.6.0",
#        "vimeo/psalm": "^4.29.0"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-crypt)          >= 3.9           with php-autoloader(%{gh_owner}/laminas-crypt)                < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-db)             >= 2.15          with php-autoloader(%{gh_owner}/laminas-db)                   < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)           >= 2.17          with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-ldap)           >= 2.15          with php-autoloader(%{gh_owner}/laminas-ldap)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)        >= 2.13          with php-autoloader(%{gh_owner}/laminas-session)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)            >= 2.10          with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)      >= 2.26          with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.25
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-stdlib": "^3.6.0"
Requires:       php(language) >= 8.0
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6     with php-autoloader(%{gh_owner}/laminas-stdlib)              < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.12    with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
# From composer, "suggest": {
#        "laminas/laminas-crypt": "Laminas\\Crypt component",
#        "laminas/laminas-db": "Laminas\\Db component",
#        "laminas/laminas-http": "Laminas\\Http component",
#        "laminas/laminas-ldap": "Laminas\\Ldap component",
#        "laminas/laminas-session": "Laminas\\Session component",
#        "laminas/laminas-uri": "Laminas\\Uri component",
#        "laminas/laminas-validator": "Laminas\\Validator component"
Suggests:       php-autoloader(%{gh_owner}/laminas-crypt)
Suggests:       php-autoloader(%{gh_owner}/laminas-db)
Suggests:       php-autoloader(%{gh_owner}/laminas-http)
Suggests:       php-autoloader(%{gh_owner}/laminas-ldap)
Suggests:       php-autoloader(%{gh_owner}/laminas-session)
Suggests:       php-autoloader(%{gh_owner}/laminas-uri)
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.7.0
Requires:       php-ctype
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.7.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{namespace}\\Authentication component provides an API for authentication and
includes concrete authentication adapters for common use case scenarios.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Db/autoload.php',
    '%{php_home}/%{namespace}/Crypt/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/Ldap/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
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
exit (class_exists("\\Zend\\%{library}\\Result") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
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
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency on PHP 8.0

* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0
- raise dependency on PHP 7.4
- raise dependency on laminas-stdlib 3.13.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Remi Collet <remi@remirepo.net> - 2.11.0-2
- add dependency on laminas-servicemanager to workaround
  issue with old psr/container

* Thu Jun 23 2022 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0

* Thu Mar 10 2022 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Wed Mar  9 2022 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec  7 2021 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0 (no change)
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Wed Nov 10 2021 Remi Collet <remi@remirepo.net> - 2.8.0-3
- ignore tests for deprecation

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.8.0-1
- switch to Laminas

* Wed May 15 2019 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0
- raise dependency on zend-stdlib 3.2.1
- use range dependencies

* Mon Apr 16 2018 Remi Collet <remi@remirepo.net> - 2.6.0-2
- update to 2.6.0
- raise dependency on PHP 5.6
- raise dependency on zend-stdlib 3.1
- use phpunit7

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.5.3-4
- switch from zend-loader to fedora/autoloader

* Sun Feb 28 2016 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3
- raise dependency on zend-stdlib ~2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package
