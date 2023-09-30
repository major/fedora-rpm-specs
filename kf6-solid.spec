%global gitdate 20230911.192300
%global cmakever 5.240.0
%global commit0 eaebf4a0adc65e4765ce978da1075b2682707d4f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global framework solid

Name:           kf6-%{framework}
Version:        %{cmakever}^%{gitdate}.%{shortcommit0}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 integration module that provides hardware information
License:        LGPL-2.1-or-later AND LGPL-2.1-only AND CCO-1.0 AND BSD-3-Clause AND LGPL-3.0-only
URL:            https://solid.kde.org/
Source0:        https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules >= %{cmakever}
Requires:       kf6-filesystem
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Tools)
BuildRequires:  libupnp-devel
BuildRequires:  systemd-devel
BuildRequires:  flex
BuildRequires:  bison
Recommends:     media-player-info
Recommends:     udisks2
Recommends:     upower

%description
Solid provides the following features for application developers:
 - Hardware Discovery
 - Power Management
 - Network Management

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 solid6_qt

%files -f solid6_qt.lang
%doc README.md TODO
%license LICENSES/*.txt
%{_kf6_bindir}/solid-hardware6
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Solid.so.5.240.0
%{_kf6_libdir}/libKF6Solid.so.6
%{_kf6_qmldir}/org/kde/solid/

%files devel
%{_kf6_archdatadir}/mkspecs/modules/qt_Solid.pri
%{_kf6_includedir}/Solid/
%{_kf6_libdir}/cmake/KF6Solid/
%{_kf6_libdir}/libKF6Solid.so

%changelog
* Tue Sep 19 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230911.192300.eaebf4a-1
- Initial Package
