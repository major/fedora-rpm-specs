# So pre releases can be tried
%bcond_with gitcommit

%if %{with gitcommit}
# commit is what PyTorch 2.3 at its gitcommit expects
%global commit0 fcbf55af6cf28a4627bcd1f703ab7ad843f0f3a2
%global date0 20240229
%else
# commit is what PyTorch 2.1 expects, TOT has API changes that break PyTorch
%global commit0 51a987591a6fc9f0fc0707077f53d763ac132cbf
%global date0 20221221
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
%if %{with gitcommit}
# https://github.com/google/XNNPACK/pull/6144
Patch0:         0001-Fix-cmake-for-pthread-and-cpuinfo-with-USE_SYSTEM_LI.patch
%else
Patch0:         0001-Prepare-xnnpack-cmake-for-fedora.patch
%endif

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

%if %{with gitcommit}
# On RHEL 9, gcc 11, there is this error
# /tmp/ccnF75eP.s:120: Error: unsupported instruction `vpdpbusd'
sed -i 's@IF(CMAKE_C_COMPILER_VERSION VERSION_LESS "11")@IF(CMAKE_C_COMPILER_VERSION VERSION_LESS "13")@' CMakeLists.txt
# version of the *.so
echo "SET_TARGET_PROPERTIES(XNNPACK PROPERTIES SOVERSION \"24.02.29\")" >> CMakeLists.txt

%endif

%build
%cmake -G Ninja \
      -DBUILD_SHARED_LIBS=ON \
      -DCMAKE_C_FLAGS=-fPIC \
      -DCMAKE_CXX_FLAGS=-fPIC \
      -DXNNPACK_BUILD_BENCHMARKS=OFF \
      -DXNNPACK_BUILD_LIBRARY=ON \
      -DXNNPACK_BUILD_TESTS=OFF \
      -DXNNPACK_USE_SYSTEM_LIBS=ON \
      -DXNNPACK_LIBRARY_TYPE=shared

%cmake_build

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 include/xnnpack.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
%if %{with gitcommit}
strip libXNNPACK.so.24.02.29
install -p -m 755 libXNNPACK.so.24.02.29 %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
ln -s libXNNPACK.so.24.02.29 libXNNPACK.so
%else
strip libXNNPACK.so.0.0.221221
install -p -m 755 libXNNPACK.so.0.0.221221 %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
ln -s libXNNPACK.so.0.0.221221 libXNNPACK.so
%endif

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
* Tue Jan 30 2024 Tom Rix <trix@redhat.com> - 0.0^git20221221.51a9875-4
- Fix arm build

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0^git20221221.51a9875-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Tom Rix <trix@redhat.com> - 0.0^git20221221.51a9875-2
- Address review comments

* Thu Oct 5 2023 Tom Rix <trix@redhat.com> - 0.0^git20221221.51a9875-1
- Initial package
