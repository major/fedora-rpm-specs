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
Patch:   https://www.opencode.net/trialuser/qt6ct/-/merge_requests/9.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-linguist
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: desktop-file-utils

%description
This program allows users to configure Qt6 settings (theme, font, icons, etc.)
under DE/WM without Qt integration.

%prep
%forgeautosetup -p1


%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc AUTHORS README.md ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_qt6_plugindir}/platformthemes/libqt6ct.so
%{_qt6_plugindir}/styles/libqt6ct-style.so
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/colors/
%{_datadir}/%{name}/colors/*.conf
%dir %{_datadir}/%{name}/qss/
%{_datadir}/%{name}/qss/*.qss
%{_libdir}/libqt6ct-common.so
%{_libdir}/libqt6ct-common.so.%{version}*

%changelog
%autochangelog
