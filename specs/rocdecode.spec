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
%if 0%{?suse_version}
%global rocdecode_name librocdecode0
%else
%global rocdecode_name rocdecode
%endif

%global upstreamname rocDecode

%global rocm_release 7.0
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

# Requires actual HW, so disabled by default.
# Tests also have issues and possibly requires ffmpeg from rpmfusion to work 
%bcond_with check

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# Use ninja if it is available
%if 0%{?fedora} || 0%{?suse_version}
%bcond_without ninja
%else
%bcond_with ninja
%endif

%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif

Name:           %{rocdecode_name}
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        High-performance video decode SDK for AMD GPUs

Url:            https://github.com/ROCm/rocDecode
# Note: MIT with a clause clarifying that AMD will not pay for codec royalties
# The clause has little weight on the licensing, it is just a clarification
License:        MIT
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

%if %{with check}
%if 0%{?suse_version}
BuildRequires:  ffmpeg
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
BuildRequires:  Mesa-libva
%else 
BuildRequires:  ffmpeg-free
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  mesa-va-drivers
%endif
%endif

%if %{with ninja}
%if 0%{?fedora}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  ninja
%define __builder ninja
%endif
%endif

# Rocdecode isn't useful without AMD's mesa va drivers:
Requires:     mesa-va-drivers
Provides:     rocdecode = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocDecode is a high-performance video decode SDK for AMD GPUs. Using the
rocDecode API, you can access the video decoding features available on your GPU.

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%package devel
Summary: The rocDecode development package
Requires:     %{name}%{?_isa} = %{version}-%{release}
Provides:     rocdecode-devel = %{version}-%{release}

%description devel
The rocDecode development package.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
# Allow overriding CMAKE_CXX_COMPILER: 
# https://github.com/ROCm/rocDecode/pull/436
sed -i "s|\(llvm/bin/clang++\)|\1 CACHE STRING \"ROCm Compiler path\"|" \
	CMakeLists.txt \
	samples/*/CMakeLists.txt

# Problems finding va.h
# https://github.com/ROCm/rocDecode/issues/477
sed -i "s|/opt/amdgpu/include NO_DEFAULT_PATH|/usr/include|" cmake/FindLibva.cmake

# cpack cruft in the middle of the configure, this breaks TW and is only used for ubuntu
sed -i -e 's@file(READ "/etc/os-release" OS_RELEASE)@#file(READ "/etc/os-release" OS_RELEASE)@'  CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@#string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@'  CMakeLists.txt

# Need to add libdrm_amdgpu to link
# https://github.com/ROCm/rocDecode/issues/571
sed -i -e 's@${LINK_LIBRARY_LIST} ${LIBVA_DRM_LIBRARY}@${LINK_LIBRARY_LIST} ${LIBVA_DRM_LIBRARY} -ldrm_amdgpu@' CMakeLists.txt

%build
%cmake %{cmake_generator} \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocdecode/LICENSE
rm -f %{buildroot}%{_prefix}/share/doc/rocdecode-asan/LICENSE
rm -f %{buildroot}%{_prefix}/share/doc/packages/%{name}/LICENSE
rm -f %{buildroot}%{_prefix}/share/doc/packages/%{name}-asan/LICENSE

# Need to install the sample first
%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE
%{_libdir}/librocdecode.so.1{,.*}

%files devel
%dir %{_libdir}/cmake/rocdecode
%{_libdir}/librocdecode.so
%{_libdir}/cmake/rocdecode/*.cmake
%{_includedir}/rocdecode
%{_datadir}/rocdecode
%exclude %{_datadir}/rocdecode/samples

%changelog
* Fri Sep 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-2
- Rebuild

* Sun Sep 21 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-8
- Add Fedora copyright

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-7
- Simplify file removal

* Sat Aug 16 2025 Egbert Eich <eich@suse.com> - 6.4.0-6
- Fix dependencies on SUSE when 'check' is enabled.
 
* Thu Aug 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-5
- change --with test to --with check

* Tue Jul 29 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Remove -mtls-dialect cflag

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Remove suse check for ldconfig

* Wed Apr 23 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- Fix link on suse

* Sat Apr 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Thu Apr 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-6
- Reenable ninja

* Tue Feb 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-5
- Fix SLE 15.6

* Tue Feb 4 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- Fix TW build

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- multithread compress

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Tue Dec 17 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

