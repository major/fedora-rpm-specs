%global upstreamname rocBLAS
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

Name:           rocblas
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        BLAS implementation for ROCm
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        MIT AND BSD-3-Clause

Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch0:         0001-prepare-rocblas-cmake-for-fedora.patch

BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  compiler-rt
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules

%if %{with test}
BuildRequires:  gtest-devel
BuildRequires:  blas-devel
BuildRequires:  libomp-devel
BuildRequires:  python3-pyyaml
BuildRequires:  rocminfo
%endif

Requires:       rocm-rpm-macros-modules

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocBLAS is the AMD library for Basic Linear Algebra Subprograms
(BLAS) on the ROCm platform. It is implemented in the HIP
programming language and optimized for AMD GPUs.

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
%if %{with test}
           %rocm_cmake_test_options \
%endif
           -DBUILD_WITH_TENSILE=OFF

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
* Sun Oct 22 2023 Tom Rix <trix@redhat.com> - 5.7.1-3
- Change url
- capitalize AND

* Sat Oct 21 2023 Tom Rix <trix@redhat.com> - 5.7.1-2
- Fix so location
- glob gpu family location

* Sun Oct 15 2023 Tom Rix <trix@redhat.com> - 5.7.1-1
- Update to 5.7.1
- Use rocm-rpm-macros

* Sat Oct 7 2023 Tom Rix <trix@redhat.com> - 5.7.0-1
- Update to 5.7
- Use WIP rocm-rpm-macros
- Convert to environent modules

* Sun Oct 1 2023 Tom Rix <trix@redhat.com> - 5.6.0-2
- Split the build into gpu families

* Sat Sep 23 2023 Tom Rix <trix@redhat.com> - 5.6.0-1
- Update to 5.6

* Tue Jun 6 2023 Tom Rix <trix@redhat.com> - 5.5.1-1
- Initial package
