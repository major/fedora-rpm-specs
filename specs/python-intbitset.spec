%global pypi_name intbitset

Name:           python-%{pypi_name}
Version:        4.1.0
Release:        %autorelease
Summary:        Python C-based extension implementing fast integer bit sets

License:        LGPL-3.0-or-later
URL:            https://github.com/inveniosoftware-contrib/intbitset
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  Cython
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%global common_description %{expand:
The intbitset library provides a set implementation to store sorted unsigned
integers either 32-bits integers (between 0 and 2**31 - 1 or
intbitset.__maxelem__) or an infinite range with fast set operations implemented
via bit vectors in a Python C extension for speed and reduced memory usage.

The inbitset class emulates the Python built-in set class interface with some
additional specific methods such as its own fast dump and load marshalling
functions.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        LGPL-3.0-or-later AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rfv src/intbitset.c

%generate_buildrequires
%pyproject_buildrequires

%build
cython intbitset/intbitset.pyx
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/ html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -k 'not test_set_consistency'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%pycached %{python3_sitearch}/intbitset_*.py

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
