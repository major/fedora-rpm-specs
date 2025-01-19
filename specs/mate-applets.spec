# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit c3b48ea39ab358b45048e300deafaa3f569748ad}
%{!?rel_build:%global commit_date 20140211}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-applets
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        4%{?dist}
%else
Release:        0.11%{?git_rel}%{?dist}
%endif
Summary:        MATE Desktop panel applets
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-applets.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: gucharmap-devel
BuildRequires: libgtop2-devel
BuildRequires: libmateweather-devel
BuildRequires: libnl3-devel
BuildRequires: libnotify-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libwnck3-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-settings-daemon-devel
BuildRequires: mate-notification-daemon
BuildRequires: mate-panel-devel
BuildRequires: polkit-devel
BuildRequires: startup-notification-devel
Buildrequires: upower-devel
Buildrequires: gtksourceview4-devel
%ifnarch s390 s390x sparc64
BuildRequires: kernel-tools-libs-devel
%endif

# not kernel-tools for this arch any more
ExcludeArch: i386 i686

Provides:   mate-netspeed%{?_isa} = %{version}-%{release}
Provides:   mate-netspeed = %{version}-%{release}
Obsoletes:  mate-netspeed < %{version}-%{release}

%description
MATE Desktop panel applets

%prep
%if 0%{?rel_build}
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

%build
%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%configure   \
    --disable-schemas-compile                \
    --disable-static                         \
    --with-x                                 \
    --enable-polkit                          \
    --enable-ipv6                            \
    --enable-stickynotes                     \
    --libexecdir=%{_libexecdir}/mate-applets \
    --with-dbus-sys=%{_datadir}/dbus-1/system.d \
    --enable-in-process

# https://bugzilla.redhat.com/show_bug.cgi?id=2241946
# fix linking gtksourceview
sed -i /LDFLAGS/s/--as-needed/--no-as-needed/g stickynotes/Makefile

make %{?_smp_mflags} V=1

