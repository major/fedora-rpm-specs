Summary:        Library with simple API for communication with LXI devices
Name:           liblxi
Version:        1.22
Release:        2%{?dist}
# src/vxi11core* and src/include/vxi11core* are EPICS, rest is BSD-3-Clause
License:        BSD-3-Clause AND EPICS
URL:            https://lxi-tools.github.io/
Source0:        https://github.com/lxi/liblxi/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxi/liblxi/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  meson >= 0.53.2
BuildRequires:  %{_bindir}/rpcgen
BuildRequires:  libtirpc-devel
BuildRequires:  avahi-devel
BuildRequires:  libxml2-devel

%description
The LXI library (liblxi) is an open source software library for GNU/Linux
systems which offers a simple API for communicating with LXI enabled
instruments. The API allows applications to easily discover instruments on
networks and communicate SCPI commands.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS NEWS README.md
%{_libdir}/%{name}.so.1*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/lxi.h
%{_mandir}/man3/lxi_*.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Robert Scheck <robert@fedoraproject.org> 1.22-1
- Upgrade to 1.22 (#2324967)

* Fri Oct 04 2024 Robert Scheck <robert@fedoraproject.org> 1.21-1
- Upgrade to 1.21 (#2316416)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 20 2023 Robert Scheck <robert@fedoraproject.org> 1.20-1
- Upgrade to 1.20 (#2208790)

* Wed May 03 2023 Robert Scheck <robert@fedoraproject.org> 1.19-1
- Upgrade to 1.19 (#2192857)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 26 2022 Robert Scheck <robert@fedoraproject.org> 1.18-1
- Upgrade to 1.18 (#2137767)

* Sat Oct 01 2022 Robert Scheck <robert@fedoraproject.org> 1.17-1
- Upgrade to 1.17 (#2131162)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 03 2022 Robert Scheck <robert@fedoraproject.org> 1.16-1
- Upgrade to 1.16 (#2050367)

* Sun Jan 23 2022 Robert Scheck <robert@fedoraproject.org> 1.15-1
- Upgrade to 1.15 (#2043963)

* Sat Jan 22 2022 Robert Scheck <robert@fedoraproject.org> 1.14-1
- Upgrade to 1.14 (#2042909)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Robert Scheck <robert@fedoraproject.org> 1.13-1
- Upgrade to 1.13 (#1556050)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Robert Scheck <robert@fedoraproject.org> 1.7-1
- Upgrade to 1.7

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.3-1
- Upgrade to 1.3

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.2-1
- Upgrade to 1.2

* Sun Oct 08 2017 Robert Scheck <robert@fedoraproject.org> 1.0-2
- Run /sbin/ldconfig (#1499559, thanks to Robert-André Mauchin)

* Sun Oct 08 2017 Robert Scheck <robert@fedoraproject.org> 1.0-1
- Upgrade to 1.0
- Initial spec file for Fedora and Red Hat Enterprise Linux
