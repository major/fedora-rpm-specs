%global utf8_range_commit 72c943dea2b9240cd09efde15191e144bc7c7d38
%global utf8_range_name utf8_range-%( echo %utf8_range_commit | cut -c1-7 )

%if 0%{?fedora} && ! 0%{?flatpak}
%ifarch x86_64
%bcond rocm 1
%else
%bcond rocm 0
%endif
%else
%bcond rocm 0
%endif

%bcond rocm_test 0
%bcond test 1

# $backend will be evaluated below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${backend}
%global backends cpu
%if %{with rocm}
%global backends %backends rocm
%endif

Summary:    A cross-platform inferencing and training accelerator
Name:       onnxruntime
Version:    1.20.1
Release:    %autorelease
# onnxruntime and SafeInt are MIT
# onnx is Apache License 2.0
# optional-lite is Boost Software License 1.0
# some protobuf helper files files are BSD (protobuf_function.cmake, pb_helper.*)
License:    MIT and ASL 2.0 and Boost and BSD
URL:        https://github.com/microsoft/onnxruntime
Source0:    https://github.com/microsoft/onnxruntime/archive/v%{version}/%{name}-%{version}.tar.gz
# Bundled utf8_range until they get propperly exposed from the protobuff package
Source1:    https://github.com/protocolbuffers/utf8_range/archive/%{utf8_range_commit}/%{utf8_range_name}.zip

# Add an option to not install the tests
Patch:      0000-dont-install-tests.patch
# Use the system flatbuffers
Patch:      0001-system-flatbuffers.patch
# Use the system protobuf
Patch:      0002-system-protobuf.patch
# Use the system onnx
Patch:      0003-system-onnx.patch
# Fedora targets power8 or higher
Patch:      0004-disable-power10.patch
# Do not use nsync
Patch:      0005-no-nsync.patch
# Do not link against WIL
Patch:      0006-remove-wil.patch
# Use the system safeint
Patch:      0007-system-safeint.patch
# Versioned libonnxruntime_providers_shared.so
Patch:      0008-versioned-onnxruntime_providers_shared.patch
# Disable gcc -Werrors with false positives
Patch:      0009-gcc-false-positive.patch
# Test data not available 
Patch:      0010-disable-pytorch-tests.patch
# Use the system date and boost
Patch:      0011-system-date-and-mp11.patch
# Use the system cpuinfo
Patch:      0012-system-cpuinfo.patch
# Trigger onnx fix for onnxruntime_providers_shared
Patch:      0013-onnx-onnxruntime-fix.patch
# Use the system python version
Patch:      0014-system-python.patch
# Fix errors when DISABLE_ABSEIL=ON
Patch:      0015-abseil-disabled-fix.patch
# Fix missing includes
Patch:      0016-missing-cpp-headers.patch
# Revert https://github.com/microsoft/onnxruntime/pull/21492 until
# Fedora's Eigen3 is compatible with the fix.
Patch:      0017-revert-nan-propagation-bugfix.patch
# Backport upstream implementation of onnx
# from https://github.com/microsoft/onnxruntime/pull/21897
Patch:      0019-backport-onnx-1.17.0-support.patch
Patch:      0020-disable-locale-tests.patch
Patch:      0021-fix-range-loop-construct.patch
Patch:      0022-onnxruntime-convert-gsl-byte-to-std-byte.patch
# [Build] Fails to build with abseil-cpp 20250814
# https://github.com/microsoft/onnxruntime/issues/25815
# Patch suggested in a comment in the above issue.
Patch:      abseil-cpp-20250814.patch
# Build fails on ROCm 7
Patch:     0001-onnxruntime-warpSize-is-not-constant-in-ROCm-7.patch
Patch:     0001-onnxruntime-ignore-deprecated-thrust-warnings.patch

# s390x:   https://bugzilla.redhat.com/show_bug.cgi?id=2235326
# armv7hl: https://bugzilla.redhat.com/show_bug.cgi?id=2235328
# i686:    https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    s390x %{arm} %{ix86}

