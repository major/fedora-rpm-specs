
%global qt_module qtlottie

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif

Summary: Qt6 - Lottie Animation
Name:    qt6-%{qt_module}
Version: 6.4.0
Release: 1%{?dist}

License: GPLv3
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: openssl-devel

%description
Qt Lottie Animation provides a QML API for rendering graphics and animations
that are exported in JSON format by the Bodymovin plugin for Adobe After
Effects.

%package devel
Summary: Development files for %{name}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6

%cmake_build

%install
%cmake_install


%files
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6Bodymovin.so*
%{_qt6_qmldir}/Qt/labs/lottieqt/

%files devel
%dir %{_qt6_libdir}/cmake/Qt6BodymovinPrivate
%dir %{_qt6_headerdir}/QtBodymovin
%{_qt6_headerdir}/QtBodymovin
%{_qt6_libdir}/libQt6Bodymovin.so
%{_qt6_libdir}/libQt6Bodymovin.prl
%{_qt6_libdir}/cmake/Qt6BodymovinPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLottieTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6lottieqtplugin*.cmake
%{_qt6_datadir}/modules/*.json
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/metatypes/qt6*_metatypes.json


%changelog
* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 6.4.0-1
- 6.4.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.1-1
- 6.3.1

* Wed Apr 13 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.0-1
- 6.3.0

* Fri Feb 25 2022 Jan Grulich <jgrulich@redhat.com> - 6.2.3-2
- Enable s390x builds

* Mon Jan 31 2022 Jan Grulich <jgrulich@redhat.com> - 6.2.3-1
- 6.2.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.2-1
- 6.2.2

* Fri Oct 29 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.1-1
- 6.2.1

* Thu Sep 30 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0-1
- 6.2.0

* Mon Sep 27 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc2-1
- 6.2.0 - rc2

* Sat Sep 18 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc-1
- 6.2.0 - rc

* Mon Sep 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~beta4-1
- 6.2.0 - beta4

* Thu Aug 12 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.2-1
- 6.1.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.1
- 6.1.1
