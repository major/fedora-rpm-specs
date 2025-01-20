%global upstreamname RCCL
%global rocm_release 6.3
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-flto=thin//' )

%global _lto_cflags %{nil}

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# downloads tests, use mock --enable-network
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif

# rccl is not supported on gfx1103
# On 6.1.1
# lld: error: ld-temp.o <inline asm>:1:25: specified hardware register is not supported on this GPU
#        s_getreg_b32 s1, hwreg(HW_REG_HW_ID)
#
# On 6.2
# Problems reported with gfx10, removing gfx10 and default (gfx10 and gfx11) from build list
#
# Handle with a custom gpu list
# Because this package is a leaf, set it to the minimum until there is a request for
# more support or it is used by another package
%global rccl_gpu_list "gfx90a:xnack+;gfx90a:xnack-;gfx1100;gfx1101;gfx1102;gfx1200;gfx1201"

Name:           rccl
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        ROCm Communication Collectives Library

Url:            https://github.com/ROCm/rccl
License:        BSD-3-Clause AND MIT AND Apache-2.0
# From License.txt the main license is BSD 3
# Modifications from Microsoft is MIT
# The NVIDIA based header files below are Apache-2.0
#  src/include/nvtx3/nv*.h and similar
# The URL for NVIDIA in the License.txt https://github.com/NVIDIA/NVTX is Apache-2.0

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  hipify
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-smi-devel

%if %{with test}
BuildRequires:  gtest-devel
%endif

Requires:       %{name}-data = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
RCCL (pronounced "Rickle") is a stand-alone library of standard
collective communication routines for GPUs, implementing all-reduce,
all-gather, reduce, broadcast, reduce-scatter, gather, scatter, and
all-to-all. There is also initial support for direct GPU-to-GPU
send and receive operations. It has been optimized to achieve high
bandwidth on platforms using PCIe, xGMI as well as networking using
InfiniBand Verbs or TCP/IP sockets. RCCL supports an arbitrary
number of GPUs installed in a single node or multiple nodes, and
can be used in either single- or multi-process (e.g., MPI)
applications.

The collective operations are implemented using ring and tree
algorithms and have been optimized for throughput and latency. For
best performance, small operations can be either batched into
larger operations or aggregated through the API.

%package devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for %{name}

%package data
Summary:        Data for %{name}
BuildArch:      noarch

%description data
Data for %{name}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{name}-rocm-%{version}

# Allow user to set AMDGPU_TARGETS
sed -i -e '/AMD GPU targets to compile for/d' CMakeLists.txt

# No /opt/rocm/.info/version
sed -i -e 's@cat ${ROCM_PATH}/.info/version@echo %{rocm_version}@' CMakeLists.txt

# wrong path
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' src/include/hip_rocm_version_info.h

%build
%cmake \
    -DBUILD_TESTS=%{build_test} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_CXX_COMPILER=/usr/bin/hipcc \
    -DCMAKE_C_COMPILER=/usr/bin/hipcc \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DROCM_SYMLINK_LIBS=OFF \
    -DAMDGPU_TARGETS=%{rccl_gpu_list} \
    -DHIP_PLATFORM=amd \
    -DRCCL_ROCPROFILER_REGISTER=OFF


%cmake_build

%install
%cmake_install

echo s@%{buildroot}@@ > br.sed
find %{buildroot}%{_libdir} -name '*.so.*.[0-9]' | sed -f br.sed >  %{name}.files
find %{buildroot}%{_libdir} -name '*.so.[0-9]'   | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name '*.so'         | sed -f br.sed >  %{name}.devel
find %{buildroot}%{_libdir} -name '*.cmake'      | sed -f br.sed >> %{name}.devel
%if %{with test}
find %{buildroot}           -name '%{name}*'     | sed -f br.sed >  %{name}.test
%endif

if [ -f %{buildroot}%{_prefix}/share/doc/%{name}/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/%{name}/LICENSE.txt
fi

%files -f %{name}.files
%license LICENSE.txt

%files data
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/msccl-algorithms
%dir %{_datadir}/%{name}/msccl-unit-test-algorithms
%{_datadir}/%{name}/msccl-algorithms/*.xml
%{_datadir}/%{name}/msccl-unit-test-algorithms/*.xml

%files devel -f %{name}.devel
%doc README.md
%dir %{_includedir}/%{name}
%dir %{_libdir}/cmake/%{name}
%{_includedir}/%{name}/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
* Sat Jan 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- Add gfx1200,gfx1201

* Fri Dec 27 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- Add --with export
- Remove unneeded requires rocm-rpm-macros-modules

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3


