Name:       kst
Version:    2.0.8
Release:    54%{?dist}
Summary:    A data viewing program

License:    GPL-3.0-only
URL:        http://kst-plot.kde.org/
Source0:    http://downloads.sourceforge.net/%{name}/Kst-%{version}.tar.gz
# Fix calls to set_target_properties in KstMacros.cmake
# https://bugs.kde.org/show_bug.cgi?id=322286
Patch0:     kst-properties.patch
# Upstream patch to fix qreal for arm
# https://bugs.kde.org/show_bug.cgi?id=342642
# https://bugzilla.redhat.com/show_bug.cgi?id=1180348
Patch1:     kst-qreal.patch
Patch2:     kst-gsl21.patch
Patch3:     nest.patch

BuildRequires: gsl-devel cmake
BuildRequires: cfitsio-devel
BuildRequires: pkgconf
%if 0%{?fedora} >= 17
BuildRequires:  netcdf-cxx-devel
%else
BuildRequires:  netcdf-devel
%endif
BuildRequires: getdata-devel muParser-devel
BuildRequires: matio-devel
BuildRequires: desktop-file-utils
BuildRequires: qt4-devel

%description
Kst is a real-time data viewing and plotting tool with basic data analysis 
functionality. Kst contains many powerful built-in features and is 
expandable with plugins and extensions. 

Main features of kst include:
  * Robust plotting of live "streaming" data.
  * Powerful keyboard and mouse plot manipulation.
  * Powerful plugins and extensions support.
  * Large selection of built-in plotting and data manipulation functions, 
    such as histograms, equations, and power spectra.
  * Color mapping and contour mapping capabilities for three-dimensional data.
  * Monitoring of events and notifications support.
  * Filtering and curve fitting capabilities.
  * Convenient command-line interface.
  * Powerful graphical user interface.
  * Support for several popular data formats.
  * Multiple tabs or windows. 

%package docs
Summary:    Documentation for kst
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description docs
Documentation, tutorial, and sample data for kst.

%package devel
Summary:    Development libraries and headers for kst
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries required when building against kst.

%package netcdf
Summary:    netcdf datasource plugin for kst
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description netcdf
A plugin allowing kst to open and read data in netcdf format.

%package fits
Summary:    fits datasource plugin for kst
Requires:   %{name}%{?_isa} = %{version}-%{release}
# Hack because cfitsio won't run if it's internal library version
# doesn't perfectly match between installed library and compiled
# against library.  Meh.
Requires:   cfitsio = %(pkgconf --modversion cfitsio 2>/dev/null || echo "0")

%description fits
A plugin allowing kst to open and read data and images contained within 
fits files. 

%package getdata
Summary:    getdata datasource plugin for kst
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description getdata
A plugin allowing kst to open and read data in getdata (dirfile) format.

%prep
%setup -q -n Kst-%{version}
%patch -P0 -p1 -b .properties
%patch -P1 -p1 -b .qreal
%patch -P2 -p0 -b .gsl21
%patch -P3 -p0 -b .nest

%build
# -Dkst_merge_files=1 is failing for now
# https://bugs.kde.org/show_bug.cgi?id=322289
%cmake -Dkst_merge_files=0 -Dkst_rpath=0 \
  -Dkst_install_prefix=%{_prefix} -Dkst_install_libdir=%{_lib} \
  -Dkst_test=1 -Dkst_release=1 -Dkst_verbose=1
%cmake_build --target kst2

%check
#make test

%install
%cmake_install
rm -f %{buildroot}%{_bindir}/test_*
# omit deprecated kde3-era stuff -- rex
rm -frv %{buildroot}%{_datadir}/{applnk,mimelink}/
%find_lang %{name}_common --with-qt

%ldconfig_scriptlets

%files -f %{name}_common.lang
%doc INSTALL AUTHORS README COPYING COPYING-DOCS COPYING.LGPL 

#binaries
%{_bindir}/kst*
%{_libdir}/libkst*so.*
%dir %{_libdir}/kst2
%dir %{_libdir}/kst2/plugins
%{_libdir}/kst2/plugins/libkst2_dataobject*so
%{_libdir}/kst2/plugins/libkst2_fi*so

%{_datadir}/applications/kst2.desktop
#%{_datadir}/services/kst/kstplugin_*desktop
#%{_datadir}/servicetypes/kst/kst*desktop
#%{_datadir}/apps/kst/kstui.rc
#%{_datadir}/man/man1/kst*

%{_libdir}/kst2/plugins/libkst2_datasource_ascii.so
#%{_datadir}/services/kst/kstdata_ascii.desktop

%{_libdir}/kst2/plugins/libkst2_datasource_qimagesource.so
#%{_datadir}/services/kst/kstdata_qimagesource.desktop

