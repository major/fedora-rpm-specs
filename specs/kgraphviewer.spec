Name:           kgraphviewer
Summary:        Graphviz dot graph file viewer
Version:        24.12.1
Release:        1%{?dist}
# Bit of a mess. README states it's GPLv2+, however the source files
# indicate it's GPLv2. FDL is included in COPYING.DOC, but does not
# apply to anything.
License:        GPL-2.0-only
Url:            https://apps.kde.org/kgraphviewer/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

Requires:       graphviz
Requires:       kf6-filesystem
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  boost-devel
BuildRequires:  graphviz-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)


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
%cmake_kf6
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml
%find_lang %{name} --with-html


%files -f %{name}.lang
%{_kf6_bindir}/kgraphviewer
%{_qt6_plugindir}/kf6/parts/kgraphviewerpart.so 
%{_kf6_datadir}/applications/org.kde.kgraphviewer.desktop
%{_kf6_metainfodir}/org.kde.kgraphviewer.appdata.xml
%{_kf6_datadir}/icons/hicolor
%{_kf6_datadir}/config.kcfg/kgraphviewersettings.kcfg
%{_kf6_datadir}/config.kcfg/kgraphviewer_partsettings.kcfg
%{_kf6_datadir}/qlogging-categories6/kgraphviewer.categories

%files devel
%{_includedir}/kgraphviewer
%{_kf6_libdir}/cmake/KGraphViewerPart
%{_kf6_libdir}/libkgraphviewer.so


%files libs

%{_kf6_libdir}/libkgraphviewer.so.*
%doc AUTHORS
%license COPYING


%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Aug 14 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.07.90-1
- 24.07.90

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 16 2024 Marie Loise Nolden <loise@kde.org> - 2.5.0-1
- 2.5.0 for Qt6/KF6

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
