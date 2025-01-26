# Disable automatic .la file removal
%global __brp_remove_la_files %nil
%global configure ./configure~

Name:    kdewebdev
Summary: Web development applications 
Epoch:   6
Version: 3.5.10
Release: 59%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Url:     http://kdewebdev.org/ 

Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Source1: http://download.sourceforge.net/quanta/css.tar.bz2
Source2: http://download.sourceforge.net/quanta/html.tar.bz2
Source3: http://download.sourceforge.net/quanta/php_manual_en_20030401.tar.bz2
Source4: http://download.sourceforge.net/quanta/javascript.tar.bz2
Source5: hi48-app-kxsldbg.png

Patch0: javascript.patch
Patch1: kdewebdev-3.5.4-kxsldbg-icons.patch
# fixes crash in kimagemapeditor when using freehand tool
Patch3: kdewebdev-3.5.10-fix-freehand-crash.patch
# fixes using a temporary as a lvalue in KafkaPart (FTBFS with g++ 4.6, probably
# silently did the wrong thing before)
Patch4: kdewebdev-3.5.10-gcc46.patch
# docbParseFile is dropped in libxml2-2.9 amd later
Patch6: kdewebdev-3.5.10-docbParseFile.patch

# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
# fix aarch64 FTBFS due to libtool not liking the file output on *.so files
Patch303: kde3-libtool-aarch64.patch
# autoconf 2.7x
Patch304: kde3-autoconf-version.patch
# automake-1.16.5
Patch305: kdewebdev-3.5.10-automake-1.16.5.patch
Patch306: kdewebdev-3.5.10-libxml-ftbfs.patch
Patch307: kdewebdev-configure-c99.patch
# ftbfs, include cstdlib
Patch308: kdewebdev-3.5.10-include-cstdlib.patch
Patch309: kdewebdev-3.5.10-ftbfs.patch

BuildRequires: gcc gcc-c++
BuildRequires: automake libtool
BuildRequires: desktop-file-utils
BuildRequires: kdelibs3-devel >= %{version}
BuildRequires: libxslt-devel libxml2-devel
BuildRequires: perl-interpreter
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

# should be optional but no hint support anymore
#Requires: gnupg
Requires: tidy

Provides: kdewebdev3 = %{version}-%{release}

Obsoletes: quanta < %{epoch}:%{version}-%{release}
Provides:  quanta = %{epoch}:%{version}-%{release}

%define kommander_ver 1.2.2
#Obsoletes: kommander < %{kommander_ver}-%{release}
Provides:  kommander = %{kommander_ver}-%{release}

%description
%{summary}, including:
* kfilereplace: batch search and replace tool
* kimagemapeditor: HTML image map editor
* klinkstatus: link checker
* kommander: visual dialog building tool
* kxsldbg: xslt Debugger
* quanta+: web development

%package devel
Summary: Header files and documentation for %{name} 
Provides: kdewebdev3-devel = %{version}-%{release}
Requires: kdelibs3-devel
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: quanta-devel < %{epoch}:%{version}-%{release}
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
Requires: kdelibs3%{?_isa} >= %{version}
# helps multilib upgrades
#Obsoletes: %{name} < %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:  %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q -a 1 -a 2 -a 3 -a 4
%patch -P0 -p0 -b .javascript
%patch -P1 -p1 -b .kxsldbg-icons
%patch -P3 -p1 -b .fix-freehand-crash
%patch -P4 -p1 -b .gcc46
%patch -P6 -p1 -b .docbParseFile

install -m644 -p %{SOURCE5} kxsldbg/

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .autoconf-2.7x
%patch -P305 -p1 -b .automake-1.16.5
%patch -P306 -p1 -b .ftbfs
%patch -P307 -p1 -b .configure-c99
%patch -P308 -p1 -b .ftbfs
%patch -P309 -p1 -b .ftbfs

make -f admin/Makefile.common cvs


%build
unset QTDIR && . /etc/profile.d/qt.sh

export CXXFLAGS="%{optflags} -std=gnu++98 -fpermissive"

%configure \
  --includedir=%{_includedir}/kde \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \

make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

## package separately?  Why doesn't upstream include this? -- Rex
# install docs
for i in css html javascript ; do
   pushd $i
   ./install.sh <<EOF
