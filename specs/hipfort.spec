%global upstreamname hipfort
%global rocm_release 6.3
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Needs ROCm HW so is only suitable for local testing
%bcond_with test

Name:           hipfort
Version:        %{rocm_version}
Release:        %autorelease
Summary:        Fortran interfaces for ROCm libraries

Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch0:         0001-Handle-cmake-DBUILD_SHARED_LIBS-ON.patch
Patch1:         0001-Generalize-hipfc-to-other-linux-distros.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  hipcc
BuildRequires:  hipblas-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsolver-devel
BuildRequires:  hipsparse-devel
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake
BuildRequires:  rocblas-devel
BuildRequires:  rocfft-devel
BuildRequires:  rocrand-devel
BuildRequires:  rocsolver-devel
BuildRequires:  rocsparse-devel


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

sed -i -e 's/-o $@/-lrocfft -lrocrand -lrocblas -lrocsolver -lrocsparse -lhipfft -lhiprand -lhipblas -lhipsolver -lhipsparse -o $@/' test/Makefile.in

%build

%cmake -G Ninja \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_SKIP_RPATH=ON \
       -DROCM_SYMLINK_LIBS=OFF \
       -DHIP_PLATFORM=amd \
       -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_BUILD_TYPE=%{build_type}

%cmake_build

# Assume you _just_ installed hipfort as the tests assume hipfc is in the PATH
%if %{with test}
%check
# Mixing rpm gfortran security flags with hipcc does not work
# Override the normal rpm flags
export CFLAGS=""
export CXXFLAGS=""
export FFLAGS=""
export FCFLAGS=""
export LDFLAGS=""
%cmake_build -t all-tests-run
%endif

%install
%cmake_install
# nvidia is not supported on Fedora
rm -rf %{buildroot}%{_includedir}/%{name}/nvptx
rm -rf %{buildroot}%{_libdir}/lib%{name}-nvptx*

# rpmbuild has a problem with this file
rm %{buildroot}%{_libdir}/cmake/%{name}/%{name}-config.cmake

%files
%license LICENSE
%exclude %{_docdir}/%{name}/LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_includedir}/%{name}
%dir %{_libdir}/cmake/%{name}
%{_bindir}/hipfc
%{_libdir}/lib%{name}-amdgcn.so.*
%{_libexecdir}/%{name}


%files devel
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/lib%{name}-amdgcn.so
%{_libdir}/cmake/%{name}

%changelog
%autochangelog

