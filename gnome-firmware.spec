%global uuid    org.gnome.Firmware
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-firmware
Version:        43.1
Release:        2%{?dist}
Summary:        Install firmware on devices

License:        GPLv2+
URL:            https://gitlab.gnome.org/hughsie/gnome-firmware
Source0:        https://people.freedesktop.org/~hughsient/releases/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.0
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(fwupd) >= 1.2.10
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  pkgconfig(xmlb) >= 0.1.7
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       hicolor-icon-theme

%description
This application can:

- Upgrade, downgrade and reinstall firmware on devices supported by fwupd.
- Unlock locked fwupd devices
- Verify firmware on supported devices
- Display all releases for a fwupd device

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Dman=true
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md MAINTAINERS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*.1.*
%{_metainfodir}/*.xml

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 07 2022 Richard Hughes <rhughes@redhat.com> - 43.1-1
- New upstream release

* Fri Sep 16 2022 Richard Hughes <rhughes@redhat.com> - 43.0-1
- New upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 12 2022 Richard Hughes <rhughes@redhat.com> - 42.1-1
- New upstream release

* Thu Mar 31 2022 Richard Hughes <rhughes@redhat.com> - 42.0-1
- New upstream release
- Port to GTK4
- Add the device branch to the device page
- Allow installing firmware with the AFFECTS_FDE flag

* Thu Feb 17 2022 Richard Hughes <rhughes@redhat.com> - 42~beta-1
- New upstream release
- Correctly print release flags
- Enable releases leaflet gestures to be more adaptable
- Hide the back button when folded

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Richard Hughes <rhughes@redhat.com> - 41.0-1
- New upstream release
- Add support for showing the update message
- Add support for switching branch
- Send the client features at startup
- Show a FDE warning when required
- Show composite devices clearly
- Use libhandy to make UI responsive
- Use the new API from fwupd to avoid blocking the main thread

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Mohan Boddu <mboddu@bhujji.com> - 3.36.0-4
- Rebuild for the libxmlb API bump.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Richard Hughes <rhughes@redhat.com> - 3.36.0-1
- New upstream release
- Dynamically show verify and releases buttons
- Show device and progress when doing updates
- Show the release issues if supplied in the metadata

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.34.0-4
- Update to 3.34.0

* Wed Sep 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-4.20190911git9d823d8
- Update to latest git snapshot

* Wed Aug 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20190827gitd5014ed
- Initial package

