# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit d3538696e2b4e4372e9f526a0a4e2e4be08fc832}
%{!?rel_build:%global commit_date 20150629}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-utils
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        4%{?dist}
%else
Release:        0.22%{?git_rel}%{?dist}
%endif
Summary:        MATE utility programs
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-utils.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: desktop-file-utils
BuildRequires: e2fsprogs-devel
BuildRequires: gtk-layer-shell-devel
BuildRequires: hardlink
BuildRequires: libcanberra-devel
BuildRequires: libgtop2-devel
BuildRequires: libudisks2-devel
BuildRequires: libX11-devel
BuildRequires: libXmu-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-panel-devel
BuildRequires: mesa-libGL-devel
BuildRequires: popt-devel
BuildRequires: usermode
BuildRequires: yelp-tools

%if 0%{?fedora} && 0%{?fedora} >= 29
BuildRequires: gcc-c++
%endif

Requires: mate-dictionary = %{version}-%{release}
Requires: mate-screenshot = %{version}-%{release}
Requires: mate-search-tool = %{version}-%{release}
Requires: mate-system-log = %{version}-%{release}
Requires: mate-disk-usage-analyzer = %{version}-%{release}

%description
The mate-utils package contains a set of small "desk accessory" utility
applications for MATE, such as a dictionary, a disk usage analyzer,
a screen-shot tool and others.

%package common
Summary: Common files for %{name}
BuildArch: noarch
%description common
%{summary}.

%package devel
Summary: Development files for mate-utils
Requires:  mate-dictionary%{?_isa} = %{version}-%{release}
%description devel
The mate-utils-devel package contains header files and other resources
needed to develop programs using the libraries contained in mate-utils.

%package -n mate-system-log
Summary: A log file viewer for the MATE desktop
Requires: %{name}-common = %{version}-%{release}
Requires: usermode
# rhbz (#1016935)
Requires: mate-desktop-libs
%description -n mate-system-log
An application that lets you view various system log files.

%package -n mate-screenshot
Summary: A utility to take a screen-shot of the desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-screenshot
An application that let you take a screen-shot of your desktop.

%package -n mate-dictionary
Summary: A dictionary for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-dictionary
The mate-dictionary package contains a dictionary application for MATE Desktop.

%package -n mate-search-tool
Summary: A file searching tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
Requires: mate-desktop-libs
%description -n mate-search-tool
An application to search for files on your computer.

%package -n mate-disk-image-mounter
Summary: A disk image mounter tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-disk-image-mounter
An application to mount disk images.

%package -n mate-disk-usage-analyzer
Summary: A disk usage analyzing tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-disk-usage-analyzer
An application to help analyze disk usage.


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

# disable pt language for help in search tool
sed -i s/"IGNORE_HELP_LINGUAS ="/"IGNORE_HELP_LINGUAS = pt"/g gsearchtool/help/Makefile.am
# pt translation fix
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
    --disable-static            \
    --disable-schemas-compile   \
    --enable-gdict-applet       \
    --enable-in-process         \
    --enable-wayland            \
    --enable-gtk-doc-html       \
    --enable-ipv6=yes           \
    --enable-maintainer-flags=no  \
    --with-x

make %{?_smp_mflags} V=1

%install
%{make_install}

# make mate-system-log use consolehelper until it starts using polkit
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cat <<EOF >%{buildroot}%{_sysconfdir}/pam.d/mate-system-log
#%%PAM-1.0
auth      include      config-util
account      include      config-util
session      include      config-util
EOF

mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
cat <<EOF >%{buildroot}%{_sysconfdir}/security/console.apps/mate-system-log
USER=root
PROGRAM=/usr/sbin/mate-system-log
SESSION=true
FALLBACK=true
EOF

mkdir -p  %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/mate-system-log %{buildroot}%{_sbindir}
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/mate-system-log

