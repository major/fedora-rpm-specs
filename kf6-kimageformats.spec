%global gitdate 20230925.210237
%global cmakever 5.240.0
%global commit0 d932e0d16b77b180a972df199089d42a5d625194
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%undefine __cmake_in_source_build
%global framework kimageformats

Name:           kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with additional image plugins for QtGui

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:  https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  jasper-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libavif)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt6-qtbase-devel
BuildRequires:	pkgconfig(libjxl) >= 0.7.0
BuildRequires:	pkgconfig(libjxl_threads) >= 0.7.0
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(libraw_r)
BuildRequires:	libxkbcommon-devel

Requires:       kf6-filesystem

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_qtplugindir}/imageformats/*.so

%changelog
* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230925.210237.d932e0d-1
- Initial Release