%install
%{make_install}

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-cpufreq-selector
%{_libdir}/mate-applets
#%%{_libexecdir}/mate-applets
%config(noreplace) %{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_datadir}/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%{_datadir}/mate-applets
%{_datadir}/mate-panel/applets
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.CommandAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.TimerAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.drivemount.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.cpufreq.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.command.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.timer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/devices/*.png
%{_datadir}/icons/hicolor/*/status/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/*
%{_datadir}/pixmaps/mate-cpufreq-applet


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Thu Jan 25 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-10
- rebuild to fix rhbz (2262518)

* Thu Jan 25 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-9
- fix building with gcc14

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 06 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-6
- fix linking gtksourceview, rhbz (#2241946)

* Wed Sep 13 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-5
- rebuild for soname bump in kernel-tools

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0 release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.24.1-2
- Migrate from wireless-tools to libnl3

* Tue Aug 11 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-3
- rebuild against latest kernel to fix cpu-freq-applet
- fix rhbz (#1827937)

* Thu Mar 26 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-2
- fix broken SVG icons
- use https://github.com/mate-desktop/mate-applets/pull/447

* Tue Feb 11 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Sun Feb 02 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.1-1
- update to 1.23.3
- fix f32 mass rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-1
- update 1.22.2 release
- revert https://github.com/mate-desktop/mate-applets/commit/bd0cf4
- to fix build for s390x arch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-3
- bump version

* Thu May 09 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-2
- multiload-applet, filter out non local disks and mounts
- fix https://github.com/mate-desktop/mate-applets/issues/395
- cpufreq, add support for kernel-5.1.0

* Fri Apr 26 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.3-2
- fix https://github.com/mate-desktop/mate-applets/issues/230
- fix rhbz (#1355867)
- use https://github.com/mate-desktop/mate-applets/commit/3b5b33a

* Mon Dec 17 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.3-1
- update to 1.20.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2

* Tue Mar 27 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-1
- update to 1.20.1

* Mon Feb 12 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.0-1
- uppdate to 1.20.0
- drop GSettings Schema rpm scriptlet
- drop IconCache rpm scriptlet
- switch to using autosetup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.4-1
- update to 1.19.4
- fix for https://github.com/mate-desktop/libmateweather/issues/51
- fixing clock-applet crashes, rhbz (#1529899), (#1529897)
- drop invest applet

* Tue Jan 16 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.2-3
- fixing clock-applet crashes, rhbz (#1529899), (#1529897)

* Thu Nov 09 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.2-2
- add some upstream patches
- https://github.com/mate-desktop/mate-applets/commit/99f9632
- https://github.com/mate-desktop/mate-applets/commit/d0abc32
- https://github.com/mate-desktop/mate-applets/commit/721ebf7

* Tue Sep 12 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.2-1
- update to 1.19.2 release

* Tue Sep 12 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.1-2
- use https://github.com/mate-desktop/mate-applets/commit/29c3ce44

* Sun Sep 10 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.1-1
- update to 1.19.1 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0 release

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 1.18.1-2
- Rebuilt for libgtop2 soname bump

* Fri Apr 07 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-1
- update 1.18.1
- use cpufreq: set frequency on all cores from upstream

* Tue Mar 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-2
- enable cpufreq-applet again

* Tue Dec 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update 1.17.0 release
- disable cpufreq-applet temporary for kernel-4.9

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Fri Sep 02 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.2-1
- update to 1.15.2 release

* Mon Aug 01 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-1
- update to 1.15.1 release
- drop BR mate-desktop

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release
- switch to gtk+3

* Tue Apr 05 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Fri Apr 01 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.1-1
- update to 1.13.1 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.1-11
- update to 1.12.1 release

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Thu Jul 16 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.3.1
- update to 1.10.3 release

* Tue Jul 14 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2.1
- update to 1.10.2 release

* Thu Jun 25 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Sun Apr 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release
- remove cpu-freq patch
- add --with-cpufreq-lib=cpupower flag

* Thu Jan 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 1.9.0-3
- Rebuilt for upower 0.99.1 soname bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release
- remove gucharmap BR for GTK2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-2
- rebuild for libgtop2 soname bump

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Tue Feb 11 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> 1.7.2-0.1.git20140211.c3b48ea
- update to git snapshot from 2014.02.11
- add improved snapshot usage
- add gtksourceview2-devel BR for stickynotes
- update configure flags
- sort file section

* Sun Feb 09 2014 Dan Mashal <dan.mashal@fedoraproject.org> 1.7.1-1
- Update to 1.7.1

* Mon Jan 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> 1.7.0-1
- update to 1.7.0 release
- update BR's
- add --with-gnome --all-name for find language
- use modern 'make install' macro
- clean up file section
- build without gucharmap support
- update configure flags

* Wed Jan 1 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-1
- update to 1.6.2 release
- remove upstreamed upower patches

* Sun Nov 10 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-8
- improve upower-1.0 adjustments

* Thu Nov 07 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-7
- add patch for build against upower-1.0
- clean up BRs

* Fri Nov 01 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-6
- disable upower BR > f20, until we know to handle upower-1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Dan Horák <dan[at]danny.cz> - 1.6.1-4
- kernel-tools-libs-devel isn't built on s390(x) and sparc64

* Sun Jun 02 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-3
- bump version

* Sun Jun 02 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-2
- activate cpufreq applet
- build against mate-character-map instead of gurchmap
- remove stickynotes-applet.convert gsettings convert file
- add runtime require hicolor-icon-theme
- use polkit-devel as BR
- add BR libICE-devel and libSM-devel
- sort files section

* Sat Apr 13 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.1-1
- Update to latest upstream release

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Tue Mar 12 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.2-2
- Add libnotify-devel and hard requires on libnotify. mate-notification-daemon was switched to libnotify.

* Mon Mar 11 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.2-1
- Update to latest upstream release

* Sun Feb 03 2013 - Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-5
- Fix conflicts with gnome by adding libexec configure flag

* Sun Feb 03 2013 - Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-4
- Fix dist tag
- Remove duplicate files
- Sort BRs in alphabetical order

* Sat Jan 26 2013 - Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-3
- bump

* Sat Jan 26 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-2
- Add missing BR

* Fri Jan 25 2013 - Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-1
- Initial build
