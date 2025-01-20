#global commit 2cee656cab3867e243483ec75e519012f14949be
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: qmapshack
Version: 1.17.1
Release: 12%{?dist}
Summary: GPS mapping and management tool

# src/animation = WTFPL
License: GPL-2.0-or-later AND GPL-3.0-or-later AND WTFPL
URL: https://github.com/Maproom/qmapshack/wiki
%if 0%{?commit:1}
Source0: https://github.com/Maproom/qmapshack/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0: https://github.com/Maproom/qmapshack/archive/V_%{version}/%{name}-%{version}.tar.gz
%endif

Recommends: routino
Recommends: qmaptool

BuildRequires: gcc-c++
%if 0%{?rhel}
BuildRequires: cmake3
%else
BuildRequires: cmake
%endif
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Script)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(proj)
BuildRequires: cmake(QuaZip-Qt5)
BuildRequires: pkgconfig(gdal)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: routino-devel
BuildRequires: alglib-devel
BuildRequires: desktop-file-utils

# because new dependency on WebEngine
ExclusiveArch: %{qt5_qtwebengine_arches}


%description
QMapShack provides a versatile tool for GPS maps in GeoTiff format as well as
Garmin's img vector map format. You can also view and edit your GPX tracks.
QMapShack is the successor of QLandkarteGT.

Main features:
- use of several work-spaces
- use several maps on a work-space
- handle data project-oriented
- exchange data with the device by drag-n-drop


%package -n qmaptool
Summary: Create raster maps from paper map scans
Recommends: gdal

%description -n qmaptool
This is a tool to create raster maps from paper map scans. QMapTool can be
considered as a front-end to the well-known GDAL package. It complements
QMapShack.


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-V_%{version}
%endif


%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build


%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/qmaptool.desktop

%files
%license LICENSE
%doc changelog.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/QMapShack.*
%{_datadir}/pixmaps/QMapShack.png
%{_datadir}/%{name}/
%{_datadir}/doc/HTML/QMSHelp.q??
%{_mandir}/man1/%{name}.*

%files -n qmaptool
%{_bindir}/qmaptool
%{_bindir}/qmt_*
%{_datadir}/applications/qmaptool.desktop
%{_datadir}/icons/hicolor/*/apps/QMapTool.*
%{_datadir}/pixmaps/QMapTool.png
%{_datadir}/qmaptool/
%{_datadir}/qmt_*/
%{_datadir}/doc/HTML/QMTHelp.q??
%{_mandir}/man1/qmaptool.*
%{_mandir}/man1/qmt_*.*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 22 2024 Sandro Mani <manisandro@gmail.com> - 1.17.1-11
- Rebuild (alglib)

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 1.17.1-10
- Rebuild (GDAL)

* Fri Nov 08 2024 Sandro Mani <manisandro@gmail.com> - 1.17.1-9
- Rebuild (gdal)

* Sun Sep 29 2024 Sandro Mani <manisandro@gmail.com> - 1.17.1-8
- Rebuild (alglib)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 04 2024 Sandro Mani <manisandro@gmail.com> - 1.17.1-6
- Rebuild (alglib)

* Mon May 13 2024 Sandro Mani <manisandro@gmail.com> - 1.17.1-5
- Rebuild (gdal)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Dan Horák <dan@danny.cz> - 1.17.1-2
- Rebuild (alglib)

