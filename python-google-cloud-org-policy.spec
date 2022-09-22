# F35: Do not update past 1.3.2. F35's protobuf is too old.

# The package currently has an empty test directory.
%bcond_with     tests

%global         srcname     google-cloud-org-policy
%global         forgeurl    https://github.com/googleapis/python-org-policy
Version:        1.4.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Organization Policy API

License:        ASL 2.0
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
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google

# Remove extra scripts, docs files, and tests.
rm -rf %{buildroot}%{python3_sitelib}/{docs,samples,scripts,tests}


%if %{with tests}
%check
# Work around an unusual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest --disable-warnings tests/unit
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_org_policy-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
