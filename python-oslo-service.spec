%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name oslo.service
%global pname oslo-service
%global with_doc 1

%global common_desc \
Library for running OpenStack services

%global common_desc1 \
Tests for oslo.service

Name:           python-%{pname}
Version:        1.29.0
Release:        3%{?dist}
Summary:        Oslo service library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git


%package -n     python3-%{pname}
Summary:        Oslo service library
%{?python_provide:%python_provide python3-%{pname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr >= 2.0.0
# Required for tests
BuildRequires:  procps-ng
BuildRequires:  python3-eventlet
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-oslo-concurrency
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-paste
BuildRequires:  python3-paste-deploy
BuildRequires:  python3-requests
BuildRequires:  python3-routes
BuildRequires:  python3-webob

Requires:       python3-eventlet >= 0.18.2
Requires:       python3-greenlet
Requires:       python3-monotonic >= 0.6
Requires:       python3-oslo-config >= 2:5.1.0
Requires:       python3-oslo-concurrency >= 3.25.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-paste
Requires:       python3-paste-deploy >= 1.5.0
Requires:       python3-routes
Requires:       python3-six >= 1.10.0
Requires:       python3-webob


%description -n python3-%{pname}
%{common_desc}

%package -n python3-%{pname}-tests
Summary:        Oslo service tests
%{?python_provide:%python_provide python3-%{pname}-tests}

Requires:  python3-%{pname} = %{version}-%{release}
Requires:  procps-ng
Requires:  python3-fixtures
Requires:  python3-mock
Requires:  python3-requests
Requires:  python3-routes
Requires:  python3-oslotest

%description -n python3-%{pname}-tests
%{common_desc1}

%if 0%{?with_doc}
%package -n python-%{pname}-doc
Summary:        Oslo service documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-%{pname}-doc
Documentation for oslo.service
%endif

%description
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Drop capping of eventlet < 0.21.0
sed -i 's/eventlet.*/eventlet/g' requirements.txt

%build
%py3_build

%if 0%{?with_doc}
# generate html docs
%{__python3} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
export PYTHON=%{__python3}
%{__python3} setup.py test ||
rm -rf .testrepository

%files -n python3-%{pname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_service
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_service/tests

%files -n python3-%{pname}-tests
%{python3_sitelib}/oslo_service/tests

%files -n python-%{pname}-doc
%doc doc/build/html
%license LICENSE

%changelog
* Tue Feb 26 2019 Alfredo Moralejo <amoralej@redhat.com> 1.29.0-3
- Drop eventlet capping

* Thu Jan 31 2019 Yatin Karel <ykarel@redhat.com> - 1.29.0-2
- Drop python2 sub packages (#1632343)

* Mon Jul 23 2018 Matthias Runge <mrunge@redhat.com> - 1.29.0-1
- update to Queens

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.19.0-6
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.19.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.19.0-2
- Fix python tests subpackages

* Wed Feb 08 2017 Alfredo Moralejo <amoralej@redhat.com> 1.19.0-1
- Update to 1.19.0

