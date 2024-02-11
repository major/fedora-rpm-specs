Summary:        Port of OpenAI's Whisper model in C/C++
Name:           whisper-cpp

License:        MIT
# Some execptions
# Apache-2
# bindings/java/gradlew*
# examples/whisper.android/gradlew*
# These are not distributed

Version:        1.5.4
Release:        %autorelease

URL:            https://github.com/ggerganov/whisper.cpp
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/whisper.cpp-%{version}.tar.gz
# https://github.com/ggerganov/whisper.cpp/pull/1791
Patch0:         0001-Generalize-install-locations.patch
# https://github.com/ggerganov/whisper.cpp/pull/1792
Patch1:         0001-libwhisper.so-should-be-position-independent.patch

ExclusiveArch:  x86_64 aarch64 ppc64le
%global toolchain clang

BuildRequires:  cmake
BuildRequires:  clang

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

# verson the *.so
sed -i -e 's/POSITION_INDEPENDENT_CODE ON/POSITION_INDEPENDENT_CODE ON SOVERSION %{version}/' CMakeLists.txt

%build

%cmake \
    -DWHISPER_BUILD_TESTS=ON \
    -DWHISPER_NO_AVX=ON \
    -DWHISPER_NO_AVX2=ON \
    -DWHISPER_NO_FMA=ON \
    -DWHISPER_NO_F16C=ON
    
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_libdir}/libwhisper.so.%{version}

%files devel
%doc README.md
%{_includedir}/ggml.h
%{_includedir}/whisper.h
%{_libdir}/libwhisper.so

%changelog
%autochangelog

