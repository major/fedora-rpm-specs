%global srcname extension-helpers
%global modname extension_helpers

%bcond_with doc

Name:           python-%{srcname}
Version:        1.1.1
Release:        %autorelease
Summary:        A build time package to simplify C/Cython extensions

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/extension-helpers
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  gcc

%global _description %{expand:
The extension-helpers package includes convenience helpers to assist with
building Python packages with compiled C/Cython extensions. It is developed
by the Astropy project but is intended to be general and usable by any
Python package.

This is not a traditional package in the sense that it is not intended to be
installed directly by users or developers. Instead, it is meant to be accessed
when the setup.py command is run and should be defined as a build-time
dependency in pyproject.toml files.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname} %_description


%if %{with doc}
%package doc
Summary:        Documentation for %{srcname}
BuildRequires:  python3dist(sphinx)

%description doc %_description
%endif

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test 

%build
%pyproject_wheel


%install
%pyproject_install

%if %{with doc}
pushd docs
PYTHONPATH=.. make html
rm -f _build/html/.buildinfo
popd
%endif

%pyproject_save_files %{modname}


%check
%pytest -q %{modname}/tests


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst licenses/LICENSE_ASTROSCRAPPY.rst
%doc README.rst

%if %{with doc}
%files doc
%license LICENSE.rst licenses/LICENSE_ASTROSCRAPPY.rst
%doc README.rst docs/_build/html
%endif

%changelog
%autochangelog
