%global sources_gpg 1
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318
%global pypi_name reno

# docs have problems generating in release rather than upstream git
# to be checked....
%global with_docs 0

%global common_desc %{expand:
Reno is a release notes manager for storing
release notes in a git repository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.}

Name:           python-%{pypi_name}
Version:        4.1.0
Release:        %autorelease
Summary:        Release NOtes manager

License:        Apache-2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

BuildRequires:  python3-devel
# tests require source to be a git repo.
BuildRequires:  git-core

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n     python3-%{pypi_name}
Summary:        RElease NOtes manager
Requires :      git-core


%description -n python3-%{pypi_name}
%{common_desc}


%package -n python-%{pypi_name}-doc
Summary:        reno documentation
%description -n python-%{pypi_name}-doc
Documentation for reno


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{version} -S git

sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini
sed -i /.*sphinx\]$/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    test-requirements.txt


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

%pyproject_save_files -l reno

%if 0%{?with_docs}
# generate html docs
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc ChangeLog README.rst
%license LICENSE
%{_bindir}/%{pypi_name}


%files -n python-%{pypi_name}-doc
%if 0%{?with_docs}
%doc doc/build/html
%endif
%license LICENSE


%changelog
%autochangelog
