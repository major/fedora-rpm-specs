%?mingw_package_header

Name:           mingw-gtkmm24
Version:        2.24.5
Release:        23%{?dist}
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.24/gtkmm-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glibmm24
BuildRequires:  mingw32-atk
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-gtk2 >= 2.19.6
BuildRequires:  mingw32-cairomm
BuildRequires:  mingw32-pangomm
BuildRequires:  mingw32-atkmm

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glibmm24
BuildRequires:  mingw64-atk
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-gtk2 >= 2.19.6
BuildRequires:  mingw64-cairomm
BuildRequires:  mingw64-pangomm
BuildRequires:  mingw64-atkmm


%description
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2.  Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.


# Win32
%package -n mingw32-gtkmm24
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)
Requires:       pkgconfig

# Fix upgrade path for people updating from the mingw-w64 testing repository
Obsoletes:      mingw32-gtkmm24-static < 2.24.2-5

%description -n mingw32-gtkmm24
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2.  Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

# Win64
%package -n mingw64-gtkmm24
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)
Requires:       pkgconfig

# Fix upgrade path for people updating from the mingw-w64 testing repository
Obsoletes:      mingw64-gtkmm24-static < 2.24.2-5

%description -n mingw64-gtkmm24
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2.  Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.


%?mingw_debug_package


%prep
%setup -q -n gtkmm-%{version}


%build
%mingw_configure --disable-static --enable-shared --disable-demos --disable-documentation
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/gtkmm-2.4/demo/
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/gtkmm-2.4/demo/

# hack: some headers are not available on win32
sed -i -e "s,#include <gtkmm/pagesetupunixdialog.h>,," $RPM_BUILD_ROOT/%{mingw32_includedir}/gtkmm-2.4/gtkmm.h
sed -i -e "s,#include <gtkmm/printer.h>,," $RPM_BUILD_ROOT/%{mingw32_includedir}/gtkmm-2.4/gtkmm.h
sed -i -e "s,#include <gtkmm/printjob.h>,," $RPM_BUILD_ROOT/%{mingw32_includedir}/gtkmm-2.4/gtkmm.h
sed -i -e "s,#include <gtkmm/printunixdialog.h>,," $RPM_BUILD_ROOT/%{mingw32_includedir}/gtkmm-2.4/gtkmm.h

# Remove .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-gtkmm24
%doc COPYING
%{mingw32_bindir}/libgdkmm-2.4-1.dll
%{mingw32_bindir}/libgtkmm-2.4-1.dll
%{mingw32_libdir}/libgdkmm-2.4.dll.a
%{mingw32_libdir}/libgtkmm-2.4.dll.a
%{mingw32_includedir}/gdkmm-2.4
%{mingw32_includedir}/gtkmm-2.4
%{mingw32_libdir}/gdkmm-2.4
%{mingw32_libdir}/gtkmm-2.4
%{mingw32_libdir}/pkgconfig/gdkmm-2.4.pc
%{mingw32_libdir}/pkgconfig/gtkmm-2.4.pc

# Win64
%files -n mingw64-gtkmm24
%doc COPYING
%{mingw64_bindir}/libgdkmm-2.4-1.dll
%{mingw64_bindir}/libgtkmm-2.4-1.dll
%{mingw64_libdir}/libgdkmm-2.4.dll.a
%{mingw64_libdir}/libgtkmm-2.4.dll.a
%{mingw64_includedir}/gdkmm-2.4
%{mingw64_includedir}/gtkmm-2.4
%{mingw64_libdir}/gdkmm-2.4
%{mingw64_libdir}/gtkmm-2.4
%{mingw64_libdir}/pkgconfig/gdkmm-2.4.pc
%{mingw64_libdir}/pkgconfig/gtkmm-2.4.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.24.5-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.24.5-15
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:39:27 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.24.5-11
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.24.5-8
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Kalev Lember <klember@redhat.com> - 2.24.5-1
- Update to 2.24.5
- Don't set group tags

* Fri Feb 12 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.4-5
- build fix (enable C++11)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.4-1
- update to 2.24.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.2-8
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.2-6
- Added win64 support (contributed by Tim Mayberry)

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.2-5
- Renamed the source package to mingw-gtkmm24 (RHBZ #800880)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.2-4
- Rebuild against the mingw-w64 toolchain

* Thu Feb  2 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.2-3
- Dropped the .la files
- Dropped the BuildRoot tag

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 2.24.2-2
- Rebuilt for libpng 1.5

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.2-1
- update to 2.24.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Kalev Lember <kalevlember@gmail.com> - 2.24.0-3
- Rebuilt against win-iconv

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.24.0-2
- Rebuilt for proxy-libintl removal

* Sun Feb 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.0-1
- update to 2.24.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.22.0-1
- update to 2.22.0

* Sun Feb 28 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.19.6-1
- update to 2.19.6

* Sun Jan 31 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.19.2-1
- update to 2.19.2

* Tue Oct  6 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.18.2-1
- update to 2.18.2
- remove includes of nonexistent header files

* Sun Sep 27 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.18.1-1
- update to 2.18.1 to match native

* Sat Sep 19 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.17.11-1
- update to 2.17.11 to match native

* Mon Aug 31 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.17.2-1
- update to 2.17.2 to match native

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.16.0-2
- add debuginfo packages

* Sat Apr 18 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.16.0-1
- update to 2.16.0 to match native
- remove COPYING.tools, as the binary does not contain any program from
  the tools directory
- do not build docs

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.15.0-2
- replace %%define with %%global

* Wed Mar 25 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.15.0-1
- update to 2.15.0

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.1-5
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.1-4
- Include license file.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.1-3
- Use _smp_mflags.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.1-2
- Requires pkgconfig.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.1-1
- Initial RPM release.
