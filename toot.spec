%global modname toot

Name:           %{modname}
Version:        0.28.0
Release:        4%{?dist}
Summary:        A CLI and TUI tool for interacting with Mastodon

License:        GPLv3
URL:            https://github.com/ihabunek/%{modname}
Source0:        https://github.com/ihabunek/%{modname}/releases/download/%{version}/%{modname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/ihabunek/%{modname}/%{version}/LICENSE

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist pytest} %{py3_dist requests} %{py3_dist wcwidth} %{py3_dist beautifulsoup4}

%description
Toot is a CLI and TUI tool for interacting with Mastodon instances
from the command line.

%prep
%autosetup -n %{modname}-%{version}
install -m 644 %{SOURCE1} .
rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest

%files -n %{modname}
%{_bindir}/toot
%{python3_sitelib}/%{modname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{modname}
%license LICENSE

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.28.0-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Alessio <alciregi@fedoraproject.org> - 0.28.0-1
- Update to 0.28.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.27.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Alessio <alciregi@fedoraproject.org> - 0.27.0-1
- Initial release
