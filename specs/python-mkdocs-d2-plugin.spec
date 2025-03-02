Name:           python-mkdocs-d2-plugin
Version:        1.6.0
Release:        %autorelease
Summary:        D2 plugin for MkDocs

License:        MIT
URL:            https://github.com/landmaj/mkdocs-d2-plugin
Source:         %{pypi_source mkdocs_d2_plugin}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides a plugin for embedding D2 diagrams in MkDocs.}

%description %_description

%package -n     python3-mkdocs-d2-plugin
Summary:        %{summary}
Requires:       d2

%description -n python3-mkdocs-d2-plugin %_description

%prep
%autosetup -p1 -n mkdocs_d2_plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l d2

%check
%pyproject_check_import

%files -n python3-mkdocs-d2-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
