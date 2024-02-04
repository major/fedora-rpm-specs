%global upstreamname hipRAND

%global rocm_release 6.0
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Option to test suite for testing on real HW:
%bcond_with test

Name:           hiprand
Version:        %{rocm_version}
Release:        %autorelease
Summary:        HIP random number generator

Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT and BSD
Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  doxygen
BuildRequires:  glibc-headers
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocrand-devel

%if %{with test}
BuildRequires:  gtest-devel
%endif

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipRAND is a RAND marshalling library, with multiple supported backends. It
sits between the application and the backend RAND library, marshalling inputs
into the backend and results back to the application. hipRAND exports an
interface that does not require the client to change, regardless of the chosen
backend. Currently, hipRAND supports either rocRAND or cuRAND.

%package devel
Summary:        The hipRAND development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rocrand-devel

%description devel
The hipRAND development package.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

#Remove RPATH:
sed -i '/INSTALL_RPATH/d' CMakeLists.txt

%build
%cmake \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
%if %{with test}
    -DBUILD_TEST=ON \
%endif
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DROCM_SYMLINK_LIBS=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license %{_docdir}/%{name}/LICENSE.txt
%{_libdir}/lib%{name}.so.1{,.*}

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}

%if %{with test}
%files test
%{_bindir}/test_%{name}*
%endif

%changelog
%autochangelog
