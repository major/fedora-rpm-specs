%global upstreamname hipFFT
%global rocm_release 6.0
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Only good for testing with a local gpu
# Need to
# export QA_RPATHS=0xff
%bcond_with test

# https://github.com/ROCm/hipFFT/issues/83
# Fixed on the 6.0 branch with this commit
%global commit0 18c75d803dfd52bfd7cd07d8a4cede64bb945078
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           hipfft
Version:        %{rocm_version}.%{shortcommit0}
Release:        %autorelease
Summary:        ROCm FFT marshalling library
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT

# Only x86_64 works right now
ExclusiveArch:  x86_64

Source0:        %{url}/archive/%{commit0}/hipfft-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocprim-devel
BuildRequires:  rocfft-devel

%if %{with test}
BuildRequires:  boost-devel
BuildRequires:  fftw-devel
BuildRequires:  gtest-devel
BuildRequires:  hiprand-devel
BuildRequires:  libomp-devel
BuildRequires:  rocrand-devel
%endif

%description
hipFFT is an FFT marshalling library. Currently, hipFFT supports
the rocFFT backends

hipFFT exports an interface that does not require the client to
change, regardless of the chosen backend. It sits between the
application and the backend FFT library, marshalling inputs into
the backend and results back to the application.

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
%autosetup -p1 -n hipFFT-%{commit0}

%build
%cmake -G Ninja \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
%if %{with test}
       -DBUILD_CLIENTS_TESTS=ON \
%endif
       -DROCM_SYMLINK_LIBS=OFF \
       -DHIP_PLATFORM=amd \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

%install
%cmake_install

%files
%license LICENSE.md
%exclude %{_docdir}/%{name}/LICENSE.md
%{_libdir}/lib%{name}.so.*

%files devel
%dir %{_libdir}/cmake/%{name}

%doc README.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/lib%{name}.so

%if %{with test}
%files test
%{_bindir}/hipfft-test
%endif

%changelog
%autochangelog


