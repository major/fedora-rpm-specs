# remirepo/Fedora spec file for php-laminas-progressbar
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    cb57c459f3c2cef516e6d36218b70f780289d383
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-progressbar
%global zf_name      zend-progressbar
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      ProgressBar
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.10.1
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-date
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-json": "^3.0.0",
#        "laminas/laminas-session": "^2.8.5",
#        "phpunit/phpunit": "^9.3"
# ignore max version
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)                  >= 3.0.0   with php-autoloader(%{gh_owner}/laminas-json)                  < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)               >= 2.8.5   with php-autoloader(%{gh_owner}/laminas-session)               < 3)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.3
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0 || ~8.1.0",
#        "laminas/laminas-stdlib": "^3.2.1"
Requires:       php(language) >= 7.3
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-json": "Laminas\\Json component",
#        "laminas/laminas-session": "To support progressbar persistent"
Suggests:       php-autoloader(%{gh_owner}/laminas-json)
Suggests:       php-autoloader(%{gh_owner}/laminas-session)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.7.0
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl
# apc and uploadprogress are optional

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.7.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\ProgressBar is a component to create and update progress bars in
different environments. It consists of a single backend, which outputs
the progress through one of the multiple adapters. On every update, it
takes an absolute value and optionally a status message, and then calls
the adapter with some precalculated values like percentage and estimated
time left.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Json/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
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
exit (class_exists("\\Zend\\%{library}\\ProgressBar") ? 0 : 1);
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
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Mon Aug  1 2022 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb  7 2022 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec  7 2021 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.7.0-1
- switch to Laminas

* Fri Oct 18 2019 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0 (no change)
- raise dependency on zend-stdlib >= 3.2.1

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 2.6.0-2
- update to 2.6.0
- raise dependency on PHP 5.6
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.5.2-4
- switch from zend-loader to fedora/autoloader

* Wed Mar  2 2016 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
