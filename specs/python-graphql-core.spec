%global pypi_name graphql-core

Name:           python-%{pypi_name}
Version:        3.2.6
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
sed -r \
    -e 's/(pytest.*)>=[0-9.]+.*/\1/g' \
    -e '/pytest-cov/d' \
    -e '/pytest-describe/d' \
    -i tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files graphql

%check
%pytest -r fEs

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
