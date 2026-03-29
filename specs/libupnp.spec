Version: 1.18.4
Summary: Universal Plug and Play (UPnP) SDK
Name: libupnp
Release: 1%{?dist}
License: BSD-3-Clause AND ISC AND MIT
URL: https://github.com/pupnp/pupnp
Source: %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: libtool


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
autoreconf -vif
%configure \
  --enable-static=no \
  --enable-ipv6

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

%{__rm} %{buildroot}%{_libdir}/{libixml.la,libupnp.la}

%files
%license COPYING
%doc THANKS
%{_libdir}/libixml.so.11*
%{_libdir}/libupnp.so.20*

%files devel
%{_includedir}/upnp/
%{_libdir}/libixml.so
%{_libdir}/libupnp.so
%{_libdir}/pkgconfig/libupnp.pc

%changelog
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
