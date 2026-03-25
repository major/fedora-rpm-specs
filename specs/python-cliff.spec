# There is circular dependency with this requiring stestr requiring cliff requiring stevedore
%bcond_with bootstrap

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order sphinx coverage

%global modname cliff

%global common_desc \
cliff is a framework for building command line programs. It uses setuptools \
entry points to provide subcommands, output formatters, and other \
extensions. \
\
Documentation for cliff is hosted on readthedocs.org at \
http://readthedocs.org/docs/cliff/en/latest/

%global common_desc_tests This package contains tests for the python cliff library.

Name:             python-%{modname}
Version:          4.13.2
Release:          %autorelease
Summary:          Command Line Interface Formulation Framework

Group:            Development/Libraries
License:          Apache-2.0
URL:              https://pypi.io/pypi/cliff
Source0:          https://pypi.io/packages/source/c/cliff/cliff-%{version}.tar.gz

# Backport of https://opendev.org/openstack/cliff/commit/fcf9710013e40c1aea22a76d76158acb56f5fc46.patch
Patch0:           relax-caller.patch

BuildArch:        noarch

%package -n python3-%{modname}
Summary:          Command Line Interface Formulation Framework

BuildRequires:    python3-devel


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
%autosetup -p1 -n %{modname}-%{upstream_version}

# Ignore openstack global constraints
sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

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
%pyproject_check_import -e cliff.tests.*
%else
%tox
%endif


%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc doc/ README.rst ChangeLog AUTHORS CONTRIBUTING.rst
%exclude %{python3_sitelib}/%{modname}/tests


%files -n python3-%{modname}-tests
%{python3_sitelib}/%{modname}/tests


%changelog
%autochangelog
