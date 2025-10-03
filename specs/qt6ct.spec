%global forgename gitlab
%global forgeurl https://www.opencode.net/trialuser/qt6ct
%global commit 23a985f45cf793ce7ce05811411d2374b4f979c4

%forgemeta

Name:    qt6ct
Version: 0.11
Release: %autorelease
Summary: Qt6 - Configuration Tool

License: BSD-2-Clause
URL:     %{forgeurl}

Source0: %{forgesource}
# https://www.opencode.net/trialuser/qt6ct/-/merge_requests/9
Patch0:  qt6ct-kde.patch
Patch1:  0001-build-refactor-CMake-build-rules.patch
Patch2:  0002-Wrap-forward-declaration-within-QT_NAMESPACE.patch
Patch3:  0003-Revert-Use-KDE-s-QtQuick-QtWidgets-style-bridge.patch

Patch4:  qt6ct-fix-build-against-qt-6-10.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: qt6-qtbase-private-devel
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6IconThemes)

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
This program allows users to configure Qt6 settings (theme, font, icons, etc.)
under DE/WM without Qt integration.

%prep
%forgeautosetup -p1


%build
%cmake -DQT6CT_IN_TREE=ON
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc AUTHORS README.md ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/colors/
%{_datadir}/%{name}/colors/*.conf
%dir %{_datadir}/%{name}/qss/
%{_datadir}/%{name}/qss/*.qss
%exclude %{_libdir}/libqt6ct-common.so
%{_libdir}/libqt6ct-common.so.%{version}
%{_qt6_plugindir}/platformthemes/libqt6ct.so
%{_qt6_plugindir}/styles/libqt6ct-style.so

%changelog
%autochangelog
