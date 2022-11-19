%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1
%global pypi_name oslo.log
%global pkg_name oslo-log

%global common_desc \
OpenStack logging configuration library provides standardized configuration \
for all openstack projects. It also provides custom formatters, handlers and \
support for context specific logging (like resource id’s etc).

%global common_desc1 \
Tests for the Oslo Log handling library.

Name:           python-oslo-log
Version:        5.0.0
Release:        1%{?dist}
Summary:        OpenStack Oslo Log library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
%if "%{version}" == "4.6.1"
# TODO(jcapitao): patch to be removed once https://review.opendev.org/c/openstack/oslo.log/+/828017
# is available in uc tag.
Patch0001:      0001-Use-project-when-logging-the-user-identity.patch
%endif
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo Log library
%{?python_provide:%python_provide python3-%{pkg_name}}
Obsoletes: python2-%{pkg_name} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  git-core
# Required for tests
BuildRequires:  python3-dateutil
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-context
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-subunit
BuildRequires:  python3-testtools
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
# Required to compile translation files
BuildRequires:  python3-babel
BuildRequires:  python3-inotify
BuildRequires:  python3-eventlet

Requires:       python3-pbr
Requires:       python3-dateutil
Requires:       python3-oslo-config >= 2:5.2.0
Requires:       python3-oslo-context >= 2.21.0
Requires:       python3-oslo-i18n >= 3.20.0
Requires:       python3-oslo-utils >= 3.36.0
Requires:       python3-oslo-serialization >= 2.25.0
Requires:       python3-debtcollector >= 1.19.0
Requires:       python3-inotify

Requires:       python-%{pkg_name}-lang = %{version}-%{release}

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Log handling library

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-utils

%description -n python-%{pkg_name}-doc
Documentation for the Oslo Log handling library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Log handling library

Requires:       python3-%{pkg_name} = %{version}-%{release}
Requires:       python3-mock
Requires:       python3-oslotest
Requires:       python3-oslo-config >= 2:5.2.0
Requires:       python3-subunit
Requires:       python3-testtools
Requires:       python3-testrepository
Requires:       python3-testscenarios

%description -n python3-%{pkg_name}-tests
%{common_desc1}

%description
%{common_desc}

%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo log library

%description -n python-%{pkg_name}-lang
Translation files for Oslo log library

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the dependencies
rm -rf {test-,}requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
PYTHONPATH=. sphinx-build-3 -W -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif
# Generate i18n files
python3 setup.py compile_catalog -d build/lib/oslo_log/locale --domain oslo_log

%install
%{py3_install}
ln -s ./convert-json %{buildroot}%{_bindir}/convert-json-3

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_log/locale/*/LC_*/oslo_log*po
rm -f %{buildroot}%{python3_sitelib}/oslo_log/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_log/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_log --all-name

%check
python3 setup.py test

%files -n python3-%{pkg_name}
%doc README.rst ChangeLog AUTHORS
%license LICENSE
%{python3_sitelib}/oslo_log
%{python3_sitelib}/*.egg-info
%{_bindir}/convert-json
%{_bindir}/convert-json-3
%exclude %{python3_sitelib}/oslo_log/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_log/tests

%files -n python-%{pkg_name}-lang -f oslo_log.lang
%license LICENSE

%changelog
* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 5.0.0-1
- Update to upstream version 5.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 4.7.0-2
- Rebuilt for Python 3.11

* Mon May 23 2022 Joel Capitao <jcapitao@redhat.com> 4.7.0-1
- Update to upstream version 4.7.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 4.4.0-2
- Update to upstream version 4.4.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 4.1.1-1
- Update to upstream version 4.1.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.44.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.44.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 3.44.1-2
- Update to upstream version 3.44.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.42.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.42.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 3.42.3-1
- Update to 3.42.3

