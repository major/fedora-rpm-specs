Summary:    A cross-platform inferencing and training accelerator
Name:       onnxruntime
Version:    1.15.1
Release:    1%{?dist}
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

# MLAS is not implemented for s390x
# https://github.com/microsoft/onnxruntime/blob/master/cmake/onnxruntime_mlas.cmake#L222
# The memory exhausted when building for armv7hl
# safeint flatbuffers not available in i686
#     https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# aarch64 needs pytorch cpuinfo
#     https://bugzilla.redhat.com/show_bug.cgi?id=2181740
ExcludeArch:    s390x %{arm} %{ix86} aarch64

BuildRequires:  cmake >= 3.13
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	onnx-devel = 1.14.0
BuildRequires:  abseil-cpp-devel
BuildRequires:  boost-devel >= 1.66
BuildRequires:  bzip2
BuildRequires:  date-devel
BuildRequires:  flatbuffers-compiler
BuildRequires:  flatbuffers-devel
BuildRequires:  gmock-devel
BuildRequires:  gsl-devel
BuildRequires:  gtest-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  json-devel
BuildRequires:  protobuf-lite-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  re2-devel >= 20211101
BuildRequires:  safeint-devel
BuildRequires:  zlib-devel
Buildrequires:  eigen3-devel >= 1.34

%description
%{name} is a cross-platform inferencing and training accelerator compatible
with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras,
scikit-learn, and more.

%package devel
Summary:    The development part of the %{name} package
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
The development part of the %{name} package

%package doc
Summary:    Documentation files for the %{name} package

%description doc
Documentation files for the %{name} package

%prep
%autosetup -p1

%build
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
    -Donnxruntime_ENABLE_CPUINFO=OFF \
    -Donnxruntime_DISABLE_ABSEIL=ON \
    -Donnxruntime_ENABLE_CPUINFO=OFF \
    -Deigen_SOURCE_PATH=/usr/include/eigen3 \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -S cmake
%cmake_build

%install
%cmake_install
mkdir -p "%{buildroot}/%{_docdir}/"
cp --preserve=timestamps -r "./docs/" "%{buildroot}/%{_docdir}/%{name}"

%check
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

%files doc
%{_docdir}/%{name}

%changelog
* Wed Jul 26 2023 Alejandro Álvarez Ayllón <a.alvarezayllon@gmail.com> - 1.15.1-1
- Release 1.15.1

* Mon Jun 05 2023 Alejandro Álvarez Ayllón <a.alvarezayllon@gmail.com> - 1.15.0-1
- Release 1.15.0

* Wed Jan 05 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 1.10.0-1
- Release 1.10.0

* Wed Nov 03 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 1.9.1-1
- Release 1.9.1
