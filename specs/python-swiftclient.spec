%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global with_doc 1

%global sname swiftclient

%global common_desc %{expand:
Client library and command line utility for interacting with Openstack
Object Storage API.}

Name:       python-swiftclient
Version:    4.10.0
Release:    %autorelease
Summary:    Client Library for OpenStack Object Storage API
License:    Apache-2.0
URL:        http://launchpad.net/python-swiftclient/
Source0:    https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:  https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz.asc
Source102:  https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

BuildRequires: python3-devel
BuildRequires: git-core

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n python3-%{sname}
Summary:    Client Library for OpenStack Object Storage API
Requires:   python3-%{sname}+keystone = %{version}-%{release}


%description -n python3-%{sname}
%{common_desc}


%if 0%{?with_doc}
%package doc
Summary:    Documentation for OpenStack Object Storage API Client
Group:      Documentation


%description doc
Documentation for the client library for interacting with Openstack
Object Storage API.
%endif


%pyproject_extras_subpkg -n python3-%{sname} keystone


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{sname}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
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

%pyproject_save_files -l swiftclient


%if 0%{?with_doc}
export LANG=en_US.utf-8
export LC_ALL=C
export LANGUAGE=en_US:en
%tox -e docs
rm -rf doc/build/html/.{doctrees,buildinfo}

sphinx-build -W -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/
%endif


%check
%tox -e %{default_toxenv}


%files -n python3-%{sname}  -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/swift
%{_mandir}/man1/*


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
