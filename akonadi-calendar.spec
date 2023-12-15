Name:    akonadi-calendar
Version: 24.01.80
Release: 1%{?dist}
Summary: The Akonadi Calendar Library

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(QGpgmeQt6)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6CalendarCore)

BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6MessageCore)
BuildRequires:  cmake(KPim6MessageComposer)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactCore)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KF6TextTemplate)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6AkonadiContactCore)
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KF6CalendarCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/kalendarac
%{_kf6_datadir}/akonadi/plugins/serializer/
%{_kf6_datadir}/dbus-1/services/org.kde.kalendarac.service
%{_kf6_datadir}/knotifications6/kalendarac.notifyrc
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_datadir}/qlogging-categories6/org_kde_kalendarac.categories
%{_kf6_libdir}/libKPim6AkonadiCalendar.so.*
%{_kf6_qtplugindir}/akonadi_serializer_kcalcore.so
%{_kf6_qtplugindir}/kf6/org.kde.kcalendarcore.calendars/libakonadicalendarplugin.so
%{_kf6_sysconfdir}/xdg/autostart/org.kde.kalendarac.desktop


%files devel
%{_includedir}/KPim6/AkonadiCalendar/Akonadi/
%{_includedir}/KPim6/AkonadiCalendar/akonadi-calendar_version.h
%{_includedir}/KPim6/AkonadiCalendar/akonadi/
%{_kf6_libdir}/cmake/KPim6AkonadiCalendar/
%{_kf6_libdir}/libKPim6AkonadiCalendar.so


%changelog
* Wed Dec 13 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
