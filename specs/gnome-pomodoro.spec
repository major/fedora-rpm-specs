%global uuid pomodoro@arun.codito.in
%global gittag %{version}

Epoch:          1
Name:           gnome-pomodoro
Version:        0.26.0
Release:        2%{?dist}
Summary:        A time management utility for GNOME

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gnomepomodoro.org/
Source0:        https://github.com/gnome-pomodoro/gnome-pomodoro/archive/%{gittag}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(json-glib-1.0)

# For gnome shell extension part of gnome-pomodoro
Requires:       gnome-shell >= 40.0
Requires:       hicolor-icon-theme
# For /usr/share/dbus-1/services ownership
Requires:       dbus-common

# Provides/Obsoletes added in F35 due to package rename
Provides:       gnome-shell-extension-pomodoro = %{epoch}:%{version}-%{release}
Obsoletes:      gnome-shell-extension-pomodoro < 1:0.19.2-1

%description
This GNOME utility helps to manage time according to Pomodoro Technique.
It intends to improve productivity and focus by taking short breaks.

%prep
%autosetup -n gnome-pomodoro-%{gittag}

%build
%meson
%meson_build

%install
%meson_install

# Remove unneeded unversioned symlink
rm %{buildroot}%{_libdir}/lib%{name}.so

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Pomodoro.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/*/org.gnome.Pomodoro.appdata.xml

%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{_bindir}/gnome-pomodoro
%{_libdir}/gnome-pomodoro
%{_libdir}/libgnome-pomodoro.so*
%{_datadir}/gnome-pomodoro
%{_datadir}/*/org.gnome.Pomodoro.appdata.xml
%{_datadir}/applications/org.gnome.Pomodoro.desktop
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/glib-2.0/schemas/org.gnome.pomodoro.*
%{_datadir}/dbus-1/services/org.gnome.Pomodoro.service

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Vicente Maroto Garzón <vicente.maroto.garzon@c512l.dev> 1:0.26.0-1
- Update to 0.26.0

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.25.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 04 2024 Michal Srb <michal@redhat.com> - 1:0.25.1-1
- Update to 0.25.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1:0.24.0-1
- Update to latest release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 22 2023 Jaka Hudoklin <jaka@x-truder.net> - 1:0.23.1-1
- Update to latest upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Jaka Hudoklin <jaka@x-truder.net> - 1:0.22.0-1
- Update to latest upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 13 2022 Mat Booth <mat.booth@gmail.com> - 1:0.21.1-1
- Update to latest upstream release

* Tue Apr 12 2022 Mat Booth <mat.booth@gmail.com> - 1:0.21.0-1
- Update to latest upstream release

* Mon Mar 14 2022 Mat Booth <mat.booth@gmail.com> - 1:0.20.1-0.1
- Use latest gnome-42 branch snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Mat Booth <mat.booth@gmail.com> - 1:0.20.0-1
- Update to latest upstream release

* Fri Sep 03 2021 Mat Booth <mat.booth@gmail.com> - 1:0.19.2-0.3
- Remove unverioned .so symlink (not a dev package), be more strict with
  obsoletes version and add explicit requirement on dbus-common

* Fri Aug 27 2021 Mat Booth <mat.booth@gmail.com> - 1:0.19.2-0.2
- Rename package to gnome-pomodoro

* Fri Aug 27 2021 Mat Booth <mat.booth@gmail.com> - 1:0.19.2-0.1
- Update to snapshot of gnome-40 branch to fix rhbz#1963736 (upstream bug #554)
- Allow loading on Gnome 41 for Fedora 35 support
- Switch to meson build system

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 05 2021 Mat Booth <mbooth@apache.org> - 1:0.19.0-1
- Update for Gnome 40 support

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Mat Booth <mat.booth@redhat.com> - 1:0.18.0-1
- Update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 01 2020 Mat Booth <mat.booth@redhat.com> - 1:0.17.0-1
- Update to version 0.17.0 of pomodoro

* Wed Apr 01 2020 Mat Booth <mat.booth@redhat.com> - 1:0.16.0-1
- Update to version 0.16.0 of pomodoro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.2-0.2.gitcb1ad32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Mat Booth <mat.booth@redhat.com> - 1:0.15.2-0.1
- Update to pre-release snapshot of 0.15.2 for gnome-shell 3.34 support

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Mat Booth <mat.booth@redhat.com> - 1:0.15.1-2
- Bump epoch due to downgrade needed for F29

