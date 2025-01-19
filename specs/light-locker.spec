Name:           light-locker
Version:        1.9.0
Release:        15%{?dist}
Summary:        Simple session-locker for lightdm
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later

URL:            https://github.com/the-cavalry/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  xorg-x11-proto-devel

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xxf86vm)

# functional runtime
Requires:       lightdm


%description
light-locker is a simple locker (forked from gnome-screensaver)
that aims to have simple, sane, secure defaults and be well
integrated with the desktop while not carrying any desktop-
specific dependencies.

It relies on lightdm for locking and unlocking your session.


%prep
%autosetup -p1


%build
%meson \
    -Dmit-ext=true \
    -Ddpms-ext=true \
    -Dxf86gamma-ext=true \
    -Dsystemd=true \
    -Dupower=true \
    -Dlate-locking=true \
    -Dlock-on-suspend=true \
    -Dlock-on-lid=true \
    -Dgsettings=true

%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop

%{_bindir}/%{name}
%{_bindir}/%{name}-command

%{_datadir}/glib-2.0/schemas/apps.%{name}.gschema.xml
%{_mandir}/man1/%{name}*.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.0-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 13 2019 Fabio Valentini <decathorpe@gmail.com> - 1.9.0-1
- Update to version 1.9.0.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Raphael Groner <projects.rg@smart.ms> - 1.8.0-1
- new version
- drop upstream patch for systemd (rhbz#1462463)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Björn Esser <besser82@fedoraproject.org> - 1.7.0-4
- Add upstream patch to fix detection of systemd (rhbz#1462463)
- Update spec file to recent guidelines
- Use unmodified git-tree as souces, so patches can be applied easily

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Raphael Groner <projects.rg@smart.ms> - 1.7.0-1
- new version (flagged as pre-release at upstream), rhbz#1275116

* Sun Jul 05 2015 Raphael Groner <projects.rg@smart.ms> - 1.6.0-4
- enforce lock on suspend

* Sun Jul 05 2015 Raphael Groner <projects.rg@smart.ms> - 1.6.0-3
- fix NotShowIn desktop file entry

* Fri Jun 26 2015 Raphael Groner <projects.rg@smart.ms> - 1.6.0-2
- fix license, enhance build options, add gsettings schema scriplets

* Tue May 26 2015 Raphael Groner <projects.rg@smart.ms> - 1.6.0-1
- initial
