%bcond tests 1
# The azure-key-vault extra needs python-azure-keyvault-secrets>=4.8.0, but
# azure-cli is not ready:
# https://src.fedoraproject.org/rpms/python-azure-keyvault-secrets/pull-request/1
%bcond azure_key_vault 0
# The aws-secrets-manager extra needs boto3-stubs[secretsmanager], but
# python-boto3-stubs is not packaged.
%bcond aws_secrets_manager 0
# The gcp-secret-manager extra needs google-cloud-secret-manager>=2.23.1, but
# python-google-cloud-secret-manager is not packaged.
%bcond gcp_secret_manager 0

%global forgeurl https://github.com/pydantic/pydantic-settings

Name:           python-pydantic-settings
Version:        2.9.1
%forgemeta
Release:        %autorelease
Summary:        Settings management using pydantic

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli
%if %{with tests}
# See dependency-groups.testing in pyproject.toml.
# We list test dependencies manually to avoid having to patch out verious
# unwanted and unnecessary dependencies:
#
# - coverage (coverage analysis)
# - pytest-examples, moto: not packaged, not mandatory
# - pytest-pretty: purely cosmetic
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
%endif

%global _description %{expand:
Settings management using pydantic.}

%description %_description


%package -n python3-pydantic-settings
Summary:        %{summary}

%description -n python3-pydantic-settings %_description


%prep
%autosetup -p1 %{forgesetupargs}

# Erroring on warnings is too strict for downstream packaging
tomcli set pyproject.toml lists delitem \
    'tool.pytest.ini_options.filterwarnings' 'error'


%generate_buildrequires
%{pyproject_buildrequires \
    -x yaml \
    -x toml \
    %{?with_azure_key_vault:-x azure-key-vault} \
    %{?with_aws_secrets_manager:-x aws-secrets-manager} \
    %{?with_gcp_secret_manager:-x gcp-secret-manager}}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pydantic_settings


%check
%if %{with tests}
ignore="${ignore-} --ignore=tests/test_docs.py"
%if %{without azure_key_vault}
ignore="${ignore-} --ignore tests/test_source_azure_key_vault.py"
%endif
%if %{without aws_secrets_manager}
ignore="${ignore-} --ignore tests/test_source_aws_secrets_manager.py"
%endif
%if %{without gcp_secret_manager}
ignore="${ignore-} --ignore tests/test_source_gcp_secret_manager.py"
%endif

%pytest ${ignore-} -k "${k-}" -rs -v
%endif


%files -n python3-pydantic-settings -f %{pyproject_files}
%doc README.md


%pyproject_extras_subpkg -n python3-pydantic-settings yaml toml
%if %{with azure_key_vault}
%pyproject_extras_subpkg -n python3-pydantic-settings azure-key-vault
%endif
%if %{with aws_secrets_manager}
%pyproject_extras_subpkg -n python3-pydantic-settings aws-secrets-manager
%endif
%if %{with gcp_secret_manager}
%pyproject_extras_subpkg -n python3-pydantic-settings gcp-secret-manager
%endif


%changelog
%autochangelog
