Name:           python-mkdocs-monorepo-plugin
Version:        1.1.2
Release:        %autorelease
Summary:        Plugin for adding monorepository support in Mkdocs

License:        Apache-2.0
URL:            https://github.com/backstage/mkdocs-monorepo-plugin
Source:         %{pypi_source mkdocs-monorepo-plugin}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This packages provides a Mkdocs plugin to build multiple sets of documentation
in a single Mkdocs.}

%description %_description

%package -n     python3-mkdocs-monorepo-plugin
Summary:        %{summary}

%description -n python3-mkdocs-monorepo-plugin %_description

%prep
%autosetup -p1 -n mkdocs-monorepo-plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mkdocs_monorepo_plugin

%check
%pytest -v -k "not test_plugin_on_config_with_nav"

%files -n python3-mkdocs-monorepo-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
