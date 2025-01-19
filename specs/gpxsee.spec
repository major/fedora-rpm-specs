%global appname GPXSee

Name:           gpxsee
Version:        13.32
Release:        2%{?dist}
Summary:        GPS log file viewer and analyzer

License:        GPL-3.0-only
URL:            https://www.gpxsee.org/

Source0:        https://github.com/tumic0/%{appname}/archive/%{version}/%{appname}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  make

Recommends:     qt5-qtpbfimageformat


%description
GPS log file viewer and analyzer with support for
GPX, TCX, KML, FIT, IGC and NMEA files.


%prep
%autosetup -p1 -n %{appname}-%{version}


%build
lrelease-qt5 %{name}.pro
%{qmake_qt5} PREFIX=/usr %{name}.pro
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

# localization
%find_lang %{name} --with-qt

%check
# appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%license licence.txt
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CRS/
%{_datadir}/%{name}/maps/
%{_datadir}/%{name}/symbols/
%dir %{_datadir}/%{name}/translations
%{_datadir}/icons/*/*/*/%{name}.*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 13.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 24 2024 Packit <hello@packit.dev> - 13.32-1
- Update to version 13.32
- Resolves: rhbz#2328542

* Fri Nov 22 2024 Packit <hello@packit.dev> - 13.31-1
- Update to version 13.31
- Resolves: rhbz#2327962

* Wed Nov 20 2024 Packit <hello@packit.dev> - 13.30-1
- Update to version 13.30
- Resolves: rhbz#2327738

* Mon Nov 18 2024 Packit <hello@packit.dev> - 13.29-1
- Update to version 13.29
- Resolves: rhbz#2326976

* Mon Nov 18 2024 Packit <hello@packit.dev> - 13.28-1
- Update to version 13.28
- Resolves: rhbz#2324059

* Mon Sep 23 2024 Packit <hello@packit.dev> - 13.26-1
- Update to version 13.26
- Resolves: rhbz#2313510

* Mon Sep 09 2024 Packit <hello@packit.dev> - 13.24-1
- Update to version 13.24
- Resolves: rhbz#2300397

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Packit <hello@packit.dev> - 13.22-1
- Update to version 13.22
- Resolves: rhbz#2283078

* Sat Apr 20 2024 Packit <hello@packit.dev> - 13.19-1
- Update to version 13.19
- Resolves: rhbz#2256623

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Packit <hello@packit.dev> - 13.13-1
- Increase the default pixmap cache size on Android to 384MB (Martin Tůma)
- Fixed broken map scale (ruler) on HiDPI maps (Martin Tůma)
- Limit the overzoom by the resulting tile size rather than number of levels (Martin Tůma)
- Version++ (Martin Tůma)
- Resolves rhbz#2255189

* Tue Dec 12 2023 Packit <hello@packit.dev> - 13.12-1
- Code cleanup (Martin Tůma)
- Fixed broken TMS maps rendering (Martin Tůma)
- Asynchronous rendering of online vector maps (Martin Tůma)
- Added support for online vector maps overzoom (Martin Tůma)
- Limit the overzoom to max 3 levels (Martin Tůma)
- Added support for MVT overzoom (Martin Tůma)
- Code cleanup (Martin Tůma)
- Provide the zoom level to QImageReader when fetching the tile size (Martin Tůma)
- Cosmetics (Martin Tůma)
- Added workaround for broken Qt SVG image plugin colliding with the MVT plugin (Martin Tůma)
- Translated using Weblate (Ukrainian) (Vadym Nekhai)
- Translated using Weblate (Esperanto) (Nikolay Korotkiy)
- Translated using Weblate (Ukrainian) (Nikolay Korotkiy)
- Translated using Weblate (Russian) (Nikolay Korotkiy)
- Translated using Weblate (Finnish) (Nikolay Korotkiy)
- Fixed possible double delete (Martin Tůma)
- Improved error reporting (Martin Tůma)
- Fixed crash on empty MBTiles files (Martin Tůma)
- Version++ (Martin Tůma)
- Metadata update (Martin Tůma)
- Translated using Weblate (Catalan) (raf)
- Translated using Weblate (Hungarian) (99 efi)
- Translated using Weblate (Swedish) (bittin1ddc447d824349b2)
- Code cleanup (Martin Tůma)
- Resolves rhbz#2231722

