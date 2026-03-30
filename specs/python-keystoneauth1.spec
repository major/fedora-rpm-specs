%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff
%global pypi_name keystoneauth1

%global common_desc %{expand:
Keystoneauth provides a standard way to do authentication and service requests
within the OpenStack ecosystem. It is designed for use in conjunction with
the existing OpenStack clients and for simplifying the process of writing
new clients.}

%global with_doc 1

Name:       python-%{pypi_name}
Version:    5.13.1
Release:    %autorelease
Summary:    Authentication Library for OpenStack Clients
License:    Apache-2.0
URL:        https://pypi.io/pypi/%{pypi_name}
Source0:    https://tarballs.openstack.org/keystoneauth/keystoneauth1-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/keystoneauth/keystoneauth1-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:     noarch

BuildRequires: git-core
BuildRequires: python3-devel


# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n     python3-%{pypi_name}
Summary:        Authentication Libarary for OpenStack Identity


%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:    Documentation for OpenStack Identity Authentication Library


%description -n python-%{pypi_name}-doc
Documentation for OpenStack Identity Authentication Library
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{version} -S git

sed -i '/sphinx.ext.intersphinx.*$/d'  doc/source/conf.py

# remove syntax tests
rm keystoneauth1/tests/unit/test_hacking_checks.py

sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini
sed -i '/sphinx-build/ s/-W//' tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[~!><=]/d" \
    -e "/^hacking[[:space:]]*[~!><=]/d" \
    -e "/^reno[[:space:]]*[~!><=]/d" \
    -e "/^flake8-docstrings[[:space:]]*[~!><=]/d" \
    -e "/^flake8-import-order[[:space:]]*[~!><=]/d" \
    -e "/^bandit[[:space:]]*[~!><=]/d" \
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

%pyproject_save_files -l keystoneauth1

%if 0%{?with_doc}
# generate html docs
export PYTHONPATH=.
# Disabling warning-is-error because of issue with python2 giving a warning:
# "The config value `apidoc_module_dir' has type `unicode', expected to ['str']."
%tox -e docs
rm -rf doc/build/html/.buildinfo
%endif


%check
%tox -e %{default_toxenv} -- -- --exclude-regex '(.*test_keystoneauth_betamax_fixture)'


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE


%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%endif


%changelog
%autochangelog
