%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global pypi_name oslo.metrics
%global pypi_name_under oslo_metrics
%global pkg_name oslo-metrics

%global common_desc %{expand:
The OpenStack Oslo Metrics library.
Oslo metrics API supports collecting metrics data from other Oslo
libraries and exposing the metrics data to monitoring system.}

Name:           python-oslo-metrics
Version:        0.15.1
Release:        %autorelease
Summary:        OpenStack Oslo Metrics library

License:        Apache-2.0
URL:            https://opendev.org/openstack/oslo.metrics
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name_under}-%{version}.tar.gz
%if 0%{?sources_gpg} == 1
Source101:      https://tarballs.openstack.org/%{pypi_name}/%{pypi_name_under}-%{version}.tar.gz.asc
Source102:      https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo Metrics library


%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Metrics library
Group:      Documentation


%description -n python-%{pkg_name}-doc
Documentation for the Oslo Metrics library.
%endif


%package -n python3-%{pkg_name}-tests
Summary:   Tests for the Oslo Metrics library
Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-oslotest


%description -n python3-%{pkg_name}-tests
Tests for the Oslo Metrics library.


%description
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name_under}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
#sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
#sed -i /^minversion.*/d tox.ini
#sed -i /^requires.*virtualenv.*/d tox.ini
sed -i '/sphinx-build/ s/-W//' tox.ini


sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
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
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l %{pypi_name_under}


%check
%tox -e %{default_toxenv}


%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/oslo-metrics
%exclude %{python3_sitelib}/oslo_metrics/tests/


%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif


%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_metrics/tests/


%changelog
%autochangelog
