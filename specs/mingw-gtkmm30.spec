%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-gtkmm30
Version:        3.24.9
Release:        3%{?dist}
Summary:        MinGW Windows C++ interface for the GTK+ library

License:        LGPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gtkmm/%{release_version}/gtkmm-%{version}.tar.xz

BuildArch:      noarch

# For glib-compile-resources
BuildRequires:  glib2-devel
# For gdk-pixbuf-pixdata
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  meson

BuildRequires:  mingw32-atkmm
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairomm
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glibmm24
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-pangomm

BuildRequires:  mingw64-atkmm
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairomm
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glibmm24
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-pangomm

%description
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.

This package contains the MinGW Windows cross compiled gtkmm library,
API version 3.0.


%package -n mingw32-gtkmm30
Summary:        MinGW Windows C++ interface for the GTK+ library

%description -n mingw32-gtkmm30
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.

This package contains the MinGW Windows cross compiled gtkmm library,
API version 3.0.


%package -n mingw64-gtkmm30
Summary:        MinGW Windows C++ interface for the GTK+ library

%description -n mingw64-gtkmm30
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.

This package contains the MinGW Windows cross compiled gtkmm library,
API version 3.0.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gtkmm-%{version}


%build
%mingw_meson -Dbuild-demos=false -Dbuild-tests=false
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-gtkmm30
%license COPYING
%{mingw32_bindir}/libgdkmm-3.0-1.dll
%{mingw32_bindir}/libgtkmm-3.0-1.dll
%{mingw32_libdir}/libgdkmm-3.0.dll.a
%{mingw32_libdir}/libgtkmm-3.0.dll.a
%{mingw32_includedir}/gdkmm-3.0/
%{mingw32_includedir}/gtkmm-3.0/
%{mingw32_libdir}/gdkmm-3.0/
%{mingw32_libdir}/gtkmm-3.0/
%{mingw32_libdir}/pkgconfig/gdkmm-3.0.pc
%{mingw32_libdir}/pkgconfig/gtkmm-3.0.pc

%files -n mingw64-gtkmm30
%license COPYING
%{mingw64_bindir}/libgdkmm-3.0-1.dll
%{mingw64_bindir}/libgtkmm-3.0-1.dll
%{mingw64_libdir}/libgdkmm-3.0.dll.a
%{mingw64_libdir}/libgtkmm-3.0.dll.a
%{mingw64_includedir}/gdkmm-3.0/
%{mingw64_includedir}/gtkmm-3.0/
%{mingw64_libdir}/gdkmm-3.0/
%{mingw64_libdir}/gtkmm-3.0/
%{mingw64_libdir}/pkgconfig/gdkmm-3.0.pc
%{mingw64_libdir}/pkgconfig/gtkmm-3.0.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 23 2024 Sandro Mani <manisandro@gmail.com> - 3.24.9-1
- Update to 3.24.9

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Sandro Mani <manisandro@gmail.com> - 3.24.8-1
- Update to 3.24.8

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Sandro Mani <manisandro@gmail.com> - 3.24.7-1
- Update to 3.24.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Sandro Mani <manisandro@gmail.com> - 3.24.6-1
- Update to 3.24.6

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.24.5-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Sandro Mani <manisandro@gmail.com> - 3.24.5-1
- Update to 3.24.5

* Wed Feb 24 2021 Sandro Mani <manisandro@gmail.com> - 3.24.4-1
- Update to 3.24.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Sandro Mani <manisandro@gmail.com> - 3.24.3-1
- Update to 3.24.3

* Wed Aug 12 13:39:40 GMT 2020 Sandro Mani <manisandro@gmail.com> - 3.24.2-4
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Sandro Mani <manisandro@gmail.com> - 3.24.2-1
- Update to 3.24.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.24.1-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Aug 30 2019 Sandro Mani <manisandro@gmail.com> - 3.24.1-1
- Update to 3.24.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Don't set group tags

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-2
- Rebuild against latest mingw-gcc

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro for the COPYING file

* Sat Nov 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.12.0-1
- Update to 3.12.0
- Fixes FTBFS against modern mingw-gtk3 versions

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.8.1-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Mon May  6 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.8.1-1
- update to 3.8.1

* Mon Apr  1 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.12-1
- update to 3.7.12

* Sun Mar  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.10-1
- Update to 3.7.10

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.6.0-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Thu Nov 29 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 14 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Fri Mar 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.2.0-5
- Build 64 bit Windows binaries

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.2.0-4
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 3.2.0-3
- Rebuilt for libpng 1.5
- Dropped the .la files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 3.2.0-1
- Update to 3.2.0
- Dropped upstreamed patch

* Thu Jul 07 2011 Kalev Lember <kalevlember@gmail.com> - 3.0.1-3
- Rebuilt against win-iconv

* Sun May 29 2011 Kalev Lember <kalev@smartlink.ee> - 3.0.1-2
- Renamed the base package to mingw-gtkmm30 as per updated guidelines
- Use the automatic dep extraction available in mingw32-filesystem 68

* Mon May 09 2011 Kalev Lember <kalev@smartlink.ee> - 3.0.1-1
- Update to 3.0.1

* Mon May 02 2011 Kalev Lember <kalev@smartlink.ee> - 3.0.0-1
- Initial RPM release
