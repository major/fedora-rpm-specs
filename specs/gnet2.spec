Name:           gnet2
Version:        2.0.8
Release:        34%{?dist}
Summary:        A simple network library built upon glib

License:        LGPL-2.0-or-later
URL:            http://www.gnetlibrary.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnet/2.0/gnet-%{version}.tar.bz2
Patch1:         gnet2-2.0.8-build.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires: make

%description
GNet is a simple network library. It is written in C, object-oriented, and
built upon GLib. It is intended to be easy to use and port.

%package        devel
Summary:        Headers and libraries for building apps that use gnet2
Requires:       %{name} = %{version} glib2-devel

%description    devel
This package contains headers and libraries required to build applications that
use GNet 2.

%prep
%setup -q -n gnet-%{version}
%patch -P1 -p1 -b .build

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

%ldconfig_scriptlets

%files
%doc AUTHORS BUGS COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%doc HACKING
%{_datadir}/aclocal/*
%{_datadir}/gtk-doc/html/gnet
%{_includedir}/*
%{_libdir}/gnet-*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-29
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Tomas Mraz <tmraz@redhat.com> 2.0.8-4
- Fix FTBFS due to linker and gcc changes (#564691)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun  5 2008 Tomas Mraz <tmraz@redhat.com> 2.0.8-1
- upgrade to new upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.7-11
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Tomas Mraz <tmraz@redhat.com> 2.0.7-10
- license tag fix

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.0.7-9
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Tomas Mraz <tmraz@redhat.com> 2.0.7-8
- Rebuild for Fedora Extras 6

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-6
- Rebuild for Fedora Extras 5

* Wed Nov  9 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-5
- Removed static libs
- Removed .la

* Tue Jun 21 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-4
- Added .so to -devel (#161283)
- Cleaned up %%changelog

* Mon May  9 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-3
- Added disttag

* Mon Apr 11 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-3
- Added glib2-devel to Requires of -devel

* Mon Apr 11 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-2
- Minor specfile cleanups

* Wed Mar 30 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-1
- Initial RPM release
