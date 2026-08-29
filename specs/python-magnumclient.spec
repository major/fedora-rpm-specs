%global sources_gpg 1
%global sources_gpg_sign 0x30566c450e41d7c91e442dfb231f942f608ddeff

%global sname magnumclient
%global with_doc 1

%global _description %{expand:
This is the client library for Magnum built on the Magnum API.
It provides a Python API ( the mangumclient module ) and a
command line tool (magnum).}


Name:             python-%{sname}
Version:          5.0.0
Release:          %autorelease
Summary:          Python API and CLI for the Magnum Client
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
BuildRequires:    /usr/bin/gpgv2
%endif

BuildRequires:    git-core
BuildRequires:    python3-devel


%description %{_description}


%package -n python3-%{sname}
Summary:          %{summary}


%description -n python3-%{sname} %{_description}


%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Magnum API Client


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

# Drop dependencies for lint, coverage, ...
%pyproject_patch_dependency reno:ignore
%pyproject_patch_dependency hacking:ignore
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency bandit:ignore
%pyproject_patch_dependency osprofiler:ignore


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


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
