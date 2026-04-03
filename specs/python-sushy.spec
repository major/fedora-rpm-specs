%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global with_doc 1
%global sname sushy

%global common_desc %{expand:
Sushy is a Python library to communicate with Redfish based systems (http://redfish.dmtf.org)}

%global common_desc_tests Tests for Sushy

Name: python-%{sname}
Version: 5.10.0
Release: %autorelease
Summary: Sushy is a Python library to communicate with Redfish based systems
License: Apache-2.0
URL: http://launchpad.net/%{sname}/

Source0: http://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildRequires: git-core
BuildRequires: python3-devel

BuildArch: noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n python3-%{sname}
Summary: Sushy is a Python library to communicate with Redfish based systems


%description -n python3-%{sname}
%{common_desc}


%package -n python3-%{sname}-tests
Summary: Sushy tests
Requires: python3-%{sname} = %{version}-%{release}


%description -n python3-%{sname}-tests
%{common_desc_tests}

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: Sushy documentation


%description -n python-%{sname}-doc
Documentation for Sushy
%endif


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{sname}-%{version} -S git


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
#sed -i /^minversion.*/d tox.ini
#sed -i /^requires.*virtualenv.*/d tox.ini


sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
    test-requirements.txt doc/requirements.txt

# Automatic BR generation
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


%check
%tox -e %{default_toxenv}

%install
%pyproject_install

%pyproject_save_files -l %{sname}


%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%exclude %{python3_sitelib}/%{sname}/tests


%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests


%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif


%changelog
%autochangelog
