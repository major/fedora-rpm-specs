%bcond tests 1

Name:           python-mkdocs-literate-nav
Version:        0.6.2
Release:        %autorelease
Summary:        MkDocs plugin to specify the navigation in Markdown instead of YAML

License:        MIT
URL:            https://oprypin.github.io/mkdocs-literate-nav
Source:         %{pypi_source mkdocs_literate_nav}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-golden)
%endif

%global _description %{expand:
This package provides a plugin for MkDocs to specify the navigation in Markdown
instead of YAML.}

%description %_description

%package -n     python3-mkdocs-literate-nav
Summary:        %{summary}

%description -n python3-mkdocs-literate-nav %_description

%prep
%autosetup -p1 -n mkdocs_literate_nav-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_literate_nav

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-literate-nav -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
