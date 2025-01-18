Name:      gnome-app-list
Version:   1.0
Release:   2%{?dist}
BuildArch: noarch
Summary:   A curated list of apps to feature or highlight in GNOME
License:   LGPL-2.1-or-later
URL:       https://gitlab.gnome.org/GNOME/gnome-app-list/
Source0:   https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires: meson
BuildRequires: /usr/bin/python3
BuildRequires: /usr/bin/xmllint

%description
The %{name} provides an AppStream data, which marks
some apps as featured or highlighted in GNOME.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSES/LGPL-2.1-or-later.txt
%dir %{_datadir}/swcatalog
%dir %{_datadir}/swcatalog/xml
%{_datadir}/swcatalog/xml/org.gnome.App-list.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

%autochangelog
