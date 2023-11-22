%global upstreamname hipBLAS
%global rocm_release 5.7
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# $gpu will be evaluated in the loops below             
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

# It is necessary to use this with a local build
# export QA_RPATHS=0xff
%bcond_with test

# gfortran and clang rpm macros do not mix
%global build_fflags %{nil}

Name:           hipblas
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm BLAS marshalling library
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  compiler-rt
BuildRequires:  gcc-gfortran
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  ninja-build
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules

%if %{with test}

# test parallel building broken
%global _smp_mflags -j1

BuildRequires:  gtest-devel
BuildRequires:  blas-static
BuildRequires:  lapack-static
%endif

Requires:       rocm-rpm-macros-modules

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipBLAS is a Basic Linear Algebra Subprograms (BLAS) marshalling
library, with multiple supported backends. It sits between the
application and a 'worker' BLAS library, marshalling inputs into
the backend library and marshalling results back to the
application. hipBLAS exports an interface that does not require
the client to change, regardless of the chosen backend. Currently,
hipBLAS supports rocBLAS and cuBLAS as backends.

%package devel
Summary:        Libraries and headers for %{name}
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
           -DBUILD_WITH_SOLVER=OFF \
%if %{with test}
           %rocm_cmake_test_options \
%endif

    %cmake_build
    module purge
done

%install

for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

%files
%dir %{_libdir}/cmake/%{name}/
%license LICENSE.md
%exclude %{_docdir}/%{name}/LICENSE.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/rocm/gfx*/lib/lib%{name}.so.*


%files devel
%doc README.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/rocm/gfx*/lib/lib%{name}.so
%{_libdir}/rocm/gfx*/lib/cmake/%{name}/

%if %{with test}
%files test
%{_bindir}/%{name}*
%{_libdir}/rocm/gfx*/bin/%{name}*
%endif

%changelog
* Wed Nov 15 2023 Tom Rix <trix@redhat.com> - 5.7.1-1
- Initial package
