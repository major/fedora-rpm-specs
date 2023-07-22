%global upstreamname hipCUB

%global rocm_release 5.6
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# Compiler is hipcc, which is clang based:
%global toolchain clang
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')
# there is no debug package
%global debug_package %{nil}

# Option to test suite for testing on real HW:
%bcond_with check

Name:           hipcub
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        ROCm port of CUDA CUB library

Url:            https://github.com/ROCmSoftwarePlatform
License:        MIT and BSD-3-Clause
Source0:        %{url}/%{upstreamname}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
%if %{with check}
BuildRequires:  gtest-devel
%endif
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocprim-static
BuildRequires:  rocm-runtime-devel

# Only headers, cmake infra
BuildArch: noarch
# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipCUB is a thin wrapper library on top of rocPRIM or CUB. It enables developers
to port a project using the CUB library to the HIP layer to run on AMD hardware.
In the ROCm environment, hipCUB uses the rocPRIM library as the backend.

%package devel
Summary:        The %{upstreamname} development package
Provides:       %{name}-static = %{version}-%{release}

%description devel
The %{upstreamname} development package.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
%if %{with check}
    -DBUILD_TEST=ON \
%endif
    -DCMAKE_INSTALL_LIBDIR=share \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DROCM_SYMLINK_LIBS=OFF
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}/usr/lib/cmake %{buildroot}%{_datadir}

%check
%if %{with check}
%ctest
%endif

%files devel
%doc README.md
%license %{_docdir}/%{name}/LICENSE.txt
%{_includedir}/%{name}
%{_datadir}/cmake/%{name}

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 8 2023 Tom Rix <trix@redhat.com> - 5.6.0-2
- Review changes

* Sun Jul 2 2023 Tom Rix <trix@redhat.com> - 5.6.0-1
- Initial package
