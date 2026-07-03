%global so_version 1

Name:       onnx
Version:    1.21.0
Release:    %autorelease
Summary:    Open standard for machine learning interoperability
License:    Apache-2.0

URL:        https://github.com/onnx/onnx
Source0:    https://github.com/onnx/onnx/archive/v%{version}/%{name}-%{version}.tar.gz
# Build shared libraries and fix install location 
Patch:     0001-Build-shared-libraries.patch
Patch:     0002-Fix-install-location.patch
# Latest nanobind uses different argument format
Patch:     0003-Fix-nanobind-arguments.patch
# Let pyproject_wheel use binaries from cmake_build
Patch:     0004-Let-pyproject_wheel-use-binaries-from-cmake_build.patch
# Fixes protobuf conflicts when using both python-onnx and python-onnxruntime
Patch:     0005-Python-binary-should-link-to-system-onnx.patch
# Remove obsoleted testing dependency
Patch:     0006-Remove-python-parameterized-dependency.patch
# Add fixes for use with onnxruntime
Patch:     0007-Add-fixes-for-use-with-onnxruntime.patch

%if %{undefined fc40} && %{undefined fc41}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

BuildRequires:  cmake >= 3.13
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pybind11
BuildRequires:  python3-pytest
BuildRequires:  python3-nanobind
BuildRequires:  python3-ml-dtypes 
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-static

%global _description %{expand:
%{name} provides an open source format for AI models, both deep learning and
traditional ML. It defines an extensible computation graph model, as well as
definitions of built-in operators and standard data types.}

%description %_description

%package libs
Summary:    Libraries for %{name}

%description libs %_description

%package devel
Summary:    Development files for %{name}
Requires:   %{name}-libs = %{version}-%{release}

%description devel %_description

%package -n python3-onnx
Summary:    %{summary}
Requires:   %{name}-libs = %{version}-%{release}

%description -n python3-onnx %_description

%prep
%autosetup -p1 -n onnx-%{version}

%generate_buildrequires
%pyproject_buildrequires requirements-reference.txt

%build
export VPATH_BUILDDIR=%{_vpath_builddir}
%cmake \
    -DONNX_USE_LITE_PROTO=OFF \
    -DONNX_USE_PROTOBUF_SHARED_LIBS=OFF \
    -DONNX_BUILD_PYTHON=ON \
    -DPython_EXECUTABLE=python3.14 \
    -DPY_EXT_SUFFIX=%{python3_ext_suffix} \
    -DPY_SITEARCH=%{python3_sitearch} \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DONNX_DISABLE_STATIC_REGISTRATION=OFF

# Build 
%cmake_build
# Build python libs
%pyproject_wheel

%install
%cmake_install
# Need to remove empty directories
find "%{buildroot}/%{_includedir}" -type d -empty -delete
find "%{buildroot}/%{python3_sitearch}" -type d -empty -delete
# Install *.proto files
install -p "./onnx/"*.proto -t "%{buildroot}/%{_includedir}/onnx/"

%pyproject_install
%pyproject_save_files onnx

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%ifarch riscv64
export PYTEST_ADDOPTS="-k 'not test_float8_e4m3fn_negative_nan and \
not test_float8_e5m2_negative_nan and not test_maxpool_2d_uint8_cpu'"
%endif
%ifarch s390x
export PYTEST_ADDOPTS="-k 'not test_make_tensor_raw'"
%endif

%pytest

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libonnx.so.%{so_version}{,.*}
%{_libdir}/libonnx_proto.so.%{so_version}{,.*}

%files devel
%{_libdir}/libonnx.so
%{_libdir}/libonnx_proto.so
%{_libdir}/cmake/ONNX
%{_includedir}/%{name}/

%files -n python3-onnx -f %{pyproject_files}
%{_bindir}/backend-test-tools
%{_bindir}/check-model
%{_bindir}/check-node

%changelog
%autochangelog
