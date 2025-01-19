# Milter header files package name
%if 0%{?fedora} > 25 || 0%{?rhel} > 7
%global milter_devel_package sendmail-milter-devel
%else
%global milter_devel_package sendmail-devel
%endif

# Don't support legacy GeoIP library from F-32, EPEL-8 onwards
# Support libmaxminddb instead
%if 0%{?fedora} > 31 || 0%{?rhel} > 7
%global geoip_support		0
%global maxminddb_support	1
%else
%global geoip_support		1
%global maxminddb_support	0
%endif

Summary:		Milter for greylisting, the next step in the spam control war
Name:			milter-greylist
Version:		4.6.4
Release:		16%{?dist}
# License is like BSD-4-Clause but without the 4th clause
# We use spamd.c but not queue.h
# See READNE for details
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:		LicenseRef-Callaway-BSD-with-advertising
URL:			http://hcpnet.free.fr/milter-greylist/
Source0:		ftp://ftp.espci.fr/pub/milter-greylist/milter-greylist-%{version}.tgz
Source1:		README.fedora
Source20:		milter-greylist.systemd.service
Patch0:			milter-greylist-4.6.3-config.patch
Patch1:			milter-greylist-4.4.2-utf8.patch
Patch2:			milter-greylist-4.5.11-warning.patch
Patch4:			ai_addrconfig.patch
BuildRequires:		bison
BuildRequires:		coreutils
BuildRequires:		curl-devel
BuildRequires:		flex
BuildRequires:		gcc
%if %{geoip_support}
BuildRequires:		GeoIP-devel
%endif
%if %{maxminddb_support}
BuildRequires:		libmaxminddb-devel
%endif
BuildRequires:		libspf2-devel
BuildRequires:		m4
BuildRequires:		make
BuildRequires:		%milter_devel_package
BuildRequires:		perl-interpreter
BuildRequires:		sed

# Scriptlet dependencies
BuildRequires:		systemd
Requires(pre):		shadow-utils
%{?systemd_requires}

%if %{maxminddb_support}
Recommends:		geolite2-country
%endif

%description
Greylisting is a new method of blocking significant amounts of spam at
the mailserver level, but without resorting to heavyweight statistical
analysis or other heuristical (and error-prone) approaches. Consequently,
implementations are fairly lightweight, and may even decrease network
traffic and processor load on your mailserver.

This package provides a greylist filter for sendmail's milter API.

%prep
%setup -q -n milter-greylist-%{version}

# Customize config for Fedora / EPEL
# * Specify pidfile in initscript rather than config file
# * Specify socket in config file rather than initscript
# * Specify grmilter as the user to run the dæmon as
# * Specify the GeoIP/GeoIP2 database location
%patch -P0

# Re-code docs as UTF8
%patch -P1

# Work around warning about _BSD_SOURCE being deprecated in favor
# of _DEFAULT_SOURCE breaking build due to use of -Werror
# (patch breaks builds with EL < 7)
%if 0%{?fedora} > 20 || 0%{?rhel} > 6
%patch -P2
%endif

# Work around issues with ISC libbind and AI_ADDRCONFIG
# http://tech.groups.yahoo.com/group/milter-greylist/message/5048
%patch -P4 -p1

# Drop GeoIP configuration if we don't support it
%if ! %{geoip_support}
perl -i -ne 'print $_ unless m{^geoipdb }' greylist.conf
%endif
%if ! %{maxminddb_support}
perl -i -ne 'print $_ unless m{^geoip2db }' greylist.conf
%endif

# README.fedora
install -p -m 644 %{SOURCE1} .

# Don't let the configure script find libresolv
sed -i -e 's!/libresolv.a!/../../../no-such-lib.a!g' configure

