Name:    akonadi-calendar
Version: 24.12.1
Release: 2%{?dist}
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
BuildRequires:  cmake(KF6Crash)

Obsoletes:      kf5-akonadi-calendar < 24.01.80-1

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6AkonadiContactCore)
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KF6CalendarCore)
Requires:       cmake(KPim6IdentityManagementCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libakonadi-calendar5.po -execdir mv {} libakonadi-calendar6.po \;
find ./po -type f -name libakonadi-calendar5-serializer.po -execdir mv {} libakonadi-calendar6-serializer.po \;


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
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Sun Mar 10 2024 Marie Loise Nolden <loise@kde.org> - 24.02.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90
- Add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-3
- Backport rename translation files

* Sat Dec 16 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Obsoletes the old plasma 5 package

* Wed Dec 13 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
