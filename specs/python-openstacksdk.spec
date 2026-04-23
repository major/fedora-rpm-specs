# Disable docs until bs4 package is available
%global with_doc 0

%global pypi_name openstacksdk

%global common_desc \
A collection of libraries for building applications to work with OpenStack \
clouds.

%global common_desc_tests %{expand:
A collection of libraries for building applications to work with OpenStack
clouds - test files}

Name:           python-%{pypi_name}
Version:        4.10.0
Release:        %autorelease
Summary:        An SDK for building applications to work with OpenStack

License:        Apache-2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.io/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# https://review.opendev.org/c/openstack/openstacksdk/+/985641
Patch0:         0001-fix-hashlib-ValueError-message-check-for-py3.15.patch

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel

%description
%{common_desc}


%package -n python3-%{pypi_name}
Summary:        An SDK for building applications to work with OpenStack


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
%description -n python-%{pypi_name}-doc
A collection of libraries for building applications to work with OpenStack
clouds - documentation.
%endif


%prep
%autosetup -n %{pypi_name}-%{version} -S git -p 1
# This unit test requires python-prometheus, which is optional and not needed
rm -f openstack/tests/unit/test_stats.py

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^hacking[[:space:]]*[><=]/d" \
    -e "/^statsd[[:space:]]*[><=]/d" \
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

%pyproject_save_files -l openstack


%check
rm -f ./openstack/tests/unit/test_hacking.py
%tox -e %{default_toxenv} -- -- --exclude-regex '(openstack.tests.unit.test_connection.TestConnection.test_create_unknown_proxy|openstack.tests.unit.test_missing_version.TestMissingVersion.test_unsupported_version_override)'


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst ChangeLog
%license LICENSE
%{_bindir}/openstack-inventory
%exclude %{python3_sitelib}/openstack/tests


%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/openstack/tests


%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
