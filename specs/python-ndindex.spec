Name:           python-ndindex
Version:        1.10.0
Release:        %autorelease
Summary:        Python library for manipulating indices of ndarrays
# Upstream specified license as MIT and this covers almost all source files.
# ndindex-1.7/ndindex/_crt.py is BSD-3-Clause
License:        MIT AND BSD-3-Clause
URL:            https://quansight-labs.github.io/ndindex/
Source:         https://github.com/quansight-labs/ndindex/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  gcc
BuildRequires:  gcc-g++
# For tests:
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-numpy
BuildRequires:  python3-sympy

ExcludeArch:    %{ix86}

%global _description %{expand:
ndindex is a library that allows representing and manipulating objects that can
be valid indices to numpy arrays, i.e., slices, integers, ellipses, None,
integer and boolean arrays, and tuples thereof.

The goals of the library are to provide a uniform API to manipulate these
objects, match semantics of numpy's ndarray, and to provide useful
transformation and manipulation functions on index objects.}

%description %_description

%package -n python3-ndindex
Summary:        %{summary}
Requires:       python3-numpy

%description -n python3-ndindex %_description

%prep
%autosetup -p1 -n ndindex-%{version}

# It wants to add coverage and flakes, which is not useful for us
rm pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l ndindex

%check
OPTIONS=(
  # These tests are flaky
  --deselect=ndindex/tests/test_shapetools.py::test_iter_indices_matmul
  --deselect=ndindex/tests/test_as_subindex.py::test_as_subindex_hypothesis
)

# Ugly hack to make the tests work.
# Upstream uses an editable build, which drops the .so files in the tree.
# The usual remedies like using `--import-mode=importlib` do not work.
pushd ndindex
ln -s %{buildroot}%{python3_sitearch}/ndindex/*.so .
popd
%pytest -v "${OPTIONS[@]}"

%files -n python3-ndindex -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
