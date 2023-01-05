# remirepo/Fedora spec file for php-laminas-router
#
# Copyright (c) 2016-2023 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    3512c28cb4ffd64a62bc9e8b685a50a6547b0a11
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-router
%global zf_name      zend-router
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Router
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.11.1
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15   with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.14   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "laminas/laminas-i18n": "^2.19.0",
#        "phpunit/phpunit": "^9.5.26",
#        "psalm/plugin-phpunit": "^0.18.0",
#        "vimeo/psalm": "^5.0.0"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.19   with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-http": "^2.15",
#        "laminas/laminas-servicemanager": "^3.14.0",
#        "laminas/laminas-stdlib": "^3.10.1"
Requires:       php(language) >= 8.0
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15   with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.14   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "zendframework/zend-i18n": "^2.15.0, if defining translatable HTTP path segments"
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
# From composer, "conflict": {
#       "laminas/laminas-mvc": "<3.0.0"
Conflicts:      php-composer(%{gh_owner}/laminas-mvc)                <  3
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 3.3.1
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.3.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} provides flexible HTTP routing.

Routing currently works against the laminas-http request and responses,
and provides capabilities around:

* Literal path matches
* Path segment matches (at path boundaries, and optionally validated
  using regex)
* Regular expression path matches
* HTTP request scheme
* HTTP request method
* Hostname

Additionally, it supports combinations of different route types in tree
structures, allowing for fast, b-tree lookups.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/I18n/autoload.php',
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
exit (class_exists("\\Zend\\%{library}\\RouterFactory") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d memory_limit=1G ${2:-%{_bindir}/phpunit9} --verbose || ret=1
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
* Tue Jan  3 2023 Remi Collet <remi@remirepo.net> - 3.11.1-1
- update to 3.11.1

* Tue Dec  6 2022 Remi Collet <remi@remirepo.net> - 3.11.0-1
- update to 3.11.0

* Tue Oct 11 2022 Remi Collet <remi@remirepo.net> - 3.10.0-1
- update to 3.10.0
- raise dependency on PHP 8.0

* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 3.9.0-1
- update to 3.9.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Remi Collet <remi@remirepo.net> - 3.7.0-1
- update to 3.7.0

* Wed Jul 13 2022 Remi Collet <remi@remirepo.net> - 3.6.0-1
- update to 3.6.0
- raise dependency on PHP 7.4
- raise dependency on laminas-servicemanager 3.14
- raise dependency on laminas-stdlib 3.10.1

* Thu Jun 23 2022 Remi Collet <remi@remirepo.net> - 3.5.0-3
- drop dependency on container-interop/container-interop
  replaced by servicemanager >= 3.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on laminas-http 2.15
- raise dependency on laminas-servicemanager 3.7
- raise dependency on laminas-stdlib 3.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Remi Collet <remi@remirepo.net> - 3.4.5-1
- update to 3.4.5 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Remi Collet <remi@remirepo.net> - 3.4.4-1
- update to 3.4.4

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 3.4.3-1
- update to 3.4.3

* Tue Nov 24 2020 Remi Collet <remi@remirepo.net> - 3.4.2-1
- update to 3.4.2 (no change)

* Mon Nov 23 2020 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Wed Nov 18 2020 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- raise dependency on PHP 7.3
- raise dependency on zendframework/zend-stdlib 3.3
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 3.3.2-1
- update to 3.3.2 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 3.3.1-1
- switch to Laminas
- update to 3.3.1

* Wed Feb 27 2019 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0 (no change)
- raise dependency on zendframework/zend-stdlib 3.2.1

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- raise dependency on zendframework/zend-http 2.8.1

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 5.6
- raise dependency on container-interop/container-interop 1.2
- raise dependency on zendframework/zend-http 2.6
- raise dependency on zendframework/zend-servicemanager 2.7.8
- raise dependency on zendframework/zend-stdlib 2.7.7

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 3.0.2-5
- switch from zend-loader to fedora/autoloader

* Tue Oct 24 2017 Remi Collet <remi@fedoraproject.org> - 3.0.2-4
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-router/pull/39

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- initial package

