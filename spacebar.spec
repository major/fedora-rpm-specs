Name:           spacebar
Version:        22.09
Release:        1%{?dist}
License:        GPLv2+ and GPLv3 and GPLv2
Summary:        Messaging app for Plasma Mobile
Url:            https://invent.kde.org/plasma-mobile/spacebar
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel

BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5People)

BuildRequires:  cmake(QCoro5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5QmlModels)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(TelepathyQt5)

BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)

Requires:       hicolor-icon-theme
Requires:       kf5-kirigami2
Requires:       telepathy-mission-control

%description
Spacebar is a telepathy-qt based SMS application that primarily targets Plasma Mobile.

%prep
%autosetup -n spacebar-%{version} -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/{GPL-2.0-or-later,LicenseRef-KDE-Accepted-GPL}.txt
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf5_datadir}/knotifications5/%{name}.notifyrc

%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_libexecdir}/%{name}-daemon
%{_sysconfdir}/xdg/autostart/org.kde.%{name}.daemon.desktop

%changelog
* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Mon Sep 26 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.06-1
- initial version spacebar
