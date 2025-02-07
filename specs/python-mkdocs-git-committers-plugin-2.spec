Name:           python-mkdocs-git-committers-plugin-2
Version:        2.4.1
Release:        %autorelease
Summary:        MkDocs plugin to create a list of contributors on the page

License:        MIT
URL:            https://github.com/ojacques/mkdocs-git-committers-plugin-2/
Source:         %{pypi_source mkdocs_git_committers_plugin_2}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides an MkDocs plugin to create a list of contributors on the
page. The git-committers plugin will seed the template context with a list of
GitHub or GitLab committers and other useful GIT info such as last modified
date.}

%description %_description

%package -n     python3-mkdocs-git-committers-plugin-2
Summary:        %{summary}

%description -n python3-mkdocs-git-committers-plugin-2 %_description

%prep
%autosetup -p1 -n mkdocs_git_committers_plugin_2-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_git_committers_plugin_2

%check
%pyproject_check_import

%files -n python3-mkdocs-git-committers-plugin-2 -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
