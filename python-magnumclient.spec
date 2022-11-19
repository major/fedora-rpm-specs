%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global sname python-magnumclient
%global pname magnumclient
%global with_doc 1

%global common_desc \
This is a client library for Magnum built on the Magnum API. \
It provides a Python API (the magnumclient module) and a \
command-line tool (magnum).

%global common_desc_tests Python-magnumclient test subpackage

Name:           python-%{pname}
Version:        4.0.0
Release:        1%{?dist}
Summary:        Client library for Magnum API

License:        ASL 2.0
URL:            https://launchpad.net/python-magnumclient
Source0:        https://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n     python3-%{pname}
Summary:        Client library for Magnum API
%{?python_provide:%python_provide python3-%{pname}}
Obsoletes: python2-%{pname} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  git-core

# test dependencies
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-openstackclient
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-oslo-log
%if 0%{?rhel}
BuildRequires:  python3-osprofiler
%endif
BuildRequires:  python3-stevedore
BuildRequires:  python3-requests
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-testtools
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-prettytable
BuildRequires:  python3-stestr

Requires:    python3-cryptography
Requires:    python3-keystoneauth1 >= 3.4.0
Requires:    python3-oslo-i18n >= 3.15.3
Requires:    python3-oslo-log >= 3.36.0
Requires:    python3-oslo-serialization >= 2.18.0
Requires:    python3-oslo-utils >= 3.33.0
Requires:    python3-osc-lib >= 1.8.0
Requires:    python3-os-client-config >= 1.28.0
Requires:    python3-pbr
Requires:    python3-prettytable

Requires:    python3-decorator

%description -n python3-%{pname}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pname}-doc
Summary:        python-magnumclient documentation
BuildRequires:   python3-sphinx
BuildRequires:   python3-openstackdocstheme
BuildRequires:   python3-os-client-config

BuildRequires:   python3-decorator

%description -n python-%{pname}-doc
Documentation for python-magnumclient
%endif

%package -n python3-%{pname}-tests
Summary: Python-magnumclient test subpackage
%{?python_provide:%python_provide python2-%{pname}-tests}

Requires:  python3-%{pname} = %{version}-%{release}
Requires:  python3-oslo-utils
Requires:  python3-stevedore
Requires:  python3-requests
Requires:  python3-oslo-i18n
Requires:  python3-fixtures
Requires:  python3-mock
Requires:  python3-testtools
Requires:  python3-keystoneauth1
Requires:  python3-prettytable
Requires:  python3-stestr

%description -n python3-%{pname}-tests
%{common_desc_tests}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

# let RPM handle deps
rm -rf *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
# (TODO) Re-add -W once https://review.openstack.org/#/c/554197 is in a
# tagged release
sphinx-build-3 -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
%if 0%{?rhel}
PYTHON=%{__python3} stestr run --slowest
%else
PYTHON=%{__python3} stestr run --slowest || true
%endif

%files -n python3-%{pname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pname}
%{_bindir}/magnum
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/%{pname}/tests

%if 0%{?with_doc}
%files -n python-%{pname}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python3-%{pname}-tests
%{python3_sitelib}/%{pname}/tests

%changelog
* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 4.0.0-1
- Update to upstream version 4.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 3.6.0-2
- Rebuilt for Python 3.11

* Thu May 19 2022 Joel Capitao <jcapitao@redhat.com> 3.6.0-1
- Update to upstream version 3.6.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Joel Capitao <jcapitao@redhat.com> 3.4.0-1
- Update to upstream version 3.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 3.2.1-2
- Update to upstream version 3.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Joel Capitao <jcapitao@redhat.com> 3.0.0-1
- Update to upstream version 3.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.15.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Alfredo Moralejo <amoralej@redhat.com> 2.15.0-1
- Update to upstream version 2.15.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.12.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.12.0-4
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Alfredo Moralejo <amoralej@redhat.com> - 2.12.0-3
- Removed osprofiler as BR.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 2.12.0-1
- Update to 2.12.0