* Wed Oct 11 2023 Packit <hello@packit.dev> - 13.9-1
- Fixed storing of WMTS tiles with file system incompatible tile matrix names (Martin Tůma)
- Decreased map zoom level treshold to 80% (Martin Tůma)
- Fixed map resolution computation for maps > world/2 (Martin Tůma)
- Use OpenSSL v3 for Windows Qt6 builds (Martin Tůma)
- Fixed Qt6 build (Martin Tůma)
- Yet another TrekBuddy compatability enhancement & fixes + related map API refactoring (Martin Tůma)
- Check for bounds overflow in the computed/approximated case (Martin Tůma)
- Support all variants of TrekBuddy maps/atlases (Martin Tůma)
- Allow arbitrary .map file names in TrekBuddy TAR maps (Martin Tůma)
- Contiguous zones (Martin Tůma)
- Distinguish silos and tanks (Martin Tůma)
- Version++ (Martin Tůma)
- Refactoring (Martin Tůma)
- Reference the exact S-57 document describing the catalogue (Martin Tůma)
- Less aggressive anchor/no-anchor lines (Martin Tůma)

* Mon Jul 31 2023 Packit <hello@packit.dev> - 13.5-1
- Yet another one-way arrows improvement (Martin Tůma)
- Use less agressive one-way street arrows (Martin Tůma)
- Properly mark one-way streets in data from NET links (Martin Tůma)
- Display one-way streets info in IMG maps (Martin Tůma)
- Build universal x86_64/arm64 binaries on OS X (Martin Tůma)
- Yet another ENV path fix (Martin Tůma)
- Fixed ENV file path (Martin Tůma)
- Switched to MSVC 2022 and Qt 6.5 (Martin Tůma)
- Do not affect the map object scaling when resizing the tiles (Martin Tůma)
- Removed obsolete include (Martin Tůma)
- Added graph pinch zooming (Martin Tůma)
- Revert "Removed SDK/buildtools workaround" (Martin Tůma)
- Removed SDK/buildtools workaround (Martin Tůma)
- Code cleanup (Martin Tůma)
- Version++ (Martin Tůma)
- Make the Mapsforge tiles sufficient large for the layout (Martin Tůma)
- Back to Qt 6.4 on Windows (Martin Tůma)
- Switched Qt 6 CI builds to Qt 6.5 (Martin Tůma)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Packit <hello@packit.dev> - 12.3-1
- Added currents rendering (Martin Tůma)
- Render masts as pylons (Martin Tůma)
- Label sizes adjustment (Martin Tůma)
- Properly crop the image (Martin Tůma)
- Various ENC rendering improvements (Martin Tůma)
- Translated using Weblate (Catalan) (raf)
- A better point items layout algorithm (Martin Tůma)
- A better "entry prohibited" line (Martin Tůma)
- Added fog signals rendering (Martin Tůma)
- Render lights merged with the root objects, not as separate objects (Martin Tůma)
- Translated using Weblate (Norwegian Bokmål) (ovl-1)
- Removed duplicit map error debug output (Martin Tůma)
- Properly chceck for GCS/PCS files (Martin Tůma)
- Do not try to load the style when it does not exist (Martin Tůma)
- Version++ (Martin Tůma)
- Render international border lines (Martin Tůma)
- Fixed header length check (Martin Tůma)
- Added missing nmea serial port baudrate setting (Martin Tůma)
- Translated using Weblate (Esperanto) (Nikolay Korotkiy)
- Translated using Weblate (Ukrainian) (Nikolay Korotkiy)
- Translated using Weblate (Russian) (Nikolay Korotkiy)
- Translated using Weblate (Finnish) (Nikolay Korotkiy)
- Translated using Weblate (Chinese (Simplified)) (mtriau)

