Name: libqrtr-glib
Version: 1.0.0
Release: 4%{?dist}
Summary: Support library to use and manage the QRTR (Qualcomm IPC Router) bus.
License: LGPLv2+
URL: http://freedesktop.org/software/libqrtr-glib
Source: http://freedesktop.org/software/libqmi/libqrtr-glib/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: glib2-devel >= 2.48.0
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gudev-1.0) >= 147
BuildRequires: make
BuildRequires: python3

%description
This package contains the libraries that make it easier to use and
manage the QRTR (Qualcomm IPC Router) bus.


%package devel
Summary: Header files for adding QRTR support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel

%description devel
This package contains the header and pkg-config files for development
applications using QRTR functionality from applications that use glib.


%prep
%autosetup -p1


%build
%configure --enable-gtk-doc
%make_build V=1


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete


%ldconfig_scriptlets


%files
%license COPYING.LIB
%doc NEWS AUTHORS README
%{_libdir}/libqrtr-glib.so.*
%{_libdir}/girepository-1.0/Qrtr-1.0.typelib


%files devel
%{_includedir}/libqrtr-glib/
%{_libdir}/libqrtr-glib.so
%{_libdir}/pkgconfig/qrtr-glib.pc
%{_datadir}/gtk-doc/html/libqrtr-glib/
%{_datadir}/gir-1.0/Qrtr-1.0.gir


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 13 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-1
- Initial package
