Name:           gulrak-filesystem
Version:        1.5.14
Release:        %autorelease
Summary:        Implementation of C++17 std::filesystem for C++11/14/17/20

# SPDX
License:        MIT
URL:            https://github.com/gulrak/filesystem
Source:         %{url}/archive/v%{version}/filesystem-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

# Consider migrating to Catch2 v3
# https://github.com/gulrak/filesystem/issues/165
BuildRequires:  pkgconfig(catch2) < 3

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
This is a header-only single-file std::filesystem compatible helper library,
based on the C++17 and C++20 specs, but implemented for C++11, C++14, C++17 or
C++20 (tightly following the C++17 standard with very few documented
exceptions). It is currently tested on macOS 10.12/10.14/10.15, Windows 10,
Ubuntu 18.04, Ubuntu 20.04, CentOS 7, CentOS 8, FreeBSD 12 and Alpine ARM/ARM64
Linux but should work on other systems too, as long as you have at least a
C++11 compatible compiler. It should work with Android NDK, Emscripten and I
even had reports of it being used on iOS (within sandboxing constraints) and
with v1.5.6 there is experimental support for QNX. The support of Android NDK,
Emscripten and QNX is not backed up by automated testing but PRs and bug
reports are welcome for those too. It is of course in its own namespace
ghc::filesystem to not interfere with a regular std::filesystem should you use
it in a mixed C++17 environment (which is possible).}

%description %{common_description}


%package devel
Summary:        Development files for %{name}

# Header-only library
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n filesystem-%{version}

# Remove bundled Catch library and use the system version
rm -vf test/catch.hpp
sed -r -i 's|(include[[:blank:]]+")(catch.hpp")|\1catch2/\2|' test/*.cpp
sed -r -i 's|[[:blank:]]+catch\.hpp||' test/CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license LICENSE
%doc README.md
%doc examples/

%{_includedir}/ghc/
%{_libdir}/cmake/ghc_filesystem/


%changelog
%autochangelog
