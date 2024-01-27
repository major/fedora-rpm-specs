# remirepo/fedora spec file for php-ircmaxell-security-lib
#
# Copyright (c) 2014-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    f3db6de12c20c9bcd1aa3db4353a1bbe0e44e1b5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     ircmaxell
%global gh_project   SecurityLib
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-ircmaxell-security-lib
Version:        1.1.0
Release:        21%{?dist}
Summary:        A Base Security Library

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

# Upstream patches
Patch0:         %{name}-upstream.patch

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-bcmath
BuildRequires:  php-gmp
BuildRequires:  php-hash
BuildRequires:  %{_bindir}/phpab
BuildRequires:  %{_bindir}/phpunit
#      "mikey179/vfsStream": "1.1.*", ignore max version on purpose
# 1.6.0 is first version with autoloader
BuildRequires:  php-composer(mikey179/vfsStream) >= 1.6
%endif

# From composer.json
#      "php": ">=5.3.2"
Requires:       php(language) >= 5.3.2
# From phpcompatinfo report for version 1.0.0
Requires:       php-hash
Requires:       php-reflection
Requires:       php-spl
%if 0%{?fedora} > 21
Suggests:       php-bcmath
Suggests:       php-gmp
%endif

Provides:       php-composer(ircmaxell/security-lib) = %{version}


%description
This is a base set of libraries used in other projects.
This isn't useful on its own...

Optional dependency: php-gmp or php-bcmath

Autoloader: %{_datadir}/php/SecurityLib/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1

rm lib/SecurityLib/composer.json


%build
: Generate library autoloader
%{_bindir}/phpab \
    --output lib/SecurityLib/autoload.php \
    lib/SecurityLib


%install
mkdir -p     %{buildroot}%{_datadir}/php
cp -pr lib/* %{buildroot}%{_datadir}/php


%check
%if %{with_tests}
: Generate test suite autoloader
%{_bindir}/phpab \
    --output test/autoload.php \
    test

mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once __DIR__ . '/../test/autoload.php';
require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';
require_once '%{buildroot}%{_datadir}/php/SecurityLib/autoload.php';
EOF

: Run test suite
%{_bindir}/phpunit --verbose
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/SecurityLib


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-4
- add upstream patches to fix test suite
- add autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- add LICENSE file

* Wed Aug 13 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- drop composer.json from library path

* Wed Aug 13 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package