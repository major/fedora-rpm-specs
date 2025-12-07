Name:           python-azure-ai-projects
Version:        1.0.0
Release:        %autorelease
Summary:        Azure AI Projects client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-ai-projects/
Source:         %{pypi_source azure_ai_projects %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
The AI Projects client library is part of the Azure AI Foundry SDK, and
provides easy access to resources in your Azure AI Foundry Project.}

%description %{_description}


%package -n python3-azure-ai-projects
Summary:        %{summary}

%description -n python3-azure-ai-projects %{_description}


%prep
%autosetup -n azure_ai_projects-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l azure


# Like other Azure SDK packages, the tests expect Azure to be available
%check
%pyproject_check_import


%files -n python3-azure-ai-projects -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
