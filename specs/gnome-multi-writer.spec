Name:      gnome-multi-writer
Version:   3.35.90
Release:   15%{?dist}
Summary:   Write an ISO file to multiple USB devices at once

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Apps/MultiWriter
Source0:   https://download.gnome.org/sources/gnome-multi-writer/3.35/gnome-multi-writer-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: itstool
BuildRequires: libcanberra-devel >= 0.10
BuildRequires: libgusb-devel >= 0.2.4
BuildRequires: libudisks2-devel
BuildRequires: libgudev1-devel
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: polkit-devel
BuildRequires: gcc

%description
GNOME MultiWriter can be used to write an ISO file to multiple USB devices
simultaneously.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS
%{_bindir}/gnome-multi-writer
%{_libexecdir}/gnome-multi-writer-probe
%{_datadir}/applications/org.gnome.MultiWriter.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.MultiWriter.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.gnome.MultiWriter.appdata.xml
%{_datadir}/polkit-1/actions/org.gnome.MultiWriter.policy
%{_mandir}/man1/gnome-multi-writer.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.35.90-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Richard Hughes <rhughes@redhat.com> - 3.35.90-2
- Remove requires which no longer exists

* Wed Mar 04 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Richard Hughes <rhughes@redhat.com> - 3.32.1-1
- Update to 3.32.1
- This fixes a memory corruption issue causing the UI to crash.

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-2
- Remove obsolete scriptlets

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90
- Switch to the meson build system

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Sat Mar 11 2017 Richard Hughes <rhughes@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Mon Feb 15 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 15 2015 Richard Hughes <rhughes@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Mon Mar 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91
- Use the %%license macro for the COPYING file

* Fri Feb 13 2015 Richard Hughes <rhughes@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Mon Jan 19 2015 Richard Hughes <richard@hughsie.com> 3.15.4-1
- New upstream release
- Add quirks for the 36 port MegaHub
- Fix crash when libusb context creation fails
- Lots of new translations
- Never use the USB platform ID for the hub label
- Show the size next to the device name when the device is idle
- Support root hubs with bus numbers >= 8
- Unmount all partitions when a device is inserted

* Fri Jan 09 2015 Richard Hughes <richard@hughsie.com> 3.15.2-2
- Depend on a new enough version of libgusb
- Depend on the correct icon sets being installed
- Resolves: #1180630, #1180610

* Fri Jan 09 2015 Richard Hughes <richard@hughsie.com> 3.15.2-1
- New upstream release
- Make the verification and wipe optional
- Queue the device writes according to the connected root hub
- Show a warning dialog before copying for the first time
- Show some global read/write stats in the title bar
- Use GUsb to renumber composite hubs

* Sun Jan 04 2015 Richard Hughes <richard@hughsie.com> 3.15.1-1
- First attempt at packaging
