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
%global upstreamname roctracer
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

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

%global toolchain clang
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Needs ROCm HW and is only suitable for local testing
# GPU_TARGETS in the cmake config are only for testing
%bcond_with test
%if %{with test}
# rpm flags interfere with building the tests
%global build_cflags %{nil}
%endif

%bcond_with doc

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio

Name:           roctracer%{pkg_suffix}
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        ROCm Tracer Callback/Activity Library for Performance tracing AMD GPUs

Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}

%if 0%{?suse_version}
BuildRequires:  libatomic1
BuildRequires:  %{python_module CppHeaderParser}
%else
BuildRequires:  libatomic
# https://github.com/ROCm/roctracer/issues/113
BuildRequires:  python3-cppheaderparser
%endif

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  texlive-adjustbox
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-hanging
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-metafont
BuildRequires:  texlive-multirow
BuildRequires:  texlive-newunicodechar
BuildRequires:  texlive-stackengine
BuildRequires:  texlive-texlive-scripts
BuildRequires:  texlive-tocloft
BuildRequires:  texlive-ulem
BuildRequires:  texlive-url
BuildRequires:  texlive-wasy
BuildRequires:  texlive-wasysym
%endif

# ROCm is only x86_64 for now
ExclusiveArch:  x86_64

%description
ROC-tracer

* ROC-tracer library: Runtimes Generic Callback/Activity APIs

  The goal of the implementation is to provide a generic independent
  from specific runtime profiler to trace API and asynchronous activity.

  The API provides functionality for registering the runtimes API
  callbacks and asynchronous activity records pool support.

* ROC-TX library: Code Annotation Events API

  Includes API for:

  * roctxMark
  * roctxRangePush
  * roctxRangePop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%package devel
Summary:        The %{name} development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The headers of libraries for %{name}.

%if %{with doc}
%package doc
Summary:        Docs for %{name}

%description doc
%{summary}
%endif

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# No knob in cmake to turn off testing
%if %{without test}
sed -i -e 's@add_subdirectory(test)@#add_subdirectory(test)@' CMakeLists.txt

%else

# Adjust test running script lib dir
sed -i -e 's@../lib/@../%{pkg_libdir}/@' test/run.sh

%endif

%build
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_MODULE_PATH=%{pkg_prefix}/%{pkg_libdir}/cmake/hip \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DGPU_TARGETS=%{rocm_gpu_list_test} \
    -DHIP_PLATFORM=amd \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=RelDebInfo

%cmake_build

%if %{with doc}
%cmake_build -t doc
%endif

%install
%cmake_install

# Only install the pdf
rm -rf rm %{buildroot}%{pkg_prefix}/share/html
# Extra licenses
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/LICENSE.md

%files
%license LICENSE.md
%doc README.md
%{pkg_prefix}/%{pkg_libdir}/libroctracer64.so.*
%{pkg_prefix}/%{pkg_libdir}/libroctx64.so.*
%{pkg_prefix}/%{pkg_libdir}/roctracer/

%files devel
%{pkg_prefix}/include/roctracer
%{pkg_prefix}/%{pkg_libdir}/libroctracer64.so
%{pkg_prefix}/%{pkg_libdir}/libroctx64.so

%if %{with doc}
%files doc
%{pkg_prefix}/share/doc/roctracer/
%endif

%if %{with test}
%files test
%{pkg_prefix}/share/roctracer/
%endif

%changelog
* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Sat Sep 20 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-6
- Add Fedora copyright

* Thu Aug 7 2025 Egbert Eich <eich@suse.com> - 6.4.0-5
- Fix python dependencies for SUSE.

* Thu Aug 7 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Fix building test subpackage - 6.4.0-3

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- Remove suse check of ldconfig

* Fri Apr 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Mon Feb 24 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-7
- Specialize python-cppheaderparser for tw

* Thu Feb 13 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-6
- Fix SLE 15.6

* Wed Feb 5 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-5
- Fix TW build

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- multithread compress

* Sat Jan 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- fix gpu list

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3
