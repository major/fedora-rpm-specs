#Image support is x86 only
%ifarch x86_64
%global enableimage 1
%endif
%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%if 0%{?suse_version}
%bcond_with kfdtest
%else
%bcond_without kfdtest
%endif

%bcond_without compat_gcc
%if %{with compat_gcc}
%global compat_gcc_major 13
%global gcc_major_str -13
%else
%global compat_gcc_major %{nil}
%global gcc_major_str %{nil}
%endif

Name:       rocm-runtime
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    ROCm Runtime Library

License:    NCSA
URL:        https://github.com/ROCm/ROCR-Runtime
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc%{compat_gcc_major}-c++
BuildRequires:  libdrm-devel
BuildRequires:  libffi-devel
BuildRequires:  rocm-llvm-static
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-device-libs

%if 0%{?suse_version}
BuildRequires:  libelf-devel
BuildRequires:  libnuma-devel
BuildRequires:  xxd
%else
BuildRequires:  elfutils-libelf-devel
BuildRequires:  numactl-devel
BuildRequires:  vim-common
%endif

Obsoletes:  hsakmt < 6.3

%description
The ROCm Runtime Library is a thin, user-mode API that exposes the necessary
interfaces to access and interact with graphics hardware driven by the AMDGPU
driver set and the AMDKFD kernel driver. Together they enable programmers to
directly harness the power of AMD discrete graphics devices by allowing host
applications to launch compute kernels directly to the graphics hardware.

%package devel
Summary: ROCm Runtime development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:  hsakmt-devel = %{version}-%{release}

%description devel
ROCm Runtime development files

%if %{with kfdtest}
%package -n kfdtest
Summary: Test suite for ROCm's KFD kernel module
Requires: rocm-smi

%description -n kfdtest
This package includes ROCm's KFD kernel module test suite (kfdtest), the list of
excluded tests for each ASIC, and a convenience script to run the test suite.
%endif

%prep
%autosetup -n ROCR-Runtime-rocm-%{version} -p1

# Use llvm's static libs kfdtest
sed -i -e 's@LLVM_LINK_LLVM_DYLIB@0@' libhsakmt/tests/kfdtest/CMakeLists.txt

%build

export PATH=%{rocmllvm_bindir}:$PATH

export CC=/usr/bin/gcc%{gcc_major_str}
export CXX=/usr/bin/g++%{gcc_major_str}

%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_SHARED_LINKER_FLAGS=-ldrm_amdgpu \
    -DINCLUDE_PATH_COMPATIBILITY=OFF \
    %{?!enableimage:-DIMAGE_SUPPORT=OFF}
%cmake_build

%if %{with kfdtest}
export LIBHSAKMT_PATH=$(pwd)/%__cmake_builddir/libhsakmt/archive
cd libhsakmt/tests/kfdtest
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_RPATH=ON -DLLVM_DIR=%{rocmllvm_cmakedir}
%cmake_build
%endif

%install
%cmake_install

%if %{with kfdtest}
cd libhsakmt/tests/kfdtest
%cmake_install
%endif

if [ -f %{buildroot}%{_prefix}/share/doc/hsa-runtime64/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/hsa-runtime64/LICENSE.md
elif [ -f %{buildroot}%{_prefix}/share/doc/packages/rocm-runtime/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/rocm-runtime/LICENSE.md
fi

if [ -f %{buildroot}%{_libdir}/libhsakmt.a ]; then
    rm %{buildroot}%{_libdir}/libhsakmt.a
fi
if [ -f %{buildroot}%{_libdir}/libhsakmt.so ]; then
    rm %{buildroot}%{_libdir}/libhsakmt.*
fi
if [ -d %{buildroot}%{_includedir}/hsakmt ]; then
    rm -rf %{buildroot}%{_includedir}/hsakmt
fi
if [ -d %{buildroot}%{_libdir}/cmake/hsakmt ]; then
    rm -rf %{buildroot}%{_libdir}/cmake/hsakmt
fi
if [ -f %{buildroot}%{_libdir}/pkgconfig/libhsakmt.pc ]; then
    rm %{buildroot}%{_libdir}/pkgconfig/libhsakmt.pc
fi

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/libhsa-runtime64.so.1{,.*}

%files devel
%{_includedir}/hsa/
%{_libdir}/libhsa-runtime64.so
%{_libdir}/cmake/hsa-runtime64/

%if %{with kfdtest}
%files -n kfdtest
%doc libhsakmt/tests/kfdtest/README.txt
%license libhsakmt/tests/kfdtest/LICENSE.kfdtest
%{_bindir}/kfdtest
%{_bindir}/run_kfdtest.sh
%{_datadir}/kfdtest
%endif

%changelog
* Thu Jan 9 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- Use compat gcc

* Sun Dec 22 2024 Tom Rix <Tom.Rix@amc.com> - 6.3.1-1
- Update to 6.3.1

* Fri Dec 20 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- Link kfdtest with static llvm libs

* Sat Dec 7 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 3 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed

