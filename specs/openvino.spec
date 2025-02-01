%define so_ver 2450
%global desc %{expand: \
OpenVINO is an open-source toolkit for optimizing and deploying deep learning
models from cloud to edge. It accelerates deep learning inference across
various use cases, such as generative AI, video, audio, and language with
models from popular frameworks like PyTorch, TensorFlow, ONNX, and more.}

Name:		openvino
Version:	2024.5.0
Release:	%autorelease
Summary:	Toolkit for optimizing and deploying AI inference

# Most of the source code is Apache-2.0, with the following exceptions:
# src/core/reference/include/openvino/reference/deformable_psroi_pooling.hpp : MIT
# src/core/src/type/nf4.cpp : MIT
# src/plugins/intel_cpu/src/hash_builder.hpp : BSL-1.0
# src/core/reference/include/openvino/reference/interpolate_pil.hpp : HPND
# oneDNN-373e65b/src/common/utils.hpp : BSL-1.0
# oneDNN-373e65b/src/graph/backend/graph_compiler/core/src/util/hash_utils.hpp : BSL-1.0
# oneDNN-373e65b/src/cpu/x64/xbyak/xbyak.h : BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/disable_warnings.h : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/ittnotify_config.h : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/ittnotify.h : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/ittnotify_static.c : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/ittnotify_static.h : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/ittnotify_types.h : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/jitprofiling.c : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/jitprofiling.h : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/common/ittnotify/legacy/ittnotify.h : GPL-2.0-only OR BSD-3-Clause
# oneDNN-373e65b/src/sycl/level_zero/layers/zel_tracing_api.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/layers/zel_tracing_ddi.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/layers/zel_tracing_register_cb.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/loader/ze_loader.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/ze_api.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/ze_ddi.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/zes_api.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/zes_ddi.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/zet_api.h : MIT
# oneDNN-373e65b/src/sycl/level_zero/zet_ddi.h : MIT
License:	Apache-2.0 AND MIT AND BSL-1.0 AND HPND AND BSD-3-Clause AND (GPL-2.0-only OR BSD-3-Clause)
URL:		https://github.com/openvinotoolkit/openvino
Source0:	%url/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/openvinotoolkit/oneDNN/archive/c60a9946aa2386890e5c9f5587974facb7624227/onednn-c60a994.tar.gz
Source2:	https://github.com/openvinotoolkit/mlas/archive/d1bc25ec4660cddd87804fcf03b2411b5dfb2e94/mlas-d1bc25e.tar.gz
Source3:	https://github.com/intel/level-zero-npu-extensions/archive/110f48ee8eda22d8b40daeeecdbbed0fc3b08f8b/level-zero-npu-extensions-110f48e.tar.gz
Source4:	dependencies.cmake
Source5:	pyproject.toml

Patch0:		openvino-fedora.patch
# Support numpy 2.2.0
Patch1:		https://github.com/openvinotoolkit/openvino/pull/28039.patch
Patch2:		npu-level-zero.patch

ExclusiveArch:	x86_64

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gflags-devel
BuildRequires:	oneapi-level-zero-devel
BuildRequires:	patchelf
BuildRequires:	pugixml-devel
BuildRequires:	pybind11-devel
BuildRequires:	python3-devel
BuildRequires:	python3-pip
BuildRequires:	python3-setuptools
BuildRequires:	python3-wheel
BuildRequires:	numpy
BuildRequires:	ShellCheck
BuildRequires:	zlib-ng-compat-devel
BuildRequires:	xbyak-devel
BuildRequires:	yaml-cpp-devel
BuildRequires:	tbb-devel
# forked version of OpenVINO oneDNN does not have a proper version
Provides:	bundled(onednn)
# MLAS upstream does not have any release
Provides:	bundled(mlas)
Requires:	lib%{name}-ir-frontend = %{version}
Requires:	lib%{name}-pytorch-frontend = %{version}
Requires:	numpy
Recommends:	%{name}-plugins = %{version}

%description
%{desc}

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package plugins
Summary:	OpenVINO Plugins
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description plugins
The OpenVINO plugins package provides support for various hardware devices.
It includes plugins for auto, auto_batch, hetero, intel_cpu and template.

