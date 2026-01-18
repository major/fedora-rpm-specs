Name:    libkexiv2-qt5
Summary: A wrapper around Exiv2 library
Version: 25.08.3
Release: 3%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/libkexiv2
Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/libkexiv2-%{version}.tar.xz

## upstream patches (master branch)

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(exiv2)

# Renamed from kf5-libkexiv2
Obsoletes: kf5-libkexiv2 < %{version}-%{release}
Provides:  kf5-libkexiv2 = %{version}-%{release}

%global _description %{expand:
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures metadata
as EXIF IPTC and XMP.}

%description %{_description}

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Gui)
Obsoletes: kf5-libkexiv2-devel < %{version}-%{release}
Provides:  kf5-libkexiv2-devel = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -p1 -n libkexiv2-%{version}


%build
%cmake_kf5 -DBUILD_WITH_QT6=OFF
%cmake_build

%install
%cmake_install

%files
%{_kf5_datadir}/qlogging-categories5/*libkexiv2.*
%{_kf5_libdir}/libKF5KExiv2.so.15.0.0
%{_kf5_libdir}/libKF5KExiv2.so.5.1.0

%files devel
%{_kf5_libdir}/libKF5KExiv2.so
%{_kf5_includedir}/KExiv2/
%{_kf5_libdir}/cmake/KF5KExiv2/

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 25.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Nov 16 2025 Steve Cossette <farchord@gmail.com> - 25.08.3-2
- 25.08.3
