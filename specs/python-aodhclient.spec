%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global pypi_name aodhclient

%global common_desc %{expand:
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool.}

Name:             python-aodhclient
Version:          3.10.1
Release:          %autorelease
Summary:          Python API and CLI for OpenStack Aodh

License:          Apache-2.0
URL:              https://launchpad.net/python-aodhclient
Source0:          https://tarballs.openstack.org/%{name}/%{pypi_name}-%{version}.tar.gz
# Profiler not available in Fedora
Patch0:           0001-Remove-osprofiler-usage.patch
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:        noarch

BuildRequires:    python3-devel
BuildRequires:    git-core

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n python3-%{pypi_name}
Summary:          Python API and CLI for OpenStack Aodh


%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package  doc
Summary:          Documentation for OpenStack Aodh API Client


%description doc
%{common_desc}
(aodh).

This package contains auto-generated documentation.
%endif


%package -n python3-%{pypi_name}-tests
Summary:          Python API and CLI for OpenStack Aodh Tests
Requires:         python3-%{pypi_name} = %{version}-%{release}


%description -n python3-%{pypi_name}-tests
%{common_desc}


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^pifpaf[[:space:]]*[><=]/d" \
    -e "/^tempest[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
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

%pyproject_save_files -l aodhclient


%if 0%{?with_doc}
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%check
%tox -e %{default_toxenv}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/aodh


%files -n python3-%{pypi_name}-tests
%license LICENSE
%{python3_sitelib}/aodhclient/tests


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
