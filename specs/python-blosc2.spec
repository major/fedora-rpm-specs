Name:           python-blosc2
Version:        3.8.0
Release:        %autorelease
Summary:        Python wrapper for the Blosc2 compression library
License:        BSD-3-Clause
URL:            https://blosc.org/python-blosc2/python-blosc2.html
Source:         https://github.com/Blosc/python-blosc2/archive/v%{version}/python-blosc2-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-g++
BuildRequires:  blosc2-devel >= 2.21.0
BuildRequires:  tomcli

ExcludeArch:    %{ix86}

%global _description %{expand:
C-Blosc2 is the new major version of C-Blosc, and is backward compatible with
both the C-Blosc1 API and its in-memory format. Python-Blosc2 is a Python
package that wraps C-Blosc2, the newest version of the Blosc compressor.

In addition, Python-Blosc2 aims to leverage the new C-Blosc2 API so as to
support super-chunks, multi-dimensional arrays (NDArray), serialization and
other bells and whistles introduced in C-Blosc2. Although this is always and
endless process, it has already caught up with most of the C-Blosc2 API
capabilities.}

%description %_description

%package -n python3-blosc2
Summary:        %{summary}

%description -n python3-blosc2 %_description

%prep
%autosetup -p1
# Remove the numpy version constraint
tomcli set pyproject.toml lists replace "build-system.requires" "numpy.*" "numpy"
# Remove torch tests for now
tomcli set pyproject.toml lists delitem "project.optional-dependencies.test" "torch.*"

%generate_buildrequires
%pyproject_buildrequires -x test

%build
export USE_SYSTEM_BLOSC2=ON
export SKBUILD_CMAKE_BUILD_TYPE=RelWithDebInfo
export SKBUILD_BUILD_DIR=python-build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files blosc2

%check
OPTIONS=(
    --deselect=tests/test_embed_store.py::test_with_remote
)

%pytest tests/ "${OPTIONS[@]}" -v \
%ifarch s390x
  || :    # https://github.com/Blosc/python-blosc2/issues/125
%endif

%files -n python3-blosc2 -f %{pyproject_files}
%doc README.rst RELEASE_NOTES.md

%changelog
%autochangelog
