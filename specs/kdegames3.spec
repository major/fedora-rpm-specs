
%define debug 0
%define final 0

# These games are already in KDE 4.
%define donotcompilelist atlantik katomic kbattleship kblackbox kbounce kgoldrunner kjumpingcube klickety klines kmahjongg kmines knetwalk kolf konquest kpat kreversi ksame kshisen ksokoban kspaceduel ktron ktuberling kwin4 lskat

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Name:    kdegames3
Summary: KDE 3 Games not ported to KDE 4
Version: 3.5.10
Release: 52%{?dist}

License: GPL-2.0-only
Url:     http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdegames-%{version}.tar.bz2
Patch0: kdegames-3.5.10-trademarks.patch
# fix FTBFS with the new stricter ld in F13 (#565113)
Patch2: kdegames-3.5.10-ftbfs.patch
Patch3: kde3-autoconf-version.patch
# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
Patch303: kdegames-configure-c99.patch
# fix build with autoconf 2.72
Patch304: kde3-autoconf-2.72.patch

Requires: kdelibs3 >= %{version}
# directory ownership
Requires: hicolor-icon-theme kde-filesystem

Conflicts: kdegames < 6:3.80

Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires: kdelibs3-devel >= %{version}
BuildRequires: automake libtool
BuildRequires: make

%description
Games and gaming libraries for KDE which have not been ported to KDE 4 yet.
Included with this package are: kasteroids, kbackgammon,
kenolaba, kfouleggs, kpoker, ksirtet, ksmiletris, ksnakerace.

%package libs
Summary: %{name} runtime libraries
Requires: kdelibs3 >= %{version}
License: LGPLv2
%description libs
%{summary}.


%prep
%setup -q -n kdegames-%{version}
%patch -P0 -p1
%patch -P2 -p1 -b .ftbfs
%patch -P3 -p1 -b .autoconf2.7x

export DO_NOT_COMPILE="%{donotcompilelist}"

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1
%patch -P304 -p1
make -f admin/Makefile.common cvs


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export DO_NOT_COMPILE="%{donotcompilelist}"

%configure \
   --disable-new-ldflags \
   --disable-dependency-tracking \
   --disable-rpath \
%if %{final}
   --enable-final \
%endif
%if %{debug} == 0
   --disable-debug \
   --disable-warnings \
%endif
   --includedir=%{_includedir}/kde \
   --disable-setgid

%make_build


%install
export DO_NOT_COMPILE="%{donotcompilelist}"
%make_install

# locales
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    # remove documentation for games we don't ship
    pushd $lang_dir
      for i in *; do
        case "%{donotcompilelist}" in
          *$i*)
            # $i is listed in %{donotcompilelist}, zap
            [ -d $i ] && rm -rf $i
          ;;
        esac
      done
      rm -rf kdegames-apidocs
    popd
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
      done
    popd
  fi
done
fi

# rpmdocs
for dir in atlantik k* ; do
  case "%{donotcompilelist}" in
    *$dir*)
      # $dir is listed in %{donotcompilelist}, skip
    ;;
    *)
      for file in AUTHORS ChangeLog README TODO ; do
        test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
      done
    ;;
  esac
done

# remove libkdegames devel stuff, not used by anything and conflicts with KDE 4
rm -rf %{buildroot}%{_includedir}/kde/k* %{buildroot}%{_libdir}/libkdegames.so

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001


