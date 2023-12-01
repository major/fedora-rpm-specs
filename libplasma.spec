%global base_name plasma-framework

Name:    libplasma
Version: 5.27.80
Release: 2%{?dist}
Summary: Plasma is the foundation of the KDE user interface (v6)

# LicenseRef-QtCommercial is also in the licenses, but is being omitted as it is optional.
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND Qt-LGPL-exception-1.1
URL:     https://invent.kde.org/plasma/plasma-framework

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Activities)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Solid)
BuildRequires:  openssl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6WaylandClient)

BuildRequires:  wayland-devel
BuildRequires:  kf6-kwayland-devel

Requires:       kf6-filesystem

# Renamed from kf6-plasma
Obsoletes:      kf6-plasma < 1:%{version}-%{release}
Provides:       kf6-plasma = 1:%{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Package)
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6Service)
Requires:       cmake(KF6WindowSystem)
Obsoletes:      kf6-plasma-devel < 1:%{version}-%{release}
Provides:       kf6-plasma-devel = 1:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{base_name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-man --all-name

# create/own dirs
mkdir -p %{buildroot}%{_kf6_datadir}/plasma/plasmoids
mkdir -p %{buildroot}%{_kf6_qmldir}/org/kde/private

%files -f %{name}.lang
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%dir %{_kf6_qmldir}/org/kde/private/
%doc README.md
%lang(lt) %{_datadir}/locale/lt/LC_SCRIPTS/libplasma6/
%license LICENSES/*.txt
%{_kf6_datadir}/plasma/
%{_kf6_datadir}/qlogging-categories6/*plasma*
%{_kf6_libdir}/libKF6Plasma.so.*
%{_kf6_libdir}/libKF6PlasmaQuick.so.*
%{_kf6_plugindir}/kirigami/
%{_kf6_plugindir}/packagestructure
%{_kf6_qmldir}/org/kde/plasma/
%{_kf6_qmldir}/org/kde/kirigami/styles/Plasma/AbstractApplicationHeader.qml
%{_kf6_qmldir}/org/kde/kirigami/styles/Plasma/Icon.qml

%files devel
%dir %{_kf6_datadir}/kdevappwizard/
%{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_includedir}/Plasma/
%{_kf6_includedir}/PlasmaQuick/
%{_kf6_libdir}/cmake/KF6Plasma/
%{_kf6_libdir}/cmake/KF6PlasmaQuick/
%{_kf6_libdir}/libKF6Plasma.so
%{_kf6_libdir}/libKF6PlasmaQuick.so

%changelog
* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 5.27.80-2
- Rebuild (qt6)

* Fri Nov 24 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-plasma
