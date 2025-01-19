# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit 3a68372f379644cc50d4cd9bb6f012653eddb683}
%{!?rel_build:%global commit_date 20150319}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:          mate-power-manager
Version:       %{branch}.1
%if 0%{?rel_build}
Release:       4%{?dist}
%else
Release:       0.21%{?git_rel}%{?dist}
%endif
Summary:       MATE power management service
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://pub.mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-power-manager.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: cairo-devel
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: libcanberra-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: libnotify-devel
BuildRequires: libsecret-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-panel-devel
BuildRequires: mesa-libGL-devel
BuildRequires: popt-devel
BuildRequires: upower-devel
BuildRequires: polkit-devel

%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.


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
%configure \
     --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                               \
     --delete-original                             \
     --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop

%find_lang %{name} --with-gnome --all-name


%files  -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/mate-power-*.*
%{_bindir}/mate-power-manager
%{_bindir}/mate-power-preferences
%{_bindir}/mate-power-statistics
%{_sbindir}/mate-power-backlight-helper
%{_datadir}/applications/mate-*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mate-power-manager/
%{_datadir}/icons/hicolor/*/apps/mate-*.*
%{_datadir}/polkit-1/actions/org.mate.power.policy
%{_datadir}/mate-panel/applets/org.mate.BrightnessApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.InhibitApplet.mate-panel-applet
%{_datadir}/glib-2.0/schemas/org.mate.power-manager.gschema.xml
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 25 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.1-1
- update to 1.28.1

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 06 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-3
- add upstream commits from 1.26 branch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.3-1
- update to 1.24.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 15 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.2-1
- update to 1.24.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-2
- drop BR pangox-compat-devel

* Sun Mar 15 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1 release

* Mon Feb 24 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-2
- fix desktop file in autostart

* Mon Feb 10 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Mon Feb 03 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.2-1
- update to 1.23.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-1
- update to 1.22.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.3-1
- update to 1.20.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2

* Tue May 01 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-3
- improve scaling of inhibit Applet

* Tue May 01 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-2
- Fix excessive CPU use of inhibit Applet
- fix https://github.com/mate-desktop/mate-power-manager/issues/248
- use https://github.com/mate-desktop/mate-power-manager/commit/8e29023

* Tue Mar 27 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-1
- update to 1.20.1
- drop IconCache rpm scriplet

* Sun Feb 11 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- drop GSettings Schema rpm scriplet
- switch to using autosetup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.1-1
- update to 1.19.1

* Wed Oct 11 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0

* Thu Aug 17 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-5
- bump version to match rawhide (f28) after f27 branching

* Wed Aug 16 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-4
- should fix partial rhbz (#1476622)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.1-1
- update to 1.17.1 release

* Tue Dec 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update 1.17.0 release

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Mon Aug 01 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-1
- update to 1.15.1 release
- drop BR mate-control-center

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release
- switch to gtk+3

* Thu Apr 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> 1.12.1-1
- update to 1.12.1 release
- remove upstreamed patches

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release
- fix handle backlight in different cases
- add an option to disable power button

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Wed Sep 02 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2.1
- update to 1.10.2 release

* Tue Jul 14 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1.1
- update to 1.10.1 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Sat Apr 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release

* Thu Mar 19 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-0.1.git20150319.3a68372
- update to latest git snapshot from 2015-03-19
- remove upstreamed patch

* Thu Jan 08 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-2
- fix mate-power-manager brightness pop-up is a blank square
- rhbz (#1142224)

* Sun Oct 26 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0
- Add support for UPower 0.99
- remove upstreamed patch

* Fri Oct 03 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.1-1
- update to 1.8.1 release
- remove upstreamed upower-0.99 patches

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 1.8.0-5
- Rebuilt for upower 0.99.1 soname bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-2
- use new upower patches from upstream

* Wed Mar 05 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-1
- update to 1.8.0 release
- remove uptreamed mouse-click-on-brightness-applet patch

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90
- remove --disable-scrollkeeper configure flag

* Mon Jan 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> 1.7.0-1
- update to 1.7.0 release
- use modern 'make install' macro
- update BR's
- add --with-gnome --all-name for find language
- clean up file section
- remove upstreamed switch-to-gnome-keyring patch for rawhide
- remove upstreamed set-DISABLE_DEPRECATED-to-an-empty-string.patch
- add better comment

* Fri Dec 20 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.3-1
- updated to 1.6.3 release
- fix build, add  mate-power-manager_set-DISABLE_DEPRECATED-to-an-empty-string.patch
- remove BR mate-keyring-devel
- fix bogus date in %%changelog

* Sun Nov 10 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.3-0.4.gitbc54d96
- support for upower-1.0

* Sat Oct 19 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.3-0.3.gitbc54d96
- switch to gnome-keyring for > f19

* Mon Oct 14 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.3-0.2.gitbc54d96
- fix mouse click on brightness applet, rhbz (#1018915)

* Sun Oct 13 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.3-0.1.gitbc54d96
- update to latest snapshot
- removed upstreamed patches, already in snapshot
- add DBUS interface to kbdbacklight control patch, rhbz (#964678)

* Sun Sep 29 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-4
- fix suspend on lid close, fix rhbz (#1012718)

* Fri Aug 09 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-3
- fix display-to-sleep-when-inactive, rhbz #994232

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-1
- update to 1.6.2 release
- fix systemd-login1 support, (#972881)
- remove runtime require ConsoleKit-x11
- remove gsettings convert file
- remove runtime require ConsoleKit-x11
- remove BR systemd-devel
- remove systemd configure flags
- remove NOCONFIGURE=1 ./autogen.sh

* Thu Jun 20 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.1-3
- Requires: ConsoleKit-x11 (#972881)

* Tue Jun 18 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.6.1-2
- Add patch to fix suspend on lid close

* Fri May 10 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.6.1-1
- Update to latest upstream release
- Add systemd sleep configure flag

* Sun Apr 21 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-2
- Add upstream patch to fix suspend on lid close

* Mon Apr 08 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 stable release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.5.1-5
- Rework specfile to make it easier to read and pretty.
- Drop duplicate BRs

* Thu Nov 29 2012 Nelson Marques <nmo.marques@gmail.com> - 1.5.1-4
- Add %%name-1.5.1-add_systemd_checks.patch - fixes crasher,
  systemd inhibit requires systemd >= 195, merged upstream

* Mon Nov 26 2012 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-3
- Add hard requires to mate-panel-libs to fix dependency issues

* Fri Nov 23 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.1-2
- add br systemd-devel as we need systemd support

* Thu Nov 22 2012 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1 release
- Drop patches that already exist in 1.5.1 release

* Wed Nov 14 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-2
- add upstream patch to add keyboard backlight support

* Thu Nov 08 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- update to 1.5.0 release

* Mon Oct 29 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.1-0.1.git543b06f
- update to latest git snapshot
- patch to build against latest mate-panel

* Fri Oct 19 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-2
- add V=1 to make command
- add mate-conf requires and remove mate-icon-theme

* Fri Oct 19 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Initial build
