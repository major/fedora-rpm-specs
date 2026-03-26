%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff
%global sources_gpg 1

%global sname ironicclient

%global common_desc A python and command line client library for Ironic

Name:           python-ironicclient
Version:        6.0.0
Release:        %autorelease
Summary:        Python client for Ironic

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/python-%{sname}
Source0:        https://tarballs.openstack.org/python-%{sname}/python_%{sname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/python-%{sname}/python_%{sname}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# Tests require
# https://bugzilla.redhat.com/show_bug.cgi?id=2450758
BuildRequires:  python3-osc-lib-tests

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}

%package -n python3-%{sname}
Summary:        Python client for Ironic

Requires:       xorriso
Suggests:       python3-openstackclient


%description -n python3-%{sname}
%{common_desc}


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{sname}-%{version}

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^mypy[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
    -e "/^tempest[[:space:]]*[><=]/d" \
    test-requirements.txt doc/requirements.txt


%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l ironicclient


%check
%tox


%files -n python3-%{sname} -f %{pyproject_files}
%doc ChangeLog README.rst
%license LICENSE
%{_bindir}/baremetal


%changelog
%autochangelog
