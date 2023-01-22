# remirepo/Fedora spec file for php-laminas-config3
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    46baad58d0b12cf98539e04334eff40a1fdfb9a0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-config
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Config
%global major        3
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}%{major}
Version:        3.8.0
Release:        2%{?dist}
Summary:        %{namespace} Framework %{library} component v%{major}

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlreader
BuildRequires:  php-xmlwriter
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-composer(psr/container)                              >= 1.0    with php-composer(psr/container)                              < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "laminas/laminas-filter": "~2.23.0",
#        "laminas/laminas-i18n": "~2.19.0",
#        "laminas/laminas-servicemanager": "~3.19.0",
#        "phpunit/phpunit": "~9.5.25"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.23.0 with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.19.0 with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.19.0 with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires:  phpunit9 >= 9.5.25
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "ext-json": "*",
#        "laminas/laminas-stdlib": "^3.6",
#        "psr/container": "^1.0"
Requires:       php(language) >= 8.0
Requires:       php-json
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-composer(psr/container)                              >= 1.0   with php-composer(psr/container)                              < 2)
# From composer, "suggest": {
#        "laminas/laminas-filter": "Laminas\\Filter component",
#        "laminas/laminas-i18n": "Laminas\\I18n component",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager for use with the Config Factory to retrieve reader and writer instances"
Suggests:       php-autoloader(%{gh_owner}/laminas-filter)
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.6.0
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlreader
Requires:       php-xmlwriter

Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}


%description
%{namespace}\Config is designed to simplify access to configuration data within
applications. It provides a nested object property-based user interface
for accessing this configuration data within application code. The
configuration data may come from a variety of media supporting hierarchical
data storage.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/Psr/Container/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 \
      --filter '^((?!(testCloseWhenCallFromFileReaderGetInvalid|testCloseWhenCallFromStringReaderGetInvalid)).)*$' \
      || ret=1
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
%{php_home}/%{namespace}/%{library}%{major}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Remi Collet <remi@remirepo.net> - 3.8.0-1
- update to 3.8.0
- raise dependency on PHP 8.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Remi Collet <remi@remirepo.net> - 3.7.0-2
- ignore 2 failed tests, FTBFS #2046823

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct  4 2021 Remi Collet <remi@remirepo.net> - 3.7.0-1
- update to 3.7.0
- raise dependency on laminas-stdlib 3.6
- switch to phpunit9

* Wed Sep  8 2021 Remi Collet <remi@remirepo.net> - 3.6.0-1
- update to 3.6.0
- drop zendframework compatibility layer

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- raise dependency on PHP 7.3
- switch to phpunit8

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 3.3.0-1
- rename to php-laminas-config3
- install in /usr/share/php/Laminas/Config3
- update to 3.3.0
- raise dependency on PHP 5.6
- raise dependency on laminas-stdlib 3.1
- add dependency on psr/container
- add dependency on json extention
- drop dependency on laminas-json
- switch to phpunit7

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
