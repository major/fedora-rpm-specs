# TESTING NOTE: An OpenCL device is needed to run the tests.  Since the koji
# builders may or may not have a GPU, we use the CPU-only POCL implementation.
#
# Except, as of pocl 3.1, the tests no longer pass.  We get this:
#
# The following tests FAILED:
#	 10 - clblast_test_xamax (Subprocess aborted)
#	 48 - clblast_test_xaxpybatched (Failed)
#	 49 - clblast_test_xgemmbatched (Failed)
#
# Reverting to pocl 1.8 makes the tests pass.  We seem unable to run the tests
# at all at this point.  Try again when pocl 4.0 is released.

# https://koji.fedoraproject.org/koji/taskinfo?taskID=113330948
%bcond_with check
%bcond_with pocl

Name:           clblast
Version:        1.6.3
Release:        %autorelease
Summary:        Tuned OpenCL BLAS routines

License:        Apache-2.0
URL:            https://cnugteren.github.io/clblast/clblast.html
Source0:        https://github.com/CNugteren/CLBlast/archive/%{version}/%{name}-%{version}.tar.gz
# Fix name clashes between macros in altivec.h and standard types on ppc64le
Patch0:         %{name}-altivec.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(flexiblas)
%if %{with pocl}
BuildRequires:  pocl-devel
%endif
BuildRequires:  ocl-icd-devel


%description
CLBlast is a modern, lightweight, performant and tunable OpenCL BLAS
library written in C++11.  It is designed to leverage the full
performance potential of a wide variety of OpenCL devices from different
vendors, including desktop and laptop GPUs, embedded GPUs, and other
accelerators.  CLBlast implements BLAS routines: basic linear algebra
subprograms operating on vectors and matrices.  See the CLBlast website
for performance reports on various devices as well as the latest CLBlast
news.

The library is not tuned for all possible OpenCL devices: if
out-of-the-box performance is poor, please run the tuners first.

%package devel
Summary:        Headers and libraries for CLBlast
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocl-icd-devel%{?_isa}

%description devel
Headers and libraries for developing applications that use CLBlast.

%package clients
Summary:        Clients for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description clients
Clients to test and compare performance of %{name} for your OpenCL device.

%package tuners
Summary:        Tuners for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tuners
Programs to tune %{name} for your OpenCL device.

%prep
%autosetup -p0 -n CLBlast-%{version}

# Fix the path to the openblas headers
sed -i 's,openblas/include,include/openblas,' cmake/Modules/FindCBLAS.cmake
# Add paths for FlexiBLAS
sed -i 's,include/openblas,include/openblas include/flexiblas,' cmake/Modules/FindCBLAS.cmake
sed -i 's,NAMES cblas blas,NAMES cblas blas flexiblas,' cmake/Modules/FindCBLAS.cmake
# For CMake 4
sed -i 's@cmake_minimum_required(VERSION 2.8.11@cmake_minimum_required(VERSION 3.5@' CMakeLists.txt
sed -i 's@cmake_minimum_required(VERSION 3.20@cmake_minimum_required(VERSION 3.5@' src/pyclblast/CMakeLists.txt

%build
# https://github.com/CNugteren/CLBlast/issues/529
# add -Wno-error=format-security to CMAKE_CXX_FLAGS when building tests
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCLIENTS=ON \
  -DNETLIB=ON \
%if %{with check}
  -DTESTS=ON \
  -DCMAKE_CXX_FLAGS="%{optflags} -Wno-error=format-security" \
%else
  -DTESTS=OFF \
%endif

%cmake_build

%install
%cmake_install

%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE
%doc CHANGELOG README.md
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc doc
%{_includedir}/%{name}*.h
%{_libdir}/lib{%name}.so
%{_libdir}/cmake/CLBlast/
%{_libdir}/pkgconfig/%{name}.pc

%files clients
%{_bindir}/clblast_client*

%files tuners
%{_bindir}/clblast_tuner*

%changelog
%autochangelog
