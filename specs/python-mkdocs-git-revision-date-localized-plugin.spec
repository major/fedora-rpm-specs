%bcond tests 1
%global forgeurl https://github.com/timvink/mkdocs-git-revision-date-localized-plugin

Name:           python-mkdocs-git-revision-date-localized-plugin
Version:        1.3.0
Release:        %autorelease
Summary:        Mkdocs plugin to display the last git modification date

License:        MIT
URL:            https://timvink.github.io/mkdocs-git-revision-date-localized-plugin/
Source:         %{pypi_source mkdocs_git_revision_date_localized_plugin}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  git-core
%endif

%global _description %{expand:
This package is a MkDocs plugin that enables displaying the date of the last
git modification of a page. The plugin uses babel and timeago.js to provide
different localized date formats. It was originally forked from
mkdocs-git-revision-date-plugin.}

%description %_description

%package -n     python3-mkdocs-git-revision-date-localized-plugin
Summary:        %{summary}

%description -n python3-mkdocs-git-revision-date-localized-plugin %_description

%pyproject_extras_subpkg -n python3-mkdocs-git-revision-date-localized-plugin all,base

%prep
%autosetup -p1 -n mkdocs_git_revision_date_localized_plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires -x all,base,dev

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_git_revision_date_localized_plugin

%check
%if %{with tests}
git config --global user.email mock-build@example.com
git config --global user.name 'Mock build'
# Disable tests that need to be run inside a git repository
%pytest -v \
  --deselect='tests/test_builds.py::test_tags_are_replaced[mkdocs file: basic_project/mkdocs_theme_timeago_locale.yml]' \
  --deselect='tests/test_builds.py::test_tags_are_replaced[mkdocs file: basic_project/mkdocs_theme_timeago.yml]' \
  --deselect='tests/test_builds.py::test_tags_are_replaced[mkdocs file: basic_project/mkdocs_theme_timeago_override.yml]' \
  --deselect='tests/test_builds.py::test_tags_are_replaced[mkdocs file: basic_project/mkdocs_theme_timeago_instant.yml]' \
  --deselect='tests/test_builds.py::test_tags_are_replaced[mkdocs file: basic_project/mkdocs_timeago_locale.yml]' \
  --deselect='tests/test_builds.py::test_tags_are_replaced[mkdocs file: basic_project/mkdocs_timeago.yml]' \
  --deselect=tests/test_builds.py::test_build_material_theme \
  --deselect=tests/test_builds.py::test_material_theme_locale \
  --deselect=tests/test_builds.py::test_material_theme_no_locale \
  --deselect=tests/test_builds.py::test_exclude_pages \
  %{nil}
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-git-revision-date-localized-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
