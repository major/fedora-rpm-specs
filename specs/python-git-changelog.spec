%bcond check 0

Name:           python-git-changelog
Version:        2.7.0
Release:        %autorelease
Summary:        Automatic Changelog generator using Jinja2 templates
License:        ISC
URL:            https://github.com/pawamoy/git-changelog
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(prep): -n git-changelog-%{version}
%if %{with check}
BuildRequires:  python3dist(pytest)
# griffe not packaged
BuildRequires:  python3dist(griffe)
# mkdocstrings not packaged
BuildRequires:  python3dist(mkdocstrings)
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
sed -i 's/Jinja2>=[0-9]\+\.[0-9]\+/Jinja2/' pyproject.toml
sed -i 's/platformdirs>=[0-9]\+\.[0-9]\+/platformdirs/' pyproject.toml
git tag %{version}

%if %{with check}
%check
%pytest
%endif

%files -n python3-git-changelog -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/git-changelog

%changelog
%autochangelog
