# tests are enabled by default
%bcond_without  tests

%global         srcname     google-cloud-access-approval
%global         forgeurl    https://github.com/googleapis/python-access-approval
Version:        1.11.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Access Approval API

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
The Access Approval API is an API for controlling access to data by Google
personnel.}

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

# Remove unneeded executable.
rm -f %{buildroot}%{_bindir}/fixup_accessapproval_v1_keywords.py


%check
%pyproject_check_import

%if %{with tests}
# Work around an usual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest --disable-warnings tests/unit
mv google{_,}
%endif



%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_access_approval-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
