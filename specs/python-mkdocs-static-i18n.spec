Name:           python-mkdocs-static-i18n
Version:        1.3.0
Release:        %autorelease
Summary:        MkDocs i18n plugin using static translation Markdown files

License:        MIT
URL:            https://ultrabug.github.io/mkdocs-static-i18n/
Source:         %{pypi_source mkdocs_static_i18n}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
The mkdocs-static-i18n plugin allows you to support multiple languages of your
documentation by adding static translation files to your existing documentation
pages.}

%description %_description

%package -n     python3-mkdocs-static-i18n
Summary:        %{summary}

%description -n python3-mkdocs-static-i18n %_description

%pyproject_extras_subpkg -n python3-mkdocs-static-i18n material

%prep
%autosetup -p1 -n mkdocs_static_i18n-%{version}

%generate_buildrequires
%pyproject_buildrequires -x material

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_static_i18n

%check
%pytest -v

%files -n python3-mkdocs-static-i18n -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
