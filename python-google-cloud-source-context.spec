# F35: Do not update past 1.2.3. F35's protobuf is too old.

# tests are enabled by default
%bcond_without  tests

%global         srcname     google-cloud-source-context
%global         forgeurl    https://github.com/googleapis/python-source-context
Version:        1.2.6
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Source Context

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
This package contains generated Python types for google.cloud.source_context_v1.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
%pyproject_check_import -e "tests*"

%if %{with tests}
# Work around an unusual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest tests/unit
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.rst README.rst SECURITY.md
%{python3_sitelib}/google_cloud_source_context-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