%{_libdir}/kst2/plugins/libkst2_datasource_matlab.so
#%{_datadir}/services/kst/kstdata_matlab.desktop

%{_libdir}/kst2/plugins/libkst2_datasource_sampledatasource.so
#%{_datadir}/services/kst/kstdata_sampledatasource.desktop

%{_libdir}/kst2/plugins/libkst2_datasource_sourcelist.so

#%{_datadir}/config/colors/IDL*

%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/kst2.1.gz

%files devel
%{_libdir}/libkst*a
%{_libdir}/libkst*so

%files docs
#%{_datadir}/apps/kst/tutorial/gyrodata.dat

%files fits
%{_libdir}/kst2/plugins/libkst2_datasource_fitsimage.so
#%{_datadir}/services/kst/kstdata_fitsimage.desktop

%files netcdf
%{_libdir}/kst2/plugins/libkst2_datasource_netcdf.so
#%{_datadir}/services/kst/kstdata_netcdf.desktop

%files getdata
%{_libdir}/kst2/plugins/libkst2_datasource_dirfilesource.so
#%{_datadir}/services/kst/kstdata_dirfilesource.desktop

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-53
- cfitsio rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-51
- matio rebuild

* Thu Mar 07 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-50
- cfistio rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-47
- cfitsio rebuild

* Tue Oct 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-46
- cfitsio rebuild

* Wed Aug 30 2023 Adam Williamson <awilliam@redhat.com> - 2.0.8-45
- Fix cfitsio dependency

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-43
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 2.0.8-41
- Rebuild for cfitsio 4.2

* Sun Aug 28 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.8-40
- Rebuild for new cfitsio

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.8-39
- Rebuild for gsl-2.7.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.8-36
- rebuild for new cfitsio

* Tue Nov 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-35
- getdata rebuild.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-33
- matio rebuild

* Tue Feb 02 2021 Christian Dersch <lupinix@mailbox.org> - 2.0.8-32
- Rebuilt for libcfitsio.so.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.0.8-30
- Matio rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 23 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.8-27
- Rebuild for new cfitsio

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.8-26
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 01 2019 Christian Dersch <lupinix@fedoraproject.org> - 2.0.8-24
- rebuilt for matio soname bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.8-21
- rebuilt for cfitsio 3.450

* Tue Mar 13 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.8-20
- rebuilt (cfitsio)

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.8-19
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.8-17
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 14 2016 Jon Ciesla <limburgher@gmail.com> - 2.0.8-12
- aarch64 rebuild.

* Sat Sep 10 2016 Dan Horák <dan[at]danny.cz> - 2.0.8-11
- Rebuild for getdata 0.9.4

* Fri Jul 01 2016 Jon Ciesla <limburgher@gmail.com> - 2.0.8-10
- matio rebuild.

* Thu Mar 03 2016 Jon Ciesla <limburgher@gmail.com> - 2.0.8-9
- Fix gsl 2.1 build, BZ 1310817.

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.8-8
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.8-6
- Rebuild for netcdf 4.4.0

