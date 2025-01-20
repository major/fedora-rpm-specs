Name:           python-pytest-testinfra
Version:        10.1.1
Release:        4%{?dist}
Summary:        Unit testing for config-managed server state

License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-testinfra
Source:         %{pypi_source pytest-testinfra}

BuildArch:      noarch
BuildRequires:  python3-devel

# TODO 'crypt' test requirement for Python 3.13 - remove in next release
BuildRequires:  python3-crypt-r

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
Provides: 	python3-testinfra = %{version}-%{release}
Obsoletes: 	python3-testinfra < 5.3.1-14

%description -n python3-pytest-testinfra %_description

%pyproject_extras_subpkg -n python3-pytest-testinfra ansible,paramiko,salt,winrm

%prep
%autosetup -p1 -n pytest-testinfra-%{version}

# types-paramiko package is not available and is not needed for build tests
sed -i '/types-paramiko/d' test-requirements.txt

%generate_buildrequires
%pyproject_buildrequires -t 

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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

%autochangelog
