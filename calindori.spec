%global kf5_min_version 5.88.0

Name:           calindori
Version:        23.03.90
Release:        1%{?dist}
Summary:        Calendar application for Plasma Mobile
License:        GPLv3+ and LGPLv3+ and BSD and CC0
URL:            https://apps.kde.org/%{name}/
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros      >= %{kf5_min_version}
BuildRequires:  libappstream-glib

BuildRequires: cmake(Qt53DRender)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)

BuildRequires: cmake(KF5CalendarCore) >= %{kf5_min_version}
BuildRequires: cmake(KF5Config) >= %{kf5_min_version}
BuildRequires: cmake(KF5DBusAddons) >= %{kf5_min_version}
BuildRequires: cmake(KF5I18n) >= %{kf5_min_version}
BuildRequires: cmake(KF5Kirigami2) >= %{kf5_min_version}
BuildRequires: cmake(KF5Notifications) >= %{kf5_min_version}
BuildRequires: cmake(KF5People) >= %{kf5_min_version}
BuildRequires: cmake(KF5Service) >= %{kf5_min_version}

Requires:       hicolor-icon-theme
Requires:       kf5-kirigami2
Requires:       qt5-qtwayland

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name}
%find_lang calindac
cat %{name}.lang calindac.lang > %{name}-full.lang

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}-full.lang
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf5_datadir}/applications/org.kde.%{name}.desktop

%{_kf5_bindir}/calindac
%{_kf5_datadir}/knotifications5/calindac.notifyrc
%{_kf5_sysconfdir}/xdg/autostart/org.kde.calindac.desktop
%{_kf5_datadir}/dbus-1/services/org.kde.calindac.service

%license LICENSES/*

%changelog
* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- Initial package
