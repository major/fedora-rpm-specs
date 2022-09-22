%global sname oslosphinx
%global pypi_name oslo-sphinx

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
The Oslo project intends to produce a python library containing \
infrastructure code shared by OpenStack projects. The APIs provided \
by the project should be high quality, stable, consistent and generally \
useful. \
 \
The oslo-sphinx library contains Sphinx theme and extensions support used by \
OpenStack.

Name:       python-oslo-sphinx
Version:    4.18.0
Release:    16%{?dist}
Summary:    OpenStack Sphinx Extensions

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    https://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz
Patch0:     sphnix-app-info.diff

BuildArch:  noarch

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:    OpenStack Sphinx Extensions
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:   python3-setuptools

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-d2to1
BuildRequires: python3-pbr
BuildRequires: python3-sphinx

Requires:      python3-requests >= 2.14.2
Requires:      python3-pbr
Requires:      python3-six >= 1.10.0

# tests
BuildRequires: python3-requests >= 2.14.2

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%autosetup -n oslosphinx-%{upstream_version} -p1
# Remove bundled egg-info
rm -rf oslo_sphinx.egg-info
rm -rf {test-,}requirements.txt

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python3} setup.py test

## Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslosphinx
%{python3_sitelib}/oslosphinx*.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.18.0-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.18.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.18.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.18.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.18.0-6
- Rebuilt for Python 3.8

* Sun Aug  4 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.18.0-5
- Add patch to avoid logging through sphinx.api (#1737205)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Alfredo Moralejo <amoralej@redhat.com> - 4.18.0-3
* Remove python2 subpackages

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Feb 09 2018 RDO <dev@lists.rdoproject.org> 4.18.0-1
- Update to 4.18.0

