# Created by pyp2rpm-3.2.2
%global pypi_name ansible-runner

Name:           python-%{pypi_name}
Version:        2.4.3
Release:        %autorelease
Summary:        A tool and python library to interface with Ansible

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/ansible/ansible-runner
Source0:        https://github.com/ansible/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# Fix a test failure with Python 3.13(?)
# https://github.com/ansible/ansible-runner/pull/1377
# https://github.com/ansible/ansible-runner/pull/1379
# merged and looks staged for next release.
Patch:          0001-Base64IO-set-write-buffer-before-doing-attr-check.patch
# Fix a test failure with Python 3.14 - codecs.open was deprecated
# https://github.com/ansible/ansible-runner/pull/1434
Patch:          0001-Python-3.14-compat-replace-codecs.open-with-open.patch

BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: ansible-core
BuildRequires: python3dist(pbr)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(psutil)
BuildRequires: python3dist(pexpect) >= 4.6
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-mock)
BuildRequires: python3dist(pytest-timeout)
BuildRequires: python3dist(pytest-xdist)
BuildRequires: python3dist(pyyaml)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(six)
BuildRequires: python3dist(python-daemon)
BuildRequires: python3dist(wheel)

Requires: (ansible-core or ansible)

%description
Ansible Runner is a tool and python library that helps when interfacing with
Ansible from other systems whether through a container image interface, as a
standalone tool, or imported into a python project.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Ansible Runner is a tool and python library that helps when interfacing with
Ansible from other systems whether through a container image interface, as a
standalone tool, or imported into a python project.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Allow the version of setuptools that's in fedora
sed -i 's/, <=[0-9.]*//g' pyproject.toml

# Allow the version of setuptools-scm that's in fedora
sed -i 's/, <=8.0.4//' pyproject.toml

sed -i '166 i \@pytest.mark.skip(reason="can not resolve example.com in build system")' test/integration/test_display_callback.py
sed -i '/test_resolved_actions/i \@pytest.mark.skip(reason="ansible version lookup is blank in build")' test/integration/test_display_callback.py
# there's a locale issue with ansible that makes these tests fail.
sed -i '/^def test_worker_without_delete_no_dir.*/i @pytest.skip("Ansible could not initialize the preferred locale: unsupported locale setting", allow_module_level=True)' test/integration/test_transmit_worker_process.py
sed -i '/^def test_worker_without_delete_dir_exists.*/i @pytest.skip("Ansible could not initialize the preferred locale: unsupported locale setting", allow_module_level=True)' test/integration/test_transmit_worker_process.py
sed -i '/^def test_worker_delete_no_dir.*/i @pytest.skip("Ansible could not initialize the preferred locale: unsupported locale setting", allow_module_level=True)' test/integration/test_transmit_worker_process.py
sed -i '/^def test_worker_delete_dir_exists.*/i @pytest.skip("Ansible could not initialize the preferred locale: unsupported locale setting", allow_module_level=True)' test/integration/test_transmit_worker_process.py
# Syntax error upstream with this test, still fails after fixing so skip for now
sed -i '/^def test_dump_artifacts_inventory_object.*/i @pytest.mark.skip("syntax error upstream")' test/unit/utils/test_dump_artifacts.py
# Deprecation Warning from datetime.utcnow()
sed -i '/^def test_no_ResourceWarning_error.*/i @pytest.mark.skip("DeprecationWarning: datetime.utcnow() is deprecated ")' test/unit/test_runner.py

%generate_buildrequires
export PBR_VERSION=%{version}
%pyproject_buildrequires

%build
export PBR_VERSION=%{version}
%pyproject_wheel

%install
export PBR_VERSION=%{version}
%pyproject_install
cp %{buildroot}/%{_bindir}/ansible-runner %{buildroot}/%{_bindir}/ansible-runner-%{python3_version}
ln -s ansible-runner-%{python3_version} %{buildroot}/%{_bindir}/ansible-runner-3

%check
# test suite hangs indefinitely on exit without -n auto
# note this implies the dep on xdist, so don't remove it
# https://github.com/ansible/ansible-runner/issues/1369
%pytest -n auto

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{_bindir}/ansible-runner-3
%{_bindir}/ansible-runner-%{python3_version}
%{python3_sitelib}/ansible_runner
%{python3_sitelib}/ansible_runner-%{version}.dist-info
%{_bindir}/ansible-runner

%changelog
%autochangelog
