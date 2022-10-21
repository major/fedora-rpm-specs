# F35: Max version 2.8.0 due to old protobuf version.

# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-containeranalysis
%global         forgeurl    https://github.com/googleapis/python-containeranalysis
Version:        2.9.3
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python SDK for Google Cloud Container Analysis API

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
Container Analysis API: An implementation of the Grafeas API, which stores, and
enables querying and retrieval of critical metadata about all of your software
artifacts.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} libcst


%prep
%forgeautosetup -p1

# Allow a slightly older protobuf.
sed -i 's/"protobuf.*",/"protobuf>=3.19.4",/' setup.py

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

# Remove unnecessary files.
rm -f %{buildroot}%{_bindir}/fixup* samples/snippets/.gitignore


%if %{with tests}
%check
# Disable two tests that require network connectivity.
%pytest --disable-warnings tests/unit \
    -k "not test_get_grafeas_client and not test_get_grafeas_client_async"
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.rst SECURITY.md UPGRADING.md samples
%{python3_sitelib}/google_cloud_containeranalysis-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
