Name:    libkdcraw
Summary: A C++ interface around LibRaw library
Version: 24.02.0
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{name}
Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


## upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: cmake(Qt6Gui)
BuildRequires: pkgconfig(libraw) >= 0.15

Requires: kf6-filesystem

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install


%files
%doc AUTHORS
%license LICENSES/*
%{_kf6_libdir}/libKDcrawQt6.so.*
%{_kf6_datadir}/qlogging-categories6/*

%files devel
%{_kf6_libdir}/libKDcrawQt6.so
%{_includedir}/KDcrawQt6/
%{_kf6_libdir}/cmake/KDcrawQt6/


%changelog
* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Tue Dec 26 2023 Marie Loise Nolden <loise@kde.org> - 24.01.85-1	
- 24.01.85
- use libkdcraw again for consistency with qt6/kf6 libraries from gears6
- keep kf5-libkdcraw until all apps are migrated in the meantime

