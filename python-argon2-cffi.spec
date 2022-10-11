%global pypi_name argon2-cffi

Name:           python-%{pypi_name}
Version:        21.1.0
Release:        %autorelease
Summary:        The secure Argon2 password hashing algorithm

License:        MIT
URL:            https://argon2-cffi.readthedocs.io/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel >= 3.5

BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(wheel)

BuildRequires:  pkgconfig(libargon2)

%global _description %{expand:
CFFI-based Argon2 Bindings for Python.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description


%package     -n python-%{pypi_name}-doc
Summary:        Documentation for argon2-cffi
BuildRequires:  python3dist(argon2-cffi)

%description -n python-%{pypi_name}-doc
Documentation for argon2-cffi.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# using system libargon
rm -r   extras/libargon2/LICENSE \
        extras/libargon2/README.md \
        docs/license.rst

# Theme error:
# no theme named 'furo' found (missing theme.conf?)
sed -i '/html_theme = "furo"/d' \
    docs/conf.py


%build
export ARGON2_CFFI_USE_SYSTEM=1
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
%pytest


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/argon2/
%{python3_sitearch}/argon2_cffi-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html


%changelog
%autochangelog
