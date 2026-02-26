%bcond check 1

Name:           python-git-changelog
Version:        2.7.1
Release:        %autorelease
Summary:        Automatic Changelog generator using Jinja2 templates
License:        ISC
URL:            https://github.com/pawamoy/git-changelog
Source:         %{url}/archive/%{version}/git-changelog-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(prep): -n git-changelog-%{version}
%if %{with check}
BuildRequires:  python3dist(pytest)
# griffe not packaged
#BuildRequires:  python3dist(griffe)
# mkdocstrings not packaged
#BuildRequires:  python3dist(mkdocstrings)
BuildRequires:  python3dist(pytest-gitconfig)
%endif
BuildOption(install): -l git_changelog
BuildRequires:  git-core

%global _description %{expand:
git-changelog parses your commit messages to extract useful data that is then
rendered using Jinja2 templates, for example to a changelog file formatted in
Markdown.

Each Git tag will be treated as a version of your project. Each version contains
a set of commits, and will be an entry in your changelog. Commits in each
version will be grouped by sections, depending on the commit coonvention you
follow.}

%description %_description

%package -n python3-git-changelog
Requires:       git-core
Summary:        %{summary}

%description -n python3-git-changelog %_description

%prep -a
%autosetup -n git-changelog-%{version} -S git
git tag %{version}

%check
%pyproject_check_import
%if %{with check}
# Requires griffe and mkdocstrings, both not packaged
ignore="${ignore-} --ignore=tests/test_api.py"
%pytest -v -rs ${ignore-}
%endif

%files -n python3-git-changelog -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/git-changelog

%changelog
%autochangelog