rm -fv %{buildroot}%{_libdir}/*.la
rm -fv %{buildroot}%{_datadir}/MateConf/gsettings/*.convert

# weird new files
rm -rf %{buildroot}%{_datadir}/icons/shot.png

desktop-file-install                          \
  --delete-original                           \
  --dir %{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome --all-name
%find_lang mate-disk-usage-analyzer --with-gnome --all-name
%find_lang mate-dictionary --with-gnome --all-name
%find_lang mate-search-tool --with-gnome --all-name
%find_lang mate-system-log --with-gnome --all-name


%files
# empty

%files common -f %{name}.lang
%doc COPYING COPYING.libs
%doc NEWS README.md

%files devel
%{_libdir}/libmatedict.so
%{_libdir}/pkgconfig/mate-dict.pc
%{_includedir}/mate-dict/
%{_datadir}/gtk-doc/html/mate-dict/

%files -n mate-system-log -f mate-system-log.lang
%{_bindir}/mate-system-log
%{_sbindir}/mate-system-log
%{_sysconfdir}/security/console.apps/mate-system-log
%{_sysconfdir}/pam.d/mate-system-log
%{_datadir}/glib-2.0/schemas/org.mate.system-log.gschema.xml
%{_datadir}/applications/mate-system-log.desktop
%{_mandir}/man1/mate-system-log.1.*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-system-log-symbolic.svg

%files -n mate-screenshot
%{_bindir}/mate-screenshot
%{_bindir}/mate-panel-screenshot
%{_datadir}/metainfo/mate-screenshot.appdata.xml
%{_datadir}/applications/mate-screenshot.desktop
%{_mandir}/man1/mate-screenshot.1.*
%{_mandir}/man1/mate-panel-screenshot.1.gz
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml

%files -n mate-dictionary -f mate-dictionary.lang
%doc mate-dictionary/AUTHORS
%doc mate-dictionary/README.md
%{_bindir}/mate-dictionary
%{_datadir}/metainfo/mate-dictionary.appdata.xml
%{_datadir}/applications/mate-dictionary.desktop
%{_datadir}/mate-dict/
%{_datadir}/mate-dictionary/
#%%{_libexecdir}/mate-dictionary-applet
%{_libdir}/libmatedict.so.*
%{_libdir}/mate-utils/libmate-dictionary-applet.so*
%{_mandir}/man1/mate-dictionary.1.*
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service

%files -n mate-search-tool -f mate-search-tool.lang
%{_bindir}/mate-search-tool
%{_datadir}/metainfo/mate-search-tool.appdata.xml
%{_datadir}/applications/mate-search-tool.desktop
%{_mandir}/man1/mate-search-tool.1.*
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%{_datadir}/pixmaps/mate-search-tool/

%files -n mate-disk-image-mounter
%{_bindir}/mate-disk-image-mounter
%{_datadir}/applications/mate-disk-image-mounter.desktop

%files -n mate-disk-usage-analyzer -f mate-disk-usage-analyzer.lang
%doc baobab/AUTHORS
%doc baobab/README.md
%{_bindir}/mate-disk-usage-analyzer
%{_datadir}/metainfo/mate-disk-usage-analyzer.appdata.xml
%{_datadir}/applications/mate-disk-usage-analyzer.desktop
%{_mandir}/man1/mate-disk-usage-analyzer.1.*
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/mate-disk-usage-analyzer.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-2
- disable pt language for help in search tool again

* Tue May 09 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-3
- add upstream commits from 1.26 branch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Sun Feb 02 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.2-1
- update to 1.23.3
- fix f32 mass rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-2
- drop non needed build requires

* Tue Sep 24 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-1
- update to 1.22.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-1
- update to 1.20.1 release

* Sun Feb 11 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- drop GSettings Schema rpm scriplet
- switch to using autosetup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.1-1
- update 1.19.1 release
- add style class for logviewer

* Sat Aug 26 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 1.18.2-2
- Rebuilt for libgtop2 soname bump

* Sat May 06 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.2-1
- update to 1.18.2
- fix a runtime warning with mate-screenshot

* Tue Apr 04 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-1
- update to 1.18.1

* Tue Mar 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update 1.17.0 release

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Fri Sep 02 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-1
- update to 1.15.1 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release
- switch to gtk+3

* Thu Apr 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Wed Sep 02 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.3.1
- update to 1.10.3 release

* Sat Jul 11 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-1
- update to 1.10.2 release
- remove upstreamed patches

* Fri Jul 03 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-0.1.git20150629.d353869
- fix help

* Thu Jun 18 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release
- remove upstreamed patches

* Wed Jun 17 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-2
- fix translations in gsettings

* Thu May 07 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release
- add patch to fix f23 build

* Mon Apr 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release

* Fri Jan 23 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-2
- rebuild for libgtop2 soname bump

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90
- add --disbale-maintainer-flags configure flag

* Tue Feb 11 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-2
- fix build on ARM
- remove --disable-scrollkeeper configure flag
- add --with-gnome --all-name for find language
- remove usage of hardlink, no need anymore
- fix usage of desktop-file-install
- re-work configure flags
- add BR yelp-tools

* Sun Feb 09 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Mon Jan 6 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-1
- update to 1.6.1 release
- use modern 'make install' macro
- removed upstreamed patches
- add gtk-doc dir to -devel subpackage
- mate-disk-usage-analyzer icons are renamed, moved to hicolor dir

* Tue Oct 22 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-10
- add runtime require mate-desktop-libs for mate-system-log, rhbz (#1016935)

* Tue Oct 22 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-9
- screenshot: do not segfault when taking a window picture with no delay
- fix rhbz (#1022082)
 
* Thu Sep 05 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-8
- Files and libs duplicated in mate-dictionary and mate-utils (#1003196)
- drop mate-dictionary-devel
- add -common subpkg (for licenses, translations)
- make main empty metapackage, that pulls all subpkgs 
- only mate-system log uses usermode (consolehelper)

* Thu Aug 08 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-7
- runtime require mate-desktop-libs for mate-search-tool
- and main package, fix rhbz #988278

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-5
- add upstream patch to fix rhbz #975199

* Tue Jul 02 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-4
- add mate-dictionary binary to subpackage, rhbz #980434
- add mate-dictionary applet dbus file to subpackage, rhbz #980434
- move baobab docs to mate-disk-usage-analyzer subpackage
- add missing copying files to some subpackages
- move baobab icons to mate-disk-usage-analyzer subpackage
- add baobab icons to main packackes
- add rpm spriptlets for mate-disk-usage-analyzer
- remove mime-types spriptlets,
- because there are not mime-types in desktop files
- remove icon-cache sriptlets from most subpackages,
- only needed for main and mate-disk-usage-analyzer package
- remove glib-compile-schemas from all %%post sections
- remove BR gsettings-desktop-schemas-devel
- remove BR glib2-devel, already called by mate-common
- add -devel subpackage for mate-dictionary
- add mate-search-tool binary to main package
- add /usr/share/mate-dictionary directory to main package

* Sat Jun 15 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-3
- Update gtk-update-icon-cache scriptlet 

* Sat Jun 15 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-2
- Split all the packages up in to sub packages (882184)
- Update source URL
- Remove useless convert files
- Own dirs we're supposed to own

* Sat Apr 13 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Mon Feb 18 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.0-1
- Update to latest upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.4.0-7
- gdict_applet option (don't build by default)
- minor cleanup

* Fri Dec 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-6
- revert -5 changes (#884886)

* Thu Nov 08 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-4
- rebuild for 1.5.0
- drop gdict-applet till upstream fixes it

* Mon Nov 05 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-3
- sort out lang file mess
- link identical immages in help to save space
- fix directory ownership of help files
- add build requires mate-conf-devel
- add build requires desktop-file-utils

* Sun Nov 04 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-2
- add build requires popt-devel

* Tue Oct 23 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Initial build

