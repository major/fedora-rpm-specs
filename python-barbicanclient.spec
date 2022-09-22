%{?python_enable_dependency_generator}
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

%global sname barbicanclient

%global common_desc \
This is a client for the Barbican Key Management API. There is a \
Python library for accessing the API (barbicanclient module), and \
a command-line script (barbican).

Name:           python-barbicanclient
Version:        5.3.0
Release:        3%{?dist}
Summary:        Client Library for OpenStack Barbican Key Management API

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-barbicanclient
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
%description
%{common_desc}

%package -n python3-%{sname}
Summary:        Client Library for OpenStack Barbican Key Management API
%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
Requires:       python3-requests >= 2.14.2
Requires:       python3-six >= 1.10.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-prettytable
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-cliff >= 2.8.0

%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: Documentation for OpenStack Barbican API client

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-prettytable

%description -n python-%{sname}-doc
Documentation for the barbicanclient module
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

rm -rf {test-,}requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# doc
%{__python3} setup.py build_sphinx -b html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%{py3_install}
ln -s ./barbican %{buildroot}%{_bindir}/barbican-3

%files -n python3-%{sname}
%license LICENSE
%doc AUTHORS CONTRIBUTING.rst README.rst PKG-INFO ChangeLog
%{_bindir}/barbican
%{_bindir}/barbican-3
%{python3_sitelib}/barbicanclient
%{python3_sitelib}/python_barbicanclient-%{upstream_version}-py%{python3_version}.egg-info

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 5.3.0-2
- Rebuilt for Python 3.11

* Wed May 18 2022 Joel Capitao <jcapitao@redhat.com> 5.3.0-1
- Update to upstream version 5.3.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1.0-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 5.1.0-1
- Update to upstream version 5.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 5.0.1-2
- Update to upstream version 5.0.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 4.10.0-1
- Update to upstream version 4.10.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.9.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 4.9.0-2
- Update to upstream version 4.9.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.8.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.8.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 RDO <dev@lists.rdoproject.org> 4.8.1-1
- Update to 4.8.1