* Mon Apr 15 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.1-1
- Update to 0.15.1
- Remove unneeded patch
- Use autosetup

* Wed Feb 13 2019 Mat Booth <mat.booth@redhat.com> - 0.14.0-4
- Fix failure to build from source

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.14.0-3
- Update BRs for vala packaging changes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Mat Booth <mat.booth@redhat.com> - 0.14.0-1
- Update to latest upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Mat Booth <mat.booth@redhat.com> - 0.13.4-4
- Remove no longer necessary ldconfig invocations

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.4-2
- Remove obsolete scriptlets

* Wed Nov 22 2017 Mat Booth <mat.booth@redhat.com> - 0.13.4-1
- Update to latest upstream release

* Fri Sep 22 2017 Mat Booth <mat.booth@redhat.com> - 0.13.3-1
- Update to latest upstream release
- Adds support for GNOME Shell 3.26

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 08 2017 Mat Booth <mat.booth@redhat.com> - 0.13.2-1
- Update to latest upstream release

* Tue Feb 21 2017 Mat Booth <mat.booth@redhat.com> - 0.13.1-1
- Update to latest release
- Drop upstreamed patches

* Fri Feb 17 2017 Mat Booth <mat.booth@redhat.com> - 0.13.0-5
- Fix compilation with new version of vala

* Fri Feb 17 2017 Mat Booth <mat.booth@redhat.com> - 0.13.0-4
- Backport a patch from upstream to fix a crash during initial startup
- rhbz#1422595, rhbz#1422981

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Ville SkyttÃ¤ <ville.skytta@iki.fi> - 0.13.0-2
- Build with $RPM_OPT_FLAGS, verbosely
- Install COPYING as %%license

* Tue Jan 17 2017 Mat Booth <mat.booth@redhat.com> - 0.13.0-1
- Update to latest upstream release

* Mon Oct 31 2016 Mat Booth <mat.booth@redhat.com> - 0.12.3-1
- Update to latest upstream release for Gnome 3.22 compatibility

* Mon Jul 04 2016 Mat Booth <mat.booth@redhat.com> - 0.12.1-1
- Update to latest upstream release

* Sat May 07 2016 Mat Booth <mat.booth@redhat.com> - 0.11.3-1
- Update to latest upstream release

* Sat Apr 23 2016 Mat Booth <mat.booth@redhat.com> - 0.11.2-1
- Update to latest release for Gnome 3.20 compatibility

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Mat Booth <mat.booth@redhat.com> - 0.11.0-1
- Update to 0.11.0 release
- Add patch for gnome-shell >= 3.17 support

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-0.3.gitc7ad79d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Mat Booth <mat.booth@redhat.com> - 0.11.0-0.2.gitc7ad79d3
- Update to latest snapshot for gnome 3.16 support

* Mon Sep 29 2014 Mat Booth <mat.booth@redhat.com> - 0.11.0-0.1.git656e0643
- Update to git snapshot of 0.11.0 for gnome 3.14 support

* Mon Sep 29 2014 Mat Booth <mat.booth@redhat.com> - 0.10.2-1
- Update to upstream version 0.10.2

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 0.10.0-6
- Rebuilt for upower 0.99.1 soname bump

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Mat Booth <fedora@matbooth.co.uk> - 0.10.0-3
- Rebuilt for new gnome

* Thu Feb 13 2014 Mat Booth <fedora@matbooth.co.uk> - 0.10.0-2
- Extra BRs required on F21

* Tue Feb 11 2014 Mat Booth <fedora@matbooth.co.uk> - 0.10.0-1
- Update to upstream version 0.10.0
- Require gnome-shell 3.10
- gnome-pomodoro is no longer a noarch package

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Mat Booth <fedora@matbooth.co.uk> - 0.8-1
- Update to upstream version 0.8
- Require gnome-shell 3.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Mat Booth <fedora@matbooth.co.uk> - 0.7-1
- Update to upstream version 0.7
- Require gnome-shell 3.6

* Mon Nov 19 2012 Mat Booth <fedora@matbooth.co.uk> - 0.6-1
- Update to upstream version 0.6
- Require gnome-shell 3.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitdf98ce0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.4.gitdf98ce0
- Updated to new upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git13030cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Fabian Affolter <fabian@bernewireless.net> - 0-0.2.git13030cd
- License is GPLv3+
- COPYING file added

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 0-0.1.git286a249
- Initial package for Fedora
