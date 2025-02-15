# Regenerate documentation with asciidoctor
%bcond_without  oidentd_enables_asciidoctor
Summary:    RFC 1413-compliant identification server with NAT support
Name:       oidentd
Version:    3.1.0
Release:    8%{?dist}
# COPYING:                  GPL-2.0 text
# COPYING.DOC:              GFDL-1.3 text
# doc/book/src/download.md:                                 GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/capabilities.md:             GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/configuration/index.md:      GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/configuration/examples.md:   GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/index.md:                    GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/installation.md:             GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/starting-the-server.md:      GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/support.md:                  GFDL-1.3-no-invariants-or-later
# doc/book/src/guides/index.md:                             GFDL-1.3-no-invariants-or-later
# doc/book/src/guides/using-oidentd-with-quassel.md:        GFDL-1.3-no-invariants-or-later
# doc/book/src/guides/using-oidentd-with-znc.md:            GFDL-1.3-no-invariants-or-later
# doc/book/src/index.md:                                    GFDL-1.3-no-invariants-or-later
# doc/book/src/nat/forwarding.md:                           GFDL-1.3-no-invariants-or-later
# doc/book/src/nat/index.md:                                GFDL-1.3-no-invariants-or-later
# doc/book/src/nat/introduction.md:                         GFDL-1.3-no-invariants-or-later
# doc/book/src/nat/static-replies.md:                       GFDL-1.3-no-invariants-or-later
# doc/book/src/security/dropping-privileges.md:             GFDL-1.3-no-invariants-or-later
# doc/book/src/security/hiding-connections.md:              GFDL-1.3-no-invariants-or-later
# doc/book/src/security/identification-vs-authentication.md:    GFDL-1.3-no-invariants-or-later
# doc/book/src/security/index.md:                           GFDL-1.3-no-invariants-or-later
# doc/book/src/SUMMARY.md:  GFDL-1.3-no-invariants-or-later
# doc/oidentd.8:            GFDL-1.3-no-invariants-or-later
# doc/oidentd.8.adoc:       GFDL-1.3-no-invariants-or-later
# doc/oidentd.conf.5.adoc:  GFDL-1.3-no-invariants-or-later
# doc/oidentd_masq.conf.5:  GFDL-1.3-no-invariants-or-later
# doc/oidentd_masq.conf.5.adoc  GFDL-1.3-no-invariants-or-later
# src/cfg_scan.l:           GPL-2.0-only
# src/forward.c:            GPL-2.0-only
# src/forward.h:            GPL-2.0-only
# src/inet_util.c:          GPL-2.0-only
# src/inet_util.h:          GPL-2.0-only
# src/oidentd.c:            GPL-2.0-only
# src/oidentd.h:            GPL-2.0-only
# src/options.c:            GPL-2.0-only
# src/options.h:            GPL-2.0-only
# src/masq.c:               GPL-2.0-only
# src/masq.h:               GPL-2.0-only
# src/missing/missing.h:    GPL-2.0-only
# src/netlink.h:            GPL-2.0-only
# src/os.c:                 GPL-2.0-only
# src/user_db.c:            GPL-2.0-only
# src/user_db.h:            GPL-2.0-only
# src/util.c:               GPL-2.0-only
# src/util.h:               GPL-2.0-only
## Files unbundled
# src/cfg_parse.c:          GPL-3.0-or-later WITH Bison-exception-2.2
#                           AND GPL-2.0-only (derived from src/cfg_parse.y)
# src/cfg_parse.h:          GPL-3.0-or-later WITH Bison-exception-2.2
#                           AND GPL-2.0-only (derived from src/cfg_parse.y)
# src/cfg_scan.c:           GPL-2.0-only
# src/missing/inet_aton.c:  BSD-4-Clause-UC AND MIT-like (completely hidden by HAVE_INET_ATON macro)
# src/missing/ipv6_missing.c:   BSD-2-Clause
# src/missing/getopt.c:     LGPL-2.1-or-later (bundled from glibc)
# src/missing/getopt_missing.h: LGPL-2.1-or-later (bundled from glibc)
# src/missing/vasprintf.c:  LGPL-2.0-or-later (bundled from libiberty)
## Files not in a binary package
# aclocal.m4:               FSFULLRWD
# ar-lib:                   GPL-2.0-or-later WITH Autoconf-exception-generic
# compile:                  GPL-2.0-or-later WITH Autoconf-exception-generic
# config.sub:               GPL-3.0-or-later WITH Autoconf-exception-generic
# config.guess:             GPL-3.0-or-later WITH Autoconf-exception-generic
# configure:                FSFUL
# configure.ac:             GPL-2.0-only
# depcomp:                  GPL-2.0-or-later WITH Autoconf-exception-generic
# doc/Makefile.in:          FSFULLRWD
# INSTALL:                  FSFAP
# install-sh:               X11 AND LicenseRef-Fedora-Public-Domain
# Makefile.in:              FSFULLRWD
# missing:                  GPL-2.0-or-later WITH Autoconf-exception-generic
# src/missing/getopt_missing.h:     LGPL-2.1-or-later (bundled from glibc)
# src/kernel/dflybsd1.c:    GPL-2.0-only
# src/kernel/netbsd5.c:     GPL-2.0-only
# src/kernel/openbsd30.c:   GPL-2.0-only
# ylwrap:                   GPL-2.0-or-later WITH Autoconf-exception-generic
License:    GPL-2.0-only AND GFDL-1.3-no-invariants-or-later
URL:        https://%{name}.janikrabe.com/
Source0:    https://files.janikrabe.com/pub/%{name}/releases/%{version}/%{name}-%{version}.tar.xz
Source1:    https://files.janikrabe.com/pub/%{name}/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2:    https://files.janikrabe.com/keys/63694DD76ED116B84D286F75C4CD3CE186D1CA13.asc
Source3:    oidentd.service
Source4:    oidentd.sysconfig
# Use sysconfig options in a per-connection unit file, not suitable for
# the upstream
Patch0:     oidentd-3.1.0-Make-per-connection-unit-file-similar-to-Fedora-long.patch
Patch1:     oidentd-configure-c-compatibility.patch
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
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
Requires(pre):  shadow-utils
%endif
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
%autosetup -p1
# Replace files whose code is excluded from compilation by a C preprocessor
# macro but whose license would influence a license of the executable.
truncate -c -s 0 src/missing/getopt.c
truncate -c -s 0 src/missing/getopt_missing.h
truncate -c -s 0 src/missing/inet_aton.c
truncate -c -s 0 src/missing/ipv6_missing.c
truncate -c -s 0 src/missing/vasprintf.c
# Regenerate files
rm src/cfg_parse.{c,h}
rm src/cfg_scan.c
%if %{with oidentd_enables_asciidoctor}
rm doc/*.{5,8}
%endif
# Remove VCS files
rm doc/book/.gitignore

# Create a sysusers.d config file
cat >oidentd.sysusers <<EOF
u oidentd - 'oidentd daemon' - -
EOF

%build
autoreconf -fi
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
install -m0644 -D oidentd.sysusers %{buildroot}%{_sysusersdir}/oidentd.conf

%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
%pre
getent group oidentd >/dev/null || groupadd -r oidentd
getent passwd oidentd >/dev/null || \
    useradd -r -g oidentd -d / -s /sbin/nologin -c "oidentd daemon" oidentd
exit 0
%endif

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
%{_mandir}/man5/oidentd*
%{_mandir}/man8/oidentd.*
%{_sysusersdir}/oidentd.conf

%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.0-8
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Florian Weimer <fweimer@redhat.com> - 3.1.0-3
- Fix C compatibility issue in the configure script

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 13 2023 Petr Pisar <ppisar@redhat.com> - 3.1.0-1
- 3.1.0 bump
- License changed to "GPL-2.0-only AND GFDL-1.3-no-invariants-or-later"

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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

