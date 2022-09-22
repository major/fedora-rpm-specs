# F35: Do not update past 3.7.0. F35's protobuf is too old.

# tests are enabled by default
%bcond_without  tests

%global         srcname     google-cloud-dlp
%global         forgeurl    https://github.com/googleapis/python-dlp
Version:        3.9.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python SDK for Google Cloud Data Loss Prevention API

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
Cloud Data Loss Prevention (DLP) API: Provides methods for detection, risk
analysis, and de-identification of privacy-sensitive fragments in text, images,
and Google Cloud Platform storage repositories.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

# Build the libcst extras subpackage.
%pyproject_extras_subpkg -n python3-%{srcname} libcst


%prep
%forgeautosetup -p1

# Replace mock imports with unittest.mock.
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google

# Remove unnecessary scripts.
rm -f %{buildroot}%{_bindir}/fixup*


%if %{with tests}
%check
%pytest --disable-warnings tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.rst SECURITY.md UPGRADING.md samples
%{python3_sitelib}/google_cloud_dlp-%{version}-py%{python3_version}-nspkg.pth



%changelog
%autochangelog
