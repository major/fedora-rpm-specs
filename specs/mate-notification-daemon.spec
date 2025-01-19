# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit f9aedafffba0ecc55072a933f28500c0e24c9bf1}
%{!?rel_build:%global commit_date 20150724}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-notification-daemon
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        5%{?dist}
%else
Release:        0.25%{?git_rel}%{?dist}
%endif
Summary:        Notification daemon for MATE Desktop
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-notification-daemon.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

# https://github.com/mate-desktop/mate-notification-daemon/commit/90b39ec
Patch1: mate-notification-daemon_0001-daemon-Properly-update-the-set-of-monitors-when-it-c.patch

BuildRequires: desktop-file-utils
BuildRequires: gtk-layer-shell-devel
BuildRequires: libcanberra-devel
BuildRequires: libnotify-devel
BuildRequires: libwnck3-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-panel-devel

Provides:      desktop-notification-daemon

%description
Notification daemon for MATE Desktop

%prep
%if 0%{?rel_build}
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure --disable-schemas-compile \
           --enable-x11 \
           --enable-wayland \
           --enable-in-process

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/mate-notification-properties.desktop

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

# remove desktop file, no need of it
rm -f  %{buildroot}%{_datadir}/applications/mate-notification-daemon.desktop

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-notification-daemon.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-notification-properties
%{_datadir}/applications/mate-notification-properties.desktop
%{_datadir}/dbus-1/services/org.freedesktop.mate.Notifications.service
#%%{_libexecdir}/mate-notification-applet
%{_libexecdir}/mate-notification-daemon
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.MateNotificationAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.NotificationDaemon.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.MateNotificationApplet.mate-panel-applet
%{_datadir}/icons/hicolor/*/apps/mate-notification-properties.*
%{_mandir}/man1/mate-notification-properties.1.gz
%{_libdir}/mate-notification-daemon
%{_sysconfdir}/xdg/autostart/mate-notification-daemon.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 19 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-4
- use https://github.com/mate-desktop/mate-notification-daemon/commit/90b39ec

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 24 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-3
- fix building with libxml-2.12.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-3
- add upstream commit
- Add AssumedAppArmorLabel to dbus service file

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.2-1
- update to 1.24.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Mon Feb 03 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.1-1
- update to 1.23.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-1
- update to 1.20.1

* Sun Feb 11 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- drop GSettings Schema rpm scriplet
- switch to using autosetup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.1-1
- update to 1.19.1

* Sat Sep 02 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Sun Dec 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.1-1
- update to 1.16.1 release

* Sat Oct 15 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-2
- fix rhbz (#1384691)

* Wed Sep 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Wed Jun 29 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.15.1-1
- Update to 3.15.1

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Sat May 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-2
- fix window hint for Coco and Nodoka theme

* Tue Apr 05 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release
- switch to gtk3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.1-11
- update to 1.12.1 release
- remove upstreamed patches

* Tue Nov 24 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-12
- fix crash of notifications with images, rhbz (#1284651, #1281403)

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Tue Oct 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2.1
- update to 1.10.2 release
- remove upstreamed patches

* Fri Jul 31 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-0.5.git20150724.f9aedaf
- fix crash if clicking on close button in standard theme

* Fri Jul 24 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-0.4.git20150724.f9aedaf
- update to git snapshot from 2015-07-24
- fix rhbz (#1233293)

* Wed Jul 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release
- fix rhythmbox, rhbz (#1224782)

* Wed Jul 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-0.4.git20150719.4b8e9d5
- update to git snapshot from 2015-07-22
- fix rhythmbox, rhbz (#1224782)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0-1 release

* Mon Mar 02 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release
- remove upstreamed patch

* Thu Jan 08 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-2
- fixed-logic-in-a-couple-of-places
- rhbz (#1142441)

* Tue Nov 11 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Fri Oct 03 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-3
- try fix rhbz (#890728)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Sat Jan 18 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-1
- update to 1.7.1

* Thu Jan 16 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-1
- update to 1.7.0

* Sat Dec 28 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-0.2.git20131227.0280831
- make maintainers life easier and use better git snapshot usage, thanks to Björn Esser
- use latest git snapshot, fix rhbz (#1046716)
- add missing changelog entry from package owner
- use --with-gnome --all-name for find locale
- use modern 'make install' macro

* Sat Dec 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.0-0.1.git9f4203a1
- update to latest git snapshot for rawhide

* Fri Oct 25 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-1
- update to 1.6.1 release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-2
- add provide desktop-notification-daemon , needed for using
- libnotify, otherwise we run in yum probs with other DE's
- remove require libnotify, already called by rpm through BR
- remove BR gsettings-desktop-schemas-devel
- remove gsettings convert file


* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Mon Mar 11 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.2-1
- Update to latest upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1 release
- Update configure flags
- Update icon scriptlets
- Switch back to old BR style
- Sort BR's in alphabetical order
- Remove explicit variable for libtool in make

* Tue Oct 30 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- update to 1.5.0 release
- add schema scriptlets and remove mateconf scriptlets
- add requires gsettings-desktop-schemas
- add build requires gsettings-desktop-schemas-devel
- change build requires style
- fix ldconfig scriptlet

* Wed Sep 26 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-9
- Fix mate-conf scriptlets (again)

* Wed Sep 26 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-8
- Fix mate-conf scriptlets and bump release version

* Sat Sep 15 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-7
- Fix post and postun scriptlets

* Sat Sep 15 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-6
- Add desktop-file-validate and remove only showin for < f18 since desktop-file-utils was updated to the latest version. 

* Sat Sep 15 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-5
- Remove unneeded pre scriptlet and move post postun scriptlets before install scriptlet

* Mon Aug 27 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-4
- fix schema scriptlets
- drop uneeded update-desktop-database scriptlets
- License: GPLv2+
- %%doc AUTHORS COPYING README

* Sun Aug 26 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-3
- Switch from gconf scriptlets to mate conf scriptlets

* Wed Aug 08 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-2
- Remove po_package and add provides field.

* Thu Jul 12 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-1
-Initial build
