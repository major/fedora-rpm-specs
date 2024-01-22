%global gitdate 20231011.024803
%global cmakever 5.240.0
%global commit0 f7e03a06078abcc277f85f96b5fa5ff3ca1a48bf
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kmoretools

Name:    kf6-%{framework}
Version: 5.246.0
Release: 2%{?dist}
Summary: KDE library to support for downloading application assets from the network

License: BSD-2-Clause and CC0-1.0 and LGPL-2.1-only and LGPL-2.1-or-later and LGPL-3.0-only and LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/libraries/%{framework}
Source0: https://invent.kde.org/libraries/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

Requires:        kf6-filesystem

%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/kf6/kmoretools/presets-kmoretools
%{_kf6_libdir}/libKF6MoreTools.so.5*
%{_kf6_libdir}/libKF6MoreTools.so.6*

%files devel
%{_kf6_includedir}/KMoreTools
%{_kf6_includedir}/kmoretools_version.h
%{_kf6_libdir}/cmake/KF6MoreTools
%{_kf6_libdir}/libKF6MoreTools.so

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.246.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024803.f7e03a0-1
- Initial release
