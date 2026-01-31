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
%global upstreamname rdc
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

Name:           rocm-rdc
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Data Center Tool

URL:            https://github.com/ROCm/%{upstreamname}
License:        MIT AND NCSA
# The main license is MIT
# These are the files that are NCSA
# cmake_modules/utils.cmake
# include/rdc_modules/kernels/binary_search_kernels.cl
# rdc_libs/rdc_modules/kernels/binary_search_kernels.cl
# rdc_libs/rdc_modules/kernels/gpuReadWrite_kernels.cl
# tests/rdc_tests/test_utils.cc
# tests/rdc_tests/test_utils.h
# tools/run_github_actions_locally.sh

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

# ROCm is only x86_64 for now
ExclusiveArch:  x86_64

BuildRequires:  amdsmi-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  grpc-devel
BuildRequires:  libcap-devel
BuildRequires:  libdrm-devel
BuildRequires:  python3dist(cppheaderparser)
BuildRequires:  protobuf-devel
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

%description
ROCm Data Center Tool (RDC)
The ROCm Data Center Tool simplifies the administration and addresses
key infrastructure challenges in AMD GPUs in cluster and data center
environments. The main features are:

* GPU telemetry
* GPU statistics for jobs
* Integration with third-party tools
* Open source

%package devel
Summary:        The %{name} development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The headers of libraries for %{name}.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Use the system gRPC
sed -i -e 's@${GRPC_DESIRED_VERSION}@@' CMakeLists.txt
# Use the system Protobuf
sed -i -e 's@protobuf HINTS ${GRPC_ROOT} CONFIG@Protobuf@' CMakeLists.txt
# Location of call_op_set is a little different on Fedora
sed -i -e 's@grpcpp/impl/call_op_set.h@grpcpp/impl/codegen/call_op_set.h@' server/src/rdc_api_service.cc

%build
%cmake \
    -DGPU_TARGETS=%{gpu_list} \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DBUILD_RASLIB=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_STANDALONE=ON \
    -DBUILD_RVS=OFF \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DHIP_PLATFORM=amd \
    -DROCM_SYMLINK_LIBS=OFF \
    -DROCM_DIR=%{_prefix}

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rdc/LICENSE.md

# rocm-rdc.x86_64: W: unstripped-binary-or-object /usr/lib64/rdc/hsaco/gfx1010/binary_search_kernels.hsaco
%rocmllvm_bindir/llvm-strip %{buildroot}%{_libdir}/rdc/hsaco/*/*.hsaco

# rocm-rdc.x86_64: E: non-executable-script /usr/libexec/rdc/authentication/01gen_root_cert.sh 644 /bin/bash
chmod a+x %{buildroot}%{_libexecdir}/rdc/authentication/*.sh

%files
%license LICENSE.md
%doc README.md
%dir %{_datadir}/rdc
%dir %{_libdir}/rdc
%{_bindir}/rdc*
%{_datadir}/rdc/conf/
%{_libdir}/librdc.so.1{,.*}
%{_libdir}/librdc_bootstrap.so.1{,.*}
%{_libdir}/librdc_client.so.1{,.*}
%{_libdir}/rdc/librdc_rocr.so.1{,.*}
%{_libdir}/rdc/hsaco/
%{_libexecdir}/rdc/

%files devel
%dir %{_includedir}/rdc
%dir %{_libdir}/cmake/rdc
%{_datadir}/rdc/example/
%{_includedir}/rdc/*.h
%{_libdir}/librdc.so
%{_libdir}/librdc_bootstrap.so
%{_libdir}/librdc_client.so
%{_libdir}/rdc/librdc_rocr.so
%{_libdir}/cmake/rdc/*.cmake


%changelog
* Fri Jan 16 2026 Tom Rix <Tom.Rix@amd.com> - 7.1.1-1
- Initial package

