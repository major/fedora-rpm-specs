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
%global upstreamname hipfort
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

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Needs ROCm HW so is only suitable for local testing
%bcond_with check

Name:           hipfort%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        Fortran interfaces for ROCm libraries

Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch0:         0001-Handle-cmake-DBUILD_SHARED_LIBS-ON.patch
Patch1:         0001-Generalize-hipfc-to-other-linux-distros.patch
# https://github.com/ROCm/hipfort/issues/261
Patch2:         0001-hipfort-remove-build-type-check.patch
# https://github.com/ROCm/hipfort/issues/279
Patch3:         0001-hipfort-remove-rocblas_sgemm_kernel_name.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  hipblas%{pkg_suffix}-devel
BuildRequires:  hipfft%{pkg_suffix}-devel
BuildRequires:  hiprand%{pkg_suffix}-devel
BuildRequires:  hipsolver%{pkg_suffix}-devel
BuildRequires:  hipsparse%{pkg_suffix}-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocblas%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocfft%{pkg_suffix}-devel
BuildRequires:  rocrand%{pkg_suffix}-devel
BuildRequires:  rocsolver%{pkg_suffix}-devel
BuildRequires:  rocsparse%{pkg_suffix}-devel

Requires:       rocminfo%{pkg_suffix}

# ROCm is only x86_64 for now
ExclusiveArch:  x86_64

%description
This repository contains the source and testing for hipfort.
This is a FORTRAN interface library for accessing GPU Kernels.

%package devel
Summary:        The %{name} development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The headers of libraries for %{name}.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Can not pass -L*, hipfc gets confused and treats '-' as the start of a passthrough arg 
sed -i -e 's|-o $@|-lrocfft -lrocrand -lrocblas -lrocsolver -lrocsparse -lhipfft -lhiprand -lhipblas -lhipsolver -lhipsparse -o $@|' test/Makefile.in

# For CMake 4
sed -i 's@cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR@cmake_minimum_required(VERSION 3.5@' bin/CMakeLists.txt


%build

%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_Fortran_FLAGS="-fPIE -L%{pkg_prefix}/%{pkg_libdir}" \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_SKIP_RPATH=ON \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=%{build_type}

%cmake_build

# Assume you _just_ installed hipfort-devel as the tests assume hipfc is in the PATH
%if %{with check}
%check
# Mixing rpm gfortran security flags with hipcc does not work
# Override the normal rpm flags
export CFLAGS=""
export CXXFLAGS=""
export FFLAGS=""
export FCFLAGS=""
export LDFLAGS=""
# hipfc needs these set to find things
export HIPFORT="%{pkg_prefix}"
export ROCM_PATH="%{pkg_prefix}"
%cmake_build -t all-tests-run
%endif

%install
%cmake_install
# nvidia is not supported on Fedora
rm -rf %{buildroot}%{pkg_prefix}/include/hipfort/nvptx
rm -rf %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libhipfort-nvptx*

# rpmbuild has a problem with this file
rm %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake/hipfort/hipfort-config.cmake

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipfort/LICENSE

%files
%license LICENSE
%doc README.md
%{pkg_prefix}/bin/hipfc
%{pkg_prefix}/%{pkg_libdir}/libhipfort-amdgcn.so.*
%{pkg_prefix}/libexec/hipfort

%files devel
%{pkg_prefix}/share/hipfort/
%{pkg_prefix}/include/hipfort/
%{pkg_prefix}/%{pkg_libdir}/libhipfort-amdgcn.so
%{pkg_prefix}/%{pkg_libdir}/cmake/hipfort/

%changelog
* Fri Jan 30 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-1
- Update to 7.2.0

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jan 8 2026 Tom Rix <Tom.Rix@amd.com> - 7.1.0-3
- Remove rocblas_sgemm_kernel_name and similar
- Add requires rocminfo

* Wed Dec 24 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Add --with compat
- Change --with test to --with check

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Sun Sep 21 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Aug 28 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-2
- Add Fedora copyright

* Thu Jul 24 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.2-1
- Update to 6.4.2

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-2
- Increase the minimum cmake version

* Sun Apr 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

