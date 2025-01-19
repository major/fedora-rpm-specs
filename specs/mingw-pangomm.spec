%{?mingw_package_header}

%global apiver 1.4
# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-pangomm
Version:        2.46.4
Release:        3%{?dist}
Summary:        MinGW Windows C++ interface for Pango

License:        LGPL-2.0-or-later
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/pangomm/%{release_version}/pangomm-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson

BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairomm
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glibmm24
BuildRequires:  mingw32-pango

BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairomm
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glibmm24
BuildRequires:  mingw64-pango

%description
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package -n mingw32-pangomm
Summary:        MinGW Windows C++ interface for Pango
Obsoletes:      mingw32-pangomm-static < 2.28.4-3
Provides:       mingw32-pangomm-static = 2.28.4-3

%description -n mingw32-pangomm
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package -n mingw64-pangomm
Summary:        MinGW Windows C++ interface for Pango
Obsoletes:      mingw64-pangomm-static < 2.28.4-3
Provides:       mingw64-pangomm-static = 2.28.4-3

%description -n mingw64-pangomm
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n pangomm-%{version}


%build
%mingw_meson
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-pangomm
%license COPYING COPYING.tools
%{mingw32_bindir}/libpangomm-%{apiver}-1.dll
%{mingw32_libdir}/libpangomm-%{apiver}.dll.a
%{mingw32_libdir}/pkgconfig/pangomm-%{apiver}.pc
%{mingw32_libdir}/pangomm-%{apiver}/
%{mingw32_includedir}/pangomm-%{apiver}

%files -n mingw64-pangomm
%license COPYING COPYING.tools
%{mingw64_bindir}/libpangomm-%{apiver}-1.dll
%{mingw64_libdir}/libpangomm-%{apiver}.dll.a
%{mingw64_libdir}/pkgconfig/pangomm-%{apiver}.pc
%{mingw64_libdir}/pangomm-%{apiver}/
%{mingw64_includedir}/pangomm-%{apiver}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Sandro Mani <manisandro@gmail.com> - 2.46.4-1
- Update to 2.46.4

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 01 2022 Sandro Mani <manisandro@gmail.com> - 2.46.3-1
- Update to 2.46.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.46.2-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Sandro Mani <manisandro@gmail.com> - 2.46.2-1
- Update to 2.46.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Sandro Mani <manisandro@gmail.com> - 2.46.1-1
- Update to 2.46.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Sandro Mani <manisandro@gmail.com> - 2.42.2-1
- Update to 2.42.2

* Wed Aug 12 13:44:39 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.42.1-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Sandro Mani <manisandro@gmail.com> - 2.42.1-1
- Update to 2.42.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.40.2-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Aug 29 2019 Sandro Mani <manisandro@gmail.com> - 2.40.2-1
- Update to 2.40.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.40.1-1
- update to 2.40.1

* Mon May 02 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.40.0-1
- update to 2.40.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.39.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 2.39.1-2
- Use global instead of define.

* Tue Dec 29 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.39.1-1
- update to 2.39.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 2.38.1-1
- Update to 2.38.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 2.36.0-2
- Rebuild against latest mingw-gcc

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 2.36.0-1
- Update to 2.36.0
- Use license macro for the COPYING files

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.34.0-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Mon May  6 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.34.0-1
- update to 2.34.0

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.4-5
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.4-3
- Bump EVR to be higher than the package in the mingw-w64 testing repo
- Fix upgrade path for people who are upgrading from the mingw-w64 testing repo

* Sun Apr  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.4-1
- Update to 2.28.4

* Thu Mar 15 2012 Kalev Lember <kalevlember@gmail.com> - 2.28.3-6
- Build 64 bit Windows binaries

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 2.28.3-5
- Renamed the source package to mingw-pangomm (#801010)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.3-4
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 2.28.3-3
- Rebuilt for libpng 1.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 2.28.3-1
- Update to 2.28.3
- Use automatic mingw dep extraction
- Clean up the spec file for recent rpmbuild

* Thu Jul 07 2011 Kalev Lember <kalevlember@gmail.com> - 2.28.2-2
- Rebuilt against win-iconv

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.28.2-1
- Update to 2.28.2
- Use macro for calculating two digit version in download url
- Own libdir/pangomm-1.4/ dir

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.27.1-2
- Rebuilt for proxy-libintl removal

* Sun Feb 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.27.1-1
- update to 2.27.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.26.2-1
- update to 2.26.2

* Sun Sep 27 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.26.0-1
- update to 2.26.0 to match native package

* Sun Sep 20 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.25.1.3-2
- also package pangommconfig.h

* Sat Sep 19 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.25.1.3-1
- update to 2.25.1.3 to match native package

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.0-3
- add debuginfo packages

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.0-2
- replace %%define with %%global

* Tue Apr  7 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.0-1
- Update to upstream 2.24.0, to keep mingw32 package in sync with
  native pangomm

* Wed Mar 25 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.14.1-1
- update to 2.14.1

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-6
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-5
- Include license file.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-4
- Use _smp_mflags.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-3
- Requires pkgconfig.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-2
- Initial RPM release.
