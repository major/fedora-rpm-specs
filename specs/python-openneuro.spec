%global pypi_name openneuro-py
# The importable module is called 'openneuro'
%global module_name openneuro

Name:           python-%{module_name}
Version:        2025.2.0
Release:        %{autorelease}
Summary:        A Python client for OpenNeuro

%global forgeurl https://github.com/hoechenberger/openneuro-py
%global tag v%{version}
%forgemeta

License:        GPL-3.0-only
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest

%global _description %{expand:
A Python client for accessing OpenNeuro datasets.}

%description %_description


%package -n python3-%{module_name}
Summary:        %{summary}
Provides:       %{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{module_name} %_description


%prep
%forgeautosetup -p1

# Exclude tests from wheel
sed -i '/^packages.*openneuro/a exclude = ["src/openneuro/tests"]' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{module_name}

install -d \
    '%{buildroot}%{bash_completions_dir}' \
    '%{buildroot}%{zsh_completions_dir}' \
    '%{buildroot}%{fish_completions_dir}'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
'%{buildroot}%{_bindir}/%{pypi_name}' --show-completion bash \
    > '%{buildroot}%{bash_completions_dir}/%{pypi_name}'
'%{buildroot}%{_bindir}/%{pypi_name}' --show-completion zsh \
    > '%{buildroot}%{zsh_completions_dir}/_%{pypi_name}'
'%{buildroot}%{_bindir}/%{pypi_name}' --show-completion fish \
    > '%{buildroot}%{fish_completions_dir}/%{pypi_name}.fish'


%check
# Exclude tests requiring network (they also require an API key)
k="${k-}${k+ and }not test_download"
k="${k-}${k+ and }not test_resume_download"
k="${k-}${k+ and }not test_ds000248"
k="${k-}${k+ and }not test_doi_handling"
k="${k-}${k+ and }not test_restricted_dataset"
%pytest -r fEs ${k+-k "${k-}"}

# Also run import test since majority of tests cannot be run in mock
%pyproject_check_import


%files -n python3-%{module_name} -f %{pyproject_files}
%doc README.*
%{_bindir}/%{pypi_name}
%{bash_completions_dir}/%{pypi_name}
%{zsh_completions_dir}/_%{pypi_name}
%{fish_completions_dir}/%{pypi_name}.fish


%changelog
%autochangelog
