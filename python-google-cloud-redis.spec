%bcond_without tests

%global         srcname     google-cloud-redis
%global         reponame    google-cloud-python

Name:           python-%{srcname}
Version:        2.13.2
Release:        %autorelease
Summary:        Python Client for Google Cloud Memorystore for Redis API

License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python
Source0:        %{url}/archive/refs/tags/%{srcname}-v%{version}.tar.gz

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


%prep
# Upstream buries the package into a subdirectory. 😭
%setup -c -T
tar xzf %{SOURCE0} --strip-components=3 \
    %{reponame}-%{srcname}-v%{version}/packages/%{srcname}

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

# Remove unneeded executables.
rm -f %{buildroot}/%{_bindir}/fixup*


%check
%pyproject_check_import -e "google.cloud.redis*"

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_redis-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
