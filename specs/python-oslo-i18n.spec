%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global pypi_name oslo.i18n
%global pkg_name oslo-i18n
%global with_doc 1

%global common_desc \
The oslo.i18n library contain utilities for working with internationalization \
(i18n) features, especially translation for text strings in an application \
or library.

Name:           python-oslo-i18n
Version:        6.7.2
Release:        %autorelease
Summary:        OpenStack i18n library
License:        Apache-2.0
URL:            https://github.com/openstack/%{pypi_name}
Source0:        https://tarballs.openstack.org/%{pypi_name}/oslo_i18n-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/oslo_i18n-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core

%description
%{common_desc}

%package -n python3-%{pkg_name}
Summary:        OpenStack i18n Python 3 library

BuildRequires:  python3-devel
BuildRequires:  python3-babel
Requires:       python-%{pkg_name}-lang = %{version}-%{release}

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:        Documentation for OpenStack i18n library

%description -n python-%{pkg_name}-doc
Documentation for the oslo.i18n library.
%endif

%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo i18n library

%description -n python-%{pkg_name}-lang
Translation files for Oslo i18n library

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n oslo_i18n-%{version} -S git


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[><=]/d" \
    -e "/^reno[[:space:]]*[><=]/d" \
    -e "/^oslo.config[[:space:]]*[><=]/d" \
    test-requirements.txt doc/requirements.txt

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e docs
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install

%if 0%{?with_doc}
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

# Fix this rpmlint warning
if [ -f html/_static/jquery.js ]; then
sed -i "s|\r||g" html/_static/jquery.js
fi
%endif

# Generate i18n files
python3 setup.py compile_catalog -d %{buildroot}%{python3_sitelib}/oslo_i18n/locale --domain oslo_i18n

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_i18n/locale/*/LC_*/oslo_i18n*po
rm -f %{buildroot}%{python3_sitelib}/oslo_i18n/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_i18n/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_i18n --all-name

%check
%tox

%files -n python3-%{pkg_name}
%doc ChangeLog CONTRIBUTING.rst README.rst
%license LICENSE
%{python3_sitelib}/oslo_i18n
%{python3_sitelib}/*.dist-info

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python-%{pkg_name}-lang -f oslo_i18n.lang
%license LICENSE

%changelog
%autochangelog
