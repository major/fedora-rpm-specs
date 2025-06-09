Name:           python-pytest-testinfra
Version:        10.2.2
Release:        2%{?dist}
Summary:        Unit testing for config-managed server state

License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-testinfra
Source:         %{pypi_source pytest_testinfra}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
With Testinfra you can write unit tests in Python to test actual state of your
servers configured by management tools like Salt, Ansible, Puppet, Chef and so
on.
Testinfra aims to be a Serverspec equivalent in python and is written as a
plugin to the powerful Pytest test engine.}

%description %_description

%package -n     python3-pytest-testinfra
Summary:        %{summary}

# Using suggests to avoid unnecessary dependencies being installed
Suggests:       python3-pytest-testinfra+ansible
Suggests:       python3-pytest-testinfra+paramiko
Suggests:       python3-pytest-testinfra+salt
Suggests:       python3-pytest-testinfra+winrm

# python-testinfra is a duplicate with wrong name
Provides:       python3-testinfra = %{version}-%{release}

%description -n python3-pytest-testinfra %_description

%pyproject_extras_subpkg -n python3-pytest-testinfra ansible,paramiko,salt,winrm

%prep
%autosetup -p1 -n pytest_testinfra-%{version}

# types-paramiko package is not available and is not needed for build tests
sed -i '/types-paramiko/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x ansible,paramiko,salt,winrm -e %{toxenv}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files testinfra 

%check
%pyproject_check_import
%tox

%files -n python3-pytest-testinfra -f %{pyproject_files}
%doc README.rst

%changelog
* Sat Jun 07 2025 Python Maint <python-maint@redhat.com> - 10.2.2-2
- Rebuilt for Python 3.14

%autochangelog
