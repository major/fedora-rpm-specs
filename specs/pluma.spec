# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit c1ca209172a8b3a0751ac0a1e2dbec33c1894290}
%{!?rel_build:%global commit_date 20140712}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Summary:  Text editor for the MATE desktop
Name:     pluma
Version:  %{branch}.0
%if 0%{?rel_build}
Release:  4%{?dist}
%else
Release:  0.19%{?git_rel}%{?dist}
%endif
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:  GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:      http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R pluma.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: desktop-file-utils
BuildRequires: enchant-devel
BuildRequires: libpeas1-devel
BuildRequires: gtk3-devel
BuildRequires: gtksourceview4-devel
BuildRequires: iso-codes-devel
BuildRequires: libSM-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: python3-gobject-base
BuildRequires: python3-devel
BuildRequires: (python3-setuptools if python3-devel >= 3.12)

Requires: %{name}-data = %{version}-%{release}
# needed to get a gsettings schema, #959607
Requires: mate-desktop-libs
# needed to get a gsettings schema, #959607
Requires: caja-schemas
# the run-command plugin uses zenity
Requires: zenity
Requires: libpeas-loader-python3

%description
pluma is a small, but powerful text editor designed specifically for
the MATE desktop. It has most standard text editor functions and fully
supports international text in Unicode. Advanced features include syntax
highlighting and automatic indentation of source code, printing and editing
of multiple documents in one window.

pluma is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels.

%package data
Summary:   Data files for pluma
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}

%description data
This package contains shared data needed for pluma.


%package devel
Summary:   Support for developing plugins for the pluma text editor
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  gtksourceview4-devel

%description devel
Development files for pluma


%prep
%if 0%{?rel_build}
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

%if 0%{?rel_build}
# for releases
#NOCONFIGURE=1 ./autogen.sh
%else
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif

# Fix debug permissions with messy hack 
find ./*/* -type f -exec chmod 644 {} \;
find ./*/*/* -type f -exec chmod 644 {} \;

%build
%configure \
        --disable-static          \
        --enable-gtk-doc-html     \
        --enable-gvfs-metadata    \
        --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/*.desktop

# clean up all the static libs for plugins
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files
%{_bindir}/pluma
%{_libdir}/pluma/
%{_libexecdir}/pluma/
%{_libdir}/girepository-1.0/Pluma-1.0.typelib
%{_datadir}/applications/pluma.desktop
%{_datadir}/metainfo/pluma.appdata.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.pythonconsole.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.spell.gschema.xml

%files data -f %{name}.lang
%doc README.md COPYING AUTHORS
%{_datadir}/pluma/
%{_mandir}/man1/pluma.1.*

%files devel
%{_includedir}/pluma/
%{_libdir}/pkgconfig/pluma.pc
%{_datadir}/gtk-doc/html/pluma/
%{_datadir}/gir-1.0/Pluma-1.0.gir


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Thu Jan 25 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-4
- fix building with gcc14

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 08 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Mon Feb 27 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-7
- Fix out-of-bounds write
- https://github.com/mate-desktop/pluma/commit/8ca37be

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-5
- update spec file to build with python-3.12 in f39

* Sun Jul 31 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-4
- add a few upstream commits from 1.26 branch

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0 release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 27 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.2-1
- update to 1.24.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Mon Feb 03 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.3-1
- update to 1.23.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-1
- update to 1.22.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-2
- enable python moduls again
- use python3

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.4-1
- update to 1.20.4 release

* Thu Nov 22 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.3-1
- update to 1.20.3

* Fri Jul 20 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-3
- cleanup build requires and requires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2 release
- disable python plugins for f29

* Tue Mar 27 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-1
- update to 1.20.1
- drop IconCache rpm scriptlet

* Sun Feb 11 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- drop desktop-database rpm scriptlet
- drop GSettings Schema rpm scriptlet
- switch to autosetup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.3-1
- update to 1.19.3

* Tue Oct 03 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.2-1
- update to 1.19.2

* Wed Aug 09 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.1-4
- remove virtual provides

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.1-1
- update to 1.19.1

* Sat May 06 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.2-1
- update to 1.18.2

* Wed Apr 26 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.1-2
- use gtk+-3 bookmark location for file-browser-plugin

* Tue Apr 04 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.1-1
- update to 1.18.1

* Fri Mar 31 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-3
- fix running under wayland
- https://github.com/mate-desktop/pluma/commit/06b9ba3

* Tue Mar 28 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-2
- use https://github.com/mate-desktop/pluma/commit/910aec0

* Tue Mar 14 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Mar 10 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.4-1
- update to 1.17.4 release

* Wed Feb 08 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.3-2
- use BR libpeas-loader-python only for fedora

* Mon Jan 09 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.3-1
- update to 1.17.3
- fix rhbz (#1411052)
- add BR libpeas-loader-python

* Sun Dec 25 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.2-1
- update to 1.17.2 release

* Thu Nov 17 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Wed Sep 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Fri Sep 02 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.2-1
- update to 1.15.2 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-1
- update to 1.15.1 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Tue Apr 05 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Mon Feb 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.1-1
- update to 1.13.1 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.1-1
- update to 1.12.1 release

* Sat Nov 21 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-2
- build with gtk3
- disable python plugins for the moment

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Tue Jul 14 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2.1
- update to 1.10.2 release

* Thu Jul 02 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-2
- version bump to fix f21 build

* Thu Jun 18 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release
- remove upstreamed patches

* Thu May 07 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-2
- fix translations in gsettings
- fix size of statusbar (gtk3)

* Thu May 07 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release
- add patch to fix f23 build

* Mon Apr 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release

* Thu Jan 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release
- enable gtk-docs for release build
- disable autogen for release build

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-0.1.git20131511.c1ca209
- use git snapshot from 2014.07.12
- disable gtk-docs for snapshot build

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.1.1
- update to 1.8.1 release

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90
- remove obsolete mate-text-editor binary from spec file

* Thu Feb 13 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.2-1
- update to 1.7.2 release
- fix rpmlint warning 'can't find source0'
- fix license information
- use a joker for the man file attribute
- move data in a noarch subpackage
- improve obsoletes
- update rpm scriplets

* Wed Dec 25 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-1
- update to 1.7.1 release
- add gtk-doc dir to -devel subpackage for release builds

* Wed Dec 25 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-0.1.git20131511.7ceb8fe
- rename to pluma
- make maintainers life easier and use better git snapshot usage, thanks to Björn Esser
- simplify remove of static libaries
- use modern 'make install' macro
- add --with-gnome flag to find_language, needed for yelp
- sort file section

* Fri Dec 06 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Thu Aug 08 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-5
- add runtime require mate-file-manager-schemas to fix #959607

* Thu Aug 08 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-4
- switch to runtime require mate-desktop-libs
- remove needless --with-gnome flag in find_language 

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-2
- add runtime require mate-desktop, fix rhbz #959607
- remove pluma.convert files
- cleanup BR's
- fix desktop file install command, no needed to add X-MATE
- use runtime require mate-dialogs instead of zenity
- remove BR mate-conf-devel
- add --disable-static configure flag
- general usage of %%{buildroot}
- no need of mimeinfo rpm scriptlets
- fix desktop-database rpm scriptlets
- update BR's 
- add isa tag to -devel subpackage

* Sat Apr 13 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Sun Feb 10 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-1
- Update to latest upstream release

* Mon Oct 15 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-2
- Fix build requires

* Sun Oct 14 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Initial build


