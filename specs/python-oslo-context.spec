%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global pypi_name oslo.context
%global pkg_name oslo-context
%global with_doc 1

%global common_desc %{expand:
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.}

Name:           python-%{pkg_name}
Version:        6.3.0
Release:        %autorelease
Summary:        OpenStack Oslo Context library

License:        Apache-2.0
URL:            https://launchpad.net/oslo.context
Source0:        https://tarballs.openstack.org/%{pypi_name}/oslo_context-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/oslo_context-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

BuildRequires:  python3-devel

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core


%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo Context library


%description -n python3-%{pkg_name}
%{common_desc}


%package -n python3-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo context library

Requires:  python3-%{pkg_name} = %{version}-%{release}


%description -n python3-%{pkg_name}-tests
Tests for OpenStack Oslo context library


%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:        Documentation for the OpenStack Oslo context library


%description -n python-%{pkg_name}-doc
Documentation for the OpenStack Oslo context library.
%endif


%description
%{common_desc}


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n oslo_context-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^mypy[[:space:]]*[!><=]/d" \
    -e "/^bandit[[:space:]]*[!><=]/d" \
    -e "/^pre-commit[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt

%generate_buildrequires

%if 0%{?with_doc}
%pyproject_buildrequires -t -e docs
%else
%pyproject_buildrequires -t
%endif


%build
%pyproject_wheel


%if 0%{?with_doc}
%tox -e docs
rm -r doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l oslo_context


# The tests are not being loaded here, the testenvs environment
# never seems to run ... confused.
%check
%tox


%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%exclude %{python3_sitelib}/oslo_context/tests


%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif


%files -n python3-%{pkg_name}-tests
%license LICENSE
%{python3_sitelib}/oslo_context/tests


%changelog
%autochangelog
