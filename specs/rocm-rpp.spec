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
%global upstreamname rpp
%global rocm_release 7.2
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

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# The default list in the project does not cover our expected targets
%global gpu_list "gfx900;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack+;gfx90a:xnack-;gfx942;gfx950;gfx1010;gfx1012;gfx1030;gfx1100;gfx1101;gfx1102;gfx1103;gfx1150;gfx1151;gfx1152;gfx1153;gfx1200;gfx1201"
%global _gpu_list gfx1100

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Testing does not work well, it requires local hw.
%bcond_with test

Name:           rocm-rpp%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Performace Primatives for computer vision
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain
# The main license is MIT
# A couple of files have Apache-2.0
#   src/include/common/rpp/kernel_cache.hpp
#   src/modules/kernel_cache.cpp
# A Public Domain
#   src/modules/md5.cpp

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  half-devel
BuildRequires:  ninja-build
%if 0%{?fedora}
BuildRequires:  opencv-devel
%endif
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-omp%{pkg_suffix}-devel
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
AMD ROCm Performance Primitives (RPP) library is a comprehensive,
high-performance computer vision library for AMD processors that
have HIP, OpenCL, or CPU backends.

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
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# hip compiler
sed -i -e 's@set(COMPILER_FOR_HIP ${ROCM_PATH}/llvm/bin/clang++)@set(COMPILER_FOR_HIP hipcc)@' CMakeLists.txt
# remove clang++
sed -i -e '/set(CMAKE_CXX_COMPILER clang++)/d' CMakeLists.txt

# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.cpp' -o -name '*.h' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done

# Remove search for HALF, ours is installed in the usual place
sed -i -e '/HALF/d' CMakeLists.txt

%if %{without test}
# Some things that are not used
sed -i -e '/COMPONENT test/d' CMakeLists.txt
%endif

# Remove third_party libs
# https://github.com/ROCm/rpp/issues/602
rm -rf libs/third_party

# Problems building mivsionx
# CMake Error at /usr/lib64/cmake/rpp/rpp-config.cmake:28 (message):
#  File or directory //include referenced by variable rpp_INCLUDE_DIR does not
#
# Adjust the cmake install locations
sed -i -e 's|@PACKAGE_INCLUDE_INSTALL_DIR@|%{pkg_prefix}/include|' cmake_modules/rpp-config.cmake.in
sed -i -e 's|@PACKAGE_LIB_INSTALL_DIR@|%{pkg_prefix}/%{pkg_libdir}|' cmake_modules/rpp-config.cmake.in

%build

%cmake \
    -G Ninja \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DGPU_TARGETS=%{gpu_list} \
    -DBACKEND=HIP \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DHIP_PLATFORM=amd \
    -DROCM_SYMLINK_LIBS=OFF \
    -DRPP_AUDIO_SUPPORT=OFF \
    -DROCM_PATH=%{pkg_prefix} \
    -DHIP_PATH=%{pkg_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_prefix}/%{pkg_libdir}

%cmake_build

%install
%cmake_install

# ERROR   0020: file '/usr/lib64/librpp.so.1.9.1' contains a runpath referencing '..' of an absolute path [/usr/lib64/rocm/llvm/bin/../lib]
chrpath -r %{rocmllvm_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/librpp.so.2.*.*

# Extra licenses
rm -f %{buildroot}%{pkg_prefix}/share/doc/rpp-asan/FFTS_LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rpp-asan/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rpp/FFTS_LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rpp/LICENSE

%files
%license LICENSE
%{pkg_prefix}/%{pkg_libdir}/librpp.so.2{,.*}

%files devel
%doc README.md
%{pkg_prefix}/include/rpp/
%{pkg_prefix}/%{pkg_libdir}/librpp.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rpp/

%if %{with test}
%files test
%{pkg_prefix}/share/rpp/
%endif

%changelog
* Fri Jan 30 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-1
- Update to 7.2.0

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Dec 24 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-4
- Add --with compat

* Sat Nov 22 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-3
- Remove dir tags

* Thu Nov 6 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Fix cmake patch

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Sun Sep 21 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Aug 28 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-6
- Add Fedora copyright

* Thu Aug 21 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-5
- Remove prebuild libffts.a library

* Wed Jul 30 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Remove -mtls-dialect cflag
- Add gfx950,gfx1150,gfx1151,gfx1152,gfx1153

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 13 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- Add --with test

* Sun Apr 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Tue Feb 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-3
- Remove opencv for RHEL

* Sun Jan 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- build requires gcc-c++
- Add gfx12

* Sun Dec 29 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

