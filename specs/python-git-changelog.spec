%bcond check 1

Name:           python-git-changelog
Version:        2.12.0
Release:        %autorelease
Summary:        Automatic Changelog generator using Jinja2 templates
License:        ISC
URL:            https://github.com/pawamoy/git-changelog
Source:         %{url}/archive/%{version}/git-changelog-%{version}.tar.gz

# tests: Fix remote URL (/ instead of :)
# https://github.com/pawamoy/git-changelog/commit/ba7609d33e01066e40b1e8f9c55e950e0bdb7c76
#
# Fixes:
#
# bug: Python 3.16.0a2: `test_removing_credentials_from_remotes` fails
# https://github.com/pawamoy/git-changelog/issues/148
Patch:          %{url}/commit/ba7609d33e01066e40b1e8f9c55e950e0bdb7c76.patch

BuildArch:      noarch

BuildSystem:    pyproject
BuildOption(install): -l git_changelog

%if %{with check}
BuildRequires:  python3dist(pytest)
# griffe not packaged
#BuildRequires:  python3dist(griffe)
# mkdocstrings not packaged
#BuildRequires:  python3dist(mkdocstrings)
BuildRequires:  python3dist(pytest-gitconfig)
%endif
BuildRequires:  git-core

%global _description %{expand:
Automatic Changelog generator using Jinja2 templates. From git logs to change
logs.

Features:

  • Jinja2 templates! You get full control over the rendering. Built-in Keep a
    Changelog and Angular templates (also see Conventional Changelog).
  • Commit styles/conventions parsing. Built-in Angular, Conventional Commit
    and basic conventions.
  • Git service/provider agnostic, plus references parsing (issues, commits,
    etc.). Built-in GitHub, Gitlab and Bitbucket support.
  • Understands SemVer and PEP 440 versioning schemes. Guesses next version
    based on last commits.
  • Parses Git trailers, allowing to reference issues, PRs, etc., in your
    commit messages in a clean, provider-agnostic way.
  • Template context injection, to furthermore customize how your changelog
    will be rendered.

Todo:

  • Plugin architecture, to support more commit conventions and git services.
  • Easy access to “Breaking Changes” in the templates.}

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
%pytest -v -rs ${ignore-} -k "${k-}"
%endif

%files -n python3-git-changelog -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%{_bindir}/git-changelog

%changelog
%autochangelog
