%define double_profiling_build 1

Name:      hunspell
Summary:   A spell checker and morphological analyzer library
Version:   1.7.2
Release:   10%{?dist}
Source:    https://github.com/hunspell/hunspell/releases/download/v%{version}/hunspell-%{version}.tar.gz
URL:       https://github.com/hunspell/hunspell
License:   LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1
BuildRequires:  gcc-c++
BuildRequires: autoconf, automake, libtool, ncurses-devel, gettext-devel
BuildRequires: perl-generators
%ifarch %{ix86} x86_64
BuildRequires: valgrind
%endif
%if %{double_profiling_build}
BuildRequires: words
%endif
BuildRequires: make
Requires:  hunspell-en-US
Requires:  hunspell-filesystem = %{version}-%{release}

Patch0: 0001-Resolves-rhbz-2158548-allow-longer-words-for-hunspel.patch

%description
Hunspell is a spell checker and morphological analyzer library and program
designed for languages with rich morphology and complex word compounding or
character encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, LibreOffice UNO module.

%package devel
Requires: hunspell = %{version}-%{release}, pkgconfig
Summary: Files for developing with hunspell

%description devel
Includes and definitions for developing with hunspell

%package filesystem
Summary: Hunspell filesystem layout

%description filesystem
Provides a directory in which to store dictionaries provided by other
packages.

%prep
%setup -q
%patch -P0 -p1 -b .rhbz2158548

%build
autoreconf -vfi
configureflags="--disable-rpath --disable-static --with-ui --with-readline"

%define profilegenerate \
    CFLAGS="${RPM_OPT_FLAGS} -fprofile-generate"\
    CXXFLAGS="${RPM_OPT_FLAGS} -fprofile-generate"
%define profileuse \
    CFLAGS="${RPM_OPT_FLAGS} -fprofile-use"\
    CXXFLAGS="${RPM_OPT_FLAGS} -fprofile-use"

%if !%{double_profiling_build}
%configure $configureflags
%make_build
%else
#Generate a word list to use for profiling, take half of it to ensure
#that the original word list is then considered to contain correctly
#and incorrectly spelled words
head -n $((`cat /usr/share/dict/words | wc -l`/2)) /usr/share/dict/words |\
    sed '/\//d'> words

#generate profiling
%{profilegenerate} %configure $configureflags
%make_build
./src/tools/affixcompress words > /dev/null 2>&1
./src/tools/hunspell -d words -l /usr/share/dict/words > /dev/null
make check
make distclean

#use profiling
%{profileuse} %configure $configureflags
%make_build
%endif

