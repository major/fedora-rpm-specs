Summary:        Port of OpenAI's Whisper model in C/C++
Name:           whisper-cpp

License:        MIT
# Some execptions
# Apache-2
# bindings/java/gradlew*
# examples/whisper.android/gradlew*
# These are not distributed

Version:        1.7.1
Release:        %autorelease

URL:            https://github.com/ggerganov/whisper.cpp
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/whisper.cpp-%{version}.tar.gz
# https://github.com/ggerganov/whisper.cpp/pull/1791
# Patch0:         0001-Generalize-install-locations.patch

ExclusiveArch:  x86_64 aarch64 ppc64le
%global toolchain clang

# OpenVINO only supports x86_64 and aarch64
# Presently, Fedora only packages it on x86_64
%ifarch x86_64
# FIXME: Enable OpenVINO backend on 1.7.2 and later
%bcond_with openvino
%else
%bcond_with openvino
%endif

BuildRequires:  cmake
BuildRequires:  clang
%if %{with openvino}
BuildRequires:	openvino-devel
%endif

%description
High-performance inference of OpenAI's Whisper automatic speech
recognition (ASR) model:

* Plain C/C++ implementation without dependencies
* Apple Silicon first-class citizen - optimized via ARM NEON,
  Accelerate framework, Metal and Core ML
* AVX intrinsics support for x86 architectures
* VSX intrinsics support for POWER architectures
* Mixed F16 / F32 precision
* 4-bit and 5-bit integer quantization support
* Zero memory allocations at runtime
* Support for CPU-only inference
* Efficient GPU support for NVIDIA
* Partial OpenCL GPU support via CLBlast
* OpenVINO Support
* C-style API

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
High-performance inference of OpenAI's Whisper automatic speech
recognition (ASR) model:

* Plain C/C++ implementation without dependencies
* Apple Silicon first-class citizen - optimized via ARM NEON,
  Accelerate framework, Metal and Core ML
* AVX intrinsics support for x86 architectures
* VSX intrinsics support for POWER architectures
* Mixed F16 / F32 precision
* 4-bit and 5-bit integer quantization support
* Zero memory allocations at runtime
* Support for CPU-only inference
* Efficient GPU support for NVIDIA
* Partial OpenCL GPU support via CLBlast
* OpenVINO Support
* C-style API

%prep
%autosetup -p1 -n whisper.cpp-%{version}

# verson the ggml *.so
sed -i -e 's@POSITION_INDEPENDENT_CODE ON@POSITION_INDEPENDENT_CODE ON SOVERSION ${SOVERSION}@' ggml/src/CMakeLists.txt

%build

%cmake \
    -DWHISPER_BUILD_TESTS=ON \
%if %{with openvino}
    -DWHISPER_OPENVINO=1 \
%endif
    -DGGML_NATIVE=OFF \
    -DGGML_AVX=OFF \
    -DGGML_AVX2=OFF \
    -DGGML_AVX512=OFF \
    -DGGML_AVX512_VBMI=OFF \
    -DGGML_AVX512_VNNI=OFF \
    -DGGML_AVX512_BF16=OFF \
    -DGGML_FMA=OFF \
    -DGGML_F16C=OFF
    
%cmake_build

%install
%cmake_install

find %{buildroot} -name 'whisper.pc' -delete

%check
# FIXME: Tests have been disabled in upstream sources since v1.7.0
%ctest

%files
%license LICENSE
%{_libdir}/libggml.so.*
%{_libdir}/libwhisper.so.*

%files devel
%doc README.md
%{_includedir}/ggml*.h
%{_includedir}/whisper.h
%{_libdir}/libggml.so
%{_libdir}/libwhisper.so
%{_libdir}/cmake/whisper/*.cmake

%changelog
%autochangelog

