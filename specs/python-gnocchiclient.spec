%global sources_gpg 0
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f

%global pypi_name gnocchiclient

# NOTE(jpena): doc build fails with recent cliff versions, and hardcodes
# a call to unversioned python in
# https://github.com/gnocchixyz/python-gnocchiclient/blob/master/doc/source/conf.py#L54
%global with_doc 0


%global common_desc %{expand:
This is a client library for Gnocchi built on the Gnocchi API. It
provides a Python API (the gnocchiclient module) and a command-line tool.}

Name:             python-gnocchiclient
Version:          7.2.0
Release:          %autorelease
Summary:          Python API and CLI for OpenStack Gnocchi

License:          Apache-2.0
URL:              https://github.com/openstack/%{name}
Source0:          https://pypi.io/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n python3-%{pypi_name}
Summary:          Python API and CLI for OpenStack Gnocchi


BuildRequires:    python3-devel
%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:          Documentation for OpenStack Gnocchi API Client
Group:            Documentation


%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{version}


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini
sed -i '/\.\[test,openstack\]/,+2d' tox.ini
sed -i '/\.*\[testenv\]deps/,+1d' tox.ini
sed -i '/\.\[test,doc\]/d' tox.ini



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
%tox -e docs

# Fix hidden-file-or-dir warnings
rm -rf doc/build/html/.doctrees doc/build/html/.buildinfo
%endif


%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/gnocchi


%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%endif


%changelog
%autochangelog