%files -f %{name}.lang
%doc AUTHORS README
%doc rpmdocs/*
%license COPYING*
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/*
%{_datadir}/config.kcfg/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*

%ldconfig_scriptlets libs

%files libs
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun May 19 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 3.5.10-50
- Drop ksokoban, replaced by skladnik based on KF6
- Fix build with autoconf 2.72

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 3.5.10-47
- Drop atlantik, now available separately based on KF5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Florian Weimer <fweimer@redhat.com> - 3.5.10-45
- Port configure script to C99 (#2190286)

* Tue Feb 21 2023 Than Ngo <than@redhat.com> - 3.5.10-44
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 3.5.10-41
- Disable automatic .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Than Ngo <than@redhat.com> - 3.5.10-39
- Fixed bz#1999503, FTBFS with autoconf-2.7x

* Tue Jul 27 2021 Than Ngo <than@redhat.com> - 3.5.10-38
- Fixed FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-35
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-30
- .spec cleanup, use %%make_build %%make_install %%license %%ldconfig_scriptlets

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5.10-27
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.5.10-21
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.5.10-19
- Fix FTBFS due to --enable-new-ldflags (#1028849, #1106999)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-16
- use automake --force-missing to get aarch64 support (#925029/#925627)
- also use automake --copy (the default is symlinking)

* Sat Mar 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-15
- unify KDE 3 autotools fixes between packages

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-12
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-9
- drop Klickety, now in KDE 4 kdegames (#656523)
- refer to ksnake as KSnakeRace in the description, since that's how it shows up
  in the menu, and to distinguish it from KDE 4 KSnakeDuel's KSnake mode

* Mon Feb 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-8
- enable "make_cvs" (as in other KDE 3 stuff) so we can patch Makefile.am
- fix build with make_cvs enabled and automake >= 1.11
- fix build with make_cvs enabled and autoconf >= 2.64
- fix FTBFS with the new stricter ld in F13 (#565113)

* Wed Dec 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 3.5.10-7
- Repositioning the KDE Brand (#547361)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-5
- drop KSnakeDuel, part of kdegames since 4.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-3
- readd kbackgammon, not actually part of KDE 4

* Wed Sep 17 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-2
- remove no longer used libkdegames development files

* Fri Aug 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-1
- update to 3.5.10
- update trademarks patch

* Wed Jun 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-2
- reinclude crystalsvg icons also on f9+ (no longer using crystalsvg from KDE 4)

* Fri Feb 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-1
- update to 3.5.9
- update trademarks patch

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-4
- rebuild for GCC 4.3

* Mon Dec 24 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-3
- remove crystalsvg icons which conflict with kdeartwork (F9+) (#426694)

* Thu Nov 29 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-2
- clarify Summary

* Fri Oct 26 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-1
- update to 3.5.8
- fix/update trademarks patch (Rex Dieter)
- License: GPLv2, libs/devel License: LGPLv2
- libs subpkg (more multilib friendly)
- include ksirtet (has been omitted from KDE 4.0)
- drop kpoker-desktop patch (fixed upstream)

* Wed Aug 08 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.7-4
- patch out the trademarked names of a certain box pushing game and a certain
  snake-like duel game

* Fri Jul 27 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.7-3
- Conflicts with pre-KDE-4 kdegames

* Fri Jul 27 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.7-2
- drop RHEL conditional using patched tarball
- fix macro in changelog
- don't mark %%{_datadir}/config.kcfg/* as %%config
- add Requires on hicolor-icon-theme and kde-filesystem for dir ownership
- patch out obsolete Miniicon= line from kpoker.desktop

* Tue Jul 17 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.7-1
- rename to kdegames3
- drop Epoch
- change R/BR to kdelibs3(-devel)
- drop Konquest part as Konquest is now part of KDE 4
- build and install only games which aren't part of KDE 4
- add mkdir %%{buildroot} after the rm -rf %%{buildroot}

* Mon Jun 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-1
- 3.5.7

* Tue Apr 24 2007 Than Ngo <than@redhat.com> - 6:3.5.6-3.fc7
- cleanup

* Tue Mar 06 2007 Than Ngo <than@redhat.com> - 6:3.5.6-2.fc7
- cleanup 

* Wed Feb 07 2007 Than Ngo <than@redhat.com> 6:3.5.6-1.fc7
- 3.5.6

* Thu Aug 10 2006 Than Ngo <than@redhat.com> 6:3.5.4-1
- rebuild

* Mon Jul 24 2006 Than Ngo <than@redhat.com> 6:3.5.4-0.pre1
- prerelease of 3.5.4 (from the first-cut tag)

* Thu Jul 13 2006 Dennis Gregorovic <dgregor@redhat.com> - 6:3.5.3-2.2
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.3-2.1
- rebuild

* Thu Jun 08 2006 Than Ngo <than@redhat.com> 6:3.5.3-2
- move only *.so symlinks to -devel subpackage
- enable --enable-new-ldflags since ld bug fixed

* Fri Jun 02 2006 Than Ngo <than@redhat.com> 6:3.5.3-1
- update to 3.5.3

* Tue Apr 04 2006 Than Ngo <than@redhat.com> 6:3.5.2-1
- update to 3.5.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Than Ngo <than@redhat.com> 6:3.5.1-1 
- 3.5.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Dec 05 2005 Than Ngo <than@redhat.com> 6:3.5.0-1
- 3.5

* Tue Nov 15 2005 Than Ngo <than@redhat.com> 6:3.4.92-2
- apply patch to fix build problem with gcc4

* Tue Oct 25 2005 Than Ngo <than@redhat.com> 6:3.4.92-1
- update to 3.5 Beta2

* Wed Oct 05 2005 Than Ngo <than@redhat.com> 6:3.4.91-1
- update to 3.5 Beta1

* Mon Aug 08 2005 Than Ngo <than@redhat.com> 6:3.4.2-1
- update to 3.4.2

* Tue Jun 28 2005 Than Ngo <than@redhat.com> 6:3.4.1-1
- 3.4.1

* Fri Mar 18 2005 Than Ngo <than@redhat.com> 6:3.4.0-1
- 3.4.0

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.2
- rebuilt against gcc-4.0.0-0.31

* Sat Feb 26 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.1
- KDE-3.4.0 rc1

* Sun Feb 20 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.1
- KDE-3.4 beta2

* Mon Jan 31 2005 Than Ngo <than@redhat.com> 3.3.2-0.2
- fix a bug in changeBackside #146609

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.1
- update to 3.3.2

* Mon Oct 18 2004 Than Ngo <than@redhat.com> 6:3.3.1-2
- add missing klickety icons #135614

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 6:3.3.1-1 
- update to 3.3.1

* Fri Oct 08 2004 Than Ngo <than@redhat.com> 6:3.3.0-2
- fix buildrequire on automake
- disable ksokoban

* Mon Aug 23 2004 Than Ngo <than@redhat.com> 3.3.0-1
- update to 3.3.0 release

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 3.3.0-0.1.rc2
- update to 3.3.0 rc2

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 3.3.0-0.1.rc1
- update to 3.3.0 rc1

* Wed Aug 04 2004 Than Ngo <than@redhat.com> 3.2.92-1
- update to 3.3 Beta 2

* Sat Jun 19 2004 Than Ngo <than@redhat.com> 3.2.3-2
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 02 2004 Than Ngo <than@redhat.com> 6:3.2.3-0.1
- update to 3.2.3

* Wed Apr 14 2004 Than Ngo <than@redhat.com> 6:3.2.2-1
- update to 3.2.2

* Thu Apr 08 2004 Than Ngo <than@redhat.com> 6:3.2.1-4
- fix dependency bug again, bug #120399

* Wed Apr 07 2004 Than Ngo <than@redhat.com> 3.2.1-3
- add missing icons, bug #118281

* Mon Mar 22 2004 Than Ngo <than@redhat.com> 6:3.2.1-2
- fixed klickety crash, bug #118280

* Sun Mar 07 2004 Than Ngo <than@redhat.com> 6:3.2.1-1
- 3.2.1 release

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Than Ngo <than@redhat.com> 6:3.2.0-1.4
- gcc 3.4 build problem

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 05 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.3
- 3.2.0 release
- built against qt 3.3.0
- add Prereq /sbin/ldconfig

* Mon Jan 19 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.1
- KDE 3.2 RC1

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.1
- KDE 3.2 Beta2

* Thu Nov 27 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.2
- get rid of rpath

* Tue Nov 11 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.1
- KDE 3.2 Beta1
- cleanup specfile
- remove some patch files, which are included in new upstream

* Mon Oct 13 2003 Than Ngo <than@redhat.com> 6:3.1.4-2
- backport from CVS to fix atlantikdesigner crashed on startup
- fix miscompiled code, (bug #106198, #106888)

* Tue Sep 30 2003 Than Ngo <than@redhat.com> 6:3.1.4-1
- 3.1.4

* Tue Aug 12 2003 Than Ngo <than@redhat.com> 6:3.1.3-3
- fix build problem with gcc 3.3

* Wed Aug 06 2003 Than Ngo <than@redhat.com> 6:3.1.3-2
- rebuilt

* Sun Aug 03 2003 Than Ngo <than@redhat.com> 6:3.1.3-1
- 3.1.3

* Mon Jul  7 2003 Than Ngo <than@redhat.com> 3.1.2-5
- fix a bug in katomic, which caused icons are invisible (bug #89628)

* Thu Jun 26 2003 Than Ngo <than@redhat.com> 3.1.2-4
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 19 2003 Than Ngo <than@redhat.com> 3.1.2-0.9x.2
- 3.1.2

* Thu May  8 2003 Than Ngo <than@redhat.com> 3.1.1-3
- fix command line option (bug #90082)

* Wed Apr 30 2003 Elliot Lee <sopwith@redhat.com> 3.1.1-2
- headusage patch (from kdebindings) for ppc64

* Wed Mar 19 2003 Than Ngo <than@redhat.com> 3.1.1-1
- 3.1.1

* Thu Feb 27 2003 Than Ngo <than@redhat.com> 3.1-5
- add requires kdebase (#84679)

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Fri Feb 21 2003 Than Ngo <than@redhat.com> 3.1-3
- get rid of gcc path from dependency_libs

* Thu Feb 13 2003 Than Ngo <than@redhat.com> 3.1-2
- rebuild against new arts

* Tue Jan 28 2003 Than Ngo <than@redhat.com> 3.1-1
- 3.1 final

* Mon Jan 27 2003 Than Ngo <than@redhat.com> 3.1-0.6
- add missing plugins
- cleanup specfile

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 6:3.1-0.5
- rebuild

* Tue Jan 14 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.3
- fixed missing file

* Tue Jan 14 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.3
- rc6
- removed size_t check
- excluded ia64

* Fri Nov 29 2002 Than Ngo <than@redhat.com> 3.1-0.2
- desktop file issues

* Wed Nov 27 2002 Than Ngo <than@redhat.com> 3.1-0.1
- update to 3.1 rc4

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 3.0.5-1
- update to 3.0.5

* Tue Oct 15 2002 Than Ngo <than@redhat.com> 3.0.4-1
- 3.0.4

* Fri Sep 13 2002 Than Ngo <than@redhat.com> 3.0.3-3.1
- Fixed to build on x86_64

* Thu Aug 29 2002 Preston Brown <pbrown@redhat.com>
- remove kbattleship and ktron (#72763)

* Fri Aug 23 2002 Than Ngo <than@redhat.com> 3.0.3-2
- desktop files issues (bug #72408)

* Mon Aug 12 2002 Than Ngo <than@redhat.com> 3.0.3-1
- 3.0.3
- desktop files issues

* Tue Jul 23 2002 Tim Powers <timp@redhat.com> 3.0.2-2
- build using gcc-3.2-0.1

* Tue Jul 09 2002 Than Ngo <than@redhat.com> 3.0.2-1
- 3.0.2
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 10 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.1-1
- 3.0.1

* Tue Apr 16 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-2
- Change sonames

* Wed Mar 27 2002 Than Ngo <than@redhat.com> 3.0.0-1
- final

* Wed Mar  6 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020306.1
- Fix packaging glitch in monolithic version

* Tue Mar  5 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020305.1
- Make splits a buildtime option (off by default) on request

* Mon Jan  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020107.1
- Update to work with latest kdelibs changes

* Wed Dec 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20011226.1
- Update
- Add missing %%{_bindir}/kbattleship

* Sat Dec 15 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20011215.1
- Update
- Split into several packages (one package per game)

* Sun Jul 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010722.1
- Update
- Work around ia64 breakages
- Add build requirements (#48977)

* Thu Feb 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix problem when changing the card type (Bug #28824)

* Wed Feb 21 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.1-respin

* Tue Feb 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.1

* Sun Feb 11 2001 Than Ngo <than@redhat.com>
- don't use make -j CPU, it's broken

* Thu Feb  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Run ldconfig in %%post and %%postun to make libkdegames happy
- Replace absolute symlinks with relative symlinks (#24787)

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update
- includedir=/usr/include/kde,
  now that libkdegames installs kcarddeck.h

* Wed Jan 17 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Get rid of the gcc bug workaround, it's no longer needed

* Mon Jan  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update
- Don't exclude ia64

* Wed Nov 15 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to HEAD

* Sat Oct 28 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to KDE_2_0_BRANCH, now that the ".0 release" bugs are fixed.

* Mon Oct 16 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.0 final

* Tue Oct  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.0

* Mon Oct  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new CVS
- work around g++ bugs (in kjumpingcube)

* Thu Aug 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.93

* Mon Aug  7 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new version

* Wed Jul 19 2000 Than Ngo <than@redhat.de>
- fix docdir
- rebuild 16 July snapshot

* Thu Jul 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- SMPify
- don't hardcode QTDIR

* Tue Jul 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- use gcc 2.96
- new snapshot

* Tue Jun 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new snapshot
- ExcludeArch ia64 for now

* Sat Mar 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new snapshot
- move it to /usr, where it belongs

* Fri Oct 22 1999 Bernhard Rosenkraenzer <bero@redhat.de>
- 2.0 snapshot

* Fri Sep 24 1999 Preston Brown <pbrown@redhat.com>
- mark doc files as such

* Thu Sep 09 1999 Preston Brown <pbrown@redhat.com>
- 1.1.2 release.

* Fri Jun 11 1999 Preston Brown <pbrown@redhat.com> 
- snapshot, includes kde 1.1.1 + fixes

* Mon Apr 19 1999 Preston Brown <pbrown@redhat.com>
- last snapshot before release
- ripped out asteroids and sirtet

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- latest stable snapshot

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to KDE 1.1 final.

* Fri Feb 05 1999 Preston Brown <pbrown@redhat.com>
- rebuilt for new libstdc++ etc.

* Wed Jan 06 1999 Preston Brown <pbrown@redhat.com>
- re-merged updates from Duncan Haldane, change /opt/kde --> /usr