* Fri Jan 15 2016 Jon Ciesla <limburgher@gmail.com> - 2.0.8-5
- Rebuild for new getdata.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.8-3
- Rebuild for hdf5 1.8.15

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.8-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 14 2015 Orion Poplawski <orion@cora.nwra.com> 2.0.8-1
- Add patch to fix qreal issues on arm (bug #1180348)

* Wed Jan 7 2015 Orion Poplawski <orion@cora.nwra.com> 2.0.8-1
- Update to 2.0.8

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Orion Poplawski <orion@cora.nwra.com> - 2.0.7-6
- Rebuild for cfitsio 3.360

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Jon Ciesla <limburgher@gmail.com> - 2.0.7-4
- Rebuild for new cfitsio.

* Tue Aug 13 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.0.7-3
- fix arm build
- update scriptlets
- tighten subpkg deps
- fix unowned dirs

* Thu Aug 01 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.7-2
- Rebuild to fix broken dep.  This 2.0.7-1 does not
- exist on arm, but the noarch subpackge was copied/tagged there.

* Thu Jul 11 2013 Orion Poplawski <orion@cora.nwra.com> 2.0.7-1
- Update to 2.0.7
- Add BR on matio-devel, ship datasource plugin
- Drop arm patch applied upstream
- Add patch to fix calls to set_target_properties
- spec cleanup
- Rebuild for new cfitsio

* Fri Mar 22 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.6-6
- Rebuild for new cfitsio.

* Wed Mar 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.6-5
- Rebuild for new cfitsio.

* Tue Mar 19 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.6-4
- respin kst-2.0.6-fix-qreal-vs-double-for-arm.patch

* Tue Mar 19 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.6-3
- s/qt-devel/qt4-devel/
- drop extraneous buildrequires
- fix build on arm
- use build options: -Dkst_release=1 -Dkst_verbose=1

* Wed Feb 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.6-2
- Fix cfitsio deps.

* Wed Feb 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.6-1
- Latest upstream.
- Fix Source0, URL.

* Wed Feb 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.3-9
- Rebuild for new cfitsio.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-6
- Rebuild for cfitsio 3.300
- BR netcdf-cxx-devel on Fedora 17+

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-5
- Rebuilt for c++ ABI breakage

* Mon Jan 09 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.3-4
- Rebuild with manual cfitsio hack,

* Fri Jan 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.3-3
- Rebuild for new cfitsio.

* Fri Jun 10 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.3-2
- Rebuild for new cfitsio.

* Wed Jun 01 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.3-1
- Update to 2.0.3 final.

* Fri Feb 18 2011 Matthew Truch <matt at truch.net> - 2.0.3-0.rc1
- Major overhaul to kst2.  

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 5 2010 Matthew Truch <matt at truch.net> - 1.8.0-8
- Bump to pickup new cfitsio.

* Wed Feb 24 2010 Matthew Truch <matt at truch.net> - 1.8.0-7
- Bump to pickup fixed cfitsio.
- Remove packaged fonts (which are unused and packaged incorrectly).

* Fri Feb 12 2010 Matthew Truch <matt at truch.net> - 1.8.0-6
- Hack to work around autotools build issue.
-  Use the libtool in the tarball; do not generate a new one.
- Modify kst-except.diff patch to *not* turn off exceptions in CXXFLAGS

* Wed Nov 25 2009 Orion Poplawski <orion at cora.nwra.com> - 1.8.0-5
- Rebuild for netcdf 4.1.0 and new cfitsio

* Tue Nov 17 2009 Matthew Truch <matt at truch.net> - 1.8.0-4
- Bump to pickup new cfitsio.

* Fri Jul 24 2009 Matthew Truch <matt at truch.net> - 1.8.0-3
- Really fix the patch.  Don't know how it wasn't fixed the first time.

* Fri Jul 24 2009 Matthew Truch <matt at truch.net> - 1.8.0-2
- Fix patch so it doesn't require fuzz.

* Sat Jul 18 2009 Matthew Truch <matt at truch.net> - 1.8.0-1
- Upstream kst 1.8.0
- Drop patch for saveperiod as it's included in upstream 1.8.0
- Separate out getdata support to subpackage (requires getdata)
- Include muParser support for general non-linear fit plugin.
- Bump for mass rebuild.

* Tue Mar 10 2009 Matthew Truch <matt at truch.net> - 1.7.0-6
- Make cfitsio explicit version check work.

* Thu Feb 26 2009 Matthew Truch <matt at truch.net> - 1.7.0-5
- Make documentation noarch.

* Mon Feb 23 2009 Matthew Truch <matt at truch.net> - 1.7.0-4
- Bump for mass rebuild.

* Fri Oct 17 2008 Matthew Truch <matt at truch.net> - 1.7.0-3
- Include patch from upstream to fix savePeriod.

* Fri Sep 19 2008 Matthew Truch <matt at truch.net> - 1.7.0-2
- Allow build from netcdf version 4.  

* Fri Sep 19 2008 Matthew Truch <matt at truch.net> - 1.7.0-1
- Update to upstream 1.7.0.  
- Re-enable ppc64 build of netcdf subpackage.

* Sat May 10 2008 Matthew Truch <matt at truch.net> - 1.6.0-4
- ExcludeArch ppc64 for netcdf subpackage as netcdf is disabled on ppc64.

* Sat May 10 2008 Matthew Truch <matt at truch.net> - 1.6.0-3
- Pick up patch from upstream fixing -F command line option
  Upstream KDE svn revision 805176
  Fixes upstream reported KDE BUG:161766

* Thu Apr 24 2008 Matthew Truch <matt at truch.net> - 1.6.0-2
- Also remove PlanckIDEF datasoure.

* Thu Apr 24 2008 Matthew Truch <matt at truch.net> - 1.6.0-1
- New version of kst.
- Re-add gsl-devel as qt is now compatable with GPLv3.

* Mon Feb 11 2008 Matthew Truch <matt at truch.net> - 1.5.0-3
- Bump release for rebuild.

* Wed Dec 12 2007 Matthew Truch <matt at truch.net> - 1.5.0-2
- Remove BR kdebindings-devel; it is no longer provided for KDE3 in Fedora.
  kst will use its internal kdebindings branch which is older, but should suffice.

* Sun Nov 18 2007 Matthew Truch <matt at truch.net> - 1.5.0-1
- Update to kst 1.5.0 [primarily] bugfix release
- Remove patch to fix open() call; fix was pushed upstream.
- Add autoreconf (and associated BR) as 1.5.0 tarball requires such.

* Tue Nov 13 2007 Matthew Truch <matt at truch.net> - 1.4.0-10
- Remove gsl-devel BuildRequires as gsl is GPLv3+ which is incompatable with qt.

* Sat Nov 10 2007 Matthew Truch <matt at truch.net> - 1.4.0-9
- Bump build to pick up new cfitsio

* Tue Aug 21 2007 Matthew Truch <matt at truch.net> - 1.4.0-8
- Add patch to fix open() call that was not compliant.  

* Thu Aug 2 2007 Matthew Truch <matt at truch.net> - 1.4.0-7
- Update License tag

* Mon Jul 23 2007 Matthew Truch <matt at truch.net> - 1.4.0-6
- Readd kdebindings-devel: KDE4 slipped; will readjust when appropriate.

* Mon Jul 23 2007 Matthew Truch <matt at truch.net> - 1.4.0-5
- kst never needed BR kdebase-devel
- Change BR to kdelibs3-devel for upcoming switch to KDE4 as primary.
- Remove BR kdebindings-devel; kst will use it's internal bindings which
  should suffice until kst 2.0 is released (and switch to KDE4).  
- Fix typo in version of Jesse's changelog entry below from 1.3.0-4 to 1.4.0-4

* Thu Jul 19 2007 Jesse Keating <jkeating@redhat.com> - 1.4.0-4
- Rebuild for new cfitsio

* Tue May 29 2007 Matthew Truch <matt at truch.net> - 1.4.0-3
- Recall that things get installed into %%{buildroot}

* Tue May 29 2007 Matthew Truch <matt at truch.net> - 1.4.0-2
- Remove wmap and scuba2 datasources.  They shouldn't have been included
  in the upstream release.  

* Thu May 17 2007 Matthew Truch <matt at truch.net> - 1.4.0-1
- Update to kst 1.4.0 release.  

* Mon Jan 8 2007 Matthew Truch <matt at truch.net> - 1.3.1-3
- Bump release to pick up newest cfitsio (3.030).

* Fri Jan 5 2007 Matthew Truch <matt at truch.net> - 1.3.1-2
- Include explicit Requires: for cfitsio exact version compiled against.  

* Fri Oct 20 2006 Matthew Truch <matt at truch.net> - 1.3.1-1
- Update to kst 1.3.1 bugfix release.

* Fri Sep 29 2006 Matthew Truch <matt at truch.net> - 1.3.0-2
- Bump release to maintain upgrade path.

* Wed Sep 27 2006 Matthew Truch <matt at truch.net> - 1.3.0-1
- Update to kst 1.3.0 release.

* Mon Aug 28 2006 Matthew Truch <matt at truch.net> - 1.2.1-2
- Bump release to force build in prep. for FC6.

* Thu Mar 23 2006 Matthew Truch <matt at truch.net> - 1.2.1-1
- Update to kst 1.2.1 bugfix release from upstream.

* Sun Mar 12 2006 Matthew Truch <matt at truch.net> - 1.2.0-10
- Yet another tweak to configure options.
- Bump build so new cfitsio version is picked up.

* Sun Feb 26 2006 Matthew Truch <matt at truch.net> - 1.2.0-9
- Improve qt lib and include configure options.

* Sun Feb 26 2006 Matthew Truch <matt at truch.net> - 1.2.0-8
- Bump release due to build issue.

* Sun Feb 26 2006 Matthew Truch <matt at truch.net> - 1.2.0-7
- Teach configure to properly find qt libs and includes.

* Fri Feb 17 2006 Matthew Truch <matt at truch.net> - 1.2.0-6
- Make desktop file appear in proper menu.

* Fri Feb 17 2006 Matthew Truch <matt at truch.net> - 1.2.0-5
- Use a better script for fixing non-relative doc symlinks.
- Install desktop file in proper Fedora location.

* Thu Feb 16 2006 Matthew Truch <matt at truch.net> - 1.2.0-4
- Fix compile flags.
- Take two at fixing non-relative symlinks.  
- Own doc kst directories.

* Wed Feb 15 2006 Matthew Truch <matt at truch.net> - 1.2.0-3
- Fix non-relative symlinks.

* Wed Feb 15 2006 Matthew Truch <matt at truch.net> - 1.2.0-2
- Own all directories.
- Remove redundant build requires.

* Tue Feb 14 2006 Matthew Truch <matt at truch.net> - 1.2.0-1
- Initial fedora specfile for kst based partially on spec file 
  included with kst source.
