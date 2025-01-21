Name:           sqlgrey
Version:        1.8.0
Release:        30%{?dist}
Summary:        Postfix grey-listing policy service
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sqlgrey.sourceforge.net/
Source0:        http://dl.sourceforge.net/sqlgrey/sqlgrey-%{version}.tar.gz
Source1:        sqlgrey.service
Patch0:         sqlgrey-1.7.4-sqlite.patch
Patch1:         sqlgrey-1.7.4-warnings.patch
BuildArch:      noarch

Requires:               postfix
Requires:               perl(DBD::SQLite)
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires: systemd
BuildRequires: perl-generators
BuildRequires: perl-Pod-Perldoc
BuildRequires: perl-podlators

%description
SQLgrey is a Postfix grey-listing policy service with auto-white-listing
written in Perl with SQL database as storage backend.  Greylisting stops 50
to 90% of junk mails (spam and virus) before they reach your Postfix server
(saves BW, user time and CPU time).

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make rh-install ROOTDIR=$RPM_BUILD_ROOT
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/sqlgrey.service
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/init.d/
mkdir -p -m 755 $RPM_BUILD_ROOT%{_var}/lib
mkdir -m 750 $RPM_BUILD_ROOT%{_var}/lib/sqlgrey
touch $RPM_BUILD_ROOT%{_var}/lib/sqlgrey/sqlgrey.db

