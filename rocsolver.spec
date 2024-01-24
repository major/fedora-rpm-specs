%global upstreamname rocSOLVER
%global rocm_release 6.0
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
# build_cxxflags does not honor CMAKE_BUILD_TYPE, strip out -g
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /')

# Do not build the debug package
# building with CMAKE_BUILD_TYPE=RelWithDebInfo causes link overflows
# So instead of breaking building into gpu specific libs, disable debug info
%global debug_package %{nil}

# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

# Tests are downloaded so this option is only good for local building
# Also need to
# export QA_RPATHS=0xff
%bcond_with test

# may run out of memory for both compile and link
# Use fine tuned cmake ROCSOLVER_PARALLEL_COMPILE|LINK_JOBS switches
%global _smp_mflags %{nil}

# Fortran is only used in testing
%global build_fflags %{nil}

Name:           rocsolver
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        Next generation LAPACK implementation for ROCm platform
Url:            https://github.com/ROCmSoftwarePlatform/rocSOLVER

# License check reports BSD 2-Clause
# But reviewing LICENSE.md, this is only for AMD
# Later in the file are BSD 3-Clause for LAPACK and MAGMA
License:        BSD-3-Clause AND BSD-2-Clause

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
# https://github.com/ROCm/rocSOLVER/pull/652
Patch0:         0001-Add-llvm-style-compile-and-link-options.patch

BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  fmt-devel
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  ninja-build
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocprim-devel
BuildRequires:  rocsparse-devel

%if %{with test}
BuildRequires:  blas-static
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  lapack-static
%endif

%description
rocSOLVER is a work-in-progress implementation of a subset
of LAPACK functionality on the ROCm platform.

%package devel
Summary: Libraries and headers for %{name}
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

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
BUILD_MEM=4
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
LINK_MEM=32
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`

for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    %cmake %rocm_cmake_options \
           -DROCSOLVER_PARALLEL_COMPILE_JOBS=$COMPILE_JOBS \
           -DROCSOLVER_PARALLEL_LINK_JOBS=$LINK_JOBS \
           -DCMAKE_BUILD_TYPE=RELEASE \
%if %{with test}
           -DBUILD_CLIENTS_TESTS=ON
%endif

    %cmake_build
    module purge
done

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

# strip *.so
strip %{buildroot}%{_libdir}/librocsolver.so.0.*
strip %{buildroot}%{_libdir}/rocm/gfx10/lib/librocsolver.so.0.*
strip %{buildroot}%{_libdir}/rocm/gfx11/lib/librocsolver.so.0.*
strip %{buildroot}%{_libdir}/rocm/gfx8/lib/librocsolver.so.0.*
strip %{buildroot}%{_libdir}/rocm/gfx9/lib/librocsolver.so.0.*

%files
%license LICENSE.md
%exclude %{_docdir}/%{name}/LICENSE.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/rocm/gfx*/lib/lib%{name}.so.*

%files devel
%dir %{_includedir}/%{name}
%dir %{_libdir}/cmake/%{name}
%dir %{_libdir}/rocm/gfx8/lib/cmake/%{name}
%dir %{_libdir}/rocm/gfx9/lib/cmake/%{name}
%dir %{_libdir}/rocm/gfx10/lib/cmake/%{name}
%dir %{_libdir}/rocm/gfx11/lib/cmake/%{name}

%doc README.md
%{_includedir}/%{name}/*.h
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/lib%{name}.so
%{_libdir}/rocm/gfx*/lib/lib%{name}.so
%{_libdir}/rocm/gfx*/lib/cmake/%{name}/*.cmake

%if %{with test}
%files test
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/test
%dir %{_datadir}/%{name}/test/mat_20_60
%dir %{_datadir}/%{name}/test/mat_20_100
%dir %{_datadir}/%{name}/test/mat_20_140
%dir %{_datadir}/%{name}/test/mat_50_60
%dir %{_datadir}/%{name}/test/mat_50_100
%dir %{_datadir}/%{name}/test/mat_50_140
%dir %{_datadir}/%{name}/test/mat_100_300
%dir %{_datadir}/%{name}/test/mat_100_500
%dir %{_datadir}/%{name}/test/mat_100_700
%dir %{_datadir}/%{name}/test/mat_250_300
%dir %{_datadir}/%{name}/test/mat_250_500
%dir %{_datadir}/%{name}/test/mat_250_700

%{_datadir}/%{name}/test/mat_20_60/*
%{_datadir}/%{name}/test/mat_20_100/*
%{_datadir}/%{name}/test/mat_20_140/*
%{_datadir}/%{name}/test/mat_50_60/*
%{_datadir}/%{name}/test/mat_50_100/*
%{_datadir}/%{name}/test/mat_50_140/*
%{_datadir}/%{name}/test/mat_100_300/*
%{_datadir}/%{name}/test/mat_100_500/*
%{_datadir}/%{name}/test/mat_100_700/*
%{_datadir}/%{name}/test/mat_250_300/*
%{_datadir}/%{name}/test/mat_250_500/*
%{_datadir}/%{name}/test/mat_250_700/*
%{_bindir}/%{name}*
%{_libdir}/rocm/gfx*/bin/%{name}*
%endif

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Tom Rix <trix@redhat.com> - 6.0.0-2
- fix url
- comment on multiple licenses
- post pr for the link and compile jobs patch

* Wed Jan 3 2024 Tom Rix <trix@redhat.com>  - 6.0.0-1
- Update to 6.0

* Thu Nov 30 2023 Tom Rix <trix@redhat.com>  - 5.7.1-2
- Add compile and link jobs switches
- Remove -g, debug linking overflow
- Fix license

* Thu Nov 2 2023 Tom Rix <trix@redhat.com>  - 5.7.1-1
- Initial package
