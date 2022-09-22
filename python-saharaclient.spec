%{?python_enable_dependency_generator}
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363
%global sname saharaclient


%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:             python-saharaclient
Version:          3.5.0
Release:          3%{?dist}
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          https://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python3-%{sname}
Summary:	Client library for OpenStack Sahara API
BuildRequires:    python3-setuptools
BuildRequires:    python3-devel
BuildRequires:    python3-mock >= 2.0.0
BuildRequires:    python3-osc-lib >= 1.11.0
BuildRequires:    python3-osc-lib-tests >= 1.11.0
BuildRequires:    python3-oslotest >= 3.2.0
BuildRequires:    python3-oslo-log >= 3.36.0
BuildRequires:    python3-oslo-serialization >= 2.18.0
BuildRequires:    python3-pbr >= 2.0.0
BuildRequires:    python3-requests-mock >= 1.2.0
BuildRequires:    python3-stestr >= 1.0.0

Requires:         python3-keystoneauth1 >= 3.4.0
Requires:         python3-openstackclient >= 5.2.0
Requires:         python3-osc-lib >= 2.0.0
Requires:         python3-oslo-i18n >= 3.15.3
Requires:         python3-oslo-log >= 3.36.0
Requires:         python3-oslo-serialization >= 2.18.0
Requires:         python3-oslo-utils >= 3.33.0
Requires:         python3-pbr >= 2.0.0
Requires:         python3-requests >= 2.14.2
Requires:         python3-six >= 1.10.0

%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
Python client library for interacting with OpenStack Sahara API.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n %{name}-%{upstream_version}

rm -rf python_saharaclient.egg-info
rm -rf *requirements.txt

%build
%{py3_build}


%install
%{py3_install}

%check
# Remove hacking tests, we don't need them
rm saharaclient/tests/unit/test_hacking.py
export PYTHON=%{__python3}
stestr-3 run

%files -n python3-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{python3_sitelib}/saharaclient
%{python3_sitelib}/*.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 3.5.0-2
- Rebuilt for Python 3.11

* Wed May 18 2022 Joel Capitao <jcapitao@redhat.com> 3.5.0-1
- Update to upstream version 3.5.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 3.3.0-1
- Update to upstream version 3.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 3.2.1-2
- Update to upstream version 3.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 3.1.0-1
- Update to upstream version 3.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 2.3.0-1
- Update to upstream version 2.3.0

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 2.3.0-1
- Update to upstream version 2.3.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 2.2.0-1
- Update to 2.2.0

