Name:               python-iniconfig
Version:            1.1.1
Release:            %autorelease
Summary:            Brain-dead simple parsing of ini files
# SPDX
License:            MIT
URL:                http://github.com/RonnyPfannschmidt/iniconfig
BuildArch:          noarch
BuildRequires:      python3-devel
BuildRequires:      pyproject-rpm-macros

# pytest 6+ needs this and this uses pytest for tests
%bcond_without tests

%if %{with tests}
# We BR pytest manually to avoid a dependency on tox in ELN/RHEL
BuildRequires:      python3-pytest
%endif

Source0:            %{pypi_source iniconfig}

%global _description %{expand:
iniconfig is a small and simple INI-file parser module
having a unique set of features:

* tested against Python2.4 across to Python3.2, Jython, PyPy
* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an Error if two sections have the same name.}
%description %_description


%package -n python3-iniconfig
Summary:            %{summary}
%description -n python3-iniconfig %_description


%prep
%autosetup -n iniconfig-%{version}
# Remove undeclared dependency on python-py
# Merged upstream https://github.com/pytest-dev/iniconfig/pull/47
sed -i "s/py\.test/pytest/" testing/test_iniconfig.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files iniconfig


%if %{with tests}
%check
%pytest -v
%endif


%files -n python3-iniconfig -f %{pyproject_files}
%doc README.txt
%license LICENSE


%changelog
%autochangelog