# Set socket/db/pidfile to be in FHS-compliant places
for i in `find -type f`; do
    sed -e 's|/var/milter-greylist/milter-greylist.sock|/run/milter-greylist/milter-greylist.sock|g;
	    s|/var/milter-greylist/greylist.db|%{_localstatedir}/lib/milter-greylist/db/greylist.db|g;
	    s|/var/milter-greylist/milter-greylist.pid|/run/milter-greylist.pid|g;
	   ' "$i" >"$i.tmp"
    cmp -s "$i" "$i.tmp" || cat "$i.tmp" >"$i"
    rm -f "$i".tmp
done


%build
# Harden the build if supported
%global _hardened_build 1
export CFLAGS="%{__global_cflags} -fno-strict-aliasing -D_GNU_SOURCE -std=gnu17"
export LDFLAGS="-Wl,-z,now -Wl,-z,relro %{__global_ldflags} -Wl,--as-needed $LDLIBS"
%configure \
	--disable-drac				\
	--disable-rpath				\
	--enable-dnsrbl				\
	--enable-p0f				\
	--enable-spamassassin			\
	--with-drac-db=%{_localstatedir}/lib/milter-greylist/drac/drac.db \
	--with-libcurl				\
%if %{geoip_support}
	--with-libGeoIP				\
%endif
%if %{maxminddb_support}
	--with-libmaxminddb			\
%endif
	--with-libspf2				\
	--with-user=grmilter

%{make_build} BINDIR=%{_sbindir}

%install
install -d -m 755 %{buildroot}{/run/milter-greylist,%{_localstatedir}/lib/milter-greylist/db}
%{make_install} \
	BINDIR=%{_sbindir} \
	TEST=false \
	USER="$(id -u)"

# Create a dummy socket so we can %%ghost it and remove it on uninstall
touch %{buildroot}/run/milter-greylist/milter-greylist.sock

# Initscript
install -D -p -m 0644 %{SOURCE20} %{buildroot}%{_unitdir}/milter-greylist.service

# Make sure /run/milter-greylist is re-created at boot time if /run is on tmpfs
install -d -m 755 %{buildroot}%{_prefix}/lib/tmpfiles.d
cat << EOF > %{buildroot}%{_prefix}/lib/tmpfiles.d/milter-greylist.conf
d /run/milter-greylist 0710 root mail
EOF

%pre
# Create account for milter-greylist to run as
getent group grmilter >/dev/null || groupadd -r grmilter
getent passwd grmilter >/dev/null || \
	useradd -r -g grmilter -d %{_localstatedir}/lib/milter-greylist -s /sbin/nologin \
	 -c "Greylist-milter user" grmilter
exit 0

%post
%systemd_post milter-greylist.service

%preun
%systemd_preun milter-greylist.service

%postun
%systemd_postun_with_restart milter-greylist.service

%files
%license README
%doc ChangeLog README.fedora milter-greylist.m4
%{_sbindir}/milter-greylist
%attr(0640,root,grmilter) %verify(not mtime) %config(noreplace) %{_sysconfdir}/mail/greylist.conf
%dir %attr(0751,grmilter,grmilter) %{_localstatedir}/lib/milter-greylist/
%dir %attr(0770,root,grmilter) %{_localstatedir}/lib/milter-greylist/db/
%dir %attr(0710,root,mail) /run/milter-greylist/
%{_mandir}/man5/greylist.conf.5*
%{_mandir}/man8/milter-greylist.8*
%ghost /run/milter-greylist/milter-greylist.sock
%{_prefix}/lib/tmpfiles.d/milter-greylist.conf
%{_unitdir}/milter-greylist.service

