%global srcname extension_helpers
%global pkgname extension-helpers

%bcond_with doc

Name:           python-extension-helpers
Version:        1.4.0
Release:        %autorelease
Summary:        A build time package to simplify C/Cython extensions

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/extension-helpers
Source0:        %{pypi_source %srcname}

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

%package -n python3-%{pkgname}
Summary: %{summary}

# Fix for an accidental name change
# The Obsoletes can be removed when Rawhide is F44
Obsoletes: python3-extension_helpers < 1.2.0-2


%description -n python3-%{pkgname} %_description


%if %{with doc}
%package doc
Summary:        Documentation for %{pkgname}
BuildRequires:  python3dist(sphinx)

%description doc %_description
%endif

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e 's|312|312,313|' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t -x test 

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

%pyproject_save_files %{srcname}


%check
%tox

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE.rst licenses/LICENSE_ASTROSCRAPPY.rst
%doc README.rst

%if %{with doc}
%files doc
%license LICENSE.rst licenses/LICENSE_ASTROSCRAPPY.rst
%doc README.rst docs/_build/html
%endif

%changelog
%autochangelog
