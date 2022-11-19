%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global library osc-lib
%global module osc_lib

%global common_desc osc-lib is a package of common support modules for writing OSC plugins.
%global with_doc 1

Name:       python-%{library}
Version:    2.6.2
Release:    1%{?dist}
Summary:    OpenStack library for writing OSC plugins
License:    ASL 2.0
URL:        https://github.com/openstack/%{library}/

Source0:    https://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%package -n python3-%{library}
Summary:    OpenStack library for writing OSC plugins
%{?python_provide:%python_provide python3-%{library}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  git-core
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-mock
BuildRequires:  python3-fixtures
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-os-client-config
BuildRequires:  python3-openstacksdk
BuildRequires:  python3-requests
BuildRequires:  python3-stevedore
BuildRequires:  python3-cliff
BuildRequires:  python3-requests-mock
BuildRequires:  python3-simplejson

Requires:   python3-pbr >= 2.0.0
Requires:   python3-keystoneauth1 >= 3.14.0
Requires:   python3-openstacksdk >= 0.15.0
Requires:   python3-oslo-i18n >= 3.15.3
Requires:   python3-oslo-utils >= 3.33.0
Requires:   python3-stevedore >= 1.20.0
Requires:   python3-cliff >= 3.2.0
Requires:   python3-simplejson >= 3.5.1

%description -n python3-%{library}
%{common_desc}

%package -n python3-%{library}-tests
Summary:    OpenStack osc-lib library tests
%{?python_provide:%python_provide python3-%{library}-tests}

Requires:   python3-%{library} = %{version}-%{release}
Requires:   python3-fixtures
Requires:   python3-mock
Requires:   python3-stestr
Requires:   python3-testtools
Requires:   python3-requests-mock

%description -n python3-%{library}-tests
%{common_desc}

This package contains the osc-lib library test files.

%if 0%{?with_doc}
%package -n python-%{library}-doc
Summary:    OpenStack osc-lib library documentation

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme
BuildRequires: python3-sphinxcontrib-apidoc

%description -n python-%{library}-doc
%{common_desc}

This package contains the documentation.
%endif

%description
%{common_desc}


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{library}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
export PYTHONPATH=.
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
PYTHON=%{__python3} stestr run

%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.egg-info
%exclude %{python3_sitelib}/%{module}/tests

%files -n python3-%{library}-tests
%license LICENSE
%{python3_sitelib}/%{module}/tests

%if 0%{?with_doc}
%files -n python-%{library}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 2.6.2-1
- Update to upstream version 2.6.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 2.5.0-2
- Rebuilt for Python 3.11

* Mon May 23 2022 Joel Capitao <jcapitao@redhat.com> 2.5.0-1
- Update to upstream version 2.5.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Alfredo Moralejo <amoralej@redhat.com> - 2.3.1-3
- skip failing unit test with python 3.10.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.1-2
- Rebuilt for Python 3.10

* Wed Mar 17 2021 Joel Capitao <jcapitao@redhat.com> 2.3.1-1
- Update to upstream version 2.3.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 2.2.1-2
- Update to upstream version 2.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 2.0.0-1
- Update to upstream version 2.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14.1-5
- Rebuilt for Python 3.9

* Fri Mar 13 2020 Alfredo Moralejo <amoralej@redhat.com> - 1.14.1-4
- Replace assertItemsEqual with assertCountEqual

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.14.1-2
- Update to upstream version 1.14.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Alfredo Moralejo <amoralej@lists.rdoproject.org> 1.12.1-2
- Remove osprofile as requirement for tests subpackage.

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 1.12.1-1
- Update to 1.12.1

