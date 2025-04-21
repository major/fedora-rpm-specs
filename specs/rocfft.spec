%if 0%{?suse_version}
%global rocfft_name librocfft0
%else
%global rocfft_name rocfft
%endif

%global upstreamname rocFFT

%global rocm_release 6.4
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm

# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host-fcf-protection/')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%bcond_with test
%if %{with test}
# Disable rpatch checks for a local build
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif

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

Name:           %{rocfft_name}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Fast Fourier Transforms (FFT) library

Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-rocm-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

%if %{with test}
BuildRequires:  gtest-devel
BuildRequires:  rocrand-devel
BuildRequires:  fftw-devel
BuildRequires:  boost-devel
BuildRequires:  hipcc-libomp-devel
BuildRequires:  hiprand-devel

# rocfft-test compiles some things and requires rocm-hip-devel
Requires:  rocm-hip-devel
%endif

%if %{with doc}
BuildRequires:  python3-sphinx
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

Provides:       rocfft = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Patch0: 0001-cmake-use-gnu-installdirs.patch

%description
A library for computing Fast Fourier Transforms (FFT), part of ROCm.

%if 0%{?suse_version}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%package devel
Summary:        The rocFFT development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rocfft-devel = %{version}-%{release}
Requires:       rocm-hip-devel

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
%autosetup -n %{upstreamname}-rocm-%{version} -p 1

# Do not care so much about the sqlite version
sed -i -e 's@SQLite3 3.36 @SQLite3 @' cmake/sqlite.cmake

%build

# ensuring executables are PIE enabled
export LDFLAGS="${LDFLAGS} -pie"

# OpenMP tests are disabled because upstream sets rpath in that case without
# a way to skip
#
# RHEL 9 has an issue with missing symbol __truncsfhf2 in libgcc.
# So switch from libgcc to rocm-llvm's libclang-rt.builtins with
# the rtlib=compiler-rt. Leave unwind unchange with unwindlib=libgcc

%cmake %{cmake_generator} \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_CXX_FLAGS="--rtlib=compiler-rt --unwindlib=libgcc" \
    -DCMAKE_C_COMPILER=hipcc \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DROCFFT_BUILD_OFFLINE_TUNER=OFF \
    -DROCFFT_KERNEL_CACHE_ENABLE=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DSQLITE_USE_SYSTEM_PACKAGE=ON

%cmake_build

%install
%cmake_install

# we don't need the rocfft_rtc_helper binary, don't package it
find %{buildroot} -type f -name "rocfft_rtc_helper" -print0 | xargs -0 -I {} /usr/bin/rm -rf "{}"

# we don't need or want the client-info file installed by rocfft
rm -rf %{buildroot}/%{_prefix}/.info

echo s@%{buildroot}@@ > br.sed
find %{buildroot}%{_libdir} -name '*.so.*.[0-9]'     | sed -f br.sed >  %{name}.files
find %{buildroot}%{_libdir} -name '*.so.[0-9]'       | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name '*.so'             | sed -f br.sed >  %{name}.devel
find %{buildroot}%{_libdir} -name '*.cmake'          | sed -f br.sed >> %{name}.devel
%if %{with test}
find %{buildroot}           -name 'rocfft-test'      | sed -f br.sed >  %{name}.test
find %{buildroot}           -name 'rtc_helper_crash' | sed -f br.sed >> %{name}.test
%endif

if [ -f %{buildroot}%{_prefix}/share/doc/rocfft/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocfft/LICENSE.md
fi

%files -f %{name}.files
%doc README.md
%license LICENSE.md

%files devel -f %{name}.devel
%dir %{_libdir}/cmake/rocfft
%dir %{_includedir}/rocfft
%{_includedir}/rocfft/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
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



