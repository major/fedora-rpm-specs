%global modname toot

Name:           %{modname}
Version:        0.33.1
Release:        2%{?dist}
Summary:        A CLI and TUI tool for interacting with Mastodon

License:        GPLv3
URL:            https://github.com/ihabunek/%{modname}
Source0:        https://github.com/ihabunek/%{modname}/releases/download/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist pytest} %{py3_dist requests} %{py3_dist wcwidth} %{py3_dist beautifulsoup4}
BuildRequires:  %{py3_dist urwid} %{py3_dist psycopg2}

%description
Toot is a CLI and TUI tool for interacting with Mastodon instances
from the command line.

%prep
%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest -k 'not test_console'

%files -n %{modname}
%{_bindir}/toot
%{python3_sitelib}/%{modname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{modname}
%license LICENSE

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

%autochangelog
