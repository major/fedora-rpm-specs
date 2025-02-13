%global upstreamname rocWMMA
%global rocm_release 6.3
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Testing needs to be done manually

# This is a header only
%global debug_package %{nil}

Name:           rocwmma
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Matrix Multiple and Accumulate library
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-omp-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocWMMA is a C++ library for accelerating mixed-precision matrix
multiply-accumulate (MMA) operations leveraging AMD GPU hardware.
rocWMMA makes it easier to break down MMA problems into fragments
and distribute block-wise MMA operations in parallel across GPU
wavefronts. Our API consists of a header library, that you can
use to compile MMA acceleration directly into GPU kernel device
code. This can benefit from compiler optimization in the
generation of kernel assembly, and doesn't incur additional
overhead costs of linking to external runtime libraries or having
to launch separate kernels.

%package devel
Summary:        Headers for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake \
       -DROCM_SYMLINK_LIBS=OFF \
       -DHIP_PLATFORM=amd \
       -DROCWMMA_BUILD_SAMPLES=FALSE \
       -DROCWMMA_BUILD_TESTS=FALSE

%cmake_build

%install
%cmake_install

%files devel
%dir %{_includedir}/%{name}/
%license LICENSE.md
%exclude %{_docdir}/%{name}/LICENSE.md
%{_includedir}/%{name}/*

%changelog
* Thu Feb 6 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-1
- Initial package

