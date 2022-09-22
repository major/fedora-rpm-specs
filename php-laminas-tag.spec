# remirepo/Fedora spec file for php-laminas-tag
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    570b206c9a5126a97fdd5f0bf9de6cec08402658
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-tag
%global zf_name      zend-tag
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Tag
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.9.0
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.3",
#        "laminas/laminas-servicemanager": "^3.8",
#        "phpunit/phpunit": "^9.5.5"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.9   with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.7   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.4 || ~8.0.0 || ~8.1.0",
#        "laminas/laminas-escaper": "^2.9",
#        "laminas/laminas-stdlib": "^3.6"
Requires:       php(language) >= 7.4
Requires:      (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.9   with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component"
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.7.1
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.7.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Tag is a component suite which provides a facility to work with
taggable Items. As its base, it provides two classes to work with Tags,
%{namespace}\Tag\Item and %{namespace}\Tag\ItemList. Additionally, it comes with the
interface %{namespace}\Tag\TaggableInterface, which allows you to use any of
your models as a taggable item in conjunction with %{namespace}\Tag.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}
mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Escaper/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
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

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Item") ? 0 : 1);
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec  3 2021 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on PHP 7.4
- raise dependency on laminas-escaper 2.9
- raise dependency on laminas-stdlib 3.6

* Tue Aug  3 2021 Remi Collet <remi@remirepo.net> - 2.8.0-2
- add fix for laminas-escaper 2.8.0
  https://github.com/laminas/laminas-tag/pull/6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0 (no change)
- raise dependency on PHP 7.3
- raise dependency on laminas-escaper 2.7
- raise dependency on laminas-stdlib 3.2
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.7.2-2
- cleanup

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 2.7.2-1
- switch to Laminas

* Thu May  2 2019 Remi Collet <remi@remirepo.net> - 2.7.1-2
- update to 2.7.1

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 2.7.0-2
- update to 2.7.0
- raise dependency on PHP 5.6
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Wed Dec  6 2017 Remi Collet <remi@remirepo.net> - 2.6.1-4
- switch from zend-loader to fedora/autoloader

* Thu Feb  4 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1
- raise dependency on PHP >= 5.5
- raise dependency on zend_stdlib ~2.7
- raise build dependency on zend-servicemanager ~2.7.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
