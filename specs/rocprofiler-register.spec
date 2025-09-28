%global upstreamname rocprofiler-register
%global rocm_release 7.0
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global glog_version 0.7.1

%bcond_with check
%if %{with check}
%global build_test ON
%else
%global build_test OFF
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Summary:        A rocprofiler helper library
Name:           rocprofiler-register
License:        MIT AND BSD-3-Clause
Version:        %{rocm_version}
Release:        1%{?dist}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Url:            https://github.com/ROCm/%{upstreamname}
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Source1:        https://github.com/google/glog/archive/refs/tags/v%{glog_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  git

# BSD-3-Clause
# rocprofile needs a newer glog
# glog looks like a dead project, notifiy the upstream they should move off of it.
# https://github.com/ROCm/rocprofiler-sdk/issues/87
Provides:       bundled(glog) = %{glog_version}

%description
The rocprofiler-register library is a helper library that coordinates
the modification of the intercept API table(s) of the HSA/HIP/ROCTx
runtime libraries by the ROCprofiler (v2) library. The purpose of this
library is to provide a consistent and automated mechanism of enabling
performance analysis in the ROCm runtimes which does not rely on
environment variables or unique methods for each runtime library.

When a runtime is initialized (either explicitly and lazily) and the
intercept API table is constructed, it passes this API table to
rocprofiler-register. Rocprofiler-register scans the symbols in the
address space and if it detects there is at least one visible symbol
named rocprofiler_configure (which is a function provided by tools),
it passes the intercept API table to the rocprofiler library (dlopening
the rocprofiler library if it is not already loaded). The rocprofiler
library then does an extensive scan for all the instances of the
rocprofiler_configure symbols and invokes each of them. The
rocprofiler_configure function (again, provided by a tool) returns
effectively tells rocprofiler which behaviors it wants to be notified
about, features it wants to use (e.g. API tracing, kernel dispatch
timing), etc.

%package devel
Summary:        The development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# When using the system fmt, need to change this link
sed -i 's@fmt::fmt@fmt@' source/lib/rocprofiler-register/CMakeLists.txt

# Do not hardcode install lib
sed -i 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt

# Do not use git to fetch glog, use cached source
cd external
rm -rf glog
tar xf %{SOURCE1}
mv glog-* glog
# Need to remove the fetch
sed -i -e '/rocprofiler_register_checkout_git_submodule/,+6d' CMakeLists.txt
cd -

# Copy glog's license file
cp -p external/glog/COPYING COPYING.glog

%build
%cmake \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DROCPROFILER_REGISTER_BUILD_TESTS=%{build_test} \
    -DROCPROFILER_REGISTER_BUILD_FMT=OFF

%cmake_build

%install
%cmake_install

# Do not install the test source etc
if [ -d %{buildroot}%{_prefix}/share/rocprofiler-register ]; then
    rm -rf %{buildroot}%{_prefix}/share/rocprofiler-register
fi
if [ -d %{buildroot}%{_prefix}/share/modulefiles ]; then
    rm -rf %{buildroot}%{_prefix}/share/modulefiles
fi
if [ -f %{buildroot}%{_prefix}/share/doc/rocprofiler-register/LICENSE ]; then
    rm -rf %{buildroot}%{_prefix}/share/doc/rocprofiler-register/LICENSE
fi

%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE COPYING.glog
%{_libdir}/librocprofiler-register.so.0{,.*}

%files devel
%doc README.md
%{_includedir}/rocprofiler-register/
%{_libdir}/librocprofiler-register.so
%{_libdir}/cmake/rocprofiler-register/

%changelog
* Fri Sep 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Aug 21 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-1
- Initial package


