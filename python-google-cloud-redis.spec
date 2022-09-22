# F35: Do not update past 2.8.0. F35's protobuf is too old.

# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-redis
%global         forgeurl    https://github.com/googleapis/python-redis
Version:        2.9.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Memorystore for Redis API

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
The Google Cloud Memorystore for Redis API is used for creating and managing
Redis instances on the Google Cloud Platform.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} libcst


%prep
%forgeautosetup

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

# Remove unneeded executables.
rm -f %{buildroot}/%{_bindir}/fixup*


%if %{with tests}
%check
%pytest --disable-warnings
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_redis-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
