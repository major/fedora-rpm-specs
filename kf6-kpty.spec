%global gitdate 20231001.123821
%global cmakever 5.240.0
%global commit0 2d5f7cb0e1319f0a8b5ef327f5a83956374f67cf
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kpty

Name:           kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 module providing Pty abstraction

License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:  https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  libutempter-devel
BuildRequires:  qt6-qtbase-devel

Requires:       kf6-filesystem
# runtime calls %%_libexexdir/utempter/utempter
Requires:       libutempter

%description
KDE Frameworks 6 tier 2 module providing Pty abstraction.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
# If seems to, for some reason, not find utempter without the following:
%cmake_kf6 -DUTEMPTER_EXECUTABLE:PATH=/usr/libexec/utempter/utempter
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Pty.so.5*
%{_kf6_libdir}/libKF6Pty.so.6

%files devel
%{_kf6_includedir}/KPty/
%{_kf6_libdir}/libKF6Pty.so
%{_kf6_libdir}/cmake/KF6Pty/

%changelog
* Fri Oct 06 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20231001.123821.2d5f7cb-1
- Initial build
