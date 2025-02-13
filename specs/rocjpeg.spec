%if 0%{?suse_version}
%global rocjpeg_name librocjpeg0
%else
%global rocjpeg_name rocjpeg
%endif

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

Name:           %{rocjpeg_name}
Version:        %{rocm_version}
Release:        5%{?dist}
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
Provides:     rocjpeg = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocJPEG is a high performance JPEG decode SDK for AMD GPUs. Using
the rocJPEG API, you can access the JPEG decoding features available
on your GPU.

%if 0%{?suse_version}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%package devel
Summary:        The development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:     rocjpeg-devel = %{version}-%{release}

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

# cpack cruft in the middle of the configure, this breaks TW 
sed -i -e 's@file(READ "/etc/os-release" OS_RELEASE)@#file(READ "/etc/os-release" OS_RELEASE)@'  CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@#string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@'  CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "SLES" SLES_FOUND ${OS_RELEASE})@#string(REGEX MATCH "SLES" SLES_FOUND ${OS_RELEASE})@' CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "Mariner" MARINER_FOUND ${OS_RELEASE})@#string(REGEX MATCH "Mariner" MARINER_FOUND ${OS_RELEASE})@' CMakeLists.txt

%build

%cmake \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/rocjpeg/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocjpeg/LICENSE
fi
if [ -f %{buildroot}%{_prefix}/share/doc/rocjpeg-asan/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocjpeg-asan/LICENSE
fi
if [ -f %{buildroot}%{_prefix}/share/doc/rocjpeg-dev/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocjpeg-dev/LICENSE
fi
if [ -f %{buildroot}%{_prefix}/share/doc/rocjpeg-test/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocjpeg-test/LICENSE
fi
if [ -f %{buildroot}%{_prefix}/share/doc/packages/%{name}/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/%{name}/LICENSE
fi
if [ -f %{buildroot}%{_prefix}/share/doc/packages/%{name}-dev/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/%{name}-dev/LICENSE
fi
if [ -f %{buildroot}%{_prefix}/share/doc/packages/%{name}-test/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/%{name}-test/LICENSE
fi
if [ -f %{buildroot}%{_prefix}/share/doc/packages/%{name}-asan/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/%{name}-asan/LICENSE
fi

# Need to install first
%if %{with test}
%check
%ctest
%endif

%files
%license LICENSE
%{_libdir}/librocjpeg.so.0{,.*}

%files devel
%{_libdir}/librocjpeg.so
%{_includedir}/rocjpeg
%{_datadir}/rocjpeg

%changelog
* Tue Feb 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-5
- Fix SLE 15.6

* Tue Feb 4 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-4
- Fix TW build

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-3
- multithread compress

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- build requires gcc-c++

* Wed Dec 25 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Initial package
