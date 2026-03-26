# There is circular dependency with this requiring stestr requiring cliff requiring stevedore
%bcond_with bootstrap

%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global common_desc Manage dynamic plugins for Python applications

Name:           python-stevedore
Version:        5.7.0
Release:        %autorelease
Summary:        Manage dynamic plugins for Python applications

Group:          Development/Languages
License:        Apache-2.0
URL:            https://github.com/openstack/stevedore
Source0:        https://tarballs.openstack.org/stevedore/stevedore-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source1:        https://tarballs.openstack.org/stevedore/stevedore-%{version}.tar.gz.asc
Source2:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif
BuildRequires:  python3-devel
BuildRequires:  git-core

%description
%{common_desc}


%package -n python3-stevedore
Summary:        Manage dynamic plugins for Python applications
Group:          Development/Libraries


%description -n python3-stevedore
%{common_desc}


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q -n stevedore-%{version}

# Remove empty file
rm stevedore/tests/extension_unimportable.py

sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt


%generate_buildrequires
%if %{with bootstrap}
%pyproject_buildrequires
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel


%check
%if %{with bootstrap}
%pyproject_check_import -e stevedore.example* -e stevedore.sphinxext -e stevedore.tests.test_sphinxext
%else
%tox
%endif


%install
%pyproject_install

%pyproject_save_files -l stevedore


%files -n python3-stevedore -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
