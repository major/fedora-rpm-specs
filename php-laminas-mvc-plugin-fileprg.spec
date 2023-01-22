# remirepo/Fedora spec file for php-laminas-mvc-plugin-fileprg
#
# Copyright (c) 2016-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    2d6a64bf916b3f5f26a062b9c62d06af26ee483f
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mvc-plugin-fileprg
%global zf_name      zend-mvc-plugin-fileprg
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mvc
%global subproj      Plugin
%global subsubp      FilePrg
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.2.0
Release:        5%{?dist}
Summary:        %{namespace} Framework %{library}/%{subproj}/%{subsubp} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^9.3"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.6.1  with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-form)                 >= 2.7    with php-autoloader(%{gh_owner}/laminas-form)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-inputfilter)          >= 2.8.1  with php-autoloader(%{gh_owner}/laminas-inputfilter)          < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0    with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.8.5  with php-autoloader(%{gh_owner}/laminas-session)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.6    with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.3
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0",
#        "laminas/laminas-filter": "^2.6.1",
#        "laminas/laminas-form": "^2.7",
#        "laminas/laminas-inputfilter": "^2.8.1",
#        "laminas/laminas-mvc": "^3.0",
#        "laminas/laminas-session": "^2.8.5",
#        "laminas/laminas-stdlib": "^3.3",
#        "laminas/laminas-validator": "^2.6",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 7.3
Requires:      (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.6.1  with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-form)                 >= 2.7    with php-autoloader(%{gh_owner}/laminas-form)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-inputfilter)          >= 2.8.1  with php-autoloader(%{gh_owner}/laminas-inputfilter)          < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0    with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-session)              >= 2.8.5  with php-autoloader(%{gh_owner}/laminas-session)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.6    with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.1.0
Requires:       php-reflection

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.1.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Provides a Post-Redirect-Get controller plugin for laminas-mvc versions 3.0
and up, specifically for submissions that include file uploads.

If you want a generic PRG plugin without file upload support,
see laminas-mvc-plugin-prg.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/Form/autoload.php',
    '%{php_home}/%{namespace}/InputFilter/autoload.php',
    '%{php_home}/%{namespace}/Mvc/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(dirname(__DIR__)))) . '/%{namespace}/%{library}/%{subproj}/%{subsubp}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}
 
: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\%{subproj}\\%{subsubp}\\', dirname(__DIR__) . '/test');
EOF


: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\%{subsubp}\\Module") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
       --filter '^((?!(testCorrectInputDataMerging)).)*$' \
       --verbose || ret=1
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
%dir %{php_home}/Zend/%{library}/%{subproj}
     %{php_home}/Zend/%{library}/%{subproj}/%{subsubp}
%dir %{php_home}/%{namespace}/%{library}/%{subproj}
     %{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug  3 2021 Remi Collet <remi@remirepo.net> - 1.2.0-2
- ignore 1 test with erratic result, fix FTBFS #1987837

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 14 2021 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0
- raise dependency on PHP 7.3
- raise dependency on laminas-stdlib 3.3
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 1.1.0-1
- switch to Laminas

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7
- raise dependency on zend-inputfilter 2.8.1
- raise dependency on zend-session 2.8.5

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 1.0.0-4
- switch from zend-loader to fedora/autoloader

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package

