%global upstreamname hipSOLVER
%global rocm_release 6.0
%global rocm_patch 0
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

Name:           hipsolver
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm SOLVER marshalling library
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  clang
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
BuildRequires:  rocsolver-devel

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
hipSOLVER is a LAPACK marshalling library, with multiple supported
backends. It sits between the application and a 'worker'
LAPACK library, marshalling inputs into the backend library and
marshalling results back to the application. hipSOLVER exports an
interface that does not require the client to change, regardless
of the chosen backend. Currently, hipSOLVER supports rocSOLVER
and cuSOLVER as backends.

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
          -DCMAKE_BUILD_TYPE=RelWithDebugInfo \
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
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/test
%dir %{_datadir}/%{name}/test/mat_20_60
%dir %{_datadir}/%{name}/test/mat_20_100
%dir %{_datadir}/%{name}/test/mat_20_140
%dir %{_datadir}/%{name}/test/mat_50_60
%dir %{_datadir}/%{name}/test/mat_50_100
%dir %{_datadir}/%{name}/test/mat_50_140
%dir %{_datadir}/%{name}/test/mat_100_300
%dir %{_datadir}/%{name}/test/mat_100_500
%dir %{_datadir}/%{name}/test/mat_100_700
%dir %{_datadir}/%{name}/test/mat_250_300
%dir %{_datadir}/%{name}/test/mat_250_500
%dir %{_datadir}/%{name}/test/mat_250_700

%{_datadir}/%{name}/test/mat_20_60/*
%{_datadir}/%{name}/test/mat_20_100/*
%{_datadir}/%{name}/test/mat_20_140/*
%{_datadir}/%{name}/test/mat_50_60/*
%{_datadir}/%{name}/test/mat_50_100/*
%{_datadir}/%{name}/test/mat_50_140/*
%{_datadir}/%{name}/test/mat_100_300/*
%{_datadir}/%{name}/test/mat_100_500/*
%{_datadir}/%{name}/test/mat_100_700/*
%{_datadir}/%{name}/test/mat_250_300/*
%{_datadir}/%{name}/test/mat_250_500/*
%{_datadir}/%{name}/test/mat_250_700/*
%{_bindir}/%{name}*
%{_libdir}/rocm/gfx*/bin/%{name}*
%endif

%changelog
%autochangelog
