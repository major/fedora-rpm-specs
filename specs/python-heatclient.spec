%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global with_doc 1

%global sname heatclient

%global common_desc %{expand:
This is a client for the OpenStack Heat API. There is a Python API (the
heatclient module), and a command-line script (heat). Each implements 100% of
the OpenStack Heat API.}

Name:    python-heatclient
Version: 5.1.0
Release: %autorelease
Summary: Python API and CLI for OpenStack Heat

License: Apache-2.0
URL:     https://launchpad.net/python-heatclient
Source0: https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: git-core

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n python3-%{sname}
Summary: Python API and CLI for OpenStack Heat


%description -n python3-%{sname}
%{common_desc}


%if 0%{?with_doc}
%package doc
Summary: Documentation for OpenStack Heat API Client


%description doc
%{common_desc}

This package contains auto-generated documentation.
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{sname}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^tempest[[:space:]]*[!><=]/d" \
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

%pyproject_save_files -l heatclient

echo "%{version}" > %{buildroot}%{python3_sitelib}/heatclient/versioninfo

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/heat.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/heat

%if 0%{?with_doc}
export PYTHONPATH="%{buildroot}/%{python3_sitelib}"
%tox -e docs
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

# generate man page
sphinx-build -W -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/heat.1 %{buildroot}%{_mandir}/man1/heat.1
%endif


%check
%pyproject_check_import heatclient -e heatclient.tests.*


%files -n python3-%{sname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%dir %{_sysconfdir}/bash_completion.d
%config(noreplace) %{_sysconfdir}/bash_completion.d/heat
%if 0%{?with_doc}
%{_mandir}/man1/heat.1.gz
%endif
%{_bindir}/heat
%{python3_sitelib}/heatclient/versioninfo


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
