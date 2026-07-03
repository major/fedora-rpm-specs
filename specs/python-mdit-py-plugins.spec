# A "fake" bootstrap to not require python-pytest-regessions,
# as its long dependency chain allows to build it much later in new Python bootstrap
%bcond bootstrap 0
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
%if %{without bootstrap}
BuildRequires:  python3dist(pytest-regressions)
%endif

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
%pytest %{?with_bootstrap:-k 'not test_plugin_parse and not test_attrs_allowed and not test_tokens and not test_no_new_line_issue and not test_custom_renderer'}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
