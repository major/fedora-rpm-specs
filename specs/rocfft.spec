#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif

%global upstreamname rocFFT
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%if 0%{?suse_version}
%global rocfft_name librocfft0%{pkg_suffix}
%else
%global rocfft_name rocfft%{pkg_suffix}
%endif

%global toolchain rocm

# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host-fcf-protection/')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# kernel oops on gfx1201
# https://github.com/ROCm/rocFFT/issues/560
%bcond_with test
%if %{with test}
# Disable rpatch checks for a local build
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif

# Option to test suite for testing on real HW:
# May have to set gpu under test with
# export HIP_VISIBLE_DEVICES=<num> - 0, 1 etc.
%bcond_with check

# For docs
%bcond_with doc

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# Use rocm-llvm strip
%global __strip %rocmllvm_bindir/llvm-strip

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
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_BUILD_TYPE=%{build_type} \\\
  -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \\\
  -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \\\
  -DCMAKE_CXX_FLAGS="--rtlib=compiler-rt --unwindlib=libgcc" \\\
  -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \\\
  -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DROCFFT_BUILD_OFFLINE_TUNER=OFF \\\
  -DROCFFT_KERNEL_CACHE_ENABLE=OFF \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DSQLITE_USE_SYSTEM_PACKAGE=ON

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

Name:           rocfft%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        6%{?dist}
%endif
Summary:        ROCm Fast Fourier Transforms (FFT) library
License:        MIT

%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/archive/%{commit0}/rocm-libraries-%{shortcommit0}.tar.gz
%else
Url:            https://github.com/ROCm/%{upstreamname}
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-rocm-%{version}.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel >= %{rocm_release}

%if %{with test}
BuildRequires:  rocrand%{pkg_suffix}-devel
BuildRequires:  fftw-devel
BuildRequires:  boost-devel
BuildRequires:  hiprand%{pkg_suffix}-devel

%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif

# rocfft-test compiles some things and requires rocm-hip-devel
Requires:  rocm-hip%{pkg_suffix}-devel >= %{rocm_release}

%endif

%if %{with doc}
%if 0%{?suse_version}
BuildRequires:  %{python_module Sphinx}
%else
BuildRequires:  python3dist(sphinx)
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

Provides:       rocfft%{pkg_suffix} = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Patch0: 0001-cmake-use-gnu-installdirs.patch

%description
A library for computing Fast Fourier Transforms (FFT), part of ROCm.

%if 0%{?suse_version}
%package -n %{rocfft_name}
Summary:        Shared libraries for %{name}

%description -n %{rocfft_name}
%{summary}

%ldconfig_scriptlets -n %{rocfft_name}
%endif

%package devel
Summary:        The rocFFT development package
Requires:       %{rocfft_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-hip%{pkg_suffix}-devel

%description devel
The rocFFT development package.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/rocfft
%else
%autosetup -n %{upstreamname}-rocm-%{version} -p 1
%endif

# Do not care so much about the sqlite version
sed -i -e 's@SQLite3 3.50.2 @SQLite3 @' cmake/sqlite.cmake

%build
%if %{with gitcommit}
cd projects/rocfft
%endif

# ensuring executables are PIE enabled
export LDFLAGS="${LDFLAGS} -pie"

# OpenMP tests are disabled because upstream sets rpath in that case without
# a way to skip
#
# RHEL 9 has an issue with missing symbol __truncsfhf2 in libgcc.
# So switch from libgcc to rocm-llvm's libclang-rt.builtins with
# the rtlib=compiler-rt. Leave unwind unchange with unwindlib=libgcc
%cmake %{cmake_generator} %{cmake_config} \
    -DGPU_TARGETS=%{gpu_list}

%cmake_build

%install
%if %{with gitcommit}
cd projects/rocfft
%endif

%cmake_install

# we don't need the rocfft_rtc_helper binary, don't package it
find %{buildroot} -type f -name "rocfft_rtc_helper" -print0 | xargs -0 -I {} /usr/bin/rm -rf "{}"

# we don't need or want the client-info file installed by rocfft
rm -rf %{buildroot}/%{pkg_prefix}/.info

rm -f %{buildroot}%{pkg_prefix}/share/doc/rocfft/LICENSE.md


%check
%if %{with test}
%if %{with check}
%if 0%{?suse_version}
%{__builddir}/clients/staging/rocfft-test
%else
%{_vpath_builddir}/clients/staging/rocfft-test
%endif
%endif
%endif

%files -n %{rocfft_name}
%if %{with gitcommit}
%doc projects/rocfft/README.md
%license projects/rocfft/LICENSE.md
%else
%doc README.md
%license LICENSE.md
%endif

%{pkg_prefix}/%{pkg_libdir}/librocfft.so.0{,.*}

%files devel
%{pkg_prefix}/include/rocfft/
%{pkg_prefix}/%{pkg_libdir}/librocfft.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocfft/

%if %{with test}
%files test
%{pkg_prefix}/bin/rocfft-test
%{pkg_prefix}/bin/rtc_helper_crash
%endif

%changelog
* Mon Jan 5 2026 Tom Rix <Tom.Rix@amd.com> - 7.1.0-6
- Remove omp tests

* Wed Dec 17 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-5
- Add -with compat
- Remove -with generic

* Wed Nov 19 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-4
- Remove dir tags

* Wed Nov 12 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-3
- Rebuild for gfx1036

* Wed Nov 5 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Remove sqlite version check

* Thu Oct 30 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Sun Oct 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-2
- better handling of shared library on opensuse

* Fri Oct 10 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Mon Oct 6 2025 Tim Flink <tflink@fedoraproject.org> - 7.0.1-9
- require rocm-omp-devel for test subpackage
- re-enable omp tests for test subpackage builds

* Thu Sep 25 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-8
- require a new rocm-runtime

* Tue Sep 23 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-7
- Rebuild

* Sat Sep 20 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-6
- Simplify file removal

* Fri Aug 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-5
- Remove buildrequires hipcc-libomp-devel

* Fri Aug 8 2025 Egbert Eich <eich@suse.com> - 6.4.2-4
- Adjust python dependency for SUSE.

* Mon Jul 28 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-3
- Remove experimental gfx950

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.2-1
- Update to 6.4.2

* Tue Jun 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-6
- Remove suse check for using ldconfig

* Mon May 12 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-5
- Fix gfx950 mock build

* Sun May 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Add experimential gfx950

* Sun Apr 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Improve testing on suse

* Sat Apr 26 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- Add generic gpus

* Sat Apr 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Sun Apr 13 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-10
- Remove global rocfft_version

* Thu Apr 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-9
- Reenble ninja

* Fri Apr 4 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-8
- Work around old gcc for rhel 9

* Thu Apr 3 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-7
- Remove sqlite version check for ol9

* Fri Feb 14 2025 Christoph Junghans <junghans@votca.org> - 6.3.0-6
- Add missing dep on rocm-hic-devel

* Wed Feb 12 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-5
- Fix provides

* Tue Feb 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- Remove multi build
- Fix SLE 15.6

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- multithread compress

* Tue Jan 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Sun Dec 8 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed



