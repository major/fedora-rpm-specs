# Where the default web root will be configured and default files installed
%global webroot /var/www/thttpd

Name:           thttpd
Version:        2.29
Release:        19%{?dist}
Summary:        A tiny, turbo, throttleable lightweight HTTP server

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.acme.com/software/thttpd/
Source0:        http://www.acme.com/software/thttpd/thttpd-%{version}.tar.gz
Source1:        thttpd.service
Source2:        thttpd.logrotate
Source10:       index.html
Source11:       thttpd_powered_3.png
Source12:       poweredby.png
Patch0:         thttpd-2.25b-CVE-2005-3124.patch
Patch1:         thttpd-2.25b-CVE-2012-5640-check_crypt_return_value.patch
Patch2:         thttpd-fix-world-readable-log.patch
Patch3:         thttpd-c99.patch
BuildRequires: make
BuildRequires:  systemd gcc
%{?systemd_requires}
Requires(pre):  shadow-utils

%description
Thttpd is a very compact no-frills httpd serving daemon that can handle
very high loads. While lacking many of the advanced features of Apache, 
thttpd operates without forking and is extremely efficient in memory use. 
Basic support for cgi scripts, authentication, and ssi is provided for. 
Advanced features include the ability to throttle traffic.

%prep
%setup -q
%patch -P0 -p1 -b .CVE-2005-3124
%patch -P1 -p1 -b .CVE-2012-5640
%patch -P2 -p1 -b .rhbz924857
%patch -P3 -p1 -b .c99
# Convert man pages to UTF8
for man in *.8 */*.8 */*.1; do
    iconv -f iso8859-1 -t utf-8 -o tmp ${man}
    mv -f tmp ${man}
done

%build
%configure
# Hacks :-)
sed -i.old -e 's/-o bin -g bin//g' Makefile
sed -i.old -e 's/-m 444/-m 644/g; s/-m 555/-m 755/g' Makefile
sed -i.old -e 's/.*chgrp.*//g; s/.*chmod.*//g' extras/Makefile
# Config changes
%{?_without_indexes:      sed -i.old -e 's/#define GENERATE_INDEXES/#undef GENERATE_INDEXES/g' config.h}
%{!?_with_showversion:    sed -i.old -e 's/#define SHOW_SERVER_VERSION/#undef SHOW_SERVER_VERSION/g' config.h}
%{!?_with_expliciterrors: sed -i.old -e 's/#define EXPLICIT_ERROR_PAGES/#undef EXPLICIT_ERROR_PAGES/g' config.h}

%{make_build} \
    SUBDIRS="extras" WEBDIR=%{webroot} STATICFLAG="" \
    CCOPT="%{optflags} -D_FILE_OFFSET_BITS=64"

%install
# Prepare required directories
mkdir -p %{buildroot}%{webroot}          \
         %{buildroot}%{_mandir}/man{1,8} \
         %{buildroot}%{_sbindir}         \
         %{buildroot}%{_unitdir}

# Install init script and logrotate entry
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/thttpd

# Main install (list SUBDIRS to exclude "cgi-src")
make install SUBDIRS="extras" \
    BINDIR=%{buildroot}%{_sbindir} \
    MANDIR=%{buildroot}%{_mandir} \
    WEBDIR=%{buildroot}%{webroot}

# Rename htpasswd in case apache is installed too
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_sbindir}/htpasswd \
        %{buildroot}%{_bindir}/thtpasswd
mv %{buildroot}%{_mandir}/man1/htpasswd.1 \
        %{buildroot}%{_mandir}/man1/thtpasswd.1

# Install the default index.html and related files
install -pm0644 %{SOURCE10} %{SOURCE11} %{SOURCE12}\
                %{buildroot}%{webroot}/

# Symlink for the powered-by-$DISTRO image
# Removed: thttpd does not support symlink outsidedocroot
# See: http://acme.com/software/thttpd/thttpd_man.html#SYMLINKS

# Install a default configuration file
cat << EOF > %{buildroot}%{_sysconfdir}/thttpd.conf
# BEWARE : No empty lines are allowed!
# This section overrides defaults
dir=%{webroot}
chroot
user=thttpd         # default = nobody
logfile=/var/log/thttpd.log
pidfile=/var/run/thttpd.pid
# This section _documents_ defaults in effect
# port=80
# nosymlink         # default = !chroot
# novhost
# nocgipat
# nothrottles
# host=0.0.0.0
# charset=iso-8859-1
EOF

%pre
/usr/sbin/groupadd -r www &>/dev/null || :
/usr/sbin/useradd -s /sbin/nologin -c "Thttpd Web Server User" \
    -d %{webroot} -M -r -g www thttpd &>/dev/null || :

%post
%systemd_post thttpd.service

%preun
%systemd_preun thttpd.service

%postun
%systemd_postun thttpd.service

%files
%doc README TODO
%{_bindir}/thtpasswd
%if 0%{?_with_makeweb:1}
    %attr(2755,root,www) %{_sbindir}/makeweb
    %{_mandir}/man1/makeweb.1*
%else
    %exclude %{_sbindir}/makeweb
    %exclude %{_mandir}/man1/makeweb.1*
%endif
%{_sbindir}/syslogtocern
%{_sbindir}/thttpd
%{_unitdir}/thttpd.service
%config(noreplace) %{_sysconfdir}/logrotate.d/thttpd
%config(noreplace) %{_sysconfdir}/thttpd.conf
%{webroot}/
%{_mandir}/man1/thtpasswd.1*
%{_mandir}/man8/syslogtocern.8*
%{_mandir}/man8/thttpd.8*
# Hack to own parent directory for the default "webroot". Remove if needed.
%dir /var/www

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.29-18
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Florian Weimer <fweimer@redhat.com> - 2.29-13
- Port to C99 (#2147555)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Stuart Gathman <stuart@gathman.org> - 2.29-4
- Use nologin instead of false

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.29-3
- Rebuilt for libcrypt.so.2 (#1666033)

* Tue Aug 28 2018 Stuart Gathman <stuart@gathman.org> - 2.29-2
- Incorporate package review suggestions.

* Tue Aug 28 2018 Stuart Gathman <stuart@gathman.org> - 2.29-1
- Update to latest upstream release 2.29

* Wed May 11 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.27-1
- Update to latest upstream release 2.27

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.25b-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Athmane Madjoudj <athmane@fedoraproject.org> 2.25b-37
- Fix world readable patch

* Sat Nov 28 2015 Athmane Madjoudj <athmane@fedoraproject.org> 2.25b-36
- Add a patch to fix RHBZ #924857 / CVE-2013-0348

* Fri Nov 27 2015 Athmane Madjoudj <athmane@fedoraproject.org> 2.25b-35
- Add patch to fix RHBZ #887451 / CVE-2012-5640
- Fix fedora logo issue (RHBZ #1114423).
- Enable PIE flags (RHBZ #955129)
- Use systemd for post-rotate script (RHBZ #1218259)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 2.25b-33
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Matthias Saou <matthias@saou.eu> 2.25b-27
- Fix PID file location in the systemd service file (#789662).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Tom Callaway <spot@fedoraproject.org> - 2.25b-25
- convert to systemd

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Matthias Saou <http://freshrpms.net/> 2.25b-22
- Update init script all the way.

* Sat Apr 11 2009 Matthias Saou <http://freshrpms.net/> 2.25b-21
- Include patch to rename conflicting "getline" function (stdio.h).
- Fix so that makeweb gets compiled in "build" section with the right WEBDIR.

* Thu Apr  9 2009 Matthias Saou <http://freshrpms.net/> 2.25b-20
- Fix thttpd-2.25b-CVE-2005-3124.patch (#483733).
- Remove unwanted .orig files from patches (#484205).
- Don't ship useless man pages (#484205).
- Reorganize all of the webroot files under /var/www/thttpd, remove cgi-bin
  by default, remove useless log directory.
- Have makeweb be conditional and disabled by default.
- Fix thttpd mode from 555 to 755.
- Add new init block to the init script (commands and exit status need work).
- Re-enable indexes by default, it's possible to turn them off with dir modes.
- Don't even compile the CGI programs instead of just excluding them.
- No longer build htpasswd as static.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  2 2008 Matthias Saou <http://freshrpms.net/> 2.25b-18
- Own /var/www in a hack-ish way, but comment it well (#474024).

* Thu Sep 25 2008 Matthias Saou <http://freshrpms.net/> 2.25b-17
- Update patches to remove fuzz.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Mon Oct 22 2007 Matthias Saou <http://freshrpms.net/> 2.25b-15
- Update to latest upstream sources, same filename, only email address changes.
- Remove trademarked Fedora logo button and replace with a symlink to the
  main system-logo provided button image.
- Update default index.html to UTF-8 and thttpd green background color.

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 2.25b-14
- Rebuild to fix wrong execmem requirement on ppc32.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 2.25b-13
- Add missing requirements for the scriplets, they could cause the thttpd user
  to not be added when thttpd was installed from the F7 media (#234740).
- Preserve timestamps for all the installed sources.
- Init scripts are *not* config files.
- Default service to disable.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 2.25b-12
- FC6 rebuild.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 2.25b-11
- Include "fixes" patch from Debian (#191095) to fix thtpasswd and makeweb.
- Rename htpasswd as thtpasswd instead of htpasswd.thttpd.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 2.25b-10
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 2.25b-9
- Rebuild for new gcc/glibc.
- Remove prever stuff, 2.25b final has been around for while now.

* Mon Nov  7 2005 Matthias Saou <http://freshrpms.net/> 2.25b-8
- Add patch from Gentoo to fix CVE-2005-3124 (#172469, Ville Skyttä).
- Minor cosmetic spec file changes.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.25b
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Jan 20 2005 Matthias Saou <http://freshrpms.net/> 2.25b-5
- Compile with -D_FILE_OFFSET_BITS=64 to support > 2GB log files.

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 2.25b-4
- Bump release to provide Extras upgrade path.
- Re-brand Fedora where it was freshrpms previously.

* Sat Jul 10 2004 Dag Wieers <dag@wieers.com> - 2.25b-3
- Fixed location of service in logrotate conf. (Peter Bieringer)

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 2.25b-2
- Rebuild for Fedora Core 2.

* Mon Apr 26 2004 Matthias Saou <http://freshrpms.net/> 2.25b-2
- Add logrotate entry, it needs to restart thttpd completely because
  of the permissions dropped after opening the log file :-(

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 2.25b-1
- Update to 2.25b.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 2.24-1
- Update to 2.24 final.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.23-0.beta1.3
- Rebuild for Fedora Core 1.
- Escaped the %%install and others later in this changelog.

* Wed Oct 22 2003 Matthias Saou <http://freshrpms.net/>
- Added build options and now default to no indexes, explicit errors or
  showing version.

* Mon Nov  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.23beta1.

* Fri May  4 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat 7.
- New, clean initscript.
- Built the latest 2.21b version since 2.20b won't compile even with kgcc.
- Custom config file based on the contrib/redhat one.

* Wed Sep 13 2000 Jef Poskanzer <jef@acme.com>
- Updated to 2.20

* Mon Sep 11 2000 Bennett Todd <bet@rahul.net>
- added thttpd.conf, took config info out of init script
- switched to logging in /var/log, used pidfile

* Thu Jun 15 2000 Jef Poskanzer <jef@acme.com>
- Updated to 2.19

* Thu May 18 2000 Jef Poskanzer <jef@acme.com>
- Updated to 2.18

* Fri Mar 17 2000 Jef Poskanzer <jef@acme.com>
- Updated to 2.17

* Mon Feb 28 2000 Jef Poskanzer <jef@acme.com>
- Updated to 2.16

* Thu Feb 03 2000 Jef Poskanzer <jef@acme.com>
- Updated to 2.15

* Fri Jan 21 2000 Jef Poskanzer <jef@acme.com>
- Updated to 2.14

* Thu Jan  6 2000 Jef Poskanzer <jef@acme.com>
- Updated to 2.13

* Mon Jan  3 2000 Bennett Todd <bet@rahul.net>
- updated to 2.12, tweaked to move thttpd.init into tarball

* Mon Dec 13 1999 Bennett Todd <bet@mordor.net>
- Updated to 2.09

* Fri Dec 10 1999 Bennett Todd <bet@mordor.net>
- Updated to 2.08

* Wed Nov 24 1999 Bennett Todd <bet@mordor.net>
- updated to 2.06, parameterized Version string in source url
- changed to use "make install", simplified %%files list

* Wed Nov 10 1999 Bennett Todd <bet@mordor.net>
- Version 2.05, reset release to 1
- dropped bugfix patch since Jef included that
- streamlined install

* Sun Jul 25 1999 Bennett Todd <bet@mordor.net>
- Release 4, added mime type swf

* Mon May  3 1999 Bennett Todd <bet@mordor.net>
- Release 2, added patch to set cgi-timelimit up to 10 minutes
  fm default 30 seconds

* Wed Feb 10 1999 Bennett Todd <bet@mordor.net>
- based on 2.00-2, bumped to 2.04, reset release back to 1
- fixed a couple of broken entries in %%install to reference %%{buildroot}
- simplified %%files to populate /usr/doc/... with just [A-Z]* (TODO had gone
  away, this simplification makes it liklier to be trivially portable to
  future releases).
- added %%doc tags for the man pages

