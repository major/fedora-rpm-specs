%global upstreamname rpp
%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# The default list in the project does not cover our expected targets
%global all_rocm_gpus "gfx900;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack+;gfx90a:xnack-;gfx942;gfx1010;gfx1012;gfx1030;gfx1100;gfx1101;gfx1102;gfx1103;gfx1200;gfx1201"

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Testing does not work well, it requires local hw.

Name:           rocm-rpp
Version:        %{rocm_version}
Release:        2%{?dist}
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
BuildRequires:  opencv-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-omp-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

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

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# hip compiler
sed -i -e 's@set(COMPILER_FOR_HIP ${ROCM_PATH}/llvm/bin/clang++)@set(COMPILER_FOR_HIP hipcc)@' CMakeLists.txt
# remove clang++
sed -i -e '/set(CMAKE_CXX_COMPILER clang++)/d' CMakeLists.txt

# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.cpp' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done

# Remove search for HALF, ours is installed in the usual place
sed -i -e '/HALF/d' CMakeLists.txt

# Some things that are not used
sed -i -e '/COMPONENT test/d' CMakeLists.txt

%build

%cmake -G Ninja \
       -DAMDGPU_TARGETS=%{all_rocm_gpus} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DHIP_PLATFORM=amd \
       -DBACKEND=HIP \
       -DROCM_SYMLINK_LIBS=OFF \
       -DCMAKE_BUILD_TYPE=%{build_type} \
       -DROCM_PATH=%{_prefix} \
       -DHIP_PATH=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

# ERROR   0020: file '/usr/lib64/librpp.so.1.9.1' contains a runpath referencing '..' of an absolute path [/usr/lib64/rocm/llvm/bin/../lib]
chrpath -r %{rocmllvm_libdir} %{buildroot}%{_libdir}/librpp.so.1.*.*

%files
%license LICENSE
%exclude %{_docdir}/rpp/LICENSE
%exclude %{_docdir}/rpp-asan/LICENSE
%{_libdir}/librpp.so.1{,.*}

%files devel
%doc README.md
%{_includedir}/rpp
%{_libdir}/librpp.so


%changelog
* Sun Jan 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- build requires gcc-c++
- Add gfx12

* Sun Dec 29 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

