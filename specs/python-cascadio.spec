%bcond bootstrap 0
# Break a test-dependency loop between this package and python-trimesh.
%bcond tests %{without bootstrap}

Name:           python-cascadio
Version:        0.0.16
Release:        %autorelease
Summary:        Convert STEP files to GLB using OpenCASCADE

License:        MIT
URL:            https://github.com/mikedh/cascadio
# The PyPI project does not have sdists, so we must use the GitHub archive.
Source:         %{url}/archive/%{version}/cascadio-%{version}.tar.gz

# Tests for cascadio fail on s390x, wrong endianness
# https://github.com/mikedh/trimesh/issues/2251
# https://bugzilla.redhat.com/show_bug.cgi?id=2298452
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86} s390x

BuildRequires:  python3-devel

BuildRequires:  gcc-c++
BuildRequires:  ninja-build

BuildRequires:  cmake(OpenCASCADE)
# RapidJSON headers are included indirectly via
# opencascade/RWGltf_CafWriter.hxx, so the header-only library is compiled into
# this extension and should technically be tracked even though it is an
# indirect dependency.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  rapidjson-static

%global common_description %{expand:
A Python library which uses OpenCASCADE to convert STEP files to a GLB file
which can quickly be loaded by trimesh and other libraries.

This is not intended to be a full binding of OpenCASCADE like OCP or PythonOCC.
Rather it is intended to be an easy minimal way to load boundary representation
files into a triangulated scene in Python. There are a few options for loading
STEP geometry in the open-source ecosystem: GMSH, FreeCAD, etc. However nearly
all of them use OpenCASCADE under the hood as it is pretty much the only
open-source BREP kernel.}

%description %{common_description}


%package -n python3-cascadio
Summary:        %{summary}

%description -n python3-cascadio %{common_description}


%prep
%autosetup -n cascadio-%{version} -p1
# The CMake scripts shipped with the system VTK try to find HDF5 by compiling
# and linking a C program; we need to enable the C language in the top-level
# project in order for this to work.
sed -r -i 's/\bCXX\b/C &/' CMakeLists.txt


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}


%build
# https://scikit-build-core.readthedocs.io/en/latest/configuration.html
%{pyproject_wheel \
    -Ccmake.define.SYSTEM_OPENCASCADE=ON \
    -Clogging.level=INFO \
    -Ccmake.verbose=true \
    -Ccmake.build-type="RelWithDebInfo" \
    -Cinstall.strip=false}


%install
%pyproject_install
%pyproject_save_files -L cascadio


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-cascadio -f %{pyproject_files}
# We include only the license for the actual package, omitting
# LICENSE/LICENSE-opencascade.md (for the opencascade library that is bundled
# in PyPI wheels) and LICENSE/README.md (which explains the difference).
%license LICENSE/LICENSE-cascadio.md
%doc README.md


%changelog
%autochangelog
