%global srcname ansible-pylibssh
%global _summary Python bindings specific to Ansible use case for libssh

Name:           python-%{srcname}
Version:        1.2.2
Release:        2%{?dist}
Summary:        %{_summary}

License:        LGPL-2.1-or-later
URL:            https://github.com/ansible/pylibssh
Source0:        %{pypi_source}
# Downstream patch to disable coverage tests
Patch0:         python-ansible-pylibssh-nocov.patch

BuildRequires:  gcc
BuildRequires:  libssh-devel
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  /usr/bin/ssh
BuildRequires:  /usr/bin/ssh-keygen
BuildRequires:  /usr/sbin/sshd

%global _description %{expand:
Python bindings to client functionality of libssh specific to Ansible use
case.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{_summary}

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -e just-pytest


%build
export PYTHONPATH=bin
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l '*pylibssh*'


%check
# Fails - need to disable cython coverage
%tox
# -- -- --deselect tests/unit/scp_test.py::test_get --deselect tests/unit/scp_test.py::test_put


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc AUTHORS.rst README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 20 2024 Orion Poplawski <orion@nwra.com> - 1.2.2-1
- Initial Fedora package
