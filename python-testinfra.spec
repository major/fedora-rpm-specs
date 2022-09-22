%global srcname testinfra

Name:    python-%{srcname}
Version: 5.3.1
Release: 9%{?dist}
Summary: Unit testing for config-managed server state

License: ASL 2.0
URL:     https://github.com/philpep/testinfra
Source:  %{pypi_source}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)

# testing requirements
# Use ansible-core for testing wherever it's available.
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
BuildRequires: ansible-core
%else
BuildRequires: (ansible-core or ansible)
%endif

BuildRequires: python3dist(pywinrm)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(paramiko)

# docs requirements
BuildRequires: python3dist(sphinx)

%global _description %{expand:
With Testinfra you can write unit tests in Python to test actual state of your
servers configured by management tools like Salt, Ansible, Puppet, Chef and so
on.

Testinfra aims to be a Serverspec equivalent in python and is written as a
plugin to the powerful Pytest test engine.
}

%description %{_description}

%package -n python3-%{srcname}
Summary: %summary

# See https://src.fedoraproject.org/rpms/ansible/pull-request/19#comment-93748.
# This will allow users to choose between ansible 2.9 and ansible-core 2.11
# when available, while avoiding unnecessarily pulling in the entire collections bundle on F36 and above.
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
Requires: ansible-core
%else
Requires: (ansible-core or ansible)
%endif

Requires: python3dist(pywinrm)
Requires: python3dist(paramiko)
Suggests: python3dist(pytest-xdist)

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

# no Python 3 salt
rm testinfra/backend/salt.py
sed -i "/'salt':/d" testinfra/backend/__init__.py

%build
%py3_build

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -vr html/.{doctrees,buildinfo}

%install
%py3_install

%check
# majority of the tests gets skipped without docker, but some run
%{python3} -m pytest test -v

%files -n python3-%{srcname}
%license LICENSE
%doc html *.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 5.3.1-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Chedi Toueiti <chedi.toueiti@gmail.com> 5.3.1-6
- spec file modernization

* Wed Jan 12 2022 Maxwell G <gotmax@e.email> - 5.3.1-5
- Fix ansible dependency

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.3.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 5.3.1-1
- Update to version 5.3.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 5.2.2-1
- Update to version 5.2.2

* Fri Jul 10 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 5.2.1-1
- Update to version 5.2.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0

* Sat Aug 31 2019 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Miro Hrončok <mhroncok@redhat.com>
- Drop Python 2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Brett Lentz <brett.lentz@gmail.com> - 1.17.0-1
- update version

* Tue Jul 17 2018 Brett Lentz <brett.lentz@gmail.com> - 1.14.0-1
- update version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-2
- Rebuilt for Python 3.7

* Tue May 1 2018 Brett Lentz <brett.lentz@gmail.com> - 1.12.0-1
- update version

* Tue Apr 3 2018 Brett Lentz <brett.lentz@gmail.com> - 1.11.1-2
- fix deps

* Tue Mar 6 2018 Brett Lentz <brett.lentz@gmail.com> - 1.11.1-1
- update version

* Wed Jan 24 2018 Brett Lentz <brett.lentz@gmail.com> - 1.10.1-1
- initial package