BuildRequires:  cmake >= 3.13
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	onnx-devel = 1.17.0
BuildRequires:  abseil-cpp-devel
BuildRequires:  boost-devel >= 1.66
BuildRequires:  bzip2
%ifnarch ppc64le
BuildRequires:  cpuinfo-devel
%endif
BuildRequires:  date-devel
BuildRequires:  flatbuffers-compiler
BuildRequires:  flatbuffers-devel >= 23.5.26
BuildRequires:  gmock-devel
BuildRequires:  gsl-devel
BuildRequires:  gtest-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  json-devel
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  re2-devel >= 20211101
BuildRequires:  safeint-devel
BuildRequires:  zlib-devel
Buildrequires:  eigen3-devel >= 1.34
BuildRequires:  pybind11-devel

%if %{with rocm}
BuildRequires:  hipcc
BuildRequires:  hipify
BuildRequires:  hipblas-devel
BuildRequires:  hipcub-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsparse-devel
BuildRequires:  miopen-devel
BuildRequires:  rccl-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-clang
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-smi-devel
BuildRequires:  rocthrust-devel
BuildRequires:  roctracer-devel
%endif

Provides:       bundled(utf8_range)

%description
%{name} is a cross-platform inferencing and training accelerator compatible
with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras,
scikit-learn, and more.

%package devel
Summary:    The development part of the %{name} package
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
The development part of the %{name} package

%if %{with rocm}
%package rocm
Summary:    The ROCm runtime backend for the %{name} package

%description rocm
%{summary}

%package rocm-devel
Summary:    The ROCm development part of the %{name} package
Requires:   %{name}-rocm%{_isa} = %{version}-%{release}

%description rocm-devel
%{summary}

%package rocm-test
Summary:    The ROCm tests for the %{name} package
Requires:   %{name}-rocm%{_isa} = %{version}-%{release}

%description rocm-test
%{summary}
%endif

%package -n python3-onnxruntime
Summary:    %{summary}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description -n python3-onnxruntime
Python bindings for the %{name} package

%package doc
Summary:    Documentation files for the %{name} package

%description doc
Documentation files for the %{name} package

%if %{with rocm}
%endif

%prep

%autosetup -p1
# Downstream-only: do not pin the version of abseil-cpp; use what we have.
sed -r -i 's/(FIND_PACKAGE_ARGS[[:blank:]]+)[0-9]{8}/\1/' \
    cmake/external/abseil-cpp.cmake

for backend in %backends; do
  mkdir -p ./%{_vpath_builddir}/_deps/utf8_range-subbuild/utf8_range-populate-prefix/src/
  cp -r %{SOURCE1} ./%{_vpath_builddir}/_deps/utf8_range-subbuild/utf8_range-populate-prefix/src/%{utf8_range_commit}.zip
done

%build
# Broken test in aarch64
%ifarch aarch64
rm -v onnxruntime/test/optimizer/nhwc_transformer_test.cc
%endif

# Re-compile flatbuffers schemas with the system flatc
%{python3} onnxruntime/core/flatbuffers/schema/compile_schema.py --flatc /usr/bin/flatc
%{python3} onnxruntime/lora/adapter_format/compile_schema.py --flatc /usr/bin/flatc

# -Werror is too strict and brittle for distribution packaging.
CXXFLAGS+="-Wno-error"

# Overrides BUILD_SHARED_LIBS flag since onnxruntime compiles individual components as static, and links
# all together into a single shared library when onnxruntime_BUILD_SHARED_LIB is ON.
# The array-bounds and dangling-reference checks have false positives.
%global cmake_config \\\
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
 -Donnxruntime_BUILD_BENCHMARKS=OFF \\\
 -Donnxruntime_BUILD_SHARED_LIB=ON \\\
 -Donnxruntime_BUILD_UNIT_TESTS=ON \\\
 -Donnxruntime_ENABLE_PYTHON=ON \\\
 -DPYTHON_VERSION=%{python3_version} \\\
 -Donnxruntime_DISABLE_ABSEIL=ON \\\
 -Donnxruntime_USE_FULL_PROTOBUF=ON \\\
 -Donnxruntime_USE_NEURAL_SPEED=OFF \\\
 -Donnxruntime_USE_PREINSTALLED_EIGEN=ON \\\
 -Deigen_SOURCE_PATH=/usr/include/eigen3 \\\
 -S cmake \\\

