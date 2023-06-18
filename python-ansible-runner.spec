# Created by pyp2rpm-3.2.2
%global pypi_name ansible-runner

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{pypi_name}
Version:        2.3.2
Release:        2%{?dist}
Summary:        A tool and python library to interface with Ansible

License:        ASL 2.0
URL:            https://github.com/ansible/ansible-runner
Source0:        https://github.com/ansible/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: ansible-core
BuildRequires: python3dist(mock)
BuildRequires: python3dist(pbr)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(psutil)
BuildRequires: python3dist(pexpect) >= 4.6
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
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
%autosetup -n %{pypi_name}-%{version}
sed -i '166 i \@pytest.mark.skip(reason="can not resolve example.com in build system")' test/integration/test_display_callback.py
sed -i '/test_resolved_actions/i \@pytest.mark.skip(reason="ansible version lookup is blank in build")' test/integration/test_display_callback.py
# there's a locale issue with ansible that makes these tests fail.
sed -i '/^def test_worker_without_delete_no_dir.*/i @pytest.skip("Ansible could not initialize the preferred locale: unsupported locale setting", allow_module_level=True)' test/integration/test_transmit_worker_process.py
sed -i '/^def test_worker_without_delete_dir_exists.*/i @pytest.skip("Ansible could not initialize the preferred locale: unsupported locale setting", allow_module_level=True)' test/integration/test_transmit_worker_process.py
sed -i '/^def test_worker_delete_no_dir.*/i @pytest.skip("Ansible could not initialize the preferred locale: unsupported locale setting", allow_module_level=True)' test/integration/test_transmit_worker_process.py
sed -i '/^def test_worker_delete_dir_exists.*/i @pytest.skip("Ansible could not initialize the preferred locale: unsupported locale setting", allow_module_level=True)' test/integration/test_transmit_worker_process.py

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
%pytest

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{_bindir}/ansible-runner-3
%{_bindir}/ansible-runner-%{python3_version}
%{python3_sitelib}/ansible_runner
%{python3_sitelib}/ansible_runner-%{version}.dist-info
%{_bindir}/ansible-runner
%{_datadir}/ansible-runner/utils

%changelog
* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.3.2-2
- Rebuilt for Python 3.12

* Fri Mar 24 2023 Dan Radez <dradez@redhat.com> - 2.3.2-1
- update to 2.3.2 rhbz#2174741

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Dan Radez <dradez@redhat.com> - 2.3.1-1
- update to 2.3.1 (rhbz#2139251)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Dan Radez <dradez@redhat.com> - 2.2.1-1
- update to 2.2.1

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.1.3-4
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Dan Radez <dradez@redhat.com> - 2.1.3-3
- updating to use pyproject macros

* Mon Apr 11 2022 Maxwell G <gotmax@e.email> - 2.1.3-2
- Allow users to choose between ansible and ansible-core.
- Switch BR from ansible to ansible-core.
- Use relative symlinks.

* Thu Mar 24 2022 Dan Radez <dradez@redhat.com> - 2.1.3-1
- Update to 2.1.3

* Tue Feb 08 2022 Dan Radez <dradez@redhat.com> - 2.1.1-3
- Don't remove egginfo

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Dan Radez <dradez@redhat.com> - 2.1.1-1
- updating to version 2.1.1

* Tue Dec 14 2021 Dan Radez <dradez@redhat.com> - 2.0.0a1-4
- remove the test module from packaged files

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0a1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0a1-2
- Rebuilt for Python 3.10

* Fri Apr 30 2021 Dan Radez <dradez@redhat.com> - 2.0.0a1
- updating to version 2.0.0a1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Dan Radez <dradez@redhat.com> - 1.4.6-1
- updating to version 1.4.6

* Tue Mar 24 2020 Dan Radez <dradez@redhat.com> - 1.4.5-1
- updating to version 1.4.5

* Wed Dec 04 2019 Yatin Karel <ykarel@redhat.com> - 1.4.4-2
- Drop dependency on tox

* Tue Nov 05 2019 Dan Radez <dradez@redhat.com> - 1.4.4-1
- updating to version 1.4.4

* Wed Oct 09 2019 Dan Radez <dradez@redhat.com> - 1.4.2-1
- Updating to version 1.4.2

* Tue Oct 08 2019 Dan Radez <dradez@redhat.com> - 1.4.0-1
- Updating to version 1.4.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Dan Radez <dradez@redhat.com> - 1.3.4-1
- Updating to version 1.3.4

* Mon Apr 22 2019 Dan Radez <dradez@redhat.com> - 1.3.3-1
- Updating to version 1.3.3

* Wed Apr 10 2019 Dan Radez <dradez@redhat.com> - 1.3.2-1
- Updating to version 1.3.2

* Wed Mar 20 2019 Dan Radez <dradez@redhat.com> - 1.3.0-1
- Updating to version 1.3

* Wed Feb 13 2019 Yatin Karel <ykarel@redhat.com> - 1.2.0-2
- Enable python2 build for CentOS <= 7

* Mon Feb 04 2019 Dan Radez <dradez@redhat.com> - 1.2.0-1
- Updating to version 1.2
- removing python 2 from the spec for F30

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Dan Radez <dradez@redhat.com> - 1.1.2-1
- Updating to version 1.1.2

* Wed Sep 12 2018 Dan Radez <dradez@redhat.com> - 1.1.0-1
- Updating to version 1.1.0

* Wed Jul 25 2018 Dan Radez <dradez@redhat.com> - 1.0.5-1
- Updating to version 1.0.5

* Wed Jul 25 2018 Dan Radez <dradez@redhat.com> - 1.0.4-4
- 1.0.4 requires pexepct 4.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Iryna Shcherbina - 1.0.4-2
- Fix Python 3 dependency from python2-ansible-runner

* Mon Jul 02 2018 Dan Radez <dradez@redhat.com> - 1.0.4-1
- Updating to version 1.0.4

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-4
- Rebuilt for Python 3.7

* Fri Jun 01 2018 Dan Radez <dradez@redhat.com> - 1.0.3-3
- skip py3 on non-fedora

* Thu May 31 2018 Dan Radez <dradez@redhat.com> - 1.0.3-1
- Updating to version 1.0.3

* Tue May 29 2018 Dan Radez <dradez@redhat.com> - 1.0.2-1
- Updating to version 1.0.2
- Package Requires versions updated
- added py3 support

* Fri May 11 2018 Dan Radez <dradez@redhat.com> - 1.0.1-2
- Adding conditionals so the same spec can be built on fedora and el7

* Fri May 04 2018 Dan Radez <dradez@redhat.com> - 1.0.1-1
- Initial package. Python 2 support only initially.
