Name:    ksanecore
Summary: Library providing logic to interface scanners
Version: 22.12.0
Release: 1%{?dist}

License: BSD and LGPLv2.1-only and LGPLv3.0-only
URL:     https://invent.kde.org/libraries/ksanecore
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Core)
BuildRequires: pkgconfig(sane-backends)

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{version}


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf5_libdir}/libKSaneCore.so.*

%files devel
%{_includedir}/KSaneCore/*
%{_kf5_libdir}/cmake/KSaneCore/*
%{_kf5_libdir}/libKSaneCore.so


%changelog
* Wed Dec 21 2022 Justin Zobel <justin@1707.io> - 22.12.0-1
- Initial inclusion
