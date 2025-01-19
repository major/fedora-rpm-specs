%if 0%{?fedora} > 39 || 0%{?rhel} > 9
%global system_qtsingleapplication 1
%endif

Name:           merkaartor
Version:        0.20.0
Release:        4%{?dist}
Summary:        Qt-Based OpenStreetMap editor

# GPL-2.0-or-later: main program
# GPL-3.0-or-later: plugins/background/MCadastreFranceBackground/qadastre
# LGPL-3.0-or-later:
# - src/ImportExport/fileformat.proto
# - src/ImportExport/osmformat.proto
# LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only: src/QToolBarDialog
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only)
URL:            http://www.merkaartor.be
Source0:        https://github.com/openstreetmap/merkaartor/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/openstreetmap/merkaartor/pull/291
Patch0:         merkaartor-0.19.0-CMAKE_INSTALL_LIBDIR.patch
# https://github.com/openstreetmap/merkaartor/pull/292
Patch1:         merkaartor-0.20.0-system-qtsingleapplication.patch

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(proj) >= 6.0.0
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qtchooser
%if 0%{?system_qtsingleapplication}
BuildRequires:  qtsingleapplication-qt6-devel
%else
Provides:       bundled(qtsingleapplication) = 2.6.1
%endif
Requires:       hicolor-icon-theme

%description
Merkaartor is a small editor for OpenStreetMap available under the
GNU General Public License and developed using the Qt toolkit.

It has some unique features like anti-aliased displaying,
transparent display of map features like roads and curved roads.

%prep
%setup -q -n %{name}-%{version}

%patch -P0 -p1 -b .CMAKE_INSTALL_LIBDIR
%patch -P1 -p1 -b .system-qtsingleapplication

%if 0%{?system_qtsingleapplication}
# Use packaged qtsingleapplication instead of bundled version
rm -rfv 3rdparty/qtsingleapplication-2.6_1-opensource
%endif

%build
# ZBAR: zbar is still Qt 5, Merkaartor is now Qt 6
# WEBENGINE: QtWebEngine support is not implemented yet, the flag does nothing
%if 0%{?system_qtsingleapplication}
%global system_qtsingleapplication_cmake ON
%else
%global system_qtsingleapplication_cmake OFF
%endif
%cmake -DZBAR=OFF \
       -DGEOIMAGE=ON \
       -DGPSD=ON \
       -DWEBENGINE=OFF \
       -DUSE_SYSTEM_QTSINGLEAPPLICATION=%{system_qtsingleapplication_cmake}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{name}.desktop
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/org.%{name}.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS CHANGELOG HACKING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libdir}/%{name}/
%{_metainfodir}/org.%{name}.%{name}.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 0.20.0-3
- Rebuild (GDAL)

* Fri Nov 08 2024 Sandro Mani <manisandro@gmail.com> - 0.20.0-2
- Rebuild (gdal)

