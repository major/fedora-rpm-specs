# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-pubsub
%global         forgeurl    https://github.com/googleapis/python-pubsub
Version:        2.13.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Google Cloud Pub/Sub API client library

License:        ASL 2.0
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


%if %{with tests}
%check
# Work around an unusual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest tests/unit
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md CODE_OF_CONDUCT.md README.rst SECURITY.md
%{python3_sitelib}/google_cloud_pubsub-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
