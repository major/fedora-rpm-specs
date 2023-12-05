Name:    plasma-activities-stats
Summary: Library to access the usage statistics data collected by the KDE activity manager
Version: 5.90.0
Release: 1%{?dist}

License: CC0-1.0, GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/plasma/%{name}

Source0:    https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Config)
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig

BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtbase-devel

# Renamed from kf6-kactivities-stats
Obsoletes:      kf6-kactivities-stats < 1:%{version}-%{release}
Provides:       kf6-kactivities-stats = 1:%{version}-%{release}

# Renamed from kactivities-stats
Obsoletes:      kactivities-stats < 5.27.81

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
Obsoletes:      kf6-kactivities-stats-devel < 1:%{version}-%{release}
Provides:       kf6-kactivities-stats-devel = 1:%{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc MAINTAINER README.developers TODO
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{name}.*
%{_kf6_libdir}/libPlasmaActivitiesStats.so.1
%{_kf6_libdir}/libPlasmaActivitiesStats.so.5.*

%files devel
%{_includedir}/PlasmaActivitiesStats/
%{_kf6_libdir}/cmake/PlasmaActivitiesStats/
%{_kf6_libdir}/libPlasmaActivitiesStats.so
%{_kf6_libdir}/pkgconfig/PlasmaActivitiesStats.pc

%changelog
* Sun Dec 03 2023 Justin Zobel <justin.zobel@gmail.com> - 5.90.0-1
- Update to 5.90.0

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-kactivities-stats
- 5.27.80

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231007.105021.eae8543-1
- Initial release
