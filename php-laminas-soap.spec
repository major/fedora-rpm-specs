# remirepo/Fedora spec file for php-laminas-soap
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    b1245a09b523485060407f73a0058fb871d2c656
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-soap
%global zf_name      zend-soap
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Soap
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.10.0
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-curl
BuildRequires:  php-dom
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-soap
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-server)               >= 2.11    with php-autoloader(%{gh_owner}/laminas-server)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.9.1   with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.2.1",
#        "laminas/laminas-config": "^3.7",
#        "laminas/laminas-http": "^2.15",
#        "phpspec/prophecy-phpunit": "^2.0.1",
#        "phpunit/phpunit": "^9.5.5"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 3.7     with php-autoloader(%{gh_owner}/laminas-config)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15    with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-composer(phpspec/prophecy-phpunit)                   >= 2.0.1   with php-composer(phpspec/prophecy-phpunit)                   < 3)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~7.4.0 || ~8.0.0 || ~8.1.0",
#        "ext-dom": "*",
#        "ext-soap": "*",
#        "laminas/laminas-server": "^2.11",
#        "laminas/laminas-stdlib": "^3.6",
#        "laminas/laminas-uri": "^2.9.1",
Requires:       php(language) >= 7.3
Requires:       php-dom
Requires:       php-soap
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-server)               >= 2.11    with php-autoloader(%{gh_owner}/laminas-server)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.9.1   with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "ext-curl": "Curl is required when .NET compatibility is required",
#        "laminas/laminas-http": "Laminas\\Http component"
Suggests:       php-autoloader(%{gh_owner}/laminas-http)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.8.0
Requires:       php-curl
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.8.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Soap is a component to manage the SOAP protocol in order
to design client or server PHP application.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Server/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Uri/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Http/autoload.php',
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
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/Prophecy/PhpUnit/autoload.php',
    dirname(__DIR__) .  '/test/TestAsset/commontypes.php',
    dirname(__DIR__) .  '/test/TestAsset/call_user_func.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Server") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80 php81; do
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependency on PHP 7.4
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on laminas-server 2.11
- raise dependency on laminas-stdlib 3.6
- raise dependency on laminas-uri 2.9.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on PHP 7.3
- raise dependency on laminas-server 2.9
- raise dependency on laminas-stdlib 3.2
- raise dependency on laminas-uri 2.8
- raise dependency on laminas-zendframework-bridge 1.1
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.8.0-1
- switch to Laminas

* Thu May  2 2019 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- use range dependencies

* Wed Jan 31 2018 Remi Collet <remi@remirepo.net> - 2.7.0-1
- Update to 2.7.0
- raise dependency on PHP >= 5.6
- switch to phpunit6

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.6.0-4
- switch from zend-loader to fedora/autoloader

* Fri Apr 22 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-server >= 2.6.1
- raise dependency on zend-stdlib >= 2.7
- raise dependency on zend-uri >= 2.5.2

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
