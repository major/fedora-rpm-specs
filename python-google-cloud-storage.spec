%bcond_without  tests

%global         srcname     google-cloud-storage

Name:           python-%{srcname}
Version:        2.14.0
Release:        %autorelease
Summary:        Python Client for Google Cloud Storage

License:        Apache-2.0
URL:            https://github.com/googleapis/python-storage
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
Google Cloud Storage allows you to store data on Google infrastructure with
very high reliability, performance and availability, and can be used to
distribute large data objects to users via direct download.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n python-storage-%{version} -p1

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


%check
%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit \
        -k "not test_create_bucket_w_custom_endpoint \
            and not test_ctor_w_custom_endpoint_use_auth \
            and not test_list_buckets_w_custom_endpoint \
            and not test_seek_fails \
            and not test_downloads_w_client_custom_headers"
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md


%changelog
%autochangelog