* Sat Sep 07 2024 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.20.0-1
- Update to 0.20.0, fixes OSM upload by adding OAuth2 support (#2299157)
- Specfile cleanups (remove %%auto* and %%forge* macros, rename patches)
- Rebase system-qtsingleapplication patch
- Use cmake() instead of pkgconfig() for Qt BuildRequires
- Fix missing BuildRequires: cmake(Qt6NetworkAuth)
- Remove obsolete BuildRequires: pkgconfig(QtWebKit)
- Document disabled build options
- System qtsingleapplication-qt6 only available on F40+/EL10+

* Sat Nov 18 2023 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.0-1
- Update to 0.19.0
- Convert to SPDX licensing
- Use pkgconfig
- Use find_lang
- Reformat

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 0.18.4-19
- Rebuild (gdal)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 0.18.4-17
- Rebuild (gdal)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 0.18.4-15
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 0.18.4-14
- Rebuild for proj-9.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 0.18.4-12
- Rebuild (gdal)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 0.18.4-10
- Rebuild (gdal)

* Mon Mar 08 2021 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.18.4-9
- Apply upstream patch to port to proj >= 6 API, fixes FTBFS with proj >= 8

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 0.18.4-8
- Rebuild (proj)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 12:48:08 CET 2020 Sandro Mani <manisandro@gmail.com> - 0.18.4-6
- Rebuild (proj, gdal)
- Fix build against Qt 5.15

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 0.18.4-4
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 0.18.4-3
- Rebuild (gdal)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.18.4-1
- update to 0.18.4, fixes FTBFS (#1736107)
- set SourceURL to a valid URL rather than an unpathed file name

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.18.3-11
- rebuilt (proj)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.18.3-9
- rebuild (exiv2)

* Tue Jan 29 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.18.3-8
- Rebuild for GDAL 2.3.2 (#1650980)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.18.3-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.18.3-2
- rebuild (exiv2)

* Fri Feb 17 2017 Sven Lankes <sven@lank.es> - 0.18.3-1
- new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0.18.2-2
- use %%qmake_Qt6 macro to ensure proper build flags

* Mon Jul 27 2015 Sven Lankes <sven@lank.es> - 0.18.2-1
- new upstream release
- now built against Qt6
- zbar support disabled (zbar is only qt4 for now)
- upstream patch for gdal2.0

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 0.18.1-14
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.18.1-12
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 19 2015 Sven lankes <sven@lank.es> - 0.18.1-11
- rebuild (libproj)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.18.1-8
- fix the ARM fix (#992224) to also do the right thing at runtime

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.18.1-7
- fix FTBFS on arm (#992224)

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.18.1-6
- rebuild (exiv2)

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 0.18.1-5
- Rebuild for gdal 1.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Sven lankes <sven@lank.es> - 0.18.1-1
- new upstream release
- remove upstreamed desktop-file patch

* Tue Jun 05 2012 Sven Lankes <sven@lank.es> - 0.18.0-4
- require hicolor-icon theme (fixes rhbz #768620 - again)

* Mon Jun 04 2012 Sven Lankes <sven@lank.es> - 0.18.0-3
- update icon cache (rhbz #768620)
- Add Education to Desktop category to make desktop-file-validate happy (rhbz  #768616)

* Thu May 31 2012 Sven Lankes <sven@lank.es> - 0.18.0-2
- new upstream release

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.18.0-0.4.git654e49ba
- rebuild (exiv2)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-0.3.git654e49ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.18.0-0.2.git654e49ba
- rebuild (exiv2)

* Sun Feb 20 2011 Sven Lankes <sven@lank.es> - 0.18.0-0.1.git654e49ba
- git snapshot
- no longer depend on boost (fixes FTBFS)

* Sat Feb 12 2011 Sven Lankes <sven@lank.es> - 0.17.2-1
- new upstream bugfix release
- Fixes rhbz #673667 and #674944

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Sven Lankes <sven@lank.es> - 0.17.0-2
- fix source url and versioning

* Tue Dec 28 2010 Sven Lankes <sven@lank.es> - 0.17-1
- new upstream release

* Sun Dec 19 2010 Sven Lankes <sven@lank.es> - 0.17-0.3.rc5
- new upstream prerelease

* Mon Dec 13 2010 Sven Lankes <sven@lank.es> - 0.17-0.2.rc4
- fix build on i686

* Sun Dec 12 2010 Sven Lankes <sven@lank.es> - 0.17-0.1.rc4
- new upstream pre-release
- don't use bundled qtsingleapplication

* Sun Dec 05 2010 Sven Lankes <sven@lank.es> - 0.17-0.1.rc3
- new upstream pre-release
- now includes a plugin for bing maps

* Sun Aug 29 2010 Sven Lankes <sven@lank.es> - 0.16.3-1
- new upstream release
- fixes broken translations

* Sun Aug 15 2010 Sven Lankes <sven@lank.es> - 0.16.2-1
- new upstream release
- add zbar dependency to enable zbar support

* Fri Jul 09 2010 Sven Lankes <sven@lank.es> - 0.16.1-2
- bump to fix broken dep and ftbfs (fixes #599993)

* Tue Jun 15 2010 Sven Lankes <sven@lank.es> - 0.16.1-1
- new upstream release

* Sun Jun 06 2010 Sven Lankes <sven@lank.es> - 0.16.0-1
- new upstream release

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.15-0.3.svn20001 
- rebuild (exiv2)
- BR: qt4-webkit-devel

* Sun Feb 14 2010 Sven Lankes <sven@lank.es> - 0.15-0.2.svn20001
- remove upstreamed src.pro-patch

* Sun Feb 14 2010 Sven Lankes <sven@lank.es> - 0.15-0.1.svn20001
- new svn-prerelease
- build against system boost instead of shipped copy
 
* Sat Feb 13 2010 Sven Lankes <sven@lank.es> - 0.15-0.1.svn19986
- svn-prerelease
- fix DSO induced FTBFS

* Mon Jan 04 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.14-3 
- rebuild (exiv2)

* Thu Dec 10 2009 Sven Lankes <sven@lank.es> - 0.14-2
- Write log to /dev/null unless specified (bz# 544284)

* Wed Aug 12 2009 Sven Lankes <sven@lank.es> - 0.14-1
- 0.14
- Remove patch for gdal/qtgtkstyle-related crash - seems to be fixed in gdal

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-0.2.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 05 2009 Sven Lankes <sven@lank.es> - 0.14-0.1-pre2
- 0.14-pre2

* Thu Jul 02 2009 Sven Lankes <sven@lank.es> - 0.14-0.1-pre1
- 0.14-pre1

* Tue Apr 28 2009 Sven Lankes <sven@lank.es> - 0.13.2-2
- disable use of qgtkstyle until gdal conflict (bz# 498111) is solved

* Sun Apr 26 2009 Sven Lankes <sven@lank.es> - 0.13.2-1
- new upstream release

* Sat Apr 04 2009 Sven Lankes <sven@lank.es> - 0.13.1-1
- new upstream release

* Wed Oct 15 2008 Sven Lankes <sven@lank.es> - 0.12-2
- remove additional source merkaartor.xpm - now included
- minor update of .desktop-file

* Mon Oct 13 2008 Sven Lankes <sven@lank.es> - 0.12-1
- new upstream release
- enable geotagging support (requires exiv2)
- remove -fixes patch

* Wed Sep 10 2008 Sven Lankes <sven@lank.es> - 0.11-3
- add patch from -fixes branch (fixes upload error)

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.11-2
- include unowned directories

* Wed Aug 06 2008 Sven Lankes <sven@lank.es> - 0.11-1
- final 0.11 release 
- Updated versioning scheme - 0.x 

* Mon Jul 28 2008 slankes <sven@lank.es> - 0.0.11-0.1.rc1
- update to release candidate

* Thu Jul 24 2008 slankes <sven@lank.es> - 0.0.10-7
- fix executable source-files

* Wed Jun 25 2008 slankes <sven@lank.es> - 0.0.10-6
- remove superfluous make install from specfile
- tune requires/buildrequires

* Sat Jun 14 2008 slankes <sven@lank.es> - 0.0.10-5
- Remove unneeded buildrequires
- SPEC-Cleanup

* Sun May 18 2008 slankes <sven@lank.es> - 0.0.10-4
- Build in release mode instead of debug. This (among other things) makes merkaartor honour the rpm optflags) 

* Thu May  8 2008 slankes <sven@lank.es> - 0.0.10-3
- Preserve timestamps 

* Sun May  4 2008 slankes <sven@lank.es> - 0.0.10-2
- First package version

