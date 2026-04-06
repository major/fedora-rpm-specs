%global pypi_name django-formtools

# All the current tests are coverage and ruff
%global skip_tests 1

%global _description %{expand:
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.}


Name:           python-%{pypi_name}
Version:        2.5.1
Release:        %autorelease
Summary:        A set of high-level abstractions for Django forms

License:        BSD-3-Clause
URL:            http://django-formtools.readthedocs.org/en/latest/
Source0:        https://pypi.io/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# For docs
BuildRequires:  python3-sphinx


%description %_description


%package -n python3-%{pypi_name}
Summary:        A set of high-level abstractions for Django forms


%description -n python3-%{pypi_name} %_description


%package -n python3-%{pypi_name}-doc
Summary:        A set of high-level abstractions for Django forms - documentation
%{?python_provide:%python_provide python3-%{pypi_name}-doc}

Requires:       python3-%{pypi_name} = %{version}-%{release}


%description -n python3-%{pypi_name}-doc %_description

This is the associated documentation.


%prep
%autosetup -n %{pypi_name}-%{version}

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^isort[[:space:]]*[!><=]/d" \
    -e "/^ruff$/d" \
    tests/requirements.txt


%generate_buildrequires 
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l formtools


# generate html docs
# Fix doc build with latest Sphinx, see https://github.com/jazzband/django-formtools/issues/279
sed -i "s#'http://docs.python.org/': None#'python': ('https://docs.python.org/3', None)#" docs/conf.py
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%check
%pyproject_check_import formtools

# All tests are coverage and ruff.
%if 0%{?skip_tests} == 0
%tox
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%exclude %{python3_sitelib}/tests


%files -n python3-%{pypi_name}-doc
%doc html
%license LICENSE


%changelog
%autochangelog
