Name:           gnome-online-accounts-gtk
Version:        3.50.3
Release:        3%{?dist}
Summary:        GUI Utility for logging into online accounts
License:        GPL-3.0-or-later
URL:            https://github.com/xapp-project/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/pull/14.patch#/fix_gtk415_compile.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(goa-1.0) >= 3.50
BuildRequires:  pkgconfig(goa-backend-1.0) >= 3.50
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)


%description
GUI Utility for logging into online accounts for the
purpose of syncing mail, contacts and remote filesystems.

%prep
%autosetup -p1

%build
%meson
%meson_build


%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/gnome-online-accounts-gtk
%{_datadir}/applications/gnome-online-accounts-gtk.desktop
%{_datadir}/icons/hicolor/scalable/apps/gnome-online-accounts-gtk.svg

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Leigh Scott <leigh123linux@gmail.com> - 3.50.3-1
- Update to 3.50.3

* Sun Apr 21 2024 Leigh Scott <leigh123linux@gmail.com> - 3.50.2-1
- Update to 3.50.2

* Thu Mar 28 2024 Leigh Scott <leigh123linux@gmail.com> - 3.50.1-1
- Initial build

