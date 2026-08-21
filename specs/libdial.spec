Name: libdial
Summary: Helper library for displaying clocks or dials
License: GPL-3.0-or-later

Version: 2.7
Release: 1%{?dist}

URL: https://theknight.co.uk
Source0: %{URL}/releases/Source/libdial-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: make

BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)

%description
libdial is a GTK3 library which can be used to display a clock or a dial.


%package devel
Summary: Development files for libdial
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files for developing applications using %{name}.


%prep
%autosetup -p1
%configure --enable-static=no


%build
%make_build


%install
%make_install


%files
%doc AUTHORS
%license COPYING
%{_libdir}/libdial.so.2
%{_libdir}/libdial.so.2.0.1


%files devel
%{_libdir}/libdial.so
%{_libdir}/pkgconfig/dial.pc
%{_includedir}/dialsys.h


%changelog
* Wed Aug 12 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.7-1
- Update to v2.7

* Sun Jul 05 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.6-1
- Initial packaging