* Sun Mar 05 2023 Packit <hello@packit.dev> - 12.2-1
- Translated using Weblate (Catalan) (raf)
- Translated using Weblate (Hungarian) (99 efi)
- Translated using Weblate (Turkish) (Oğuz Ersen)
- Translated using Weblate (Swedish) (Åke Engelbrektson)
- Fixed DEM cache size configuration (Martin Tůma)
- Translation update (Martin Tůma)
- Localization update (Martin Tůma)
- Removed unnecessary metadata from icons (Martin Tůma)
- Add outlines to some more marine icons (Martin Tůma)
- Make the DEM cache configurable (Martin Tůma)
- Some more missing outlines (Martin Tůma)
- Decreased the oversize church icon (Martin Tůma)
- Redesigned marine icons (Martin Tůma)
- Fixed build with older Qt versions (Martin Tůma)
- Added support for 0.5" (7201x7201) DEM tiles (Martin Tůma)
- Marine maps draw order fix (Martin Tůma)
- Fixed broken handling of IMG "multi-maps" (maps with overviews) (Martin Tůma)
- Fix multiple MSVC warnings (Martin Tůma)
- Do not compile empty files (Martin Tůma)
- Added "brew update" (Martin Tůma)
- Fixed marine charts rendering (Martin Tůma)
- Do not unnecessary convert the image tiles to pixmaps (Martin Tůma)
- Make the MSVC2019 Debug builds compile (Martin Tůma)
- Version++ (Martin Tůma)
- Remove the qpainter/qimage draw workaround (Martin Tůma)
- Allow arbitrary large images (Martin Tůma)
- Fixed centroid computation (Martin Tůma)

* Fri Feb 24 2023 Nikola Forró <nforro@redhat.com> - 12.1-2
- Add missing changelog entry

* Fri Feb 24 2023 Nikola Forró <nforro@redhat.com> - 12.1-1
- Update to version 12.1
  resolves: #2165119

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Nikola Forró <nforro@redhat.com> - 11.11-1
- Update to version 11.11
  resolves: #2143883

* Sat Nov 12 2022 Nikola Forró <nforro@redhat.com> - 11.8-1
- Update to version 11.8
  resolves: #2141139

* Tue Oct 11 2022 Nikola Forró <nforro@redhat.com> - 11.6-1
- Update to version 11.6
  resolves: #2124119

* Mon Aug 15 2022 Nikola Forró <nforro@redhat.com> - 11.3-1
- Update to version 11.3
  resolves: #2112778

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 11.1-2
- Rebuild (qt5)

* Mon Jun 06 2022 Nikola Forró <nforro@redhat.com> - 11.1-1
- Update to version 11.1
  resolves: #2091675

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 10.7-2
- Rebuild (qt5)

* Mon Apr 25 2022 Nikola Forró <nforro@redhat.com> - 10.7-1
- Update to version 10.7
  resolves: #2069152

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 10.4-2
- Rebuild (qt5)

* Mon Feb 21 2022 Nikola Forró <nforro@redhat.com> - 10.4-1
- Update to version 10.4
  resolves: #2050236

* Mon Jan 24 2022 Nikola Forró <nforro@redhat.com> - 10.2-1
- Update to version 10.2
  resolves: #2043503

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Nikola Forró <nforro@redhat.com> - 10.1-1
- Update to version 10.1
  resolves: #2036485

* Thu Dec 09 2021 Nikola Forró <nforro@redhat.com> - 10.0-1
- Update to version 10.0
  resolves: #2024385

* Tue Nov 23 2021 Nikola Forró <nforro@redhat.com> - 9.12-1
- Update to version 9.12
  resolves: #2024385

* Wed Nov 03 2021 Nikola Forró <nforro@redhat.com> - 9.11-1
- Update to version 9.11
  resolves: #2014008

* Tue Sep 28 2021 Nikola Forró <nforro@redhat.com> - 9.7-1
- Update to version 9.7
  resolves: #2001375

* Tue Aug 31 2021 Nikola Forró <nforro@redhat.com> - 9.5-1
- Update to version 9.5
  resolves: #1996487

* Mon Aug 09 2021 Nikola Forró <nforro@redhat.com> - 9.4-1
- Update to version 9.4
  resolves: #1991362

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Nikola Forró <nforro@redhat.com> - 9.3-1
- Update to version 9.3
  resolves: #1965792

* Tue Apr 20 2021 Nikola Forró <nforro@redhat.com> - 9.0-1
- Update to version 9.0
  resolves: #1942289

* Tue Mar 23 2021 Nikola Forró <nforro@redhat.com> - 8.8-1
- Update to version 8.8
  resolves: #1933598

