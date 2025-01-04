Name:           python-numpy-stl
Version:        3.2.0
Release:        %autorelease
Summary:        Library for reading, writing and modifying STL files

License:        BSD-3-Clause
URL:            https://github.com/WoLpH/numpy-stl/
Source:         %{pypi_source numpy_stl}

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx

%ifnarch armv7hl
# the test is optional based on the presence of PyQt5
# xvfb somehow fails on this arch
BuildRequires:  python3-PyQt5
BuildRequires:  /usr/bin/xvfb-run
%endif

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
%autosetup -n numpy_stl-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files stl

%check
%pytest -v


%files -n python3-numpy-stl -f %{pyproject_files}
%doc README.rst
%{_bindir}/stl
%{_bindir}/stl2bin
%{_bindir}/stl2ascii

%files doc
%doc html

%changelog
%autochangelog
