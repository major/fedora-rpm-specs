%global gitdate 20230901.202319
%global cmakever 5.240.0
%global commit0 fe828b861140534ed728142acf03bd64ca13821e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20221109
%global framework bluez-qt
 
Name:           kf6-%{framework}
Summary:        A Qt wrapper for Bluez
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
 
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://invent.kde.org/frameworks/%{framework}
 
%global versiondir %(echo %{version} | cut -d. -f1-2)
Source0:        https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz
 
BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  kf6-rpm-macros >= %{cmakever}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:	gcc-c++
BuildRequires:  cmake
 
# For %%{_udevrulesdir}
BuildRequires:  systemd
 
Requires:       kf6-filesystem >= %{cmakever}
Recommends:     bluez >= 5
 
%description
BluezQt is Qt-based library written handle all Bluetooth functionality.
 
%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
Development files for %{name}.
 
 
%prep
%autosetup -n %{framework}-%{commit0}
 
 
%build
 %{cmake_kf6} \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
%cmake_build
 
%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_libdir}/libKF6BluezQt.so.*
%{_kf6_qmldir}/org/kde/bluezqt/
 
%files devel
%{_kf6_includedir}/BluezQt/
 
%{_kf6_libdir}/libKF6BluezQt.so
%{_kf6_libdir}/cmake/KF6BluezQt/
%{_kf6_libdir}/pkgconfig/KF6BluezQt.pc
%{_qt6_archdatadir}/mkspecs/modules/qt_BluezQt.pri
 
 
%changelog
* Fri Sep 22 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230901.202319.fe828b8-1
- Initial build
