%{?python_enable_dependency_generator}
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

%global cname neutron
%global sname %{cname}client

%global common_desc \
Client library and command line utility for interacting with OpenStack \
Neutron's API.

Name:       python-neutronclient
Version:    7.8.0
Release:    3%{?dist}
Summary:    Python API and CLI for OpenStack Neutron

License:    ASL 2.0
URL:        http://launchpad.net/%{name}/
Source0:    https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

Obsoletes:  python-%{sname}-tests <= 4.1.1-3

%description
%{common_desc}

%package -n python3-%{sname}
Summary:    Python API and CLI for OpenStack Neutron
%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires: git-core
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
# Required for unit tests
BuildRequires: python3-osc-lib-tests
BuildRequires: python3-oslotest
BuildRequires: python3-testtools
BuildRequires: python3-testrepository
BuildRequires: python3-testscenarios
BuildRequires: python3-keystoneauth1
BuildRequires: python3-keystoneclient
BuildRequires: python3-os-client-config
BuildRequires: python3-osc-lib
BuildRequires: python3-oslo-log
BuildRequires: python3-oslo-serialization
BuildRequires: python3-oslo-utils
BuildRequires: python3-cliff

Requires: python3-iso8601 >= 0.1.11
Requires: python3-os-client-config >= 1.28.0
Requires: python3-oslo-i18n >= 3.15.3
Requires: python3-oslo-log >= 3.36.0
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-pbr
Requires: python3-requests >= 2.14.2
Requires: python3-debtcollector >= 1.2.0
Requires: python3-osc-lib >= 1.12.0
Requires: python3-keystoneauth1 >= 3.8.0
Requires: python3-keystoneclient >= 1:3.8.0
Requires: python3-cliff >= 3.4.0
Requires: python3-netaddr >= 0.7.18

Requires: python3-simplejson >= 3.5.1

%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary:    Python API and CLI for OpenStack Neutron - Unit tests
%{?python_provide:%python_provide python3-%{sname}-tests}
Requires: python3-%{sname} == %{version}-%{release}
Requires: python3-osc-lib-tests
Requires: python3-oslotest
Requires: python3-testtools
Requires: python3-testrepository
Requires: python3-testscenarios

%description -n python3-%{sname}-tests
%{common_desc}

This package containts the unit tests.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Neutron API Client

BuildRequires:    python3-sphinx
BuildRequires:    python3-openstackdocstheme
BuildRequires:    python3-reno

%description      doc
%{common_desc}
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -rf *requirements.txt

# Remove unit tests requiring osprofiler which is not in Fedora
rm neutronclient/tests/unit/test_http.py

%build
%{py3_build}

%if 0%{?with_doc}
# Build HTML docs
export PYTHONPATH=.
sphinx-build -W -b html doc/source doc/build/html

# Fix hidden-file-or-dir warnings
rm -rf doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

%install
%{py3_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s %{cname} %{buildroot}%{_bindir}/%{cname}-3

%check
stestr run

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{sname}
%{python3_sitelib}/*.egg-info
%{_bindir}/%{cname}
%{_bindir}/%{cname}-3
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 7.8.0-2
- Rebuilt for Python 3.11

* Wed May 18 2022 Joel Capitao <jcapitao@redhat.com> 7.8.0-1
- Update to upstream version 7.8.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.3.0-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 7.3.0-1
- Update to upstream version 7.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 7.2.1-2
- Update to upstream version 7.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 7.1.1-1
- Update to upstream version 7.1.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.14.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Alfredo Moralejo <amoralej@redhat.com> 6.14.0-1
- Update to upstream version 6.14.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.12.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.12.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 6.12.0-1
- Update to 6.12.0

