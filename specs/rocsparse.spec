%if 0%{?suse_version}
%global rocsparse_name librocsparse1
%else
%global rocsparse_name rocsparse
%endif

%global upstreamname rocSPARSE
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

# downloads tests, use mock --enable-network
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

# Option to test suite for testing on real HW:
# May have to set gpu under test with
# export HIP_VISIBLE_DEVICES=<num> - 0, 1 etc.
%bcond_with check

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# Use ninja if it is available
%if 0%{?fedora} || 0%{?suse_version}
%bcond_without ninja
%else
%bcond_with ninja
%endif

%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif

%global cmake_config \\\
  -DCMAKE_CXX_COMPILER=hipcc \\\
  -DCMAKE_C_COMPILER=hipcc \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_BUILD_TYPE=%build_type \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DCMAKE_SKIP_RPATH=ON \\\
  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DHIP_PLATFORM=amd \\\
  -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \\\
  -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_FORTRAN_CLIENTS=OFF

# gfx950 is an experimental target
# Enabling will short circuit the normal build.
# There is no check support.
# To use do
# $ module load rocm/gfx950
#     <do stuff>
# $ module purge
%bcond_with gfx950

Name:           %{rocsparse_name}
Version:        %{rocm_version}
Release:        4%{?dist}
Summary:        SPARSE implementation for ROCm
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch0:         0001-rocsparse-offload-compress.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocprim-static

%if %{with compress}
BuildRequires:  pkgconfig(libzstd)
%endif

%if %{with test}
BuildRequires:  libomp-devel
BuildRequires:  python3dist(pyyaml)
%if %{with gfx950}
BuildRequires:  rocblas-gfx950-devel
%else
BuildRequires:  rocblas-devel
%endif

%if 0%{?suse_version}
BuildRequires:  gcc-fortran
BuildRequires:  gtest
%else
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
%endif


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

Provides:       rocsparse = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocSPARSE exposes a common interface that provides Basic
Linear Algebra Subroutines for sparse computation
implemented on top of AMD's Radeon Open eCosystem Platform
ROCm runtime and toolchains. rocSPARSE is created using
the HIP programming language and optimized for AMD's
latest discrete GPUs.

%if 0%{?suse_version}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rocsparse-devel = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%if %{with gfx950}

%package gfx950
Summary:        The gfx950 rocSPARSE package
Provides:       rocsparse-gfx950 = %{version}-%{release}
Conflicts:      %{name}

%description gfx950
%{summary}

%package gfx950-devel
Summary:        The gfx950 rocSPARSE development package
Requires:       %{name}-gfx950%{?_isa} = %{version}-%{release}
Provides:       rocsparse-gfx950-devel = %{version}-%{release}
Conflicts:      %{name}-devel

%description gfx950-devel
%{summary}

%if %{with test}
%package gfx950-test
Summary:        The gfx950 rocSPARSE test package
Requires:       %{name}-gfx950%{?_isa} = %{version}-%{release}
Conflicts:      %{name}-test

%description gfx950-test
%{summary}

%endif # gfx950-test
%endif # gfx950

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%if %{with gfx950}

module load rocm/gfx950

# Build fails in 6.4.0
# /usr/include/rocprim/intrinsics/atomic.hpp:210:6: error: support for 128-bit atomics not implemented for current architecture
# https://github.com/ROCm/rocPRIM/issues/738
%cmake %{cmake_generator} %{cmake_config} \
    -DGPU_TARGETS=${ROCM_GPUS} \
    -DCMAKE_INSTALL_BINDIR=${ROCM_BIN} \
    -DCMAKE_INSTALL_INCLUDEDIR=${ROCM_INCLUDE} \
    -DCMAKE_INSTALL_LIBDIR=${ROCM_LIB}

%else

%cmake %{cmake_generator} %{cmake_config} \
    -DGPU_TARGETS=%{rocm_gpu_list_default} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
%if %{with test}
    -DCMAKE_MATRICES_DIR=%{_builddir}/rocsparse-test-matrices/
%endif


%endif

%cmake_build

%if %{with gfx950}
module purge
%endif

%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/rocsparse/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocsparse/LICENSE.md
fi

%if %{with test}
    mkdir -p %{buildroot}/%{_datadir}/%{name}/matrices
    install -pm 644 %{_builddir}/rocsparse-test-matrices/* %{buildroot}/%{_datadir}/%{name}/matrices
%endif

%check
%if %{with test}
%if %{with check}
%if 0%{?suse_version}
export LD_LIBRARY_PATH=%{__builddir}/library:$LD_LIBRARY_PATH
%{__builddir}/clients/staging/rocsparse-test
%else
export LD_LIBRARY_PATH=%{_vpath_builddir}/library:$LD_LIBRARY_PATH
%{_vpath_builddir}/clients/staging/rocsparse-test
%endif
%endif
%endif

%if %{with gfx950}
%files gfx950
%license LICENSE.md
%{_libdir}/rocm/gfx950/lib/librocsparse.so.1{,.*}

%files gfx950-devel
%dir %{_libdir}/rocm/gfx950/lib/cmake/rocsparse
%dir %{_libdir}/rocm/gfx950/include/rocsparse
%{_libdir}/rocm/gfx950/lib/cmake/rocsparse/*.cmake
%{_libdir}/rocm/gfx950/lib/librocsparse.so
%{_libdir}/rocm/gfx950/include/rocsparse/*.{h,hpp}

%if %{with test}
%files gfx950-test
%endif

%else

%files 
%license LICENSE.md
%{_libdir}/librocsparse.so.1{,.*}

%files devel
%doc README.md
%dir %{_libdir}/cmake/rocsparse
%dir %{_includedir}/rocsparse
%{_includedir}/rocsparse/*
%{_libdir}/librocsparse.so
%{_libdir}/cmake/rocsparse/*.cmake

%if %{with test}
%files test
%dir %{_datadir}/rocsparse
%dir %{_libdir}/rocsparse
%{_bindir}/rocsparse*
%{_datadir}/rocsparse/test/rocsparse_*
%{_libdir}/rocsparse/rocsparseio-*
%{_datadir}/rocsparse/matrices/*

%endif
%endif

%changelog
* Mon May 12 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Add experimental gfx950

* Fri May 2 2025 Tim Flink <tflink@fedoraproject.org> - 6.4.0-3
- include downloaded matrix files for test subpackage

* Tue Apr 29 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- Improve testing for suse

* Fri Apr 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Thu Apr 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-3
- Reenable ninja

* Wed Feb 12 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-2
- Remove multi build
- Fix SLE 15.6

* Wed Jan 29 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-1
- Update to 6.3.2

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- multithread compress

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Mon Dec 9 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed
