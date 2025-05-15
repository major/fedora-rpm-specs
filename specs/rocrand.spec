%if 0%{?suse_version}
%global rocrand_name librocrand1
%else
%global rocrand_name rocrand
%endif

%global upstreamname rocRAND

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
%global build_type RelWithDebInfo
%endif

# flags for testing, neither should be enabled for official builds in koji
# relevant HW is required to run %check
%bcond_with test
%bcond_with check

# do not check for rpaths when building test subpackages
%if %{with test} || %{with check}
%global __brp_check_rpaths %{nil}
%endif

# enable building of tests if check or test are enabled
%if %{with test} || %{with check}
%global build_test ON
%else
%global build_test OFF
%endif

# For docs
%bcond_with doc

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

# The common parts of the cmake configuration
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
  -DBUILD_TEST=%build_test

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

%bcond_with generic
%global rocm_gpu_list_generic "gfx9-generic;gfx9-4-generic;gfx10-1-generic;gfx10-3-generic;gfx11-generic;gfx12-generic"
%if %{with generic}
%global gpu_list %{rocm_gpu_list_generic}
%else
%global gpu_list %{rocm_gpu_list_default}
%endif

# gfx950 is an experimental target
# Enabling will short circuit the normal build.
# There is no check support.
# To use do
# $ module load rocm/gfx950
#     <do stuff>
# $ module purge
%bcond_with gfx950

Name:           %{rocrand_name}
Version:        %{rocm_version}
Release:        6%{?dist}
Summary:        ROCm random number generator

Url:            https://github.com/ROCm/rocRAND
License:        MIT AND BSD-3-Clause
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules

%if %{with test} || %{with check}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif
%endif

%if %{with doc}
BuildRequires:  doxygen
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

Provides:       rocrand = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
The rocRAND project provides functions that generate pseudo-random and
quasi-random numbers.

The rocRAND library is implemented in the HIP programming language and
optimized for AMD's latest discrete GPUs. It is designed to run on top of AMD's
Radeon Open Compute ROCm runtime, but it also works on CUDA enabled GPUs.

%if 0%{?suse_version}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%package devel
Summary:        The rocRAND development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rocrand-devel = %{version}-%{release}

%description devel
The rocRAND development package.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%if %{with gfx950}

%package gfx950
Summary:        The gfx950 rocRAND package
Provides:       rocrand-gfx950 = %{version}-%{release}
Conflicts:      %{name}

%description gfx950
%{summary}

%package gfx950-devel
Summary:        The gfx950 rocRAND development package
Requires:       %{name}-gfx950%{?_isa} = %{version}-%{release}
Provides:       rocrand-gfx950-devel = %{version}-%{release}
Conflicts:      %{name}-devel

%description gfx950-devel
%{summary}

%if %{with test}
%package gfx950-test
Summary:        The gfx950 rocRAND test package
Requires:       %{name}-gfx950%{?_isa} = %{version}-%{release}
Conflicts:      %{name}-test

%description gfx950-test
%{summary}

%endif # gfx950-test
%endif # gfx950

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# On Tumbleweed Q2,2025
# /usr/include/gtest/internal/gtest-port.h:279:2: error: C++ versions less than C++14 are not supported.
#   279 | #error C++ versions less than C++14 are not supported.
# https://github.com/ROCm/rocRAND/issues/639
# Convert the c++11's to c++14
sed -i -e 's@set(CMAKE_CXX_STANDARD 11)@set(CMAKE_CXX_STANDARD 14)@' {,test/{cpp_wrapper,package}/}CMakeLists.txt

%build

%if %{with gfx950}

module load rocm/gfx950

%cmake %{cmake_generator} %{cmake_config} \
    -DAMDGPU_TARGETS=${ROCM_GPUS} \
    -DCMAKE_INSTALL_BINDIR=${ROCM_BIN} \
    -DCMAKE_INSTALL_INCLUDEDIR=${ROCM_INCLUDE} \
    -DCMAKE_INSTALL_LIBDIR=${ROCM_LIB}

%else
%cmake %{cmake_generator} %{cmake_config} \
    -DAMDGPU_TARGETS=%{gpu_list} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir
%endif

%cmake_build

%if %{with gfx950}
module purge
%endif


%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/rocrand/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocrand/LICENSE.txt
fi

%check
%if %{with check}
%if 0%{?suse_version}
# Need some help to find librocrand.so on suse
# find . -name 'librocrand.so.1'
export LD_LIBRARY_PATH=$PWD/build/library:$LD_LIBRARY_PATH
%endif

%ctest
%endif

%if %{with gfx950}
%files gfx950
%doc README.md
%license LICENSE.txt
%{_libdir}/rocm/gfx950/lib/librocrand.so.1{,.*}

%files gfx950-devel
%dir %{_libdir}/rocm/gfx950/lib/cmake/rocrand
%dir %{_libdir}/rocm/gfx950/include/rocrand
%{_libdir}/rocm/gfx950/include/rocrand/*.{h,hpp}
%{_libdir}/rocm/gfx950/lib/cmake/rocrand/*.cmake
%{_libdir}/rocm/gfx950/lib/librocrand.so

%if %{with test}
%files gfx950-test
%dir %{_libdir}/rocm/gfx950/bin/rocRAND
%{_libdir}/rocm/gfx950/bin/test_*
%{_libdir}/rocm/gfx950/bin/rocRAND/*.cmake
%endif

%else

%files 
%doc README.md
%license LICENSE.txt
%{_libdir}/librocrand.so.1{,.*}

%files devel 
%dir %{_libdir}/cmake/rocrand
%dir %{_includedir}/rocrand
%{_includedir}/rocrand/*.{h,hpp}
%{_libdir}/cmake/rocrand/*.cmake
%{_libdir}/librocrand.so

%if %{with test}
%files test
%dir %{_bindir}/rocRAND
%{_bindir}/test_*
%{_bindir}/rocRAND/*.cmake
%endif
%endif

%changelog
* Tue May 13 2025 Tim Flink <tflink@fedoraproject.org> - 6.3.0-6
- updated logic to adhere to desired test and check behavior

* Mon May 12 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-5
- Fix gfx950 mock build

* Sat May 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Add experimental gfx950

* Sun Apr 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Improve testing on suse

* Fri Apr 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- Add generic gpus

* Sat Apr 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Wed Apr 9 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-5
- Reenable ninja build

* Mon Feb 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- Remove split building
- Fix SLE 15.6

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- multithread compress

* Tue Jan 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Sun Dec 8 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed


