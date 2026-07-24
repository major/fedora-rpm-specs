Name:           python-numpy-stl
Version:        4.0.0
Release:        %autorelease
Summary:        Library for reading, writing and modifying STL files

License:        BSD-3-Clause
URL:            https://github.com/WoLpH/numpy-stl/
Source:         https://github.com/WoLpH/numpy-stl/archive/refs/tags/v%{version}.tar.gz#/numpy_stl-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-furo
BuildRequires:  python3-PyQt5
BuildRequires:  /usr/bin/xvfb-run

%description
Simple library to make working with STL files (and 3D objects in general) fast
and easy. Due to all operations heavily relying on numpy this is one of the
fastest STL editing libraries for Python available.

%package -n     python3-numpy-stl
Summary:        %{summary}

%description -n python3-numpy-stl
Simple library to make working with STL files (and 3D objects in general) fast
and easy. Due to all operations heavily relying on NumPy this is one of the
fastest STL editing libraries for Python available.

%package        doc
Summary:        %{name} documentation
Suggests:       python3-numpy-stl
BuildArch:      noarch
%description doc
Documentation for %{name}.

%prep
%autosetup -n numpy-stl-%{version} -p1
# Drop all coverage options from pytest invocation
sed -i '/-cov[-=]/d' pyproject.toml
# We must work with what we have, and compatibility is quite good in practice.
%pyproject_patch_dependency uv_build:drop_upper

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=. sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files --assert-license stl

%check
%pytest -v


%files -n python3-numpy-stl -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_bindir}/stl
%{_bindir}/stl2bin
%{_bindir}/stl2ascii

%files doc
%doc html

%changelog
%autochangelog
