%global sources_gpg 1
%global sources_gpg_sign 0x30566c450e41d7c91e442dfb231f942f608ddeff

%global sname barbicanclient
%global with_doc 1

%global _description %{expand:
This is a client for the Barbican Key Management API. There is a Python
library for accessing the API (barbicanclient module), and a
command-line script (barbican).}


Name:             python-%{sname}
Version:          7.6.0
Release:          %autorelease
Summary:          Python API and CLI for the Barbican Client
License:          Apache-2.0
URL:              https://launchpad.net/%{name}
Source0:          https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:    gpgverify
%endif

BuildRequires:    git-core
BuildRequires:    python3-devel
# This package is split not following python guidelines
BuildRequires:    python3-sphinxcontrib-rsvgconverter


%description %{_description}


%package -n python3-%{sname}
Summary:          %{summary}


%description -n python3-%{sname} %{_description}


%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Barbican API Client


%description doc
%{_description}

This package contains auto-generated documentation.
%endif


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{sname}-%{version} -S git

# Ignore global online constraints file
sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

# Disable coverage - messy.
sed -i \
    -e 's/^\s*PYTHON=coverage.*//' \
    -e 's/^\s*coverage.*//' \
    tox.ini

# Drop dependencies for lint, coverage, ...
%pyproject_patch_dependency hacking:ignore
%pyproject_patch_dependency coverage:ignore


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

%pyproject_save_files -l %{sname}


%if 0%{?with_doc}
%tox -e docs
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo doc/build/html/.htaccess
%endif


%check
%tox -e %{default_toxenv}


%files -n python3-%{sname} -f %{pyproject_files}
%doc ChangeLog README.rst
%{_bindir}/barbican


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
