%global gitdate 20231001.103550
%global cmakever 5.240.0
%global commit0 783d4884024d90b41be45f7c23eee2d0a4c730e3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kcolorscheme

Name:    kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary: Classes to read and interact with KColorScheme
License: BSD-2-Clause and CC0-1.0 and LGPL-2.0-or-later and LGPL-2.1-only and LGPL-3.0-only and LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       kf6-filesystem

%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
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
%find_lang kcolorscheme6 --all-name

%files -f kcolorscheme6.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/kcolorscheme.categories
%{_kf6_libdir}/libKF6ColorScheme.so.5*
%{_kf6_libdir}/libKF6ColorScheme.so.6*

%files devel
%{_kf6_includedir}/KColorScheme
%{_kf6_libdir}/cmake/KF6ColorScheme
%{_kf6_libdir}/libKF6ColorScheme.so

%changelog
* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.103550.783d488-1
- Initial Release
