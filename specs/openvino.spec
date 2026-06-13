#
# Copyright (C) 2026 Intel Corporation
#
# Please submit issues or comments https://github.com/openvinotoolkit/openvino/issues

%global so_ver 2600

%global desc %{expand:OpenVINO is an open-source toolkit for optimizing and deploying deep learning
models from cloud to edge. It accelerates deep learning inference across
various use cases, such as generative AI, video, audio, and language with
models from popular frameworks like PyTorch, TensorFlow, ONNX, and more.}

Name:           openvino
Version:        2026.0.0
Release:        %autorelease
Summary:        Toolkit for optimizing and deploying AI inference

# Most of the source code is Apache-2.0, with the following exceptions:
# src/core/reference/include/openvino/reference/deformable_psroi_pooling.hpp : MIT
# src/core/src/type/nf4.cpp : MIT
# src/plugins/intel_cpu/src/hash_builder.hpp : BSL-1.0
# src/core/reference/include/openvino/reference/interpolate_pil.hpp : HPND
# oneDNN: BSL-1.0, BSD-3-Clause, (GPL-2.0-only OR BSD-3-Clause), MIT
License:        Apache-2.0 AND MIT AND BSL-1.0 AND HPND AND BSD-3-Clause AND (GPL-2.0-only OR BSD-3-Clause)
URL:            https://github.com/openvinotoolkit/openvino

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/openvinotoolkit/oneDNN/archive/c6b79c1207bd5f20b9395536dab1d71a47cfcb1d/onednn-c6b79c1.tar.gz
Source2:        https://github.com/openvinotoolkit/mlas/archive/d1bc25ec4660cddd87804fcf03b2411b5dfb2e94/mlas-d1bc25e.tar.gz
Source3:        https://github.com/oneapi-src/oneDNN/archive/929fe4e5629be2a5e89f1ba13b13458b965ffe57/onednn-gpu-929fe4e.tar.gz

Patch0: protobuf_version.patch
Patch1: xbyak-gflags-system-modules.patch
Patch2: samples-system-gflags-json.patch
# pybind11 3.x (Fedora > 44) forbids py::call_guard<> on the def_property
# family; older pybind11 needs the original variant.
%if 0%{?fedora} > 44
Patch3: pybind11-call_guard-compat-3x.patch
%else
Patch3: pybind11-call_guard-compat.patch
%endif

ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  flatbuffers-compiler
BuildRequires:  flatbuffers-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  glibc-devel
BuildRequires:  nlohmann-json-devel
BuildRequires:  onnx-devel
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig(OpenCL)
%if 0%{?fedora} > 44
BuildRequires:  protobuf3-devel
%else
BuildRequires:  protobuf-devel
%endif
BuildRequires:  pugixml-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  snappy-devel
BuildRequires:  tbb-devel
BuildRequires:  xbyak-devel
BuildRequires:  zlib-devel

Requires:       lib%{name}-ir-frontend = %{version}-%{release}
Requires:       lib%{name}-pytorch-frontend = %{version}-%{release}
Requires:       lib%{name}-onnx-frontend = %{version}-%{release}
Requires:       lib%{name}-paddle-frontend = %{version}-%{release}
Requires:       lib%{name}-tensorflow-frontend = %{version}-%{release}
Requires:       lib%{name}-tensorflow-lite-frontend = %{version}-%{release}
Recommends:     lib%{name}-auto-plugin = %{version}-%{release}
Recommends:     lib%{name}-auto-batch-plugin = %{version}-%{release}
Recommends:     lib%{name}-hetero-plugin = %{version}-%{release}
Recommends:     lib%{name}-intel-cpu-plugin = %{version}-%{release}
Recommends:     lib%{name}-intel-gpu-plugin = %{version}-%{release}

%description
%{desc}


%package -n lib%{name}-devel
Summary:        Development files for %{name}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < 2025.1.0-14
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       tbb-devel
%description -n lib%{name}-devel
%{desc}
.
This package provides the headers and libraries for developing applications
with OpenVINO.


## Plugins ##

%package -n lib%{name}-auto-plugin
Summary:        Auto / Multi software plugin for OpenVINO
%description -n lib%{name}-auto-plugin
%{desc}
.
This package provides the Auto / Multi software plugin for OpenVINO.


%package -n lib%{name}-auto-batch-plugin
Summary:        Automatic batch software plugin for OpenVINO
%description -n lib%{name}-auto-batch-plugin
%{desc}
.
This package provides the automatic batch software plugin for OpenVINO.


%package -n lib%{name}-hetero-plugin
Summary:        Hetero plugin for OpenVINO
%description -n lib%{name}-hetero-plugin
%{desc}
.
This package provides the hetero plugin for OpenVINO.


%package -n lib%{name}-intel-cpu-plugin
Summary:        Intel CPU plugin for OpenVINO
# Forked version of OpenVINO oneDNN does not have a proper version
Provides:       bundled(onednn)
# Intel MLAS
Provides:       bundled(mlas)
%description -n lib%{name}-intel-cpu-plugin
%{desc}
.
This package provides the Intel CPU plugin for OpenVINO.


