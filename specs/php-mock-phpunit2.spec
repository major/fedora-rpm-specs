# remirepo/fedora spec file for php-mock-phpunit2
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    e1f7e795990b00937376e345883ea68ca3bda7e0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2024-02-11
%global gh_owner     php-mock
%global gh_project   php-mock-phpunit
%global with_tests   0%{!?_without_tests:1}
%global major        2

Name:           php-mock-phpunit%{major}
Version:        2.10.0
Release:        3%{?dist}
Summary:        Mock built-in PHP functions with PHPUnit.

License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7
%if %{with_tests}
BuildRequires: (php-composer(php-mock/php-mock-integration) >= 2.3    with php-composer(php-mock/php-mock-integration) < 3)
BuildRequires: (php-composer(php-mock/php-mock)             >= 2.2    with php-composer(php-mock/php-mock)             < 3)
# From composer.json "require-dev": {
#        "mockery/mockery": "^1.3.6"
BuildRequires: (php-composer(mockery/mockery)               >= 1.3.6  with php-composer(mockery/mockery)               < 2)
BuildRequires:  phpunit8
BuildRequires:  phpunit9
BuildRequires:  phpunit10 >= 10.0.17
# TODO phpunit11 but requires php 8.2
# For autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# from composer.json, "require": {
#        "php": ">=7",
#        "phpunit/phpunit": "^6 || ^7 || ^8 || ^9 || ^10.0.17 || ^11",
#        "php-mock/php-mock-integration": "^2.2.1"
#    "conflict": {
#        "phpunit/phpunit-mock-objects": "3.2.0"
Requires:       php(language) >= 7
Recommends:    (phpunit8 or phpunit9 or phpunit10)
Requires:      (php-composer(php-mock/php-mock-integration) >= 2.3   with php-composer(php-mock/php-mock-integration) < 3)
Requires:      (php-composer(php-mock/php-mock)             >= 2.2   with php-composer(php-mock/php-mock)             < 3)
# From phpcompatinfo report from version 2.1.0
# only Core

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Mock built-in PHP functions (e.g. time()) with PHPUnit.
This package relies on PHP's namespace fallback policy.
No further extension is needed.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Create autoloader
cat << 'AUTOLOAD' | tee rpm.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpmock\\phpunit\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    __DIR__ . '/compatibility.php',
    '%{_datadir}/php/phpmock2/autoload.php',
));
AUTOLOAD


%build
# Nothing


%install
mkdir -p             %{buildroot}%{_datadir}/php/
mkdir -p             %{buildroot}%{_datadir}/php/phpmock%{major}
cp -pr classes       %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit
cp -pr compatibility %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/compatibility
cp -p  autoload.php  %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/compatibility.php
cp -p  rpm.php       %{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/phpmock%{major}/phpunit/autoload.php';
require_once '%{_datadir}/php/phpmock%{major}/autoload.php';
require_once '%{_datadir}/php/Mockery1/autoload.php';
EOF

ret=0

if [ -x %{_bindir}/phpunit7 ]; then
: Run upstream test suite with phpunit7
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 --verbose || ret=1
  fi
done
fi

if [ -x %{_bindir}/phpunit8 ]; then
: Run upstream test suite with phpunit8
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
fi

if [ -x %{_bindir}/phpunit9 ]; then
: Run upstream test suite with phpunit9
for cmd in php php80 php81 php82 php83; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
fi

if [ -x %{_bindir}/phpunit10 ]; then
: Run upstream test suite with phpunit10
for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit10 \
       --filter '^((?!(testPreserveArgumentDefaultValue)).)*$' \
       || ret=1
  fi
done
fi

if [ -x %{_bindir}/phpunit11 ]; then
: Run upstream test suite with phpunit11
for cmd in php php82 php83; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit11 \
       --filter '^((?!(testPreserveArgumentDefaultValue)).)*$' \
       || ret=1
  fi
done
fi
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/phpmock%{major}/phpunit


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0 (no change)
- raise dependency on php-mock-integration2 2.3
- allow phpunit11

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec  4 2023 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0

* Mon Oct 30 2023 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2 (no change)

* Tue Mar 21 2023 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Tue Mar  7 2023 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0
- raise dependency on php-mock-integration2 2.2.1
- allow phpunit10
- drop build dependency on phpspec/prophecy
- add build dependency on mockery/mockery

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 12 2022 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1
- add dependency on phpspec/prophecy

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 2.6.0-4
- drop dependency on phpunit6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0
- raise dependency on php-mock2 2.2
- raise dependency on php-mock-integration2 2.1
- allow phpunit9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  7 2019 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0

* Mon Apr  8 2019 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0
- raise dependency on php-mock2 2.1.1

* Thu Mar  7 2019 Remi Collet <remi@remirepo.net> - 2.2.0-2
- update to 2.2.0
- add dependency on php-mock2 for phpunit8 compatibility
- allow phpunit8
- use php-mock2 2.1 single autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  8 2018 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr  9 2018 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Fri Mar 23 2018 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- add autoloader
- allow phpunit6 and phpunit7

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- rename to php-mock-phpunit2
- Update to 2.0.1
- raise dependency on PHP 7
- raise dependency on php-mock-integration 2
- switch top phpunit6

* Thu May 11 2017 Remi Collet <remi@remirepo.net> - 1.1.2-3
- switch to fedora/autoloader

* Thu Jun 16 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- update to 1.1.2 (no change)

* Mon Feb 22 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- Fix: license is WTFPL

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- initial package
