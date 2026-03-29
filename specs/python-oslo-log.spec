%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global with_doc 1
%global pypi_name oslo.log
%global pkg_name oslo-log

%global common_desc %{expand:
OpenStack logging configuration library provides standardized configuration
for all openstack projects. It also provides custom formatters, handlers and
support for context specific logging (like resource id’s etc).}


Name:           python-oslo-log
Version:        8.1.0
Release:        %autorelease
Summary:        OpenStack Oslo Log library

License:        Apache-2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/oslo_log-%{version}.tar.gz
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/oslo_log-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}


%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo Log library

BuildRequires:  python3-devel
BuildRequires:  git-core
Requires:       python-%{pkg_name}-lang = %{version}-%{release}

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Log handling library


%description -n python-%{pkg_name}-doc
Documentation for the Oslo Log handling library.
%endif


%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Log handling library
Requires:   python3-%{pkg_name} = %{version}-%{release}


%description -n python3-%{pkg_name}-tests
%{common_desc1}

Tests for the Oslo Log handling library.


%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo log library


%description -n python-%{pkg_name}-lang
Translation files for Oslo log library

%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n oslo_log-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^eventlet[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt

# see check section below
sed -i '\|eventlet\.hubs\.get_hub()|d' tox.ini

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
# This invocation is os of course deprecated, I think the correct thing to do may be:
# pybabel compile -d %{buildroot}%{python3_sitelib}/oslo_log/locale -D oslo_log
# which will need a BR on babel.
python3 setup.py compile_catalog -d %{buildroot}%{python3_sitelib}/oslo_log/locale --domain oslo_log

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_log/locale/*/LC_*/oslo_log*po
rm -f %{buildroot}%{python3_sitelib}/oslo_log/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_log/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_log --all-name


%check
# skipping tests using eventlet as it's not available for python 3.13 and this functionality
# in oslo.log is unused in the client packages used in Fedora
# More genrally oslo.log is deprecating use of eventlet.
rm oslo_log/tests/unit/test_pipe_mutex.py
%tox -e %{default_toxenv}


%files -n python3-%{pkg_name}
%doc README.rst ChangeLog AUTHORS
%license LICENSE
%{python3_sitelib}/oslo_log
%{python3_sitelib}/*.dist-info
%{_bindir}/convert-json
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
%autochangelog
