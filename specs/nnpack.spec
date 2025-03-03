%global commit0 70a77f485e8b934224f3a79efd8edcd84cd377b8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20230202
%global upstream_name NNPACK

Summary:        Acceleration package for neural networks on multi-core CPUs
Name:           nnpack
License:        BSD-2-Clause
Version:        1.0^git%{date0}.%{shortcommit0}
Release:        %autorelease

ExclusiveArch:  x86_64

URL:            https://github.com/Maratyszcza/%{name}
Source0:        %{url}/archive/%{commit0}/%{upstream_name}-%{shortcommit0}.tar.gz
# Need some version for the *.so, use the date yy.m.d
Patch0:         0001-Add-soversion-to-nnpack.patch

BuildRequires: cmake
BuildRequires: cpuinfo-devel
BuildRequires: FP16-devel
BuildRequires: fxdiv-devel
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: psimd-devel
BuildRequires: pthreadpool-devel

BuildRequires: python3-devel
BuildRequires: python3dist(peachpy)

%description
NNPACK is an acceleration package for neural network computations. NNPACK
aims to provide high-performance implementations of convnet layers for
multi-core CPUs.

NNPACK is not intended to be directly used by machine learning researchers;
instead it provides low-level performance primitives leveraged in leading
deep learning frameworks, such as PyTorch, Caffe2, MXNet, tiny-dnn, Caffe,
Torch, and Darknet.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstream_name}-%{commit0}

# Do not download things
sed -i -e 's@NOT DEFINED PYTHON_SIX_SOURCE_DIR@NOT@' CMakeLists.txt
sed -i -e 's@NOT DEFINED PYTHON_PEACHPY_SOURCE_DIR@NOT@' CMakeLists.txt
sed -i -e 's@NOT DEFINED CPUINFO_SOURCE_DIR@NOT@' CMakeLists.txt
sed -i -e 's@NOT TARGET cpuinfo@NOT@' CMakeLists.txt
sed -i -e 's@NOT DEFINED FP16_SOURCE_DIR@NOT@' CMakeLists.txt
sed -i -e 's@NOT TARGET fp16@NOT@' CMakeLists.txt
sed -i -e 's@NOT DEFINED FXDIV_SOURCE_DIR@NOT@' CMakeLists.txt
sed -i -e 's@NOT TARGET fxdiv@NOT@' CMakeLists.txt
sed -i -e 's@NOT DEFINED PTHREADPOOL_SOURCE_DIR@NOT@' CMakeLists.txt
sed -i -e 's@NOT TARGET pthreadpool@NOT@' CMakeLists.txt
sed -i -e 's@NOT DEFINED PSIMD_SOURCE_DIR@NOT@' CMakeLists.txt
sed -i -e 's@NOT TARGET psimd@NOT@' CMakeLists.txt
sed -i -e 's@NOT DEFINED GOOGLETEST_SOURCE_DIR@NOT@' CMakeLists.txt

# Header only packages, no library, do not link
sed -i -e 's@TARGET_LINK_LIBRARIES(nnpack PRIVATE fxdiv)@#TARGET_LINK_LIBRARIES(nnpack PRIVATE fxdiv)@' CMakeLists.txt
sed -i -e 's@TARGET_LINK_LIBRARIES(nnpack PRIVATE psimd)@#TARGET_LINK_LIBRARIES(nnpack PRIVATE psimd)@' CMakeLists.txt
sed -i -e 's@TARGET_LINK_LIBRARIES(nnpack PRIVATE fp16)@#TARGET_LINK_LIBRARIES(nnpack PRIVATE fp16)@' CMakeLists.txt
sed -i -e 's@TARGET_LINK_LIBRARIES(nnpack_reference_layers PUBLIC fp16)@#TARGET_LINK_LIBRARIES(nnpack_reference_layers PUBLIC fp16)@' CMakeLists.txt

# cmake version changed
sed -i -e 's@CMAKE_MINIMUM_REQUIRED(VERSION 2.8.12 FATAL_ERROR)@CMAKE_MINIMUM_REQUIRED(VERSION 3.5 FATAL_ERROR)@' CMakeLists.txt

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DNNPACK_BUILD_TESTS=OFF \
    -DNNPACK_LIBARY_TYPE=shared

%cmake_build

# Buiding tests is broken
# % check
# % ctest

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
