# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit f4611c3411c44e792f729a0780c31b0aa55fe004}
%{!?rel_build:%global commit_date 20131215}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:          engrampa
Version:       %{branch}.2
%if 0%{?rel_build}
Release:       2%{?dist}
%else
Release:       0.23%{?git_rel}%{?dist}
%endif
Summary:       MATE Desktop file archiver
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R engrampa.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: make
BuildRequires: mate-common
BuildRequires: desktop-file-utils
BuildRequires: file-devel
BuildRequires: gtk3-devel
BuildRequires: json-glib-devel
BuildRequires: caja-devel
BuildRequires: libSM-devel
BuildRequires: PackageKit-glib-devel

%description
Mate File Archiver is an application for creating and viewing archives files,
such as zip, xv, bzip2, cab, rar and other compress formats.


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
%configure                 \
   --disable-schemas-compile \
   --disable-static        \
   --enable-caja-actions   \
   --enable-magic

make %{?_smp_mflags} V=1


%install
%{make_install}

desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/engrampa.desktop

find %{buildroot} -name "*.la" -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc README COPYING NEWS AUTHORS
%{_mandir}/man1/*
%{_bindir}/engrampa
%{_libexecdir}/engrampa
%{_libexecdir}/engrampa-server
%{_libdir}/caja/extensions-2.0/libcaja-engrampa.so
%{_datadir}/engrampa
%{_datadir}/metainfo/engrampa.appdata.xml
%{_datadir}/applications/engrampa.desktop
%{_datadir}/caja/extensions/libcaja-engrampa.caja-extension
%{_datadir}/dbus-1/services/org.mate.Engrampa.service
%{_datadir}/icons/hicolor/*/actions/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.mate.engrampa.gschema.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 29 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.2-1
- update to 1.28.2

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.1-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.1-1
- update to 1.28.1

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Tue Feb 06 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.2-1
- update to 1.26.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 04 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Fri Apr 14 2023 Florian Weimer <fweimer@redhat.com> - 1.26.0-6
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-3
- add a few upstream patches from 1.26 branch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0 release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.2-1
- update to 1.24.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Sun Feb 02 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.3-1
- update to 1.23.3
- fix f32 mass rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 04 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.3-1
- update to 1.22.3

* Wed Sep 18 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-1
- update to 1.22.2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.1-1
- update to 1.20.1

* Sun Feb 11 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- drop desktop-database rpm scriptlet
- drop GSettings Schema rpm scriptlet
- drop IconCache Schema rpm scriptlet
- switch to autosetup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.2-1
- update to 1.19.2

* Wed Oct 11 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.1-1
- update to 1.19.1 release

* Wed Aug 09 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-4
- remove virtual provides

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0 release

* Wed Apr 05 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-1
- update to 1.18.1

* Tue Mar 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Fri Jul 29 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-1
- update to 1.15.1 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Thu May 26 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.1-2
- switch to gtk3 for f24
- https://github.com/mate-desktop/engrampa/commit/6a3dba

* Sat May 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.1-1
- update to 1.14.1 release

* Tue Apr 05 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Mon Feb 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.1-1
- update to 1.13.1 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-2
- fix for p7zip 15.09+

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release
- remove upstreamed patch
- add forgotten provides to obsolete mate-file-archiver

* Sun Oct 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-2
- fix https://github.com/mate-desktop/engrampa/issues/78
- Cannot extract mulpiple files concurently to a seprate directory

* Thu Oct 01 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-1
- update to 1.10.2 release
- fix # rhbz (#1264593)
- don't crash when opening archives on network drive (ftp, smb, ...)

* Mon Jul 13 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release
- remove upstreamed patches

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-2
- fix large statusbar in gtk3 version and create button

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Sun Apr 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release

* Thu Jan 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.2-1
- update to 1.9.2 release
- enable libmagic

* Thu Nov 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Sun Aug 17 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-3
- add json-glib-devel as BR
- fix https://github.com/mate-desktop/engrampa/issues/59 

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Sun Feb 09 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Thu Jan 16 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-1
- update to 1.7.0 release

* Wed Dec 18 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-0.2.git20131215.f4611c3
- make Maintainers life easier and use better git snapshot usage, Thanks to Björn Esser
- use modern 'make install' macro

* Sun Dec 15 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-0.1.gitf4611c3
- rename mate-file-archiver to engrampa
- use latest git snapshot from 1.7 branch
- add support for *.ar, *.cab, *.wim, *.swm files
- several zip improvements 

* Sun Oct 13 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-0.1.git95ebd69
- update to latest snapshot
- remove mate-file-archiver_missing_gsettings_schema.patch, already in snapshot
- add support for rar-0.5
- add support for unarchiver

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-2
- https://github.com/mate-desktop/mate-file-archiver/issues/19,
- fix add folder to existing archive
- remove BR gsettings-desktop-schemas
- remove BR glib2-devel
- remove needless gsettings convert file

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Thu Feb 21 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-6
- Obsoletes: mate-file-manager-archiver (#908137)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-4
- Bump release

* Tue Jan 22 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-3
- Update BRs
- Convert back to old BR style
- Get rid of separate package for shared library
- Add provides field
- Rebuild against latest version of mate-desktop
- Update icon scriptlets
- Add obsoletes tag

* Thu Nov 22 2012 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-2
- Rebuild for f17

* Mon Nov 19 2012 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-1
- Update to latest release
- Remove patches that were applied upstream

* Thu Nov 15 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-3
- Fix another schema error

* Thu Nov 15 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-2
- add patch to fix (rhbz 876354)

* Thu Oct 25 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- Initial build

