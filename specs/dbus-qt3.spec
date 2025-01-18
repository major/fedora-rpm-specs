
# fedora package review: http://bugzilla.redhat.com/429760

%define qt3pkg qt
%if 0%{?fedora} > 8
%define qt3pkg qt3
%endif

Name:    dbus-qt3
Summary: Qt3 DBus Bindings
Version: 0.9
Release: 38%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url:     http://www.freedesktop.org/wiki/Software/DBusBindings
Source0: http://people.freedesktop.org/~krake/dbus-1-qt3/dbus-1-qt3-%{version}.tar.gz

Patch0:  dbus-1-qt3-0.9-libtool-aarch64.patch
Patch1:  dbus-qt3-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: dbus-devel
BuildRequires: %{qt3pkg}-devel
BuildRequires: make

Provides: dbus-1-qt3 = %{version}-%{release}

%description
This library provides Qt3-classes for accessing the DBus.

%package devel
Summary: Development files for %{name} 
Provides: dbus-1-qt3-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: dbus-devel
Requires: %{qt3pkg}-devel
Requires: pkgconfig
%description devel
%{summary}.


%prep
%setup -q -n dbus-1-qt3-%{version}
%patch -P0 -p1 -b .libtool-aarch64
%patch -P1 -p1 -b .configure-c99


%build


%configure \
  --disable-static \
  --disable-warnings

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%ldconfig_scriptlets



%files
%doc README AUTHORS ChangeLog COPYING
%{_libdir}/lib*.so.*

%files devel
%{_bindir}/dbusxml2qt3
%{_libdir}/lib*.so
%{_includedir}/dbus-1.0/qt3/
%{_libdir}/pkgconfig/dbus-1-qt3.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9-37
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec  2 2022 Florian Weimer <fweimer@redhat.com> - 0.9-31
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.9-22
- Fix aarch64 FTBFS due to libtool not liking the file output on *.so (#1603749)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9-14
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 20 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.9-4
- Upstream generated a new tarball after the fd.o data loss, use that one
- Remove SVN checkout script as nothing has changed since July 2008

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 06 2008 Rex Dieter <rdieter@fedoraproject.org> 0.9-1
- dbus-1-qt3-0.9
- Provides: dbus-1-qt3

* Tue Jun 03 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-1.20080603svn
- 20080603svn snapshot

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8-5
- s/qt-devel/qt3-devel/ (f9+)

* Tue Feb 05 2008 Dennis Gilmore <dennis@ausil.us> 0.8-4
- actually apply the patch
- add second patch from suse

* Tue Feb 05 2008 Dennis Gilmore <dennis@ausil.us> 0.8-3
- apply BRANCH_UPDATE.diff pulled from suse
- patch needed because it changes the opttions to dbusxml2qt3 
- knm  needs the new calls

* Sun Jan 27 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8-2
- Provides: libdbus-1-qt3(-devel)
- fix mixed tabs/spaces
- -devel: %%doc COPYING

* Sat Jan 19 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8-1
- fedora'ize

* Fri Jan 11 2008 - hschaa@suse.de
- add ifdefs to qdbusobjectpath.h (fix_ifdef.patch)

* Wed Jan 09 2008 - dmueller@suse.de
- fix generation of nm introspection (branch update)

* Mon Dec 17 2007 - dmueller@suse.de
- include bugfixes from SVN

* Wed Dec 12 2007 - hschaa@suse.de
- Added packages to PDB

* Fri Nov 30 2007 - hschaa@suse.de
- Initial checkin
