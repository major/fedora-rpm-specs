%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global sname novaclient
%global with_doc 1

%global common_desc %{expand:
This is a client for the OpenStack Nova API. There is a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.}

Name:             python-novaclient
Epoch:            1
Version:          18.12.0
Release:          %autorelease
Summary:          Python API and CLI for OpenStack Nova
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
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  python3-devel
# For tests
BuildRequires:  openssl


%description
%{common_desc}


%package -n python3-%{sname}
Summary:          Python API and CLI for OpenStack Nova


%description -n python3-%{sname}
%{common_desc}


%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Nova API Client


%description      doc
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
sed -i /^.*whereto/d tox.ini
sed -i '/sphinx-build/ s/-W//' tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^tempest[[:space:]]*[><=]/d" \
    -e "/^osprofiler[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
    -e "/^whereto[[:space:]]*[><=]/d" \
    test-requirements.txt doc/requirements.txt


# Automatic BR generation
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

%pyproject_save_files -l novaclient

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/nova.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/nova

# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/novaclient/tests
sed -i '\@/novaclient/tests\(/.*\)\?$@d' %{pyproject_files}

%if 0%{?with_doc}
%tox -e docs
sphinx-build -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/nova.1 %{buildroot}%{_mandir}/man1/nova.1
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo doc/build/html/.htaccess
%endif


%check
%tox -e %{default_toxenv} -- -- --exclude-regex '(novaclient.tests.unit.test_shell.ShellTestKeystoneV3.test_osprofiler|novaclient.tests.unit.test_shell.ShellTest.test_osprofiler)'


%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc ChangeLog README.rst
%dir %{_sysconfdir}/bash_completion.d
%config(noreplace) %{_sysconfdir}/bash_completion.d/nova
%if 0%{?with_doc}
%{_mandir}/man1/nova.1.gz
%endif
%{_bindir}/nova

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
%autochangelog
