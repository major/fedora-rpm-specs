Name:           MySQL-zrm
Version:        3.0
Release:        43%{?dist}
Summary:        MySQL backup manager

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.zmanda.com/backup-mysql.html
Source0:        http://www.zmanda.com/downloads/community/ZRM-MySQL/3.0/Source/MySQL-zrm-%{version}-release.tar.gz
Source1:        MySQL-zrm.service
Source2:        MySQL-zrm.socket
# Really make --quiet quiet
Patch0:         MySQL-zrm-quiet.patch
# Abort if out of space on restore
# https://forums.zmanda.com/showthread.php?5347-mysql-zrm-restore-does-not-check-for-running-out-of-disk-space&p=17076#post17076
Patch1:         MySQL-zrm-tmpwrite.patch
# Enable exclude-pattern with logical backups
# https://forums.zmanda.com/showthread.php?5371-Support-exclude-patter-for-logical-backups-exclude-information_schema
Patch2:         MySQL-zrm-exclude.patch
# Do not fail if mysqldump emits warnings
# https://forums.zmanda.com/showthread.php?5102-How-to-report-bugs
Patch3:         MySQL-zrm-mysqldump-warnings.patch
# Do not use --same-order with -c
# https://bugzilla.redhat.com/show_bug.cgi?id=1458038
Patch4:         MySQL-zrm-taropt.patch
# Check exit status of all commands in pipes
# https://bugzilla.redhat.com/show_bug.cgi?id=1151623
Patch5:         MySQL-zrm-pipestatus.patch
# Remove duplicate command logging
Patch6:         MySQL-zrm-command-log.patch
# Avoid "tar: .: file changed as we read it" by touching the output file first
Patch7:         MySQL-zrm-tar.patch

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  systemd

Requires:       logrotate
Requires:       /usr/bin/mail
Requires:       perl(DBI)
Requires:       perl(XML::Parser)
Requires:       perl(Data::Report) >= 0.05 
Requires:       perl(Data::Report::Plugin::Html) 
Requires:       perl(Data::Report::Plugin::Text) 
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
Easy-to-use yet flexible and robust backup and recovery solution for MySQL 
server.

%prep
%setup -q -c
# Cannot do backups, they get installed
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
# FIx permissions
find -name \*.pm -o -name \*.smf | xargs chmod -x
# Fix FSF address
find -type f | xargs sed -i \
  -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/'


%build
# we should use modules from repo
rm -rf usr/lib/mysql-zrm/Data
rm -rf usr/lib/mysql-zrm/XML

# get rid of zero-length files
rm -rf var/log/mysql-zrm/*


%install
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{_docdir}
mkdir -p %{buildroot}%{_mandir}/man{1,5}
mkdir -p %{buildroot}%{_sharedstatedir}
mkdir -p %{buildroot}%{_var}/log
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_sysconfdir}/mysql-zrm
mkdir -p %{buildroot}%{_unitdir}

# install ourselves in correct locations
cp -rp usr/lib/mysql-zrm/ZRM                    %{buildroot}%{perl_vendorlib}
cp -rp usr/share/doc/%{name}-%{version}         %{buildroot}%{_docdir}/%{name}
cp -rp usr/share/man/man1/*                     %{buildroot}%{_mandir}/man1/
cp -rp usr/share/man/man5/*                     %{buildroot}%{_mandir}/man5/
cp -rp var/lib/*                                %{buildroot}%{_sharedstatedir}
cp -rp var/log/*                                %{buildroot}%{_var}/log/
cp -rp usr/share/mysql-zrm                      %{buildroot}%{_datadir}/
cp -rp usr/bin/*                                %{buildroot}%{_bindir}/
cp -rp etc/mysql-zrm                            %{buildroot}%{_sysconfdir}/
# name logrotate job as package name
cp -rp etc/logrotate.d/mysql-zrm                %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
cp -p %SOURCE1 %SOURCE2                         %{buildroot}%{_unitdir}

# This will store passwords, restrict permissions
chmod 640 %{buildroot}%{_sysconfdir}/mysql-zrm/mysql-zrm.conf


%post
%systemd_post MySQL-zrm.service

%preun
%systemd_preun MySQL-zrm.service

%postun
%systemd_postun_with_restart MySQL-zrm.service


%files
%attr(-,mysql,mysql) %dir %{_var}/log/mysql-zrm
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/mysql-zrm/
%{_sharedstatedir}/mysql-zrm/
%{_datadir}/mysql-zrm/
%attr(0755,root,root) %{_bindir}/*
%{perl_vendorlib}/ZRM
%attr(0644,root,root) %{_unitdir}/*
%{_docdir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/man5/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0-42
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Orion Poplawski <orion@nwra.com> - 3.0-38
- Add patch to fix tar complaining that ". changed as we read it"

* Thu Oct 12 2023 Orion Poplawski <orion@nwra.com> - 3.0-37
- Require /usr/bin/mail instead of mailx

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-33
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-30
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0-29
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-26
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-25
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-22
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-19
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Orion Poplawski <orion@cora.nwra.com> - 3.0-17
- Fix logging of backup command

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Orion Poplawski <orion@cora.nwra.com> - 3.0-15
- Check exit status of all commands in pipes (bug #1151623)
- Do not use --same-order with -c for tar (bug #1458038)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-14
- Perl 5.26 rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-13
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-11
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-8
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-7
- Perl 5.20 rebuild

* Fri Jul 25 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0-6
- Add patch to prevent error exit codes with mysqldump output

* Tue Jul 22 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0-5
- Add requires mailx
- Fix file ownership
- Fix FSF address
- Rebase queit patch

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 3 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0-3
- Add patch to enable exclude-pattern with logical backups

* Wed Mar 19 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0-2
- Abort if out of space on restore

* Tue Mar 18 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0-1
- Update to 3.0

* Fri Aug 02 2013 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-15
- Fix up doc (and other) install

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 2.2.0-14
- Perl 5.18 rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.2.0-13
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-11
- Use new systemd macros (bug 850223)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 2.2.0-9
- Perl 5.16 rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 4 2011 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-7
- Update quiet patch to fix bug 759854

* Tue Nov 22 2011 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-6
- Restrict permissions on mysql-zrm.conf

* Wed Nov 9 2011 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-5
- Add quiet patch to silence output with --quiet
- Move to systemd socket activation from xinetd (bug 737258)

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.0-4
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.0-3
- Perl 5.14 mass rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 15 2010 Michal Ingeli <mi@v3.sk> - 2.2.0-1
- Upgrade to 2.2.0 (bz#633912)

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.1.1-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.1.1-6
- rebuild against perl 5.10.1

* Mon Oct 12 2009 <mi@v3.sk> - 2.1.1-5
- replaced _datarootdir for _datadir

* Fri Oct 9 2009 <mi@v3.sk> - 2.1.1-4
- Removed uneeded dependencies
- Replaced /var/lib with macro

* Fri Oct 9 2009 <mi@v3.sk> - 2.1.1-3
- Removed repeated file attr-s
- Disabled mysql-zrm-socket-server by default
- Changed owner of our /var/log/* to mysql:mysql
- Corrected documentation handling

* Wed Oct 7 2009 <mi@v3.sk> - 2.1.1-2
- corrected license
- minnor changes

* Fri Oct 2 2009 <mi@v3.sk> - 2.1.1-1
- Initial packaging
