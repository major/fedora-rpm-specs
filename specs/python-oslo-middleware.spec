%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif

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
Version:        6.0.0
Release:        4%{?dist}
Summary:        OpenStack Oslo Middleware library

License:        Apache-2.0
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
BuildRequires:  pyproject-rpm-macros
# for docs build
BuildRequires:  git-core
Requires:       python-%{pkg_name}-lang = %{version}-%{release}

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Middleware library
Group:      Documentation

%description -n python-%{pkg_name}-doc
Documentation for the Oslo Middleware library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Middleware library

Requires:  python3-%{pkg_name} = %{version}-%{release}

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


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%install
%pyproject_install

%if 0%{?with_doc}
# generate html docs
PYTHONPATH="%{buildroot}/%{python3_sitelib}"
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif
# Generate i18n files
python3 setup.py compile_catalog -d %{buildroot}%{python3_sitelib}/oslo_middleware/locale --domain oslo_middleware

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_middleware/locale/*/LC_*/oslo_middleware*po
rm -f %{buildroot}%{python3_sitelib}/oslo_middleware/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_middleware/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_middleware --all-name

%check
%tox -e %{default_toxenv}

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_middleware
%{python3_sitelib}/*.dist-info
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Python Maint <python-maint@redhat.com> - 6.0.0-2
- Rebuilt for Python 3.13

* Tue Feb 20 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 6.0.0-1
- Update 6.0.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 5.1.1-2
- Switches to pyproject-rpm-macros on Python-3.12

* Fri Feb 24 2023 Hirotaka Wakabayashi <hiwkby@yahoo.com>  - 5.1.1-1
- Update 5.1.1

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

