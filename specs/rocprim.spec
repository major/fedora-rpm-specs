%global upstreamname rocPRIM
%global rocm_release 6.4
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
# Compiler is hipcc, which is clang based:
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')
# there is no debug package
%global debug_package %{nil}

# Option to test suite for testing on real HW during build
%bcond_with check
# Option to build test subpackage
%bcond_with test

# For documentation
%bcond_with doc

Name:           rocprim
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        ROCm parallel primatives

License:        MIT AND BSD-3-Clause

URL:            https://github.com/ROCm/%{name}
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# ROCm only working on x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  python3dist(marshalparser)
%endif

%if %{with check} || %{with test}
BuildRequires:  gtest-devel
%endif

%description
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%package devel
Summary:        ROCm parallel primatives
Provides:       rocprim-static = %{version}-%{release}

# the devel subpackage is only headers and cmake infra
BuildArch: noarch

%description devel
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%if %{with test}
%package test
Summary:        upstream tests for ROCm parallel primatives
Provides:       rocprim-test = %{version}-%{release}
Requires:       rocprim-devel
Requires:       gtest

%description test
tests for the rocPRIM package
%endif

%prep
%setup -q -n %{upstreamname}-rocm-%{version}

%build
%cmake \
	-DCMAKE_CXX_COMPILER=hipcc \
	-DCMAKE_C_COMPILER=hipcc \
	-DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
	-DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
	-DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
%if %{with check} || %{with test}
    -DBUILD_TEST=ON \
%endif
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build


%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/rocprim/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocprim/LICENSE.txt
fi

%if %{with test}
# force the cmake test file to use absolute paths for its referenced binaries
sed -i -e 's@\.\.@\/usr\/bin@' %{buildroot}%{_bindir}/%{name}/CTestTestfile.cmake
%endif

%if %{with check}
%check
%ctest
%endif

%files devel
%doc README.md
%license LICENSE.txt
%license NOTICES.txt
%{_includedir}/%{name}
%{_datadir}/cmake/rocprim

%if %{with test}
%files test
%{_bindir}/test*
%dir %{_bindir}/%{name}
%{_bindir}/%{name}/CTestTestfile.cmake
%endif


%changelog
* Mon May 5 2025 Tim Flink <tflink@fedoraproject.org> - 6.4.0-2
- create test subpackage and add --with test flag
- move during-build checks to %check section
- change build to be noarch only for -devel subpackage so that arch-specific tests could be packaged in -test

* Fri Apr 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Fri Apr 4 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- Use correct spdx license

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Mon Dec 9 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed
