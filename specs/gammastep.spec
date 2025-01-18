Name:           gammastep
Version:        2.0.9
Release:        10%{?dist}
Summary:        Adjusts the color temperature of your screen according to time of day

# src/gamma-control.xml is licensed under MIT
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:            https://gitlab.com/chinstrap/gammastep
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0) >= 2.26
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner) >= 1.15.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  python3-devel >= 3.2
BuildRequires:  systemd-rpm-macros

Requires:       hicolor-icon-theme

%description
Gammastep adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in front
of the screen at night.

The color temperature is set according to the position of the sun. A different
color temperature is set during night and daytime. During twilight and early
morning, the color temperature transitions smoothly from night to daytime
temperature to allow your eyes to slowly adapt.

Gammastep supports wlr-gamma-control-unstable-v1 protocol for wlroots-based
wayland compositors.

%package        indicator
Summary:        GTK indicator applet for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3
Requires:       libappindicator-gtk3
Requires:       python3dist(pygobject)
Requires:       python3dist(pyxdg)

%description    indicator
This package provides a status icon for %{name} that allows the user
to control color temperature.


%prep
%autosetup -p1 -n %{name}-v%{version}


%build
./bootstrap
%configure \
    --with-systemduserunitdir=%{_userunitdir}
%make_build


%install
%make_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}.service

%post indicator
%systemd_user_post %{name}-indicator.service

%preun
%systemd_user_preun %{name}.service

%preun indicator
%systemd_user_preun %{name}-indicator.service


%files -f %{name}.lang
%license COPYING
%doc README.md %{name}.conf.sample
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_userunitdir}/%{name}.service

%files indicator
%{_bindir}/%{name}-indicator
%{_datadir}/applications/%{name}-indicator.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-status-*.svg
%{_metainfodir}/%{name}-indicator.appdata.xml
%{_userunitdir}/%{name}-indicator.service
%{python3_sitelib}/%{name}_indicator/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.9-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.9-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.9-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 16 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9 (#2125940)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.8-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8 (#2035160)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.7-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7 (#1916565)

* Sun Dec 13 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6

* Fri Nov 20 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Thu Sep 17 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.2-1
- Initial import (#1878350)
