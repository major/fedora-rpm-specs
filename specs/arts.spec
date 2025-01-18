%define multilib_arches %{ix86} x86_64 ppc ppc64 s390 s390x sparcv9 sparc64
# This package ships .la files
%global __brp_remove_la_files %nil
# Disable LTO because it breaks ALSA versioned symbol use, crashing (#1910437)
%global _lto_cflags %nil

Name:    arts
Summary: aRts (analog realtime synthesizer) - the KDE sound system 
Epoch:   8
Version: 1.5.10
Release: 64%{?dist}

License: LGPL-2.0-or-later
Url: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/3.5.10/src/%{name}-%{version}.tar.bz2
Source1: gslconfig-wrapper.h

Patch1: arts-1.1.4-debug.patch
Patch2: arts-1.3.92-glib2.patch
Patch5: arts-1.3.1-alsa.patch
Patch6: arts-1.5.8-glibc.patch
Patch8: arts-1.5.2-multilib.patch
# don't pop up a dialog on CPU overload (#361891)
Patch9: arts-1.5.10-cpu-overload-quiet.patch
# don't call snd_pcm_close(NULL), triggers assertion failure in ALSA (#558570)
Patch10: arts-1.5.10-assertion-failure.patch
# fix detection of ALSA 1.1 (and future 1.x) in configure.in.in
Patch11: arts-1.5.10-alsa11.patch
# kde#93359
Patch50: arts-1.5.4-dlopenext.patch
Patch51: kde-3.5-libtool-shlibext.patch
Patch52: arts-1.5.8-glibc-libio.patch
Patch53: arts-autoconf-2.7x.patch
Patch54: arts-c99.patch
Patch55: kde3-autoconf-2.72.patch

# upstream patches

# security patches
# CVE-2009-3736 libtool: libltdl may load and execute code from a library in the current directory 
Patch200: libltdl-CVE-2009-3736.patch
# CVE-2015-7543 arts,kdelibs3: Use of mktemp(3) allows attacker to hijack the IPC
# backport upstream fix (the lnusertemp.c change) from kdelibs 4:
# http://commits.kde.org/kdelibs/cc5515ed7ce8884c9b18169158ba29ab2f7a3db7
# upstream fix by Joseph Wenninger, rediffed for aRts by Kevin Kofler
Patch201: arts-1.5.10-CVE-2015-7543.patch

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
Patch304: args-1.5.8-configure.patch

# Don't use __FILE__ like a string literal
Patch305: file-literal.patch

# used in artsdsp
Requires: which

BuildRequires:  gcc-c++
BuildRequires: qt3-devel >= 3.3.8
BuildRequires: alsa-lib-devel
BuildRequires: audiofile-devel
BuildRequires: automake libtool
BuildRequires: findutils sed
BuildRequires: glib2-devel
BuildRequires: libvorbis-devel
BuildRequires: pkgconfig
BuildRequires: chrpath
BuildRequires: libmad-devel
BuildRequires: make

%description
arts (analog real-time synthesizer) is the sound system of KDE 3.

The principle of arts is to create/process sound using small modules which do
certain tasks. These may be create a waveform (oscillators), play samples,
filter data, add signals, perform effects like delay/flanger/chorus, or
output the data to the soundcard.

By connecting all those small modules together, you can perform complex
tasks like simulating a mixer, generating an instrument or things like
playing a wave file with some effects.

%package devel
Summary: Development files for the aRts sound server
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: qt3-devel
Requires: pkgconfig
Requires: glib2-devel
%description devel
Install %{name}-devel if you intend to write applications using aRts.


%prep
%setup -q
%patch -P1 -p1 -b .debug
%patch -P2 -p1 -b .glib
%patch -P5 -p1 -b .alsa
%patch -P6 -p1 -b .glibc
%patch -P8 -p1 -b .multilib
%patch -P9 -p1 -b .cpu-overload-quiet
%patch -P10 -p1 -b .assertion-failure
%patch -P11 -p1 -b .alsa11

%patch -P50 -p1 -b .dlopenext
%patch -P51 -p1 -b .libtool-shlibext
%patch -P52 -p1 -b .glibc-libio
%patch -P53 -p1 -b .autoconf2.7x
%patch -P54 -p1 -b .c99
%patch -P55 -p1 -b .autoconf-2.72

%patch -P200 -p1 -b .CVE-2009-3736
%patch -P201 -p1 -b .CVE-2015-7543

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .configure
%patch -P305 -p1 -b .file-literal
make -f admin/Makefile.common cvs

%build
unset QTDIR && . /etc/profile.d/qt.sh

export CXXFLAGS="%{optflags} -Wno-error=narrowing"

%configure \
  --includedir=%{_includedir}/kde \
  --disable-rpath \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking \
  --enable-new-ldflags \
  --with-alsa \
  --enable-final

# kill rpath harder, inspired by https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Removing_Rpath
# other more standard variants didnt work or caused other problems
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' libtool

## hack for artsdsp (see http://bugzilla.redhat.com/329671)
#make %{?_smp_mflags} -k || \
#  sed -i -e "s|-Wp,-D_FORTIFY_SOURCE=2||" artsc/Makefile && \
%make_build


%install
export PATH=`pwd`:$PATH

%make_install

%ifarch %{multilib_arches}
# Ugly hack to allow parallel installation of 32-bit and 64-bit arts-devel
  mv  %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig.h \
      %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig-%{_arch}.h
  install -p -m644 %{SOURCE1}  %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig.h
%endif

## remove references to optional external libraries in .la files (#178733)
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs \
 sed -i \
 -e "s|-lmad||g" \
 -e "s|%{_libdir}/libmad.la||g" \
 -e "s|-lvorbisfile||g" \
 -e "s|-lvorbisenc||g" \
 -e "s|-lvorbis||g" \
 -e "s|-logg||g" \
 -e "s|-lasound||g" \
 -e "s|-laudiofile||g" \
 -e "s|-lesd||g" \
 -e "s|%{_libdir}/libesd.la||g" \
 -e "s|-lgmodule-2.0||g" \
 -e "s|-lgthread-2.0||g" \
 -e "s|-lglib-2.0||g" \
 -e "s|-laudio ||g" \
 -e "s|-lpng -lz ||g" \
 -e "s|%{_libdir}/libartsc.la||g" \
 -e "s@-lboost_filesystem@@g" \
 -e "s@-lboost_regex@@g" \
 -e "s@-ljack@@g"


%check
## Verify rpath, or lack thereof
test -z "$(chrpath --list %{buildroot}%{_bindir}/artsd 2>/dev/null | grep RPATH=)"


%ldconfig_scriptlets

%files
%license COPYING.LIB
%dir %{_libdir}/mcop
%dir %{_libdir}/mcop/Arts
%{_libdir}/mcop/Arts/*
%{_libdir}/mcop/*.mcopclass
%{_libdir}/mcop/*.mcoptype
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la
%{_bindir}/artscat
%{_bindir}/artsd
%{_bindir}/artsdsp
%{_bindir}/artsplay
%{_bindir}/artsrec
%{_bindir}/artsshell
%{_bindir}/artswrapper

%files devel
%{_bindir}/mcopidl
%dir %{_includedir}/kde
%{_includedir}/kde/arts/
%{_includedir}/kde/artsc/
%{_bindir}/artsc-config
%{_libdir}/pkgconfig/artsc.pc
%{_libdir}/lib*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Than Ngo <than@redhat.com> - 8:1.5.10-63
- Fix rhbz#2300566, FTBFS

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Florian Weimer <fweimer@redhat.com> - 8:1.5.10-59
- Update C99 patch

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Than Ngo <than@redhat.com> - 1.5.10-57
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Florian Weimer <fweimer@redhat.com> - 8:1.5.10-55
- Port to C99 (#2147552)

* Tue Nov 08 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8:1.5.10-54
- Disable LTO because it breaks ALSA versioned symbol use, crashing (#1910437)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 8:1.5.10-52
- Opt out of .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Than Ngo <than@redhat.com> - 8:1.5.10-50
- Fixed bz#1999495, FTBFS against autoconf-2.7x

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Jeff Law <law@redhat.com> - 8:1.5.10-45
- Fix configure tests compromised by LTO

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8:1.5.10-42
- fix aarch64 FTBFS due to libtool not liking the file output on *.so files

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 8:1.5.10-40
- .spec cleanup
- drop Group:, %%defattr
- use %%make_build %%make_install %%license %%ldconfig_scriptlets

* Thu Jun 07 2018 Than Ngo <than@redhat.com> - 8:1.5.10-39
- fixed bz#1529207 - enable MP3 support

* Thu Jun 07 2018 Than Ngo <than@redhat.com> - 8:1.5.10-38
- fixed bz#1582764, FTBFS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 08 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8:1.5.10-33
- Fix detection of ALSA 1.1 (and future 1.x) in configure.in.in

* Sun Feb 14 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8:1.5.10-32
- Add -Wno-error=narrowing to the CXXFLAGS to fix FTBFS (#1307330)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8:1.5.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8:1.5.10-30
- Backport CVE-2015-7543 fix (Joseph Wenninger) from kdelibs 4 (#1289237)
- Drop arts-1.5.0-check_tmp_dir.patch, #169631 fixed differently upstream, and
  the patch interferes with the security fix for CVE-2015-7543

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 8:1.5.10-28
- Rebuilt for GCC 5 C++11 ABI change

* Fri Apr 03 2015 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.10-27
- rebuild (gcc5)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.10-25
- kill rpaths harder

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.5.10-22
- use automake --force-missing to get aarch64 support (#925029/#925627)
- also use automake --copy (the default is symlinking)

* Sat Mar 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.5.10-21
- unify KDE 3 autotools fixes between packages

* Thu Mar 07 2013 Than Ngo <than@redhat.com> - 1.5.10-20
- fix FTBFS in rawhide

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5.10-18
- rebuild (audiofile)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Dan Horák <dan[at]danny.cz> - 8:1.5.10-16
- fix build with automake 1.11.5

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-15
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 24 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8:1.5.10-12
- don't call snd_pcm_close(NULL), triggers assertion failure in ALSA (#558570)

* Wed Dec 16 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8:1.5.10-11
- don't pop up a dialog on CPU overload (#361891)

* Thu Dec 10 2009 Stepan Kasal <skasal@redhat.com> - 8:1.5.10-10
- patch autoconfigury to build with autoconf >= 2.64

* Sun Dec 06 2009 Than Ngo <than@redhat.com> - 8:1.5.10-9
- fix url
- fix security issues in libltdl (CVE-2009-3736)

* Wed Sep 02 2009 Than Ngo <than@redhat.com> - 8:1.5.10-8
- drop support fedora < 10

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 8:1.5.10-6
- FTBFS arts-1.5.10-5.fc11 (#511653)
- -devel: Requires: %%{name}%%_isa ...

* Mon Mar 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 8:1.5.10-5
- s/i386/%%ix86/

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8:1.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.10-3
- rebuild for pkgconfig deps

* Mon Sep 29 2008 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.10-2
- multilib (sparc) fixes

* Tue Sep 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 8:1.5.10-1.1
- fix qt-devel dependency on F8

* Tue Aug 26 2008 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.10-1
- arts-1.5.10

* Thu May 15 2008 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.9-3
- arts support for mixed multilib usage (#444484)
- f10+: drop optional esd, jack, nas support

* Wed Mar 12 2008 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.9-2
- s/qt-devel/qt3-devel/

* Tue Feb 14 2008 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.9-1
- kde-3.5.9

* Wed Feb 13 2008 Rex Dieter <rdieter@fedoraproject.org> 8:1.5.8-5
- gcc43 patch 

* Wed Oct 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.8-4
- remove arts/open workaround (#329671)

* Mon Oct 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.8-3
- -devel: +Requires: glib2-devel (#331841)

* Fri Oct 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.8-2
- hack to get artsdsp buildable (#329671)

* Fri Oct 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.8-1
- 1.5.8 (kde-3.5.8)

* Mon Oct 01 2007 Than Ngo <than@redhat.com> - 8:1.5.7-7
- rh#312621, requires which

* Fri Aug 02 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.7-6
- update glibc patch ( open -> (open) )

* Fri Aug 02 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.7-5
- omit extention_loader patch (for now anyway), removes boost dep
- License: LGPLv2+

* Wed Jun 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.7-4
- own %%_includedir/kde (#245909)

* Wed Jun 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.7-3
- cleanup gslconfig.h/multilib bits, -ia64, +sparc64/sparc

* Mon Jun 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 8:1.5.7-2
- (re)add (experimental) libtool patches

* Mon Jun 04 2007 Than Ngo <than@redhat.com> - 8:1.5.7-1.fc7
- 1.5.7

* Tue May 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:1.5.6-4
- respin with higher release (for EVR upgrade paths)

* Mon May 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:1.5.6-3
- BR: nas-devel jack-audio-connection-kit-devel
- omit extraneous .la file references (#178733)
- -devel: Requires: qt-devel pkgconfig

* Mon Feb 26 2007 Than Ngo <than@redhat.com> - 6:1.5.6-2.fc7
- cleanup specfile

* Wed Jan 24 2007 Than Ngo <than@redhat.com> - 6:1.5.6-1.fc7
- 1.5.6

* Tue Nov 14 2006 Than Ngo <than@redhat.com> - 6:1.5.5-1.fc7
- rebuild

* Wed Oct 25 2006 Than Ngo <than@redhat.com> 8:1.5.5-0.1.fc6
- 1.5.5

* Tue Aug 08 2006 Than Ngo <than@redhat.com> 8:1.5.4-1
- rebuilt

* Mon Jul 24 2006 Than Ngo <than@redhat.com> 8:1.5.4-0.pre1
- prerelease of 3.5.4 (from the first-cut tag)

* Tue Jul 18 2006 Than Ngo <than@redhat.com> 8:1.5.3-2
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 8:1.5.3-1.1
- rebuild

* Wed May 31 2006 Than Ngo <than@redhat.com> 8:1.5.3-1
- update to 1.5.3

* Mon May 15 2006 Than Ngo <than@redhat.com> 8:1.5.2-2
- fix multilib issue

* Tue Mar 21 2006 Than Ngo <than@redhat.com> 8:1.5.2-1
- update to 1.5.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 8:1.5.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 8:1.5.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Feb 01 2006 Than Ngo <than@redhat.com> 8:1.5.1-1
- 1.5.1

* Wed Jan 18 2006 Than Ngo <than@redhat.com> 8:1.5.0-2
- rebuilt with --enable-new-ldflags

* Mon Dec 19 2005 Than Ngo <than@redhat.com> 8:1.5.0-1
- apply patch to fix #169631 

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 24 2005 Than Ngo <than@redhat.com> 8:1.5.0-0.1.rc2
- update to 3.5.0 rc2

* Mon Nov 14 2005 Than Ngo <than@redhat.com> 8:1.5.0-0.1.rc1
- update to 3.5.0 rc1
- another patch to fix lnusertemp problem

* Fri Nov 04 2005 Than Ngo <than@redhat.com> 8:1.4.92-2
- fix lnusertemp problem #169631

* Mon Oct 24 2005 Than Ngo <than@redhat.com> 8:1.4.92-1
- update to KDE 3.5 beta2

* Tue Sep 27 2005 Than Ngo <than@redhat.com> 8:1.4.91-1
- update to KDE 3.5 beta1
- drop multilib and pie patches which are included in new upstream

* Mon Aug 01 2005 Than Ngo <than@redhat.com> 8:1.4.2-1
- update to 1.4.2

* Tue Jun 21 2005 Than Ngo <than@redhat.com> 8:1.4.1-2 
- rebuilt

* Mon Jun 06 2005 Than Ngo <than@redhat.com> 8:1.4.1-1
- 1.4.1

* Thu Mar 17 2005 Than Ngo <than@redhat.com> 8:1.4.0-1
- KDE 3.4.0 release

* Mon Mar 14 2005 Than Ngo <than@redhat.com> 8:1.4.0-0.rc1.5
- fix build problem

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 8:1.4.0-0.rc1.4
- rebuilt against gcc-4.0.0-0.31

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 8:1.4.0-0.rc1.3
- rebuilt against gcc 4

* Fri Feb 25 2005 Than Ngo <than@redhat.com> 8:1.4.0-0.rc1.2
- KDE 3.4.0 rc1

* Mon Feb 14 2005 Than Ngo <than@redhat.com> 8:1.3.92-0.1
- 3.4beta2

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 8:1.3.2-0.1
- update to KDE 3.3.2

* Fri Nov 19 2004 Than Ngo <than@redhat.com> 8:1.3.1-4
- alsa as default

* Fri Oct 29 2004 Than Ngo <than@redhat.com> 8:1.3.1-3
- rebuilt in fc4 tree

* Sat Oct 16 2004 Than Ngo <than@redhat.com> 8:1.3.1-2
- rebuilt for rhel

* Wed Oct 06 2004 Than Ngo <than@redhat.com> 1.3.1-1
- update to KDE 3.3.1

* Wed Sep 15 2004 Than Ngo <than@redhat.com> 1.3.0-4 
- fix multilib problem #132576

* Fri Sep 03 2004 Colin Walters <walters@redhat.com> 1.3.0-3
- Fix trivial conflict in glib patch and reapply; this
  removes dependency on glib2.0 and therefore prevents
  symbol clashes with applications loading arts still
  using glib 1.2, like XMMS.

* Mon Aug 23 2004 Than Ngo <than@redhat.com> 1.3.0-2
- add missing epoch tag

* Thu Aug 19 2004 Than Ngo <than@redhat.com> 1.3.0-1
- update to 1.3.0 release

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 1.3.0-0.1.rc2
- update 3.3 rc2

* Sun Aug 08 2004 Than Ngo <than@redhat.com> 1.3.0-0.1.rc1
- update to 3.3 rc1 

* Tue Aug 03 2004 Than Ngo <than@redhat.com> 1.2.92-1.1
- update to 3.3 beta2

* Wed Jun 30 2004 Than Ngo <than@redhat.com> 1.2.91-1
- update to 3.3 beta1

* Mon Jun 28 2004 Than Ngo <than@redhat.com> 1.2.3-3
- add buildrequires on esound-devel (bug #125293)

* Thu Jun 17 2004 Than Ngo <than@redhat.com> 1.2.3-2
- rebuild

* Mon May 31 2004 Than Ngo <than@redhat.com> 1.2.3-1
- update to 1.2.3

* Thu May 13 2004 Than Ngo <than@redhat.com> 1.2.2-3
- add patch to enable PIE build of artsd

* Mon Apr 19 2004 Than Ngo <than@redhat.com> 1.2.2-2
- #120265 #119642 -devel req alsa-lib-devel esound-devel glib2-devel

* Mon Apr 12 2004 Than Ngo <than@redhat.com> 1.2.2-1
- 1.2.2 release

* Fri Apr 02 2004 Than Ngo <than@redhat.com> 1.2.1-2
- add several fixes from stable branch

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Than Ngo <than@redhat.com> 1.2.1-1
- update to 1.2.1

* Mon Feb 23 2004 Than Ngo <than@redhat.com> 8:1.2.0-1.5
- add patch file from CVS, fix mcop warning
- fix glib2 issue

* Tue Feb 17 2004 Than Ngo <than@redhat.com> 1.2.0-1.4 
- add missing build requirements
- add patch file from Bero #115507

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 05 2004 Than Ngo <than@redhat.com> 1.2.0-0.3 
- rebuilt against qt 3.3.0

* Tue Feb 03 2004 Than Ngo <than@redhat.com> 8:1.2.0-0.1
- 3.2.0 release

* Mon Jan 19 2004 Than Ngo <than@redhat.com> 8:1.1.95-0.1
- KDE 3.2RC1

* Fri Dec 12 2003 Than Ngo <than@redhat.com> 8:1.1.94-0.2
- rebuild against alsa-lib 1.0.0

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 8:1.1.94-0.1
- KDE 3.2 beta2

* Wed Nov 26 2003 Than Ngo <than@redhat.com> 8:1.1.93-0.4
- disable rpath

* Wed Nov 26 2003 Than Ngo <than@redhat.com> 8:1.1.93-0.3
- rebuild to fix dependant libraries check on x86_64

* Tue Nov 25 2003 Than Ngo <than@redhat.com> 8:1.1.93-0.2
- enable support alsa

* Fri Oct 31 2003 Than Ngo <than@redhat.com> 8:1.1.93-0.1
- KDE 3.2 beta1
- remove some unneeded patch, which are now in new upstream

* Tue Oct 14 2003 Than Ngo <than@redhat.com> 8:1.2-0.14_10_2003.1
- arts-1.2-14_10_2003

* Fri Oct 10 2003 Than Ngo <than@redhat.com> 8:1.1.4-2.1
- rebuilt against qt 3.2.1

* Mon Sep 29 2003 Than Ngo <than@redhat.com> 8:1.1.4-2
- arts_debug issue (bug #104278)

* Mon Sep 29 2003 Than Ngo <than@redhat.com> 8:1.1.4-1
- 3.1.4

* Thu Aug 28 2003 Than Ngo <than@redhat.com> 8:1.1.3-3
- rebuild

* Thu Jul 31 2003 Than Ngo <than@redhat.com> 8:1.1.3-2
- add workaround for gcc bug on ia64

* Tue Jul 29 2003 Than Ngo <than@redhat.com> 8:1.1.3-1
- add Prereq: /sbin/ldconfig

* Wed Jul 16 2003 Than Ngo <than@redhat.com> 8:1.1.3-0.9x.1
- 3.1.3

* Wed Apr  2 2003 Than Ngo <than@redhat.com> 1.1.1-0.9x.1
- 3.1.1 for RHL 9

* Wed Mar  5 2003 Than Ngo <than@redhat.com> 1.1-8
- move la files in arts package (bug #83607)
- add better patch to get rid of gcc path from la file

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Thu Feb 20 2003 Than Ngo <than@redhat.com> 1.1-6
- rebuid against gcc 3.2.2 to fix dependency in la file

* Thu Feb 13 2003 Thomas Woerner <twoerner@redhat.com> 1.1-5
- fixed artsbuilder crash (#82750)

* Wed Jan 29 2003 Than Ngo <than@redhat.com> 1.1-4
- 3.1 release

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Than Ngo <than@redhat.com> 1.1-3
- update to rc7
- change version, increase Epoch

* Tue Dec  3 2002 Than Ngo <than@redhat.com> 1.1.0-2
- use %%configure

* Fri Nov 22 2002 Than Ngo <than@redhat.com> 1.1.0-1
- update to 1.1.0

* Sat Nov  9 2002 Than Ngo <than@redhat.com> 1.0.5-1
- update 1.0.5

* Fri Nov  8 2002 Than Ngo <than@redhat.com> 1.0.4-2.1
- fix build problem on x86_64

* Fri Nov  8 2002 Than Ngo <than@redhat.com> 1.0.4-2
- fix build problem

* Mon Oct 14 2002 Than Ngo <than@redhat.com> 1.0.4-1
- 1.0.4
- cleanup specfile

* Mon Aug 12 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.3-1
- 1.0.3

* Sat Aug 10 2002 Elliot Lee <sopwith@redhat.com>
- rebuilt with gcc-3.2 (we hope)

* Wed Aug  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.2-4
- Update to current KDE_3_0_BRANCH, should be pretty much the same
  as 1.0.3

* Mon Jul 22 2002 Tim Powers <timp@redhat.com> 1.0.2-3
- rebuild using gcc-3.2-0.1

* Mon Jul 22 2002 Than Ngo <than@redhat.com> 1.0.2-2
- Added some major bugfixes from 1.0.3

* Tue Jul  2 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.2-1
- 1.0.2

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 06 2002 Than Ngo <than@redhat.com> 1.0.1-5
- rebuild

* Wed May 29 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.1-4
- Source qt.sh

* Tue May 28 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.1-3
- Increase release number by 2 to work around build system breakage

* Fri May  9 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.1-1
- 1.0.1

* Wed May  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.0-6
- Update to current KDE_3_0_BRANCH

* Thu May 02 2002 Than Ngo <than@redhat.com> 1.0.0-5
- rebuild in against gcc-3.1-0.26/qt-3.0.3-12

* Wed Apr 17 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.0-4
- Fix dangling symlink

* Mon Apr 15 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.0-3
- Change sonames to something indicating the compiler version if a compiler
  < gcc 3.1 is used
- Add compat symlinks for binary compatibility with other distributions

* Mon Apr  8 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.0-2
- Rebuild to get alpha binaries

* Wed Mar 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.0-1
- 1.0.0 final

* Tue Mar 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.9.9-0.cvs20020319.1
- aRts no longer uses the KDE version number; adapt spec file

* Wed Mar 13 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020313.1
- Build with autoconf 2.53, automake 1.5

* Thu Feb 14 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020114.1
- initial package
