%global upstreamname hipSPARSE
%global rocm_release 6.0
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

# Tests are downloaded so this option is only good for local building
# Also need to
# export QA_RPATHS=0xff
%bcond_with test

# gfortran and clang rpm macros do not mix
%global build_fflags %{nil}

Name:           hipsparse
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm SPARSE marshalling library
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        MIT

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
# Really turn the samples off
Patch0:         0001-prepare-hipsparse-cmake-for-fedora.patch

BuildRequires:  cmake
BuildRequires:  gcc-gfortran
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocprim-devel
BuildRequires:  rocsparse-devel

%if %{with test}
BuildRequires:  gtest-devel
BuildRequires:  libomp-devel
BuildRequires:  rocblas-devel
%endif

Requires:       rocm-rpm-macros-modules

%description
hipSPARSE is a SPARSE marshalling library with multiple
supported backends. It sits between your application and
a 'worker' SPARSE library, where it marshals inputs to
the backend library and marshals results to your
application. hipSPARSE exports an interface that doesn't
require the client to change, regardless of the chosen
backend. Currently, hipSPARSE supports rocSPARSE and
cuSPARSE backends.

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
           -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{with test}
           %rocm_cmake_test_options
%endif

    %cmake_build
    module purge
done

%cmake_build

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

%files
%license LICENSE.md
%exclude %{_docdir}/%{name}/LICENSE.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/rocm/gfx*/lib/lib%{name}.so.*

%files devel
%dir %{_libdir}/cmake/%{name}
%dir %{_libdir}/rocm/gfx*/lib/cmake/%{name}

%doc README.md
%{_includedir}/%{name}
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
%autochangelog
