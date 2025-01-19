# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit ac33ed09bb41ba717df3722cc71e25c1aa5134c5}
%{!?rel_build:%global commit_date 20150709}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Summary:        Terminal emulator for MATE
Name:           mate-terminal
Version:        %{branch}.1
%if 0%{?rel_build}
Release:        4%{?dist}
%else
Release:        0.21%{?git_rel}%{?dist}
%endif
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-terminal.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

#Default to black bg white fg, unlimited scrollback, turn off use theme default
Patch1:        mate-terminal_better_defaults-1.26.0.patch

BuildRequires: dconf-devel
BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: vte291-devel

# needed to get a gsettings schema, rhbz #908105
Requires:      mate-desktop-libs
Requires:      gsettings-desktop-schemas

%description
Mate-terminal is a terminal emulator for MATE. It supports translucent
backgrounds, opening multiple terminals in a single window (tabs) and
clickable URLs.

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
%configure --disable-static                \
           --disable-schemas-compile       

make %{?_smp_mflags} V=1


%install
%{make_install}

desktop-file-install                                                    \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-terminal.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/mate-terminal
%{_bindir}/mate-terminal.wrapper
%{_datadir}/applications/mate-terminal.desktop
%{_datadir}/glib-2.0/schemas/org.mate.terminal.gschema.xml
%{_datadir}/metainfo/mate-terminal.appdata.xml
%{_mandir}/man1/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.1-1
- update to 1.28.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 10 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-4
- fix rhbz (#2160523)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-2
- use https://github.com/mate-desktop/mate-terminal/commit/2030aa2
- use https://github.com/mate-desktop/mate-terminal/pull/327
- use https://github.com/mate-desktop/mate-terminal/pull/322
- use https://github.com/mate-desktop/mate-terminal/commit/c317ee8
- use https://github.com/mate-desktop/mate-terminal/pull/332

* Tue Feb 11 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-3
- use https://github.com/mate-desktop/mate-terminal/pull/316
- fixing rhbz (#1781564)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-2
- Set TERM to xterm-256color
- use https://github.com/mate-desktop/mate-terminal/commit/4f89d21
- fix rhbz https://bugzilla.redhat.com/show_bug.cgi?id=1517870

* Wed Dec 26 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-1
- update to 1.20.1

* Fri May 18 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-3
- drop patch for gnome-shell as it causes issues in MATE session

* Fri Apr 06 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-2
- use https://github.com/mate-desktop/mate-terminal/pull/236
- fix transparency background in gnome-shell

* Sun Feb 11 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- drop GSettings Schema rpm scriplet
- switch to autosetup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.1-1
- update to  1.19.1
- use https://github.com/mate-desktop/mate-terminal/pull/215

* Wed Oct 11 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 06 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-1
- update to 1.18.1

* Tue Mar 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-3
- fix rhbz (#1398234), (#1417365), (#1399641)

* Fri Jan 27 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-2
- fix rhbz (#1411035)
 
* Sun Dec 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Sun Nov 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.1-2
- fix rhbz (#1392132)

* Thu Oct 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.1-1
- update to 1.16.1 release

* Wed Sep 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-2
- fix rhbz (#1377805)
- fix terminal window position with geometry option

* Wed Sep 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Wed Sep 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-2
- fix rhbz (#1357693)

* Fri Jul 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-1
- update to 1.15.1 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Thu May 26 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-2
- switch to gtk3
- https://github.com/mate-desktop/mate-terminal/pull/118

* Thu Apr 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0

* Fri Mar 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.2-1
- update to 1.13.2 release

* Mon Feb 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.1-1
- update to 1.13.1 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.1-1
- update to 1.12.1 release

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release
- remove upstreamed patch

* Thu Oct 01 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-2
- fix usage of --tab at command line

* Sat Jul 11 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release
- remove upstreamed patches

* Fri Jul 03 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-3
- use old help from 1.8

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Wed May 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.91-1
- update to 1.9.91 release

* Mon Apr 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-11
- update to 1.9.90 release

* Thu Jan 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

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

* Sun Feb 09 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Sat Jan 18 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-1
- update to 1.7.1 release
- remove obsolete configure flags
- clean up BR's
- use modern 'make install' macro
- add --with-gnome --all-name for find language
- clean up file section

* Fri Dec 06 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Thu Aug 08 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-11
- switch to runtime require mate-desktop-libs, fix rhbz #908105

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1.9
- another fix for better default patch

* Sat Jun 29 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1.8
- add runtime require gsettings-desktop-schemas to have proxy support
- from gnome gsettings schema

* Fri Jun 28 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1.7
- improve better_default patch
- remove BR gsettings-desktop-schemas-devel
- remove update-desktop-database scriptlet

* Mon Jun 17 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.1-6
- Update patch for bold colors

* Fri May 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.1-5
- Update patch again

* Fri May 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.1-4
- Update patch (again) to really fix annoying default settings

* Fri May 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.1-3
- Update patch to really fix annoying default settings
- New defaults: unlimited scrollback black bg

* Fri May 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.1-2
- Add patch to fix annoying default settings

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.1-1
- Bugfix release. See Cangelog.

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to stable 1.6.0 release

* Tue Mar 26 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-1
- Update to latest upstream release

* Mon Feb 18 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.0-3
- Add hard requires for mate-desktop to fix RHBZ #908105

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.0-1
- Update to latest upstream release
- Special thanks to Shawn Sterling for his help

* Wed Oct 24 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-4
- Add requires libmate

* Mon Oct 15 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-3
- add build requires rarian-compat

* Mon Oct 15 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-2
- remove surplus build requires

* Sun Oct 14 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- initial build
