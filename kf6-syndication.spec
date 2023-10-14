%global gitdate 20231001.124422
%global cmakever 5.240.0
%global commit0 42914a8a3b45975a09873a1793a5e1f1ff499847
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework syndication

Name:    kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary: The Syndication Library

# Qt-Commercial-exception-1.0 is also found in the LICENSES folder, but is unused except for tests which we don't use anyway
License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6KIO)
Requires:  kf6-filesystem

%description
%{summary}.

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

%files
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Syndication.so.*

%files devel
%{_kf6_includedir}/Syndication/
%{_kf6_libdir}/cmake/KF6Syndication/
%{_kf6_libdir}/libKF6Syndication.so

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.124422.42914a8-1
- Initial release