%package -n lib%{name}-ir-frontend
Summary:	OpenVINO IR Frontend
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-ir-frontend
The primary function of the OpenVINO IR Frontend is to load an OpenVINO IR
into memory.

%package -n lib%{name}-pytorch-frontend
Summary:	OpenVINO PyTorch Frontend
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-pytorch-frontend
The PyTorch Frontend is a C++ based OpenVINO Frontend component that is 
responsible for reading and converting a PyTorch model to an ov::Model object
that can be further serialized into the Intermediate Representation (IR) format

%package -n python3-%{name}
Summary:	OpenVINO Python API
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
OpenVINO Python API allowing users to use the OpenVINO library in their Python
code. Python API provides bindings to basic and advanced APIs from OpenVINO
runtime.

%prep
%autosetup -p1

# Remove the thirdparty deps
rm -rf thirdparty/*
cp %{SOURCE4} thirdparty/

# Intel-cpu-plugin thirdparty deps
tar xf %{SOURCE1}
cp -r oneDNN-*/* src/plugins/intel_cpu/thirdparty/onednn
tar xf %{SOURCE2}
cp -r mlas-*/* src/plugins/intel_cpu/thirdparty/mlas

# Intel-npu-plugin thirdparty deps
rm -rf src/plugins/intel_npu/thirdparty/yaml-cpp
tar xf %{SOURCE3}
cp -r level-*/* src/plugins/intel_npu/thirdparty/level-zero-ext

# python:prep
sed -i '/openvino-telemetry/d' src/bindings/python/requirements.txt
cp %{SOURCE5} src/bindings/python

# gcc 15 include cstdint
sed -i '/#include <vector>.*/a#include <cstdint>' src/core/include/openvino/core/type/bfloat16.hpp
sed -i '/#include <vector>.*/a#include <cstdint>' src/core/include/openvino/core/type/float16.hpp
sed -i '/#include <vector>.*/a#include <cstdint>' src/core/include/openvino/core/type/float8_e4m3.hpp
sed -i '/#include <vector>.*/a#include <cstdint>' src/core/include/openvino/core/type/float8_e5m2.hpp
sed -i '/#include <vector>.*/a#include <cstdint>' src/core/include/openvino/core/type/float8_e8m0.hpp
sed -i '/#include <vector>.*/a#include <cstdint>' src/core/include/openvino/core/type/float4_e2m1.hpp
sed -i '/#include <vector>.*/a#include <cstdint>' src/core/dev_api/openvino/core/type/nf4.hpp
sed -i '/#include <utility>.*/a#include <cstdint>' src/common/snippets/include/snippets/utils/debug_caps_config.hpp
sed -i '/#include <utility>.*/a#include <cstdint>' src/plugins/intel_cpu/src/utils/debug_caps_config.h
sed -i '/#include <vector>.*/a#include <cstdint>' src/plugins/intel_npu/src/plugin/npuw/partitioning/online/graph.hpp

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_CXX_FLAGS="%{optflags} -Wformat -Wformat-security" \
	-DENABLE_CLANG_FORMAT=OFF \
	-DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
	-DENABLE_QSPECTRE=OFF \
	-DENABLE_INTEGRITYCHECK=OFF \
	-DENABLE_SANITIZER=OFF \
	-DENABLE_UB_SANITIZER=OFF \
	-DENABLE_THREAD_SANITIZER=OFF \
	-DENABLE_COVERAGE=OFF \
	-DENABLE_FASTER_BUILD=OFF \
	-DENABLE_CPPLINT=OFF \
	-DENABLE_CPPLINT_REPORT=OFF \
	-DENABLE_GAPI_PREPROCESSING=OFF \
	-DENABLE_NCC_STYLE=OFF \
	-DENABLE_UNSAFE_LOCATIONS=OFF \
	-DENABLE_FUZZING=OFF \
	-DENABLE_PROFILING_ITT=OFF \
	-DENABLE_PKGCONFIG_GEN=ON \
	-DENABLE_STRICT_DEPENDENCIES=OFF \
	-DENABLE_DEBUG_CAPS=ON \
	-DENABLE_AUTO=ON \
	-DENABLE_AUTO_BATCH=ON \
	-DENABLE_HETERO=ON \
	-DENABLE_INTEL_CPU=ON \
	-DENABLE_MLAS_FOR_CPU=ON \
	-DENABLE_MLAS_FOR_CPU_DEFAULT=ON \
	-DENABLE_INTEL_GNA=OFF \
	-DENABLE_INTEL_GPU=OFF \
	-DENABLE_SYSTEM_LEVEL_ZERO=ON \
	-DENABLE_INTEL_NPU=ON \
	-DENABLE_NPU_PLUGIN_ENGINE=ON \
	-DENABLE_ONEDNN_FOR_GPU=OFF \
	-DENABLE_MULTI=ON \
	-DENABLE_PROXY=ON \
	-DENABLE_TEMPLATE=ON \
	-DENABLE_OV_ONNX_FRONTEND=OFF \
	-DENABLE_OV_PADDLE_FRONTEND=OFF \
	-DENABLE_OV_IR_FRONTEND=ON \
	-DENABLE_OV_PYTORCH_FRONTEND=ON \
	-DENABLE_OV_TF_FRONTEND=OFF \
	-DENABLE_OV_TF_LITE_FRONTEND=OFF \
	-DENABLE_PYTHON=ON \
	-DPython3_EXECUTABLE=%{python3} \
	-DENABLE_WHEEL=OFF \
	-DENABLE_JS=OFF \
	-DENABLE_SYSTEM_LIBS_DEFAULT=ON \
	-DENABLE_SYSTEM_OPENCL=OFF \
	-DENABLE_SYSTEM_PUGIXML=ON \
	-DENABLE_SYSTEM_PROTOBUF=OFF \
	-DTHREADING=TBB \
	-DENABLE_SYSTEM_TBB=ON \
	-DTBB_LIB_INSTALL_DIR=%{_libdir} \
	-DENABLE_TBBBIND_2_5=OFF \
	-DENABLE_TBB_RELEASE_ONLY=ON \
	-DENABLE_SAMPLES=OFF \
	-DENABLE_TESTS=OFF \
	-DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install
