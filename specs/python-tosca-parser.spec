%global pypi_name tosca-parser

Name:           python-%{pypi_name}
Version:        2.12.0
Release:        %autorelease
Summary:        Parser for TOSCA Simple Profile in YAML

License:        Apache-2.0
URL:            https://github.com/openstack/tosca-parser
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The TOSCA Parser is an OpenStack project and licensed under Apache 2.
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.

%package -n python3-%{pypi_name}
Summary:        Parser for TOSCA Simple Profile in YAML
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 1.3
BuildRequires:  python3-PyYAML
BuildRequires:  python3-setuptools
# Required for testing
BuildRequires:  python3-six
BuildRequires:  python3-dateutil
BuildRequires:  python3-cliff
BuildRequires:  python3-fixtures
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildRequires:  python3-testscenarios
BuildRequires:  python3-oslotest
BuildRequires:  python3-subunit
BuildRequires:  python3-stestr
# Required for doc
BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

Requires:       python3-PyYAML
Requires:       python3-cliff
Requires:       python3-dateutil
Requires:       python3-requests
Requires:       python3-stevedore

%description -n python3-%{pypi_name}
The TOSCA Parser is an OpenStack project and licensed under Apache 2.
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.


%package -n python-%{pypi_name}-doc
Summary:        Parser for TOSCA Simple Profile in YAML - documentation
Provides:  python3-%{pypi_name}-doc = %{version}-%{release}
Obsoletes: python3-%{pypi_name}-doc < %{version}-%{release}

%description -n python-%{pypi_name}-doc
The TOSCA Parser is an OpenStack project and licensed under Apache 2.
This package contains its documentation


%prep
%setup -q -n %{pypi_name}-%{version}
# Let's manage requirements using rpm.
rm -f *requirements.txt

%build
%py3_build
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%check
# Ignore test results for now, they are trying to access external URLs
# which are not accessible in Koji
PYTHON=python3 %{__python3} setup.py test || true
# Cleanup test repository
rm -rf .testrepository

%install
%{py3_install}

# Set executable permission on test scripts
find %{buildroot}/%{python3_sitelib}/toscaparser/tests -name '*.sh' -execdir chmod +x '{}' \;
# Fix shebang on some test scripts
find %{buildroot}/%{python3_sitelib}/toscaparser/tests -name '*.py' -exec sed -i 's/^#!\/usr\/bin\/python/#!\/usr\/bin\/python3/' {} \;

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/tosca-parser
%{python3_sitelib}/toscaparser
%{python3_sitelib}/tosca_parser-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html README.rst
%license LICENSE

%changelog
%autochangelog
