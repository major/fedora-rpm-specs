# header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/root-project/veccore
Version:        0.8.1
%forgemeta

Name:           veccore
Release:        %autorelease
Summary:        C++ Library for Portable SIMD Vectorization
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gtest-devel

%description
VecCore is a simple abstraction layer on top of other vectorization libraries.
It provides an architecture-independent API for expressing vector operations on
data. Code written with this API can then be dispatched to one of several
backends implemented using libraries like Vc, UME::SIMD, or a scalar
implementation. This allows one to get the best performance on platforms
supported by Vc and UME::SIMD without losing portability to unsupported
architectures like PowerPC, for example, where the scalar backends can be used
instead without requiring changes in user code. Another advantage is that,
unlike with compiler intrinsics, the same code can be compiled for SSE, AVX2,
AVX512, etc, without modifications. With the addition of new backends, such as
the new backend based on C++20 and std::experimental::simd, users can
automatically take advantage of new features and better performance. This
backend supports AVX512 on Intel/AMD64 and NEON on ARM/ARM64, with best
performance in most cases. However, it does require compiling code in C++20
mode, which may not always be possible, so there is still an advantage in using
it via VecCore's implementation to have a fallback when C++20 is not avaialble.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains header files for developing applications that
use %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DBUILD_TESTING=ON \

%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/VecCore/
%dir %{_libdir}/cmake/VecCore
%{_libdir}/cmake/VecCore/*.cmake

%changelog
%autochangelog
