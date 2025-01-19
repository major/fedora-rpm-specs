%global commit 9dee4a3ff1438ce3099811833e80f614dfa78932
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:          mkrdns
Version:       3.3
Release:       16.20220829git%{shortcommit}%{?dist}
Summary:       Automatic reverse DNS zone generator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://github.com/oasys/%{name}
Source0:       https://github.com/oasys/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:     noarch
BuildRequires: perl-podlators
Requires:      perl-Getopt-Long

%description
mkrdns automates the tedious procedure of editing both forward and reverse 
zones when making changes to your zones with likely no changes to your current 
configuration file.

mkrdns does this by reading through all of the primary/secondary (master/slave) 
zones in your configuration file (either named.boot or named.conf). It will 
then automatically generate the reverse zone entries (IN PTR) for the networks 
for which you are the primary/master. It is now possible to simply edit the 
forward map, run mkrdns, and reload the zone. Clean, simple, and best of all, 
automatic.

mkrdns also acts as a limited lint-like program, issuing warnings and errors if 
there are problems with your configuration or zone files.

%prep
%autosetup -n %{name}-%{commit}

%build
# Nothing to build

%install
install -Dp -m 0755 mkrdns %{buildroot}%{_bindir}/mkrdns
mkdir -p %{buildroot}%{_mandir}/man1
pod2man mkrdns %{buildroot}%{_mandir}/man1/mkrdns.1

%files
%doc README.md
%license LICENSE
%{_bindir}/mkrdns
%{_mandir}/man1/mkrdns.1.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-16.20220829git9dee4a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3-15.20220829git9dee4a3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-14.20220829git9dee4a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-13.20220829git9dee4a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12.20220829git9dee4a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11.20220829git9dee4a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-10.20220829git9dee4a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 29 2022 Christian Schuermann <spike@fedoraproject.org> 3.3-9.20220829git9dee4a3
- Updated to latest git commit to include response-policy support

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8.20210224gitf6e8414
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7.20210224gitf6e8414
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6.20210224gitf6e8414
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 24 2021 Christian Schuermann <spike@fedoraproject.org> 3.3-5.20210224gitf6e8414
- Updated to latest git commit to include license file

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4.20190902git6b3f3a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3.20190902git6b3f3a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2.20190902git6b3f3a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 2 2019 Christian Schuermann <spike@fedoraproject.org> 3.3-1.20190902git6b3f3a4
- Initial package