* Mon Feb 22 2021 Nikola Forró <nforro@redhat.com> - 8.7-1
- Update to version 8.7
  resolves: #1901387

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Nikola Forró <nforro@redhat.com> - 7.36-1
- Update to version 7.36
  resolves: #1896991

* Wed Oct 28 2020 Nikola Forró <nforro@redhat.com> - 7.35-1
- Update to version 7.35
  resolves: #1892219

* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 7.34-2
- Add missing #includes for gcc-11

* Mon Oct 12 2020 Nikola Forró <nforro@redhat.com> - 7.34-1
- Update to version 7.34
  resolves: #1886210

* Wed Sep 23 2020 Nikola Forró <nforro@redhat.com> - 7.32-1
- Update to version 7.32
  resolves: #1880878

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Nikola Forró <nforro@redhat.com> - 7.31-1
- Update to version 7.31
  resolves: #1852674

* Tue Jun 02 2020 Nikola Forró <nforro@redhat.com> - 7.30-1
- Update to version 7.30
  resolves: #1842047

* Mon Apr 20 2020 Nikola Forró <nforro@redhat.com> - 7.29-1
- Update to version 7.29
  resolves: #1825626

* Tue Apr 07 2020 Nikola Forró <nforro@redhat.com> - 7.28-1
- Update to version 7.28
  resolves: #1821027

* Mon Mar 30 2020 Nikola Forró <nforro@redhat.com> - 7.27-1
- Update to version 7.27
  resolves: #1818511

* Thu Mar 05 2020 Nikola Forró <nforro@redhat.com> - 7.25-1
- Update to version 7.25
  resolves: #1810297

* Mon Mar 02 2020 Nikola Forró <nforro@redhat.com> - 7.24-1
- Update to version 7.24
  resolves: #1808914

* Thu Feb 20 2020 Nikola Forró <nforro@redhat.com> - 7.23-1
- Update to version 7.23
  resolves: #1804139

* Thu Feb 13 2020 Nikola Forró <nforro@redhat.com> - 7.22-1
- Update to version 7.22
  resolves: #1802326

* Wed Feb 12 2020 Nikola Forró <nforro@redhat.com> - 7.21-1
- Update to version 7.21
  resolves: #1795072

* Tue Jan 28 2020 Nikola Forró <nforro@redhat.com> - 7.20-1
- Update to version 7.20
  resolves: #1795072

* Tue Jan 14 2020 Nikola Forró <nforro@redhat.com> - 7.19-1
- Update to version 7.19
  resolves: #1790242

* Tue Nov 19 2019 Nikola Forró <nforro@redhat.com> - 7.18-1
- Update to version 7.18
  resolves: #1773117

* Wed Nov 06 2019 Nikola Forró <nforro@redhat.com> - 7.17-1
- Update to version 7.17
  resolves: #1768080

* Tue Oct 29 2019 Nikola Forró <nforro@redhat.com> - 7.16-1
- Update to version 7.16
  resolves: #1766422

* Tue Oct 08 2019 Nikola Forró <nforro@redhat.com> - 7.15-1
- Update to version 7.15
  resolves: #1758792

* Mon Sep 30 2019 Nikola Forró <nforro@redhat.com> - 7.14-1
- Update to version 7.14
  resolves: #1756742

* Mon Sep 02 2019 Nikola Forró <nforro@redhat.com> - 7.13-1
- Update to version 7.13
  resolves: #1748008

* Mon Aug 19 2019 Nikola Forró <nforro@redhat.com> - 7.12-1
- Update to version 7.12
  resolves: #1742109

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Nikola Forró <nforro@redhat.com> - 7.10-1
- Update to version 7.10
  resolves: #1727700

* Tue Jun 18 2019 Nikola Forró <nforro@redhat.com> - 7.9-1
- Update to version 7.9
  resolves: #1720866

* Sun Jun 02 2019 Nikola Forró <nforro@redhat.com> - 7.8-1
- Update to version 7.8
  resolves: #1715247

* Thu May 23 2019 Nikola Forró <nforro@redhat.com> - 7.7-1
- Update to version 7.7
  resolves: #1711584

* Wed May 15 2019 Nikola Forró <nforro@redhat.com> - 7.6-1
- Update to version 7.6
  resolves: #1709052

