%global upstreamname rocPRIM
%global rocm_release 5.5
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
# Compiler is hipcc, which is clang based:
%global toolchain clang
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')
# there is no debug package
%global debug_package %{nil}

# Option to test suite for testing on real HW:
%bcond_with check

Name:           rocprim
Version:        %{rocm_version}
Release:        4%{?dist}
Summary:        ROCm parallel primatives

License:        MIT and BSD 3-Clause License

URL:            https://github.com/rocmsoftwareplatform/%{name}
Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# Only headers, cmake infra
BuildArch: noarch
# ROCm only working on x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  doxygen
%if %{with check}
BuildRequires:  gtest-devel
%endif
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel

%description
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%package devel
Summary:        ROCm parallel primatives
Provides:       rocprim-static = %{version}-%{release}

%description devel
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%prep
%setup -q -n %{upstreamname}-rocm-%{version}

%build
%cmake \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
%if %{with check}
    -DBUILD_TEST=ON \
%endif
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build


%install
%cmake_install

cp NOTICES.txt %{buildroot}%{_docdir}/rocprim/

%if %{with check}
%ctest
%endif

%files devel
%{_docdir}/rocprim
%doc README.md
%license %{_docdir}/rocprim/LICENSE.txt
%license %{_docdir}/rocprim/NOTICES.txt
%{_includedir}/%{name}
%{_datadir}/cmake/rocprim

%changelog
* Tue Jun 20 2023 Tom Rix <trix@redhat.com> - 5.5.1-4
- For cxx flags change

* Fri Jun 16 2023 Tom Rix <trix@redhat.com> - 5.5.1-3
- Cleanup licenses
- Cleanup docdir ownership

* Thu Jun 15 2023 Tom Rix <trix@redhat.com> - 5.5.1-2
- add provides rocprim-static
- change *.cmake install location
- fix bad include dir another way
- add doxygen proactively for expected upstream change
- add NOTICES.txt to license files

* Tue Jun 6 2023 Tom Rix <trix@redhat.com> - 5.5.1-1
- Initial package
