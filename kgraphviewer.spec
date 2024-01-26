Name:           kgraphviewer
Summary:        Graphviz dot graph file viewer
Version:        2.4.3
Release:        13%{?dist}
# Bit of a mess. README states it's GPLv2+, however the source files
# indicate it's GPLv2. FDL is included in COPYING.DOC, but does not
# apply to anything.
License:        GPL-2.0-only
Url:            https://projects.kde.org/projects/extragear/graphics/kgraphviewer
Source0:        http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

Requires:       graphviz
Requires:       kf5-filesystem
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  boost-devel
BuildRequires:  graphviz-devel
BuildRequires:  zlib-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5IconThemes)


%description
KGraphViewer is a Graphviz dot graph file viewer.


%package libs
Summary:        Graphviz dot graph file viewer library
Requires:       kde-filesystem


%description libs
KGraphViewer is a Graphviz dot graph file viewer for KDE.
This packages contains a library that can be shared by other tools.


%package devel
Summary:        Graphviz dot graph file viewer development files
Requires:       cmake
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
KGraphViewer is a Graphviz dot graph file viewer for KDE
This package contains files useful for software development with
th KGraphViewer library.


%prep
%setup -q


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/*.appdata.xml
%find_lang %{name} --with-html


%files -f %{name}.lang
%{_kf5_bindir}/kgraphviewer
%{_qt5_settingsdir}/kgraphviewer.categories
%{_qt5_plugindir}/kgraphviewerpart.so
%{_kf5_datadir}/kxmlgui5/kgraphviewer
%{_kf5_metainfodir}/org.kde.kgraphviewer.appdata.xml
%{_kf5_datadir}/kgraphviewerpart
%{_kf5_datadir}/kservices5/kgraphviewer_part.desktop
%{_kf5_datadir}/applications/org.kde.kgraphviewer.desktop
%{_kf5_datadir}/icons/hicolor
%{_kf5_datadir}/config.kcfg/kgraphviewersettings.kcfg
%{_kf5_datadir}/config.kcfg/kgraphviewer_partsettings.kcfg


%files devel
%{_includedir}/kgraphviewer
%{_kf5_libdir}/cmake/KGraphViewerPart
%{_kf5_libdir}/libkgraphviewer.so


%files libs
%{_kf5_metainfodir}/org.kde.libkgraphviewer.metainfo.xml
%{_kf5_libdir}/libkgraphviewer.so.*
%doc AUTHORS
%license COPYING


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Sandro Mani <manisandro@gmail.com> - 2.4.3-1
- Update to 2.4.3
- Drop obsolete scriptlets, not needed anymore on F28+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Lubomir Rintel <lkundrak@v3.sk> - 2.4.2-1
- Update to 2.4.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-10
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-8
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.2.0-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 05 2015 Lubomir Rintel <lkundrak@v3.sk> - 2.2.0-2
- Address concerns from the review (Rex Dieter, Mario Blättermann) (rh #1190056)

* Thu Feb 05 2015 Lubomir Rintel <lkundrak@v3.sk> - 2.2.0-1
- Initial packaging
