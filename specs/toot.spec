%global modname toot

Name:           %{modname}
Version:        0.52.1
Release:        %autorelease
Summary:        A CLI and TUI tool for interacting with Mastodon

License:        GPL-3.0-only
URL:            https://github.com/ihabunek/%{modname}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(setuptools-scm) >= 8
BuildRequires:  python3dist(wheel)

%description
Toot is a CLI and TUI tool for interacting with Mastodon instances
from the command line.

%prep
%autosetup -n %{modname}-%{version} -p1
rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'
# Relax urwid dependency to allow urwid >= 3.0 (including 4.x)
sed -i 's/"urwid\~=3.0"/"urwid>=3.0"/' pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest -k "not test_console" --ignore=tests/tui/test_rich_text.py

%files -n %{modname} -f %{pyproject_files}
%{_bindir}/toot
%doc README.rst
%license LICENSE

%changelog
%autochangelog
