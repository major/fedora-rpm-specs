%bcond_without tests

%global         srcname     google-cloud-core
%global         forgeurl    https://github.com/googleapis/python-cloud-core
Version:        2.3.3
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Core Helpers for Google Cloud Python Client Library

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pkg-resources

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This library is not meant to stand-alone. Instead it defines common helpers
(e.g. base Client classes) used by all of the google-cloud-* packages.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


# Build the grpc extras subpackage.
%pyproject_extras_subpkg -n python3-%{srcname} grpc


%prep
%forgeautosetup -p0


%generate_buildrequires
%pyproject_buildrequires -x grpc


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
%pyproject_check_import

%if %{with tests}
# Python 3.15 changed site.py internals so nspkg.pth files can no longer use
# sys._getframe(1).f_locals['sitedir']. Without working nspkg.pth, the old
# google/__init__.py namespace hack restricts google.__path__ to the source
# tree, hiding google.auth from system site-packages. Removing these files
# lets Python use implicit namespace packages (PEP 420) instead.
find . \( -path "*/google/__init__.py" -o -path "*/google/cloud/__init__.py" \) -delete
%pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst *.md
%{python3_sitelib}/google_cloud_core-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
