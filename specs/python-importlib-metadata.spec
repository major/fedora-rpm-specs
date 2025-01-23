Name:           python-importlib-metadata
Version:        8.6.1
Release:        %autorelease
Summary:        Library to access the metadata for a Python package

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://importlib-metadata.readthedocs.io/
Source0:        %{pypi_source importlib_metadata}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# Test dependencies
# Not loaded via %%pyproject_buildrequires -x testing because upstream
# uses a lot unnecessary packages and some of them are not in Fedora.
BuildRequires:  python3-test
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyfakefs)
BuildRequires:  python3dist(jaraco-test)

%description
Library to access the metadata for a Python package.
This package supplies third-party access to the functionality
of importlib.metadata including improvements added to subsequent
Python versions.


%package -n     python3-importlib-metadata
Summary:        %{summary}

%description -n python3-importlib-metadata
Library to access the metadata for a Python package.
This package supplies third-party access to the functionality
of importlib.metadata including improvements added to subsequent
Python versions.


%prep
%autosetup -n importlib_metadata-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files importlib_metadata

%check
# Ignored file uses pytest_perf not available in Fedora
# test_find_local tries to install setuptools from PyPI
%pytest --ignore exercises.py -k "not test_find_local"

%files -n python3-importlib-metadata -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
