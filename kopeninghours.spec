Name:    kopeninghours
Version: 23.08.2
Release: 1%{?dist}
Summary: Library for parsing and evaluating OSM opening hours expressions

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/libraries/%{name}

Source0: https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  python3-devel
BuildRequires:  boost-devel
Requires:       kf5-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf5_libdir}/libKOpeningHours.so.*
%{_qt5_qmldir}/org/kde/kopeninghours
%{_datadir}/qlogging-categories5/org_kde_kopeninghours.categories
%{python3_sitelib}/PyKOpeningHours/

%files devel
%{_includedir}/KOpeningHours
%{_kf5_libdir}/cmake/KOpeningHours
%{_kf5_libdir}/libKOpeningHours.so
%{_includedir}/kopeninghours
%{_includedir}/kopeninghours_version.h

%changelog
* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
