Name:    eventviews
Version: 24.01.80
Release: 1%{?dist}
Summary: KDE PIM library for displaying events and calendars

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

Patch0:         24.01.80-kgantt-rename.patch

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KGantt6)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6ConfigWidgets)

BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KPim6CalendarSupport)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6Mime)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KPim6AkonadiCalendar)
Requires:       cmake(KF6CalendarCore)
Requires:       cmake(KPim6CalendarSupport)
Requires:       cmake(KPim6CalendarUtils)
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
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6EventViews.so.*

%files devel
%{_includedir}/KPim6/EventViews/
%{_kf6_libdir}/cmake/KPim6EventViews/
%{_kf6_libdir}/libKPim6EventViews.so


%changelog
* Thu Dec 14 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
