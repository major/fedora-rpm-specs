%{?mingw_package_header}

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-glibmm24
Version:        2.66.7
Release:        3%{?dist}
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)

License:        LGPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glibmm/%{release_version}/glibmm-%{version}.tar.xz
# Export Glib::Threads::wrap symbols (#2017676)
Patch0:         glibmm_export-symbols.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-libsigc++20 >= 2.0.0
BuildRequires:  mingw64-libsigc++20 >= 2.0.0
BuildRequires:  mingw32-glib2 >= 2.48.0
BuildRequires:  mingw64-glib2 >= 2.48.0

BuildRequires:  meson
BuildRequires:  perl
BuildRequires:  perl-Getopt-Long

%description
glibmm provides a C++ interface to the GTK+ GLib low-level core
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.


# Win32
%package -n mingw32-glibmm24
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)

%description -n mingw32-glibmm24
glibmm provides a C++ interface to the GTK+ GLib low-level core
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n mingw32-glibmm24-static
Summary:        Static cross compiled version of the glibmm library
Requires:       mingw32-glibmm24 = %{version}-%{release}

%description -n mingw32-glibmm24-static
Static cross compiled version of the glibmm library.

# Win64
%package -n mingw64-glibmm24
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)

%description -n mingw64-glibmm24
glibmm provides a C++ interface to the GTK+ GLib low-level core
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n mingw64-glibmm24-static
Summary:        Static cross compiled version of the glibmm library
Requires:       mingw64-glibmm24 = %{version}-%{release}

%description -n mingw64-glibmm24-static
Static cross compiled version of the glibmm library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n glibmm-%{version}


%build
%mingw_meson --default-library=both
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-glibmm24
%license COPYING COPYING.tools
%{mingw32_bindir}/libgiomm-2.4-1.dll
%{mingw32_bindir}/libglibmm-2.4-1.dll
%{mingw32_bindir}/libglibmm_generate_extra_defs-2.4-1.dll
%{mingw32_libdir}/libgiomm-2.4.dll.a
%{mingw32_libdir}/libglibmm-2.4.dll.a
%{mingw32_libdir}/libglibmm_generate_extra_defs-2.4.dll.a
%{mingw32_libdir}/giomm-2.4
%{mingw32_libdir}/glibmm-2.4
%{mingw32_includedir}/giomm-2.4
%{mingw32_includedir}/glibmm-2.4
%{mingw32_libdir}/pkgconfig/giomm-2.4.pc
%{mingw32_libdir}/pkgconfig/glibmm-2.4.pc

%files -n mingw32-glibmm24-static
%{mingw32_libdir}/libgiomm-2.4.a
%{mingw32_libdir}/libglibmm-2.4.a
%{mingw32_libdir}/libglibmm_generate_extra_defs-2.4.a

# Win64
%files -n mingw64-glibmm24
%license COPYING COPYING.tools
%{mingw64_bindir}/libgiomm-2.4-1.dll
%{mingw64_bindir}/libglibmm-2.4-1.dll
%{mingw64_bindir}/libglibmm_generate_extra_defs-2.4-1.dll
%{mingw64_libdir}/libgiomm-2.4.dll.a
%{mingw64_libdir}/libglibmm-2.4.dll.a
%{mingw64_libdir}/libglibmm_generate_extra_defs-2.4.dll.a
%{mingw64_libdir}/giomm-2.4
%{mingw64_libdir}/glibmm-2.4
%{mingw64_includedir}/giomm-2.4
%{mingw64_includedir}/glibmm-2.4
%{mingw64_libdir}/pkgconfig/giomm-2.4.pc
%{mingw64_libdir}/pkgconfig/glibmm-2.4.pc

%files -n mingw64-glibmm24-static
%{mingw64_libdir}/libgiomm-2.4.a
%{mingw64_libdir}/libglibmm-2.4.a
%{mingw64_libdir}/libglibmm_generate_extra_defs-2.4.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.66.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.66.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 26 2024 Sandro Mani <manisandro@gmail.com> - 2.66.7-1
- Update to 2.66.7

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.66.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.66.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.66.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 2.66.6-1
- Update to 2.66.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.66.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 22 2022 Sandro Mani <manisandro@gmail.com> - 2.66.5-1
- Update to 2.66.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.66.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Sandro Mani <manisandro@gmail.com> - 2.66.4-1
- Update to 2.66.4

* Wed May 04 2022 Sandro Mani <manisandro@gmail.com> - 2.66.3-1
- Update to 2.66.3