%package -n lib%{name}-intel-gpu-plugin
Summary:        Intel GPU plugin for OpenVINO
# Forked version of oneapi-src/oneDNN used by the GPU plugin
Provides:       bundled(onednn-gpu)

%description -n lib%{name}-intel-gpu-plugin
%{desc}
.
This package provides the Intel GPU plugin for OpenVINO.


## Frontend shared libraries ##

%package -n lib%{name}-ir-frontend
Summary:        OpenVINO IR Frontend
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-ir-frontend
%{desc}
.
This package provides the IR frontend for OpenVINO.


%package -n lib%{name}-onnx-frontend
Summary:        OpenVINO ONNX Frontend
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-onnx-frontend
%{desc}
.
This package provides the ONNX frontend for OpenVINO.


%package -n lib%{name}-paddle-frontend
Summary:        OpenVINO Paddle Frontend
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-paddle-frontend
%{desc}
.
This package provides the Paddle frontend for OpenVINO.


%package -n lib%{name}-pytorch-frontend
Summary:        OpenVINO PyTorch Frontend
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-pytorch-frontend
%{desc}
.
This package provides the PyTorch frontend for OpenVINO.


%package -n lib%{name}-tensorflow-frontend
Summary:        OpenVINO TensorFlow Frontend
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-tensorflow-frontend
%{desc}
.
This package provides the TensorFlow frontend for OpenVINO.


%package -n lib%{name}-tensorflow-lite-frontend
Summary:        OpenVINO TensorFlow Lite Frontend
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-tensorflow-lite-frontend
%{desc}
.
This package provides the TensorFlow Lite frontend for OpenVINO.


## Samples ##

%package -n %{name}-samples
Summary:        C and C++ samples for OpenVINO
BuildArch:      noarch
Requires:       lib%{name}-devel = %{version}-%{release}
Requires:       cmake
Requires:       gcc-c++
Requires:       gcc
Requires:       glibc-devel
Requires:       make
Requires:       pkgconf-pkg-config
Suggests:       opencv-devel >= 3.0
Suggests:       ocl-icd-devel
Suggests:       opencl-headers
%description -n %{name}-samples
%{desc}
.
This package provides C and C++ source code samples demonstrating how to
use OpenVINO runtime and APIs.


%package -n python3-%{name}
Summary:        OpenVINO Python API
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-numpy
%description -n python3-%{name}
OpenVINO Python API allowing users to use the OpenVINO library in their Python
code. Python API provides bindings to basic and advanced APIs from OpenVINO
runtime.


%prep
%autosetup -p1

