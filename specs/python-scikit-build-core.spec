%global debug_package %{nil}

Name:           python-scikit-build-core
Version:        0.11.0
Release:        %autorelease
Summary:        Build backend for CMake based projects

# The main project is licensed under Apache-2.0, but it has a vendored project
# src/scikit_build_core/_vendor/pyproject_metadata: MIT
# https://github.com/scikit-build/scikit-build-core/issues/933
License:        Apache-2.0 AND MIT
URL:            https://github.com/scikit-build/scikit-build-core
Source:         %{pypi_source scikit_build_core}

BuildRequires:  python3-devel
# Testing dependences
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git

%global _description %{expand:
A next generation Python CMake adapter and Python API for plugins
}

%description %_description

%package -n python3-scikit-build-core
Summary:        %{summary}
Requires:       cmake
Requires:       ninja-build
BuildArch:      noarch

Obsoletes:      python3-scikit-build-core+pyproject < 0.10.7-3

%description -n python3-scikit-build-core %_description


%prep
%autosetup -n scikit_build_core-%{version}
# Rename the bundled license so that it can be installed together
cp -p src/scikit_build_core/_vendor/pyproject_metadata/LICENSE LICENSE-pyproject-metadata
# Avoid cattrs test dependency -- some tests are skipped for that
# cattrs is not yet availbale for Python 3.14
# https://bugzilla.redhat.com/2343916
sed -i '/cattrs/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x test,test-meta,test-numpy


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files scikit_build_core


%check
%pyproject_check_import
%pytest \
    -m "not network" \
    --ignore tests/test_fileapi.py -k "not cattrs"


%files -n python3-scikit-build-core -f %{pyproject_files}
%license LICENSE LICENSE-pyproject-metadata
%doc README.md


%changelog
%autochangelog
