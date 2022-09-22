%global forgeurl https://github.com/hluk/CopyQ/
%global commit bf2d498ebd91df4edeb92cb3709331f3702cfe49

Name:    copyq
Version: 6.3.0
Release: 1%{?dist}
Summary: Advanced clipboard manager
License: GPLv3+

%{forgemeta}

Url:     %{forgeurl}
Source0: %{forgesource}
Source1: %{name}.rpmlintrc
BuildRequires: cmake, extra-cmake-modules, gcc-c++
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils, git
BuildRequires: libXtst-devel, libXfixes-devel
BuildRequires: kf5-knotifications-devel, kf5-rpm-macros,
BuildRequires: qt5-qtbase-devel, qt5-qtbase-private-devel
BuildRequires: qt5-qtsvg-devel, qt5-qtdeclarative-devel
BuildRequires: qt5-qttools-devel, qt5-qtscript-devel
BuildRequires: qwt-qt5-devel, qt5-qtx11extras-devel
BuildRequires: wayland-devel, qt5-qtwayland-devel

%description
CopyQ is advanced clipboard manager with searchable and editable history with
support for image formats, command line control and more.

%prep
%{forgesetup}
chmod 644 %{SOURCE0}
%autosetup -p1 -n %{archivename}
sed -i '/DQT_RESTRICTED_CAST_FROM_ASCII/d' CMakeLists.txt

%build
%cmake_kf5 \
  -Wno-dev \
  -DWITH_QT5:BOOL=ON \
  -DWITH_TESTS:BOOL=ON \
  -DPLUGIN_INSTALL_PREFIX=%{_libdir}/%{name}/plugins \
  -DTRANSLATION_INSTALL_PREFIX:PATH=%{_datadir}/%{name}/locale

%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/com.github.hluk.%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/com.github.hluk.%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS CHANGES.md HACKING README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/metainfo/com.github.hluk.%{name}.appdata.xml
%{_datadir}/applications/com.github.hluk.%{name}.desktop
%{_datadir}/bash-completion/completions/copyq
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/locale/
%{_datadir}/%{name}/themes/
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Sep 18 2022 Gerald Cox <gbcox@member.fsf.org> - 6.3.0-1
- Upstream release: rhbz#2127710

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 6.2.0-2
- Rebuild (qt5)

* Wed Jul 06 2022 Gerald Cox <gbcox@member.fsf.org> - 6.2.0-1
- Upstream release rhbz#2104600

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 6.1.0-3
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 6.1.0-2
- Rebuild (qt5)

* Sat Mar 05 2022 Gerald Cox <gbcox@member.fsf.org> - 6.1.0-1
- Upstream release: rhbz#2061087

* Sun Feb 13 2022 Gerald Cox <gbcox@member.fsf.org> - 6.0.1-3
- Wayland Titlebar Patch rhbz#2053980

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 Gerald Cox <gbcox@member.fsf.org> - 6.0.1-1
- Upstream release rhbz#2036447

* Sat Jan 01 2022 Gerald Cox <gbcox@member.fsf.org> - 6.0.0-1
- Upstream release rhbz#2036447

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-2
- %%build: -Wno-dev (silence dev-only cmake warnings)
- %%build: explicitly mark BOOL options, use ON/OFF consistently
- drop BR: appstream-qt-devel (not used, make epel compatible)

* Thu Sep 30 2021 Gerald Cox <gbcox@member.fsf.org> - 5.0.0-1
- Upstream release rhbz#2009446

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 23 2021 Gerald Cox <gbcox@member.fsf.org> - 4.1.0-1
- Upstream release rhbz#1953017

