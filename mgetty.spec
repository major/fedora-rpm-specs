%define SENDFAX_UID 78

# PIE is broken on s390 (#868839, #872148)
%ifnarch s390 s390x
%global _hardened_build 1
%endif

Summary: A getty replacement for use with data and fax modems
Name: mgetty
Version: 1.2.1
Release: 16%{?dist}
Source: ftp://mgetty.greenie.net/pub/mgetty/source/1.2/mgetty-%{version}.tar.gz
Source1: ftp://mgetty.greenie.net/pub/mgetty/source/1.2/mgetty-%{version}.tar.gz.asc
Source2: logrotate.mgetty
Source3: logrotate.sendfax
Source4: logrotate.vgetty
Source5: logrotate.vm
Source6: vgetty@.service
Source7: mgetty@.service

Patch0: mgetty-1.2.1-config.patch
Patch1: mgetty-1.2.1-policy.patch
Patch2: mgetty-1.2.1-system-gsm.patch
Patch4: mgetty-1.1.25-voiceconfig.patch
Patch5: mgetty-1.2.1-issue.patch
Patch6: mgetty-1.1.31-issue-doc.patch
Patch7: mgetty-1.1.29-helper.patch
Patch8: mgetty-1.2.1-mktemp.patch
Patch9: mgetty-1.2.1-unioninit.patch
Patch11: mgetty-1.2.1-helper2.patch
Patch12: mgetty-1.2.1-no-acroread.patch
Patch14: mgetty-1.2.1-sendmail_path.patch
Patch15: mgetty-1.2.1-lfs.patch
Patch16: mgetty-1.2.1-162174_tcflush.patch
Patch18: mgetty-1.1.33-bug_63843.patch
Patch19: mgetty-1.1.33-167830_tty_access.patch
Patch20: mgetty-1.2.1-167830.patch
Patch21: mgetty-1.2.1-turn.patch
Patch22: mgetty-1.2.1-time_range.patch
# man pages corrections
Patch23: mgetty-1.2.1-handle_spaces.patch
# updates info about starting vgetty tgrough systemd
Patch24: mgetty-1.1.36-man.patch
Patch25: mgetty-1.1.36-sd.patch
# patch updates makefiles, it removes hardcoded -s parameter of /usr/bin/install
# thus .debug files for all binaries will be generated properly
Patch26: mgetty-1.1.36-makefiles.patch
Patch27: mgetty-1.2.1-lockdev.patch
Patch28: mgetty-1.2.1-hardening.patch
Patch29: mgetty-sys_nerr-removed.patch
Patch30: mgetty-manpage-typos.patch

License: GPLv2+
BuildRequires: libX11-devel, libXext-devel, perl-generators, texinfo-tex, texlive-dvips, lockdev-devel, systemd, gsm-devel
# gcc is no longer in buildroot by default
BuildRequires: gcc
# make is no longer in buildroot by default
BuildRequires: make
# needed for rpm macros in scriptlets
BuildRequires: systemd-rpm-macros

Requires: coreutils, /usr/sbin/sendmail, uucp
Requires(post): systemd
Requires(postun): systemd
URL: http://mgetty.greenie.net/

%package sendfax
Summary: Provides support for sending faxes over a modem
Requires: mgetty = %{version}
Requires: coreutils
Requires: netpbm-progs
Requires(pre): /usr/sbin/useradd
Conflicts: hylafax+

%package voice
Summary: A program for using your modem and mgetty as an answering machine
Requires: mgetty = %{version}
Requires(post): systemd
Requires(postun): systemd

%package viewfax
Summary: An X Window System fax viewer

%description
The mgetty package contains a "smart" getty which allows logins over a
serial line (i.e., through a modem). If you're using a Class 2 or 2.0
modem, mgetty can receive faxes. If you also need to send faxes,
you'll need to install the sendfax program.

If you'll be dialing in to your system using a modem, you should
install the mgetty package. If you'd like to send faxes using mgetty
and your modem, you'll need to install the mgetty-sendfax program. If
you need a viewer for faxes, you'll also need to install the
mgetty-viewfax package.

