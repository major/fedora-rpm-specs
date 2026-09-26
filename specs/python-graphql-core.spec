%global pypi_name graphql-core

Name:           python-%{pypi_name}
Version:        3.2.12
Release:        %autorelease
Summary:        GraphQL implementation for Python

%global forgeurl https://github.com/graphql-python/graphql-core
%global tag v%{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli


%global _description %{expand:
GraphQL-core-3 is a Python port of GraphQL.js, the JavaScript reference
implementation for GraphQL, a query language for APIs.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
Obsoletes:      python3-%{pypi_name}-doc < %{version}-%{release}


%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup

# Relax version constraints
tomcli set pyproject.toml arrays replace \
    build-system.requires '(.+)>=[0-9.].*' '\1'

# Relax version constraints for test dependencies and remove linters.
# and other unused / unavailable plugins.
%pyproject_patch_dependency pytest-cov:ignore
%pyproject_patch_dependency pytest-describe:ignore


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l graphql


%check
%pytest -r fEs


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
