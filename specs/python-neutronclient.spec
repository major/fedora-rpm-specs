%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff
%global with_doc 1

%global cname neutron
%global sname %{cname}client

%global common_desc %{expand:
Client library and command line utility for interacting with the OpenStack
Neutron API.}

Name:       python-neutronclient
Version:    11.8.0
Release:    %autorelease
Summary:    Python API and CLI for OpenStack Neutron

License:    Apache-2.0
URL:        http://launchpad.net/%{name}/
Source0:    https://tarballs.openstack.org/%{name}/python_neutronclient-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_neutronclient-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

BuildRequires: git-core
BuildRequires: python3-devel

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n python3-%{sname}
Summary:    Python API and CLI for OpenStack Neutron


%description -n python3-%{sname}
%{common_desc}


%package -n python3-%{sname}-tests
Summary:    Python API and CLI for OpenStack Neutron - Unit tests
Requires: python3-%{sname} == %{version}-%{release}
Requires: python3-osc-lib
Requires: python3-oslotest
Requires: python3-stestr
Requires: python3-testtools
Requires: python3-testscenarios


%description -n python3-%{sname}-tests
%{common_desc}

This package containts the unit tests.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Neutron API Client

%description      doc
%{common_desc}
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_neutronclient-%{version} -S git


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i '/sphinx-build/ s/-W//' tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^osprofiler[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^bandit[[:space:]]*[!><=]/d" \
    -e "/^flake8-import-order[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt

# https://review.opendev.org/c/openstack/python-neutronclient/+/985789/1
sed -i "s/'reno.sphinxext',//" doc/source/conf.py

%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel

%if 0%{?with_doc}
# Build HTML docs
%tox -e docs

# Fix hidden-file-or-dir warnings
rm -rf doc/build/html/.doctrees doc/build/html/.buildinfo
%endif


%install
%pyproject_install

%pyproject_save_files -l neutronclient


%check
# test_http.py imports osprofiler
rm neutronclient/tests/unit/test_http.py
%tox -e %{default_toxenv}


%files -n python3-%{sname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%exclude %{python3_sitelib}/%{sname}/tests


%files -n python3-%{sname}-tests
%{python3_sitelib}/%{sname}/tests


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
