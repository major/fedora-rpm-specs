%global gitdate 20231001.121632
%global cmakever 5.240.0
%global commit0 8b7a35c3e36b8b1bee37a6957de295db4aa6d32e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kdesu

Name:    kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 integration with su

License: CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:  https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Pty)
#BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel
Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 3 integration with su for elevated privileges.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Pty)
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
%find_lang kdesu6_qt --all-name



%files -f kdesu6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*
%{_kf6_libdir}/libKF6Su.so.*
%{_kf6_libexecdir}/kdesu_stub
%attr(2755,root,nobody) %{_kf6_libexecdir}/kdesud

%files devel
%{_kf6_includedir}/KDESu/
%{_kf6_libdir}/libKF6Su.so
%{_kf6_libdir}/cmake/KF6Su/

%changelog
* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.121632.8b7a35c-1
- Initial Release
