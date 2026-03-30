%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

# we are excluding some runtime reqs from automatic generator
%global excluded_reqs tzdata
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif

%global pypi_name oslo.serialization
%global pkg_name oslo-serialization
%global with_doc 1

%global common_desc %{expand:
An OpenStack library for representing objects in transmittable and
storable formats.}

Name:           python-%{pkg_name}
Version:        5.9.1
Release:        %autorelease
Summary:        OpenStack oslo.serialization library

License:        Apache-2.0
URL:            https://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/oslo_serialization-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/oslo_serialization-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
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


%package -n python3-%{pkg_name}
Summary:        OpenStack oslo.serialization library


%description -n python3-%{pkg_name}
%{common_desc}


%package -n python3-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo serialization library
Requires:  python3-%{pkg_name} = %{version}-%{release}


%description -n python3-%{pkg_name}-tests
Tests for OpenStack Oslo serialization library


%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo serialization library

Requires:  python3-%{pkg_name} = %{version}-%{release}


%description -n python-%{pkg_name}-doc
Documentation for the Oslo serialization library.
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n oslo_serialization-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini


sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
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
# doc
%tox -e docs
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install


%check
export OS_TEST_PATH="./oslo_serialization/tests"
%tox -e %{default_toxenv}


%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_serialization
%{python3_sitelib}/*.dist-info
%exclude %{python3_sitelib}/oslo_serialization/tests


%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif


%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_serialization/tests


%changelog
%autochangelog
