Name:    ktnef
Version: 24.01.85
Release: 1%{?dist}
Summary: The KTNef Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://invent.kde.org/pim/ktnef/-/merge_requests/10
Patch0:         move-translations.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Codecs)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CalendarCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libktnef5.po -execdir mv {} libktnef6.po \;

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Tnef.so.*

%files devel
%{_includedir}/KPim6/KTNEF/
%{_kf6_libdir}/libKPim6Tnef.so
%{_kf6_libdir}/cmake/KPim6Tnef/

%changelog
* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Backport rename translation files

* Mon Dec 11 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
