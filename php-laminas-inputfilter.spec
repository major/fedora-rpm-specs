# remirepo/Fedora spec file for php-laminas-inputfilter
#
# Copyright (c) 2015-2023 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    e97663a756370ba8105d07dc5f4fff53b650d151
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-inputfilter
%global zf_name      zend-inputfilter
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      InputFilter
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.23.0
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
BuildRequires:  php-json
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.13   with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.16.0 with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.15   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "ext-json": "*",
#        "laminas/laminas-coding-standard": "~2.5.0",
#        "phpunit/phpunit": "^9.5.27",
#        "psalm/plugin-phpunit": "^0.18.4",
#        "psr/http-message": "^1.0.1",
#        "vimeo/psalm": "^5.4",
#        "webmozart/assert": "^1.11"
BuildRequires: (php-composer(psr/http-message)                           >= 1.0.1 with php-composer(psr/http-message)                           <  2)
BuildRequires: (php-composer(webmozart/assert)                           >= 1.11  with php-composer(webmozart/assert)                           <  2)
BuildRequires:  phpunit9 >= 9.5.27
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-filter": "^2.13",
#        "laminas/laminas-servicemanager": "^3.16.0",
#        "laminas/laminas-stdlib": "^3.0",
#        "laminas/laminas-validator": "^2.15"
Requires:       php(language) >= 8.0
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.13   with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.16   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.15   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.10.1
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.10.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{namespace}\InputFilter component can be used to filter and validate generic
sets of input data. For instance, you could use it to filter $_GET or $_POST
values, CLI arguments, etc.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/Psr/Http/Message/autoload.php',
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
    '%{php_home}/Webmozart/Assert/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Input") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 \
      --filter '^((?!(testProvidesExpectedConfiguration|testFactoryWillCreateInputWithSuggestedFilters)).)*$' \
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
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}

%changelog
* Tue Jan 10 2023 Remi Collet <remi@remirepo.net> - 2.23.0-1
- update to 2.23.0

* Mon Nov  7 2022 Remi Collet <remi@remirepo.net> - 2.22.1-1
- update to 2.22.1

* Wed Oct 12 2022 Remi Collet <remi@remirepo.net> - 2.22.0-1
- update to 2.22.0
- raise dependency on PHP 8.0

* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 2.21.0-1
- update to 2.21.0
- raise dependency on zend-servicemanager 3.16

* Tue Jul 26 2022 Remi Collet <remi@remirepo.net> - 2.19.1-1
- update to 2.19.1

* Thu Jul 21 2022 Remi Collet <remi@remirepo.net> - 2.19.0-1
- update to 2.19.0

* Wed Jul 20 2022 Remi Collet <remi@remirepo.net> - 2.18.1-1
- update to 2.18.1

* Wed Jul 20 2022 Remi Collet <remi@remirepo.net> - 2.18.0-2
- fix FTBFS, using upstream patch for test suite

* Thu Jun 16 2022 Remi Collet <remi@remirepo.net> - 2.18.0-1
- update to 2.18.0
- raise dependency on zend-servicemanager 3.12

* Fri Jun 10 2022 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0

* Thu Jun  9 2022 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec  3 2021 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on PHP 7.4
- raise dependency on laminas-filter 2.13
- raise dependency on laminas-validator 2.15

* Mon Nov 29 2021 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 17 2021 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0 (no change)

* Tue Mar 16 2021 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0 (no change)
- raise dependency on PHP 7.3
- switch to phpunit9 with phpspec/prophecy-phpunit

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.10.1-2
- cleanup

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.10.1-1
- switch to Laminas

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1
- switch to phpunit7

* Thu Jan 31 2019 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Tue Jan  8 2019 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Tue Dec 18 2018 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on zend-filter 2.9.1
- raise dependency on zend-validator 2.11

* Fri Dec 14 2018 Remi Collet <remi@remirepo.net> - 2.8.3-2
- update to 2.8.3

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 2.8.2-2
- update to 2.8.2
- use range dependencies on F27+

* Tue Jan 23 2018 Remi Collet <remi@remirepo.net> - 2.8.1-2
- Update to 2.8.1
- add dependency on zend-servicemanager
- only use phpunit6

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.8.0-2
- switch from zend-loader to fedora/autoloader

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on zend-validator 2.10.1

* Wed Nov  8 2017 Remi Collet <remi@remirepo.net> - 2.7.5-1
- Update to 2.7.5

* Tue Oct 24 2017 Remi Collet <remi@remirepo.net> - 2.7.4-1
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-inputfilter/pull/150

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 2.7.4-1
- Update to 2.7.4
- raise dependency on PHP 5.6
- use phpunit6 on F26+
- open https://github.com/zendframework/zend-inputfilter/pull/141
  fix for PHPUnit 6

* Fri Sep  2 2016 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- update to 2.7.3

* Sun Jun 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Fri Apr  8 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-stdlib >= 2.7
- skip test suite with PHPUnit >= 5

* Fri Sep  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.5-1
- update to 2.5.5
- raise dependency on zend-validator ^2.5.3
- raise build dependency on PHPUnit ^4.5

* Wed Aug 12 2015 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- update to 2.5.4

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- initial package
