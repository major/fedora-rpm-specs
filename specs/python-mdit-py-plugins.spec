%global pypi_name mdit-py-plugins

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        %autorelease
Summary:        Collection of plugins for markdown-it-py

# SPDX
# Both the package and its plugins are licensed under MIT
License:        MIT
URL:            https://github.com/executablebooks/mdit-py-plugins
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-regressions)

%global _description %{expand:
Collection of core plugins for markdown-it-py.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mdit_py_plugins

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
