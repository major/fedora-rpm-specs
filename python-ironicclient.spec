%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa7475c5f2122fec3f90343223fe3bf5aad1080e4
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname ironicclient

%global common_desc A python and command line client library for Ironic

Name:           python-ironicclient
Version:        5.1.0
Release:        2%{?dist}
Summary:        Python client for Ironic

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-%{sname}
Source0:        https://tarballs.openstack.org/python-%{sname}/python-%{sname}-%{version}%{?milestone}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/python-%{sname}/python-%{sname}-%{version}%{?milestone}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n python3-%{sname}
Summary:        Python client for Ironic
%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools

Requires:       xorriso
Requires:       python3-appdirs >= 1.3.0
Requires:       python3-cliff >= 2.8.0
Requires:       python3-dogpile-cache >= 0.8.0
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-keystoneauth1 >= 3.11.0
Requires:       python3-openstacksdk >= 0.18.0
Requires:       python3-osc-lib >= 2.0.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-yaml >= 3.13

%if 0%{?fedora} || 0%{?rhel} > 7
Suggests:       python3-openstackclient
%endif

%description -n python3-%{sname}
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n %{name}-%{upstream_version}

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/baremetal
%{python3_sitelib}/%{sname}*
%{python3_sitelib}/python_%{sname}*

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.1.0-2
- Rebuilt for Python 3.12

* Fri Apr 14 2023 Karolina Kula <kkula@redhat.com> 5.1.0-1
- Update to upstream version 5.1.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 5.0.1-1
- Update to upstream version 5.0.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.11.0-2
- Rebuilt for Python 3.11

* Wed May 18 2022 Joel Capitao <jcapitao@redhat.com> 4.11.0-1
- Update to upstream version 4.11.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.6.1-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 4.6.1-1
- Update to upstream version 4.6.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 4.3.0-2
- Update to upstream version 4.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 4.1.0-1
- Update to upstream version 4.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Alfredo Moralejo <amoralej@redhat.com> 3.1.0-1
- Update to upstream version 3.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 2.7.0-1
- Update to 2.7.0

