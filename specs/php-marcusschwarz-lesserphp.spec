%global composer_vendor   marcusschwarz
%global composer_project  lesserphp

%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgdir %{phpdir}/%{composer_vendor}-%{composer_project}

%global with_tests 1

Name:    php-%{composer_vendor}-%{composer_project}
Version: 0.6.0
Release: 11%{?dist}

Summary: A compiler for LESS written in PHP
License: MIT OR GPL-3.0-only
URL:     https://www.maswaba.de/lesserphpdocs/

%global repo_owner  MarcusSchwarz
%global repo_name   lesserphp
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/v%{version}/%{repo_name}-%{version}.tar.gz

BuildArch: noarch

%if 0%{?with_tests}
BuildRequires: phpunit9
%endif
BuildRequires: php-fedora-autoloader-devel

Requires: php-cli >= 7.2.0
Requires: php-ctype
Requires: php-date
Requires: php-fileinfo
Requires: php-pcre
Requires: php-composer(fedora/autoloader)

# Composer
Provides: php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# This project is a fork of lessphp, which was previously packaged for Fedora
Obsoletes: php-lessphp <= 0.5.0+0


%description
lesserphp is a compiler that generates CSS from a superset language which adds
a collection of convenient features often seen in other languages.
All CSS is compatible with LESS, so you can start using new features
with your existing CSS.

It is designed to be compatible with less.js (https://lesscss.org/),
and suitable as a drop-in replacement for PHP projects.

Autoloader: %{pkgdir}/autoload.php


%prep
%autosetup -p1 -n %{repo_name}-%{version}

# Lessify is broken upstream and we don't want to install it
rm lessify lessify.inc.php

# Fix include paths
sed -e 's|^require $path."lessc.inc.php";$|require "%{pkgdir}/lessc.inc.php";|' -i plessc


%build
# Create autoloader
phpab \
  --template fedora \
  --output autoload.php \
  lessc.inc.php
cat autoload.php


%install
# Library
install -d -m 755 %{buildroot}%{pkgdir}
install -m 644 -p autoload.php lessc.inc.php %{buildroot}%{pkgdir}/

# Executables
install -d -m 755 %{buildroot}%{_bindir}
install -m 0755 -p plessc  %{buildroot}%{_bindir}/plessc


%check
%if 0%{?with_tests}
phpunit9 --verbose --bootstrap %{buildroot}%{pkgdir}/autoload.php
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{pkgdir}/
%{_bindir}/plessc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0-10
- Migrate License tag to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 10 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0-1
- Update to v0.6.0
- Drop Patch0 (backport from upstream - included in this release)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-5
- Fix FedoraAutoloader-related Requires/BuildRequires

* Thu Mar 12 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-4
- Include a patch to address uses of deprecated syntax in plessc
- Do not include "lessify" in the package (broken upstream code)

* Tue Mar 10 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-3
- Add a fake revision number to the "Obsoletes: php-lessphp" tag
- Make executables include required files directly, instead of using the autoloader

* Sat Mar 07 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-2
- Fix the License: tag
- Preserve timestamps during %%install

* Mon Mar 02 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-1
- Initial packaging
