# remirepo/fedora spec file for php-ircmaxell-random-lib
#
# Copyright (c) 2014-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    e9e0204f40e49fa4419946c677eccd3fa25b8cf4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     ircmaxell
%global gh_project   RandomLib
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-ircmaxell-random-lib
Version:        1.2.0
Release:        17%{?dist}
Summary:        A Library For Generating Secure Random Numbers

# See class headers
# LICENSE file will be in next version
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-hash
BuildRequires:  php-openssl
BuildRequires:  php-posix
BuildRequires:  php-spl
BuildRequires:  php-composer(ircmaxell/security-lib) >= 1.0
#        "mikey179/vfsStream": "^1.6",
#        "friendsofphp/php-cs-fixer": "^1.11",
#        "phpunit/phpunit": "^4.8|^5.0"
BuildRequires:  php-composer(mikey179/vfsStream) >= 1.6
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8
# For autoloader
BuildRequires:  php-mikey179-vfsstream >= 1.6.0
BuildRequires:  php-ircmaxell-security-lib >= 1.1.0-3
%endif

# From composer.json
#        "ircmaxell/security-lib": "^1.1",
#        "php": ">=5.3.2"
Requires:       php(language) >= 5.3.2
Requires:       php-composer(ircmaxell/security-lib) >= 1.1
# From phpcompatinfo report for version 1.2.0
Requires:       php-hash
Requires:       php-openssl
Requires:       php-posix
Requires:       php-spl
# For autoloader
Requires:       php-ircmaxell-security-lib >= 1.1.0-3

Provides:       php-composer(ircmaxell/random-lib) = %{version}


%description
A library for generating random numbers and strings of various strengths.

This library is useful in security contexts.

Autoloader: %{_datadir}/php/RandomLib/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

chmod -x lib/RandomLib/Generator.php


%build
: Generate library autoloader
%{_bindir}/phpab --output lib/RandomLib/autoload.php lib

cat << EOF | tee -a lib/RandomLib/autoload.php
// Dependency
require_once '%{_datadir}/php/SecurityLib/autoload.php';
EOF


%install
mkdir -p     %{buildroot}%{_datadir}/php
cp -pr lib/* %{buildroot}%{_datadir}/php


%check
%if %{with_tests}
: Generate test suite autoloader
%{_bindir}/phpab --output test/autoload.php test

mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once __DIR__ . '/../test/autoload.php';
require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';
require_once '%{buildroot}%{_datadir}/php/RandomLib/autoload.php';
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
%{_datadir}/php/RandomLib


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep  8 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-3
- add autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Wed Aug 13 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package