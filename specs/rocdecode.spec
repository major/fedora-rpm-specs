%global upstreamname rocDecode

%global rocm_release 6.3
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Requires actual HW, so disabled by default.
# Tests also have issues and possibly requires ffmpeg from rpmfusion to work 
%bcond_with test

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio

Name:           rocdecode
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        High-performance video decode SDK for AMD GPUs

Url:            https://github.com/ROCm/rocDecode
# Note: MIT with a clause clarifying that AMD will not pay for codec royalties
# The clause has little weight on the licensing, it is just a clarification
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
BuildRequires:  libavutil-free-devel
BuildRequires:  mesa-va-drivers
%endif

# Rocdecode isn't useful without AMD's mesa va drivers:
Requires:     mesa-va-drivers

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocDecode is a high-performance video decode SDK for AMD GPUs. Using the
rocDecode API, you can access the video decoding features available on your GPU.

%package devel
Summary:        The rocDecode development package
Requires: %{name}%{?_isa} = %{version}-%{release}

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

%build
%cmake \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

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
%exclude %{_datadir}/%{name}/samples

%changelog
* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-3
- multithread compress

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Tue Dec 17 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

