Name:    kosmindoormap
Version: 23.08.2
Release: 1%{?dist}
Summary: OSM multi-floor indoor map renderer

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND MIT AND ODbL-1.0
URL:     https://invent.kde.org/libraries/%{name}

Source0: https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)

BuildRequires:  zlib-devel
BuildRequires:  cmake(KOpeningHours)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  osmctools
BuildRequires:  rsync
BuildRequires:  protobuf-devel
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KPublicTransport)

Requires:       kf5-filesystem

%description
A library and QML component for rendering multi-level OSM indoor
maps of for example a (large) train station.

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
%{_kf5_libdir}/libKOSM.so.*
%{_kf5_libdir}/libKOSMIndoorMap.so.*
%{_qt5_qmldir}/org/kde/kosmindoormap/
%{_datadir}/qlogging-categories5/org_kde_kosmindoormap.categories

%files devel
%{_includedir}/KOSM/Datatypes
%{_includedir}/KOSM/Element
%{_includedir}/KOSMIndoorMap/
%{_includedir}/kosm/
%{_includedir}/kosmindoormap/
%{_includedir}/kosmindoormap_version.h
%{_kf5_libdir}/cmake/KOSMIndoorMap/
%{_kf5_libdir}/libKOSM.so
%{_kf5_libdir}/libKOSMIndoorMap.so

%changelog
* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
