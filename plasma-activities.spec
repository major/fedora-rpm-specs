Name:    plasma-activities
Summary: Core components for the KDE Activity concept
Version: 5.91.0
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:     https://invent.kde.org/plasma/%{name}

Source0:    https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
Requires:  kf6-filesystem

# Renamed from kf6-kactivities
Obsoletes:      kf6-kactivities < 1:%{version}-%{release}
Provides:       kf6-kactivities = 1:%{version}-%{release}

# Renamed from kactivities
Obsoletes:      kactivities < 5.27.81

%description
KActivities provides the infrastructure needed to manage a user's activities,
allowing them to switch between tasks, and for applications to update their
state to match the user's current activity. This includes a daemon, a library
for interacting with that daemon, and plugins for integration with other
frameworks.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Obsoletes:      kf6-kactivities-devel < 1:%{version}-%{release}
Provides:       kf6-kactivities-devel = 1:%{version}-%{release}
%description    devel
%{summary}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/plasma-activities-cli6
%{_kf6_datadir}/qlogging-categories6/plasma-activities.categories
%{_kf6_datadir}/qlogging-categories6/plasma-activities.renamecategories
%{_kf6_libdir}/libPlasmaActivities.so.5.*
%{_kf6_libdir}/libPlasmaActivities.so.6
%{_kf6_qmldir}/org/kde/activities/

%files devel
%{_includedir}/PlasmaActivities/
%{_kf6_libdir}/cmake/PlasmaActivities/
%{_kf6_libdir}/libPlasmaActivities.so
%{_kf6_libdir}/pkgconfig/PlasmaActivities.pc


%changelog
* Thu Dec 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.91.0-1
- 5.91.0

* Sun Dec 03 2023 Justin Zobel <justin.zobel@gmail.com> - 5.90.0-1
- Update to 5.90.0

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-kactivities
- 5.27.80

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231009.214418.330a3e2-2
- Rebuild (qt6)

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231009.214418.330a3e2-1
- Initial release
