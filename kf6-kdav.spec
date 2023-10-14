%global gitdate 20231012.021227
%global cmakever 5.240.0
%global commit0 67a6369dec7a17e7c2dd5ff4b8bd9007dd92603a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kdav

Name:    kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary: A DAV protocol implementation with KJobs

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:  https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Gui)

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)

Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
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
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%doc README*
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_libdir}/libKF6DAV.so.6
%{_kf6_libdir}/libKF6DAV.so.5.240.0

%files devel
%{_kf6_includedir}/KDAV/
%{_kf6_libdir}/libKF6DAV.so
%{_kf6_libdir}/cmake/KF6DAV/

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231012.021227.67a6369-1
- Initial release
