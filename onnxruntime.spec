Summary:    A cross-platform inferencing and training accelerator
Name:       onnxruntime
Version:    1.15.1
Release:    7%{?dist}
# onnxruntime and SafeInt are MIT
# onnx is Apache License 2.0
# optional-lite is Boost Software License 1.0
# some protobuf helper files files are BSD (protobuf_function.cmake, pb_helper.*)
License:    MIT and ASL 2.0 and Boost and BSD
URL:        https://github.com/microsoft/onnxruntime
Source0:    https://github.com/microsoft/onnxruntime/archive/v%{version}/%{name}-%{version}.tar.gz

# Add an option to not install the tests
Patch0:     dont-install-tests.patch
# Use the system flatbuffers
Patch1:	    system-flatbuffers.patch
# Use the system protobuf
Patch2:     system-protobuf.patch
# Use the system onnx
Patch3:     system-onnx.patch
# Fedora targets power8 or higher
Patch4:     disable-power10.patch
# Do not use nsync
Patch5:     no-nsync.patch
# Do not link against WIL
Patch6:     remove-wil.patch
# Use the system safeint
Patch7:     system-safeint.patch
# Versioned libonnxruntime_providers_shared.so
Patch8:     versioned-onnxruntime_providers_shared.patch
# Disable gcc -Werrors with false positives
Patch9:     gcc-false-positive.patch
# Test data not available 
Patch10:    disable-pytorch-tests.patch
# Use the system date and boost
Patch11:    system-date-and-mp11.patch
# Remove broken forward declarations and include flatbuffers instead
Patch12:    fix_forward_decl_flatbuffers.patch
# Use the system cpuinfo
Patch13:    system-cpuinfo.patch
# Trigger onnx fix for onnxruntime_providers_shared
Patch14:    onnx_onnxruntime_fix.patch
# Use the system python version
Patch15:    system-python.patch

# s390x:   https://bugzilla.redhat.com/show_bug.cgi?id=2235326
# armv7hl: https://bugzilla.redhat.com/show_bug.cgi?id=2235328
# i686:    https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    s390x %{arm} %{ix86}

BuildRequires:  cmake >= 3.13
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	onnx-devel = 1.14.0
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

%description
%{name} is a cross-platform inferencing and training accelerator compatible
with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras,
scikit-learn, and more.

%package devel
Summary:    The development part of the %{name} package
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
The development part of the %{name} package

%package -n python3-onnxruntime
Summary:    %{summary}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description -n python3-onnxruntime
Python bindings for the %{name} package

%package doc
Summary:    Documentation files for the %{name} package

%description doc
Documentation files for the %{name} package

%prep
%autosetup -p1

%build
# Broken test in aarch64
%ifarch aarch64
rm -v onnxruntime/test/optimizer/nhwc_transformer_test.cc
%endif

# Re-generate flatbuffer headers
%{__python3} onnxruntime/core/flatbuffers/schema/compile_schema.py --flatc %{_bindir}/flatc

# Overrides BUILD_SHARED_LIBS flag since onnxruntime compiles individual components as static, and links
# all together into a single shared library when onnxruntime_BUILD_SHARED_LIB is ON.
# The array-bounds and dangling-reference checks have false positives.
%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
    -Donnxruntime_BUILD_SHARED_LIB=ON \
    -Donnxruntime_BUILD_UNIT_TESTS=ON \
    -Donnxruntime_INSTALL_UNIT_TESTS=OFF \
    -Donnxruntime_BUILD_BENCHMARKS=OFF \
    -Donnxruntime_USE_PREINSTALLED_EIGEN=ON \
    -Donnxruntime_USE_FULL_PROTOBUF=ON \
    -DPYTHON_VERSION=%{python3_version} \
%ifarch ppc64le
    -Donnxruntime_ENABLE_CPUINFO=OFF \
%else
    -Donnxruntime_ENABLE_CPUINFO=ON \
%endif
    -Donnxruntime_DISABLE_ABSEIL=ON \
    -Donnxruntime_ENABLE_PYTHON=ON \
    -Deigen_SOURCE_PATH=/usr/include/eigen3 \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -S cmake
%cmake_build

# Build python libs
mv ./onnxruntime ./onnxruntime.src
cp -R ./%{__cmake_builddir}/onnxruntime ./onnxruntime
cp ./%{__cmake_builddir}/requirements.txt ./requirements.txt
%pyproject_wheel

%install
%cmake_install
mkdir -p "%{buildroot}/%{_docdir}/"
cp --preserve=timestamps -r "./docs/" "%{buildroot}/%{_docdir}/%{name}"

%pyproject_install
%pyproject_save_files onnxruntime

%check
export GTEST_FILTER=-CApiTensorTest.load_huge_tensor_with_external_data
%ctest

%files
%license LICENSE
%doc ThirdPartyNotices.txt
%{_libdir}/libonnxruntime.so.%{version}
%{_libdir}/libonnxruntime_providers_shared.so.%{version}

%files devel
%dir %{_includedir}/onnxruntime/
%{_includedir}/onnxruntime/*
%{_libdir}/libonnxruntime.so
%{_libdir}/libonnxruntime_providers_shared.so
%{_libdir}/pkgconfig/libonnxruntime.pc

%files -n python3-onnxruntime -f %{pyproject_files}
%{_bindir}/onnxruntime_test

%files doc
%{_docdir}/%{name}

%changelog
* Wed Jan 24 2024 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 1.15.1-7
- Build using protobuf-devel

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 31 2023 Diego Herrera <dherrera@redhat.com> - 1.15.1-5
- Trigger onnx fix for onnxruntime

* Wed Aug 30 2023 Diego Herrera <dherrera@redhat.com> - 1.15.1-4
- Fix python package build dependencies

* Tue Aug 22 2023 Diego Herrera <dherrera@redhat.com> - 1.15.1-3
- Add python library package

* Thu Aug 17 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 1.15.1-2
- Enable build on aarch64

* Wed Jul 26 2023 Alejandro Álvarez Ayllón <a.alvarezayllon@gmail.com> - 1.15.1-1
- Release 1.15.1

* Mon Jun 05 2023 Alejandro Álvarez Ayllón <a.alvarezayllon@gmail.com> - 1.15.0-1
- Release 1.15.0

* Wed Jan 05 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 1.10.0-1
- Release 1.10.0

* Wed Nov 03 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 1.9.1-1
- Release 1.9.1
