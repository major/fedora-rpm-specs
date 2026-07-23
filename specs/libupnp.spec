Version: 22.0.4
Summary: Universal Plug and Play (UPnP) SDK
Name: libupnp
Release: 2%{?dist}
License: BSD-3-Clause AND ISC AND MIT
URL: https://github.com/pupnp/pupnp
Source: %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake


%description
The Universal Plug and Play (UPnP) SDK for Linux provides 
support for building UPnP-compliant control points, devices, 
and bridges on Linux.

%package devel
Summary: Include files needed for development with libupnp
Requires: libupnp%{?_isa} = %{version}-%{release}

%description devel
The libupnp-devel package contains the files necessary for development with
the UPnP SDK libraries.

%prep
%autosetup -p1 -n pupnp-release-%{version}


%build
%cmake
%cmake_build

%install
%cmake_install

%{__rm} %{buildroot}%{_libdir}/{libixml.a,libupnp.a}

%files
%license COPYING
%doc THANKS
%{_libdir}/libixml.so.22*
%{_libdir}/libupnp.so.22*
%{_bindir}/tv_combo
%{_bindir}/tv_ctrlpt
%{_bindir}/tv_device
%{_datadir}/upnp/

%files devel
%{_includedir}/upnp/
%{_libdir}/libixml.so
%{_libdir}/libupnp.so
%{_libdir}/pkgconfig/libupnp.pc
%{_libdir}/cmake/UPNP/

%changelog
* Tue Jul 21 2026 Gwyn Ciesla <gwync@protonmail.com> - 22.0.4-1
- 22.0.4

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jun 19 2026 Gwyn Ciesla <gwync@protonmail.com> - 2.0.2-1
- 2.0.2

* Thu Apr 23 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.18.5-1
- 1.18.5

* Sat Mar 28 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.18.4-1
- 1.18.4

* Tue Mar 17 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.18.3-1
- 1.18.3

* Tue Mar 10 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.18.2-1
- 1.18.2

* Wed Mar 04 2026 Simone Caronni <negativo17@gmail.com> - 1.18.1-2
- Update license.
- Trim changelog.
- Drop ldconfig scriptlets.

* Tue Mar 03 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.18.1-1
- 1.18.1

* Tue Feb 10 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.18.0-1
- 1.18.0

* Tue Feb 10 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.14.30-1
- 1.14.30

* Mon Feb 09 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.14.29-1
- 1.14.29

* Fri Feb 06 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.14.26-1
- 1.14.26

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Sep 22 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.14.25-1
- 1.14.25

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jun 12 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.14.24-1
- 1.14.24

* Sat Jun 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.14.23-1
- 1.14.23

* Tue Jun 03 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.14.22-1
- 1.14.22

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild
