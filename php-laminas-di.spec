# remirepo/Fedora spec file for php-laminas-di
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# disabled as failed on recent version
%bcond_with          tests

%global bootstrap    0
%global gh_commit    239b22408a1f8eacda6fc2b838b5065c4cf1d88e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-di
%global zf_name      zend-di
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Di

Name:           php-%{gh_project}
Version:        2.6.1
Release:        10%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with tests}
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-reflection
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)     >= 3.12  with php-autoloader(%{gh_owner}/laminas-servicemanager)     < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-code)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-code)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "fabpot/php-cs-fixer": "1.7.*",
#        "phpunit/phpunit": "~4.0"
BuildRequires:  php-composer(phpunit/phpunit)                     >= 4.0
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.5 || ^7.0",
#        "container-interop/container-interop": "^1.1",
#        "laminas/laminas-code": "^2.6 || ^3.0",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^0.4.5 || ^1.0"
Requires:       php(language) >= 5.7
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)     >= 3.12  with php-autoloader(%{gh_owner}/laminas-servicemanager)     < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-code)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-code)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.6.1
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.6.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} is an example of an Inversion of Control (IoC) container.
IoC containers are widely used to create object instances that have all
dependencies resolved and injected. Dependency Injection containers are
one form of IoC – but not the only form.

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
    '%{php_home}/%{namespace}/Code/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
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
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

ret=0
for cmd in php php74 php80 php81; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{library}") ? 0 : 1);
'

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
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Remi Collet <remi@remirepo.net> - 2.6.1-8
- drop dependency on container-interop/container-interop
  replaced by servicemanager >= 3.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb  4 2021 Remi Collet <remi@remirepo.net> - 2.6.1-5
- disable test suite, fix FTBFS #1923569

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.6.1-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 2.6.1-1
- switch to Laminas

* Thu Feb 28 2019 Remi Collet <remi@remirepo.net> - 2.6.1-8
- use range dependencies

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.6.1-4
- switch from zend-loader to fedora/autoloader

* Tue Apr 26 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Wed Feb 24 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- add dependency on container-interop/container-interop
- raise dependency on zend-code >= 2.6
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
