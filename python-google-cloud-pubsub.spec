%bcond_without  tests

%global         srcname     google-cloud-pubsub
%global         forgeurl    https://github.com/googleapis/python-pubsub
Version:        2.14.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Google Cloud Pub/Sub API client library

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Google Cloud Pub/Sub API client library.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

# Build the libcst extras subpackage.
%pyproject_extras_subpkg -n python3-%{srcname} libcst


%prep
%forgeautosetup

# Replace mock imports with unittest.mock.
# PR opened upstream: https://github.com/googleapis/python-pubsub/pull/702
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google

# Remove unnecessary script.
rm -f %{buildroot}%{_bindir}/fixup_pubsub_v1_keywords.py


%check
%pyproject_check_import

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md CODE_OF_CONDUCT.md README.rst SECURITY.md
%{python3_sitelib}/google_cloud_pubsub-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
