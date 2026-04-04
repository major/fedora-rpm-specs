%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global sname zaqarclient

%global common_desc %{expand
Python client to Zaqar messaging service API v1}

Name:           python-zaqarclient
Version:        4.4.0
Release:        %autorelease
Summary:        Client Library for OpenStack Zaqar Queueing API

License:        Apache-2.0
URL:            http://wiki.openstack.org/zaqar
Source0:        https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

BuildRequires:  python3-devel
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}

%package -n python3-%{sname}
Summary:        Client Library for OpenStack Zaqar Queueing API


%description -n python3-%{sname}
%{common_desc}


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup  -n python_%{sname}-%{version}

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
    test-requirements.txt doc/requirements.txt


%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l %{sname}


%check
%tox -e %{default_toxenv}


%files -n python3-%{sname} -f %{pyproject_files}
%doc README.rst ChangeLog examples
%license LICENSE


%changelog
%autochangelog
