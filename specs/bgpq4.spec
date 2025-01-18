%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}

Summary:        Automate BGP filter generation based on routing database information
Name:           bgpq4
Version:        1.15
Release:        3%{?dist}
# bgpq4 itself is BSD-2-Clause but uses other source codes, breakdown:
# BSD-3-Clause: include/sys/queue.h
# ISC: compat/strlcpy.c
# LicenseRef-Fedora-Public-Domain: include/{string,sys/{_null,types}}.h
License:        BSD-2-Clause AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/bgp/bgpq4
Source0:        https://github.com/bgp/bgpq4/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make

%description
The bgpq4 utility can be used to generate BGP filter configurations
such as prefix lists, (extended) access lists, policy statement terms
and AS path lists based on routing database information and supports
output formats for BIRD, Cisco, Huawei, Juniper, MikroTik, Nokia and
OpenBGPD routers as well as generic JSON.

%prep
%autosetup -p1
autoreconf --install

%build
%configure --docdir=%{_pkgdocdir}
%make_build

%install
%make_install

%check
make check

%files
%license COPYRIGHT
%doc README.md CHANGES
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 15 2024 Robert Scheck <robert@fedoraproject.org> 1.15-1
- Upgrade to 1.15

* Wed May 15 2024 Robert Scheck <robert@fedoraproject.org> 1.14-1
- Upgrade to 1.14

* Mon May 06 2024 Robert Scheck <robert@fedoraproject.org> 1.13-1
- Upgrade to 1.13 (#2278792)

* Sat Feb 17 2024 Robert Scheck <robert@fedoraproject.org> 1.12-1
- Upgrade to 1.12 (#2263974)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 Robert Scheck <robert@fedoraproject.org> 1.11-1
- Upgrade to 1.11 (#2216590)

* Sun Jun 04 2023 Robert Scheck <robert@fedoraproject.org> 1.10-1
- Upgrade to 1.10 (#2212107)

* Sun Mar 05 2023 Robert Scheck <robert@fedoraproject.org> 1.9-1
- Upgrade to 1.9 (#2175524)

* Sat Jan 21 2023 Robert Scheck <robert@fedoraproject.org> 1.8-1
- Upgrade to 1.8 (#2162768)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Robert Scheck <robert@fedoraproject.org> 1.7-1
- Upgrade to 1.7 (#2139999)

* Thu Sep 08 2022 Robert Scheck <robert@fedoraproject.org> 1.6-1
- Upgrade to 1.6 (#2125187)

* Tue Jul 26 2022 Robert Scheck <robert@fedoraproject.org> 1.5-1
- Upgrade to 1.5 (#2110794)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Robert Scheck <robert@fedoraproject.org> 1.4-1
- Upgrade to 1.4 (#1996194)

* Thu Aug 19 2021 Robert Scheck <robert@fedoraproject.org> 1.2-1
- Upgrade to 1.2 (#1995834)

* Wed Aug 18 2021 Robert Scheck <robert@fedoraproject.org> 0.0.9-1
- Upgrade to 0.0.9 (#1994843)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 26 2021 Robert Scheck <robert@fedoraproject.org> 0.0.7-1
- Upgrade to 0.0.7 (#1953767)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Robert Scheck <robert@fedoraproject.org> 0.0.6-1
- Upgrade to 0.0.6 (#1847220)
- Initial spec file for Fedora and Red Hat Enterprise Linux