%if %{with rocm}
backend=rocm
%cmake %cmake_config \
    -DCMAKE_INSTALL_BINDIR=%{_lib}/rocm/bin \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_lib}/rocm/include \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}/rocm/lib \
    -Donnxruntime_ENABLE_CPUINFO=ON \
    -DCMAKE_HIP_ARCHITECTURES=%rocm_gpu_list_default \
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_HIP_PLATFORM=amd \
%if %{with rocm_test}
    -Donnxruntime_INSTALL_UNIT_TESTS=ON \
%else
    -Donnxruntime_INSTALL_UNIT_TESTS=OFF \
%endif
    -Donnxruntime_ROCM_HOME=%{_prefix} \
    -Donnxruntime_USE_COMPOSABLE_KERNEL=OFF \
    -Donnxruntime_USE_ROCM=ON

%cmake_build
%endif

backend=cpu
%cmake %cmake_config \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_INSTALL_INCLUDEDIR=include \
%ifarch ppc64le
    -Donnxruntime_ENABLE_CPUINFO=OFF \
%else
    -Donnxruntime_ENABLE_CPUINFO=ON \
%endif
    -Donnxruntime_INSTALL_UNIT_TESTS=OFF

%cmake_build

# Build python libs
mv ./onnxruntime ./onnxruntime.src
cp -R ./%{__cmake_builddir}/onnxruntime ./onnxruntime
cp ./%{__cmake_builddir}/requirements.txt ./requirements.txt
%pyproject_wheel

%install
%if %{with rocm}
backend=rocm
%cmake_install
%endif

backend=cpu
%cmake_install
mkdir -p "%{buildroot}/%{_docdir}/"
cp --preserve=timestamps -r "./docs/" "%{buildroot}/%{_docdir}/%{name}"

%pyproject_install
%pyproject_save_files onnxruntime

ln -s "../../../../libonnxruntime_providers_shared.so.%{version}" "%{buildroot}/%{python3_sitearch}/onnxruntime/capi/libonnxruntime_providers_shared.so"

%if %{with test}
%check

%if %{with rocm_test}
backend=rocm
export GTEST_FILTER=-CApiTensorTest.load_huge_tensor_with_external_data
%ctest
%else
backend=cpu
export GTEST_FILTER=-CApiTensorTest.load_huge_tensor_with_external_data
%ctest
%endif

%endif

%files
%license LICENSE
%doc ThirdPartyNotices.txt
%{_libdir}/libonnxruntime.so.%{version}
%{_libdir}/libonnxruntime_providers_shared.so.%{version}

%files devel
%dir %{_includedir}/onnxruntime/
%{_includedir}/onnxruntime/*
%{_libdir}/libonnxruntime.so*
%{_libdir}/libonnxruntime_providers_shared.so
%{_libdir}/pkgconfig/libonnxruntime.pc
%{_libdir}/cmake/onnxruntime/*

%files -n python3-onnxruntime -f %{pyproject_files}
%{_bindir}/onnxruntime_test
%{python3_sitearch}/onnxruntime/capi/libonnxruntime_providers_shared.so

%files doc
%{_docdir}/%{name}

%if %{with rocm}
%files rocm
%license LICENSE
%doc ThirdPartyNotices.txt
%{_libdir}/rocm/lib/libonnxruntime.so.%{version}
%{_libdir}/rocm/lib/libonnxruntime_providers_shared.so.%{version}
%{_libdir}/rocm/lib/libonnxruntime_providers_rocm.so

%files rocm-devel
%dir %{_libdir}/rocm/include/onnxruntime/
%dir %{_libdir}/rocm/lib/cmake/onnxruntime/
%{_libdir}/rocm/include/onnxruntime/*
%{_libdir}/rocm/lib/libonnxruntime.so*
%{_libdir}/rocm/lib/libonnxruntime_providers_shared.so
%{_libdir}/rocm/lib/pkgconfig/libonnxruntime.pc
%{_libdir}/rocm/lib/cmake/onnxruntime/*

%if %{with rocm_test}
%files rocm-test
%{_libdir}/rocm/bin/*
%endif
%endif

%changelog
%autochangelog