%description sendfax
Sendfax is a standalone backend program for sending fax files. The
mgetty program (a getty replacement for handling logins over a serial
line) plus sendfax will allow you to send faxes through a Class 2
modem.

If you'd like to send faxes over a Class 2 modem, you'll need to
install the mgetty-sendfax and the mgetty packages.

%description voice
The mgetty-voice package contains the vgetty system, which enables
mgetty and your modem to support voice capabilities. In simple terms,
vgetty lets your modem act as an answering machine. How well the
system will work depends upon your modem, which may or may not be able
to handle this kind of implementation.

Install mgetty-voice along with mgetty if you'd like to try having
your modem act as an answering machine.

%description viewfax
Viewfax displays the fax files received using mgetty in an X11 window.
Viewfax is capable of zooming in and out on the displayed fax.

%prep
%setup -q
mv policy.h-dist policy.h
%patch0 -p1 -b .config
%patch1 -p1 -b .policy
%patch2 -p1 -b .system-gsm
rm -r voice/libmgsm
%patch4 -p1 -b .voiceconfig
%patch5 -p1 -b .issue
%patch6 -p1 -b .issue-doc
%patch7 -p1 -b .helper
%patch8 -p1 -b .mktemp
%patch9 -p1 -b .unioninit
%patch11 -p1 -b .helper2
%patch12 -p1 -b .no-acroread
%patch14 -p1 -b .sendmail_path
%patch15 -p1 -b .lfs
%patch16 -p1 -b .162174_tcflush
%patch18 -p1 -b .bug_63843
%patch19 -p1 -b .167830_tty_access
%patch20 -p1 -b .167830
%patch21 -p1 -b .turn
%patch22 -p1 -b .time_range
%patch23 -p1 -b .handle_spaces
%patch24 -p1 -b .man
%patch25 -p1 -b .sd
%patch26 -p1 -b .makefile
%patch27 -p1 -b .lockdev
%patch28 -p1 -b .hardening
%patch29 -p1 -b .sys_nerr-removed
%patch30 -p1 -b .manpage-typos

%build
%define makeflags CFLAGS="$RPM_OPT_FLAGS -Wall -DAUTO_PPP -D_FILE_OFFSET_BITS=64 -DHAVE_LOCKDEV -fno-strict-aliasing" LIBS="-llockdev" prefix=%{_prefix} spool=%{_var}/spool BINDIR=%{_bindir} SBINDIR=%{_sbindir} LIBDIR=%{_libdir}/mgetty+sendfax HELPDIR=%{_libdir}/mgetty+sendfax CONFDIR=%{_sysconfdir}/mgetty+sendfax MANDIR=%{_mandir} MAN1DIR=%{_mandir}/man1 MAN4DIR=%{_mandir}/man4 MAN5DIR=%{_mandir}/man5 MAN8DIR=%{_mandir}/man8 INFODIR=%{_infodir} ECHO='"echo -e"' INSTALL=%{__install}
make %{makeflags}
make -C voice %{makeflags}
make -C tools %{makeflags}

pushd frontends/X11/viewfax
make OPT="$RPM_OPT_FLAGS" CONFDIR=%{_sysconfdir}/mgetty+sendfax
popd

%install
mkdir -p %{buildroot}{%{_bindir},%{_infodir},%{_libdir}/mgetty+sendfax}
mkdir -p %{buildroot}{%{_mandir},%{_sbindir},/var/spool}
mkdir -p %{buildroot}%{_sysconfdir}/mgetty+sendfax

%define instflags CFLAGS="$RPM_OPT_FLAGS -Wall -DAUTO_PPP" prefix=%{buildroot}%{_prefix} spool=%{buildroot}%{_var}/spool BINDIR=%{buildroot}%{_bindir} SBINDIR=%{buildroot}%{_sbindir} LIBDIR=%{buildroot}%{_libdir}/mgetty+sendfax HELPDIR=%{buildroot}%{_libdir}/mgetty+sendfax CONFDIR=%{buildroot}%{_sysconfdir}/mgetty+sendfax MANDIR=%{buildroot}%{_mandir} MAN1DIR=%{buildroot}%{_mandir}/man1 MAN4DIR=%{buildroot}%{_mandir}/man4 MAN5DIR=%{buildroot}%{_mandir}/man5 MAN8DIR=%{buildroot}%{_mandir}/man8 INFODIR=%{buildroot}%{_infodir} ECHO='echo -e' INSTALL=%{__install}

