# F35: Do not update past 0.1.11. F35's protobuf is too old.

# The package currently has an empty test directory.
%bcond_with tests

%global         srcname     google-cloud-access-context-manager
%global         forgeurl    https://github.com/googleapis/python-access-context-manager
Version:        0.1.14
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Google Cloud Client Libraries for google-cloud-access-context-manager

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
Protobufs for Google Access Context Manager.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%if %{with tests}
%check
# Work around an unusual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest --disable-warnings tests/unit
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.md
%{python3_sitelib}/google_cloud_access_context_manager-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
