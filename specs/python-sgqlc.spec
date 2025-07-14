%global pypi_name sgqlc
%global forgeurl https://github.com/profusion/sgqlc

Name:           python-%{pypi_name}
Version:        16.5
Release:        %{autorelease}
Summary:        Simple GraphQL Client
%forgemeta
License:        ISC
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest

%global _description %{expand:
This package offers an easy to use GraphQL client.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Allow building with Python 3.13+
sed -i 's/,<3.13//' pyproject.toml

# Disable coverage and doctest
sed -i -e "s/--cov.* //g" -e "s/ --cov.*'/'/" -e "s/ --doctest.*'/'/" pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x  websocket,requests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}


%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.* AUTHORS
%license LICENSE
%{_bindir}/sgqlc-codegen


%changelog
%autochangelog
