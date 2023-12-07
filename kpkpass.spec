Name:    kpkpass
Version: 24.01.80
Release: 1%{?dist}
Summary: Library to deal with Apple Wallet pass files

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Archive)

BuildRequires:  qt6-qtbase-devel

BuildRequires:  pkgconfig(shared-mime-info)
%if "%(pkg-config --modversion shared-mime-info 2> /dev/null || echo 2.1)" < "2.2"
%global mime 1
%endif

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/org_kde_%{name}.*
%if 0%{?mime}
%{_kf6_datadir}/mime/packages/application-vnd-apple-pkpass.xml
%endif
%{_kf6_libdir}/libKPim6PkPass.so.*

%files devel
%{_includedir}/KPim6/KPkPass/
%{_kf6_libdir}/libKPim6PkPass.so
%{_kf6_libdir}/cmake/KPim6PkPass/


%changelog
* Tue Dec 5 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
