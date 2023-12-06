%define gettext_package gnome-terminal

%global gettext_version 0.19.8
%define glib2_version 2.52.0
%define gtk3_version 3.24.0
%define vte_version 0.68.0
%define desktop_file_utils_version 0.2.90

Name:    gnome-terminal
Version: 3.48.3
Release: 1%{?dist}
Summary: Terminal emulator for GNOME

License: GPL-3.0-or-later AND GFDL-1.3
URL:     https://wiki.gnome.org/Apps/Terminal
Source0: https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1: org.gnome.Terminal.gschema.override

Patch0:  gnome-terminal-cntr-ntfy-autottl-ts.patch

BuildRequires: pkgconfig(dconf)
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(libnautilus-extension-4)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(vte-2.91) >= %{vte_version}
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: docbook-style-xsl
BuildRequires: gettext-devel >= %{gettext_version}
BuildRequires: gcc-c++
BuildRequires: gnome-shell
BuildRequires: itstool
BuildRequires: libxslt
BuildRequires: meson
BuildRequires: systemd-rpm-macros
BuildRequires: yelp-tools
BuildRequires: /usr/bin/appstream-util

Requires: dbus
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gsettings-desktop-schemas
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: vte291%{?_isa} >= %{vte_version}

%description
gnome-terminal is a terminal emulator for GNOME. It features the ability to use
multiple terminals in a single window (tabs) and profiles support.

%package nautilus
Summary: GNOME Terminal extension for Nautilus
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides: nautilus-open-terminal = %{version}-%{release}
Obsoletes: nautilus-open-terminal < 0.20-8

%description nautilus
This package provides a Nautilus extension that adds the 'Open in Terminal'
option to the right-click context menu in Nautilus.

%prep
%autosetup -p1

%build
%meson \
    -Ddebug=true \
    -Ddocs=true \
    -Dnautilus_extension=true \
    -Dsearch_provider=true

%meson_build

%install
%meson_install

install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas

%find_lang %{gettext_package} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Terminal*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Terminal.desktop
%meson_test

%files -f %{gettext_package}.lang
%license COPYING COPYING.GFDL
%doc README.md
%{_bindir}/gnome-terminal
%{_datadir}/applications/org.gnome.Terminal.desktop
%{_datadir}/applications/org.gnome.Terminal.Preferences.desktop
%{_libexecdir}/gnome-terminal-preferences
%{_libexecdir}/gnome-terminal-server
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.override
%{_datadir}/gnome-shell
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Terminal.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Terminal-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Terminal.Preferences.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Terminal.Preferences-symbolic.svg
%dir %{_datadir}/xdg-terminals
%{_datadir}/xdg-terminals/org.gnome.Terminal.desktop
%dir %{_libdir}/gnome-terminal
%{_libdir}/gnome-terminal/gschemas.compiled
%{_mandir}/man1/gnome-terminal.1*
%{_metainfodir}/org.gnome.Terminal.metainfo.xml
%{_userunitdir}/gnome-terminal-server.service

%files nautilus
%{_libdir}/nautilus/extensions-4/libterminal-nautilus.so
%{_metainfodir}/org.gnome.Terminal.Nautilus.metainfo.xml

%changelog
* Mon Dec 04 2023 David King <amigadave@amigadave.com> - 3.48.3-1
- Update to 3.48.3

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.48.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 09 2023 David King <amigadave@amigadave.com> - 3.48.1-1
- Update to 3.48.1

* Mon Mar 20 2023 David King <amigadave@amigadave.com> - 3.48.0-1
- Update to 3.48.0

* Mon Feb 27 2023 David King <amigadave@amigadave.com> - 3.47.92-1
- Update to 3.47.92

* Thu Feb 16 2023 David King <amigadave@amigadave.com> - 3.46.8-1
- Update to 3.46.8

