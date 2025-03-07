%global appname cmakerc
%global _description %{expand:
CMakeRC is a resource compiler provided in a single CMake script that can
easily be included in another project.

For the purpose of this project, a resource compiler is a tool that will
compile arbitrary data into a program. The program can then read this data
from without needing to store that data on disk external to the program.}

Name: cmrc
Version: 2.0.1
Release: %autorelease

License: MIT
Summary: Standalone CMake-Based C++ Resource Compiler
URL: https://github.com/vector-of-bool/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

# https://github.com/vector-of-bool/cmrc/pull/40
Patch100: %{name}-installation.patch
# https://github.com/vector-of-bool/cmrc/pull/48
Patch101: %{name}-cmake-compatibility.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description %{_description}

%package devel
Summary: Standalone CMake-Based C++ Resource Compiler
Provides: %{appname} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{appname}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel %{_description}

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE.txt
%{_datadir}/cmake/%{appname}/

%changelog
%autochangelog