make install %instflags
# the non-standard executable permissions are used due to security
install -m700 callback/callback %{buildroot}%{_sbindir}
# helper tests internally usage of suid - this is an intention
install -m4711 callback/ct %{buildroot}%{_bindir}

# this conflicts with efax
mv %{buildroot}%{_mandir}/man1/fax.1 %{buildroot}%{_mandir}/man1/mgetty_fax.1

# tools
make -C tools install %instflags

# voice mail extensions
mkdir -p %{buildroot}%{_var}/spool/voice/{messages,incoming}
make -C voice install %instflags
# the non-standard permissions are used due to security
install -m 600 -c voice/voice.conf-dist %{buildroot}%{_sysconfdir}/mgetty+sendfax/voice.conf

# don't ship documentation that is executable...
find samples -type f -exec chmod 644 {} \;

make -C frontends/X11/viewfax install %instflags MANDIR=%{buildroot}%{_mandir}/man1

# install logrotate control files
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d

# install unit file template for vgetty
mkdir -p %{buildroot}%{_unitdir}

install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/mgetty
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/sendfax
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/vgetty
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/vm
install -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/
# install faxrunqd.service
install -m 0644 distro/faxrunqd.service %{buildroot}%{_unitdir}/

# remove file droppings from buildroot
rm -f %{buildroot}%{_bindir}/cutbl

# remove file conflict with netpbm:
rm -f %{buildroot}%{_bindir}/g3topbm

%post
%systemd_post mgetty@.service

%preun
%systemd_preun mgetty@.service

%postun
%systemd_postun_with_restart mgetty@.service
exit 0

%pre sendfax
getent group fax >/dev/null || groupadd -g %SENDFAX_UID -r fax
getent passwd fax >/dev/null || useradd -r -u %SENDFAX_UID -g fax -d /var/spool/fax -s /sbin/nologin -c "mgetty fax spool user" fax

%post sendfax
%systemd_post faxrunqd.service

%preun sendfax
%systemd_preun faxrunqd.service

%postun sendfax
%systemd_postun_with_restart faxrunqd.service
exit 0

%post voice
%systemd_post vgetty@.service

%preun voice
%systemd_postun vgetty@.service

%postun voice
%systemd_postun_with_restart vgetty@.service
exit 0

%files
%doc BUGS ChangeLog README.1st Recommend THANKS doc/modems.db samples
%license COPYING
%{_bindir}/g3cat
%{_bindir}/g32pbm
%{_sbindir}/mgetty
%{_sbindir}/callback
%{_mandir}/man1/g32pbm.1*
%{_mandir}/man1/g3cat.1*
%{_mandir}/man4/mgettydefs.4*
%{_mandir}/man8/mgetty.8*
%{_mandir}/man8/callback.8*
%{_infodir}/mgetty.info*
%dir %{_sysconfdir}/mgetty+sendfax
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/login.config
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/mgetty.config
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/dialin.config
%config(noreplace) %{_sysconfdir}/logrotate.d/mgetty
%{_unitdir}/mgetty@.service