%{buildroot}%{_datadir}/apps/quanta/doc
EOF
   popd
   rm -rf $i
done
cp -a php php.docrc %{buildroot}%{_datadir}/apps/quanta/doc/

# make symlinks relative
pushd %{buildroot}%{_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -nfs ../common $i
   fi
done
popd

# rpmdocs
for dir in k* quanta; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001

%post
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
done

%postun
if [ $1 -eq 0 ] ; then
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
fi

%posttrans
for f in crystalsvg locolor ; do
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done

%ldconfig_scriptlets libs

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%doc rpmdocs/*
%{_bindir}/*
%{_libdir}/kde3/*
%{_datadir}/applications/kde/*
%{_datadir}/applnk/.hidden/*
%{_datadir}/apps/*
%doc %{_datadir}/apps/quanta/doc
%{_datadir}/config.kcfg/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_docdir}/HTML/en/*

%files libs
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files devel
%{_libdir}/lib*.so
%{_includedir}/kde/*


%changelog
* Fri Jan 24 2025 Than Ngo <than@redhat.com> - 6:3.5.10-59
- Fixed rhbz#2340693 - kdewebdev: FTBFS in Fedora rawhide/f42

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 6:3.5.10-57
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Than Ngo <than@redhat.com> - 3.5.10-55
- fixed bz#2261272 - FTBFS in Fedora rawhide

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Florian Weimer <fweimer@redhat.com> - 6:3.5.10-51
- Port configure script to C99 (#2167643)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Than Ngo <than@redhat.com> - 6:3.5.10-49
- Fixed FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 31 2022 Than Ngo <than@redhat.com> - 6:3.5.10-47
- Fixed FTBFS with automake-1.16.5

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 6:3.5.10-46
- Disable automatic .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Than Ngo <than@redhat.com> - 3.5.10-44
- Fixed bz#1999502, FTBFS with autoconf-2.7x

* Tue Jul 27 2021 Than Ngo <than@redhat.com> - 3.5.10-43
- Fixed FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-36
- Fix aarch64 FTBFS due to libtool not liking the file output on *.so files

* Mon Jul 23 2018 Than Ngo <than@redhat.com> - 3.5.10-35
- fixed FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6:3.5.10-33
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6:3.5.10-31
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-27
- Add -std=gnu++98 to the CXXFLAGS to fix FTBFS (#1307686)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6:3.5.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6:3.5.10-24
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-20
- use automake --force-missing to get aarch64 support (#925029/#925627)
- also use automake --copy (the default is symlinking)

* Sat Mar 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-19
- unify KDE 3 autotools fixes between packages

* Fri Mar 08 2013 Than Ngo <than@redhat.com> - 3.5.10-18
- fix build failure with libxml2-2.9

* Thu Mar 07 2013 Than Ngo <than@redhat.com> - 3.5.10-17
- fix build failure with automake-1.13

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-14
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 29 2011 Than Ngo <than@redhat.com> - 6:3.5.10-12
- drop old fedora conditions

* Thu Mar 10 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.10-11
- fix g++ 4.6 FTBFS properly, don't use a temporary as an lvalue, the code
  probably silently did the wrong thing when built with an older g++
- drop -fpermissive (which should never be used)

* Wed Mar 09 2011 Jaroslav Reznik <jreznik@redhat.com> - 6:3.5.10-10
- fixes crash in kimagemapeditor when using freehand tool
- add -fpermissive to build with gcc 4.6+

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Thomas Janssen <thomasj@fedoraproject.org> 6:3.5.10-8
- rebuild for new libxml2

* Tue Feb 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:3.5.10-7
- ressurrect -libs subpkg (legacy crud removal fallout)

* Mon Feb 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 6:3.5.10-6
- drop some legacy crud
- optimize scriptlets

* Fri Jan 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.10-5
- fix FTBFS with autoconf >= 2.64 (#538907)

* Wed Jul 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 6:3.5.10-4
- FTBFS kdewebdev-3.5.10-2.fc11 (#511439)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6:3.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.10-1
- update to 3.5.10

* Wed Jun 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.9-4
- reinclude crystalsvg icons also on f9+ (no longer using crystalsvg from KDE 4)

* Fri Mar 28 2008 Rex Dieter <rdieter@fedoraproject.org> - 6:3.5.9-3
- drop Requires: gnupg
- omit multilib upgrade hacks

* Tue Mar 04 2008 Rex Dieter <rdieter@fedoraproject.org> - 6:3.5.9-2
- -libs: Requires: %%name, fixes "yum update removes kdewebdev" (#435956)

* Fri Feb 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.9-1
- update to 3.5.9
- drop rename-arrow patch (fixed upstream, arrow icon is now app-local)
- drop gcc43 patch (fixed upstream)

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.8-7
- rebuild for GCC 4.3

* Sat Jan 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.8-6
- apply upstream build fix for GCC 4.3 (IS_BLANK macro name conflict w/ libxml)

* Mon Dec 24 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 6:3.5.8-5
- remove crystalsvg icon which conflicts with kdeartwork (F9+) (#426694)

* Wed Dec 5 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 6:3.5.8-4
- rename arrow.png because it confuses KDE 4 (kde#153476)
- drop BR: kdesdk3 on F9+

* Tue Oct 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.8-3
- -libs: Obsoletes: %%name ... to help out multilib upgrades
- -libs conditional (f8+)

* Mon Oct 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.8-2
- -libs subpkg (more multilib friendly
- kommander_ver 1.2.2

* Sat Oct 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.8-1
- kde-3.5.8

* Thu Sep 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-2
- License: GPLv2
- update %%description
- Provides: kdewebdev3 kommander 
- BR: kdelibs3

* Mon Jun 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-1
- 3.5.7
- +Requires(hint): gnupg tidy
- use Versioned Obsoletes/Provides: quanta

* Thu Feb 08 2007 Than Ngo <than@redhat.com> 6:3.5.6-1.fc7
- 3.5.6

* Fri Aug 25 2006 Than Ngo <than@redhat.com> 6:3.5.4-2
- fix #203893, add missing icon for kxsldbg

* Thu Aug 10 2006 Than Ngo <than@redhat.com> 6:3.5.4-1
- rebuild

* Mon Jul 24 2006 Than Ngo <than@redhat.com> 6:3.5.4-0.pre1
- prerelease of 3.5.4 (from the first-cut tag)

* Fri Jul 14 2006 Than Ngo <than@redhat.com> 6:3.5.3-2
- BR: autoconf automake libtool

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.3-1.1
- rebuild

* Mon Jun 05 2006 Than Ngo <than@redhat.com> 6:3.5.3-1
- update to 3.5.3

* Wed Apr 05 2006 Than Ngo <than@redhat.com> 6:3.5.2-1
- update to 3.5.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb 05 2006 Than Ngo <than@redhat.com> 6:3.5.1-1 
- 3.5.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Dec 04 2005 Than Ngo <than@redhat.com> 6:3.5.0-1
- 3.5

* Tue Oct 25 2005 Than Ngo <than@redhat.com> 6:3.4.92-1
- update to 3.5 beta2

* Mon Oct 10 2005 Than Ngo <than@redhat.com> 6:3.4.91-1
- update to 3.5 beta 1

* Mon Sep 26 2005 Than Ngo <than@redhat.com> 6:3.4.2-3
- remove tidy since it's included in extras #169217

* Thu Sep 22 2005 Than Ngo <than@redhat.com> 6:3.4.2-2
- fix uic build problem

* Thu Aug 11 2005 Than Ngo <than@redhat.com> 6:3.4.2-1
- update to 3.4.2

* Wed Jun 29 2005 Than Ngo <than@redhat.com> 6:3.4.1-1
- 3.4.1
- fix gcc4 build problem

* Wed May 04 2005 Than Ngo <than@redhat.com> 6:3.4.0-3
- apply patch to fix CAN-2005-0754, Kommander untrusted code execution,
  thanks to KDE security team

* Tue Apr 19 2005 Than Ngo <than@redhat.com> 6:3.4.0-2
- add kdesdk in buildrequires #155054

* Sat Mar 19 2005 Than Ngo <than@redhat.com> 6:3.4.0-1
- 3.4.0

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.2
- rebuilt against gcc-4.0.0-0.31

* Mon Feb 28 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.1
- 3.4.0 rc1

* Mon Feb 21 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.1
- 3.4 beta2

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.1
- update to 3.3.2
- add missing tidy for HTML syntax checking #140970

* Mon Oct 18 2004 Than Ngo <than@redhat.com> 6:3.3.1-2
- rebuilt

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 6:3.3.1-1
- update to 3.3.1

* Thu Sep 16 2004 Than Ngo <than@redhat.com> 3.3.0-1
- update to 3.3.0

* Sat Jun 19 2004 Than Ngo <than@redhat.com> 3.2.3-1 
- update to 3.2.3

* Sun Apr 11 2004 Than Ngo <than@redhat.com> 3.2.2-0.1
- 3.2.2 release

* Fri Mar 05 2004 Than Ngo <than@redhat.com> 6:3.2.1-1
- 3.2.1 release

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 17 2004 Than Ngo <than@redhat.com> 6:3.2.0-1.2
- fix typo bug, _smp_mflags instead smp_mflags

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 11 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.1
- 3.2.0 release
- built against qt 3.3.0

* Thu Jan 22 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.1
- 3.2 RC1

* Thu Dec 11 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.3
- fix build problem with new gcc

* Thu Dec 04 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.2
- remove quanta-3.1.93-xml2.patch, which is included in upstream

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.1
- KDE 3.2 Beta2

* Thu Nov 27 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.3
- get rid of rpath

* Tue Nov 25 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.2
- add fix to build against new libxml2 >= 2.6

* Thu Nov 13 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.1
- KDE 3.2 Beta 1
- cleanup
- add devel package

* Tue Sep 30 2003 Than Ngo <than@redhat.com> 6:3.1.4-1
- 3.1.4

* Tue Aug 12 2003 Than Ngo <than@redhat.com> 6:3.1.3-1
- 3.1.3
- update php docs (bug #99073)
- desktop issue (bug #87602)


* Wed Jun 25 2003 Than Ngo <than@redhat.com> 3.1.2-4
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 20 2003 Than Ngo <than@redhat.com> 3.1.2-2
- 3.1.2

* Thu Mar 20 2003 Than Ngo <than@redhat.com> 3.1.1-1
- 3.1.1

* Fri Jan 31 2003 Than Ngo <than@redhat.com> 3.1-1
- 3.1 final

* Sat Nov 30 2002 Than Ngo <than@redhat.com> 3.1-0.2
- cleanup scpecfile
- desktop file issue
- add missing %%post, %%postun ldconfig
- remove po files, it's now in kde-i18n stuff

* Thu Nov 28 2002 Than Ngo <than@redhat.com> 3.1-0.1
- update to 3.1 rc4

* Fri Aug 23 2002 Phil Knirsch <pknirsch@redhat.com> 3.0-0.pr1.5
- Rebuilt with new qt.

* Mon Aug 12 2002 Tim Powers <timp@redhat.com> 3.0-0.pr1.4
- rebuilt with gcc-3.2

* Sun Aug  4 2002 han Ngo <than@redhat.com> 3.0-0.pr1.3
- 3.0-pr1 release
- fixed desktop file issue

* Tue Jul 23 2002 Tim Powers <timp@redhat.com> 3.0-0.pr1.2
- build using gcc-3.2-0.1

* Sun Jul 14 2002 Than Ngo <than@redhat.com> 3.0-0.pr1.1
- 3.0-pr1 fixed bug #68268
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-0.cvs20020523.1
- Update, fix build with current toolchain

* Tue Apr 16 2002 Than Ngo <than@redhat.com> 2.1-0.cvs20020404.2
- rebuild

* Thu Apr  4 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-0.cvs20020404.1
- Fix bug #62648

* Tue Mar 26 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-0.cvs20020326.1
- Update
- %%langify spec file
- Move desktop file to /etc/X11/applnk; quanta is generally useful

* Tue Jan 29 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-0.cvs20020129.1
- Update, fix build, KDE3ify

* Thu Aug 23 2001 Than Ngo <than@redhat.com> 2.0-0.cvs20010724.2
- fix quanta crashes on exit (Bug #51180)
- fix bad character (Bug #51509)

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0-0.cvs20010724.1
- langify
- remove ia64 workarounds
- update

* Mon Jul 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0-0.cvs20010723.1
- Update
- Make symlinks relative

* Thu Feb 22 2001 Than Ngo <than@redhat.com>
- update to 2.0pr1

* Wed Feb  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to get rid of libkdefakes.so.0 requirement

* Thu Jan  4 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Initial build, obsoletes WebMaker