* Tue Mar 19 2019 Nikola Forró <nforro@redhat.com> - 7.5-1
- Update to version 7.5
  resolves: #1689598

* Tue Mar 12 2019 Nikola Forró <nforro@redhat.com> - 7.4-1
- Update to version 7.4
  resolves: #1687195

* Tue Feb 19 2019 Nikola Forró <nforro@redhat.com> - 7.3-1
- Update to version 7.3
  resolves: #1678584

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Nikola Forró <nforro@redhat.com> - 7.2-1
- Update to version 7.2
  resolves: #1670181

* Thu Dec 20 2018 Nikola Forró <nforro@redhat.com> - 7.0-2
- Use upstream appdata.xml and fix license

* Wed Dec 19 2018 Nikola Forró <nforro@redhat.com> - 7.0-1
- Update to version 7.0

* Wed Nov 14 2018 Nikola Forró <nforro@redhat.com> - 6.3-1
- Update to version 6.3

* Tue Sep 25 2018 Nikola Forró <nforro@redhat.com> - 6.0-1
- Update to version 6.0

* Wed Aug 08 2018 Nikola Forró <nforro@redhat.com> - 5.16-1
- Update to version 5.16
  resolves: #1613850

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Nikola Forró <nforro@redhat.com> - 5.15-1
- Update to version 5.15
  resolves: #1597925

* Mon Jun 25 2018 Nikola Forró <nforro@redhat.com> - 5.14-1
- Update to version 5.14
  resolves: #1594527

* Wed May 30 2018 Nikola Forró <nforro@redhat.com> - 5.13-1
- Update to version 5.13
  resolves: #1583873

* Mon May 28 2018 Nikola Forró <nforro@redhat.com> - 5.12-1
- Update to version 5.12
  resolves: #1582680

* Wed May 16 2018 Nikola Forró <nforro@redhat.com> - 5.11-1
- Update to version 5.11
  resolves: #1578169

* Fri May 11 2018 Nikola Forró <nforro@redhat.com> - 5.10-1
- Update to version 5.10
  resolves: #1576614

* Fri Apr 20 2018 Nikola Forró <nforro@redhat.com> - 5.9-1
- Update to version 5.9
  resolves: #1569761

* Thu Apr 19 2018 Nikola Forró <nforro@redhat.com> - 5.8-1
- Update to version 5.8
  resolves: #1568190

* Tue Apr 10 2018 Nikola Forró <nforro@redhat.com> - 5.6-1
- Update to version 5.6
  resolves: #1565383

* Wed Mar 21 2018 Nikola Forró <nforro@redhat.com> - 5.5-1
- Update to version 5.5
  resolves: #1558277

* Tue Mar 13 2018 Nikola Forró <nforro@redhat.com> - 5.4-1
- Update to version 5.4
  resolves: #1554158

* Mon Mar 05 2018 Nikola Forró <nforro@redhat.com> - 5.3-1
- Update to version 5.3
  resolves: #1550750

* Tue Feb 27 2018 Nikola Forró <nforro@redhat.com> - 5.2-1
- Update to version 5.2
  resolves: #1548602

* Tue Feb 20 2018 Nikola Forró <nforro@redhat.com> - 5.1-2
- Add missing gcc-c++ build dependency

* Tue Feb 13 2018 Nikola Forró <nforro@redhat.com> - 5.1-1
- Update to version 5.1
  resolves: #1544278

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Nikola Forró <nforro@redhat.com> - 4.19-1
- Update to version 4.19
  resolves: #1531971

* Tue Dec 12 2017 Nikola Forró <nforro@redhat.com> - 4.17-1
- Update to version 4.17
  resolves: #1524743

* Fri Oct 20 2017 Nikola Forró <nforro@redhat.com> - 4.16-1
- Update to version 4.16

* Wed Oct 11 2017 Nikola Forró <nforro@redhat.com> - 4.15-2
- Do not buildrequire qt5-devel, qt5-qtbase-devel is sufficient
- Buildrequire qt5-linguist needed for lrelease-qt5

* Tue Oct 10 2017 Nikola Forró <nforro@redhat.com> - 4.15-1
- Initial package
  resolves: #1500524
