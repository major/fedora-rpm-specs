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
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
%pyproject_check_import

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst *.md
%{python3_sitelib}/google_cloud_core-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
