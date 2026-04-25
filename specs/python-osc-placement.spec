%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global docs 1

%global _description %{expand:
This is an OpenStackClient plugin, that provides CLI for the Placement service.
Python API binding is not implemented - Placement API consumers are encouraged
to use the REST API directly, CLI is provided only for convenience of users.}


Name:             python-osc-placement
Version:          4.8.0
Release:          %{autorelease}
Summary:          OpenStackClient plugin for the Placement service
License:          Apache-2.0
URL:              https://docs.openstack.org/osc-placement

Source0:          https://tarballs.openstack.org/osc-placement/osc_placement-%{version}.tar.gz
Source1:          https://tarballs.openstack.org/osc-placement/osc_placement-%{version}.tar.gz.asc
Source2:          https://releases.openstack.org/_static/%{sources_gpg_sign}.txt

BuildArch:        noarch

%if 0%{?sources_gpg} == 1
BuildRequires:    /usr/bin/gpgv2
%endif
BuildRequires:    git-core
BuildRequires:    python%{python3_pkgversion}-devel


%description %{_description}


%package -n python%{python3_pkgversion}-osc-placement
Summary:          %{summary}


%description -n python%{python3_pkgversion}-osc-placement %{_description}


%if 0%{?docs}
%package -n python-osc-placement-docs
Summary:          %{summary}
Requires:         python%{python3_pkgversion}-osc-placement = %{version}-%{release}


%description -n python-osc-placement-docs %{_description}
%endif


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%endif
%autosetup -n osc_placement-%{version} -S git

# Ignore global openstack constraints file
sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

# Ignore coverage and release modules
sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^wsgi-intercept[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt


%generate_buildrequires
%if 0%{?docs}
%pyproject_buildrequires -t -e %{default_toxenv} -e docs
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel


%install
%pyproject_install

# Cannot generate docs unless installed so here not in build.
%if 0%{?docs}
%tox -e docs
rm doc/build/html/.buildinfo
%endif

%pyproject_save_files -l osc_placement


%check
%tox -e %{default_toxenv}


%files -n python%{python3_pkgversion}-osc-placement -f %{pyproject_files}
%doc ChangeLog


%if 0%{?docs}
%files -n python-osc-placement-docs
%doc doc/build/html
%endif


%changelog
%autochangelog
