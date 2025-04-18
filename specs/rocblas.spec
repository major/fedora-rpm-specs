%if 0%{?suse_version}
%global rocblas_name librocblas4
%else
%global rocblas_name rocblas
%endif

%global upstreamname rocBLAS
%global rocm_release 6.4
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RELEASE
%endif

%bcond_without compress
%if %{with compress}
%global build_compress ON
%else
%global build_compress OFF
%endif

%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

%bcond_without tensile
%if %{with tensile}
%global build_tensile ON
%else
%global build_tensile OFF
%endif

%if 0%{?rhel} && 0%{?rhel} < 10
# On CS9: /usr/bin/debugedit: Cannot handle 8-byte build ID
%global debug_package %{nil}
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# SUSE/OSB times out because -O is added to the make args
# This accumulates all the output from the long running tensile
# jobs.
%global _make_output_sync %{nil}

# OracleLinux 9 has a problem with it's strip not recognizing *.co's
%global __strip %rocmllvm_bindir/llvm-strip

# Use ninja if it is available
# Ninja is available on suse but obs times out with ninja build, make doesn't
%if 0%{?fedora}
%bcond_without ninja
%else
%bcond_with ninja
%endif

%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif

Name:           %{rocblas_name}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        BLAS implementation for ROCm
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        MIT AND BSD-3-Clause

Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch2:         0001-fixup-install-of-tensile-output.patch
Patch4:         0001-offload-compress-option.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  roctracer-devel

%if %{with tensile}
%if 0%{?suse_version}
%if %{suse_version} < 1699
BuildRequires:  python3-tensile-devel
%else
BuildRequires:  python311-tensile-devel
%endif
# OBS vm times out without console output
%global tensile_verbose 2
%global tensile_library_format yaml
%else
BuildRequires:  python3dist(tensile)
%if 0%{?rhel}
%global tensile_verbose 2
%global tensile_library_format yaml
%else
BuildRequires:  msgpack-devel
%global tensile_verbose 1
%global tensile_library_format msgpack
%endif

%endif
%endif

%if %{with compress}
BuildRequires:  pkgconfig(libzstd)
%endif

%if %{with test}
BuildRequires:  gtest-devel
BuildRequires:  blas-devel
BuildRequires:  libomp-devel
BuildRequires:  python3dist(pyyaml)
BuildRequires:  rocminfo
BuildRequires:  rocm-smi-devel
%endif

%if %{with ninja}
%if 0%{?fedora}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  ninja
%define __builder ninja
%endif
%endif

Provides:       rocblas = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocBLAS is the AMD library for Basic Linear Algebra Subprograms
(BLAS) on the ROCm platform. It is implemented in the HIP
programming language and optimized for AMD GPUs.

%if 0%{?suse_version}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(hip)
Provides:       rocblas-devel = %{version}-%{release}

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
sed -i -e 's@set( BLAS_LIBRARY "blas" )@set( BLAS_LIBRARY "cblas" )@' clients/CMakeLists.txt
sed -i -e 's@target_link_libraries( rocblas-test PRIVATE ${BLAS_LIBRARY} ${GTEST_BOTH_LIBRARIES} roc::rocblas )@target_link_libraries( rocblas-test PRIVATE cblas ${GTEST_BOTH_LIBRARIES} roc::rocblas )@' clients/gtest/CMakeLists.txt

# no git in this build
sed -i -e 's@find_package(Git REQUIRED)@find_package(Git)@' library/CMakeLists.txt

%build

# With compat llvm the system clang is wrong
CLANG_PATH=`hipconfig --hipclangpath`
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler
# Work around problem with koji's ld
export HIPCC_LINK_FLAGS_APPEND=-fuse-ld=lld

%if %{with tensile}
TP=`/usr/bin/TensileGetPath`
%endif

CORES=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
if [ ${CORES}x = x ]; then
    CORES=1
fi
# Try again..
if [ ${CORES} = 1 ]; then
    CORES=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${CORES}x = x ]; then
	CORES=4
    fi
fi

%cmake %{cmake_generator} \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_C_COMPILER=hipcc \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
    -DBUILD_FORTRAN_CLIENTS=OFF \
    -DBLAS_LIBRARY=cblas \
    -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \
    -DBUILD_WITH_HIPBLASLT=OFF \
    -DTensile_COMPILER=hipcc \
    -DTensile_CPU_THREADS=${CORES} \
    -DTensile_LIBRARY_FORMAT=%{tensile_library_format} \
    -DTensile_VERBOSE=%{tensile_verbose} \
    -DBUILD_WITH_TENSILE=%{build_tensile} \
    -DTensile_DIR=${TP}/cmake \
    -DBUILD_WITH_PIP=OFF

%cmake_build

%install
%cmake_install

echo s@%{buildroot}@@ > br.sed
find %{buildroot}%{_libdir} -name '*.so.*.[0-9]' | sed -f br.sed >  %{name}.files
find %{buildroot}%{_libdir} -name '*.so.[0-9]'   | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name 'library'      | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name '*.so'         | sed -f br.sed >  %{name}.devel
find %{buildroot}%{_libdir} -name '*.cmake'      | sed -f br.sed >> %{name}.devel
find %{buildroot}           -name 'rocblas-*'    | sed -f br.sed >  %{name}.test
find %{buildroot}           -name 'rocblas_*'    | sed -f br.sed >> %{name}.test

if [ -f %{buildroot}%{_prefix}/share/doc/rocblas/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocblas/LICENSE.md
fi
    
%files -f %{name}.files
%license LICENSE.md
%if %{with tensile}
%dir %{_libdir}/rocblas
%dir %{_libdir}/rocblas/library
%endif

%files devel -f %{name}.devel
%doc README.md
%dir %{_libdir}/cmake/rocblas
%dir %{_includedir}/rocblas
%{_includedir}/rocblas/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
* Fri Apr 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Thu Apr 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-12
- Reenable ninja

* Fri Apr 4 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-11
- Use rocm-llvm strip

* Thu Feb 27 2025 Cristian Le <git@lecris.dev> - 6.3.0-10
- Add hip requirement to devel package

* Thu Feb 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-9
- Enable tensile for RHEL

* Wed Feb 26 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-8
- Enable tensile for SUSE

* Sun Feb 23 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-7
- Use tensile verbosity to avoid OSB timeout

* Wed Feb 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-6
- Use tensile cmake from the python location

* Tue Feb 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-5
- Remove multibuild
- Fix SLE 15.6

* Sat Jan 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- multithread rpm compress

* Tue Jan 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- build requires gcc-c++

* Fri Dec 20 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- Build type should be release

* Fri Dec 6 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed


