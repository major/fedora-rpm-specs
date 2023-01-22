%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

%global pypi_name oslo.middleware
%global pkg_name oslo-middleware
%global common_desc \
The OpenStack Oslo Middleware library. \
Oslo middleware library includes components that can be injected into wsgi \
pipelines to intercept request/response flows. The base class can be \
enhanced with functionality like add/delete/modification of http headers \
and support for limiting size/connection etc.

Name:           python-oslo-middleware
Version:        5.0.0
Release:        7%{?dist}
Summary:        OpenStack Oslo Middleware library

License:        ASL 2.0
URL:            https://opendev.org/openstack/oslo.middleware
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
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
Summary:        OpenStack Oslo Middleware library
%py_provides python3-%{pkg_name}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# for docs build
BuildRequires:  git-core
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-context
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-oslo-utils
# Required for testing
BuildRequires:  python3-bcrypt
BuildRequires:  python3-fixtures
BuildRequires:  python3-hacking
BuildRequires:  python3-jinja2
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-statsd
BuildRequires:  python3-testtools
BuildRequires:  python3-webob
# Required to compile translation files
BuildRequires:  python3-babel

Requires:       python3-pbr
Requires:       python3-bcrypt >= 3.1.3
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-jinja2
Requires:       python3-oslo-config >= 2:5.2.0
Requires:       python3-oslo-context >= 2.19.2
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-statsd
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-webob >= 1.8.0
Requires:       python-%{pkg_name}-lang = %{version}-%{release}

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Middleware library
Group:      Documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-%{pkg_name}-doc
Documentation for the Oslo Middleware library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Middleware library

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-fixtures
Requires:  python3-hacking
Requires:  python3-oslotest
Requires:  python3-testtools

%description -n python3-%{pkg_name}-tests
Tests for the Oslo Middleware library.

%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo middleware library

%description -n python-%{pkg_name}-lang
Translation files for Oslo middleware library

%description
%{common_desc}

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
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif
# Generate i18n files
python3 setup.py compile_catalog -d build/lib/oslo_middleware/locale --domain oslo_middleware

%install
%{py3_install}

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_middleware/locale/*/LC_*/oslo_middleware*po
rm -f %{buildroot}%{python3_sitelib}/oslo_middleware/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_middleware/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_middleware --all-name

%check
python3 setup.py test

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_middleware
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/oslo_middleware/tests/

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_middleware/tests/

%files -n python-%{pkg_name}-lang -f oslo_middleware.lang
%license LICENSE

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 5.0.0-6
- Fixes issues on packaging guidelines

* Wed Nov 09 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 5.0.0-5
- Fixes issues on packaging guidelines

* Tue Nov 08 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 5.0.0-4
- Fixes issues on packaging guidelines

* Mon Oct 31 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 5.0.0-3
- Fixes issues on packaging guidelines

* Fri Oct 28 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 5.0.0-2
- Fixes issues on packaging guidelines

* Wed Oct 26 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 5.0.0-1
- Update 5.0.0

* Wed Sep 29 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 4.3.0-2
- Fixes issues on packaging guidelines

* Wed Aug 11 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 4.3.0-1
- Un-retired and update to 4.3.0

* Thu Jan 31 2019 Yatin Karel <ykarel@redhat.com>  - 3.34.0-2
- Drop python2 sub packages (#1634863)

* Sat Feb 10 2018 RDO <dev@lists.rdoproject.org> 3.34.0-1
- Update to 3.34.0

