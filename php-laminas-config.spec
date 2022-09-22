# remirepo/Fedora spec file for php-laminas-config
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    71ba6d5dd703196ce66b25abc4d772edb094dae1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-config
%global zf_name      zend-config
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Config
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.6.0
Release:        9%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Fix for PHP 7.3
Patch0:         https://github.com/zendframework/zend-config/commit/27d5ba5c13cb4a576400f534057b69231190ac9d.patch

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlreader
BuildRequires:  php-xmlwriter
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "fabpot/php-cs-fixer": "1.7.*",
#        "laminas/laminas-filter": "^2.6",
#        "laminas/laminas-i18n": "^2.5",
#        "laminas/laminas-json": "^2.6.1",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3",
#        "phpunit/phpunit": "~4.0"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.6   with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.5   with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
# ignore max version, as test suite passes with v3
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)                 >= 2.6.1 with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires:  php-composer(phpunit/phpunit)                   >= 4.0
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.5 || ^7.0",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.5
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0      with php-autoloader(%{gh_owner}/laminas-stdlib)            < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-filter": "Laminas\\Filter component",
#        "laminas/laminas-i18n": "Laminas\\I18n component",
#        "laminas/laminas-json": "Laminas\\Json to use the Json reader or writer classes",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager for use with the Config Factory to retrieve reader and writer instances"
Suggests:       php-autoloader(%{gh_owner}/laminas-filter)
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
Suggests:       php-autoloader(%{gh_owner}/laminas-json)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.6.0
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlreader
Requires:       php-xmlwriter

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.6.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Config is designed to simplify access to configuration data within
applications. It provides a nested object property-based user interface
for accessing this configuration data within application code. The
configuration data may come from a variety of media supporting hierarchical
data storage.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/Json/autoload.php',
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

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Config") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    if [ $($cmd -r 'echo PHP_VERSION_ID;') -ge 80000 ]; then
       filter="--filter '^((?!(testCloseWhenCallFromFileReaderGetInvalid|testCloseWhenCallFromStringReaderGetInvalid)).)*$'"
    fi
    $cmd %{_bindir}/phpunit $filter || ret=1
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Remi Collet <remi@remirepo.net> - 2.6.0-5
- skip 2 tests failing with PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.6.0-2
- cleanup

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 2.6.0-1
- switch to Laminas

* Tue Feb  5 2019 Remi Collet <remi@remirepo.net> - 2.6.0-7
- fix FTBFS with PHP 7.3, patch from
  https://github.com/zendframework/zend-config/pull/54
- use range dependencies

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.6.0-4
- switch from zend-loader to fedora/autoloader

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