%files
%doc Changelog CONTRIB COPYING FAQ HOWTO README* TODO
%{_unitdir}/sqlgrey.service
%{_sbindir}/sqlgrey
%{_sbindir}/update_sqlgrey_config
%{_bindir}/sqlgrey-logstats.pl
%{_mandir}/man1/sqlgrey.1*
%attr(-,sqlgrey,sqlgrey) %dir %{_var}/lib/sqlgrey
%attr(-,sqlgrey,sqlgrey) %ghost %{_var}/lib/sqlgrey/sqlgrey.db
%dir %{_sysconfdir}/sqlgrey
%config(noreplace) %{_sysconfdir}/sqlgrey/sqlgrey.conf
# Content of these files are changed by sqlgrey itself
%config(noreplace) %{_sysconfdir}/sqlgrey/clients_ip_whitelist
%config(noreplace) %{_sysconfdir}/sqlgrey/clients_fqdn_whitelist
%config(noreplace) %{_sysconfdir}/sqlgrey/*.regexp
# Warning admins to not touch the above files
%attr(644,root,root) %config %{_sysconfdir}/sqlgrey/README

%pre
getent group sqlgrey >/dev/null || groupadd -r sqlgrey
getent passwd sqlgrey >/dev/null || \
    useradd -r -g sqlgrey -d /var/lib/sqlgrey -s /sbin/nologin \
    -c "SQLgrey server" sqlgrey
exit 0

%post
%systemd_post sqlgrey.service

%preun
%systemd_preun sqlgrey.service

%postun
%systemd_postun_with_restart sqlgrey.service

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.0-29
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.0-21
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Kevin Fenzi <kevin@scrye.com> - 1.8.0-11
- Add BuildRequires for perldoc and pod2man. Fixes FTBFS.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 18 2014 Kevin Fenzi <kevin@scrye.com> 1.8.0-8
- Moderize spec file. Fixes bug #850325

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.8.0-5
- Perl 5.18 rebuild
- Build-require systemd-units

* Mon Feb 25 2013 Tom Callaway <spot@fedoraproject.org> - 1.8.0-4
- Specify SQLite database by absolute path (Bojan Smojver)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Jon Ciesla <limburgher@gmail.com> - 1.8.0-1
- Latest upstream.
- Migrate to ssytemd, BZ 722356.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.7.6-1
- fix license tag
- update to 1.7.6

* Mon Mar 12 2007 Steven Pritchard <steve@kspei.com> 1.7.5-1
- Update to 1.7.5
- Drop fedora-usermgmt requirement
- Don't remove the sqlgrey user on uninstall

* Thu Dec 14 2006 Steven Pritchard <steve@kspei.com> 1.7.4-5
- Add missing echos to init script

* Wed Dec 13 2006 Steven Pritchard <steve@kspei.com> 1.7.4-4
- Add more docs

* Tue Dec 12 2006 Steven Pritchard <steve@kspei.com> 1.7.4-3
- Change default database to SQLite
- Require DBD::SQLite
- Own (ghost) SQLite db file
- Clean up post/postun scripts a bit
- Quiet bogus variable used once warnings

* Tue Aug 29 2006 Steven Pritchard <steve@kspei.com> 1.7.4-2
- Change home directory to /var/lib/sqlgrey and create it
- Include our own init script
- Explicitly require postfix
- Drop inconsistent name macro usage

* Tue Aug 29 2006 Steven Pritchard <steve@kspei.com> 1.7.4-1
- Update to 1.7.4
- Own _sysconfdir/sqlgrey and all .regexp files in it
- Handle the service in post/preun/postun scripts
- Random spec cleanup

* Mon Apr 17 2006 Warren Togami <wtogami@redhat.com> 1.7.3-2
- Convert to fedora-usermgmt
- Spec cleanup to Fedora guidelines

* Wed Nov 16 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.7.3 release
- fixes for a crash with '*' in email adresses

* Tue Oct 25 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.7.2 release
- fixes for several errors in logging
- clean_method ported from 1.6.x

* Thu Sep 15 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.7.1 release
- fix for race condition in multiple instances configurations
- fix for weekly stats

* Tue Jun 21 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.7.0 release
- now continue if the DB isn't available at startup time
- based on 1.6.0 with Michel Bouissou's work:
  . better connect cleanup when creating AWL entries
  . source IP throttling

* Thu Jun 16 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.6.0 release
- fix for alternate conf_dir
- fix for timestamp handling in log parser
- log parser cleanup
- added README.PERF and documentation cleanup

* Tue Jun 07 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.9 release
- fix for MySQL's mishandling of timestamps
- better log parser

* Thu Jun 02 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.8 release
- fix for Makefile: rpmbuild didn't work

* Wed Jun 01 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.7 release
- fix for a memory leak
- config directory now user-configurable
- preliminary log analyser

* Mon May 02 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.6 release
- fix for MySQL disconnection crash
- IPv6 support
- Optin/optout support

* Mon Apr 25 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.5 release
- small fix for SRS (again!)
- small fix for deverp code
- log types

* Tue Mar 15 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.4 release
- fix for regexp compilation (regexp in fqdn_whitelists didn't work)
  
* Sat Mar 05 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.3 release
- the cleanup is now done in a separate process to avoid stalling the service

* Thu Mar 03 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.2 release
- optimize SQL queries by avoiding some now() function calls

* Wed Mar 02 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.1 release
- replaced smart algorithm with Michel Bouissou's one

* Wed Feb 23 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.5.0 release
- drop support for obsolete command-line parameters
- migrate databases to a new layout :
  . first_seen added to the AWLs
  . optimize AWL Primary Keys
  . add indexes

* Mon Feb 21 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.8 release
- AWL performance bugfix
- bad handling of database init errors fixed
   
* Fri Feb 18 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.7 release
- MAIL FROM: <> bugfix
  
* Fri Feb 18 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.6 release
- update_sqlgrey_whitelists fix
- removed superfluous regexp in deVERP code

* Thu Feb 17 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.5 release
- update_sqlgrey_whitelists temporary directory fixes from Michel Bouissou
- return code configurable patch from Michel Bouissou
- VERP and SRS tuning, with input from Michel Bouissou
- VERP and SRS normalisation is used only in the AWLs

* Mon Feb 14 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.4 release
- Autowhitelists understand SRS
- more VERP support for autowhitelists
- SQLgrey can warn by mail when the database is unavailable
- update_sqlgrey_whitelists doesn't rely on mktemp's '-t' parameter anymore.

* Sun Feb 06 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.3 release
- log to stdout when not in daemon mode
- added update_sqlgrey_whitelists script
  whitelists can now be fetched from repositories
      
* Thu Jan 13 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.2 release
- Better cleanup logging from Rene Joergensen
- Fix for Syslog.pm error messages at init time
- Fix doc packaging in RPM

* Tue Jan 11 2005 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.1 release
- fix for invalid group id messages from Øystein Viggen
- allow reloading whitelists with SIGUSR1
- db_maintdelay user-configurable
- don't log pid anymore

* Fri Dec 10 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.4.0 release
- windows for SQL injection fix (reported by Øystein Viggen)
- spec file tuning inspired by Derek Battams

* Tue Nov 30 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.3.6 release
- whitelist for FQDN as well as IP
- 3 different greylisting algorithms
  (RFE from Derek Battams)

* Mon Nov 22 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.3.4 release
- ip whitelisting

* Mon Nov 22 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.3.3 release
- preliminary whitelist support

* Wed Nov 17 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.3.2 release
- RPM packaging fixed
- DB connection pbs don't crash SQLgrey anymore

* Thu Nov 11 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.3.0 release
- Database schema slightly changed,
- Automatic database schema upgrade framework

* Sun Nov 07 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.2.0 release
- SQL code injection protection
- better DBI error reporting
- better VERP support
- small log related typo fix
- code cleanups

* Mon Oct 11 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.1.2 release
- pidfile handling code bugfix

* Mon Sep 27 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.1.1 release
- MySQL-related SQL syntax bugfix

* Tue Sep 21 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.1.0 release
- SQLite support (RFE from Klaus Alexander Seistrup)

* Tue Sep 14 2004 Lionel Bouton <lionel-dev@bouton.name>
- 1.0.1 release
- man page cleanup

* Tue Sep 07 2004 Lionel Bouton <lionel-dev@bouton.name>
- pushed default max-age from 12 to 24 hours

* Sat Aug 07 2004 Lionel Bouton <lionel-dev@bouton.name>
- bug fix for space trimming values from database

* Tue Aug 03 2004 Lionel Bouton <lionel-dev@bouton.name>
- trim spaces before logging possible spams
- v1.0 added license reference at the top
  at savannah request

* Fri Jul 30 2004 Lionel Bouton <lionel-dev@bouton.name>
- Bugfix: couldn't match on undefined sender
- debug code added

* Fri Jul 30 2004 Lionel Bouton <lionel-dev@bouton.name>
- Removed NetAddr::IP dependency at savannah request

* Sat Jul 17 2004 Lionel Bouton <lionel-dev@bouton.name>
- Default max-age pushed to 12 hours instead of 5
  (witnessed more than 6 hours for a mailing-list subscription
  system)

* Fri Jul 02 2004 Lionel Bouton <lionel-dev@bouton.name>
- Documentation

* Thu Jul 01 2004 Lionel Bouton <lionel-dev@bouton.name>
- PostgreSQL support added

* Tue Jun 29 2004 Lionel Bouton <lionel-dev@bouton.name>
- various cleanups and bug hunting

* Mon Jun 28 2004 Lionel Bouton <lionel-dev@bouton.name>
- 2-level AWL support

* Sun Jun 27 2004 Lionel Bouton <lionel-dev@bouton.name>
- Initial Version, replaced BDB by mysql in postgrey
