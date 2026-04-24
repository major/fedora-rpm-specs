%global sources_gpg 1
%global sources_gpg_sign 0x30566c450e41d7c91e442dfb231f942f608ddeff

%global with_doc 1

%global pypi_name oslo.concurrency
%global pkg_name oslo-concurrency

%global common_desc %{expand:
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.}

%global common_desc2 %{expand:
Tests for the Oslo concurrency library.}

Name:           python-oslo-concurrency
Version:        7.4.1
Release:        %autorelease
Summary:        OpenStack Oslo concurrency library

License:        Apache-2.0
URL:            https://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/oslo_concurrency-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/oslo_concurrency-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo concurrency library
Requires:       python-%{pkg_name}-lang = %{version}-%{release}


%description -n python3-%{pkg_name}
%{common_desc}


%if 0%{?with_doc}
%package  -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo concurrency library
Group:      Documentation
%description -n python-%{pkg_name}-doc
Documentation for the Oslo concurrency library.
%endif


%package  -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo concurrency library

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-hacking
Requires:  python3-oslotest
Requires:  python3-fixtures
Requires:  python3-stestr


%description -n python3-%{pkg_name}-tests
%{common_desc2}


%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo concurrency library


%description -n python-%{pkg_name}-lang
Translation files for Oslo concurrency library


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n oslo_concurrency-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
#sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
#sed -i /^minversion.*/d tox.ini
#sed -i /^requires.*virtualenv.*/d tox.ini
%if 0%{?fedora}
sed -i "s/TEST_EVENTLET=.*/TEST_EVENTLET=1/" tox.ini
%endif


sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt


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

%pyproject_save_files -l oslo_concurrency

# Generate i18n files
python3 setup.py compile_catalog -d %{buildroot}%{python3_sitelib}/oslo_concurrency/locale --domain oslo_concurrency

%if 0%{?with_doc}
# generate html docs
PYTHONPATH="%{buildroot}/%{python3_sitelib}"
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_concurrency/locale/*/LC_*/oslo_concurrency*po
rm -f %{buildroot}%{python3_sitelib}/oslo_concurrency/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_concurrency/locale %{buildroot}%{_datadir}/locale
sed -i \
    -e' \|%{python3_sitelib}/oslo_concurrency/locale$|d' \
    -e '\|%{python3_sitelib}/oslo_concurrency/locale/|d' \
    %{pyproject_files}


# Find language files
%find_lang oslo_concurrency --all-name


%check
%tox -e %{default_toxenv}


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/lockutils-wrapper
%exclude %{python3_sitelib}/oslo_concurrency/tests


%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif


%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_concurrency/tests


%files -n python-%{pkg_name}-lang -f oslo_concurrency.lang
%license LICENSE

%changelog
%autochangelog
