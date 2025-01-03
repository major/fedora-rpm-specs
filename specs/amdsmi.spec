%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname amdsmi

# Downloads its own googletest
# Testing also depends on having AMD hardware cpu and/or gpu installed.
# Not suitable for a general %check
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

Name:       amdsmi
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    AMD System Management Interface

License:    NCSA AND MIT AND BSD-3-Clause
URL:        https://github.com/RadeonOpenCompute/%{upstreamname}
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# esmi_ib_library is not suitable for packaging
# https://github.com/amd/esmi_ib_library/issues/13
# This tag was choosen by the amdsmi project because 4.0+ introduced variables not
# found in the upstream kernel.
%global esmi_ver 3.0.3
Source1:    https://github.com/amd/esmi_ib_library/archive/refs/tags/esmi_pkg_ver-%{esmi_ver}.tar.gz
# https://github.com/ROCm/amdsmi/pull/48
Patch0:     0001-Do-not-automatically-download-kernel-header-amd_hsmp.patch
Patch1:     0001-Fix-empty-return.patch

ExclusiveArch: x86_64

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kernel-devel
BuildRequires: libdrm-devel
BuildRequires: python3-devel

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

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p1
tar xf %{SOURCE1}
mv esmi_ib_library-* esmi_ib_library
# So we can pick up this license
mv esmi_ib_library/License.txt esmi_ib_library_License.txt 

# W: spurious-executable-perm /usr/share/doc/amdsmi/README.md
chmod a-x README.md

# /usr/libexec/amdsmi_cli/BDF.py:126: SyntaxWarning: invalid escape sequence '\.'
#   bdf_regex = "(?:[0-6]?[0-9a-fA-F]{1,4}:)?[0-2]?[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}\.[0-7]"
sed -i -e 's@bdf_regex = "@bdf_regex = r"@' amdsmi_cli/BDF.py

# Install local gtests in same dir as tests
sed -i -e 's@${CPACK_PACKAGING_INSTALL_PREFIX}/lib@${SHARE_INSTALL_PREFIX}/tests@' tests/amd_smi_test/CMakeLists.txt

%build
%cmake \
    -DBUILD_KERNEL_ASM_DIR=/usr/include/asm \
    -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
    -DBUILD_TESTS=%build_test

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}/%{python3_sitelib}
mv %{buildroot}/usr/share/amdsmi %{buildroot}/%{python3_sitelib}
mv %{buildroot}/usr/share/pyproject.toml %{buildroot}/%{python3_sitelib}/amdsmi/

# Remove some things
if [ -d %{buildroot}/usr/share/example ]; then
    rm -rf %{buildroot}/usr/share/example
fi
if [ -f %{buildroot}/usr/share/doc/amd_smi-asan/LICENSE.txt ]; then
    rm %{buildroot}/usr/share/doc/amd_smi-asan/LICENSE.txt
fi
if [ -f %{buildroot}/usr/share/doc/amd_smi/LICENSE.txt ]; then
    rm %{buildroot}/usr/share/doc/amd_smi/LICENSE.txt
fi
if [ -f %{buildroot}/usr/share/doc/amd_smi/README.md ]; then
    rm %{buildroot}/usr/share/doc/amd_smi/README.md
fi
if [ -f %{buildroot}%{_datadir}/_version.py ]; then
    rm %{buildroot}%{_datadir}/_version.py
fi
if [ -f %{buildroot}%{_datadir}/setup.py ]; then
    rm %{buildroot}%{_datadir}/setup.py
fi

# W: unstripped-binary-or-object /usr/lib/python3.13/site-packages/amdsmi/libamd_smi.so
# Does an explict open, so can not just rm it
# let's just strip it
strip %{buildroot}/%{python3_sitelib}/amdsmi/*.so
# E: non-executable-script .../amdsmi_cli/amdsmi_cli_exceptions.py 644 /usr/bin/env python3
chmod a+x %{buildroot}/%{_libexecdir}/amdsmi_cli/*.py

# RPM has a problem with this file
rm %{buildroot}%{_libdir}/cmake/amd_smi/amd_smi-config.cmake

%files
%doc README.md
%license LICENSE
%license esmi_ib_library_License.txt 
%{_libdir}/libamd_smi.so.*
%{_libdir}/libgoamdsmi_shim64.so.*
%{_bindir}/amd-smi
%{_libexecdir}/amdsmi_cli
%{python3_sitelib}/amdsmi

%files devel
%dir %{_includedir}/amd_smi
%dir %{_libdir}/cmake/amd_smi
%{_includedir}/amd_smi/*.h
%{_includedir}/*.h
%{_libdir}/libamd_smi.so
%{_libdir}/libgoamdsmi_shim64.so
%{_libdir}/cmake/amd_smi/*.cmake

%if %{with test}
%files test
%{_datadir}/tests
%endif

%changelog
* Tue Dec 31 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- Require pyyaml

* Sun Dec 22 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

* Sat Dec 7 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 3 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed


