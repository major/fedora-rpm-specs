# Regenerate documentation with asciidoctor
%bcond_without  oidentd_enables_asciidoctor
Summary:    RFC 1413-compliant identification server with NAT support
Name:       oidentd
Version:    3.0.0
Release:    3%{?dist}
# COPYING:                  GPLv2 text
# COPYING.DOC:              GFDLv1.3 text
# doc/book/src/download.md:                                 GFDL
# doc/book/src/getting-started/capabilities.md:             GFDL
# doc/book/src/getting-started/configuration/index.md:      GFDL
# doc/book/src/getting-started/configuration/examples.md:   GFDL
# doc/book/src/getting-started/index.md:                    GFDL
# doc/book/src/getting-started/installation.md:             GFDL
# doc/book/src/getting-started/starting-the-server.md:      GFDL
# doc/book/src/getting-started/support.md:                  GFDL
# doc/book/src/guides/index.md:                             GFDL
# doc/book/src/guides/using-oidentd-with-quassel.md:        GFDL
# doc/book/src/guides/using-oidentd-with-znc.md:            GFDL
# doc/book/src/index.md:                                    GFDL
# doc/book/src/nat/forwarding.md:                           GFDL
# doc/book/src/nat/index.md:                                GFDL
# doc/book/src/nat/introduction.md:                         GFDL
# doc/book/src/nat/static-replies.md:                       GFDL
# doc/book/src/security/dropping-privileges.md:             GFDL
# doc/book/src/security/hiding-connections.md:              GFDL
# doc/book/src/security/identification-vs-authentication.md:    GFDL
# doc/book/src/security/index.md:                           GFDL
# doc/book/src/SUMMARY.md:  GFDL
# doc/oidentd.8:            GFDL
# doc/oidentd.8.adoc:       GFDL
# doc/oidentd.conf.5.adoc:  GFDL
# doc/oidentd_masq.conf.5:  GFDL
# doc/oidentd_masq.conf.5.adoc  GFDL
# src/cfg_scan.l:           GPLv2
# src/forward.c:            GPLv2
# src/forward.h:            GPLv2
# src/inet_util.c:          GPLv2
# src/inet_util.h:          GPLv2
# src/oidentd.c:            GPLv2
# src/oidentd.h:            GPLv2
# src/options.c:            GPLv2
# src/options.h:            GPLv2
# src/masq.c:               GPLv2
# src/masq.h:               GPLv2
# src/missing/getopt.c:     LGPLv2+ (bundled from glibc)
# src/missing/getopt_missing.h: LGPLv2+ (bundled from glibc)
# src/missing/inet_aton.c:  BSD and MIT
# src/missing/ipv6_missing.c:   BSD
# src/missing/missing.h:    GPLv2
# src/missing/vasprintf.c:  LGPLv2+ (bundled from libiberty)
# src/netlink.h:            GPLv2
# src/os.c:                 GPLv2
# src/user_db.c:            GPLv2
# src/user_db.h:            GPLv2
# src/util.c:               GPLv2
# src/util.h:               GPLv2
## Files unbundled
# src/cfg_parse.c:          GPLv3+ with Bison exception
#                           and GPLv2 (derived from src/cfg_parse.y)
# src/cfg_parse.h:          GPLv3+ with Bison exception
#                           and GPLv2 (derived from src/cfg_parse.y)
# src/cfg_scan.c:           GPLv2
## Files not in a binary package
# aclocal.m4:               FSFULLR
# ar-lib:                   GPLv2+ with Autoconf exception
# compile:                  GPLv2+ with Autoconf exception
# config.sub:               GPLv3+ with exception
# config.guess:             GPLv3+ with exception
# configure:                FSFUL
# configure.ac:             GPLv2
# depcomp:                  GPLv2+ with Autoconf exception
# doc/Makefile.in:          FSFULLR
# INSTALL:                  FSFAP
# install-sh:               MIT and Public Domain
# Makefile.in:              FSFULLR
# missing:                  GPLv2+ with Autoconf exception
# src/missing/getopt_missing.h:     LGPLv2+ (bundled from glibc)
# src/kernel/dflybsd1.c:    GPLv2
# src/kernel/netbsd5.c:     GPLv2
# src/kernel/openbsd30.c:   GPLv2
# ylwrap:                   GPLv2+ with Autoconf exception
License:    GPLv2 and LGPLv2+ and BSD and MIT and GFDL
URL:        https://janikrabe.com/projects/%{name}/
Source0:    https://files.janikrabe.com/pub/%{name}/releases/%{version}/%{name}-%{version}.tar.xz
Source1:    https://files.janikrabe.com/pub/%{name}/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2:    https://files.janikrabe.com/keys/63694DD76ED116B84D286F75C4CD3CE186D1CA13.asc
Source3:    oidentd.service
Source4:    oidentd.sysconfig
# Use sysconfig options in a per-connection unit file
Patch0:     oidentd-2.5.0-Make-per-connection-unit-file-similar-to-Fedora-long.patch
BuildRequires:  autoconf
BuildRequires:  automake
# ylwrap script is a sh script
BuildRequires:  bash
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libnetfilter_conntrack-devel
BuildRequires:  make
%if %{with oidentd_enables_asciidoctor}
# asciidoctor regenerates the documentation
BuildRequires:  rubygem-asciidoctor
%endif
# sed called by ylwrap
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires(pre):  shadow-utils
Provides:       identd = %{version}-%{release}

%description
The oidentd package contains identd, which implements the RFC 1413
identification server.  Identd looks up specific TCP/IP connections
and returns either the user name or other information about the
process that owns the connection.

Install oidentd if you need to look up information about specific
TCP/IP connections.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch0 -p1
# Regenerate files
autoreconf -fi
rm src/cfg_parse.{c,h}
rm src/cfg_scan.c
%if %{with oidentd_enables_asciidoctor}
rm doc/*.{5,8}
%endif
# Remove VCS files
rm doc/book/.gitignore

%build
%configure \
    --disable-debug \
    --enable-ipv6 \
    --enable-libnfct \
    --enable-nat \
    --disable-warn \
    --enable-xdgbdir
%{make_build}

%install
%{make_install}
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/oidentd.service
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/oidentd
install -D -p -m 0644 contrib/systemd/oidentd.socket %{buildroot}%{_unitdir}/
install -D -p -m 0644 contrib/systemd/oidentd\@.service %{buildroot}%{_unitdir}/

%pre
getent group oidentd >/dev/null || groupadd -r oidentd
getent passwd oidentd >/dev/null || \
    useradd -r -g oidentd -d / -s /sbin/nologin -c "oidentd daemon" oidentd
exit 0

%post
%systemd_post oidentd.service

%preun
%systemd_preun oidentd.service

%postun
%systemd_postun_with_restart oidentd.service

%files
%license COPYING*
%doc AUTHORS ChangeLog doc/book KERNEL_SUPPORT.md NEWS README
%config(noreplace) %{_sysconfdir}/oidentd.conf
%config(noreplace) %{_sysconfdir}/oidentd_masq.conf
%config(noreplace) %{_sysconfdir}/sysconfig/oidentd
%dir %{_prefix}/lib/systemd
%dir %{_unitdir}
%{_unitdir}/oidentd.service
%{_unitdir}/oidentd@.service
%{_unitdir}/oidentd.socket
%{_sbindir}/oidentd
%{_mandir}/man?/*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 Petr Pisar <ppisar@redhat.com> - 3.0.0-1
- 3.0.0 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 03 2021 Petr Pisar <ppisar@redhat.com> - 2.5.1-1
- 2.5.1 bump

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Petr Pisar <ppisar@redhat.com> - 2.5.0-1
- 2.5.0 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> - 2.4.0-1
- 2.4.0 bump

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Petr Pisar <ppisar@redhat.com> - 2.3.1-1
- 2.3.1 bump

* Wed Jun 13 2018 Petr Pisar <ppisar@redhat.com> - 2.3.0-1
- 2.3.0 bump

* Tue Apr 03 2018 Petr Pisar <ppisar@redhat.com> - 2.2.3-1
- 2.2.3 bump

* Thu Mar 08 2018 Petr Pisar <ppisar@redhat.com> - 2.2.2-1
- 2.2.2 bump
- Upstream moved from <http://ojnk.sourceforge.net/> to
  <https://github.com/janikrabe/oidentd>
- /etc/sysconfig/oidentd file is world-readable now
- Run the daemon as oidentd user

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 Petr Pisar <ppisar@redhat.com> - 2.0.8-20
- Log errors when opening conntracking table (bug #1316308)
- Open conntracking table only if masquerading feature is requested
  (bug #1316308)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Petr Pisar <ppisar@redhat.com> - 2.0.8-18
- Modernize the specification file
- License tag corrected to (GPLv2 and LGPLv2+ and BSD and MIT and GFDL)
- Enable NAT support
- Migrate from System V to systemd service (bug #1082236)

* Wed Aug 19 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.8-17
- Append -std=gnu89 to CFLAGS (Fix F23FTBFS, RHBZ#1239743).
- Add %%license.
- Modernize spec.
- Fix bogus changelog entry.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Matthias Saou <http://freshrpms.net/> 2.0.8-7
- Update init script (#247006).
- Mark the ghosted config files as noreplace just in case.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 2.0.8-4
- Rebuild for new BuildID feature.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 2.0.8-3
- Include masquerade patch fix for 2.6.21+ (#247868, Vilius Šumskas).
- Update License field.
- Switch to using DESTDIR install method.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 2.0.8-2
- FC6 rebuild.

* Thu Jun 29 2006 Matthias Saou <http://freshrpms.net/> 2.0.8-1
- Update to 2.0.8 which fixes bugzilla #173754.
- Don't flag init script as %%config.
- Rename init script "identd" -> "oidentd", remove pidentd conflict and add
  update scriplet special case when upgrading from the "identd" service.
- Move options into a sysconfig file.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 2.0.7-9
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 2.0.7-8
- Remove obsolete identd.spoof and oidentd.users files (thanks to Apu).
- Ghost new configuration files (oidentd.conf & oidentd_masq.conf), but
  including some sane defaults would be even better.
- Cosmetic changes to the init file, and now default to disabled.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.0.7-7
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 2.0.7-5
- Bump release to provide Extras upgrade path.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 2.0.7-4
- Rebuild for Fedora Core 3.
- Change /etc/init.d to /etc/rc.d/init.d and minor other spec tweaks.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 2.0.7-3
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.0.7-2
- Rebuild for Fedora Core 1.

* Tue Jul 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.7.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Thu Aug 22 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the init script's status, thanks to JÃ¸rn for spotting this.

* Wed Aug 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.4.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Tue Jan  8 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.3.
- Fix user in %%files for "-".

* Sun Dec 30 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.2.

* Thu Oct  4 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.1.

* Mon Oct  1 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.0.

* Sat Sep 15 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.9.9.1.

* Mon Aug 27 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.9.9 (complete program rewrite).
- Added new docs and manpages.

* Tue Apr 24 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and rebuilt for Red Hat 7.1.

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- Added a Conflicts: for pidentd
- Quick cleanup
- Fixed o-r modes
- Changed the uid/gid in the initscript

* Wed Dec 27 2000 Matthias Saou <http://freshrpms.net/>
- Initial RPM release

