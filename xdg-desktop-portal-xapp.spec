Name:           xdg-desktop-portal-xapp
Version:        1.0.2
Release:        2%{?dist}
Summary:        Backend implementation for xdg-desktop-portal using Xapp

License:        LGPL-2.1-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(xdg-desktop-portal) >= 1.7.1
BuildRequires:  systemd-rpm-macros

Requires:       dbus-x11
Requires:       dbus-common
Requires:       xapps >= 2.5.0
Requires:       xdg-desktop-portal >= 1.7.1
Requires:       xdg-desktop-portal-gtk
Supplements:    cinnamon

%description
Xapp's Cinnamon, MATE and XFCE backends for xdg-desktop-portal.
This allows sandboxed applications to request services and information from
outside the sandbox in the MATE, XFCE and Cinnamon environments.

%prep
%autosetup -p1


%build
%meson -Dsystemduserunitdir=%{_userunitdir}
%meson_build


%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license COPYING
%doc README.md
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.xapp.service
%{_datadir}/xdg-desktop-portal/portals/xapp.portal
%{_userunitdir}/xdg-desktop-portal-xapp.service


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Leigh Scott <leigh123linux@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Thu Jun 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Fri May 26 2023 Leigh Scott <leigh123linux@gmail.com> - 1.0.0-1
- Initial build
