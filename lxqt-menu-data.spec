Name:    lxqt-menu-data
Summary: Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt
Version: 1.4.1
Release: 3%{?dist}
BuildArch: noarch
License: LGPL-2.1-or-later
URL:     https://lxqt-project.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  lxqt-build-tools
BuildRequires:  qt5-linguist

%description
Freedesktop.org compliant menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt.

%prep
%autosetup -p1

%build
%cmake -DUSE_QT5=TRUE -DPULL_TRANSLATIONS=NO
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc CHANGELOG README.md
%{_datadir}/cmake/lxqt-menu-data/
%{_datadir}/desktop-directories/lxqt-*.directory
%{_sysconfdir}/xdg/menus/lxqt-*.menu

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 26 2023 Zamir SUN <sztsian@gmail.com> - 1.4.1-1
- Initial package
