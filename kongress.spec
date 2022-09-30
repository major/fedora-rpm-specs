Name:           kongress
Version:        22.09
Release:        1%{?dist}
License:        CC0 and CC-BY-SA and BSD and GPLv3+
Summary:        A companion application for conferences made by KDE
Url:            https://apps.kde.org/kongress/
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/kongress-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Notifications)

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name
desktop-file-install --dir=%{buildroot}%{_kf5_datadir}/applications/ %{buildroot}/%{_kf5_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%{_kf5_bindir}/%{name}
%{_kf5_bindir}/%{name}ac

%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/dbus-1/services/org.kde.kongressac.service
%{_kf5_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_kf5_datadir}/knotifications5/kongressac.notifyrc

%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

%license LICENSES/*

%changelog
* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 05 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Wed Feb 16 2022 Justin Zobel <justin@1707.io> - 22.02-1
- Update to 22.02, add desktop file install, licenses, license files and gcc-c++ build dependency

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
