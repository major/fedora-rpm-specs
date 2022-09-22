# EPEL9 does not have python-aiohttp packaged yet.
%if 0%{?fedora}
%bcond_without  tests
%else
%bcond_with     tests
%endif

%global         srcname     azure-core

Name:           python-%{srcname}
Version:        1.25.1
Release:        %autorelease
Summary:        Azure Core shared client library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}
# Werkzeug >= 2.2 Support
Patch01:        Adjust-tests-for-werkzeug-2.2.patch

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


%prep
%autosetup -n %{srcname}-%{version} -p4

# Fedora 35/36 and epel9 have an older version of typing-extensions.
%if 0%{?fedora} < 37 || 0%{?rhel}
sed -i 's/typing-extensions[>=0-9\.]*/typing-extensions/' setup.py
%endif

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
%doc README.md


%changelog
%autochangelog
