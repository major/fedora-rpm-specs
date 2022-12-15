# remirepo/Fedora spec file for php-laminas-json-server
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    5c07f08c91ea2d7f6b58b1aeb32aa4bb281b81cd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-json-server
%global zf_name      zend-json-server
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Json
%global subproj      Server
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.7.0
Release:        1%{?dist}
Summary:        %{namespace} Json-Server is a JSON-RPC server implementation

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15.1 with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.3    with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-server)               >= 2.11   with php-autoloader(%{gh_owner}/laminas-server)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "ext-json": "*",
#        "laminas/laminas-coding-standard": "^2.4.0",
#        "phpunit/phpunit": "^9.5.26",
#        "psalm/plugin-phpunit": "^0.18.0",
#        "vimeo/psalm": "^5.0.0"
BuildRequires:  php-json
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.26
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.4 || ~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-http": "^2.15.1",
#        "laminas/laminas-json": "^3.3.0",
#        "laminas/laminas-server": "^2.11.0",
Requires:       php(language) >= 7.4
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15.1 with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.3    with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-server)               >= 2.11   with php-autoloader(%{gh_owner}/laminas-server)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 3.2.0
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.2.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Provides a JSON-RPC server implementation.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Json/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/Server/autoload.php',
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
require_once __DIR__ . '/../test/TestAsset/FooFunc.php';
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\Response") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
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
* Tue Dec 13 2022 Remi Collet <remi@remirepo.net> - 3.7.0-1
- update to 3.7.0

* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 3.6.0-1
- update to 3.6.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb  4 2022 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- raise dependency on laminas-http 2.15.1
- raise dependency on laminas-json 3.3.0
- raise dependency on laminas-server 2.11.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr  8 2021 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0 (no change)
- raise dependency on PHP 7.3
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 3.2.2-1
- update to 3.2.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 3.2.0-1
- switch to Laminas

* Fri Oct 18 2019 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0 (no change)

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 5.6
- raise dependency on zend-http 2.7
- raise dependency on zend-server 2.7
- switch to phpunit6 or phpunit7
- use range dependencies on F27+

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 3.0.0-4
- switch from zend-loader to fedora/autoloader

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- initial package
