
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

# Disable docs until bs4 package is available
%global with_doc 0

%global pypi_name openstacksdk

%global common_desc \
A collection of libraries for building applications to work with OpenStack \
clouds.

%global common_desc_tests \
A collection of libraries for building applications to work with OpenStack \
clouds - test files

Name:           python-%{pypi_name}
Version:        0.101.0
Release:        1%{?dist}
Summary:        An SDK for building applications to work with OpenStack

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.io/packages/source/o/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        An SDK for building applications to work with OpenStack
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-appdirs
BuildRequires:  python3-requestsexceptions
BuildRequires:  python3-munch
BuildRequires:  python3-jmespath
BuildRequires:  python3-jsonschema
BuildRequires:  python3-os-service-types

# Test requirements
%if (0%{?fedora} && 0%{?fedora} < 32) || (0%{?rhel} && 0%{?rhel} < 9)
BuildRequires:  python3-importlib-metadata
%endif
BuildRequires:  python3-iso8601 >= 0.1.11
BuildRequires:  python3-jsonpatch >= 1.16
BuildRequires:  python3-subunit
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-config
BuildRequires:  python3-stestr
BuildRequires:  python3-mock
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-requests-mock
BuildRequires:  python3-dogpile-cache
BuildRequires:  python3-ddt
BuildRequires:  python3-decorator
BuildRequires:  python3-netifaces

Requires:       python3-cryptography >= 2.7
%if (0%{?fedora} && 0%{?fedora} < 32) || (0%{?rhel} && 0%{?rhel} < 9)
Requires:       python3-importlib-metadata >= 1.7.0
%endif
Requires:       python3-jsonpatch >= 1.16
Requires:       python3-keystoneauth1 >= 3.18.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-appdirs
Requires:       python3-requestsexceptions >= 1.2.0
Requires:       python3-munch
Requires:       python3-jmespath
Requires:       python3-iso8601
Requires:       python3-os-service-types >= 1.7.0
Requires:       python3-dogpile-cache
Requires:       python3-decorator
Requires:       python3-netifaces
Requires:       python3-yaml >= 3.13

%description -n python3-%{pypi_name}
%{common_desc}

%package -n python3-%{pypi_name}-tests
Summary:        An SDK for building applications to work with OpenStack - test files

Requires: python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
%{common_desc_tests}

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        An SDK for building applications to work with OpenStack - documentation
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
A collection of libraries for building applications to work with OpenStack
clouds - documentation.
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the requirements
rm -rf {,test-}requirements.txt
# This unit test requires python-prometheus, which is optional and not needed
rm -f openstack/tests/unit/test_stats.py

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
rm -f ./openstack/tests/unit/test_hacking.py
export OS_STDOUT_CAPTURE=true
export OS_STDERR_CAPTURE=true
export OS_TEST_TIMEOUT=20
# FIXME(jpena) we are skipping some unit tests due to
# https://storyboard.openstack.org/#!/story/2005677
PYTHON=python3 stestr-3 --test-path ./openstack/tests/unit run --black-regex '(test_wait_for_task_.*|.*TestOsServiceTypesVersion.*|.*test_timeout_and_failures_not_fail.*)'

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/openstack-inventory
%{python3_sitelib}/openstack
%{python3_sitelib}/%{pypi_name}-*.egg-info
%exclude %{python3_sitelib}/openstack/tests

%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/openstack/tests

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 0.101.0-1
- Update to upstream version 0.101.0

* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 0.101.0-1
- Update to upstream version 0.101.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.61.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Alfredo Moralejo <amoralej@redhat.com> - 0.61.0-3
- Replace deprecated inspect.getargspec call

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.61.0-2
- Rebuilt for Python 3.11

* Mon May 23 2022 Joel Capitao <jcapitao@redhat.com> 0.61.0-1
- Update to upstream version 0.61.0

* Wed May 18 2022 Joel Capitao <jcapitao@redhat.com> 0.61.0-1
- Update to upstream version 0.61.0

* Wed Apr 06 2022 Karolina Kula <kkula@redhat.com> - 0.55.1-1
- Update to upstream version 0.55.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.55.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.55.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Javier Peña <jpena@redhat.com> - 0.55.0-3
- Fix auto_spec arguments passed to mock
- Skip unit tests related to dogpile.cache

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.55.0-2
- Rebuilt for Python 3.10

* Wed Mar 17 2021 Joel Capitao <jcapitao@redhat.com> 0.55.0-1
- Update to upstream version 0.55.0

* Mon Feb 08 2021 Javier Peña <jpena@redhat.comg> - 0.50.0-3
- Fix build on Python 3.10 (bz#1926361)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 RDO <dev@lists.rdoproject.org> 0.50.0-1
- Update to 0.50.0

* Fri Sep 18 2020 RDO <dev@lists.rdoproject.org> 0.49.0-1
- Update to 0.49.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 0.46.0-1
- Update to upstream version 0.46.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-5
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Javier Peña <jpena@redhat.com> - 0.36.0-4
- Add patch to replace assertItemsEqual with assertCountEqual (bz#1809970)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Alfredo Moralejo <amoralej@redhat.com> 0.36.0-2
- Update to upstream version 0.36.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.27.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.27.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 RDO <dev@lists.rdoproject.org> 0.27.0-1
- Update to 0.27.0

* Tue Mar 12 2019 RDO <dev@lists.rdoproject.org> 0.26.0-1
- Update to 0.26.0

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 0.25.0-1
- Update to 0.25.0
