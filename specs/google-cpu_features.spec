# Unsupported
# https://github.com/google/cpu_features#support
# https://bugzilla.redhat.com/show_bug.cgi?id=1997167
ExcludeArch: s390x

Name:    google-cpu_features
Version: 0.10.1
Release: %autorelease
Summary: A cross-platform C library to retrieve CPU features at runtime
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL:     https://github.com/google/cpu_features
Source0: https://github.com/google/cpu_features/archive/v%{version}/cpu_features-%{version}.tar.gz

Patch0:  google-cpu_features-unbundle_gtest.patch
Patch1:  google-cpu_features-create_soname.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
Buildrequires: gmock-devel
BuildRequires: gtest-devel
BuildRequires: make

%description
A cross-platform C library to retrieve CPU features at runtime.

%package devel
Summary: %{name} headers and development-related files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name} headers and development-related files, CMake config files.

%prep
%autosetup -n cpu_features-%{version} -p1

%build
%cmake \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCPUFEATURES_VERSION_MAJOR:STRING=0 \
 -DCPUFEATURES_VERSION:STRING=0.10 \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DBUILD_PIC:BOOL=ON -DBUILD_TESTING:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest -- -VV

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/list_cpu_features
%{_libdir}/libcpu_features.so.0.10
%{_libdir}/libcpu_features.so.0

%files devel
%{_libdir}/libcpu_features.so
%{_includedir}/cpu_features/
%{_libdir}/cmake/CpuFeatures/

%changelog
%autochangelog
