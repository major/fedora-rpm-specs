%global uuid org.gnome.BreakTimer

Name: gnome-break-timer
Version: 2.0.3
Release: 5%{?dist}
Summary: Break timer application for GNOME

License: GPLv3+
URL: https://wiki.gnome.org/Apps/BreakTimer
Source0: https://gitlab.gnome.org/GNOME/gnome-break-timer/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gsound)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libnotify)

Requires: dbus-common
Requires: hicolor-icon-theme

%description
This helps you to schedule regular breaks. It will remind you to take them
based on how much you are using the computer. It tries to be simple but
helpful, and it uses notifications to indicate when a break has arrived.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md ABOUT-NLS AUTHORS NEWS
%{_bindir}/%{name}-*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml
%{_sysconfdir}/xdg/autostart/*.desktop


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.3-1
- Initial package
