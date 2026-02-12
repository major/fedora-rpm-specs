# remirepo/fedora spec file for php-phpspec-prophecy-phpunit
#
# SPDX-FileCopyrightText:  Copyright 2020-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    89f91b01d0640b7820e427e02a007bc6489d8a26
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpspec
%global gh_project   prophecy-phpunit

Name:           php-%{gh_owner}-%{gh_project}
Version:        2.5.0
Release:        1%{?dist}
Summary:        Integrating the Prophecy mocking library in PHPUnit test cases

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
%if %{with tests}
BuildRequires: (php-composer(phpspec/prophecy) >= 1.18  with php-composer(phpspec/prophecy) < 2)
BuildRequires:  phpunit13 >= 13.0
BuildRequires:  phpunit12 >= 12.0
BuildRequires:  phpunit11 >= 11.0
BuildRequires:  phpunit10 >= 10.1
BuildRequires:  phpunit9 >= 9.1
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# from composer.json, "requires": {
#        "php": "^7.3 || ^8",
#        "phpspec/prophecy": "^1.18",
#        "phpunit/phpunit":"^9.1 || ^10.1 || ^11.0 || ^12.0 || ^13.0"
Requires:       php(language) >= 7.3
Requires:      (php-composer(phpspec/prophecy) >= 1.18  with php-composer(phpspec/prophecy) < 2)
Requires:      (phpunit9 >= 9.1 or phpunit10 >= 10.1 or phpunit11 >= 11.0 or phpunit12 >= 12.0 or phpunit13 >= 13.0)
# From phpcompatinfo report for version 2.0.1
#none
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Prophecy PhpUnit integrates the Prophecy mocking library with PHPUnit
to provide an easier mocking in your testsuite.

Autoloader: %{_datadir}/php/Prophecy/PhpUnit/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Prophecy/autoload.php',
]);
EOF


%install
mkdir -p     %{buildroot}%{_datadir}/php/Prophecy/PhpUnit
cp -pr src/* %{buildroot}%{_datadir}/php/Prophecy/PhpUnit/


%check
%if %{with tests}
: Dev autoloader
mkdir vendor
phpab --output vendor/autoload.php.in fixtures tests

cat << 'EOF' | tee -a vendor/autoload.php.in
require_once '%{buildroot}%{_datadir}/php/Prophecy/PhpUnit/autoload.php';
require_once '%{_datadir}/php/@PHPUNIT@/autoload.php';
EOF

: check autoloader
php %{buildroot}%{_datadir}/php/Prophecy/PhpUnit/autoload.php

: Fix expecteed path
sed -e 's:src/::' -i tests/MockFailure.phpt

: upstream test suite
ret=0
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
	sed -e 's/@PHPUNIT@/PHPUnit9/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit9 --no-coverage|| ret=1

	sed -e 's/@PHPUNIT@/PHPUnit10/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit10 --no-coverage|| ret=1

	sed -e 's/@PHPUNIT@/PHPUnit11/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit11 --no-coverage|| ret=1
  fi
done
for cmd in php php83 php84 php85; do
  if which %{_bindir}/phpunit12 && which $cmd; then
	sed -e 's/@PHPUNIT@/PHPUnit12/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit12 --no-coverage|| ret=1
  fi
done
for cmd in php php84 php85; do
  if which %{_bindir}/phpunit13 && which $cmd; then
	sed -e 's/@PHPUNIT@/PHPUnit13/' vendor/autoload.php.in > vendor/autoload.php
    $cmd -d auto_prepend_file=vendor/autoload.php \
      %{_bindir}/phpunit13 --no-coverage|| ret=1
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
%{_datadir}/php/Prophecy/PhpUnit


%changelog
* Tue Feb 10 2026 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0
- allow phpunit13

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 26 2025 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0 (no change)
- allow phpunit12
- re-license spec file to CECILL-2.1

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 21 2024 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar  1 2024 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- allow phpunit11

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- raise dependency on phpspec/prophecy 1.18
- allow phpunit9 or phpunit10

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- initial package
