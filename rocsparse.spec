%global upstreamname rocSPARSE
%global rocm_release 6.0
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

# Tests are downloaded so this option is only good for local building
# Also need to
# export QA_RPATHS=0xff
%bcond_with test

Name:           rocsparse
Version:        %{rocm_version}
Release:        %autorelease
Summary:        SPARSE implementation for ROCm
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        MIT

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch0:         0001-prepare-rocsparse-cmake-for-fedora.patch

BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocprim-static

%if %{with test}
BuildRequires:  gtest-devel
BuildRequires:  libomp-devel
BuildRequires:  rocblas-devel
%endif

%description
rocSPARSE exposes a common interface that provides Basic
Linear Algebra Subroutines for sparse computation
implemented on top of AMD's Radeon Open eCosystem Platform
ROCm runtime and toolchains. rocSPARSE is created using
the HIP programming language and optimized for AMD's
latest discrete GPUs.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    %cmake %rocm_cmake_options \
%if %{with test}
           %rocm_cmake_test_options
%endif

    %cmake_build
    module purge
done

%cmake_build

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

%files
%license LICENSE.md
%exclude %{_docdir}/%{name}/LICENSE.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/rocm/gfx*/lib/lib%{name}.so.*

%files devel
%doc README.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/rocm/gfx*/lib/lib%{name}.so
%{_libdir}/rocm/gfx*/lib/cmake/%{name}/

%if %{with test}
%files test
%{_bindir}/%{name}*
%{_libdir}/rocm/gfx*/bin/%{name}*
%endif

%changelog
%autochangelog
