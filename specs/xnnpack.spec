# So pre releases can be tried
%bcond_with gitcommit

%if %{with gitcommit}
# Something recent to match change to cpuinfo
%global commit0 312eb7e13554ce75d02c5cb27357555f1368f2d1
%global date0 20240814

%else
# For PyTorch 2.5
%global commit0 312eb7e13554ce75d02c5cb27357555f1368f2d1
%global date0 20240814
%endif

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


%global upstream_name XNNPACK

# This project is not well behaved so build in source
%global __cmake_in_source_build 1
# No debug info
%global debug_package %{nil}

Summary:        High-efficiency floating-point neural network inference operators
Name:           xnnpack
License:        BSD-3-Clause
Version:        0.0^git%{date0}.%{shortcommit0}
Release:        %autorelease

URL:            https://github.com/google/%{upstream_name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# https://github.com/google/XNNPACK/pull/6144
Patch0:         0001-Fix-cmake-for-pthread-and-cpuinfo-with-USE_SYSTEM_LI.patch

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  cpuinfo-devel
BuildRequires:  FP16-devel
BuildRequires:  fxdiv-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  pthreadpool-devel

%description
XNNPACK is a highly optimized solution for neural network inference on ARM,
x86, WebAssembly, and RISC-V platforms. XNNPACK is not intended for direct
use by deep learning practitioners and researchers; instead it provides
low-level performance primitives for accelerating high-level machine learning
frameworks, such as TensorFlow Lite, TensorFlow.js, PyTorch, ONNX Runtime,
and MediaPipe.

%package devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstream_name}-%{commit0}

# version of the *.so
echo "SET_TARGET_PROPERTIES(XNNPACK PROPERTIES SOVERSION \"24.08.14\")" >> CMakeLists.txt

%build
%cmake -G Ninja \
      -DBUILD_SHARED_LIBS=ON \
      -DCMAKE_C_FLAGS=-fPIC \
      -DCMAKE_CXX_FLAGS=-fPIC \
      -DXNNPACK_BUILD_BENCHMARKS=OFF \
      -DXNNPACK_BUILD_LIBRARY=ON \
      -DXNNPACK_BUILD_TESTS=OFF \
      -DXNNPACK_ENABLE_KLEIDIAI=OFF \
      -DXNNPACK_USE_SYSTEM_LIBS=ON \
      -DXNNPACK_LIBRARY_TYPE=shared

%cmake_build

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 include/xnnpack.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
strip libXNNPACK.so.24.08.14
install -p -m 755 libXNNPACK.so.24.08.14 %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
ln -s libXNNPACK.so.24.08.14 libXNNPACK.so

# building tests or benchmarks is broken
# % check
# ctest

%files
%license LICENSE
%{_libdir}/libXNNPACK.so.*

%files devel
%doc README.md
%{_includedir}/xnnpack.h
%{_libdir}/libXNNPACK.so

%changelog
%autochangelog
