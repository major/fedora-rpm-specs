
%global qt_module qtvirtualkeyboard

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif

Summary: Qt6 - VirtualKeyboard component
Name:    qt6-%{qt_module}
Version: 6.4.2
Release: 3%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

## upstreamable patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtsvg-devel >= %{version}
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: openssl-devel
BuildRequires: hunspell-devel

# version unknown
Provides: bundled(libpinyin)

%description
The Qt Virtual Keyboard project provides an input framework and reference keyboard frontend
for Qt 6.  Key features include:
* Customizable keyboard layouts and styles with dynamic switching.
* Predictive text input with word selection.
* Character preview and alternative character view.
* Automatic capitalization and space insertion.
* Scalability to different resolutions.
* Support for different character sets (Latin, Simplified/Traditional Chinese, Hindi, Japanese, Arabic, Korean, and others).
* Support for most common input languages, with possibility to easily extend the language support.
* Left-to-right and right-to-left input.
* Hardware key support for 2-way and 5-way navigation.
* Handwriting support, with gestures for fullscreen input.
* Audio feedback.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6

%cmake_build


%install
%cmake_install

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6HunspellInputMethod.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboard.so.6*
%{_qt6_plugindir}/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_qt6_qmldir}/QtQuick/VirtualKeyboard/

%files devel
%{_qt6_headerdir}/QtHunspellInputMethod/
%{_qt6_headerdir}/QtVirtualKeyboard/
%{_qt6_libdir}/libQt6HunspellInputMethod.prl
%{_qt6_libdir}/libQt6HunspellInputMethod.so
%{_qt6_libdir}/libQt6VirtualKeyboard.prl
%{_qt6_libdir}/libQt6VirtualKeyboard.so
%{_qt6_libdir}/cmake/Qt6/
%{_qt6_libdir}/cmake/Qt6HunspellInputMethod/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboard/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtVirtualKeyboardTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6BundledOpenwnn/Qt6BundledOpenwnnDependencies.cmake
%{_qt6_libdir}/cmake/Qt6BundledPinyin/Qt6BundledPinyinDependencies.cmake
%{_qt6_libdir}/cmake/Qt6BundledTcime/Qt6BundledTcimeDependencies.cmake
%{_qt6_libdir}/cmake/Qt6Gui/Qt6QVirtualKeyboardPlugin*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_hunspellinputmethod*.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_virtualkeyboard*.pri
%{_qt6_datadir}/modules/HunspellInputMethod.json
%{_qt6_datadir}/modules/VirtualKeyboard.json
%{_qt6_libdir}/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/*.pc

%files examples
%{_qt6_examplesdir}/


%changelog
* Mon Jan 23 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 6.4.2-3
- Enable the Hunspell input method

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.2-1
- 6.4.2

* Wed Nov 23 2022 Jan Grulich <jgrulich@redhat.com> - 6.4.1-1
- 6.4.1

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
