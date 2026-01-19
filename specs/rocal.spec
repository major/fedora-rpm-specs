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
%global upstreamname rocAL

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

# mixing gcc and clang, some flags need to be removed
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong//' -e 's/-fcf-protection//' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Need local gpu hw to test
# No good way to run tests from a subpackage, so need to run them as part of check
%bcond_with check
# Still need a test subpackage because tests depend on install of test data
%bcond_with test

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"        xz level 7 using %%{getncpus} threads
#
# This changes from the default compressor
#   $ gzip
# To
#   $ xz -7 -T cpus
#
# Multithreading the compress stage reduces the overall build time.
%global _source_payload         w7T0.xzdio
%global _binary_payload         w7T0.xzdio

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

Name:           rocal%{pkg_suffix}
Version:        %{rocm_version}
Release:        4%{?dist}
Summary:        ROCm Augmentation Library

Url:            https://github.com/ROCm/rocAL
License:        MIT AND BSD-3-Clause
# rocAL is MIT
# bundled rapidjson is MIT AND BSD-3-Clause
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

Patch1:         0001-rocal-find-mivisionx.patch

#
# rapidjson bundling
# rocAL uses unreleased ToT rapidjson API, see rocAL-setup.py
%global rapidjson_date 20241218
%global rapidjson_commit 24b5e7a8b27f42fa16b96fc70aade9106cf7102f
%global short_rapidjson_commit %(c=%{rapidjson_commit}; echo ${c:0:7})
Source1:        https://github.com/Tencent/rapidjson/archive/%{rapidjson_commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  chrpath
# Problems with optional ffmpeg
# rocAL-rocm-6.3.3/rocAL/source/decoders/video/hardware_video_decoder.cpp:178:11: error: no matching function for call to 'av_find_best_stream'
#  178 |     ret = av_find_best_stream(_fmt_ctx, AVMEDIA_TYPE_VIDEO, -1, -1, &_decoder, 0);
#      |           ^~~~~~~~~~~~~~~~~~~
# So disable use
# BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc-c++
BuildRequires:  half-devel
BuildRequires:  lmdb-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libsndfile-devel
BuildRequires:  mivisionx%{pkg_suffix}-devel
BuildRequires:  protobuf-devel
BuildRequires:  pybind11-devel
BuildRequires:  rocdecode%{pkg_suffix}-devel
BuildRequires:  rocjpeg%{pkg_suffix}-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-omp%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-rpp%{pkg_suffix}-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  turbojpeg-devel

# License info copied from the rapidjson spec
# License: MIT AND BSD-3-Clause
Provides:       bundled(rapidjson) = %{rapidjson_date}.g%{short_rapidjson_commit}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
The AMD ROCm Augmentation Library (rocAL) is designed to efficiently
decode and process images and videos from a variety of storage formats
and modify them through a processing graph programmable by the user.
rocAL currently provides C API.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rocal%{pkg_suffix}-devel = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# rapidjson ToT
tar xf %{SOURCE1}

# cmake 3.5 minimum
sed -i -e 's@cmake_minimum_required(VERSION 2.8)@cmake_minimum_required(VERSION 3.5)@' rapidjson-%{rapidjson_commit}/example/CMakeLists.txt

# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.h' -o -name '*.cpp' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done
sed -i -e 's@half/half.hpp@half.hpp@' cmake/FindHALF.cmake

# We set this below
sed -i -e 's@set(COMPILER_FOR_HIP@#set(COMPILER_FOR_HIP@' rocAL/rocAL_hip/CMakeLists.txt

# https://github.com/ROCm/rocAL/issues/287
# Several rpmlint warning about missing libjpeg syms
# rocal.x86_64: E: undefined-non-weak-symbol /usr/lib64/librocal.so.2.1.0 jpeg_mem_src (/usr/lib64/librocal.so.2.1.0)
sed -i -e 's@set(LINK_LIBRARY_LIST ${LINK_LIBRARY_LIST} ${TurboJpeg_LIBRARIES})@set(LINK_LIBRARY_LIST ${LINK_LIBRARY_LIST} ${LIBJPEG_LIBRARIES} ${TurboJpeg_LIBRARIES})@' rocAL/CMakeLists.txt

# Tests use the wrong ROCM_PATH
sed -i -e 's@set(ROCM_PATH /opt/rocm@set(ROCM_PATH %{pkg_prefix}@' tests/cpp_api/CMakeLists.txt
sed -i -e 's@set(ROCM_PATH /opt/rocm@set(ROCM_PATH %{pkg_prefix}@' tests/cpp_api/*/CMakeLists.txt

# tests have wrong include
for f in `find tests -type f -name '*.cpp' `; do
    sed -i -e 's@rocal_api.h@rocal/rocal_api.h@' $f
    sed -i -e 's@rocal_api_types.h@rocal/rocal_api_types.h@' $f
done

# Remove to make license simpler
# Apache License 2.0
# ------------------
# rocal-6.3.3-build/rocAL-rocm-6.3.3/docs/examples/tf/pets_training/create_pet_tf_record.py
rm -rf docs/examples/tf/pets_training

%build

cd rapidjson-%{rapidjson_commit}
p=$PWD
mkdir build
cd build
%__cmake \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_BUILD_TYPE=RELEASE \
       -DRAPIDJSON_BUILD_CXX11:BOOL=OFF \
       -DCMAKE_INSTALL_PREFIX=$p/install \
       ..
%make_build
%make_build install
cd ../..

%cmake \
    --debug-find-pkg=MIVisionX \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/amdclang \
    -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_PREFIX_PATH=$p/install/lib/cmake \
    -DCOMPILER_FOR_HIP=%rocmllvm_bindir/clang++ \
    -DGPU_TARGETS=%{gpu_list} \
    -DHIP_PLATFORM=amd \
    -DROCM_PATH=%{pkg_prefix}

%cmake_build

%if %{with check}
# Need to install rocal-test
# This issue in MiVisionX is causing test failures
# https://github.com/ROCm/MIVisionX/issues/1489
%check
%ctest
%endif

%install
%cmake_install

# Extra licenses
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocal/LICENSE.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocal-asan/LICENSE.txt
# Extra README
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocal/README.md

# No cmake knob to turn off testing, remove the install dir
%if %{without test}
rm -rf %{buildroot}%{pkg_prefix}/share/rocal/test
%endif

# ERROR   0020: file '/usr/lib64/librocal.so.2.3.0' contains a rpath referencing '..' of an absolute path [:/usr/lib64/rocm/llvm/bin/../lib]
chrpath -r %{rocmllvm_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/librocal.so.2.*.*

%files
%doc README.md
%license LICENSE.txt
%{pkg_prefix}/%{pkg_libdir}/librocal.so.2{,.*}

%files devel
%{pkg_prefix}/%{pkg_libdir}/librocal.so
%{pkg_prefix}/include/rocal/

%if %{with test}
%files test
%{pkg_prefix}/share/rocal/test
%endif

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Dec 25 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-3
- Add --with compat

* Mon Nov 10 2025 Adam Williamson <awilliam@redhat.com> - 7.1.0-2
- Rebuild for new ffmpeg / mivisionx

* Tue Nov 4 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0
- Remove buildrequires version contraints

* Sat Oct 11 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Sat Sep 27 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-2
- set cxx compiler to amdclang++

* Sun Sep 21 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Aug 28 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Add Fedora copyright

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Apr 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.0-1
- Update to 6.4.0

* Thu Feb 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-1
- Initial package
