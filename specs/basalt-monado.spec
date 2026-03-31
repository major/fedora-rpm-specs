%global forgeurl0   https://gitlab.freedesktop.org/mateosss/basalt/
%global commit0     bec83db20507dd044caf1b8a3d7a77e10610239b
%global date        20260325

# Submodules in forgeurl0
%global forgeurl1   https://gitlab.freedesktop.org/mateosss/basalt-headers/
%global commit1     e6db0fb84c69614bc4923fde6c52154c221c1768
%global forgeurl2   https://github.com/laurentkneip/opengv/
%global commit2     91f4b19c73450833a40e463ad3648aae80b3a7f3
%global forgeurl3   https://github.com/strasdat/Sophus/
%global commit3     d0b7315a0d90fc6143defa54596a3a95d9fa10ec
%forgemeta

Name:           basalt-monado
# Upstream versioning is commit based, using soname version
Version:        2.0.1
Release:        %autorelease
Summary:        Visual-Inertial Mapping with Non-Linear Factor Recovery

License:        BSD-3-Clause AND MIT
URL:            %{forgeurl0}

Source0:        %{forgesource0}
# License: BSD-3-Clause
Source1:        %{forgeurl1}/-/archive/%{commit1}/basalt-headers-%{commit1}.tar.bz2
# License: BSD-3-Clause
Source2:        %{forgeurl2}/archive/%{commit2}/opengv-%{commit2}.tar.gz
# License: MIT
Source3:        %{forgeurl3}/archive/%{commit3}/Sophus-%{commit3}.tar.gz

# Allow Eigen3 3.4+ / 5.x (remove EXACT version requirement, extract include
# dir from CMake target, set legacy EIGEN* CACHE variables for bundled projects)
# https://gitlab.freedesktop.org/mateosss/basalt/-/issues/28
Patch0:         basalt-monado-eigen3-version.patch
# Fix ignore_external_warnings(eigen) when system Eigen is used — the bundled
# target is named "eigen" but the system target is "Eigen3::Eigen"
Patch1:         basalt-monado-headers-system-eigen.patch
# Fix opengv's FindEigen.cmake version check for Eigen 3.4+ which moved the
# version macros from Macros.h to Eigen/Version
Patch2:         basalt-monado-opengv-findEigen.patch
# Guard ignore_external_warnings(cereal) — system cereal target is
# "cereal::cereal", not "cereal", so get_target_property() would error
Patch3:         basalt-monado-headers-system-cereal.patch
# Use system CLI11 via find_package instead of the bundled thirdparty copy
Patch4:         basalt-monado-system-cli11.patch
# Use system magic_enum via find_package instead of the bundled thirdparty copy
Patch5:         basalt-monado-system-magic_enum.patch
# Use system GTest via find_package instead of the empty bundled googletest
# submodule (not included in the tarball)
Patch6:         basalt-monado-headers-system-gtest.patch

ExclusiveArch:  aarch64 x86_64

BuildRequires:  boost-devel
BuildRequires:  cereal-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(catch2)
BuildRequires:  pkgconfig(CLI11)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(benchmark)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(magic_enum)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(xkbcommon)

# Best effort commit to version mapping for all thirdparty sources
# https://gitlab.freedesktop.org/mateosss/basalt-headers/
# No upstream versioning, using commit hash as version and it must match
# the git submodule commit in forgeurl0
Provides: bundled(basalt-headers)
# https://github.com/laurentkneip/opengv
# No upstream versioning, using commit hash as version and it must match
# the git submodule commit in forgeurl0
Provides: bundled(opengv)
# https://github.com/strasdat/Sophus
# must match the git submodule commit in forgeurl0
Provides: bundled(sophus) = 1.22.10


%description
This project contains tools for:

Camera, IMU and motion capture calibration.
Visual-inertial odometry and mapping.
Simulated environment to test different components of the system.


%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary:  Development files for Basalt

%description devel
Devel information for Basalt.


%prep
%forgesetup

# Remove bundled FindEigen3.cmake - it fails to detect Eigen 3.4+ which moved
# version macros from Macros.h to Eigen/Version. Use system/Eigen's config instead.
rm cmake_modules/FindEigen3.cmake

# Extract bundled submodule tarballs before applying patches so that patches
# targeting files inside these directories (basalt-headers, opengv) work.
tar -xvf %{SOURCE1} --strip-components 1 -C thirdparty/basalt-headers
tar -xvf %{SOURCE2} --strip-components 1 -C thirdparty/opengv
tar -xvf %{SOURCE3} --strip-components 1 -C thirdparty/basalt-headers/thirdparty/Sophus

# Apply patches after all submodules are extracted
%autopatch -p1


%build
%cmake -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBASALT_BUILTIN_EIGEN=off \
  -DEIGEN_ROOT=%{_includedir}/eigen3 \
  -DBASALT_BUILTIN_CEREAL=off \
  -DBASALT_BUILD_SHARED_LIBRARY_ONLY=on \
  -DBASALT_BUILD_TESTS=on \
  -DBASALT_BUILD_VISUALIZATION=off \

%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md doc/*.md
%{_libdir}/libbasalt.so.2
%{_libdir}/libbasalt.so.2.0.1
%{_datarootdir}/basalt

%files devel
%{_libdir}/libbasalt.so
%{_libdir}/pkgconfig/basalt.pc


%changelog
%autochangelog
