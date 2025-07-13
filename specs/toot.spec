%global modname toot

Name:           %{modname}
Version:        0.48.1
Release:        %autorelease
Summary:        A CLI and TUI tool for interacting with Mastodon

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/ihabunek/%{modname}
Source0:        https://github.com/ihabunek/%{modname}/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# https://github.com/ihabunek/toot/issues/540
# but tui is broken
Patch0:         urwid.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(setuptools-scm) >= 8
BuildRequires:  python3dist(wheel) python3dist(pytest) python3dist(pillow)

%description
Toot is a CLI and TUI tool for interacting with Mastodon instances
from the command line.

%prep
%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install

%check
%{python3} -m pytest -k 'not test_console' --ignore=tests/tui/test_rich_text.py 

%files -n %{modname}
%{_bindir}/toot
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}.dist-info/
%license LICENSE

%changelog
%autochangelog
