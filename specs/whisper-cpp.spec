Summary:        Port of OpenAI's Whisper model in C/C++
Name:           whisper-cpp

License:        MIT
# Some execptions
# Apache-2
# bindings/java/gradlew*
# examples/whisper.android/gradlew*
# These are not distributed

Version:        1.7.6
Release:        %autorelease

URL:            https://github.com/ggerganov/whisper.cpp
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/whisper.cpp-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64 ppc64le
%global toolchain gcc

# OpenVINO only supports x86_64 and aarch64
# Presently, Fedora only packages it on x86_64
%ifarch x86_64
%bcond_without openvino
%bcond_without rocm
%else
%bcond_with openvino
%bcond_with rocm
%endif

%if %{with openvino}
%global build_openvino ON
%else
%global build_openvino OFF
%endif

%if %{with rocm}
%global build_rocm ON
%else
%global build_rocm OFF
%global rocm_gpu_list_default %{nil}
%endif

%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

%global sover %{version}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git

%if %{with openvino}
BuildRequires:	openvino-devel
%endif

%if %{with rocm}
BuildRequires:  hipblas-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-rpm-macros
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

# Add SOVERSION to the shared libraries
sed -i -e 's@POSITION_INDEPENDENT_CODE ON@POSITION_INDEPENDENT_CODE ON SOVERSION %{sover}@' src/CMakeLists.txt
sed -i -e 's@POSITION_INDEPENDENT_CODE ON@POSITION_INDEPENDENT_CODE ON SOVERSION %{sover}@' ggml/src/CMakeLists.txt
sed -i -e 's@POSITION_INDEPENDENT_CODE ON@POSITION_INDEPENDENT_CODE ON SOVERSION %{sover}@' ggml/src/ggml-cpu/CMakeLists.txt
sed -i '/target_compile_definitions(${backend} PUBLIC  GGML_BACKEND_SHARED)/a\
set_target_properties(${backend} PROPERTIES POSITION_INDEPENDENT_CODE ON SOVERSION %{sover})' ggml/src/CMakeLists.txt

%build

%cmake \
    -DCMAKE_HIP_ARCHITECTURES=%{rocm_gpu_list_default} \
    -DWHISPER_BUILD_EXAMPLES=%{build_test} \
    -DWHISPER_BUILD_SERVER=%{build_test} \
    -DWHISPER_BUILD_TESTS=%{build_test} \
    -DWHISPER_OPENVINO=%{build_openvino} \
    -DGGML_HIP=%{build_rocm} \
    -DGGML_NATIVE=OFF \
    -DGGML_AMX_TILE=OFF \
    -DGGML_AMX_INT8=OFF \
    -DGGML_AMX_BF16=OFF \
    -DGGML_AVX=OFF \
    -DGGML_AVX_VNNI=OFF \
    -DGGML_AVX2=OFF \
    -DGGML_AVX512=OFF \
    -DGGML_AVX512_VBMI=OFF \
    -DGGML_AVX512_VNNI=OFF \
    -DGGML_AVX512_BF16=OFF \
    -DGGML_BMI2=OFF \
    -DGGML_FMA=OFF \
    -DGGML_F16C=OFF \
    -DGGML_LASX=OFF \
    -DGGML_LSX=OFF \
    -DGGML_RVV=OFF \
    -DGGML_RV_ZFH=OFF \
    -DGGML_SSE42=OFF \
    -DGGML_XTHEADVECTOR=OFF \
    -DGGML_VXE=OFF
    
%cmake_build

%install
%cmake_install

find %{buildroot} -name 'whisper.pc' -delete

%check
%if %{with test}
# FIXME: Tests have been disabled in upstream sources since v1.7.0
%ctest
%endif

%files
%license LICENSE
%{_libdir}/libggml.so.*
%{_libdir}/libggml-base.so.*
%{_libdir}/libggml-cpu.so.*
%{_libdir}/libwhisper.so.*

%if %{with rocm}
%{_libdir}/libggml-hip.so.*
%endif

%files devel
%doc README.md
%{_includedir}/ggml*.h
%{_includedir}/gguf.h
%{_includedir}/whisper.h
%{_libdir}/libggml.so
%{_libdir}/libggml-base.so
%{_libdir}/libggml-cpu.so
%{_libdir}/libwhisper.so
%dir %{_libdir}/cmake/whisper
%dir %{_libdir}/cmake/ggml
%{_libdir}/cmake/whisper/*.cmake
%{_libdir}/cmake/ggml/*.cmake

%if %{with rocm}
%{_libdir}/libggml-hip.so
%endif

%changelog
%autochangelog

