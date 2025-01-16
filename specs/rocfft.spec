%global upstreamname rocFFT

%global rocm_release 6.3
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# rocFFT has a version seperate from the ROCm version that it is released with
%global rocfft_version 1.0.31

%global toolchain rocm

# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host-fcf-protection/')

# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

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


Name:           rocfft
Version:        %{rocm_version}
Release:        2%{?dist}
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
BuildRequires:  rocm-rpm-macros-modules

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

Requires:       rocm-rpm-macros-modules

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Patch0: 0001-cmake-use-gnu-installdirs.patch

%description
A library for computing Fast Fourier Transforms (FFT), part of ROCm.

%package devel
Summary:        The rocFFT development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

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


%build

# ensuring executables are PIE enabled
export LDFLAGS="${LDFLAGS} -pie"

# OpenMP tests are disabled because upstream sets rpath in that case without
# a way to skip

for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu

    %cmake \
	-DCMAKE_CXX_COMPILER=hipcc \
	-DCMAKE_C_COMPILER=hipcc \
	-DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
	-DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
	-DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
	-DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
	-DAMDGPU_TARGETS=${ROCM_GPUS} \
    -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
    -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
    -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DROCFFT_BUILD_OFFLINE_TUNER=OFF \
    -DROCFFT_KERNEL_CACHE_ENABLE=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DSQLITE_USE_SYSTEM_PACKAGE=ON

    %cmake_build
    module purge
done

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

# we don't need the rocfft_rtc_helper binary, don't package it
find %{buildroot} -type d -name "%{rocfft_version}" -print0 | xargs -0 -I {} /usr/bin/rm -rf "{}"

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
%dir %{_libdir}/cmake/%{name}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
* Tue Jan 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Sun Dec 8 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed



