# There is circular dependency with this requiring stestr requiring cliff requiring stevedore
%bcond_with bootstrap

%global modname cliff

%global common_desc %{expand:
cliff is a framework for building command line programs. It uses setuptools
entry points to provide subcommands, output formatters, and other
extensions.

Documentation for cliff is hosted on readthedocs.org at
http://readthedocs.org/docs/cliff/en/latest/}

%global common_desc_tests This package contains tests for the python cliff library.

Name:             python-%{modname}
Version:          4.13.3
Release:          %autorelease
Summary:          Command Line Interface Formulation Framework

Group:            Development/Libraries
License:          Apache-2.0
URL:              https://pypi.io/pypi/cliff
Source0:          %pypi_source cliff

BuildArch:        noarch
BuildRequires:    python3-devel

%package -n python3-%{modname}
Summary:          Command Line Interface Formulation Framework


%description -n python3-%{modname}
%{common_desc}

%package -n python3-%{modname}-tests
Summary:          Command Line Interface Formulation Framework

BuildRequires:    bash
BuildRequires:    which
# cliff imports docutils in code which is not in requirements.txt and it is
# needed to run tests.
BuildRequires:    python3-docutils
Requires:         python3-%{modname} = %{version}-%{release}
Requires:         bash
Requires:         which
# Keep manual runtime reqs in -tests subpackages for now
Requires:         python3-subunit
Requires:         python3-testtools
Requires:         python3-testscenarios
Requires:         python3-PyYAML
Requires:         python3-fixtures


%description -n python3-%{modname}-tests
%{common_desc_tests}


%description
%{common_desc}


%prep
%autosetup -p1 -n %{modname}-%{version}

# Ignore openstack global constraints
sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini


# Avoid sphinx as BR as we are not building doc
rm cliff/tests/test_sphinxext.py


%generate_buildrequires
%if %{with bootstrap}
%pyproject_buildrequires
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l cliff


%check
%if %{with bootstrap}
%pyproject_check_import -e cliff.tests.* -e cliff.sphinxext
%else
%tox
%endif


%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc doc/ README.rst ChangeLog AUTHORS CONTRIBUTING.rst


%files -n python3-%{modname}-tests
%{python3_sitelib}/%{modname}/tests


%changelog
%autochangelog
