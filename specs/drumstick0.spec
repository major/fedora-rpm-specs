%global realname drumstick

Summary: C++/Qt4 wrapper around the ALSA library sequencer interface
Name:    drumstick0
Version: 0.5.0
Release: 40%{?dist}
#define svn svn

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://drumstick.sourceforge.net/
Source0: http://downloads.sourceforge.net/project/drumstick/%{version}%{?svn}/drumstick-%{version}%{?svn}.tar.bz2
# fix FTBFS due to the strict ld in Fedora >= 13
Patch0:  drumstick-0.5.0-fix-implicit-linking.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1307434
Patch1:  drumstick-0.5.0-gcc6.patch

BuildRequires: gcc-c++
BuildRequires: cmake qt4-devel alsa-lib-devel desktop-file-utils
BuildRequires: shared-mime-info
# For building manpages
BuildRequires: docbook-style-xsl /usr/bin/xsltproc
# For building API documents
BuildRequires: doxygen

Obsoletes: aseqmm < %{version}-%{release}
Provides: aseqmm = %{version}-%{release}

%description
The drumstick library is a C++ wrapper around the ALSA library sequencer
interface, using Qt4 objects, idioms and style. The ALSA sequencer interface
provides software support for MIDI technology on GNU/Linux.

%package devel
Summary: Developer files for %{name}
Conflicts: %{realname}-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: aseqmm-devel < %{version}-%{release}
Provides: aseqmm-devel = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{realname}-%{version}%{?svn}
%patch -P0 -p1 -b .implicit-linking
%patch -P1 -p1 -b .gcc6


%build
%cmake 
%cmake_build
doxygen %{_vpath_builddir}/Doxyfile


%install
%cmake_install
mv $RPM_BUILD_ROOT%{_datadir}/mime/packages/{%{realname},%{name}}.xml
# don't include example applications in the compat package
rm -fr $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/icons \
       $RPM_BUILD_ROOT%{_datadir}/man \
       $RPM_BUILD_ROOT%{_datadir}/applications

%files
%doc AUTHORS ChangeLog COPYING
%{_libdir}/libdrumstick-file.so.*
%{_libdir}/libdrumstick-alsa.so.*
%{_datadir}/mime/packages/%{name}.xml

%files devel
%doc doc/html/*
%{_libdir}/libdrumstick-file.so
%{_libdir}/libdrumstick-alsa.so
%{_libdir}/pkgconfig/drumstick-file.pc
%{_libdir}/pkgconfig/drumstick-alsa.pc
%{_includedir}/drumstick/
%{_includedir}/drumstick.h


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0-39
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 22 2024 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.0-37
- Rebuild after unretirement

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jul 31 2021 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-30
- Fix FTBFS

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-28
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-22
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-18
- BR: shared-mime-info

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-17
- Fix FTBFS with GCC 6 (BZ#1307434)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.0-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Nov 16 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-13
- Removed conflicts versioning of devel subpackage
- Specified Requires of devel subpackage

* Fri Nov  7 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-12
- Update the summary of the devel subpackage
- Fix Requires of the devel subpackage

* Mon Oct 27 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-11
- rename to drumstick0

* Tue Oct 21 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-10
- Fork a compat package for Fedora >= 21
- Remove all the example applications
- Other cleanup

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-9
- update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Richard Hughes <richard@hughsie.com> - 0.5.0-7
- Split out the three applications as seporate packages so they are installable
  in the software center.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 11 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.5.0-1
- update to 0.5.0
- drumstick-0.3.1-sysinfo-#597354.patch removed
- drumstick-0.3.1-fix-implicit-linking.patch updated to
  drumstick-0.5.0-fix-implicit-linking.patch
- build the manpages and API documents, BR: docbook-style-xsl /usr/bin/xsltproc
  doxygen

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 28 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.1-2
- sysinfo: don't crash when no timer module available (#597354, upstream patch)

* Fri May 28 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.1-1
- update to 0.3.1
- fix FTBFS due to the strict ld in Fedora >= 13

* Mon Mar 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.0-1
- update to 0.3.0 release

* Mon Feb 08 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.99-0.3.svn20100208
- update from SVN for KMid2 0.2.1

* Sun Jan 31 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.99-0.2.svn20100107
- put the alphatag before the disttag

* Fri Jan 29 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.99-0.1.svn20100107
- update to 0.2.99svn tarball
- renamed from aseqmm to drumstick by upstream

* Fri Jan 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.0-2
- require the main package with exact version-release in -examples

* Fri Jan 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.0-1
- First Fedora package