%files sendfax
%dir %{_var}/spool/fax
%attr(0755,fax,root) %dir %{_var}/spool/fax/incoming
%attr(0755,fax,root) %dir %{_var}/spool/fax/outgoing
%attr(0755,root,root) %{_bindir}/ct
%{_bindir}/faxq
%{_bindir}/faxrm
%{_bindir}/faxrunq
%{_bindir}/faxspool
%{_bindir}/kvg
%{_bindir}/newslock
%{_bindir}/pbm2g3
%{_bindir}/sff2g3
%{_sbindir}/faxrunqd
%{_sbindir}/sendfax
%dir %{_libdir}/mgetty+sendfax
%{_libdir}/mgetty+sendfax/cour25.pbm
%{_libdir}/mgetty+sendfax/cour25n.pbm
# helper tests internally usage of suid - this is an intention
%attr(04711,fax,root) %{_libdir}/mgetty+sendfax/faxq-helper
%{_mandir}/man1/pbm2g3.1*
%{_mandir}/man1/mgetty_fax.1*
%{_mandir}/man1/faxspool.1*
%{_mandir}/man1/faxrunq.1*
%{_mandir}/man1/faxq.1*
%{_mandir}/man1/faxrm.1*
%{_mandir}/man1/coverpg.1*
%{_mandir}/man1/sff2g3.1*
%{_mandir}/man5/faxqueue.5*
%{_mandir}/man8/faxq-helper.8*
%{_mandir}/man8/faxrunqd.8*
%{_mandir}/man8/sendfax.8*
%dir %{_sysconfdir}/mgetty+sendfax
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/sendfax.config
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/faxrunq.config
# sample config file doesn't use noreplace option to be installed always latest ver.
%config %{_sysconfdir}/mgetty+sendfax/faxspool.rules.sample
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/faxheader
# logrotate file name uses only sub-package name
%config(noreplace) %{_sysconfdir}/logrotate.d/sendfax
# faxrunqd unit file
%{_unitdir}/faxrunqd.service

