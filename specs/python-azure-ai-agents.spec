Name:           python-azure-ai-agents
Version:        1.1.0
Release:        %autorelease
Summary:        Azure AI Projects client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-ai-agents/
Source:         %{pypi_source azure_ai_agents %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
The AI Projects client library is part of the Azure AI Foundry SDK, and
provides easy access to resources in your Azure AI Foundry Project.}

%description %{_description}


%package -n python3-azure-ai-agents
Summary:        %{summary}

%description -n python3-azure-ai-agents %{_description}


%prep
%autosetup -n azure_ai_agents-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l azure


# Like other Azure SDK packages, the tests expect Azure to be available
%check
%pyproject_check_import -e "azure.ai.agents.telemetry"


%files -n python3-azure-ai-agents -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
