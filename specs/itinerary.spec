Name:           itinerary
Version:        24.12.0
Release:        2%{?dist}
Summary:        Itinerary and boarding pass management application

License:        Apache-2.0 and BSD-3-Clause and LGPL-2.0-or-later AND CC0-1.0
URL:            https://apps.kde.org/en-gb/itinerary/

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

# Qt
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  qt6-qtbase-private-devel

# KDE Frameworks
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  kf6-qqc2-desktop-style

# KDE PIM
BuildRequires:  cmake(KPim6PkPass)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6Itinerary)

# KDE Libraries
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(KOSMIndoorMap)
BuildRequires:  cmake(KHealthCertificate)
BuildRequires:  cmake(QuotientQt6)

# Misc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

# Runtime requirements
Requires:       qt6-qtlocation
Requires:       qt6-qtmultimedia
Requires:       kf6-kitemmodels
Requires:       kf6-prison

%description
%summary.

%prep
%autosetup

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
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
%{_qt6_plugindir}/kf6/kfilemetadata/kfilemetadata_itineraryextractor.so
%{_qt6_plugindir}/kf6/thumbcreator/itinerarythumbnail.so
%{_qt6_qmldir}/org/kde/solidextras/
%{_datadir}/applications/org.kde.itinerary.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.itinerary.svg
%{_datadir}/knotifications6/itinerary.notifyrc
%{_metainfodir}/org.kde.itinerary.appdata.xml
%{_datadir}/qlogging-categories6/org_kde_itinerary.categories

%changelog
* Tue Dec 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 24.12.0-2
- Drop i686 support beginning with Fedora 42 (leaf package)

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Mon Nov 18 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Mon Nov 18 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-2
- Version bump for Libquotient update

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 24.08.2-2
- Rebuild (qt6)

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 24.02.1-2
- Rebuild (qt6)

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 24.01.95-2
- Rebuild (qt6)

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Mon Dec 18 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Sat Oct 14 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
