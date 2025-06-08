%bcond_without  tests

%global         reponame    azure-sdk-for-python
%global         srcname     azure-core

Name:           python-%{srcname}
Version:        1.30.2
Release:        %autorelease
Summary:        Azure Core shared client library for Python

License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

Epoch:          2

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(msrest)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
BuildRequires:  python3dist(trio)
%endif

%global _description %{expand:
Azure Core shared client library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%pyproject_extras_subpkg -n python3-%{srcname} aio

%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%check
%pyproject_check_import

%if %{with tests}
# azure-core has a flask-based testing server that must be available to run tests.
# Disabling async/streaming tests since they require network connectivity to various
# APIs on Azure's site.
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch}:tests/testserver_tests/coretestserver/ \
    %pytest \
        --ignore=tests/async_tests \
        --ignore tests/test_streaming.py \
        -k "not test_decompress_plain_no_header \
            and not test_compress_plain_no_header \
            and not test_decompress_compressed_no_header \
            and not test_text_and_encoding \
            and not test_response_headers" \
        tests
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md CLIENT_LIBRARY_DEVELOPER.md README.md


%changelog
%autochangelog
