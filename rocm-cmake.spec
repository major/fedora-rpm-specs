# there is no debug package - this is just cmake modules
%global debug_package %{nil}

%global rocm_release 5.7
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:     rocm-cmake
Version:  %{rocm_version}
Release:  %autorelease
Summary:  CMake modules for common build and dev tasks within the ROCm project
License:  MIT
URL:      https://github.com/radeonopencompute/rocm-cmake
Source:   https://github.com/RadeonOpenCompute/rocm-cmake/archive/refs/tags/rocm-%{version}.tar.gz#/rocm-cmake-rocm-%{version}.tar.gz

BuildArch: noarch
BuildRequires: cmake
Requires: cmake

%description
rocm-cmake is a collection of CMake modules for common build and development
tasks within the ROCm project. It is therefore a build dependency for many of
the libraries that comprise the ROCm platform.

rocm-cmake is not required for building libraries or programs that use ROCm; it
is required for building some of the libraries that are a part of ROCm.


%prep
%autosetup -n rocm-cmake-rocm-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install

rm %{buildroot}/%{_docdir}/rocm-cmake/LICENSE

%files
%doc CHANGELOG.md
%license LICENSE
%{_datadir}/rocm

%changelog
%autochangelog
