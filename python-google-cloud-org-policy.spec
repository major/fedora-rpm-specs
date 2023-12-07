%bcond_without  tests

%global         srcname     google-cloud-org-policy
%global         forgeurl    https://github.com/googleapis/python-org-policy
Version:        1.8.3
%global         tag         v%{version_no_tilde %{quote:%nil}}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Organization Policy API

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
The Organization Policy API allows users to configure governance rules on their
GCP resources across the Cloud Resource Hierarchy.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google

# Remove extra scripts, docs files, and tests.
rm -rf %{buildroot}%{python3_sitelib}/{docs,samples,scripts,tests}


%check
%pyproject_check_import

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_org_policy-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
