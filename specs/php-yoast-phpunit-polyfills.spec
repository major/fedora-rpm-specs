# remirepo/fedora spec file for php-yoast-phpunit-polyfills
#
# SPDX-FileCopyrightText:  Copyright 2020-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please preserve changelog entries
#
# Github
%global gh_commit    134921bfca9b02d8f374c48381451da1d98402f9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Yoast
%global gh_project   PHPUnit-Polyfills
# Packagist
%global pk_vendor    yoast
%global pk_project   phpunit-polyfills
# Namespace
%global ns_vendor    Yoast
%global ns_project   PHPUnitPolyfills
# don't change major version used in package name
%global major        4
%bcond_without       tests
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}
Version:        4.0.0
Release:        2%{?dist}
Summary:        Set of polyfills for changed PHPUnit functionality, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-reflection
# From composer.json, "require-dev": {
#        "yoast/yoastcs": "^2.3.0"
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
BuildRequires:  phpunit12
BuildRequires:  phpunit11
%endif
# phpunit10 is not supported
BuildRequires:  phpunit9
BuildRequires:  phpunit8
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#               "php": ">=7.1",
#               "phpunit/phpunit": "^7.5 || ^8.0 || ^9.0 || ^11.0 || ^12.0"
Requires:       php(language) >= 7.1
# from phpcompatinfo report on version 0.2.0
Requires:       php-reflection

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Set of polyfills for changed PHPUnit functionality to allow for creating
PHPUnit cross-version compatible tests.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

# Fix for RPM layout
sed -e 's:src/::' phpunitpolyfills-autoload.php > src/autoload.php


%build
# Empty build section, most likely nothing required.


%install
mkdir -p        %{buildroot}/%{php_home}/%{ns_vendor}
cp -pr src      %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Yoast\\PHPUnitPolyfills\\Tests\\', dirname(__DIR__) . '/tests');
require_once '%{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF

: Run upstream test suite
ret=0
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php81 php82 php83; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --no-coverage || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php81 php82 php83 php84; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --no-coverage || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit11 ]; then
  for cmd in php  php82 php83 php84; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit11 --no-coverage || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit12 ]; then
  for cmd in php  php83 php84; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit11 --no-coverage || ret=1
    fi
  done
fi

exit $ret
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/%{ns_vendor}


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Feb 10 2025 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- move to /usr/share/php/Yoast/PHPUnitPolyfills4
- raise dependency on PHP 7.1
- add phpunit12

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0
- re-license spec file to CECILL-2.1

* Mon Sep  9 2024 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- move to /usr/share/php/Yoast/PHPUnitPolyfills3
- raise dependency on PHP 7.0
- drop phpunit10, add phpunit11

* Fri Aug 30 2024 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- move to /usr/share/php/Yoast/PHPUnitPolyfills2
- raise dependency on PHP 5.6
- drop phpunit7, add phpunit10

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr  9 2024 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Remi Collet <remi@remirepo.net> - 1.0.4-1
- update to 1.0.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Mon Oct  4 2021 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Tue Aug 10 2021 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Remi Collet <remi@remirepo.net> - 1.0.0-1
- update to 1.0.0

* Wed Mar 10 2021 Remi Collet <remi@remirepo.net> - 0.2.0-2
- reduce build matrix

* Thu Nov 26 2020 Remi Collet <remi@remirepo.net> - 0.2.0-1
- initial rpm
