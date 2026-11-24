# header-only library
%global debug_package %{nil}

%if 0%{?el8}
# EL8's %%cmake builds in-source by default, which upstream refuses
%undefine __cmake_in_source_build
%endif

Name:           simpleini
Version:        4.25
Release:        %autorelease
Summary:        Cross-platform C++ library to read and write INI-style configuration files
License:        MIT
URL:            https://github.com/brofield/simpleini
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
%if 0%{?el8}
# EL8's gtest 1.8.0 ships no CMake config; CMake's FindGTest module finds it
BuildRequires:  gtest-devel
%else
BuildRequires:  cmake(GTest)
%endif

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
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake -DSIMPLEINI_USE_SYSTEM_GTEST=ON
%cmake_build

%install
%cmake_install
install -pDm644 ConvertUTF.h %{buildroot}%{_includedir}/ConvertUTF.h
install -pDm644 ConvertUTF.c %{buildroot}%{_includedir}/ConvertUTF.c

%check
%ctest

%files devel
%license LICENCE.txt
%doc README.md
%{_includedir}/SimpleIni.h
%{_includedir}/ConvertUTF.h
%{_includedir}/ConvertUTF.c
%{_libdir}/cmake/SimpleIni/

%changelog
%autochangelog
