%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global sname keystoneclient
%global with_doc 1

%global common_desc %{expand:
Client library and command line utility for interacting with Openstack
Identity API.}


Name:       python-keystoneclient
Epoch:      1
Version:    5.8.0
Release:    %autorelease
Summary:    Client library for OpenStack Identity API
License:    Apache-2.0
URL:        https://launchpad.net/python-keystoneclient
Source0:    https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires: /usr/bin/openssl


%description
%{common_desc}


%package -n python3-%{sname}
Summary:    Client library for OpenStack Identity API

BuildRequires: python3-devel
BuildRequires: git-core
# keyring is a optional dep but we are maintataining as default for backwards
# compatibility
Requires: python3-keyring >= 5.5.1


%description -n python3-%{sname}
%{common_desc}


%package -n python3-%{sname}-tests
Summary:  Python API and CLI for OpenStack Keystone (tests)

Requires:  python3-%{sname} = %{epoch}:%{version}-%{release}
#Requires:  python3-fixtures
#Requires:  python3-oauthlib
#Requires:  python3-oslotest
#Requires:  python3-stestr
#Requires:  python3-testtools
#Requires:  python3-testresources
#Requires:  python3-testscenarios
#Requires:  python3-requests-mock
#Requires:  python3-lxml


%description -n python3-%{sname}-tests
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: Documentation for OpenStack Keystone API client


%description -n python-%{sname}-doc
%{common_desc}
%endif


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{sname}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

# Disable warnint-is-error in doc build
sed -i '/sphinx-build/ s/-W//' tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^tempest[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^bandit[[:space:]]*[!><=]/d" \
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

%pyproject_save_files keystoneclient
sed -i '\@/keystonclient/tests\(/.*\)\?$@d' %{pyproject_files}

%if 0%{?with_doc}
# Build HTML docs
# Disable warning-is-error as intersphinx extension tries
# to access external network and fails.
%tox -e docs
# Drop intersphinx downloaded file objects.inv to avoid rpmlint warning
rm -fr doc/build/html/objects.inv
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif


%check
%tox -e %{default_toxenv} -- -- --exclude-regex '^.*test_cms.*'


%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%exclude %{python3_sitelib}/%{sname}/tests


%if 0%{?with_doc}
%files -n python-%{sname}-doc
%doc doc/build/html
%license LICENSE
%endif


%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests


%changelog
%autochangelog
