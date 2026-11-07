%undefine __cmake_in_source_build
%define soversion 0.7

Name:           fcl
Version:        0.7.0
Release:        10%{?dist}
Summary:        Flexible Collision Library


# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/flexible-collision-library/fcl
Source0:        https://github.com/flexible-collision-library/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# patches tests to fix compilation error for tests: -Wtemplate-body
Patch0: 0001-add-cassert.h-to-includes.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  flann-devel
BuildRequires:  gcc-c++
BuildRequires:  libccd-devel
BuildRequires:  octomap-devel
BuildRequires:  tinyxml-devel

%description
FCL is a library for performing three types of proximity queries on a pair
of geometric models composed of triangles.
* Collision detection: detecting whether the two models overlap, and
optionally, all of the triangles that overlap.
* Distance computation: computing the minimum distance between a pair
of models, i.e., the distance between the closest pair of points.
* Tolerance verification: determining whether two models are closer or
farther than a tolerance distance.
* Continuous collision detection: detecting whether the two moving models
overlap during the movement, and optionally, the time of contact.
* Contact information: for collision detection and continuous collision
detection, the contact information (including contact normals and contact
points) can be returned optionally.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p 1

# Remove spurious executable permissions
find . -type f -perm /111 -name "*.h" -print -exec chmod -x '{}' \;
find . -type f -perm /111 -name "*.cpp" -print -exec chmod -x '{}' \;

# Use the distribution's default C++ standard version
sed -i 's/-std=c++11 //g' CMakeModules/CompilerSettings.cmake

%build
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DFCL_NO_DEFAULT_RPATH:BOOL=OFF \
  -DFCL_USE_HOST_NATIVE_ARCH:BOOL=OFF \
  -DFCL_USE_X64_SSE:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
%ctest --output-on-failure || exit 0

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}
%{_datadir}/%{name}

%files devel
%{_includedir}/fcl
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*
%{_libdir}/*.so

%changelog
%autochangelog