# generate python dist-info
export WHEEL_VERSION=%{version}
%{python3} src/bindings/python/wheel/setup.py dist_info -o %{buildroot}/%{python3_sitearch}
rm -v %{buildroot}/%{python3_sitearch}/requirements.txt
rm -v %{buildroot}/%{python3_sitearch}/%{name}/preprocess/torchvision/requirements.txt

%check
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir} PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} samples/python/hello_query_device/hello_query_device.py
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir} PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} samples/python/model_creation_sample/model_creation_sample.py samples/python/model_creation_sample/lenet.bin CPU

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{so_ver}
%{_libdir}/lib%{name}_c.so.%{version}
%{_libdir}/lib%{name}_c.so.%{so_ver}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_c.so
%{_libdir}/lib%{name}_pytorch_frontend.so
%{_libdir}/cmake/openvino-%{version}
%{_libdir}/pkgconfig/%{name}.pc

%files plugins
%dir %_libdir/%{name}-%{version}
%{_libdir}/%{name}-%{version}/lib%{name}_auto_plugin.so
%{_libdir}/%{name}-%{version}/lib%{name}_auto_batch_plugin.so
%{_libdir}/%{name}-%{version}/lib%{name}_hetero_plugin.so
%{_libdir}/%{name}-%{version}/lib%{name}_intel_cpu_plugin.so
%{_libdir}/%{name}-%{version}/lib%{name}_intel_npu_plugin.so
%{_bindir}/compile_tool

%files -n lib%{name}-ir-frontend
%{_libdir}/lib%{name}_ir_frontend.so.%{version}
%{_libdir}/lib%{name}_ir_frontend.so.%{so_ver}

%files -n lib%{name}-pytorch-frontend
%{_libdir}/lib%{name}_pytorch_frontend.so.%{version}
%{_libdir}/lib%{name}_pytorch_frontend.so.%{so_ver}

%files -n python3-%{name}
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-%{version}.dist-info

%changelog
%autochangelog
