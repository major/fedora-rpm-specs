%bcond_without  tests

%global         srcname     google-cloud-firestore
%global         forgeurl    https://github.com/googleapis/python-firestore
Version:        2.10.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Firestore API

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch
# Expected hash values in test_documentsnapshot___hash__ assume a 64-bit
# platform. We could make the base package arched and the binary package
# arched, and conditionally skip this test on 32-bit architectures; or, we can
# just exclude 32-bit architectures, ensuring the package will be built on a
# 64-bit platform.
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(aiounittest)
BuildRequires:  python3dist(google-cloud-testutils)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
The Google Cloud Firestore API is a flexible, scalable database for mobile,
web, and server development from Firebase and Google Cloud Platform.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


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

# Remove unnecessary script.
rm -f %{buildroot}%{_bindir}/fixup*.py


%check
%pyproject_check_import

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst *.md samples
%{python3_sitelib}/google_cloud_firestore-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
