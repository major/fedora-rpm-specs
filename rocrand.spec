%global upstreamname rocRAND

%global rocm_release 5.7
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

# Compiler is hipcc, which is clang based:
%global toolchain clang
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Option to test suite for testing on real HW:
%bcond_with check

Name:           rocrand
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm random number generator

Url:            https://github.com/ROCmSoftwarePlatform
License:        MIT and BSD
Source0:        %{url}/%{upstreamname}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# Someone forgot to tag 5.6.0
Source1:        %{url}/hipRAND/archive/c7b8bcfa7d3907b9e00911f17761d6f51b1636c7.tar.gz#/hipRAND-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  doxygen
BuildRequires:  glibc-headers
%if %{with check}
BuildRequires:  gtest-devel
%endif
BuildRequires:  lld
BuildRequires:  llvm-devel
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

%package -n hiprand
Summary:        HIP random number generator
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n hiprand
hipRAND is a RAND marshalling library, with multiple supported backends. It
sits between the application and the backend RAND library, marshalling inputs
into the backend and results back to the application. hipRAND exports an
interface that does not require the client to change, regardless of the chosen
backend. Currently, hipRAND supports either rocRAND or cuRAND.

%package -n hiprand-devel
Summary:        The hipRAND development package
Requires:       hiprand%{?_isa} = %{version}-%{release}

%description -n hiprand-devel
The hipRAND development package.

%prep
%autosetup -p1 -a 1 -n %{upstreamname}-rocm-%{version}

#hipRAND is a git submodule of rocRAND, so it expects a specific DIR name:
mv hipRAND-*/* hipRAND/

#Remove RPATH:
sed -i '/INSTALL_RPATH/d' hipRAND/library/CMakeLists.txt

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
%license LICENSE.txt
%{_libdir}/lib%{name}.so.1{,.*}
%exclude %{_docdir}/%{name}/LICENSE.txt
%if %{with check}
%{_bindir}/test_*
%exclude %{_bindir}/test_hiprand*
%exclude %{_bindir}/*RAND/
%endif

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}

%files -n hiprand
%doc hipRAND/README.md
%license hipRAND/LICENSE.txt
%{_libdir}/libhiprand.so.1{,.*}
%if %{with check}
%{_bindir}/test_hiprand*
%endif

%files -n hiprand-devel
%{_libdir}/libhiprand.so
%{_includedir}/hiprand
%{_libdir}/cmake/hiprand

%changelog
* Fri Oct 20 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.7.1-1
- Update to 5.7.1

* Tue Oct 03 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.7.0-1
- Update to 5.7

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.6.0-1
- Update to 5.6

* Fri Jun 16 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-3
- Fix hardening flags
- Fix license field

* Sat Jun 10 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-2
- Add with check option (requires HW), useful for CI or manual tests
- Drop chrpath, patch the cmake in prep instead
- Package README.md's instead of CHANGLOG.md files
- clean up in build section
- rpmlint fixes

* Fri Jun 09 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-1
- Initial package
