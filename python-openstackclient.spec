%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

# Command name
%global cname openstack

# library name
%global sname %{cname}client

%global with_doc 1

%global common_desc \
python-%{sname} is a unified command-line client for the OpenStack APIs. \
It is a thin wrapper to the stock python-*client modules that implement the \
actual REST API client actions.

Name:             python-%{sname}
Version:          6.0.0
Release:          2%{?dist}
Summary:          OpenStack Command-line Client

License:          ASL 2.0
URL:              http://launchpad.net/%{name}
Source0:          https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:    git-core

%description
%{common_desc}

%package -n python3-%{sname}
Summary:    OpenStack Command-line Client
%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-pbr
BuildRequires:    python3-six
BuildRequires:    python3-oslo-i18n
BuildRequires:    python3-oslo-utils
BuildRequires:    python3-requests
BuildRequires:    python3-keystoneclient
BuildRequires:    python3-novaclient
BuildRequires:    python3-cinderclient
BuildRequires:    python3-mock
BuildRequires:    python3-os-client-config
BuildRequires:    python3-cliff
BuildRequires:    python3-simplejson
BuildRequires:    python3-requests-mock

# Required to compile translation files
BuildRequires:    python3-babel
# Required for unit tests
BuildRequires:    python3-stestr
BuildRequires:    python3-osc-lib-tests
BuildRequires:    python3-fixtures
BuildRequires:    python3-oslotest
BuildRequires:    python3-reno
BuildRequires:    python3-requestsexceptions
BuildRequires:    python3-openstacksdk
BuildRequires:    python3-ddt

Requires:         python3-pbr
Requires:         python3-openstacksdk >= 0.61.0
Requires:         python3-oslo-i18n >= 3.15.3
Requires:         python3-oslo-utils >= 3.33.0
Requires:         python3-keystoneclient >= 1:3.22.0
Requires:         python3-novaclient >= 1:17.0.0
Requires:         python3-cinderclient >= 3.3.0
Requires:         python3-neutronclient >= 6.7.0
Requires:         python3-osc-lib >= 2.3.0
Requires:         python3-cliff

Requires:         python-%{sname}-lang = %{version}-%{release}
Requires:         python3-stevedore >= 2.0.1
Requires:         python3-iso8601 >= 0.1.11

# Dependency for auto-completion
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:         bash-completion
%endif

%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary:          Documentation for OpenStack Command-line Client

BuildRequires:    python3-sphinx
BuildRequires:    python3-openstackdocstheme
BuildRequires:    python3-sphinxcontrib-apidoc

Requires: python3-%{sname} = %{version}-%{release}

%description -n python-%{sname}-doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%package  -n python-%{sname}-lang
Summary:   Translation files for Openstackclient

%description -n python-%{sname}-lang
Translation files for Openstackclient

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

# We handle requirements ourselves, pkg_resources only bring pain
rm -rf *requirements.txt

# (TODO) Remove this sed after fix is merged upstream
# https://review.opendev.org/c/openstack/python-openstackclient/+/808079
# Replace assertItemsEqual by assertCountEqual in test_volume_messages.py file
sed -i 's/assertItemsEqual/assertCountEqual/g' ./openstackclient/tests/unit/volume/v3/test_volume_message.py

%build
%{py3_build}

# Generate i18n files
%{__python3} setup.py compile_catalog -d build/lib/%{sname}/locale --domain openstackclient

%install
%{py3_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s %{cname} %{buildroot}%{_bindir}/%{cname}-3

%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build -b html doc/source doc/build/html
sphinx-build -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/%{cname}.1 %{buildroot}%{_mandir}/man1/%{cname}.1

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo doc/build/html/.htaccess
%endif

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/%{sname}/locale/*/LC_*/%{sname}*po
rm -f %{buildroot}%{python3_sitelib}/%{sname}/locale/*pot
mv %{buildroot}%{python3_sitelib}/%{sname}/locale %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{python3_sitelib}/%{sname}/locale

# Find language files
%find_lang %{sname} --all-name

%post -n python3-%{sname}
mkdir -p /etc/bash_completion.d
openstack complete | sed -n '/_openstack/,$p' > /etc/bash_completion.d/osc.bash_completion

%check
%if %{lua:print(rpm.vercmp('%{version}', '6.0.0'));} > 0
export PYTHON=%{__python3}
stestr run
%endif

%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/%{cname}
%{_bindir}/%{cname}-3
%{python3_sitelib}/%{sname}
%{python3_sitelib}/*.egg-info
%if 0%{?with_doc}
%{_mandir}/man1/%{cname}.1*

%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python-%{sname}-lang -f %{sname}.lang
%license LICENSE

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-1
- Update to upstream version 6.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 5.8.0-2
- Rebuilt for Python 3.11

* Mon May 23 2022 Joel Capitao <jcapitao@redhat.com> 5.8.0-1
- Update to upstream version 5.8.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.5.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 RDO <dev@lists.rdoproject.org> 5.5.0-1
- Update to 5.5.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 5.4.0-2
- Update to upstream version 5.4.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 5.2.0-1
- Update to upstream version 5.2.0

* Mon Jun 01 2020 Alfredo Moralejo <amoralej@redhat.com> - 4.0.0-4
- Fix unit tests

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Alfredo Moralejo <amoralej@redhat.com> 4.0.0-1
- Update to upstream version 4.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.18.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.18.0-4
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Alfredo Moralejo <amoralej@redhat.com> - 3.18.0-3
- Remove unneeded osprofiler as BR.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 3.18.0-1
- Update to 3.18.0

