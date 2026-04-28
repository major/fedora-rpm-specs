%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global sname glanceclient
%global with_doc 1


%global common_desc %{expand:
This is a client for the OpenStack Glance API. There is a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.}

Name:             python-glanceclient
Epoch:            1
Version:          4.11.0
Release:          %autorelease
Summary:          Python API and CLI for OpenStack Glance

License:          Apache-2.0
URL:              https://launchpad.net/python-glanceclient
Source0:          https://tarballs.openstack.org/%{name}/python_glanceclient-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_glanceclient-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

# https://review.opendev.org/c/openstack/python-glanceclient/+/986313
Patch0:           0001-fix-hashlib-ValueError-message-check-for-py3.15.patch

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:    git-core

%description
%{common_desc}

%package -n python3-%{sname}
Summary:          Python API and CLI for OpenStack Glance

BuildRequires:    python3-devel

%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Glance API Client

%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_glanceclient-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^hacking[[:space:]]*[><=]/d" \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
    -e "/^tempest[[:space:]]*[><=]/d" \
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

%pyproject_save_files -l glanceclient

# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/glanceclient/tests
sed -i '\@/glanceclient/tests\(/.*\)\?$@d' %{pyproject_files}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s glance %{buildroot}%{_bindir}/glance-3

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/glance.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/glance

%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
# generate man page
sphinx-build -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/glance.1 %{buildroot}%{_mandir}/man1/glance.1
%endif


%check
# CentOS CI environment is setting "http://cache.rdu2.centos.org:8080" which breaks the unit tests.
unset http_proxy
unset https_proxy
%tox -e %{default_toxenv} -- -- --exclude-regex '(glanceclient.tests.unit.test_ssl.TestHTTPSVerifyCert*|.*test_cache_schemas_gets_when_not_exists|.*test_cache_schemas_gets_when_forced)|.*test_http_chunked_response|.*test_log_request_id_once'


%files -n python3-%{sname} -f %{pyproject_files}
%doc ChangeLog README.rst
%license LICENSE
%dir %{_sysconfdir}/bash_completion.d
%config(noreplace) %{_sysconfdir}/bash_completion.d/glance
%if 0%{?with_doc}
%{_mandir}/man1/glance.1.gz
%endif
%{_bindir}/glance
%{_bindir}/glance-3

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
%autochangelog
