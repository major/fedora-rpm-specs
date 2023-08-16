%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa7475c5f2122fec3f90343223fe3bf5aad1080e4

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname troveclient
%global with_doc 1

%global common_desc \
This is a client for the Trove API. There's a Python API (the \
troveclient module), and a command-line script (trove). Each \
implements 100% (or less ;) ) of the Trove API.

Name:           python-troveclient
Version:        8.1.0
Release:        2%{?dist}
Summary:        Client library for OpenStack DBaaS API

License:        ASL 2.0
URL:            http://www.openstack.org/
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
Summary:        Client library for OpenStack DBaaS API
%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-pbr
BuildRequires:  python3-oslotest
BuildRequires:  python3-mock
BuildRequires:  python3-testtools
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-mistralclient
BuildRequires:  python3-openstackclient
BuildRequires:  python3-swiftclient
BuildRequires:  python3-testrepository
BuildRequires:  python3-simplejson
BuildRequires:  python3-requests-mock
BuildRequires:  python3-httplib2

Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-mistralclient >= 3.1.0
Requires:       python3-openstackclient >= 3.12.0
Requires:       python3-swiftclient >= 3.2.0
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pbr
Requires:       python3-prettytable
Requires:       python3-requests
Requires:       python3-simplejson

%description -n python3-%{sname}
%{common_desc}


%if 0%{?with_doc}
%package doc
Summary:        Documentation for troveclient
# These are doc requirements
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-apidoc
%description doc
%{common_desc}

This package contains the documentation
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

# Remove bundled egg-info
rm -rf %{name}.egg-info

# Let RPM handle the requirements
rm -f {test-,}requirements.txt


%build
%{py3_build}

%install
%{py3_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s trove %{buildroot}%{_bindir}/trove-3


%if 0%{?with_doc}
# generate html docs
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%check
export PYTHON=%{__python3}
# A unit test fails because of a warning thrown from keystoneauth
export PYTHONWARNINGS=ignore::DeprecationWarning
PYTHONPATH=. %{__python3} setup.py test


%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/python_troveclient-*.egg-info
%{python3_sitelib}/troveclient
%{_bindir}/trove-3
%{_bindir}/trove

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Karolina Kula <kkula@redhat.com> 8.1.0-1
- Update to upstream version 8.1.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 8.0.0-1
- Update to upstream version 8.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 7.2.0-2
- Rebuilt for Python 3.11

* Wed May 18 2022 Joel Capitao <jcapitao@redhat.com> 7.2.0-1
- Update to upstream version 7.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.0.0-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 7.0.0-1
- Update to upstream version 7.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 5.1.1-2
- Update to upstream version 5.1.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 3.3.1-1
- Update to upstream version 3.3.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 3.0.0-1
- Update to upstream version 3.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.17.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.17.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 RDO <dev@lists.rdoproject.org> 2.17.0-1
- Update to 2.17.0

