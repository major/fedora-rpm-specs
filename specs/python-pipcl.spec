%global pypi_name pipcl
%global module_name pipcl

%bcond docs 1
%bcond tests 1

Name:		python-%{pypi_name}
Version:	11
Release:	%autorelease
Summary:	Python packaging operations including PEP-517 support

# Clarified by license classifier
License:	AGPL-3.0-only
URL:		https://github.com/ArtifexSoftware/pipcl
Source0:	%{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# alternative:	%%{pypi_source %%{pypi_name}}

BuildArch:	noarch
BuildRequires:	python3-devel

%if %{with tests}
# test dependencies not picked up by generator
BuildRequires:	gcc-c++
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(swig)
%endif

%if %{with docs}
# doc dependencies
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx-theme-alabaster
BuildRequires:	python3dist(autodocsumm)
%endif

%global _description %{expand:
Python packaging operations, including PEP-517 support, for use by a script.}

%description %_description

%package -n python3-%{pypi_name}
Summary:	%{summary}

%description -n python3-%{pypi_name} %_description

%if %{with docs}
%package	doc
Summary:	Documentation for python-%{pypi_name}
BuildArch:	noarch

%description    doc
python-%{pypi_name}-doc contains documentation for %{pypi_name}

%endif

%prep
%autosetup -n %{pypi_name}-%{version} -p 1
# do not run pip over the internet
sed -i -e '/pip install/d' docs/conf.py tests/test_doctest.py

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel
%if %{with docs}
export PYTHONPATH=%{_pyproject_wheeldir}/%{pypi_name}-%{version}-py3-none-any.whl
sphinx-build -M html docs docs/_build
%endif

%install
%pyproject_install
%pyproject_save_files -L %{module_name}

%check
%pyproject_check_import
%if %{with tests}
# do not run linters during build check
# test_change_versions and test_project use piprepo (not packaged)
%pytest -k "not test_lint and not test_change_versions and not test_project"
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING

%if %{with docs}
%files doc
%license COPYING
%doc docs/_build/* README.rst
%endif

%changelog
%autochangelog
