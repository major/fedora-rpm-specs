Name:           itinerary
Version:        23.08.2
Release:        1%{?dist}
Summary:        Itinerary and boarding pass management application

License:        Apache-2.0 and BSD-3-Clause and LGPL-2.0-or-later AND CC0-1.0
URL:            https://apps.kde.org/en-gb/itinerary/

Source0:        https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib

# Qt
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Keychain)

# KDE Frameworks
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5UnitConversion)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  qqc2-desktop-style
BuildRequires:  cmake(KF5Prison)
BuildRequires:  cmake(KF5FileMetaData)

# KDE PIM
BuildRequires:  cmake(KPim5PkPass)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KPim5Itinerary)

# KDE Libraries
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(KOSMIndoorMap)
BuildRequires:  cmake(KHealthCertificate)
BuildRequires:  cmake(Quotient)

# Misc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
%summary.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang kde-itinerary
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.itinerary.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f kde-itinerary.lang
%license LICENSES/*
%{_bindir}/itinerary
%{_libdir}/libSolidExtras.so
%{_qt5_plugindir}/kf5/kfilemetadata/kfilemetadata_itineraryextractor.so
%{_qt5_plugindir}/kf5/thumbcreator/itinerarythumbnail.so
%{_qt5_qmldir}/org/kde/solidextras/
%{_datadir}/applications/org.kde.itinerary.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.itinerary.svg
%{_datadir}/knotifications5/itinerary.notifyrc
%{_metainfodir}/org.kde.itinerary.appdata.xml
%{_datadir}/qlogging-categories5/org_kde_itinerary.categories

%changelog
* Sat Oct 14 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
