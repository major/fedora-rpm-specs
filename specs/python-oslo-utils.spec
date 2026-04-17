%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff
%global pypi_name oslo.utils
%global pkg_name oslo-utils
%global with_doc 1

%global common_desc %{expand:
The OpenStack Oslo Utility library.
* Documentation: http://docs.openstack.org/developer/oslo.utils
* Source: http://git.openstack.org/cgit/openstack/oslo.utils
* Bugs: http://bugs.launchpad.net/oslo}


Name:           python-oslo-utils
Version:        10.0.1
Release:        %autorelease
Summary:        OpenStack Oslo Utility library

License:        Apache-2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/oslo_utils-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/oslo_utils-%{version}.tar.gz.asc
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


%package -n python3-%{pkg_name}
Summary:    OpenStack Oslo Utility library

BuildRequires:  python3-devel
BuildRequires:  qemu-img

Requires:       python-%{pkg_name}-lang = %{version}-%{release}


%description -n python3-%{pkg_name}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Utility library


%description -n python-%{pkg_name}-doc
Documentation for the Oslo Utility library.
%endif


%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Utility library

Requires: python3-%{pkg_name} = %{version}-%{release}


%description -n python3-%{pkg_name}-tests
%{common_desc_tests}

Tests for the Oslo Utility library.


%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo utils library


%description -n python-%{pkg_name}-lang
Translation files for Oslo utils library


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n oslo_utils-%{version} -S git


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
# we consume zoneinfo from stdlibg instead of tzdata
sed -i -e '/tzdata.*/d' test-requirements.txt requirements.txt

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^eventlet[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt


%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel

%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo} doc/build/html/objects.inv
%endif


%install
%pyproject_install

# Generate i18n files
python3 setup.py compile_catalog -d %{buildroot}%{python3_sitelib}/oslo_utils/locale --domain oslo_utils


# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_utils/locale/*/LC_*/oslo_utils*po
rm -f %{buildroot}%{python3_sitelib}/oslo_utils/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_utils/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_utils --all-name


%check
%if 0%{?fedora} || 0%{?epel} || 0%{?eln}
# eventlet is not yet supported on python 3.13 and it's not used in openstack clients
rm oslo_utils/tests/test_eventletutils.py
%endif
%tox -e %{default_toxenv} -- -- --exclude-regex '(oslo_utils.tests.test_netutils.NetworkUtilsTest.test_is_valid_ip)'


%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_utils
%{python3_sitelib}/*.dist-info
%exclude %{python3_sitelib}/oslo_utils/tests


%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif


%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_utils/tests


%files -n python-%{pkg_name}-lang -f oslo_utils.lang
%license LICENSE


%changelog
%autochangelog
