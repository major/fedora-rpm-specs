Name:           massif-visualizer
Summary:        Visualizer for Massif heap memory profiler data files
Version:        0.7.0
Release:        10%{?dist}
License:        GPL-2.0-or-later
URL:            https://cgit.kde.org/%{name}.git
Source0:        http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz

Requires:       kf5-filesystem

BuildRequires:  kf5-rpm-macros
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KChart) >= 2.6.0
%if 0%{?fedora}
BuildRequires:  cmake(KGraphViewerPart) >= 2.3.90
%endif
BuildRequires:  shared-mime-info

%description
Massif Visualizer is a tool that visualizes massif data.

You run your application in Valgrind with "--tool=massif" and then open the
generated "massif.out.<pid>" in the visualizer. Gzip or Bzip2 compressed massif
files can also be opened transparently.


%prep
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/*.desktop
%find_lang %{name} --with-kde


%files -f %{name}.lang
%{_kf5_bindir}/massif-visualizer
%{_kf5_datadir}/mime/packages/massif.xml
%{_kf5_datadir}/applications/org.kde.massif-visualizer.desktop
%{_kf5_datadir}/config.kcfg/massif-visualizer-settings.kcfg
%{_kf5_datadir}/icons/hicolor
%{_kf5_datadir}/kxmlgui5/massif-visualizer
%{_kf5_datadir}/massif-visualizer/icons/hicolor/22x22/actions/shortentemplates.png
%{_kf5_metainfodir}/org.kde.massif-visualizer.appdata.xml
%license COPYING
%doc AUTHORS


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.7.0-1
- Update to 0.7.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.4.0-13
- update URL

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-8
- update URL (#1325300)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 10 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4.0-4
- BR kgraphviewer
- Fix ARM build

* Tue Feb 10 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4.0-3
- Update desktop database (Zbigniew Jędrzejewski-Szmek, rh #1190055)
- Fix license tag (Zbigniew Jędrzejewski-Szmek, rh #1190055)

* Fri Feb 06 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4.0-2
- Streamline BRs
- Fix %%license tag

* Thu Feb 05 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4.0-1
- Initial packaging