* Thu Dec 14 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.17.1-1
- Update to 1.17.1 (rhbz#2254510)

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 1.17.0-2
- Rebuild (gdal)

* Fri Jul 21 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.17.0-1
- Update to 1.17.0 (rhbz#2224655)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 23 2023 Sandro Mani <manisandro@gmail.com> - 1.16.1-14
- Rebuild (alglib)

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 1.16.1-13
- Rebuild (gdal)

* Fri May 05 2023 Nicolas Chauvet <kwizart@gmail.com> - 1.16.1-12
- Rebuilt for quazip 1.4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Sandro Mani <manisandro@gmail.com> - 1.16.1-10
- Rebuild (alglib)

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 1.16.1-9
- Rebuild (gdal)

* Sun Oct 30 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.16.1-8
- Add Recommends for gdal to qmaptool (#2138688)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Dan Horák <dan@danny.cz> - 1.16.1-6
- rebuild (alglib)

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 1.16.1-5
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Mon Apr 18 2022 Miro Hrončok <mhroncok@redhat.com> - 1.16.1-4
- Rebuilt for quazip 1.3

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 1.16.1-3
- Rebuild for proj-9.0.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Dan Horák <dan@danny.cz> - 1.16.1-1
- update to 1.16.1 (#2029117)

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 1.16.0-3
- Rebuild (gdal)

* Fri Aug 20 2021 Dan Horák <dan@danny.cz> - 1.16.0-2
- rebuild (alglib)

* Fri Aug 20 2021 Dan Horák <dan@danny.cz> - 1.16.0-1
- update to 1.16.0 (#1995959)

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 1.15.2-10.git2cee656
- Rebuild (quazip)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-9.git2cee656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 1.15.2-8.git2cee656
- Rebuild (gdal)

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 1.15.0-7.git2cee656
- Update to git 2cee656 for proj8 support

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 16:18:23 CET 2020 Sandro Mani <manisandro@gmail.com> - 1.15.0-5
- Rebuild (alglib)

* Wed Nov 11 13:09:42 CET 2020 Sandro Mani <manisandro@gmail.com> - 1.15.0-4
- Rebuild (proj, gdal)
- Add missing BRs
- Fix build against Qt5.15

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Dan Horák <dan@danny.cz> - 1.15.0-1
- update to 1.15.0 (#1751288)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 1.14.0-4
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.14.0-3
- Rebuild (gdal)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Dan Horák <dan@danny.cz> - 1.14.0-1
- update to 1.14.0 (#1751288)
- drop support for RHEL <= 7 - no QtWebEngine there

* Wed Jul 24 2019 Dan Horák <dan@danny.cz> - 1.13.1-7
- update to 1.13.1

* Tue May 14 2019 Dan Horák <dan@danny.cz> - 1.13.0-6
- allow build in F<=30

* Tue Apr 16 2019 Dan Horák <dan@danny.cz> - 1.13.0-5
- update to 1.13.0 (#1697564)

* Sat Feb 23 2019 Sandro Mani <manisandro@gmail.com> - 1.12.3-4
- Rebuild (alglib)

* Sat Feb 09 2019 Dan Horák <dan@danny.cz> - 1.12.3-3
- update to 1.12.3 (#1672366)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Dan Horák <dan@danny.cz> - 1.12.1-1
- update to 1.12.1

* Tue Sep 04 2018 Dan Horák <dan@danny.cz> - 1.12.0-1
- update to 1.12.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Sandro Mani <manisandro@gmail.com> - 1.11.1-2
- Rebuild (alglib)

* Thu Apr 19 2018 Dan Horák <dan@danny.cz> - 1.11.1-1
- update to 1.11.1 (#1569518)

* Mon Mar 12 2018 Dan Horák <dan@danny.cz> - 1.11.0-1
- update to 1.11.0 (#1551560)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Sandro Mani <manisandro@gmail.com> - 1.10.0-2
- Rebuild (alglib)

* Thu Dec 21 2017 Dan Horák <dan@danny.cz> - 1.10.0-1
- update to 1.10.0 (#1528494)

* Mon Sep 18 2017 Dan Horák <dan@danny.cz> - 1.9.1-1
- update to 1.9.1 (#1492506)

* Thu Aug 24 2017 Sandro Mani <manisandro@gmail.com> - 1.9.0-2
- Rebuild (alglib)

* Wed Aug 02 2017 Dan Horák <dan@danny.cz> - 1.9.0-1
- update to 1.9.0 (#1474557)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Dan Horák <dan@danny.cz> - 1.8.1-1
- update to 1.8.1 (#1450653)

* Fri May 12 2017 Sandro Mani <manisandro@gmail.com> - 1.8.0-2
- Rebuild (alglib)

* Mon Mar 27 2017 Dan Horák <dan@danny.cz> - 1.8.0-1
- update to 1.8.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Dan Horák <dan@danny.cz> - 1.7.2-2
- Rebuilt for proj 4.9.3

* Tue Dec 13 2016 Dan Horák <dan[at]danny.cz> - 1.7.2-1
- update to 1.7.2

* Tue Sep 13 2016 Dan Horák <dan[at]danny.cz> - 1.7.1-1
- update to 1.7.1

* Tue Sep 13 2016 Dan Horák <dan[at]danny.cz> - 1.7.0-1
- update to 1.7.0

* Thu Jul 14 2016 Dan Horák <dan[at]danny.cz> - 1.6.3-1
- update to 1.6.3

* Mon Jul 04 2016 Dan Horák <dan[at]danny.cz> - 1.6.2-1
- update to 1.6.2

* Mon Mar 28 2016 Dan Horák <dan[at]danny.cz> - 1.6.1-1
- update to 1.6.1

* Fri Feb 26 2016 Dan Horák <dan[at]danny.cz> - 1.6.0-1
- update to 1.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 22 2015 Dan Horák <dan[at]danny.cz> - 1.5.1-1
- update to 1.5.1

* Thu Nov 12 2015 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- update to 1.4.0

* Mon Jul 27 2015 Dan Horák <dan@danny.cz> - 1.3.0-2
- rebuild for GDAL 2.0

* Thu Jul 02 2015 Dan Horák <dan[at]danny.cz> - 1.3.0-1
- update to 1.3.0

* Wed Jun 24 2015 Dan Horák <dan[at]danny.cz> - 1.2.2-1
- update to 1.2.2
- add missing desktop-database scriptlets
- fix license tag

* Tue Apr 14 2015 Dan Horák <dan[at]danny.cz> - 1.2.0-1
- update to 1.2.0

* Sun Apr 05 2015 Dan Horák <dan[at]danny.cz> - 1.1.0-1
- initial Fedora version
