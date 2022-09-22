# remirepo/Fedora spec file for php-laminas-permissions-rbac
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    77011e721c1af3c4cede98df2f8c06944c0f0b67
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-permissions-rbac
%global zf_name      zend-permissions-rbac
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Permissions
%global subproj      Rbac
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.3.0
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
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.3.0",
#        "phpunit/phpunit": "^9.5.21",
#        "psalm/plugin-phpunit": "^0.17.0",
#        "vimeo/psalm": "^4.24.0"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.21
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.4 || ~8.0.0 || ~8.1.0"
Requires:       php(language) >= 7.4
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 3.0.2
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Provides role-based access control (RBAC) permissions management.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src

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
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\Role") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in "php %{phpunit}" php74 php80 php81 php82; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} \
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
%dir %{php_home}/Zend/%{library}
     %{php_home}/Zend/%{library}/%{subproj}
%dir %{php_home}/%{namespace}/%{library}
     %{php_home}/%{namespace}/%{library}/%{subproj}


%changelog
* Fri Jul 22 2022 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0
- raise dependency on PHP 7.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0 (no change)
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr  9 2021 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 3.0.2-2
- cleanup

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2
- switch to Laminas
- raise dependency on PHP 7.1

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 2.6.0-1
- Update to 2.6.0
- raise dependency on PHP 5.6
- switch to phpunit6

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.5.1-6
- switch from zend-loader to fedora/autoloader

* Tue Oct 31 2017 Remi Collet <remi@remirepo.net> - 2.5.1-5
- fix FTBFS from Koschei, add patch for tests with PHP 7.2
  https://github.com/zendframework/zend-permissions-rbac/pull/31

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
