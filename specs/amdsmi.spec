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
%global rocm_release 7.2
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname amdsmi

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

# Downloads its own googletest
# Testing also depends on having AMD hardware cpu and/or gpu installed.
# Not suitable for a general check
#
# Non root result for gfx1100 and this kernel 6.13.0-0.rc0.20241126git7eef7e306d3c.10.fc42.x86_64
# 25 pass, 5 fail
# No oops
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

Name:       amdsmi%{pkg_suffix}
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    AMD System Management Interface

License:    MIT AND (GPL-2.0-only WITH Linux-syscall-note)
# Main license is MIT
# 
# This file is GPL-2.0
# include/amd_smi/impl/amd_hsmp.h

URL:        https://github.com/ROCm/%{upstreamname}
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# esmi_ib_library is not suitable for packaging
# https://github.com/amd/esmi_ib_library/issues/13
# This tag was choosen by the amdsmi project because 4.0+ introduced variables not
# found in the upstream kernel.
%global esmi_ver 4.2
Source1:    https://github.com/amd/esmi_ib_library/archive/refs/tags/esmi_pkg_ver-%{esmi_ver}.tar.gz
# https://github.com/ROCm/amdsmi/pull/165
Patch4:     0001-Fix-compilation-with-libdrm-2.4.130.patch

ExclusiveArch: x86_64

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kernel-devel
BuildRequires: libdrm-devel
BuildRequires: python3-devel
BuildRequires: rocm-filesystem%{pkg_suffix}

%if %{with test}
%if 0%{?suse_version}
BuildRequires: gtest
%else
BuildRequires: gtest-devel
%endif
%endif

Requires:      python3dist(pyyaml)

# University of Illinois/NCSA Open Source License
Provides: bundled(esmi_ib_library) = %{esmi_ver}

%description
The AMD System Management Interface Library, or AMD SMI library, is a C
library for Linux that provides a user space interface for applications
to monitor and control AMD devices.

%package devel
Summary: Libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libdrm-devel

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p1
tar xf %{SOURCE1}
mv esmi_ib_library-* esmi_ib_library
# So we can pick up this license
mv esmi_ib_library/License.txt esmi_ib_library_License.txt 
# The esmi version check uses git tags, but we use tar's without git files.
# Just inject in the tag that we've pulled into the version check:
sed -i 's/NOT latest_esmi_tag/NOT "esmi_pkg_ver-%{esmi_ver}"/' CMakeLists.txt

# W: spurious-executable-perm /usr/share/doc/amdsmi/README.md
chmod a-x README.md

# /usr/libexec/amdsmi_cli/BDF.py:126: SyntaxWarning: invalid escape sequence '\.'
#   bdf_regex = "(?:[0-6]?[0-9a-fA-F]{1,4}:)?[0-2]?[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}\.[0-7]"
sed -i -e 's@bdf_regex = "@bdf_regex = r"@' amdsmi_cli/BDF.py

# Fix script shebang
sed -i -e 's@env python3@python3@' amdsmi_cli/*.py

# Install local gtests in same dir as tests
sed -i -e 's@${CPACK_PACKAGING_INSTALL_PREFIX}/lib@${SHARE_INSTALL_PREFIX}/tests@' tests/amd_smi_test/CMakeLists.txt

# fix cstdint include
# https://github.com/ROCm/amdsmi/issues/123
sed -i '/#include <unordered_set.*/a#include <cstdint>' rocm_smi/include/rocm_smi/rocm_smi_common.h

# fix iomanip include
# https://github.com/ROCm/amdsmi/issues/124
sed -i '/#include <string.*/a#include <iomanip>' tests/amd_smi_test/test_common.h

# Do not hardcode share dir
sed -i 's@set(SHARE_INSTALL_PREFIX@#set(SHARE_INSTALL_PREFIX@' CMakeLists.txt

%build
%cmake \
    -DBUILD_KERNEL_ASM_DIR=/usr/include/asm \
    -DBUILD_TESTS=%build_test \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
    -DSHARE_INSTALL_PREFIX=%{pkg_prefix}/share \
%if %{with test}
    -DUSE_SYSTEM_GTEST=On \
%endif
    %{nil}

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
if [ -d %{buildroot}%{pkg_prefix}/share/amd_smi/amdsmi ]; then
    mv %{buildroot}%{pkg_prefix}/share/amd_smi/amdsmi %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
    mv %{buildroot}%{pkg_prefix}/share/amd_smi/pyproject.toml %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/
