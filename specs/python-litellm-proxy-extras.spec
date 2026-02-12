Name:           python-litellm-proxy-extras
Version:        0.4.29
Release:        %autorelease
Summary:        Additional files for the LiteLLM Proxy

License:        MIT
URL:            https://litellm.ai
Source:         %{pypi_source litellm_proxy_extras}

BuildSystem:    pyproject
BuildOption(install):  -l litellm_proxy_extras

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Additional files for the LiteLLM Proxy.
Reduces the size of the main litellm package.
}

%description %_description

%package -n     python3-litellm-proxy-extras
Summary:        %{summary}

%description -n python3-litellm-proxy-extras %_description

%check
%pyproject_check_import


%files -n python3-litellm-proxy-extras -f %{pyproject_files}


%changelog
%autochangelog