* Sun Apr 11 2021 Gerald Cox <gbcox@fedoraproject.org> - 4.0.0-1
- Upstream release rhbz#1948314

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.13.0-2
- drop BR: qt5-qtbase-private-devel (#1888764#c10)

* Fri Oct 16 2020 Gerald Cox <gbcox@fedoraproject.org> - 3.13.0-1
- Reverse 3.12.0-6 changes (#1888764)
- Upstream release - rhbz#1888986

* Thu Oct 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.12.0-6
- drop BR: qt5-qtbase-private-devel, minor cleanup (#1888764)

* Thu Oct 15 2020 Gerald Cox <gbcox@fedoraproject.org> - 3.12.0-5
- rhbz#1888764

* Thu Aug 06 2020 Gerald Cox <gbcox@fedoraproject.org> - 3.12.0-4
- rhbz#1863364

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Gerald Cox <gbcox@fedoraproject.org> - 3.12.0-1
- Upstream release rhbz#1856080

* Fri May 08 2020 Gerald Cox <gbcox@fedoraproject.org> - 3.11.1-1
- Upstream release rhbz#1830240

* Fri May 01 2020 Gerald Cox <gbcox@fedoraproject.org>- 3.11.0-1
- Upstream release rhbz#1830240

* Sun Feb 02 2020 Gerald Cox <gbcox@fedoraproject.org>- 3.10.0-1
- Upstream release rhbz#1797335

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.9.3-1
- Upstream release rhbz#1773189

* Tue Oct 22 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.9.2-2
- Add rpmlintrc

* Sun Aug 25 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.9.2-1
- Upstream release rhbz#1742997

* Sun Aug 18 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.9.1-1
- Upstream release rhbz#1742997

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.9.0-1
- Upstream release rhbz#1724540

* Wed Apr 10 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.8.0-1
- Upstream release rhbz#1698544

* Mon Feb 04 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.7.3-2
- Patch for missing tray icon rhbz#1672064

* Sun Feb 03 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.7.3-1
- Upstream release rhbz#1672064

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.7.2-1
- Upstream release rhbz#1662682

* Sun Nov 18 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.7.1-1
- Upstream release rhbz#1651015

* Sun Nov 04 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.7.0-1
- Upstream release rhbz#1645873

* Tue Sep 25 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.6.1-1
- Upstream release rhbz#1632031

* Sun Sep 23 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.6.0-1
- Upstream release rhbz#1632031

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.5.0-1
- Upstream release rhbz#1592132

* Sun Apr 29 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.4.0-1
- Upstream release rhbz#1573011

* Fri Apr 13 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.3.1-1
- Upstream release rhbz#1567094

* Sat Mar 17 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.3.0-1
- Upstream release rhbz#1557681

* Sun Feb 18 2018 Gerald Cox <gbcox@fedoraproject.org> - 3.2.0-1
- Upstream release rhbz#1546543

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.2-2
- Remove obsolete scriptlets

* Sun Oct 22 2017 Gerald Cox <gbcox@fedoraproject.org> - 3.1.2-1
- Upstream release rhbz#1505132

* Thu Sep 28 2017 Gerald Cox <gbcox@fedoraproject.org> - 3.1.1-1
- Upstream release rhbz#1496733

* Thu Sep 28 2017 Gerald Cox <gbcox@fedoraproject.org> - 3.1.0-1
- Upstream release rhbz#1496733

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Gerald Cox <gbcox@fedoraproject.org> - 3.0.3-1
- Upstream release rhbz#1467112

* Sat Jun 03 2017 Gerald Cox <gbcox@fedoraproject.org> - 3.0.2-1
- Upstream release rhbz#1456802

* Tue May 09 2017 Gerald Cox <gbcox@fedoraproject.org> - 3.0.1-1
- Upstream release rhbz#1449207

* Tue Apr 04 2017 Gerald Cox <gbcox@fedoraproject.org> - 3.0.0-1
- Upstream release rhbz#1438781

* Fri Feb 17 2017 Gerald Cox <gbcox@fedoraproject.org> - 2.9.0-1
- Upstream release rhbz#1423475

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Gerald Cox <gbcox@fedoraproject.org> - 2.8.3-1
- Upstream release rhbz#1417607

* Sun Jan 15 2017 Gerald Cox <gbcox@fedoraproject.org> - 2.8.2-1
- Upstream release rhbz#1413359

* Sat Dec 03 2016 Gerald Cox <gbcox@fedoraproject.org> - 2.8.1-1
- Upstream release rhbz#1401190

* Tue Nov 22 2016 Gerald Cox <gbcox@fedoraproject.org> - 2.8.0-1
- Upstream release rhbz#1397608

* Sun Jul 24 2016 Gerald Cox <gbcox@fedoraproject.org> - 2.7.1-3
- Open tray menu on left mouse click rhbz#1359526

* Sat Jul 16 2016 Gerald Cox <gbcox@fedoraproject.org> - 2.7.1-2
- Make translations available rhbz#1357235

* Sun Jun 19 2016 Gerald Cox <gbcox@fedoraproject.org> - 2.7.1-1
- Upstream release rhbz#1347965

* Sun May 1 2016 Gerald Cox <gbcox@fedoraproject.org> - 2.7.0-1
- Upstream release rhbz#1332032

* Sun Feb 14 2016 Gerald Cox <gbcox@fedoraproject.org> - 2.6.1-1
- Upstream releease rhbz#1308340

* Sat Feb 06 2016 Gerald Cox <gbcox@fedoraproject.org> - 2.6.0-1
- Upstream releease rhbz#1305247

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Gerald Cox <gbcox@fedoraproject.org> 2.5.0-1
- Upstream release rhbz#1282017

* Sun Aug 30 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.9-1
- Upstream release rhbz#1258225

* Tue Jul 7 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.8-2
- Upstream release rhbz#1240642

* Tue Jul 7 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.8-1
- Upstream release rhbz#1240642

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 1 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.7-1
- Upstream release rhbz#1227038

* Fri May 8 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.6-6
- Change requirement from Qt4 to Qt5

* Fri May 1 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.6-5
- Deactivate DEBUG messages rhbz#1217874

* Sat Apr 25 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.6-4
- Remove superfluous explicit requires rhbz#1211831

* Fri Apr 24 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.6-3
- Resolve duplicate file warnings, runtime dependencies rhbz#1211831

* Fri Apr 24 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.6-2
- Enable end user testing - http://goo.gl/ue6e2F rhbz#1211831

* Tue Apr 14 2015 Gerald Cox <gbcox@fedoraproject.org> 2.4.6-1
- Initial Build 2.4.6-1 rhbz#1211831