%changelog
* Fri Jan 17 2025 Paul Howarth <paul@city-fan.org> - 4.6.4-16
- Build with -std=gnu17 due to issues with milter API (#2336394)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 4.6.4-14
- Convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul  9 2024 Software Management Team <packaging-team-maint@redhat.com> - 4.6.4-12
- Eliminate use of obsolete %%patchN syntax (rhbz#2283636)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar  3 2023 Paul Howarth <paul@city-fan.org> - 4.6.4-8
- Use %%license unconditionally
- Drop legacy SysV init support
- Drop decade-old obsoletes/provides for milter-greylist-systemd
- Unconditionally used hardened build
- Use systemd scriptlet macros

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Florian Weimer <fweimer@redhat.com> - 4.6.4-6
- Build with -D_GNU_SOURCE for improved C99 compatibility (#2160360)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Paul Howarth <paul@city-fan.org> - 4.6.4-1
- Update to 4.6.4
  - Fix crash when GeoIP2 is not configured
  - MacOSX build fix for --enable-dnsrbl

* Tue Jul 28 2020 Paul Howarth <paul@city-fan.org> - 4.6.3-1
- Update to 4.6.3
  - Add support for GeoIP2
  - Build fixes for conflicting ns_type in SPF and NSupdate code
  - Quiet build warnings
  - Missing bits to make rawfrom usable
  - Fix crash when GeoIP for IPv6 is not configured
  - Report queueId for maxpeek overflow warnings
  - Sendmail access.db usage documentation
- Add libmaxminddb support for builds on F-32/EL-8 onwards
- Modernize spec using %%{make_build} and %%{make_install}

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct  3 2019 Paul Howarth <paul@city-fan.org> - 4.6.2-11
- Drop legacy GeoIP support from F-32, EPEL-8 onwards

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Paul Howarth <paul@city-fan.org> - 4.6.2-9
- Make run/milter-greylist directory owned by root to avoid need for
  dac_override (#1678038)
- BR: systemd rather than systemd-units for %%{_unitdir} macro
- Use %%{_initddir} rather than the deprecated %%{_initrddir}
- Improve readability by not using full paths for scriptlet commands
- Drop EL-5 support
  - Nothing needs libbind now
  - Drop explicit buildroot cleaning in %%install section

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Paul Howarth <paul@city-fan.org> - 4.6.2-2
- Fix crash on IPv6 connection with no GeoIPv6 database in use

* Thu Nov 24 2016 Paul Howarth <paul@city-fan.org> - 4.6.2-1
- Update to 4.6.2
  - Add rawfrom ACL clause to match unprocessed FROM command
  - Fix helo ACL clause string match
  - Avoid excessive GeoIP logs if database was not set
  - Fix crashes on configuration reload
  - Allow empty quoted strings in configuration
  - Add GeoIP support for IPv6

* Fri Aug  5 2016 Paul Howarth <paul@city-fan.org> - 4.6.1-2
- sendmail-devel renamed to sendmail-milter-devel from Fedora 26
- Explicitly BR: systemd-units for %%{_unitdir} macro definition

* Tue Jul 12 2016 Paul Howarth <paul@city-fan.org> - 4.6.1-1
- Update to 4.6.1
  - Fix DKIM ACL evaluation

* Mon May  9 2016 Paul Howarth <paul@city-fan.org> - 4.6-1
- Update to 4.6
  - Support IPv6 DNSRBL
  - Fix strtok_r() state usage
  - Document queueID log for PostFix
  - Fix file descriptor leak in spamd code

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Paul Howarth <paul@city-fan.org> - 4.5.16-2
- Enable SPF support using libspf2

* Mon Nov  2 2015 Paul Howarth <paul@city-fan.org> - 4.5.16-1
- Update to 4.5.16
  - Reflect config syntax in addhheader logs
  - Honour daemon option in Redhat startup script
  - Fix crash in SPF code

* Mon Oct  5 2015 Paul Howarth <paul@city-fan.org> - 4.5.15-1
- Update to 4.5.15
  - Use QueueId on Postfix
  - Only change socket ownership if it exists in filesystem
  - Index option for the addheader clause
  - Add format strings for SPF and DKIM results
  - Update author list

* Thu Jul  2 2015 Paul Howarth <paul@city-fan.org> - 4.5.14-1
- Update to 4.5.14
  - Accept format strings in helo acl and compare without case
  - Improve configure ability to run with -Werror
  - Overcome select(2) file descriptor limit
  - Support glob(7) pattern matching for properties
  - Build fixes

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Paul Howarth <paul@city-fan.org> - 4.5.12-2
- Include milter-greylist.m4 as %%doc
- Add preset support for EL-7 build
- Tag README as %%license where possible as it includes the license details

* Thu Dec 18 2014 Paul Howarth <paul@city-fan.org> - 4.5.12-1
- Update to 4.5.12
  - Prevent buffer overflow on IP address in DRAC code
  - Remove duplicate dkim check in configure
  - Let MX clause work if a MX has no DNS A record
  - Fix build on CentOS

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Paul Howarth <paul@city-fan.org> - 4.5.11-1
- Update to 4.5.11
  - Use asynchronous LDAP calls to reduce lock contention on heavy load
- Work around warning about _BSD_SOURCE being deprecated in favor
  of _DEFAULT_SOURCE breaking build due to use of -Werror

* Mon Feb 10 2014 Paul Howarth <paul@city-fan.org> - 4.5.10-1
- Update to 4.5.10
  - Fix msgcount miscomputation and crashes

* Wed Feb  5 2014 Paul Howarth <paul@city-fan.org> - 4.5.9-1
- Update to 4.5.9
  - multiracl option to disable sticky whitelisting among recipients

* Tue Feb  4 2014 Paul Howarth <paul@city-fan.org> - 4.5.8-1
- Update to 4.5.8
  - FreeBSD build fix
  - Fix CRLF in multiline headers for DKIM
  - Support OpenDKIM
  - Build if PACKAGE_URL is not defined
  - res_state Solaris build fix
  - Fix maxpeek usage for body matching clauses
- Drop DKIM re-entrancy patch

* Mon Sep 16 2013 Paul Howarth <paul@city-fan.org> - 4.5.7-1
- Update to 4.5.7
  - Do not use strndup(), for POSIX.1-2001 compatibility

* Mon Sep  2 2013 Paul Howarth <paul@city-fan.org> - 4.5.6-1
- Update to 4.5.6
  - Fix bug that replaced first character of hostname by '['
  - Do not force into lowercase properties set using the set clause
  - Add %%cA and %%ca to report current ACL line number and id
  - Increase format string maximum length to 4096
  - Break long SMTP replies into mutiple lines
  - Add configure --disable-parallel-make in case make -j is unsupported

* Sun Sep  1 2013 Paul Howarth <paul@city-fan.org> - 4.5.5-1
- Update to 4.5.5
  - Fix memory leak in log ACL clause
  - Updated AUTHORS in manpage
  - Fix typos in manpage, style
  - Numeric operator tests for property versus number
  - Numeric operator tests for property versus property

* Mon Aug 19 2013 Paul Howarth <paul@city-fan.org> - 4.5.3-1
- Update to 4.5.3
  - Format string expansions now honor %%r everywhere possible
  - Add unbracket option to resolve MTA-passed bracketed unresolved IP
  - set ACL clause to set/increment/decrement properties
  - log ACL clause to send formatted string to syslog

* Wed Aug 14 2013 Paul Howarth <paul@city-fan.org> - 4.5.2-1
- Update to 4.5.2
  - Fix crash when chown socket without group
  - Fix memory leak in nsupdate config reload
  - Fix nsupdate servers option
  - Build fixes
  - Fix ACL bypass for second recipient when sender passed auth/tls/spf
  - Parallel build
  - Configurable package information
  - More verbosity in SPF logs
  - Use localaddr for p0f and %%V format string
  - Search current directory first for includes
  - Make unknown AF family non fatal in p0f, report errors once
- Enable parallel build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Paul Howarth <paul@city-fan.org> - 4.5.1-1
- Update to 4.5.1
  - More Solaris build fixes
  - Fix swapped %%f and %%r for stat example in default greylist.conf
  - Support p0f v3.06 and up with --with-p0f-src or --enable-p0f306
  - DNS update support
  - "make clean" clears milter-greylist.spec
  - Add IPv6 support for MX sync

* Thu Apr 11 2013 Paul Howarth <paul@city-fan.org> - 4.4.2-1902
- Drop unused upstart support
- Drop unused libspf support
- Drop %%defattr, redundant since rpm 4.4
- Merge sysv/system packages back into main package, configuring appropriate
  initscrit for target distribution
- Move tmpfiles configuration from /etc to /usr/lib
- Re-do scriptlets

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 4.4.2-1901
- Migrate from fedora-usermgmt to guideline scriptlets

* Sun Jan 27 2013 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.4.2-1900
- updated to 4.4.2
- rediffed patches and removed obsolete ones
- enabled hardened build
- enabled PrivateTmp for systemd

* Sun Aug 19 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.7-1900
- disabled upstart
- removed old sysv related cruft

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.7-1701
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan  4 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.7-1700
- fixed various systemd and tmpfile related issues (698961, comments 5 + 6)

* Sat Apr 23 2011 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.7-1600
- updated to 4.2.7
- fixed tmpfiles syntax

* Tue Mar  1 2011 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.6-1600
- fixed byte order of src port in p0f check

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-1501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.6-1401
- added systemd initscripts and obsolete the old sysvinit ones

* Wed Jul 14 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.6-1400
- updated to 4.2.6

* Fri Jul  9 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.5-1401
- added spamd-null patch

* Wed Jun  9 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.5-1400
- updated to 4.2.5
- added cloexec patch
- rediffed patches

* Sun Apr 18 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.4-1400
- updated to 4.2.4
- removed patches which have been applied upstream

* Sat Feb 20 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.3-1400
- added patches to fix races in dkim, geoip and p0f modules
- conditionalized -upstart subpackage
- added conditional to build it with libbind (required for RHEL5)

* Sun Dec  6 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.3-1300
- updated -upstart to upstart 0.6.3

* Wed Aug 19 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.3-2
- moved pre-2007 %%changelog entries into ChangeLog.rpm
- do not link against libbind anymore; recent glibc seems to have
  fixed its resolver API so that -lresolv can be used by dnsrbl. Old
  -lbind conflicts with this library in a subtly way causing segfaults
  (#518274).

* Wed Aug 19 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.3-1
- updated to 4.2.3
- use conditionalized %%noarch macro to mark noarch subpackages
- simplified upstart initscript because #501155 is solved

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2.2-0.
- updated to 4.2.2
- removed patches which where applied upstream

* Mon Mar 09 2009 Adam Tkac <atkac redhat com> - 4.2-0.5.b1
- libbind has been moved to separate package, rebuild

* Sat Mar  7 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2-0.4.b1
- added -upstart subpackage
- renamed -sysv to -sysvinit to let -upstart win the default depresolving

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-0.3.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.2-0.1.b1
- updated to 4.2b1
- enabled spamassassin + p0f support
- set path to GeoIP database in sample configuration (#439087)
- changed /var/run/milter-greylist to be owned by the mail group and
  made it group-accessibly; this should allow usage with postfix when
  setting a 0666 socket mode (#210765)
- added README.fedora

* Fri Aug  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.1.1-2
- fix license tag

* Sat Jun 21 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.1.1-1
- updated to 4.1.1

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.0-2
- Autorebuild for GCC 4.3

* Sat Nov 10 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.0-1
- updated to final 4.0
- fixed conflicts between libbind and libresolv by linking them manually

* Mon Oct 29 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.0-0.3.rc2
- updated to 4.0rc2

* Sun Oct 14 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 4.0-0.2.rc1
- updated to 4.0rc1
- built with curl and GeoIP support

* Wed Apr 25 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 3.0-2
- fixed user name in config file (bz #237737)
- commented out pidfile entry; it is to be set by the init methods

* Tue Apr 17 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 3.0-1
- updated to 3.0
- enabled dnsrbl
- removed -initng subpackage

* Tue Jan 30 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 2.1.12-3
- removed -minit subpackage
