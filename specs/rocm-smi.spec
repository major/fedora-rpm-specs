#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname rocm-smi-lib

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix -%{rocm_release}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%global pkg_name rocm-smi%{pkg_suffix}

%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

%bcond_with doc

Name:       %{pkg_name}
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    ROCm System Management Interface Library

License:    MIT AND NCSA
URL:        https://github.com/ROCm/rocm-systems
Source0:    %{url}/releases/download/rocm-%{version}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

%if 0%{?rhel} || 0%{?suse_version}
ExclusiveArch:  x86_64
%else
# SMI requires the AMDGPU kernel module, which only builds on:
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64
%endif

BuildRequires:  cmake
%if %{with doc}
# Fedora 38 has doxygen 1.9.6
%if 0%{?fedora} > 38
BuildRequires:  doxygen >= 1.9.7
BuildRequires:  doxygen-latex >= 1.9.7
%endif
%endif
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel

%if %{with test}
BuildRequires:  gtest-devel
%endif

%description
The ROCm System Management Interface Library, or ROCm SMI library, is part of
the Radeon Open Compute ROCm software stack . It is a C library for Linux that
provides a user space interface for applications to monitor and control GPU
applications.

%package devel
Summary: ROCm SMI Library development files
Requires: %{name}%{?_isa} = %{version}-%{release}
# /usr/include/rocm_smi/kfd_ioctl.h:26:10: fatal error: 'libdrm/drm.h' file not found
Requires: libdrm-devel

%description devel
ROCm System Management Interface Library development files

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname} -p1

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

# Fix script shebang
sed -i -e 's@env python3@python3@' python_smi_tools/*.py
sed -i -e 's@env python3@python3@' python_smi_tools/rsmiBindingsInit.py.in

# do not download gtest and install
# https://github.com/ROCm/rocm-systems/issues/1022
sed -i -e 's@FetchContent_MakeAvailable(googletest)@#FetchContent_MakeAvailable(googletest)@' tests/rocm_smi_test/CMakeLists.txt
sed -i -e 's@PUBLIC GTest::gtest_main@PUBLIC gtest_main gtest@' tests/rocm_smi_test/CMakeLists.txt
sed -i -e '/TARGETS gtest gtest_main/,+3d' tests/rocm_smi_test/CMakeLists.txt

# fix iomanip include
# https://github.com/ROCm/rocm-systems/issues/1021
sed -i '/#include <string.*/a#include <iomanip>' tests/rocm_smi_test/test_base.h

%build
%cmake -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
       -DBUILD_TESTS=%{build_test}

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-smi-lib/LICENSE.md

%if 0%{?suse_version}
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc README.md
%license LICENSE.md
%{pkg_prefix}/bin/rocm-smi
%{pkg_prefix}/libexec/rocm_smi/
%{pkg_prefix}/%{pkg_libdir}/librocm_smi64.so.1{,.*}
%{pkg_prefix}/%{pkg_libdir}/liboam.so.1{,.*}

%files devel
%{pkg_prefix}/include/rocm_smi/
%{pkg_prefix}/include/oam/
%{pkg_prefix}/%{pkg_libdir}/librocm_smi64.so
%{pkg_prefix}/%{pkg_libdir}/liboam.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocm_smi/

%if %{with test}
%files test
%{pkg_prefix}/share/rsmitst_tests
%endif

%changelog
* Thu Dec 18 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-2
- Add --with compat

* Wed Nov 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-1
- Update to 7.1.1

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Fri Oct 10 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Tue Sep 16 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.0-1
- Update to 7.0.0

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-3
- Add Fedora copyright

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-2
- Simplify file removal

* Thu Aug 7 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-1
- Update to 6.4.3
- remove debian dir

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.2-1
- Update to 6.4.2

* Thu May 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.1-1
- Update to 6.4.1

* Sat Apr 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- devel requires libdrm-devel
- refactor empty return patch

* Wed Apr 16 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.0-1
- Update to 6.4.0

* Fri Jan 17 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-3
- Cleanup for suse

* Thu Jan 16 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- Update license and url
- Fix script shebangs

* Sun Dec 22 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

* Sat Dec 7 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 3 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed
