%global upstreamname rocRAND

%global rocm_release 6.0
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

# Compiler is hipcc, which is clang based:
%global toolchain clang
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Option to test suite for testing on real HW:
%bcond_with check

Name:           rocrand
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm random number generator

Url:            https://github.com/ROCm/rocRAND
License:        MIT and BSD
Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  glibc-headers
%if %{with check}
BuildRequires:  gtest-devel
%endif
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
The rocRAND project provides functions that generate pseudo-random and
quasi-random numbers.

The rocRAND library is implemented in the HIP programming language and
optimised for AMD's latest discrete GPUs. It is designed to run on top of AMD's
Radeon Open Compute ROCm runtime, but it also works on CUDA enabled GPUs.

%package devel
Summary:        The rocRAND development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The rocRAND development package.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
%if %{with check}
    -DBUILD_TEST=ON \
%endif
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DROCM_SYMLINK_LIBS=OFF
%cmake_build

%install
%cmake_install

%check
%if %{with check}
%ctest
%endif

%files
%doc README.md
%license %{_docdir}/%{name}/LICENSE.txt
%{_libdir}/lib%{name}.so.1{,.*}
%if %{with check}
%{_bindir}/test_*
%exclude %{_bindir}/test_hiprand*
%exclude %{_bindir}/*RAND/
%endif

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}

%changelog
%autochangelog
