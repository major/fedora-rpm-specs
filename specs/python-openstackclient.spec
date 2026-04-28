%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

# Command name
%global cname openstack

# library name
%global sname %{cname}client

%global with_doc 1

%global common_desc \
python-%{sname} is a unified command-line client for the OpenStack APIs. \
It is a thin wrapper to the stock python-*client modules that implement the \
actual REST API client actions.

Name:             python-%{sname}
Version:          9.0.0
Release:          %autorelease
Summary:          OpenStack Command-line Client

License:          Apache-2.0
URL:              http://launchpad.net/%{name}
Source0:          https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/python_%{sname}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:        noarch

BuildRequires:    python3-devel

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:    git-core

%description
%{common_desc}

%package -n python3-%{sname}
Summary:          OpenStack Command-line Client

BuildRequires:    python3-babel

Requires:         python-%{sname}-lang = %{version}-%{release}
Recommends:       bash-completion

%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary:          Documentation for OpenStack Command-line Client

Requires: python3-%{sname} = %{version}-%{release}

%description -n python-%{sname}-doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%package  -n python-%{sname}-lang
Summary:   Translation files for Openstackclient

%description -n python-%{sname}-lang
Translation files for Openstackclient

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{sname}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i '/sphinx-build/ s/-W//' tox.ini
sed -i '/whereto*/d' tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^tempest[[:space:]]*[!><=]/d" \
    -e "/^osprofiler[[:space:]]*[!><=]/d" \
    -e "/^tempest[[:space:]]*[!><=]/d" \
    -e "/^whereto[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt

# autocomplete docs are optional per package add these back 
# if they exist in fedora/epel

sed -i \
    -e "/^python-barbicanclient[[:space:]]*[!><=]/d" \
    -e "/^python-cyborgclient[[:space:]]*[!><=]/d" \
    -e "/^python-zunclient[[:space:]]*[!><=]/d" \
    -e "/^python-watcherclient[[:space:]]*[!><=]/d" \
    -e "/^python-designateclient[[:space:]]*[!><=]/d" \
    -e "/^python-magnumclient[[:space:]]*[!><=]/d" \
    -e "/^python-ironic-inspector-client[[:space:]]*[!><=]/d" \
    doc/requirements.txt

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

# Generate i18n files
%{__python3} setup.py compile_catalog -d %{buildroot}%{python3_sitelib}/%{sname}/locale --domain openstackclient


%if 0%{?with_doc}
export PYTHONPATH=.
%tox -e docs
sphinx-build -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/%{cname}.1 %{buildroot}%{_mandir}/man1/%{cname}.1

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo doc/build/html/.htaccess
%endif

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}

rm -f %{buildroot}%{python3_sitelib}/%{sname}/locale/*/LC_*/%{sname}*po
rm -f %{buildroot}%{python3_sitelib}/%{sname}/locale/*pot

mv %{buildroot}%{python3_sitelib}/%{sname}/locale %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{python3_sitelib}/%{sname}/locale
sed -i '\|%{python3_sitelib}/%{sname}/locale\(/.*\)\?$|d' %{pyproject_files}

# Find language files
%find_lang %{sname} --all-name


%post -n python3-%{sname}
mkdir -p /etc/bash_completion.d
openstack complete | sed -n '/_openstack/,$p' > /etc/bash_completion.d/osc.bash_completion


%check
export PYTHON=%{__python3}
%tox -e %{default_toxenv} -- -- --exclude-regex 'openstackclient.tests.unit.common.test_module.TestModuleList.*'


%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/%{cname}
%if 0%{?with_doc}
%{_mandir}/man1/%{cname}.1*


%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html
%endif


%files -n python-%{sname}-lang -f %{sname}.lang
%license LICENSE


%changelog
%autochangelog
