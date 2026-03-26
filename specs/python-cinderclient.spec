%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global sname cinderclient

%global with_doc 1

%global common_desc %{expand:
Client library (cinderclient python module) and command line utility
(cinder) for interacting with OpenStack Cinder (Block Storage) API.}

Name:             python-cinderclient
Version:          9.9.0
Release:          %autorelease
Summary:          Python API and CLI for OpenStack Cinder

License:          Apache-2.0
URL:              http://github.com/openstack/python-cinderclient
Source0:          https://tarballs.openstack.org/%{name}/python_cinderclient-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_cinderclient-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:    git-core


%description
%{common_desc}


%package -n python3-%{sname}
Summary:          Python API and CLI for OpenStack Cinder

BuildRequires:    python3-devel


%description -n python3-%{sname}
%{common_desc}


%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Cinder API Client
Group:            Documentation

%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_cinderclient-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^flake8-import-order[[:space:]]*[><=]/d" \
    -e "/^doc8[[:space:]]*[><=]/d" \
    -e "/^hacking[[:space:]]*[><=]/d" \
     test-requirements.txt doc/requirements.txt


%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel

%if 0%{?with_doc}
export PYTHONPATH=.
%tox -e docs
sphinx-build-3 -W -b man doc/source doc/build/man

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif


%install
%pyproject_install

%pyproject_save_files -l cinderclient

# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/cinderclient/tests
sed -i '\@/cinderclient/tests\(/.*\)\?$@d' %{pyproject_files}

install -p -D -m 644 tools/cinder.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/cinder.bash_completion

%if 0%{?with_doc}
install -p -D -m 644 doc/build/man/cinder.1 %{buildroot}%{_mandir}/man1/cinder.1
%endif


%files -n python3-%{sname} -f %{pyproject_files}
%doc ChangeLog README.rst
%license LICENSE
%{_bindir}/cinder
%dir %{_sysconfdir}/bash_completion.d
%config(noreplace) %{_sysconfdir}/bash_completion.d/cinder.bash_completion
%if 0%{?with_doc}
%{_mandir}/man1/cinder.1*
%endif


%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif


%changelog
%autochangelog
