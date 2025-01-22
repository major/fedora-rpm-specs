%global upstreamname rocJPEG

%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Requires actual HW, so disabled by default.
# Testing is not well behaved.
%bcond_with test

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio

Name:           rocjpeg
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        A high-performance jpeg decode library for AMD’s GPUs

Url:            https://github.com/ROCm/rocJPEG
License:        MIT
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libva-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
%if %{with test}
BuildRequires:  ffmpeg-free
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  mesa-va-drivers
%endif

# Rocjpeg isn't useful without AMD's mesa va drivers:
Requires:     mesa-va-drivers

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocJPEG is a high performance JPEG decode SDK for AMD GPUs. Using
the rocJPEG API, you can access the JPEG decoding features available
on your GPU.

%package devel
Summary:        The development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The rocJPEG development package.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Fix this error:
# gmake[2]: /opt/rocm/lib/llvm/bin/clang++: No such file or directory
sed -i "s|\(llvm/bin/clang++\)|\1 CACHE STRING \"ROCm Compiler path\"|" CMakeLists.txt

# There is no /opt/amgpu/include, just use the normal path.
sed -i "s|/opt/amdgpu/include NO_DEFAULT_PATH|/usr/include|" cmake/FindLibva.cmake

# Fix up sample
sed -i -e 's@${ROCM_PATH}/lib/llvm/bin/clang++@/usr/bin/hipcc@' samples/*/CMakeLists.txt
sed -i -e 's@{ROCM_PATH}/lib@/usr/lib64@' samples/*/CMakeLists.txt test/CMakeLists.txt
sed -i -e 's@{ROCM_PATH}/include/rocjpeg@/usr/include/rocjpeg@' samples/*/CMakeLists.txt test/CMakeLists.txt
sed -i -e 's@set(ROCM_PATH /opt/rocm@set(__ROCM_PATH /opt/rocm@' samples/*/CMakeLists.txt test/CMakeLists.txt
# Fix up test
sed -i -e 's@{ROCM_PATH}/share@/usr/share@' test/CMakeLists.txt

%build

%cmake \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

# Need to install first
%if %{with test}
%check
%ctest
%endif

%files
%license /usr/share/doc/%{name}/LICENSE
%exclude /usr/share/doc/%{name}-*/LICENSE
%dir %{_docdir}/%{name}
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_datadir}/%{name}

%changelog
* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-3
- multithread compress

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- build requires gcc-c++

* Wed Dec 25 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Initial package