%files voice
%doc voice/doc/* voice/Announce voice/ChangeLog voice/Readme
%dir %{_var}/spool/voice
%dir %{_var}/spool/voice/incoming
%dir %{_var}/spool/voice/messages
%{_sbindir}/vgetty
%{_bindir}/vm
%{_bindir}/pvfamp
%{_bindir}/pvfcut
%{_bindir}/pvfecho
%{_bindir}/pvffft
%{_bindir}/pvffile
%{_bindir}/pvffilter
%{_bindir}/pvfmix
%{_bindir}/pvfnoise
%{_bindir}/pvfreverse
%{_bindir}/pvfsine
%{_bindir}/pvfspeed
%{_bindir}/rmdfile
%{_bindir}/pvftormd
%{_bindir}/rmdtopvf
%{_bindir}/pvftovoc
%{_bindir}/voctopvf
%{_bindir}/pvftolin
%{_bindir}/lintopvf
%{_bindir}/pvftobasic
%{_bindir}/basictopvf
%{_bindir}/pvftoau
%{_bindir}/autopvf
%{_bindir}/pvftowav
%{_bindir}/wavtopvf
%{_mandir}/man1/zplay.1*
%{_mandir}/man1/pvf.1*
%{_mandir}/man1/pvfamp.1*
%{_mandir}/man1/pvfcut.1*
%{_mandir}/man1/pvfecho.1*
%{_mandir}/man1/pvffile.1*
%{_mandir}/man1/pvffft.1*
%{_mandir}/man1/pvfmix.1*
%{_mandir}/man1/pvfreverse.1*
%{_mandir}/man1/pvfsine.1*
%{_mandir}/man1/pvfspeed.1*
%{_mandir}/man1/pvftormd.1*
%{_mandir}/man1/pvffilter.1*
%{_mandir}/man1/pvfnoise.1*
%{_mandir}/man1/rmdtopvf.1*
%{_mandir}/man1/rmdfile.1*
%{_mandir}/man1/pvftovoc.1*
%{_mandir}/man1/voctopvf.1*
%{_mandir}/man1/pvftolin.1*
%{_mandir}/man1/lintopvf.1*
%{_mandir}/man1/pvftobasic.1*
%{_mandir}/man1/basictopvf.1*
%{_mandir}/man1/pvftoau.1*
%{_mandir}/man1/autopvf.1*
%{_mandir}/man1/pvftowav.1*
%{_mandir}/man1/wavtopvf.1*
%{_mandir}/man8/vgetty.8*
%dir %{_sysconfdir}/mgetty+sendfax
%config(noreplace) %{_sysconfdir}/mgetty+sendfax/voice.conf
# logrotate file name uses only sub-package name
%config(noreplace) %{_sysconfdir}/logrotate.d/vgetty
%config(noreplace) %{_sysconfdir}/logrotate.d/vm
%{_unitdir}/vgetty@.service

%files viewfax
%doc frontends/X11/viewfax/C* frontends/X11/viewfax/README
%{_bindir}/viewfax
%dir %{_libdir}/mgetty+sendfax
%{_libdir}/mgetty+sendfax/viewfax.tif
%{_mandir}/man1/viewfax.1*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.1-13
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.2.1-11
- 1711365 - mgetty man pages typos

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.2.1-9
- 1856765 - mgetty-1.2.1-8.fc33 FTBFS: logfile.c:354:20: error: 'sys_nerr' undeclared

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.2.1-7
- use correct systemd macros in scriptlets

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.2.1-5
- 1716409 - mgetty: %systemd_postun scriptlets need service files as an argument

* Tue Mar 26 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.2.1-4
- add faxrunqd.service unit file (#1636433)

* Tue Mar 26 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.2.1-3
- adding license file

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.2.1-2
- Fix requirement for %%postun (instead of %%preun) scriptlet

* Tue Feb 12 2019 Tomas Korbar <tkorbar@redhat.com> - 1.2.1-1
- Rebase to 1.2.1
- Resolve #1628754 #1628755 #1629971 #1629972
- Resolve #1629973 #1629974 #1629975 #1629976
- Resolve #1629979 #1629980 #1629981 #1629983
- Resolve #1629985 #1629986

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.1.37-7
- gcc is no longer in buildroot by default

* Thu Feb 08 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.1.37-6
- remove old stuff https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MRWOMRZ6KPCV25EFHJ2O67BCCP3L4Y6N/

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.1.37-1
- rebase to 1.1.37 (bug #1012344)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.36-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Michal Sekletar <msekleta@redhat.com> - 1.1.36-28
- Declare conflict with hylafax+ only for mgetty-sendfax subpackage

* Fri Aug 08 2014 Michal Sekletar <msekleta@redhat.com> - 1.1.36-27
- Fix [Install] section of unit file. Enable mgetty and vgetty under getty.target

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.1.36-25
- Use system gsm instead of bundled one

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.1.36-23
- Perl 5.18 rebuild

* Wed Jul 10 2013 Michal Sekletar <msekleta@redhat.com> - 1.1.36-22
- disable strict-aliasing optimizations
- fix dates in changelog
- fix device locking in other tools than mgetty (#982711)
- require uucp package

* Tue Apr 23 2013 Michal Sekletar <msekleta@redhat.com> - 1.1.36-21
- fix broken dependencies

* Fri Apr 19 2013 Michal Sekletar <msekleta@redhat.com> - 1.1.36-20
- resolves: #754235 #947919
- improvement to systemd configuration for vgetty
- added systemd unit for mgetty
- implemented device locking using lockdev library

* Wed Mar 20 2013 Michal Sekletar <msekleta@redhat.com> - 1.1.36-19
- Fix broken dependencies for mgetty and sendfax

* Tue Mar 19 2013 Michal Sekletar <msekleta@redhat.com> - 1.1.36-18
- Resolve : #850206 #752435
- Change naming scheme for log files
- Change configuration for logrotate
- Fix rpm scriptlets
- Fix installation of a unit file template
- Remove reduntant After= from unit file
- Fix manpage, explains how to use newly added systemd capabilities
- Add conflict with hylafax+

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Michal Sekletar <msekleta@redhat.com> - 1.1.36-14
- Resolves : #752435
- Fix rotation of log files

* Mon Sep 26 2011 Michal Sekletar <msekleta@redhat.com> - 1.1.36-13
- Resolves : #737573
- Removes information about dependency on mgetty from mgetty-viewfax description

* Thu Aug 11 2011 Michal Sekletar <msekleta@redhat.com> - 1.1.36-12
- Resolves common problem in Fedora and RHEL #729003
- Patch removes hardcoded -s parameter of /usr/bin/install, thus .debug files
  are generated properly

* Fri Aug 05 2011 Jiri Skala <jskala@redhat.com> - 1.1.36-11
- fixes #721208 - How to get vgetty to run under systemd

* Mon Aug 01 2011 Jiri Skala <jskala@redhat.com> - 1.1.36-10
- rebuild for libcap

* Tue May 10 2011 Jiri Skala <jskala@redhat.com> - 1.1.36-9
- fixes #673801 - mgetty(8) manpage fixes

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 21 2010 Jiri Skala <jskala@redhat.com> - 1.1.36-7
- group id should be equal to fax user id

* Mon Jan 25 2010 Jiri Skala <jskala@redhat.com> - 1.1.36-6
- modified spec to make rpmlint more silent
- added comments to spec to surviving rpmlint W and E

* Mon Sep 14 2009 Jiri Skala <jskala@redhat.com> - 1.1.36-5
- fixed #516001 - Errors installing mgetty with --excludedocs

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 10 2008 Jiri Skala <jskala@redhat.com> - 1.1.36-2
- fix #464983 - FTBFS mgetty-1.1.36-1.fc10 - regenerated patches

* Thu Apr 10 2008 Martin Nagy <mnagy@redhat.com> - 1.1.36-1
- update to new upstream release
- use our own faxq-helper man page now that we updated
- fix -t flag of faxspool so it now accepts time ranges as it should (#171280)
- fix mgetty and vgetty logrotate configuration files (#436727)
- faxspool will handle spaces in file names better (#46697)

* Thu Apr 03 2008 Martin Nagy <mnagy@redhat.com> - 1.1.33-17
- make sure we compile everything with FORTIFY_SOURCE

* Wed Mar 05 2008 Martin Nagy <mnagy@redhat.com> - 1.1.33-16
- fix -t option of g32pbm (#188028)
- move g32pbm and g3cat from mgetty-sendfax to mgetty (#190179)
- some whitespace changes (#263641)
- added faxq-helper man page (#243293)

* Mon Feb 18 2008 Jindrich Novy <jnovy@redhat.com> - 1.1.33-15
- fix BuildRoot, License tag
- fix policy and issue patches
- remove useless rpm macros
- rpmlint fixes

* Sun Feb 17 2008 Jindrich Novy <jnovy@redhat.com> - 1.1.33-14
- fix broken BuildRequires (#433177)

* Mon Jan 28 2008 Martin Nagy <mnagy@redhat.com> - 1.1.33-13
- fix homepage URL (#353531)
- correct Requires

* Wed Jan 09 2008 Martin Nagy <mnagy@redhat.com> - 1.1.33-12
- changed MAILER from /usr/lib/sendmail to /usr/sbin/sendmail (#427585)

* Thu Sep 06 2007 Maros Barabas <mbarabas@redhat.com> - 1.1.33-11
- rebuild

* Tue Jan 23 2007 Maros Barabas <mbarabas@redhat.com> - 1.1.33-10
- fixed install-info scriptlets (post,preun)
- Resolves #223710

* Mon Aug 21 2006 Nalin Dahyabhai <nalin@redhat.com> - 1.1.33-9
- add /usr/sbin/useradd as a prereq for the -sendfax subpackage, because
  we call it during the -sendfax %%pre scriptlet (#203266)

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 1.1.33-8
- Change BuildPrereq from texinfo to texinfo-tex

* Mon Mar 27 2006 Miloslav Trmac <mitr@redhat.com> - 1.1.33-7.FC5.3
- Change BuildPrereq from texinfo to texinfo-tex

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.1.33-7.FC5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1.33-7.FC5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Dec 18 2005 Jason Vas Dias<jvdias@redhat.com> - 1.1.33-7.FC5
- rebuild for new gcc + remove 'xmkmf' invocation for Modular X11

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Aug 01 2005 Jason Vas Dias <jvdias@redhat.com> 1.1.33-4_FC5
- fix bug 63848

* Fri Jul 22 2005 Jason Vas Dias <jvdias@redhat.com> 1.1.33-3_FC5
- fix bug 162174: prevent uninterruptable hang on exit() when
                  direct line disconnected (kernel bug 164002)
                  do tcflush(1,TCOFLUSH) before exit() in sig_goodbye()
                  block signals before entering syslog()
  workaround build system 'buffer overflow checks' bug:
                  use memcpy instead of sprintf in record.c, line 53

* Mon Apr 25 2005 Jason Vas Dias <jvdias@redhat.com> 1.1.33-1
- Upgrade to new upstream version 1.1.33

* Thu Apr 21 2005 Peter Vrabec <pvrabec@redhat.com> 1.1.31-5
- support FILE_OFFSET_BITS=64 in statvfs (#155440)

* Wed Mar 16 2005 Jason Vas Dias <jvdias@redhat.com> 1.1.31-4
- Rebuild for gcc4

* Mon Feb 21 2005 Jason Vas Dias <jvdias@redhat.com> 1.1.31-3
- fix bug 145582: wrong path to sendmail
- Rebuild for FC4

* Fri Aug 20 2004 Jason Vas Dias <jvdias@redhat.com> 1.1.31-2
- Fixed bug: 115164 - remove *printf format errors

* Fri Aug 20 2004 Jason Vas Dias <jvdias@redhat.com> 1.1.31-2
- Fixed bug: 115261 - let faxspool work if acroread isn't installed
- or gs can't understand its level3 output .

* Tue Aug 17 2004 Jason Vas Dias <jvdias@redhat.com> 1.1.31-1
- Upgraded to 1.1.31

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 18 2004 Jeremy Katz <katzj@redhat.com> 1.1.30-8
- rebuild

* Tue May 18 2004 Nalin Dahyabhai <nalin@redhat.com> 1.1.30-7
- mark configuration files config(noreplace) (#123439)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Nov 18 2003 Nalin Dahyabhai <nalin@redhat.com> 1.1.30-5
- fix paths given for faxq-helper in faxq and faxrm (#92090)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May  1 2003 Elliot Lee <sopwith@redhat.com> 1.1.30-3
- ppc64 calls for the union init patch

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.30-1
- update to 1.1.30
- use mktemp to make the temporary file when spooling fax data from stdin

* Tue Dec 10 2002 Elliot Lee <sopwith@redhat.com> 1.1.29-1
- Fix logrotate.vgetty wildcard

* Mon Nov 25 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.29-1
- update to 1.1.29
- create the fax user in -sendfax %%pre
- remove /var/spool/fax/outgoing/locks

* Tue Nov 12 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.28-10
- define PTR_IS_LONG on x86_64

* Tue Nov 12 2002 Tim Powers <timp@redhat.com>
- remove files from $RPM_BUILD_ROOT that we aren't including

* Tue Sep  3 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.28-9
- include vgetty's man page

* Fri Aug 23 2002 Elliot Lee <sopwith@redhat.com> 1.1.28-8
- /var/spool/fax/outgoing/locks needs to be sticky

* Tue Aug 13 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.28-7
- rotate mgetty.log.unknown and mgetty.log.callback (#68049)
- don't logrotate already-rotated logs (#68422)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.28-4
- rebuild in new environment

* Thu Feb 28 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.28-3
- rotate the mgetty and vgetty logs by default, specifying them with
  wildcards in the logrotate configs (#62159)

* Fri Feb 22 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.28-2
- rebuild

* Fri Jan 11 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.28-1
- update to 1.1.28

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Oct 22 2001 Nalin Dahyabhai <nalin@redhat.com> 1.1.27-1
- update to 1.1.27
- drop s390x patch (no longer needed)

* Tue Jul 24 2001 Nalin Dahyabhai <nalin@redhat.com> 1.1.26-6
- tweak the issue patch

* Tue Jul 10 2001 Bill Nottingham <notting@redhat.com>
- make /etc/issue parsing match other gettys

* Tue Jun 12 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add 64 bit patch for s390x from <oliver.paukstadt@millenux.com>

* Wed Apr 18 2001 Nalin Dahyabhai <nalin@redhat.com>
- define _sysconfdir, not sysconfdir

* Mon Apr 16 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.1.26
- add logrotate.vm and logrotate.vgetty (note from Heiner Kordewiner)
- add voice/{Announce,Changelog,Readme} to documentation set

* Tue Apr 10 2001 Nalin Dahyabhai <nalin@redhat.com>
- define CNDFILE in policy.h

* Tue Mar 20 2001 Nalin Dahyabhai <nalin@redhat.com>
- change the default group in the vgetty configuration file from phone to uucp,
  which matches the settings for faxes

* Tue Mar 13 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.1.25
- ditch the elsa patch in favor of the current vgetty patch
- don't need to strip binaries, buildroot policies do that
- add docs to the voice subpackage

* Tue Jan 16 2001 Nalin Dahyabhai <nalin@redhat.com>
- use mkdtemp() when printing faxes

* Mon Jan 15 2001 Preston Brown <pbrown@redhat.com>
- fix misdetection of USR voice modem detection <cjj@u.washington.edu>

* Mon Jan 08 2001 Preston Brown <pbrown@redhat.com>
- 1.1.24 includes tmpfile security enhancements, some of our patches

* Tue Sep 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- back out quoting patch
- change Copyright: distributable to License: GPL
- add URL
- remove logging changes from excl patch, based on input from Gert
- rework ia64 patch, break out gets/fgets change based on input from Gert

* Thu Sep  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- make sure all scripts quote variables where possible (#17179)
- make sure all scripts use mktemp for generating temporary files

* Sat Aug 26 2000 Bill Nottingham <notting@redhat.com>
- update to 1.1.22; fixes security issues

* Mon Aug  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix excl patch to keep everything from segfaulting all the time (#11523,11590)

* Mon Jul 24 2000 Nalin Dahyabhai <nalin@redhat.com>
- forcibly strip binaries (#12431)
- change dependency on libgr-progs (which is gone) to netgr-progs (#10819)
- change dependency on giftoppm to giftopnm (#8088)
- attempt to plug some potential security problems (#11874)

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- add new V250modem patch from ELSA (thanks to Jürgen Kosel)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 23 2000 Than Ngo <than@redhat.de>
- add support ELSA Microlink 56k

* Sun Jun  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- Overhaul for FHS fixes.
- Stop removing logs in postun.
- Stop stripping everything.
- ia64 fixes.

* Wed May 17 2000 Ngo Than <than@redhat.de>
- updated the new vgetty (#bug 10440)

* Sat May  6 2000 Bill Nottingham <notting@redhat.com>
- fix compilation with new gcc, or ia64, or something...

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- man pages are compressed

* Tue Sep  7 1999 Jeff Johnson <jbj@redhat.com>
- add fax print command (David Fox).

* Tue Sep 07 1999 Cristian Gafton <gafton@redhat.com>
- version 1.1.21

* Tue Aug 31 1999 Jeff Johnson <jbj@redhat.com>
- move callback to base package (#4799).

* Wed Jun  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.1.20 (#3216).

* Tue Apr  6 1999 Bill Nottingham <notting@redhat.com>
- strip setuid bit from ct

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- better log handling

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- rebuild for glibc 2.1

* Sat Aug 22 1998 Jos Vos <jos@xos.nl>
- Use a patch for creating policy.h using policy.h-dist.
- Add viewfax subpackage (X11 fax viewing program).
- Add logrotate config files for mgetty and sendfax log files.
- Properly define ECHO in Makefile for use with bash.
- Add optional use of dialin.config (for modems supporting this).
- Change default notification address to "root" (was "faxadmin").
- Change log file names according to better defaults.
- Change default notify program to /etc/mgetty+sendfax/new_fax (was
  /usr/local/bin/new_fax).

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- add faxrunqd man page (problem #850)
- add missing pbm2g3 (and man page); remove unnecessary "rm -f pbmtog3"
- delete redundant ( cd tools; make ... )

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.1.14
- AutoPPP patch

* Thu Dec 18 1997 Mike Wangsmo <wanger@redhat.com>
- added more of the documentation files to the rpm

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info support

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- updated version

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- now requires libgr-progs instead of netpbm

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- built against glibc
