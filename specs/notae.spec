%global gitcommit c5b97e4020be23e431d53fb3642accc55d36f1c7
%global gitdate 20240409.165252
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:          notae
Version:       0.1~%{gitdate}.%{shortcommit}
Release:       2%{?dist}
License:       CC0-1.0 AND BSD-2-Clause AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause
Summary:       A simple note taking application that automatically saves your work
URL:           https://apps.kde.org/notae/

Source0:       https://invent.kde.org/utilities/%{name}/-/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6KirigamiAddons)

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{gitcommit}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.notae.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSES/*
%{_bindir}/notae
%{_kf6_datadir}/applications/org.kde.notae.desktop
%{_metainfodir}/org.kde.notae.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.notae.svg

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20240409.165252.c5b97e4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jun 17 2024 Steve Cossette <farchord@gmail.com> - 0.1~20240409.165252.c5b97e4
- Initial Release
