%bcond_without  tests

%global         srcname     google-cloud-os-config
%global         forgeurl    https://github.com/googleapis/python-os-config
Version:        1.15.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud OS Config API

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
App Engine Admin allows you to manage your App Engine applications.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup

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

# Remove unnecessary script.
rm -f %{buildroot}%{_bindir}/fixup_keywords.py


%check
%pyproject_check_import -e 'google.cloud.osconfig_v1.types*' -e 'google.cloud.osconfig_v1alpha.types*'

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_os_config-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
