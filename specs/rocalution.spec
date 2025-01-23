%global upstreamname rocALUTION
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
%global debug_package %{nil}
%endif

%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio

Name:           rocalution
Version:        %{rocm_version}
Release:        4%{?dist}
Summary:        Next generation library for iterative sparse solvers for ROCm platform
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# combine libs because of circular dependency reported in fedora-review
# Patch0:         0001-prepare-rocalution-cmake-for-fedora.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocprim-devel
BuildRequires:  rocrand-devel
BuildRequires:  rocsparse-devel

%if %{with test}
BuildRequires:  gtest-devel
%endif

Requires:  rocm-rpm-macros-modules

%description
rocALUTION is a sparse linear algebra library that can be used
to explore fine-grained parallelism on top of the ROCm platform
runtime and toolchains. Based on C++ and HIP, rocALUTION
provides a portable, generic, and flexible design that allows
seamless integration with other scientific software packages.

rocALUTION offers various backends for different (parallel) hardware:

Host
* OpenMP: Designed for multi-core CPUs
* HIP: Designed for ROCm-compatible devices
* MPI: Designed for multi-node clusters and multi-GPU setups

%package devel
Summary: Libraries and headers for %{name}
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

%build
for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    %cmake \
	-DCMAKE_CXX_COMPILER=hipcc \
	-DCMAKE_C_COMPILER=hipcc \
	-DCMAKE_EXE_LINKER_FLAGS=-fuse-ld=%rocmllvm_bindir/ld.lld \
	-DCMAKE_SHARED_LINKER_FLAGS=-fuse-ld=%rocmllvm_bindir/ld.lld \
	-DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
	-DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
	-DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
	-DCMAKE_SKIP_RPATH=ON \
	-DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
	   -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
	   -DROCM_SYMLINK_LIBS=OFF \
	   -DHIP_PLATFORM=amd \
	   -DAMDGPU_TARGETS=$ROCM_GPUS \
	   -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
	   -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
           -DCMAKE_MODULE_PATH=%{_libdir}/cmake/hip \
           -DHIP_ROOT_DIR=%{_prefix} \
           -DCMAKE_BUILD_TYPE=%{build_type} \
           -DBUILD_CLIENTS_TESTS=%{build_test}

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
find %{buildroot}%{_libdir} -name '*.so'         | sed -f br.sed >  %{name}.devel
find %{buildroot}%{_libdir} -name '*.cmake'      | sed -f br.sed >> %{name}.devel
%if %{with test}
find %{buildroot}           -name '%{name}*'     | sed -f br.sed >  %{name}.test
%endif

if [ -f %{buildroot}%{_prefix}/share/doc/rocalution/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocalution/LICENSE.md
fi

%files -f %{name}.files
%license LICENSE.md

%files devel -f %{name}.devel
%doc README.md
%dir %{_libdir}/cmake/%{name}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- multithread compress

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed

