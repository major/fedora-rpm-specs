Name:          francis
Version:       1.1.0
Release:       1%{?dist}
License:       BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Time tracking app for KDE Plasma
URL:           https://apps.kde.org/francis/

Source0:       https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6KirigamiAddons)


%description
Francis is a time tracking app using the well-known
pomodoro technique to help you get more productive.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.francis.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/francis
%{_kf6_datadir}/applications/org.kde.francis.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.francis.svg
%{_metainfodir}/org.kde.francis.metainfo.xml


%changelog
* Sat Mar 2 2024 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- Initial Release
