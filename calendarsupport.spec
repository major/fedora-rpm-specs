Name:    calendarsupport
Version: 24.01.90
Release: 3%{?dist}
Summary: KDE PIM library for calendar and event handling

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# available only where kf6-pimcommon is
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6PrintSupport)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KF6TextCustomEditor)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Mime)
Requires:       cmake(KPim6IdentityManagementCore)
Requires:       cmake(KPim6AkonadiCalendar)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.


%prep
%autosetup -n %{name}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6CalendarSupport.so.*

%files devel
%{_includedir}/KPim6/CalendarSupport/
%{_kf6_libdir}/cmake/KPim6CalendarSupport/
%{_kf6_libdir}/libKPim6CalendarSupport.so
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 24.01.85-2
- add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 14 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