%check
%ifarch %{ix86} x86_64
VALGRIND=memcheck make check
make check
%endif

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
mkdir $RPM_BUILD_ROOT/%{_datadir}/hunspell
mkdir $RPM_BUILD_ROOT/%{_datadir}/myspell
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README COPYING COPYING.LESSER COPYING.MPL AUTHORS license.hunspell license.myspell THANKS
%{_libdir}/*.so.*
%{_bindir}/hunspell
%{_mandir}/man1/hunspell.1.gz
%lang(hu) %{_mandir}/hu/man1/hunspell.1.gz

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_bindir}/affixcompress
%{_bindir}/makealias
%{_bindir}/munch
%{_bindir}/unmunch
%{_bindir}/analyze
%{_bindir}/chmorph
%{_bindir}/hzip
%{_bindir}/hunzip
%{_bindir}/ispellaff2myspell
%{_bindir}/wordlist2hunspell
%{_bindir}/wordforms
%{_libdir}/pkgconfig/hunspell.pc
%{_mandir}/man1/hunzip.1.gz
%{_mandir}/man1/hzip.1.gz
%{_mandir}/man3/hunspell.3.gz
%{_mandir}/man5/hunspell.5.gz

%files filesystem
%{_datadir}/hunspell
%{_datadir}/myspell

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Caolán McNamara <caolanm@redhat.com> - 1.7.2-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Caolán McNamara <caolanm@redhat.com> - 1.7.2-2
- Resolves: rhbz#2158548 get hunspell-ko working again

* Fri Dec 30 2022 Caolán McNamara <caolanm@redhat.com> - 1.7.2-1
- Resolves: rhbz#2157049 latest release

* Mon Aug 22 2022 Caolán McNamara <caolanm@redhat.com> - 1.7.1-1
- latest release

* Tue Aug 02 2022 Caolán McNamara <caolanm@redhat.com> - 1.7.0-21
- Resolves: rhbz#2113444 FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 16 2022 Jens Petersen <petersen@redhat.com> - 1.7.0-19
- rework the new hunspell dictionary directory (#2064189)
- drop the myspell/ compatibility symlink
- keep myspell/ as directory and also the new hunspell/ dir
- because of this drop the duplicate directory patch for #2060751
- filesystem scriptlets are no more

* Mon Mar 07 2022 Caolán McNamara <caolanm@redhat.com> - 1.7.0-18
- Resolves: rhbz#2060751 - “hunspell -D” lists dictionaries twice

* Thu Feb 10 2022 Jens Petersen <petersen@redhat.com> - 1.7.0-17
- revert post script from lua back to shell to unbreak rpm-ostree compose

* Mon Feb  7 2022 Jens Petersen <petersen@redhat.com> - 1.7.0-16
- pretrans and post scriptlets should be for filesystem!
  (fixes #2051360 regression reported by Mike Fabian)

* Wed Jan 26 2022 Jens Petersen <petersen@redhat.com> - 1.7.0-15
- improve the filesystem pretrans and post scripts:
- pretrans now checks if /usr/share/hunspell exists first
- post checks that /usr/share/myspell does not exist

* Wed Jan 26 2022 Jens Petersen <petersen@redhat.com> - 1.7.0-14
- requires coreutils for post script (#2045568)

* Fri Jan 21 2022 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1.7.0-13
- Rename install dir from myspell to hunspell & create symlink myspell
- https://fedoraproject.org/wiki/Changes/Hunspell_dictionary_dir_change

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Caolán McNamara <caolanm@redhat.com> - 1.7.0-10
- Resolves: rhbz#1943087 require gettext-devel for autopoint

* Wed Feb 03 2021 Peter Oliver <rpm@mavit.org.uk> - 1.7.0-9
- Accomodate Nuspell by putting the dictionary dir in its own subpackage.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1.7.0-6
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Caolán McNamara <caolanm@redhat.com> - 1.7.0-4
- Resolves: rhbz#1771027 CVE-2019-16707

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 1.7.0-1
- latest release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 24 2017 Caolán McNamara <caolanm@redhat.com> - 1.6.2-1
- latest release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Caolán McNamara <caolanm@redhat.com> - 1.5.4-1
- latest release

* Tue May 03 2016 Caolán McNamara <caolanm@redhat.com> - 1.4.1-1
- latest version

* Mon Apr 18 2016 Caolán McNamara <caolanm@redhat.com> - 1.4.0-1
- latest version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Caolán McNamara <caolanm@redhat.com> - 1.3.3-8
- Resolves: rhbz#1261421 crash on mashing hangul korean keyboard

* Tue Jul 07 2015 Caolán McNamara <caolanm@redhat.com> - 1.3.3-7
- Resolves: rhbz#1239570 FTBFS in rawhide with valgrind warnings

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.3.3-5
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Thu Oct 16 2014 maciek <maciek@corsair.lan> - 1.3.3-4
- Resolves: rhbz#915448, UTF-8 handling patch from
  http://debbugs.gnu.org/cgi/bugreport.cgi?bug=7781#31

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Caolán McNamara <caolanm@redhat.com> - 1.3.3-1
- Resolves: rhbz#1104042 update to latest version

* Tue Oct 15 2013 Caolán McNamara <caolanm@redhat.com> - 1.3.2-15
- Resolves: rhbz#1019158 esc space in man page

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.3.2-14
- Perl 5.18 rebuild

* Thu Jul 25 2013 Caolán McNamara <caolanm@redhat.com> - 1.3.2-13
- Resolves: rhbz#985052 layout problems with very long lines

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.3.2-12
- Perl 5.18 rebuild

* Thu Apr 04 2013 Caolán McNamara <caolanm@redhat.com> - 1.3.2-11
- Resolves: rhbz#925562 support aarch64

* Wed Mar 13 2013 Caolán McNamara <caolanm@redhat.com> - 1.3.2-10
- Resolves: rhbz#918938 crash in danish thesaurus/spell interaction

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 28 2012 Caolán McNamara <caolanm@redhat.com> - 1.3.2-8
- Related: rhbz#850709 en-US available standalone

* Wed Aug 01 2012 Caolán McNamara <caolanm@redhat.com> - 1.3.2-6
- Resolves: rhbz#573516 have hunspell require hunspell-en to ensure
  at least one dictionary exists

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Caolán McNamara <caolanm@redhat.com> - 1.3.2-4
- Resolves: rhbz#813478 x86_64 valgrind spews, see rhbz#813780

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Caolán McNamara <caolanm@redhat.com> - 1.3.2-2
- Resolves: rhbz#759647 temp file name collision

* Tue May 24 2011 Caolán McNamara <caolanm@redhat.com> - 1.3.2-1
- Resolves: rhbz#706686 latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Caolán McNamara <caolanm@redhat.com> - 1.2.15-1
- latest version

* Fri Jan 07 2011 Caolán McNamara <caolanm@redhat.com> - 1.2.14-1
- latest version

* Wed Jan 05 2011 Caolán McNamara <caolanm@redhat.com> - 1.2.13-1
- latest version
- drop integrated backport.warnings.patch
- drop integrated backport.rhbz650503.patch

* Mon Nov 08 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.12-3
- Resolves: rhbz#650503 Arabic spellchecking crash

* Fri Nov 05 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.12-2
- Resolves: rhbz#648740 thousands of trailing empty rules spew

* Thu Jul 15 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.12-1
- latest version
- drop integrated hunspell-1.2.11-valgrind.patch
- drop integrated hunspell-1.2.11-koreansupport.patch

* Fri Jul 09 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.11-4
- use -fprofile-generate and -fprofile-use

* Mon Jul 05 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.11-3
- add korean Hangul syllable support

* Tue Jun 22 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.11-2
- use valgrind in make check

* Thu May 06 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.11-1
- Resolves: rhbz#589326 wrong malloc

* Fri Apr 30 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.10-1
- latest version

* Thu Mar 04 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.9-2
- Resolves: ooo#107768 hunspell-1.2.9-stacksmash.patch

* Wed Mar 03 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.9-1
- latest version, drop all upstreamed patchs

* Mon Mar 01 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.8-17
- Resolves: rhbz#569449 hu man dir now exists in filesystem

* Mon Jan 18 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.8-16
- Resolves: rhbz#554876 fix suggestmgr crash

* Tue Jan 05 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.8-15
- Remove bad const warnings

* Mon Dec 21 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-14
- Preserve timestamps

* Tue Dec 08 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-13
- Resolves: rhbz#544372 survive having no HOME

* Thu Jul 30 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-12
- handle some other interesting edge-cases

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-10
- run tests in check

* Thu Jul 09 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-9
- Resolves: rhbz#510360 unowned dirs
- fix up rpmlint warnings

* Tue Jul 07 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-8
- Resolves: rhbz#509882 ignore an empty LANGUAGE variable

* Fri Jun 26 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-7
- Related: rhbz#498556 default to something sensible in "C" locale
  for language

* Wed Jun 24 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-6
- Resolves: rhbz#507829 fortify fixes

* Fri May 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.8-5
- Resolves: rhbz#498556 fix default language detection

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.8-3
- tweak summary

* Wed Nov 19 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.8-2
- Resolves: rhbz#471085 in ispell compatible mode (-a), ignore
  -m option which means something different to ispell

* Sun Nov 02 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.8-1
- latest version

* Sat Oct 18 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.7-5
- sort as per "C" locale

* Fri Oct 17 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.7-4
- make wordlist2hunspell remove blank lines

* Mon Sep 15 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.7-3
- Workaround rhbz#462184 uniq/sort problems with viramas

* Tue Sep 09 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.7-2
- add wordlist2hunspell

* Sat Aug 23 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.7-1
- latest version

* Tue Jul 29 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.6-1
- latest version

* Sun Jul 27 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.5-1
- latest version

* Tue Jul 22 2008 Kristian Høgsberg <krh@redhat.com> - 1.2.4.2-2
- Drop ABI breaking hunspell-1.2.2-xulrunner.pita.patch and fix the
  hunspell include in xulrunner.

* Wed Jun 18 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.4.2-1
- latest version

* Tue Jun 17 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.4-1
- latest version

* Fri May 16 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.2-3
- Resolves: rhbz#446821 fix crash

* Wed May 14 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.2-2
- give xulrunner what it needs so we can get on with it

* Fri Apr 18 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.2-1
- latest version
- drop integrated hunspell-1.2.1-1863239.badstructs.patch

* Wed Mar 05 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.1-6
- add ispellaff2myspell to devel

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.1-5
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.1-4
- add hunspell-1.2.1-1863239.badstructs.patch

* Fri Nov 09 2007 Caolán McNamara <caolanm@redhat.com> - 1.2.1-2
- pkg-config cockup

* Mon Nov 05 2007 Caolán McNamara <caolanm@redhat.com> - 1.2.1-1
- latest version

* Mon Oct 08 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.12.2-2
- lang fix for man pages from Ville Skyttä

* Wed Sep 05 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.12.2-1
- next version

* Tue Aug 28 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.11.2-1
- next version

* Fri Aug 24 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.10-1
- next version

* Thu Aug 02 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.9-2
- clarify license

* Wed Jul 25 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.9-1
- latest version

* Wed Jul 18 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.8.2-1
- latest version

* Tue Jul 17 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.8-1
- latest version

* Sat Jul 07 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.7-1
- latest version
- drop integrated hunspell-1.1.5.freem.patch

* Fri Jun 29 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.6-1
- latest version
- drop integrated hunspell-1.1.4-defaultdictfromlang.patch
- drop integrated hunspell-1.1.5-badheader.patch
- drop integrated hunspell-1.1.5.encoding.patch

* Fri Jun 29 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.5.3-5
- fix memory leak
  http://sourceforge.net/tracker/index.php?func=detail&aid=1745263&group_id=143754&atid=756395

* Wed Jun 06 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.5.3-4
- Resolves: rhbz#212984 discovered problem with missing wordchars

* Tue May 22 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.5.3-3
- Resolves: rhbz#240696 extend encoding patch to promote and add
  dictionary 8bit WORDCHARS to the ucs-2 word char list

* Mon May 21 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.5.3-2
- Resolves: rhbz#240696 add hunspell-1.1.5.encoding.patch

* Mon May 21 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.5.3-1
- patchlevel release

* Tue Mar 20 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.5-2
- some junk in delivered headers

* Tue Mar 20 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.5-1
- next version

* Fri Feb 09 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.4-6
- some spec cleanups

* Fri Jan 19 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.4-5
- .pc

* Thu Jan 11 2007 Caolán McNamara <caolanm@redhat.com> - 1.1.4-4
- fix out of range

* Fri Dec 15 2006 Caolán McNamara <caolanm@redhat.com> - 1.1.4-3
- hunspell#1616353 simple c api for hunspell

* Wed Nov 29 2006 Caolán McNamara <caolanm@redhat.com> - 1.1.4-2
- add hunspell-1.1.4-defaultdictfromlang.patch to take locale as default
  dictionary

* Wed Oct 25 2006 Caolán McNamara <caolanm@redhat.com> - 1.1.4-1
- initial version
