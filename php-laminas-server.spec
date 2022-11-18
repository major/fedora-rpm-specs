# remirepo/Fedora spec file for php-php-laminas-server
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    c249f0638c8bdd67305509b7173bd535c21d109d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-server
%global zf_name      zend-server
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Server
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.12.0
Release:        1%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-reflection
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^9.5.5",
#        "psalm/plugin-phpunit": "^0.15.1",
#+        "vimeo/psalm": "^4.6.4"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-code)                 >= 3.5.1 with php-autoloader(%{gh_owner}/laminas-code)                 < 5)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.2.0 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-code": "^3.5.1 || ^4.0.0",
#        "laminas/laminas-stdlib": "^3.3.1",
#        "laminas/laminas-zendframework-bridge": "^1.2.0"
Requires:       php(language) >= 8.0
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-code)                 >= 3.5.1 with php-autoloader(%{gh_owner}/laminas-code)                 < 5)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.2.0 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.8.1
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.8.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{gh_project} family of classes provides functionality for the various
server classes, including %{namespace}\XmlRpc\Server and %{namespace}\Json\Server.
%{namespace}\Server\Server provides an interface that mimics PHP 5’s SoapServer
class; all server classes should implement this interface in order to provide a
standard server API.

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
    [
        '%{php_home}/%{namespace}/Code4/autoload.php',
        '%{php_home}/%{namespace}/Code/autoload.php',
    ],
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
require_once 'test/Reflection/TestAsset/functions.php';
require_once 'test/TestAsset/reflectionTestFunction.php';
EOF

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (interface_exists("\\Zend\\%{library}\\%{library}") ? 0 : 1);
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
* Wed Nov 16 2022 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0 (no change)
- raise dependency on PHP 8.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 28 2022 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 11 2021 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependency on laminas-code 3.5.1 and allow v4
- raise dependency on laminas-stdlib 3.3.1
- raise dependency on laminas-zendframework-bridge 1.2.0

* Fri Apr  9 2021 Remi Collet <remi@remirepo.net> - 2.9.2-1
- update to 2.9.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Tue Nov 24 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.8.1-2
- cleanup

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 2.8.1-1
- switch to Laminas

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.8.1-1
- update to 2.8.1
- drop patch merged upstream

* Wed Oct 16 2019 Remi Collet <remi@remirepo.net> - 2.8.0-6
- add patch for PHP 7.4 from
  https://github.com/zendframework/zend-server/pull/30

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Thu Nov 23 2017 Remi Collet <remi@remirepo.net> - 2.7.0-4
- switch from zend-loader to fedora/autoloader

* Tue Jun 21 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- raise dependency on PHP 5.6

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise minimal php version to 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
