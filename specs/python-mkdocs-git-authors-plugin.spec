# Disable due to circular dependency with
# python-mkdocs-git-revision-date-localized-plugin
%bcond tests 0
%global forgeurl https://github.com/timvink/mkdocs-git-authors-plugin

Name:           python-mkdocs-git-authors-plugin
Version:        0.9.2
Release:        %autorelease
Summary:        Mkdocs plugin to display git authors of a page

License:        MIT
URL:            https://timvink.github.io/mkdocs-git-authors-plugin
# PyPI tarball is missing test fixtures
Source:         %{forgeurl}/archive/v%{version}/mkdocs-git-authors-plugin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(gitpython)
BuildRequires:  python3dist(mkdocs-git-revision-date-localized-plugin)
BuildRequires:  python3dist(mkdocs-material)
BuildRequires:  python3dist(mkdocs-macros-plugin)
BuildRequires:  python3dist(mkdocs-mkapi)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This package provides a lightweight MkDocs plugin to display git authors of a
markdown page.}

%description %_description

%package -n     python3-mkdocs-git-authors-plugin
Summary:        %{summary}

%description -n python3-mkdocs-git-authors-plugin %_description

%prep
%autosetup -p1 -n mkdocs-git-authors-plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_git_authors_plugin

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-git-authors-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
