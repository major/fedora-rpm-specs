%global pypi_name coremltools
# Currrently fails due to some missing py deps and ML stacks (tensorflow, CUDA)
# Also has a u/s bug when run on python RCs: https://github.com/apple/coremltools/issues/2874
%define with_tests 0

Name:          python-%{pypi_name}
Version:       9.0
Release:       3%{?dist}
Summary:       Tools for Core ML model conversion, editing, and validation
License:       BSD-3-Clause
URL:           https://github.com/apple/%{pypi_name}
Source0:       %url/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
Patch0:        coremltools-9.0-fix-python-rc-version.patch
# Build against the system protobuf, pybind11, nlohmann_json and FP16
Patch1:        coremltools-9.0-system-deps.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: protobuf3-compiler
BuildRequires: protobuf3-devel
BuildRequires: pybind11-devel
BuildRequires: json-devel
BuildRequires: FP16-devel
BuildRequires: libuuid-devel
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
# For check
%if 0%{?with_tests}
BuildRequires: python3-pandas
BuildRequires: python3-pytest
BuildRequires: python3-pillow
BuildRequires: python3-requests
BuildRequires: python3-scipy
BuildRequires: python3-torch
BuildRequires: python3-torchvision
%endif

%global _description %{expand:
Use Core ML Tools (coremltools) to convert machine learning models from
third-party libraries to the Core ML format. This Python package contains
the supporting tools for converting models from training libraries such
as the following:

* TensorFlow 1.x
* TensorFlow 2.x
* PyTorch
* Non-neural network frameworks:
  scikit-learn
  XGBoost
  LibSVM

With coremltools, you can:

* Convert trained models to the Core ML format.
* Read, write, and optimize Core ML models.
* Verify conversion/creation (on macOS) by making predictions using Core ML.

After conversion, you can integrate the Core ML models with your app using
Xcode.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf deps/

# Remove pre-generated protobuf C++ sources/headers and enum headers.
rm -f mlmodel/build/format/*.pb.cc mlmodel/build/format/*.pb.h \
      mlmodel/build/format/*_enums.h

# Pre-generated python protobuf modules, regenerate with the system protoc.
protoc --python_out=coremltools/proto -I mlmodel/format mlmodel/format/*.proto
# Use sed as lib2to3 is retired from python
sed -i -E 's/^import ([A-Za-z0-9]+_pb2) as/from . import \1 as/;
           s/^from ([A-Za-z0-9]+_pb2) import/from .\1 import/' \
    coremltools/proto/*_pb2.py

%generate_buildrequires
%if 0%{?with_tests}
%pyproject_buildrequires -r
%else
%pyproject_buildrequires
%endif

%build
# The build copies them into coremltools/ in the source treer
# where setup.py picks them up when building the wheel.
%cmake
%cmake_build --target modelpackage milstoragepython

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if 0%{?with_tests}
%check
%pyproject_check_import -e 'coremltools.converters.mil.frontend.tensorflow*' \
                        -e 'coremltools.converters.mil.frontend.tf*' \
                        -e 'coremltools.converters.mil.frontend.torch.test.test_torch_export_conversion_api' \
                        -e 'coremltools.converters.mil.frontend.torch.test.test_torch_conversion_api'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
* Mon Sep 28 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 9.0-3
- Build binary bits using system libraries
- Regenerate the protobuf C++ and python sources, and the enum headers

* Fri Sep 25 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 9.0-2
- Add option to run tests, explicitly remove unused deps directory

* Wed Sep 23 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 9.0-1
- Initial package