* Tue Mar 29 2022 Sandro Mani <manisandro@gmail.com> - 2.66.2-4
- Export Glib::Threads::wrap symbols (#2017676)

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.66.2-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.66.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Sandro Mani <manisandro@gmail.com> - 2.66.2-1
- Update to 2.66.2

* Mon Aug 02 2021 Sandro Mani <manisandro@gmail.com> - 2.66.1-1
- Update to 2.66.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Sandro Mani <manisandro@gmail.com> - 2.64.5-1
- Update to 2.64.5

* Wed Nov 25 2020 Sandro Mani <manisandro@gmail.com> - 2.64.4-1
- Update to 2.64.4

* Wed Aug 12 13:37:08 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.64.2-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Sandro Mani <manisandro@gmail.com> - 2.64.2-1
- Update to 2.64.2

* Thu Mar 19 2020 Sandro Mani <manisandro@gmail.com> - 2.64.1-1
- Update to 2.64.1

* Tue Mar 17 2020 Sandro Mani <manisandro@gmail.com> - 2.64.0-1
- Update to 2.64.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.62.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.62.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Sep 19 2019 Sandro Mani <manisandro@gmail.com> - 2.62.0-1
- Updat eto 2.62.0

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 2.60.0-1
- Update to 2.60.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.58.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.58.0-1
- update 2.58.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.56.0-1
- update to 2.56.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.54.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 2.54.1-1
- Update to 2.54.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Sandro Mani <manisandro@gmail.com> - 2.52.0-2
- Rebuild to fix missing provides misteriously missing in previous build

* Mon Jul 03 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.52.0-1
- update to 2.52.0

* Thu Jun 01 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.51.7-1
- update to 2.51.7

* Fri May 05 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.51.6-1
- update to 2.51.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 2.50.0-1
- Update to 2.50.0
- Don't set group tags

* Thu Sep 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.49.5-1
- update to 2.49.5

* Mon Aug 08 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.49.4-1
- update to 2.49.4

* Fri Apr 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.48.1-1
- update to 2.48.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 2.47.4-2
- Use global instead of define.

* Tue Dec 29 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.47.4
- update to 2.47.4

* Tue Dec  1 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.47.3.1
- update to 2.47.3.1

* Tue Dec  1 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.46.2-1
- update to 2.46.2

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 2.46.1-1
- Update to 2.46.1

* Thu Jul  2 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.45.3-1
- update to 2.45.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.0-2
- Rebuild against latest mingw-gcc

* Wed Mar 25 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.0-1
- Update to 2.44.0
- Use license macro for the COPYING files

* Fri Jan  2 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.43.2-1
- update to 2.43.2

* Wed Oct  1 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.42.0-1
- update to 2.42.0

* Tue Jul  1 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.41.1-1
- update to 2.41.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun  1 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.41.0-1
- update to 2.41.0

* Wed Apr  2 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.39.92-1
- update to 2.39.92

* Thu Mar  6 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.39.91-1
- update to 2.39.91

* Tue Dec  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.38.1-1
- update to 2.38.1

* Tue Sep  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.37.6-1
- update to 2.37.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.36.2-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Mon May  6 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.36.2-1
- update to 2.36.2

* Mon Apr  1 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.35.9-1
- update to 2.35.9

* Sun Mar  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.35.8-1
- update to 2.35.8

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.34.1-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Wed Nov 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.34.1-1
- Update to 2.34.1

* Fri Aug  3 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.32.1-1
- update to 2.32.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 14 2012 Kalev Lember <kalevlember@gmail.com> - 2.32.0-1
- Update to 2.32.0

* Sun Apr  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.31.22-1
- Update to 2.31.22
- Added -static subpackage
- Cleaned up unneeded %%global tags
- Dropped upstreamed patches

* Thu Mar 15 2012 Kalev Lember <kalevlember@gmail.com> - 2.31.2-5
- Build 64 bit Windows binaries

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.31.2-4
- Renamed the source package to mingw-glibmm24 (RHBZ #800875)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.31.2-3
- Remove .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.31.2-2
- Rebuild against the mingw-w64 toolchain

* Sat Jan 14 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.31.2-1
- Update to 2.31.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 2.30.0-1
- Update to 2.30.0
- Use automatic mingw dep extraction
- Clean up the spec file for recent rpmbuild
- Drop hacks for sed'ing headers; this is now in upstream

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 2.28.1-2
- Rebuilt against win-iconv

* Tue May 10 2011 Kalev Lember <kalev@smartlink.ee> - 2.28.1-1
- Update to 2.28.1
- Dropped upstreamed unixfdlist patch

* Mon May 02 2011 Kalev Lember <kalev@smartlink.ee> - 2.28.0-2
- Backported an upstream patch to avoid including unixfdlist.h on win32

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.28.0-1
- Update to 2.28.0
- Use macro for calculating two digit version in download url

* Wed Apr 27 2011 Kalev Lember <kalev@smartlink.ee> - 2.27.93-2
- Rebuilt for proxy-libintl removal

* Sun Feb 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.27.93-1
- update to 2.27.93

* Mon Dec  6 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.27.4-1
- update to 2.27.4

* Thu Aug  5 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.1-1
- update to 2.24.1

* Sun Feb 28 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.23.2-1
- update to 2.23.2

* Sun Jan 31 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.23.1-1
- update to 2.23.1

* Tue Oct  6 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.22.1-2
- remove nonexisting (on windows) files from giomm.h header

* Sun Sep 27 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.22.1-1
- update to 2.22.1 to match native package

* Sat Sep 19 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.21.5-1
- update to 2.21.5 to match native package

* Mon Aug 31 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.21.4-1
- update to 2.21.4 to match native package

* Mon Aug 31 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.21.3-1
- update to 2.21.3 to match native package

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.20.0-4
- add debuginfo packages

* Fri Apr 17 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.20.0-3
- fix extradefs build failure

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.20.0-2
- update to 2.20.0
- replace %%define with %%global

* Wed Mar 25 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.19.2-1
- update to 2.19.2

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.18.1-5
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.18.1-4
- Include license.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.18.1-3
- Use _smp_mflags.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.1-2
- Initial RPM release.
