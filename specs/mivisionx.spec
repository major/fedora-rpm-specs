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
%global upstreamname MIVisionX
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
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' )

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

# For testing
# Use the VX conformace tests, openvx_1.3 branch
# https://github.com/KhronosGroup/OpenVX-cts
# Results on gfx1103
#
# [ ALL DONE ] 5820 test(s) from 69 test case(s) ran
# [ PASSED   ] 5817 test(s)
# [ FAILED   ] 3 test(s), listed below:
# [ FAILED   ] SmokeTestBase.vxReleaseReferenceBase
# [ FAILED   ] SmokeTestBase.vxLoadKernels
# [ FAILED   ] SmokeTestBase.vxUnloadKernels
# [ DISABLED ] 8190 test(s)

Name:           mivisionx%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        AMD's computer vision toolkit
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT AND Apache-2.0 AND MIT-Khronos-old AND GPL-3.0-or-later
# MIT is the main license
# Apache-2.0 is used for the includes
#  amd_openvx/openvx/include/VX/vx*.h
# MIT-Khronos-old covers a couple of files
#  amd_openvx/openvx/api/vx_nodes.cpp
#  amd_openvx/openvx/api/vxu.cpp
# GPL 3 or later for a couple of files
#  apps/cloud_inference/client_app/qcustomplot.*

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  half-devel
BuildRequires:  hipcc%{pkg_suffix}
# Problem with ffmpeg
# /MIVisionX-rocm-6.3.1/amd_openvx_extensions/amd_media/kernels.cpp:98:5: error: use of undeclared identifier 'av_register_all'
#   98 |     av_register_all();
#      |     ^
# BuildRequires:  ffmpeg-free-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
%if 0%{?fedora}
BuildRequires:  mesa-va-drivers
%endif
BuildRequires:  miopen%{pkg_suffix}-devel
BuildRequires:  opencv-devel
BuildRequires:  rocblas%{pkg_suffix}-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-omp%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-rpp%{pkg_suffix}-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
MIVisionX toolkit is a set of comprehensive computer vision
and machine intelligence libraries, utilities, and applications
bundled into a single toolkit. AMD MIVisionX delivers highly
optimized conformant open-source implementation of the Khronos
OpenVX™ and OpenVX™ Extensions along with Convolution Neural
Net Model Compiler & Optimizer supporting ONNX, and Khronos
NNEF™ exchange formats. The toolkit allows for rapid prototyping
and deployment of optimized computer vision and machine learning
inference workloads on a wide range of computer hardware,
including small embedded x86 CPUs, APUs, discrete GPUs, and
heterogeneous servers.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Remove some cruft
find . -type f -name '.gitignore' -delete
find . -type f -name '.DS_Store' -delete

# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.h' -o -name '*.cpp' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done

# Fixup default ROCM_PATH
sed -i -e 's@/opt/rocm@%{pkg_prefix}@' CMakeLists.txt

# Make finding rpp required
sed -i -e 's@find_package(rpp 2.1.0 QUIET)@find_package(rpp 2.1.0 REQUIRED)@' amd_openvx_extensions/CMakeLists.txt

%build

# Finding rpp is always a problem, print out debug find info
%cmake \
    --debug-find-pkg=rpp \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DGPU_TARGETS=%{gpu_list} \
    -DMIGRAPHX=OFF \
    -DNEURAL_NET=OFF \
    -DHIP_PLATFORM=amd

%cmake_build

%install
%cmake_install

#Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{pkg_prefix}
%endif

# ERROR   0020: file '/usr/lib64/libvx_amd_custom.so.1.0.1' contains a runpath referencing '..' of an absolute path [:/usr/lib64/rocm/llvm/bin/../lib]
chrpath -r %{rocmllvm_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libvx_amd_custom.so.1.*.*

rm -f %{buildroot}%{pkg_prefix}/share/doc/mivisionx/LICENSE.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/mivisionx-asan/LICENSE.txt
rm -rf %{buildroot}%{pkg_prefix}/share/mivisionx/apps
rm -rf %{buildroot}%{pkg_prefix}/share/mivisionx/samples
rm -rf %{buildroot}%{pkg_prefix}/share/mivisionx/test


%files
%license LICENSE.txt
%{pkg_prefix}/bin/runvx
%{pkg_prefix}/%{pkg_libdir}/libopenvx.so.1{,.*}
%{pkg_prefix}/%{pkg_libdir}/libvx_amd_custom.so.1{,.*}
%{pkg_prefix}/%{pkg_libdir}/libvx_opencv.so.1{,.*}
%{pkg_prefix}/%{pkg_libdir}/libvx_rpp.so.3{,.*}
%{pkg_prefix}/%{pkg_libdir}/libvxu.so.1{,.*}

%files devel
%doc README.md
%{pkg_prefix}/share/mivisionx/
%{pkg_prefix}/include/mivisionx/
%{pkg_prefix}/%{pkg_libdir}/libopenvx.so
%{pkg_prefix}/%{pkg_libdir}/libvx_amd_custom.so
%{pkg_prefix}/%{pkg_libdir}/libvx_opencv.so
%{pkg_prefix}/%{pkg_libdir}/libvx_rpp.so
%{pkg_prefix}/%{pkg_libdir}/libvxu.so

%changelog
* Fri Feb 6 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-1
- Update to 7.2.0

* Thu Jan 29 2026 Nicolas Chauvet <kwizart@gmail.com> - 7.1.0-8
- Rebuilt for OpenCV 4.13

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Dec 25 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-6
- Add --with compat

* Wed Dec 10 2025 Nicolas Chauvet <kwizart@gmail.com> - 7.1.0-5
- Rebuilt for OpenCV-4.12

* Mon Nov 10 2025 Adam Williamson <awilliam@redhat.com> - 7.1.0-4
- Rebuild for ffmpeg 8 again

* Thu Nov 6 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-3
- Fix rpp

* Wed Nov 05 2025 Dominik Mierzejewski <dominik@greysector.net> - 7.1.0-2
- Rebuilt for FFmpeg 8

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Sun Sep 21 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Aug 28 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-6
- Add Fedora copyright

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-5
- Simplify file removal

* Mon Aug 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- mesa-va-drivers are not on RHEL

* Wed Jul 30 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Remove -mtls-dialect cflag

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Apr 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Sat Feb 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-1
- Initial package

