%global upstreamname rocFFT

%global rocm_release 6.0
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# rocFFT has a version seperate from the ROCm version that it is released with
%global rocfft_version 1.0.25

%global toolchain rocm

# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host-fcf-protection/')

# the debug build has a completely different file name, use condition to enable/disable
%bcond rocm-debug 0

# build test packages but don't run them here due to HW requirements
%bcond check 1

# the kernel cache is slightly problematic in terms of packaging and where to put it
# disable building it until the question of how to package the cache db file is answered
%bcond kernelcache 0

Name:           rocfft
Version:        %{rocm_version}
Release:        %autorelease -b 2 # this is tomkae sure that the release supercedes reviewed builds, remove for next release
Summary:        ROCm Fast Fourier Transforms (FFT) library

Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-rocm-%{version}.tar.gz


BuildRequires:  cmake
BuildRequires:  compiler-rt
# Fedora packaging guidelines require gcc, gcc-c++ or clang in the build requires. clang-devel is not sufficient
# https://docs.fedoraproject.org/en-US/packaging-guidelines/C_and_C++/
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  doxygen
BuildRequires:  glibc-headers
%if %{with check}
BuildRequires:  gtest-devel
BuildRequires:  rocrand-devel
BuildRequires:  fftw-devel
BuildRequires:  boost-devel
BuildRequires:  libomp-devel
BuildRequires:  hiprand-devel
%endif
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  sqlite-devel
BuildRequires:  python3-sphinx

# Only x86_64 works right now:
ExclusiveArch:  x86_64


Patch0: 0001-cmake-use-gnu-installdirs.patch

# the kernel cache is desired in most cases but it takes a long time to build
# and there are cases where it's nice to be able to disable that part of the 
# build

# https://github.com/ROCmSoftwarePlatform/rocFFT/pull/443
Patch2: 0002-add-kernel-cache-option.patch

# upstream hardcodes rpath for the tests
Patch3: 0003-remove-tests-hardcoded-rpath.patch

# version change was missed for 6.0 release, will be in next point release
Patch4: 0004-upstream-fix-version-number.patch

%description
A library for computing Fast Fourier Transforms (FFT), part of ROCm.

%package devel
Summary:        The rocFFT development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The rocFFT development package.

%if %{with check}
%package test
Summary:        Tests for the rocFFT package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
self tests for the rocfft library
%endif

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p 1


%build

# ensuring executables are PIE enabled
export LDFLAGS="${LDFLAGS} -pie"

# OpenMP tests are disabled because upstream sets rpath in that case without
# a way to skip

%cmake \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_C_COMPILER=hipcc \
%if %{with check}
    -DBUILD_CLIENTS_TESTS=ON \
    -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
%endif
%if %{with rocm-debug}
    -DCMAKE_BUILD_TYPE=Debug \
%else
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%endif
%if %{with kernelcache}
    -DROCFFT_KERNEL_CACHE_ENABLE=ON \
%else
    -DROCFFT_KERNEL_CACHE_ENABLE=OFF \
%endif
    -DROCFFT_BUILD_OFFLINE_TUNER=ON \
    -DROCM_SYMLINK_LIBS=OFF \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DSQLITE_USE_SYSTEM_PACKAGE=ON \
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=FALSE \
    -DCMAKE_SKIP_RPATH=TRUE \
    -DFETCH_CONTENT_FULLY_DISCONNECTED=ON \
    -DFETCH_CONTENT_QUIET=ON

%cmake_build -j

%install
%cmake_install

# we don't need the rocfft_rtc_helper binary, don't package it
rm -rf %{buildroot}/%{_libdir}/rocfft/%{rocfft_version}

# we don't need or want the client-info file installed by rocfft
rm -rf %{buildroot}/%{_prefix}/.info

# remove the license file that is installed by cmake
rm %{buildroot}/%{_docdir}/%{name}/LICENSE.md

# docs require rocm-docs-core which is not yet packaged, will complete once that is packaged
# install the samples as documentation
cp --preserve=timestamps -r docs/samples %{buildroot}/%{_docdir}/%{name}/.
rm %{buildroot}/%{_docdir}/%{name}/samples/CMakeLists.txt

# the checks for this package require a supported AMD GPU and thus aren't enabled during build
# the upstream test suite can be compiled into a subpackage, though.

%files
%doc README.md
%license LICENSE.md
%if %{with rocm-debug}
%{_libdir}/lib%{name}-d.so.0{,.*}
%else
%{_libdir}/lib%{name}.so.0{,.*}
%endif

%if %{with kernelcache}
%{_libdir}/rocfft_kernel_cache.db
%endif


%files devel
%if %{with rocm-debug}
%{_libdir}/lib%{name}-d.so
%else
%{_libdir}/lib%{name}.so
%endif
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_docdir}/%{name}/samples/

%if %{with check}
%files test
%if %{with rocm-debug}
%{_bindir}/rocfft-test-d
%else
%{_bindir}/rocfft-test
%endif
%{_bindir}/rtc_helper_crash
%endif

%changelog
%autochangelog

