%global upstreamname rocALUTION
%global rocm_release 5.7
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# No debug source produced
%global debug_package %{nil}

# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

# For testing
%bcond_with test

Name:           rocalution
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        Next generation library for iterative sparse solvers for ROCm platform
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        MIT

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# combine libs because of circular dependency reported in fedora-review
Patch0:         0001-prepare-rocalution-cmake-for-fedora.patch

BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  compiler-rt
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  ninja-build
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
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
    %cmake %rocm_cmake_options \
           -DCMAKE_MODULE_PATH=%{_libdir}/cmake/hip \
           -DHIP_ROOT_DIR=%{_prefix} \
%if %{with test}
           -DBUILD_CLIENTS_TESTS=ON
%endif

    %cmake_build
    module purge
done

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

# fedora-review complains these are unstripped
# strip *.so
strip %{buildroot}%{_libdir}/librocalution.so.0.*
strip %{buildroot}%{_libdir}/rocm/gfx10/lib/librocalution.so.0.*
strip %{buildroot}%{_libdir}/rocm/gfx11/lib/librocalution.so.0.*
strip %{buildroot}%{_libdir}/rocm/gfx8/lib/librocalution.so.0.*
strip %{buildroot}%{_libdir}/rocm/gfx9/lib/librocalution.so.0.*

%files
%license LICENSE.md
%exclude %{_docdir}/%{name}/LICENSE.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/rocm/gfx*/lib/lib%{name}.so.*

%files devel
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/base
%dir %{_includedir}/%{name}/solvers
%dir %{_includedir}/%{name}/utils
%dir %{_includedir}/%{name}/solvers/direct
%dir %{_includedir}/%{name}/solvers/krylov
%dir %{_includedir}/%{name}/solvers/multigrid
%dir %{_includedir}/%{name}/solvers/preconditioners
%dir %{_libdir}/cmake/%{name}
%dir %{_libdir}/rocm/gfx8/lib/cmake/%{name}
%dir %{_libdir}/rocm/gfx9/lib/cmake/%{name}
%dir %{_libdir}/rocm/gfx10/lib/cmake/%{name}
%dir %{_libdir}/rocm/gfx11/lib/cmake/%{name}

%doc README.md
%{_includedir}/%{name}/*.hpp
%{_includedir}/%{name}/base/*.hpp
%{_includedir}/%{name}/utils/*.hpp
%{_includedir}/%{name}/solvers/*.hpp
%{_includedir}/%{name}/solvers/direct/*.hpp
%{_includedir}/%{name}/solvers/krylov/*.hpp
%{_includedir}/%{name}/solvers/multigrid/*.hpp
%{_includedir}/%{name}/solvers/preconditioners/*.hpp
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/lib%{name}.so
%{_libdir}/rocm/gfx*/lib/lib%{name}.so
%{_libdir}/rocm/gfx*/lib/cmake/%{name}/*.cmake

%if %{with test}
%files test
%{_bindir}/%{name}*
%{_libdir}/rocm/gfx*/bin/%{name}*
%endif

%changelog
* Sat Nov 18 2023 Tom Rix <trix@redhat.com> 5.7.1-2
- Add modules to the requires

* Sat Nov 11 2023 Tom Rix <trix@redhat.com> 5.7.1-1
- Initial project
