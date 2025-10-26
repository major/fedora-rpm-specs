%global pypi_name sgqlc
Name:           python-%{pypi_name}
Version:        17.1
Release:        %{autorelease}
Summary:        Simple GraphQL Client

%global forgeurl https://github.com/profusion/sgqlc
%global tag v%{version}
%forgemeta

License:        ISC
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
BuildRequires:  %{py3_dist respx}

%global _description %{expand:
This package offers an easy to use GraphQL client.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%pyproject_extras_subpkg -n python3-%{pypi_name} websocket,requests,httpx


%prep
%forgeautosetup -p1

# Disable coverage and doctest
sed -r \
    -e "s/--cov.* //g" \
    -e "s/ --cov.*'/'/" \
    -e "s/ --doctest.*'/'/" \
    -i pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x  websocket,requests,httpx


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}


%check
%pytest -r fEs


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.* AUTHORS
%license LICENSE
%{_bindir}/sgqlc-codegen


%changelog
%autochangelog
