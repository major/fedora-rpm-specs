# remirepo/Fedora spec file for php-php-laminas-serializer
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    c4ceeb080f8d080006616072d2926949b3e5b9ea
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-serializer
%global zf_name      zend-serializer
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Serializer
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.14.0
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
BuildRequires:  php-dom
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-simplexml
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "laminas/laminas-math": "^3.6.0",
#        "laminas/laminas-servicemanager": "^3.19.0",
#        "phpunit/phpunit": "^9.5.25"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)               >= 3.1    with php-autoloader(%{gh_owner}/laminas-json)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.2    with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-math)               >= 3.3    with php-autoloader(%{gh_owner}/laminas-math)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)     >= 3.19   with php-autoloader(%{gh_owner}/laminas-servicemanager)     < 4)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.25
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-json": "^3.1",
#        "laminas/laminas-stdlib": "^3.2"
Requires:       php(language) >= 8.0
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-json)               >= 3.1    with php-autoloader(%{gh_owner}/laminas-json)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.2    with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-math": "(^3.3) To support Python Pickle serialization",
#        "laminas/laminas-servicemanager": "(^3.6) To support plugin manager support"
Suggests:       php-autoloader(%{gh_owner}/laminas-math)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-pecl(igbinary)
Suggests:       php-pecl(msgpack)
%endif
# From phpcompatinfo report for version 2.9.1
Requires:       php-dom
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-simplexml
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{gh_project} component provides an adapter based interface
to simply generate storable representation of PHP types by different
facilities, and recover.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Json/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Math/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
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
* Mon Oct 17 2022 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0
- raise dependency on PHP 8.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 12 2022 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency on PHP 7.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec  7 2021 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0 (no change)
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Mon Oct 25 2021 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1
- raise dependency on PHP 7.3
- raise dependency on laminas-json 3.1
- raise dependency on laminas-stdlib 3.2
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.9.1-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 2.9.1-1
- switch to Laminas

* Mon Oct 21 2019 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1 (no change)
- switch to phpunit7

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 2.9.0-2
- update to 2.9.0
- use range dependencies on F27+
- switch to phpunit6

* Thu Nov 23 2017 Remi Collet <remi@remirepo.net> - 2.8.1-2
- switch from zend-loader to fedora/autoloader

* Tue Nov 21 2017 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Thu Nov  9 2017 Remi Collet <remi@fedoraproject.org> - 2.8.0-4
- fix FTBFS from Koschei, add patch for bigendian from
  https://github.com/zendframework/zend-serializer/pull/31

* Tue Jun 21 2016 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- update to 2.8.0
- raise dependency on PHP 5.6

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2
- dependency to zend-math is now optional

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Thu Feb  4 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Wed Feb  3 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib ~2.7
- raise dependency on zend-math ~2.6
- raise dependency on zend-servicemanager ~2.7.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
