# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit d5b35083e4de1d7457ebd937172bb0054e1fa089}
%{!?rel_build:%global commit_date 20140125}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-screensaver
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        4%{?dist}
%else
Release:        0.23%{?git_rel}%{?dist}
%endif
Summary:        MATE Screensaver
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://pub.mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-screensaver.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

Requires:      redhat-menus
Requires:      system-logos
Requires:      gnome-keyring-pam

BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXtst-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libmatekbd-devel
BuildRequires: libnotify-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-menus-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pam-devel
BuildRequires: systemd-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: xmlto

%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.


%package devel
Summary: Development files for mate-screensaver
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-screensaver


%prep
%if 0%{?rel_build}
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure                          \
            --with-x                \
            --disable-schemas-compile \
            --enable-docbook-docs   \
            --with-mit-ext          \
            --with-xf86gamma-ext    \
            --with-libgl            \
            --with-shadow           \
            --enable-locking        \
            --with-systemd          \
            --enable-pam            \
            --without-console-kit

make %{?_smp_mflags} V=1


%install
%{make_install}

desktop-file-install --delete-original             \
  --dir %{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mate-screensaver-preferences.desktop

desktop-file-install                                          \
   --delete-original                                          \
   --dir %{buildroot}%{_datadir}/applications/screensavers    \
%{buildroot}%{_datadir}/applications/screensavers/*.desktop

# fix versioned doc dir
mkdir -p %{buildroot}%{_docdir}/mate-screensaver
mv %{buildroot}%{_docdir}/mate-screensaver-%{version}/mate-screensaver.html %{buildroot}%{_docdir}/mate-screensaver/mate-screensaver.html

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/mate-screensaver*
%{_sysconfdir}/pam.d/mate-screensaver
%{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_sysconfdir}/xdg/autostart/mate-screensaver.desktop
%{_libexecdir}/mate-screensaver-*
%{_libexecdir}/mate-screensaver/
%{_datadir}/applications/mate-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/*.desktop
%{_datadir}/mate-screensaver/
%{_datadir}/backgrounds/cosmos/
%{_datadir}/pixmaps/mate-logo-white.svg
%{_datadir}/pixmaps/gnome-logo-white.svg
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%{_datadir}/mate-background-properties/cosmos.xml
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_docdir}/mate-screensaver/mate-screensaver.html
%{_mandir}/man1/*

%files devel
%{_libdir}/pkgconfig/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 13 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.2-1
- update to 1.26.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 2 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to  1.26.1
- add a few upstream commits from 1.26 branch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-2
- use https://github.com/mate-desktop/mate-screensaver/commit/ec813df
- use https://github.com/mate-desktop/mate-screensaver/pull/262
- fix rhbz (#1997852)

* Thu Aug 05 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.2-1
- update to 1.24.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-2
- update UI to add a custom background-image for the lock-screen

* Mon Feb 10 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Mon Feb 03 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.1-1
- update to 1.23.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-1
- update to 1.22.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Adam Jackson <ajax@redhat.com> - 1.22.1-2
- Drop BuildRequires: libXxf86misc-devel, X servers haven't implemented that
  extension in 10+ years.

* Thu Apr 25 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.3-1
- update to 1.20.3

* Sun Sep 09 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.2-2
- update to 1.20.2

* Sat Aug 25 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.1-3
- fix rhbz (#1566571, #1397900, #1474046)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.1-1
- update to 1.20.1 release

* Sun Feb 11 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- drop GSettings Schema rpm scriplet
- switch to using autosetup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.19.1-2
- Rebuilt for switch to libxcrypt

* Mon Jan 01 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.1-1
- update to 1.19.1

* Sun Sep 10 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 16 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.1-1
- update to 1.18.1 release

* Tue Mar 14 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.1-1
- update to 1.17.1 release

* Sat Dec 03 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Wed Sep 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release
- switch to gtk+3

* Sat May 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.1-1
- update to 1.14.1 release

* Wed Apr 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Wed Oct 21 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.1-1
- update to 1.11.0 release

* Fri Oct 16 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-3
- revert 'Lock the screen on systemd sleep under systemd'

* Thu Sep 24 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-2
- improve systemd-login support

* Mon Jul 13 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-1
- update to 1.10.2 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1.1
- update to 1.10.1 release
- removed upstreamed patches

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0-1 release

* Sat Apr 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release

* Wed Apr 01 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.2-3
- fix user switching if more than 2 desktop managers are installed
- remove conditions for f19

* Fri Feb 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.2-2
- use gdm as last condition for user switching

* Tue Jan 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.2-1
- update to 1.9.2 release

* Thu Nov 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0.2
- fix 'has_separator'_deprecation

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Tue Feb 11 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-1
- update to 1.7.1 release

* Sun Jan 26 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-0.1.git20140125.d5b3508
- update to git snapshot from 2014.01.25
- fix rhbz (#1057402) and (#1056591)
- make Maintainers life easier and use better git snapshot usage

* Tue Jan 14 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-1
- update to 1.7.0 release
- add --with-gnome --all-name for find language
- removed upstreamed systemd-login patch
- removed --with-console-kit configure flag
- use modern 'make install' macro
- add BR xmlto
- reworked configure flags, use --with-gtk=2.0, --disable-schemas-compile
- --enable-docbook-docs
- fixed versioned doc dir
- use one style for ownning directories

* Fri Dec 06 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.7.0-1.1.git0460034
- Update to 1.7.0

* Sat Oct 19 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-4
- switch to gnome-keyring for > f19

* Sat Oct 12 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-3
- improve systemd-login support

* Fri Aug 02 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-2
- bump version to 1.6.1-2

* Fri Aug 02 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-1
- Update to 1.6.1
- Drop patches
- move doc dir for > f19

* Wed Jul 17 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-2
- add upstream patch to fix idle activation time
- remove unrecognized configure options --with-libgl
- clean up runtime requires
- add pam and systemd configure flags
- remove gsettings convert file

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Tue Mar 26 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.2-1
- Update to latest upstream release
- Redo configure flags
- Update configure flags
- Own dirs we are supposed to own

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Nelson Marques <nmo.marques@gmail.com> - 1.5.1-3
- Add missing dependencies for proper build and conditionals for
  using systemd or CK dependending on version.
- Rework %%configure

* Wed Dec 05 2012 Nelson Marques <nmo.marques@gmail.com> - 1.5.1-2
* add mate-screensaver-1.5.1-only_allow_one_instance.patch: fix double
  password prompt when returning from hibernate/suspend. Only allow one
  instance per user.

* Fri Nov 23 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.1-1
- update to 1.5.1 release
- drop upstream commits patch

* Mon Nov 12 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-3
- clean up commits patch

* Mon Nov 12 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-2
- add upstream commits patch
- add buildrequires systemd-devel

* Thu Nov 08 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- update to 1.5.0 release

* Tue Oct 23 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-2
- add V=1 to make
- use autogen instead of autoreconf

* Fri Oct 19 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Initial build

