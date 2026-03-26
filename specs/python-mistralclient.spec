%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global source_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff
%global pypi_name mistralclient
%global cliname   mistral
%global with_doc 0


%global common_desc %{expand:
Python client for Mistral REST API. Includes python library for Mistral API
and Command Line Interface (CLI) library.}

Name:           python-%{pypi_name}
Version:        6.2.0
Release:        %autorelease
Summary:        Python client for Mistral REST API

License:        Apache-2.0
URL:            https://pypi.io/pypi/python-mistralclient
Source0:        https://tarballs.openstack.org/%{name}/python_%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n     python3-%{pypi_name}
Summary:        Python client for Mistral REST API


%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{with_doc}
%package -n python-%{pypi_name}-doc
Summary:       Documentation for python client for Mistral REST API


%description -n python-%{pypi_name}-doc
%{common_desc}

This package contains documentation.
%endif


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{pypi_name}-%{version} -S git

# Remove the functional tests, we don't need them in the package
rm -rf mistralclient/tests/functional

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^tempest[[:space:]]*[><=]/d" \
    -e "/^hacking[[:space:]]*[><=]/d" \
    -e "/^osprofiler[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
    test-requirements.txt doc/requirements.txt

# No osprofiler
rm mistralclient/tests/unit/test_client.py \
   mistralclient/tests/unit/test_httpclient.py


# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel

%if 0%{with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l mistralclient

# Install bash completion scripts
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -m 644 -T tools/mistral.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/python-mistralclient


%check
%tox -e %{default_toxenv} -- -- --exclude-regex 'mistralclient.tests.unit.test_shell.TestShell.test_profile'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc ChangeLog README.rst
%{_bindir}/%{cliname}
%dir %{_sysconfdir}/bash_completion.d
%config(noreplace) %{_sysconfdir}/bash_completion.d/python-mistralclient


%if 0%{with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