else
    mv %{buildroot}%{pkg_prefix}/share/amdsmi %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
    mv %{buildroot}%{pkg_prefix}/share/pyproject.toml %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/
fi

# Remove some things
rm -rf %{buildroot}/%{pkg_prefix}/share/example
rm -rf %{buildroot}/%{pkg_prefix}/share/amd_smi/example
rm -rf %{buildroot}/%{pkg_prefix}/share/doc/amd_smi-asan/LICENSE.txt
rm -f %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/LICENSE.txt
rm -f %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/README.md
rm -rf %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/copyright
rm -f %{buildroot}%{pkg_prefix}/share/_version.py
rm -f %{buildroot}%{pkg_prefix}/share/amd_smi/_version.py
rm -f %{buildroot}%{pkg_prefix}/share/setup.py
rm -f %{buildroot}%{pkg_prefix}/share/amd_smi/setup.py

# W: unstripped-binary-or-object /usr/lib/python3.13/site-packages/amdsmi/libamd_smi.so
# Does an explict open, so can not just rm it
# let's just strip it
strip %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/*.so
# E: non-executable-script .../amdsmi_cli/amdsmi_cli_exceptions.py 644 /usr/bin/env python3
chmod a+x %{buildroot}/%{pkg_prefix}/libexec/amdsmi_cli/amdsmi_*.py

%if %{with test}
# put the test files in a reasonable place
mkdir %{buildroot}%{pkg_prefix}/share/amdsmi
mv %{buildroot}%{pkg_prefix}/share/tests %{buildroot}%{pkg_prefix}/share/amdsmi/.
%endif

%if 0%{?suse_version}
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc README.md
%license LICENSE
%license esmi_ib_library_License.txt 
%{pkg_prefix}/%{pkg_libdir}/libamd_smi.so.*
%{pkg_prefix}/%{pkg_libdir}/libgoamdsmi_shim64.so.*
%{pkg_prefix}/bin/amd-smi
%{pkg_prefix}/libexec/amdsmi_cli
%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi

%files devel
%{pkg_prefix}/include/amd_smi/
%{pkg_prefix}/include/*.h
%{pkg_prefix}/%{pkg_libdir}/libamd_smi.so
%{pkg_prefix}/%{pkg_libdir}/libgoamdsmi_shim64.so
%{pkg_prefix}/%{pkg_libdir}/cmake/amd_smi/

%if %{with test}
%files test
%{pkg_prefix}/share/amdsmi
%endif

%changelog
* Thu Feb 12 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-2
- Update license

* Mon Jan 26 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-1
- Update to 7.2.0

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Jan 6 2026 Tom Rix <Tom.Rix@amd.com> - 7.1.1-3
- Fix Tumbleweed

* Mon Dec 22 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-2
- Add --with compat

* Wed Nov 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-1
- Update to 7.1.1

* Wed Nov 19 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-3
- Fix SUSE 15.6 build, remove unneeded include

* Mon Nov 10 2025 Tim Flink <tflink@fedoraproject.org> - 7.1.0-2
- update and re-enable gcc15 include patch for upstream 7.1.0 so test subpackage builds
- removed extra dir in test subpackage

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Fri Oct 10 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 7.0.0-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Tue Sep 16 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.0-1
- Update to 7.0.0

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-6
- Add Fedora copyright

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-5
- Simplify file removal

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 6.4.2-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Wed Aug 13 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-3
- Build -test on SUSE

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.2-1
- Update to 6.4.2

* Wed Jun 18 2025 Tim Flink <tflink@fedoraproject.org> - 6.4.1-4
- update so that test subpackage builds cleanly in mock and runs outside of build environment

* Mon Jun 2 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.1-3
- handle movement of copyright file on suse

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 6.4.1-2
- Rebuilt for Python 3.14

* Thu May 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.1-1
- Update to 6.4.1

* Wed Apr 16 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.0-1
- Update to 6.4.0

* Tue Mar 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-3
- Adjust install of python for fedora

* Thu Feb 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-2
- Install amd_smi-config.cmake

* Wed Feb 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-1
- Update to 6.3.3

* Wed Jan 29 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-1
- Update to 6.3.2

* Fri Jan 17 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-6
- Cleanup for suse

* Thu Jan 16 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-5
- Improve empty return patch
- Fix shebangs

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 8 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-3
- Include cstdint for gcc 15

* Tue Dec 31 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- Require pyyaml

* Sun Dec 22 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

* Sat Dec 7 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 3 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed


