Name:       nas 
Summary:    The Network Audio System (NAS)
Version:    1.9.5
Release:    12%{?dist}
URL:        http://radscan.com/nas.html
# README:               MIT (main license)
# lib/audio/aiff.c          MIT (with Apple warranty declaration)
# server/dda/voxware/auvoxware.h:
#                           (MIT) and
#                           (something similar to MIT license by SCO)
# server/dda/sun/ausuni.c:  (MIT) and
#                           (something similar to MIT)
## Not in any binary package
# config/aclocal.m4:    FSFULLR
# config/config.guess:  GPLv2+ with exceptions, effectively same as main license
# config/config.sub:    GPL with exceptions, effectively same as main license
# config/configure:     FSFUL
# config/install-sh:    MIT
# config/ltmain.sh:     GPLv2+ with exceptions, effectively same as main license
## Unused
# contrib/nasbugs/Aproto.h: MIT
# contrib/nasbugs/audio.h:  MIT
# contrib/xemacs/nas.c:     MIT
License:    MIT
%define daemon nasd
Source0:    https://sourceforge.net/projects/nas/files/nas/nas-%{version}/nas-%{version}.tar.gz
Source1:    %{daemon}.service
Source2:    %{daemon}.sysconfig
# Move noarch data to /usr/share
Patch0:     nas-1.9.3-Move-AuErrorDB-to-SHAREDIR.patch
# Adapt to GCC 14, in upstream after 1.9.5,
# bug #2149230, <https://sourceforge.net/p/nas/bugs/10/>
Patch1:     nas-1.9.5-No-implicit-ints-and-function-declarations.patch
# Respect linker flags when linking shared libraries, in upstream after 1.9.5,
# <https://sourceforge.net/p/nas/bugs/11/>
Patch2:     nas-1.9.5-Pass-extra-linker-flags-to-shared-libraries.patch
# Adapt pointer types to GCC 14, bug #2261396, in upstream after 1.9.5,
# <https://sourceforge.net/p/nas/bugs/12/>
Patch3:     nas-1.9.5-Correct-pointer-types-for-GCC-14.patch
# Adapt to API changes in libXaw-1.0.16, bug #2276343, proposed to an
# upstream, <https://sourceforge.net/p/nas/bugs/14/>
Patch4:     nas-1.9.5-Adapt-to-libXaw-1.0.16.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
# Update config.sub to support aarch64, bug #926196
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       %{name}-libs = %{version}-%{release}


%package devel
Summary:    Development and doc files for the NAS 
Requires:   %{name}-libs = %{version}-%{release}

%package libs
Summary:    Run-time libraries for NAS


%description
In a nutshell, NAS is the audio equivalent of an X display server.  The
Network Audio System (NAS) was developed for playing, recording, and
manipulating audio data over a network.  Like the X Window System, it uses the
client/server model to separate applications from the specific drivers that
control audio input and output devices.

Key features of the Network Audio System include:
    • Device-independent audio over the network
    • Lots of audio file and data formats
    • Can store sounds in server for rapid replay
    • Extensive mixing, separating, and manipulation of audio data
    • Simultaneous use of audio devices by multiple applications
    • Use by a growing number of ISVs
    • Small size
    • Free!  No obnoxious licensing terms

%description libs
%{summary}.

%description devel
Development files and the documentation for Network Audio System.


%prep
%autosetup -p1

# Update config.sub to support aarch64, bug #926196
cp -p %{_datadir}/automake-*/config.{sub,guess} config
sed -i -e '/AC_FUNC_SNPRINTF/d' config/configure.ac
autoreconf -i -f config

%build
xmkmf
# See HISTORY file how to modify CDEBUGFLAGS
%make_build WORLDOPTS='-k CDEBUGFLAGS="%{optflags}" -k EXTRA_LDOPTIONS="%{__global_ldflags}"' World


%install
%make_install BINDIR=%{_bindir} INCROOT=%{_includedir} \
  LIBDIR=%{_libdir}/X11  SHLIBDIR=%{_libdir} USRLIBDIR=%{_libdir} \
  MANPATH=%{_mandir} INSTALLFLAGS='-p' EXTRA_LDOPTIONS='%{__global_ldflags}' \
  install.man

# Systemd integration
install -p -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{daemon}.service
install -p -m644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{daemon}

# Rename a config file
mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/nasd.conf{.eg,}

# Remove the static libraries
rm -fv $RPM_BUILD_ROOT%{_libdir}/lib*.a


%post
%systemd_post %{daemon}.service

%preun
%systemd_preun %{daemon}.service

%postun
%systemd_postun_with_restart %{daemon}.service


%files
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/nasd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{daemon}
%{_unitdir}/%{daemon}.service
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files libs
%doc FAQ HISTORY README TODO
%{_libdir}/libaudio.so.*
%{_datadir}/X11/AuErrorDB

%files devel
%doc doc/actions doc/protocol.txt doc/*.ps
%{_includedir}/audio/
%{_libdir}/libaudio.so
%{_mandir}/man3/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Petr Pisar <ppisar@redhat.com> - 1.9.5-10
- Adapt to API changes in libXaw-1.0.16 (bug #2276343)

* Fri Feb 02 2024 Petr Pisar <ppisar@redhat.com> - 1.9.5-9
- Adapt pointer types to GCC 14 (bug #2261396)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Petr Pisar <ppisar@redhat.com> - 1.9.5-5
- Respect linker flags when linking shared libraries (upstream bug #11)

* Thu Jan 19 2023 Petr Pisar <ppisar@redhat.com> - 1.9.5-4
- Adapt to GCC 14 (bug #2149230)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 31 2022 Petr Pisar <ppisar@redhat.com> - 1.9.5-1
- 1.9.5 bump

* Mon Jan 24 2022 Petr Pisar <ppisar@redhat.com> - 1.9.4-28
- Fix compiler warnings
- Fix a buffer overflow in auphone

* Mon Jan 24 2022 Petr Pisar <ppisar@redhat.com> - 1.9.4-27
- Unset LDFLAGS for config/configure (upstream bug #9)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.4-24
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Adam Jackson <ajax@redhat.com> - 1.9.4-22
- Remove unused BuildRequires: libXp-devel

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.9.4-20
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro
- Modernize systemd and ldconfig packaging

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Petr Pisar <ppisar@redhat.com> - 1.9.4-18
- Fix building with GCC 10 (upstream bug #7)
- Fix a file handle leak (upstream bug #6)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Petr Pisar <ppisar@redhat.com> - 1.9.4-14
- Remove ldconfig postscriptlets where unnecessary

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.9.4-13
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Petr Pisar <ppisar@redhat.com> - 1.9.4-11
- Modernize systemd units packaging

* Mon Jul 31 2017 Petr Pisar <ppisar@redhat.com> - 1.9.4-10
- Respect distribution linker flags

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Petr Pisar <ppisar@redhat.com> - 1.9.4-5
- Put auscope client back

* Fri Feb 20 2015 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-4
- omit broken/perl-based auscope client app

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 08 2013 Petr Pisar <ppisar@redhat.com> - 1.9.4-1
- 1.9.4 bump
- Package license corrected to MIT

* Mon Sep 16 2013 Petr Pisar <ppisar@redhat.com> - 1.9.3-9
- Fix CVE-2013-4258 (formatting string for syslog call) (bug #1006753)
- Fix CVE-2013-4256 (parsing display number, heap overflow when processing
  AUDIOHOST variable) (bug #1006753)
- Fix race when opening a TCP device (bug #1006753)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.9.3-7
- Perl 5.18 rebuild

* Wed Mar 27 2013 Petr Pisar <ppisar@redhat.com> - 1.9.3-6
- Update config.sub to support aarch64 (bug #926196)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Petr Pisar <ppisar@redhat.com> - 1.9.3-4
- Modernize systemd scriptlets

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 02 2011 Petr Pisar <ppisar@redhat.com> - 1.9.3-1
- 1.9.3 bump
- Remove useless spec code
- Migrate nasd service from sysvinit to systemd

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 09 2010 Petr Pisar <ppisar@redhat.com> - 1.9.2-1
- 1.9.2 bump, update URL, Source0
- Remove spec code specific for Fedora < 12 and EPEL < 4 as they are
  unsupported now
- Apply nas-1.9.2-asneeded.patch to get libXau linked explicitly (bug #565181)
- Move AuErrorDB non-executable to share directory, distribute with libraries
- Unify spec file indentation
- Add postun action

* Sun Mar 14 2010 Frank Büttner <frank-buettner@gmx.net> - 1.9.1-7
- fix #565181

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 07 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-4
- -libs subpkg (f9+, #438547)
- %%install: INSTALLFLAGS='-p' (preserve timestamps)
- fixup %%changelog whitespace

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9.1-3
- Autorebuild for GCC 4.3

* Sun Nov 11 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9.1-2
- fix spec file

* Sun Nov 11 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9.1-1
- update to 1.9.1
- remove unneeded patches

* Fri Nov 02 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9a-3
- add better patch for #247468 

* Fri Nov 02 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9a-2
- add patch to fix #247468

* Sun Oct 28 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9a-1
- update to 1.9a to fix #245712

* Sat Aug 18 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9-4
- fix for bug #245712

* Sat Aug 11  2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9-3
- fix for bug #250453

* Fri May 04 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9-2%{?dist}
- rebuild for the new ppc64 arch

* Sun Apr 08 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.9-1%{?dist}
- update to 1.9
- remove old patch file

* Mon Mar 26 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.8b-1%{?dist}
- update to 1.8b

* Thu Mar 22 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.8a-2%{?dist}
- use the SVN version of 1.8a

* Wed Mar 21 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.8a-1%{?dist}
- fix bug 233353 

* Fri Feb 09 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.8-13%{?dist}
- use the corrected patch

* Thu Feb 08 2007 Frank Büttner  <frank-buettner@gmx.net> - 1.8-11%{?dist}
- fix bug 227759

* Tue Sep 19 2006 Rex Dieter <rexdieter[AT]users.sf.net> - 1.8-10
- don't rely-on/use potentially broken %%_libdir/X11 symlink (#207180)

* Mon Sep 11 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-9%{?dist}
- second rebuild for FC6

* Mon Jul 24 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-8%{?dist}
- fix ugly output when starting the daemon

* Fri Jul 21 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-7%{?dist}
- disable build for EMT64 on FC4

* Thu Jul 13 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-6%{?dist}
- fix build on EMT64 

* Wed Jul 12 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-5%{?dist}
- fix include dir

* Fri Jul 7 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-4%{?dist}
- add Requires(preun): chkconfig /sbin/service
- add Requires(post):  chkconfig
- add remarks for FC4

* Fri Jul 7 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-3%{?dist}
- move man3 to devel
- rename nasd.conf.eg to .conf
- add build depend for libXext-devel libXt-devel
- change license to Public Domain
- add path to make intall
- add rc.d/sysconfig  files 

* Fri Jul 7 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-2%{?dist}
- move libaudio.so.2 to main package
- switch package name from NAS to nas
- fix depend for devel package
- fix version
- add nas subdir in etc to main package
- set license to Distributable
- add readme file

* Fri Jul 7 2006 Frank Büttner  <frank-buettner@gmx.net> - 1.8-1%{?dist}
- start
