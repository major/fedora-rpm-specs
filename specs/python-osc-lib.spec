%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global library osc-lib
%global module osc_lib

%global common_desc osc-lib is a package of common support modules for writing OSC plugins.
%global with_doc 1

Name:       python-%{library}
Version:    4.4.0
Release:    %autorelease
Summary:    OpenStack library for writing OSC plugins
License:    Apache-2.0
URL:        https://github.com/openstack/%{library}/

Source0:    https://tarballs.openstack.org/%{library}/%{module}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:  https://tarballs.openstack.org/%{library}/%{module}-%{version}.tar.gz.asc
Source102:  https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  git-core

%description
%common_desc

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%package -n python3-%{library}
Summary:    OpenStack library for writing OSC plugins

# https://bugzilla.redhat.com/show_bug.cgi?id=2450758
Provides:   python3-%{library}-tests = %{version}-%{release}
Obsoletes:  python3-%{library}-tests < 3.1.1


%description -n python3-%{library}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{library}-doc
Summary:    OpenStack osc-lib library documentation


%description -n python-%{library}-doc
%{common_desc}

This package contains the documentation.
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{module}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^osprofiler[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt
 

%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires -t  -e %{default_toxenv}
%endif


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l %{module}

%if 0%{?with_doc}
# generate html docs
PYTHONPATH="%{buildroot}/%{python3_sitelib}"
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%check
%tox -e %{default_toxenv}


%files -n python3-%{library} -f %{pyproject_files}
%license LICENSE
%doc ChangeLog README.rst


%if 0%{?with_doc}
%files -n python-%{library}-doc
%license LICENSE
%doc doc/build/html
%endif


%changelog
%autochangelog