# Intel CPU plugin thirdparty deps
tar xf %{SOURCE1}
cp -r oneDNN-c6b79c1207bd5f20b9395536dab1d71a47cfcb1d/* src/plugins/intel_cpu/thirdparty/onednn

tar xf %{SOURCE2}
cp -r mlas-d1bc25ec4660cddd87804fcf03b2411b5dfb2e94/* src/plugins/intel_cpu/thirdparty/mlas

# Intel GPU plugin thirdparty deps
tar xf %{SOURCE3}
cp -r oneDNN-929fe4e5629be2a5e89f1ba13b13458b965ffe57/* src/plugins/intel_gpu/thirdparty/onednn_gpu

# Python bindings: remove openvino-telemetry (not in Fedora)
# It is present in both pyproject.toml (root) and src/bindings/python/requirements.txt
sed -i '/openvino-telemetry/d' pyproject.toml
sed -i '/openvino-telemetry/d' src/bindings/python/requirements.txt


%build
%cmake \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_POLICY_VERSION_MINIMUM="3.5.0" \
      -DCMAKE_CXX_FLAGS="%{optflags} -Wformat -Wformat-security -Wno-free-nonheap-object -Wno-array-bounds -Wno-stringop-overflow" \
      -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
      -DCMAKE_NO_SYSTEM_FROM_IMPORTED=ON \
      -DENABLE_CLANG_FORMAT=OFF \
      -DENABLE_PRECOMPILED_HEADERS=OFF \
      -DBUILD_SHARED_LIBS=ON \
      -DCPACK_GENERATOR=RPM \
      -DENABLE_OV_ONNX_FRONTEND=ON \
      -DENABLE_OV_PADDLE_FRONTEND=ON \
      -DENABLE_OV_PYTORCH_FRONTEND=ON \
      -DENABLE_OV_IR_FRONTEND=ON \
      -DENABLE_OV_TF_FRONTEND=ON \
      -DENABLE_OV_TF_LITE_FRONTEND=ON \
      -DENABLE_OV_JAX_FRONTEND=OFF \
      -DENABLE_INTEL_NPU=OFF \
      -DENABLE_TEMPLATE=OFF \
      -DENABLE_PROXY=OFF \
      -DENABLE_PYTHON=ON \
      -DPython3_EXECUTABLE=%{python3} \
      -DENABLE_WHEEL=OFF \
      -DENABLE_JS=OFF \
      -DENABLE_SAMPLES=ON \
      -DENABLE_TESTS=OFF \
      -DENABLE_PROFILING_ITT=OFF \
      -DENABLE_PKGCONFIG_GEN=ON \
      -DENABLE_SYSTEM_TBB=ON \
      -DENABLE_SYSTEM_OPENCL=ON \
      -DENABLE_SYSTEM_PUGIXML=ON \
      -DENABLE_SYSTEM_SNAPPY=ON \
      -DENABLE_SYSTEM_PROTOBUF=ON \
      -DProtobuf_USE_STATIC_LIBS=OFF \
      -DENABLE_SYSTEM_FLATBUFFERS=ON \
      -DTHREADING=TBB
%cmake_build


%install
%cmake_install

# Remove unnecessary files that may be installed
rm -rf %{buildroot}%{_prefix}/install_dependencies \
       %{buildroot}%{_prefix}/setupvars.sh
rm -rf %{buildroot}%{_datadir}/licenses/*
rm -rf %{buildroot}%{_datadir}/doc

# Install Python components directly (CPACK_GENERATOR=RPM marks them EXCLUDE_FROM_ALL
# for the default cmake install, but explicit --component bypasses that)
cmake --install %{__cmake_builddir} --prefix %{buildroot}%{_prefix} \
      --component pyopenvino_python%{python3_version}
cmake --install %{__cmake_builddir} --prefix %{buildroot}%{_prefix} \
      --component ovc
cmake --install %{__cmake_builddir} --prefix %{buildroot}%{_prefix} \
      --component benchmark_app

# Generate dist-info metadata (dist_info does not trigger cmake sub-builds)
WHEEL_VERSION=%{version} \
    %{python3} setup.py dist_info -o %{buildroot}%{python3_sitearch}

# Remove openvino-telemetry (not packaged in Fedora)
rm -rf %{buildroot}%{python3_sitearch}/openvino_telemetry*
rm -vf %{buildroot}%{python3_sitearch}/requirements.txt
rm -vf %{buildroot}%{python3_sitearch}/%{name}/preprocess/torchvision/requirements.txt


%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} PYTHONPATH=%{buildroot}%{python3_sitearch} \
    %{python3} samples/python/hello_query_device/hello_query_device.py
LD_LIBRARY_PATH=%{buildroot}%{_libdir} PYTHONPATH=%{buildroot}%{python3_sitearch} \
    %{python3} samples/python/model_creation_sample/model_creation_sample.py \
    samples/python/model_creation_sample/lenet.bin CPU


%ldconfig_scriptlets
%ldconfig_scriptlets -n lib%{name}-ir-frontend
%ldconfig_scriptlets -n lib%{name}-onnx-frontend
%ldconfig_scriptlets -n lib%{name}-paddle-frontend
%ldconfig_scriptlets -n lib%{name}-pytorch-frontend
%ldconfig_scriptlets -n lib%{name}-tensorflow-frontend
%ldconfig_scriptlets -n lib%{name}-tensorflow-lite-frontend


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{so_ver}
%{_libdir}/lib%{name}_c.so.%{version}
%{_libdir}/lib%{name}_c.so.%{so_ver}

%files -n lib%{name}-devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}%{version}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

## Plugins

%files -n lib%{name}-auto-plugin
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/lib%{name}_auto_plugin.so

%files -n lib%{name}-auto-batch-plugin
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/lib%{name}_auto_batch_plugin.so

%files -n lib%{name}-hetero-plugin
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/lib%{name}_hetero_plugin.so

%files -n lib%{name}-intel-cpu-plugin
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/lib%{name}_intel_cpu_plugin.so

%files -n lib%{name}-intel-gpu-plugin
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/lib%{name}_intel_gpu_plugin.so
%{_libdir}/%{name}-%{version}/cache.json

## Frontends

%files -n lib%{name}-ir-frontend
%{_libdir}/lib%{name}_ir_frontend.so.*

%files -n lib%{name}-onnx-frontend
%{_libdir}/lib%{name}_onnx_frontend.so.*

%files -n lib%{name}-paddle-frontend
%{_libdir}/lib%{name}_paddle_frontend.so.*

%files -n lib%{name}-pytorch-frontend
%{_libdir}/lib%{name}_pytorch_frontend.so.*

%files -n lib%{name}-tensorflow-frontend
%{_libdir}/lib%{name}_tensorflow_frontend.so.*

%files -n lib%{name}-tensorflow-lite-frontend
%{_libdir}/lib%{name}_tensorflow_lite_frontend.so.*

## Samples

%files -n %{name}-samples
%{_datadir}/openvino/samples/

%files -n python3-%{name}
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-%{version}.dist-info


%changelog
%autochangelog