* Mon Jan 23 2023 David King <amigadave@amigadave.com> - 3.46.7-1
- Update to 3.46.7 (#2155523)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.45.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 17 2022 David King <amigadave@amigadave.com> - 3.45.90-1
- Update to 3.45.90

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.44.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 29 2022 David King <amigadave@amigadave.com> - 3.44.1-1
- Update to 3.44.1

* Mon Feb 14 2022 David King <amigadave@amigadave.com> - 3.44.0-1
- Update to 3.44.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 David King <amigadave@amigadave.com> - 3.42.2-1
- Update to 3.42.2

* Wed Nov 03 2021 David King <amigadave@amigadave.com> - 3.42.1-1
- Update to 3.42.1

* Tue Sep 28 2021 David King <amigadave@amigadave.com> - 3.42.0-1
- Update to 3.42.0

* Tue Aug 24 2021 David King <amigadave@amigadave.com> - 3.40.3-1
- Update to 3.40.3
- Minor packaging improvements
- Use pkgconfig for BuildRequires
- Drop unnecessary patch

* Wed Aug 04 2021 Kalev Lember <klember@redhat.com> - 3.40.2-3
- BuildRequire systemd-rpm-macros rather than systemd

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.40.2-1
- Update to 3.40.2
- Backport yet-to-be-released patches from upstream to avoid translation
  conflicts

* Mon May 31 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.40.1-2
- Bump required vte291 version
- Update the downstream patches to include a soft assertion

* Tue May 11 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.40.1-1
- Update to 3.40.1
- Rebase the translations
- Backport yet-to-be-released patches from upstream to avoid translation
  conflicts

* Tue May 11 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.40.0-1
- Update to 3.40.0

* Mon May 10 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.39.90-1
- Update to 3.39.90
- Rebase the patches
- Backport yet-to-be-released patches from upstream to avoid translation
  conflicts

* Fri May 07 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.38.3-1
- Update to 3.38.3
- Rebase the translations
- Backport yet-to-be-released patches from upstream to avoid translation
  conflicts

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Ting-Wei Lan <lantw44@gmail.com> - 3.38.1-2
- Fix crash when the command line is shorter than 1024 characters

* Mon Oct 12 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.38.1-1
- Update to 3.38.1
- Backport yet-to-be-released patches from upstream

* Sat Sep 26 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.38.0-1
- Update to 3.38.0
- Rebase the patches
- Backport yet-to-be-released patches from upstream

* Sat Sep 26 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.37.90-1
- Update to 3.37.90
- Rebase the patches

* Fri Sep 25 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.36.2-1
- Update to 3.36.2
- Rebase the patches

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.36.1.1-2
- Enable debugging

* Mon Apr 06 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.36.1.1-1
- Update to 3.36.1.1
- Rebase the patches

* Sun Apr 05 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.36.1-1
- Update to 3.36.1
- Rebase the patches

* Fri Mar 06 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.36.0.1-1
- Update to 3.36.0.1

* Thu Mar 05 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.35.92-2
- Limit the command line to 1024 characters when used as the title

* Mon Mar 02 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.35.92-1
- Update to 3.35.92

* Fri Feb 28 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.35.91-1
- Update to 3.35.91
- Rebase the patches
- Backport yet-to-be-released patches from upstream to avoid translation
  conflicts

* Fri Feb 28 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.35.1-1
- Update to 3.35.1
- Rebase the patches

* Mon Feb 24 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.34.2-3
- Add a "shell-command" flag for debugging.
- Backport yet-to-be-released patches from upstream to avoid translation
  conflicts.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0
- Rebase the translations

* Wed Sep 04 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90
- Rebase the patches

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Debarshi Ray <rishi@fedoraproject.org> - 3.32.2-2
- Preserve current toolbox, if any, when opening a new terminal

* Tue May 07 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1
- Rebase the translations

* Wed Apr 03 2019 Debarshi Ray <rishi@fedoraproject.org> - 3.32.0-2
- Automatically update the title with the current foreground process.
- Rewrite the command-notify patches to use the interactive shell's precmd and
  preexec hooks, instead of only the precmd hook and the history.
- Backport yet-to-be-released patches from upstream to avoid translation
  conflicts.

* Fri Mar 29 2019 Debarshi Ray <rishi@fedoraproject.org> - 3.32.0-1
- Update to 3.32.0

* Fri Mar 29 2019 Debarshi Ray <rishi@fedoraproject.org> - 3.31.92-1
- Update to 3.31.92
- Rebase the translations

* Sat Mar 16 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.31.90-4
- Revert previous commit: headerbar will come in 3.32 final

* Sat Mar 16 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.31.90-3
- Enable the headerbar

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.90-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90
- Rebase the translations
- Drop obsolete gnome-common build dep

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2
- Rebase transparency, command-notify, custom title and translation patches

* Thu Oct 11 2018 David Herrmann <dh.herrmann@gmail.com> - 3.30.1-2
- Reduce 'dbus-x11' dependency to 'dbus'. The xinit script are no longer the
  canonical way to start dbus, but the 'dbus' package is nowadays required to
  provide a user and system bus to its dependents.

* Fri Oct 05 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.30.0-1
- Update to 3.30.1
- Rebase transparency, command-notify, custom title and translation patches
- Use a GSettings override to separate the new-terminal menuitems

* Fri Oct 05 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.30.0-1
- Update to 3.30.0

* Fri Oct 05 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.29.92-1
- Update to 3.29.92
- Rebase transparency, command-notify, custom title and translation patches
- Remove upstreamed patches

* Fri Jul 27 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.28.2-4
- Include LGPLv2+ in the list of licenses

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.28.2-2
- Backport fix for client-side memory error (GNOME/gnome-terminal#1)

* Mon May 21 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Fri Apr 13 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.28.1-1
- Update to 3.28.1
- Rebase the translations

* Thu Apr 12 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.27.90-1
- Update to 3.27.90
- Rebase transparency, command-notify and translation patches

* Fri Apr 06 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.27.4-1
- Update to 3.27.4
- Rebase transparency, command-notify and translation patches

* Fri Apr 06 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.27.3-1
- Update to 3.27.3
- Rebase the translations

* Tue Apr 03 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.27.1-1
- Update to 3.27.1
- Rebase transparency, command-notify and translation patches

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2
- Remove obsolete scriptlets

* Thu Nov 02 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2
- Rebase the translations

* Wed Oct 18 2017 Marek Kasik <mkasik@redhat.com> - 3.26.1-2
- Enable unit tests
- Resolves: #1502666

* Thu Oct 12 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1
- Rebase the translations

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0
- Rebase downstream patches

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Kalev Lember <klember@redhat.com> - 3.24.2-1
- Update to 3.24.2
- Rebase the translations

* Thu Apr 13 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1
- Rebase the translations

* Wed Mar 22 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0
- Rebase the translations

* Mon Feb 27 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.23.90-1
- Update to 3.23.90
- Update translations
- Ensure that the transparency scale is sensitive only when a transparent
  background is used
- Rebase transparency, command-notify and translation patches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.22.1-2
- Backport fix for search-provider crash (RH #1398958)
- Update translations

* Tue Nov 08 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.22.1-1
- Update to 3.22.1
- Rebase the translations
- Restore custom terminal titles
- Restore separate menuitems for opening tabs and windows

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Rebase the translations

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92
- Rebase the translations
- Don't set group tags
- Use make_install macro

* Fri Aug 19 2016 Kalev Lember <klember@redhat.com> - 3.21.90-2
- Backport a patch to fix terminal shrinking with every line entered

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Rebase the translations

* Wed Jun 01 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.20.2-2
- Add Provides/Obsoletes to replace nautilus-open-terminal

* Wed May 11 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.20.2-1
- Update to 3.20.2

* Tue May 10 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.20.1-2
- Rebuild against vte291 ABI fix

* Mon Apr 11 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.20.1-1
- Update to 3.20.1
- Rebase the translations

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0
- Rebase the translations

* Thu Mar 17 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.19.92-1
- Update to 3.19.92
- Rebase the translations

* Thu Mar 03 2016 Kalev Lember <klember@redhat.com> - 3.19.91-1
- Update to 3.19.91
- Rebase transparency, command-notify and translation patches

* Thu Feb 18 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.19.2-1
- Update to 3.19.2
- Rebase the translations

* Thu Feb 18 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.19.1-2
- Adjust the dark terminal override to match the new setting

* Thu Feb 11 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.19.1-1
- Update to 3.19.1
- Rebase transparency, command-notify and translation patches
- Dark terminals have been restored upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.18.2-1
- Update to 3.18.2
- Consolidate all downstream features into a single patch to avoid conflicts
- Rebase the translations

* Thu Nov 12 2015 Owen Taylor <otaylor@redhat.com> - 3.18.1-3
- Add patch fixing transparent mode under Wayland

* Sat Oct 31 2015 Kalev Lember <klember@redhat.com> - 3.18.1-2
- Drop GConf migrator for F24 (#1276525)

* Wed Oct 14 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Wed Oct 07 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.18.0-1
- Update to 3.18.0
- Backport a few upstream fixes
- Rebase the translations

* Thu Oct 01 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.17.91-2
- Use a symbolic new tab icon

* Mon Sep 14 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.91-1
- Update to 3.17.91
- Restore translations for dark variant strings
- Rebase the translations for transparency strings

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.16.2-1
- Update to 3.16.2
- Rebase the translations for transparency strings

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Tue Mar 24 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.16.0-1
- Update to 3.16.0
- Rebase the translations for transparency strings

* Tue Mar 17 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.15.92-1
- Update to 3.15.92
- Drop upstreamed patch
- Rebase the translations for transparency strings

* Mon Mar 16 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.15.90-2
- Withdraw the notification on focus-in-event

* Wed Feb 18 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.15.90-1
- Update to 3.15.90
- Restore translations for transparency strings
- Restore dark terminals
- Add command-notify patches

* Mon Jan 26 2015 Adam Williamson <awilliam@redhat.com> - 3.14.2-2
- backport partial fix for BGO#743395

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Sun Sep 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sun Sep 14 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Fri Sep 12 2014 Debarshi Ray <rishi@fedorapeople.org> - 3.13.90-2
- Restore transparency

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.2-1
- Update to 3.13.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.0-2
- Fix parent class in template definition

* Sun Apr 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.0-1
- Update to 3.13.0

* Sat Apr 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Thu Apr 03 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.12.0-2
- Use the dark theme variant

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Mon Mar 10 2014 Kevin Fenzi <kevin@scrye.com> 3.11.3-2
- Rebuild for new gnome-shell
- Own datadir/gnome-shell for search provider

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 3.11.0-2
- Re-issued tarball. Kinda unusual, but such is life.

* Tue Nov 19 2013 Richard Hughes <rhughes@redhat.com> - 3.11.0-1
- Update to 3.11.0

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90
- Package up the nautilus extension in gnome-terminal-nautilus subpackage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  8 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.4-1
- Update to 3.8.4
- Fixes a crash on session resume (#981440)

* Mon Jun 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.3-1
- Update to 3.8.3
- Use desktop-file-validate instead of desktop-file-install

* Mon May 13 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Apr 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0.1-1
- Update to 3.8.0.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 26 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.2-3
- Bring back titlebars on maximized terminals

* Fri Jan 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.2-2
- Backport a fix for a crash in terminal_screen_container_style_updated

* Fri Jan 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1.1-1
- Update to 3.4.1.1

* Tue Mar 27 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0.1-1
- Update to 3.4.0.1
- Avoid listing files twice in %%files

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.0-1
- Update to 3.3.0

* Thu Jan 12 2012 Matthias Clasen <mclasen@redhat.com> - 3.2.1-2
- Update license field (#639132)

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> 3.0.0-1
- Update to 3.0.0

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> 2.33.90-1
- Update to 2.33.90

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> 2.33.5-3
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.33.5-1
- Update to 2.33.5

* Wed Jan 12 2011 Matthias Clasen <mclasen@redhat.com> - 2.33.4-2
- Make the find dialog work again

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.33.4-1
- Update to 2.33.4

* Fri Jan  7 2011 Matthias Clasen <mclasen@redhat.com> - 2.33.3-1
- Update to 2.33.3

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.33.2-2
- Rebuild against new gtk

* Thu Nov 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.33.2-1
- Update to 2.33.2
- Back to gtk3

* Fri Oct  8 2010 Owen Taylor <otaylor@redhat.com> - 2.33.0-3
- Revert back to a gtk2 build - the gtk3 build has major sizing issues
  (rhbz #641337)

* Thu Oct  7 2010 Matthias Clasen <mclasen@redhat.com> - 2.33.0-2
- Build against gtk3

* Mon Oct  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.33.0-1
- Update to 2.33.0

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-1
- Update to 2.31.91

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.90-1
- Update to 2.31.90

* Thu May 27 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.3-1
- Update to 2.31.3

* Tue May  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.2-2
- Add more translations for search UI

* Tue May  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.2-1
- Update to 2.31.2
- Add translations for search UI

* Tue May  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.1-1
- Update to 2.31.1

* Mon Apr 26 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Thu Mar 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.92-1
- Update to 2.29.92

* Sun Feb 14 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.6-3
- Add missing libs

* Thu Jan 14 2010 Behdad Esfahbod <behdad@redhat.com> - 2.29.6-2
- Second try
- Drop stale patch

* Thu Jan 14 2010 Behdad Esfahbod <behdad@redhat.com> - 2.29.6-1
- Update to 2.29.6
