%global upstreamname rocBLAS
%global rocm_release 6.3
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# $gpu will be evaluated in the loops below             
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

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

%if 0%{?rhel} || 0%{?suse_version}
# RHEL does not have a working tensile
# OSB/SUSE is gets stuck on tensile taking a long time with 4 jobs
%bcond_with tensile
%else
%bcond_without tensile
%endif
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
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio

Name:           rocblas
Version:        %{rocm_version}
Release:        4%{?dist}
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
BuildRequires:  rocm-rpm-macros-modules

%if %{with tensile}
%if 0%{?suse_version}
BuildRequires:  msgpack-cxx-devel
%else
BuildRequires:  msgpack-devel
%endif
BuildRequires:  python3-tensile
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

Requires:       rocm-rpm-macros-modules

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocBLAS is the AMD library for Basic Linear Algebra Subprograms
(BLAS) on the ROCm platform. It is implemented in the HIP
programming language and optimized for AMD GPUs.

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

for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    %cmake \
	-DCMAKE_CXX_COMPILER=hipcc \
	-DCMAKE_C_COMPILER=hipcc \
	-DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
	-DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
	-DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
           -DCMAKE_BUILD_TYPE=%{build_type} \
	   -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
	   -DCMAKE_SKIP_RPATH=ON \
	   -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
	   -DROCM_SYMLINK_LIBS=OFF \
	   -DHIP_PLATFORM=amd \
	   -DAMDGPU_TARGETS=${ROCM_GPUS} \
	   -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
	   -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
	   -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \
	   -DBUILD_CLIENTS_TESTS=%{build_test} \
	   -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
	   -DBUILD_FORTRAN_CLIENTS=OFF \
	   -DBLAS_LIBRARY=cblas \
	   -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \
	   -DBUILD_WITH_HIPBLASLT=OFF \
	   -DTensile_COMPILER=hipcc \
	   -DBUILD_WITH_TENSILE=%{build_tensile} \
	   -DBUILD_WITH_PIP=OFF

    %cmake_build
    module purge
done

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done
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
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/library
%endif

%files devel -f %{name}.devel
%doc README.md
%dir %{_libdir}/cmake/%{name}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
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


