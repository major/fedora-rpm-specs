# header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/brofield/simpleini
Version:        4.22
%forgemeta

Name:           simpleini
Release:        %autorelease
Summary:        Cross-platform C++ library to read and write INI-style configuration files
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(GTest)

%description
simpleini is a cross-platform library that provides a simple API to read and
write INI-style configuration files. It supports data files in ASCII, MBCS and
Unicode. It is designed explicitly to be portable to any platform and has been
tested on Windows, WinCE and Linux. Released as open-source and free using the
MIT licence.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSIMPLEINI_USE_SYSTEM_GTEST=ON

%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENCE.txt
%doc README.md
%dir %{_includedir}/SimpleIni
%{_includedir}/SimpleIni/SimpleIni.h
%{_datadir}/cmake/SimpleIni/

%changelog
%autochangelog
