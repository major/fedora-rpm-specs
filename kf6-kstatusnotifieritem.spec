%global gitdate 20231011.024138
%global cmakever 5.240.0
%global commit0 6035342ec2f4f608fce4172fca6de115279c6b5d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kstatusnotifieritem

Name:           kf6-%{framework}
Version:        %{cmakever}^%{gitdate}.%{shortcommit0}
Release:        1%{?dist}
Summary:        Implementation of Status Notifier Items

License:        CC0-1.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(x11)
BuildRequires:  qt-devel
BuildRequires:  pkgconfig(xkbcommon)
Requires:  kf6-filesystem

%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0}

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install
%find_lang_kf6 kstatusnotifieritem6_qt

%files -f kstatusnotifieritem6_qt.lang
%{_kf6_libdir}/libKF6StatusNotifierItem.so.*
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.StatusNotifierItem.xml
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.StatusNotifierWatcher.xml
%{_kf6_datadir}/qlogging-categories6/kstatusnotifieritem.categories

%files devel
%{_kf6_includedir}/KStatusNotifierItem
%{_kf6_libdir}/cmake/KF6StatusNotifierItem
%{_kf6_libdir}/libKF6StatusNotifierItem.so

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024138.6035342-1
- Initial release
