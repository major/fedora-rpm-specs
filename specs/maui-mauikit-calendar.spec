Name:          maui-mauikit-calendar
Version:       4.0.0
Release:       3%{?dist}
License:       GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND GPL-3.0-or-later
Summary:       Calendar support components for Maui applications
URL:           https://invent.kde.org/maui/mauikit-calendar/

# Akonadi has limited arches, and this package depends on it.
# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

Source0:       https://download.kde.org/stable/maui/mauikit-calendar/%{version}/mauikit-calendar-%{version}.tar.xz

# Fix build with 24.08
# https://invent.kde.org/maui/mauikit-calendar/-/merge_requests/4
Patch0:        24.08-fix.patch

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)

BuildRequires: cmake(MauiKit4)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiCalendar)
BuildRequires: cmake(KPim6AkonadiContactCore)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6CalendarUtils)

%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.


%prep
%autosetup -p1 -n mauikit-calendar-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang mauikitcalendar

%files -f mauikitcalendar.lang
%license licenses/*
%{_kf6_qmldir}/org/mauikit/calendar/
%{_kf6_libdir}/libMauiKitCalendar4.so.4
%{_kf6_libdir}/libMauiKitCalendar4.so.%{version}

%files devel
%{_kf6_libdir}/libMauiKitCalendar4.so
%{_includedir}/MauiKit4/Calendar/
%{_kf6_libdir}/cmake/MauiKitCalendar4/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 21 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-2
- Added buildArch restriction as this package depends on akonadi-calendar

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
