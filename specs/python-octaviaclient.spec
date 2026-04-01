%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global with_doc 0

%global pypi_name octaviaclient

%global common_desc %{expand:
Client for OpenStack Octavia (Load Balancer as a Service)}

Name:           python-%{pypi_name}
Version:        3.13.0
Release:        %autorelease
Summary:        Client for OpenStack Octavia (Load Balancer as a Service)

License:        Apache-2.0
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://tarballs.openstack.org/%{name}/python_%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:      https://tarballs.openstack.org/%{name}/python_%{pypi_name}-%{version}.tar.gz.asc
Source102:      https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n     python3-%{pypi_name}
Summary:        Client for OpenStack Octavia (Load Balancer as a Service)


%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for OpenStack Octavia Client


%description -n python-%{pypi_name}-doc
Documentation for the client library for interacting with Openstack
Octavia API.
%endif


# Test package
%package -n python3-%{pypi_name}-tests
Summary:        OpenStack Octavia client tests

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       python3-fixtures >= 1.3.1
Requires:       python3-testtools
Requires:       python3-subunit >= 0.0.18
Requires:       python3-osc-lib >= 1.14.1
Requires:       python3-osc-lib-tests
Requires:       python3-oslo-log
Requires:       python3-openstackclient
Requires:       python3-stestr
Requires:       python3-webob >= 1.2.3

%description -n python3-%{pypi_name}-tests
OpenStack Octavia client tests

This package contains the example client test files.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{pypi_name}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i '/sphinx-build/ s/-W//' tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^bandit[[:space:]]*[!><=]/d" \
    -e "/^flake8-import-order[[:space:]]*[!><=]/d" \
    -e "/^doc8[[:space:]]*[!><=]/d" \
    -e "/^pylint[[:space:]]*[!><=]/d" \
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
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}


%check
rm -f ./octaviaclient/tests/unit/test_hacking.py
%tox -e %{default_toxenv}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%exclude %{python3_sitelib}/%{pypi_name}/tests


%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/%{pypi_name}/tests


%changelog
%autochangelog
