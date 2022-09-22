# F35: Do not update past 1.6.0. F35's protobuf is too old.

# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-functions
%global         forgeurl    https://github.com/googleapis/python-functions
Version:        1.8.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Functions

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
Manages lightweight user-provided functions executed in response to events
via the Google Cloud Functions API.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup

# Replace mock imports with unittest.mock.
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google

# Remove unneeded executable.
rm -f %{buildroot}/%{_bindir}/fixup_functions_v1_keywords.py


%check
%pyproject_check_import -e 'google.cloud.functions_v2*'

%if %{with tests}
# Work around an usual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest --disable-warnings tests/unit
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_functions-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
