%bcond_without tests

%global         srcname     google-cloud-datacatalog
%global         forgeurl    https://github.com/googleapis/python-datacatalog
Version:        3.11.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python SDK for Google Cloud Data Catalog API

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
Google Cloud Data Catalog API: Google Cloud Data Catalog API provides features
to attach metadata to Google Cloud Platform resources like BigQuery Tables. Key
critical resources include: Entries (Data Catalog representation of a cloud
resource).}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%package -n python-%{srcname}-doc
Summary:        Documentation for %{name}

%description -n python-%{srcname}-doc
Documentation for python-%{srcname}.


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google

# Remove unnecessary scripts.
rm -f %{buildroot}%{_bindir}/fixup*


%check
%pyproject_check_import

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.rst SECURITY.md UPGRADING.md
%{python3_sitelib}/google_cloud_datacatalog-%{version}-py%{python3_version}-nspkg.pth


%files -n python-%{srcname}-doc
%doc samples


%changelog
%autochangelog
