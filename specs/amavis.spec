# SNMP enabled by default
%bcond_without snmp

Summary:        Email filter with virus scanner and spamassassin support
Name:           amavis
Version:        2.13.1
Release:        3%{?dist}
# LDAP schema is GFDL-1.2-or-later, some helpers are BSD-2-Clause, core is GPL-2.0-or-later
License:        GPL-2.0-or-later AND BSD-2-Clause AND GFDL-1.2-or-later
URL:            https://gitlab.com/amavis/amavis
Source0:        https://gitlab.com/amavis/amavis/-/archive/v%{version}/amavis-v%{version}.tar.bz2
Source2:        amavis-clamd.conf
Source4:        README.fedora
Source5:        README.quarantine
Source8:        amavisd-tmpfiles.conf
Source9:        amavisd.service
Source10:       amavisd-snmp.service
Source11:       amavis.sysusers
Source12:       amavisd.sysconfig
Patch0:         amavis-conf.patch
BuildArch:      noarch
%if 0%{?fedora}
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
%if 0%{?rhel} > 7 || 0%{?fedora} > 24
Suggests:       %{name}-doc
Recommends:     clamav-server-systemd
Recommends:     clamav
Recommends:     binutils
Recommends:     arj
Recommends:     bzip2
Recommends:     cabextract
Recommends:     pax
Recommends:     freeze
Recommends:     gzip
Recommends:     lzop
Recommends:     nomarch
Recommends:     p7zip, p7zip-plugins
Recommends:     tar
Recommends:     unzoo
Recommends:     perl(DBD::SQLite)
Recommends:     perl(Convert::TNEF)
Recommends:     perl(Convert::UUlib)
%else
Requires:       binutils
Requires:       arj
Requires:       bzip2
Requires:       cabextract
Requires:       pax
Requires:       freeze
Requires:       gzip
Requires:       lzop
Requires:       nomarch
Requires:       p7zip, p7zip-plugins
Requires:       tar
Requires:       unzoo
Requires:       perl(DBD::SQLite)
%endif
Requires:       perl-Amavis = %{version}-%{release}
Requires:       clamav-filesystem
Requires:       altermime
Requires:       file
Requires:       perl(Archive::Tar)
Requires:       perl(Authen::SASL)
Requires:       perl(Compress::Raw::Zlib) >= 2.017
Requires:       perl(File::LibMagic)
Requires:       perl(IO::Socket::IP)
Requires:       perl(MIME::Body)
Requires:       perl(MIME::Decoder::Base64)
Requires:       perl(MIME::Decoder::Binary)
Requires:       perl(MIME::Decoder::Gzip64)
Requires:       perl(MIME::Decoder::NBit)
Requires:       perl(MIME::Decoder::QuotedPrint)
Requires:       perl(MIME::Decoder::UU)
Requires:       perl(MIME::Head)
Requires:       perl(Mail::Field)
Requires:       perl(Mail::Header)
Requires:       perl(Mail::Internet) >= 1.58
Requires:       perl(Mail::SPF)
Requires:       perl(Net::DNS)
Requires:       perl(Net::LibIDN2)
Requires:       perl(Net::SSLeay)
Requires:       perl(NetAddr::IP)
Requires:       perl(Razor2::Client::Version)
Requires:       perl(Socket)
Requires:       perl(URI)
Obsoletes:      amavisd-new-zeromq <= 2.11.0-5
Obsoletes:      amavisd-new-snmp-zeromq <= 2.11.0-5
Provides:       amavisd-new = %{version}-%{release}
Obsoletes:      amavisd-new < 2.12.0-3

%package -n perl-Amavis
Summary:        Amavis perl module

%if %{with snmp}
%package snmp
Summary:        Exports amavis SNMP data
Requires:       %{name} = %{version}-%{release}
Provides:       amavisd-new-snmp = %{version}-%{release}
Obsoletes:      amavisd-new-snmp < 2.12.0-3
%endif

%package doc
Summary:        Amavis doc files
Provides:       amavisd-new-doc = %{version}-%{release}
Obsoletes:      amavisd-new-doc < 2.12.0-3

%description -n perl-Amavis
Amavis perl module used by the amavis mail scanner service.

%description
amavis is a high-performance and reliable interface between mailer
(MTA) and one or more content checkers: virus scanners, and/or
Mail::SpamAssassin Perl module. It is written in Perl, assuring high
reliability, portability and maintainability. It talks to MTA via (E)SMTP
or LMTP, or by using helper programs. No timing gaps exist in the design
which could cause a mail loss.

%if %{with snmp}
%description snmp
This package contains the program amavisd-snmp-subagent, which can be
used as a SNMP AgentX, exporting amavisd statistical counters database
(snmp.db) as well as a child process status database (nanny.db) to a
SNMP daemon supporting the AgentX protocol (RFC 2741), such as NET-SNMP.

It is similar to combined existing utility programs amavisd-agent and
amavisd-nanny, but instead of writing results as text to stdout, it
exports data to a SNMP server running on a host (same or remote), making
them available to SNMP clients (such a Cacti or mrtg) for monitoring or
alerting purposes.
%endif

%description doc
Documentation files for amavis

%prep
%autosetup -p1 -n %{name}-v%{version}
install -p -m 644 %{SOURCE4} %{SOURCE5} README_FILES/

%build

%install
mkdir -p -m 0755 %{buildroot}%{perl_vendorlib}
cp -pr lib/* %{buildroot}%{perl_vendorlib}/

install -D -p -m 755 bin/amavisd %{buildroot}%{_sbindir}/amavisd
%if %{?with_snmp}
install -D -p -m 755 bin/amavisd-snmp-subagent %{buildroot}%{_sbindir}/amavisd-snmp-subagent
%endif

mkdir -p %{buildroot}%{_bindir}
install -p -m 755 bin/amavisd-{agent,nanny,release,signer,submit} %{buildroot}%{_bindir}/

install -D -p -m 644 %{SOURCE9} %{buildroot}%{_unitdir}/amavisd.service
%if %{with snmp}
install -D -p -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/amavisd-snmp.service
%endif

mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/clamd.d
install -D -p -m 644 conf/amavisd.conf %{buildroot}%{_sysconfdir}/amavisd/amavisd.conf
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/clamd.d/amavisd.conf

mkdir -p %{buildroot}%{_localstatedir}/spool/amavisd/{tmp,db,quarantine}
mkdir -p %{buildroot}%{_rundir}/{clamd.amavisd,amavisd}

install -D -m 644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/amavisd.conf

install -p -D -m 0644 %{SOURCE11} %{buildroot}%{_sysusersdir}/amavis.conf

install -p -D -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/sysconfig/amavisd

%pre
%sysusers_create_compat %{SOURCE11}

%preun
%systemd_preun amavisd.service

%if %{with snmp}
%preun snmp
%systemd_preun amavisd-snmp.service
%endif

%post
%systemd_post amavisd.service

%if %{with snmp}
%post snmp
%systemd_post amavisd-snmp.service
%endif

%postun
%systemd_postun_with_restart amavisd.service

%if %{with snmp}
%postun snmp
%systemd_postun_with_restart amavisd-snmp.service
%endif

%files
%license LICENSE
%dir %{_sysconfdir}/amavisd/
%{_unitdir}/amavisd.service
%dir %{_sysconfdir}/clamd.d
%config(noreplace) %{_sysconfdir}/amavisd/amavisd.conf
%config(noreplace) %{_sysconfdir}/clamd.d/amavisd.conf
%{_sbindir}/amavisd
%{_bindir}/amavisd-agent
%{_bindir}/amavisd-nanny
%{_bindir}/amavisd-release
%{_bindir}/amavisd-signer
%{_bindir}/amavisd-submit
%dir %attr(750,amavis,amavis) %{_localstatedir}/spool/amavisd
%dir %attr(750,amavis,amavis) %{_localstatedir}/spool/amavisd/tmp
%dir %attr(750,amavis,amavis) %{_localstatedir}/spool/amavisd/db
%dir %attr(750,amavis,amavis) %{_localstatedir}/spool/amavisd/quarantine
%{_tmpfilesdir}/amavisd.conf
%{_sysusersdir}/amavis.conf
%dir %attr(755,amavis,amavis) %{_rundir}/amavisd
%dir %attr(770,amavis,clamupdate) %{_rundir}/clamd.amavisd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/amavisd

%files -n perl-Amavis
%license LICENSE
%{perl_vendorlib}/*

%if %{with snmp}
%files snmp
%doc AMAVIS-MIB.txt
%{_unitdir}/amavisd-snmp.service
%{_sbindir}/amavisd-snmp-subagent
%endif

%files doc
%license LICENSE
%doc AAAREADME.first contrib/LDAP.schema contrib/LDAP.ldif RELEASE_NOTES TODO
%doc README_FILES conf/amavisd.conf-* conf/amavisd-custom.conf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Juan Orti Alcaine <jortialc@redhat.com> - 2.13.1-1
- Update to version 2.13.1

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 06 2023 Chris Adams <linux@cmadams.net> - 2.13.0-4
- Add a syconfig file to be able to add arguments

* Thu Feb 23 2023 Juan Orti Alcaine <jortialc@redhat.com> - 2.13.0-3
- Update configuration to use clamdscan

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Juan Orti Alcaine <jortialc@redhat.com> - 2.13.0-1
- Version 2.13.0 (RHBZ#2158819)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-10.git35407e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.12.2-9.git35407e9
- Perl 5.36 rebuild

* Mon May 30 2022 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.2-8.git35407e9
- Update to latest git snapshot

* Mon Apr 04 2022 Michal Josef Špaček <mspacek@redhat.com> - 2.12.2-7.gitb561924
- Remove dependency to Socket6, in Socket is support for IPv6 too

* Wed Mar 09 2022 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.2-6.gitb561924
- create perl-Amavis subpackage

* Tue Mar 08 2022 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.2-5.gitb561924
- Update to master branch
- Switch from Net:LibIDN to Net:LibIDN2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.2-3
- Remove perl(IO::Stringy) dependency

* Tue Oct 26 2021 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.2-2
- Create amavis user with systemd sysusers

* Fri Oct 22 2021 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.2-1
- Version 2.12.2 (#2013555)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.12.1-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.1-5
- Enable snmp subpackage in epel8 as net-snmp-perl is now available

* Fri Jan 01 2021 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.1-4
- Change /var/run for /run (#1910344)

* Tue Nov 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.1-3
- Change ports in configuration file and add a note about SELinux (#1891003)

* Tue Nov 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.1-2
- Disable snmp subpackage in epel8

* Tue Nov 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.1-1
- Version 2.12.1 (#1897574 #1851872)

* Tue Aug 18 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.0-9
- Drop unused dependency: perl(Digest::SHA1)
- Make optional: perl(Convert::TNEF), perl(Convert::UUlib)

* Tue Aug 18 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.0-8
- Unify Fedora and EPEL >= 7 spec files

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.0-5
- Fix startup of clamd RHBZ#1756570

* Tue Sep 24 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.0-4
- Change /var/run for /run
- Remove INSTALL file

* Wed Aug 28 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.0-3
- Project renamed from amavisd-new to amavis

* Wed Aug 28 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.0-2
- Drop old patches

* Thu Aug 01 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.0-1
- Version 2.12.0
- Update patches
- Update project URL
- Create doc subpackage

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.1-3
- Drop tmpwatch dependency and use tmpfiles for directory cleanup

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.1-1
- Version 2.11.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Marcel Haerry <mh+fedora@scrit.ch> - 2.11.0-14
- Fix socket path for amavisd tools (RHBZ#1551203)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-12
- Modify service unit to honor user and group in config file

* Tue Dec 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-11
- Remove lrzip from config
- Use weak dependencies where possible

* Sun Sep 03 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-10
- Remove lrzip dependency

* Fri Aug 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-9
- Disable Avast antivirus in config file (RHBZ#1480861)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-7
- PrivateDevices=true was causing problems with SELinux transitions

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-5
- Drop subpackages which depend on the deprecated ZMQ::LibZMQ3 library (RHBZ#1394697)

* Thu Aug 18 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-4
- Add patch to fix detection of originating emails (RHBZ#1364730)

* Thu Jun 30 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-3
- Additional systemd hardening (RHBZ#1351354)

* Mon Jun 20 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-2
- Remove NoNewPrivileges from service unit (RHBZ#1346766)

* Wed Apr 27 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.0-1
- Version 2.11.0 (RHBZ#1330781)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.10.1-6
- Make clamav a weak dependency and co-own /etc/clamd.d (RHBZ#1265922)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.10.1-4
- Move amavisd socket to /var/run/amavisd

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.10.1-3
- Use license macro

* Thu Feb 26 2015 Robert Scheck <robert@fedoraproject.org> - 2.10.1-2
- Replaced requirement to cpio by pax (upstream recommendation)

* Mon Oct 27 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1
- Patch5 merged upstream

* Sat Oct 25 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.10.0-2
- Improve conf patch to fix amavis-mc daemon
- Add patch to fix imports when SQL is used

* Thu Oct 23 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.10.0-1
- Update to 2.10.0
- Replace IO::Socket::INET6 with IO::Socket::IP
- Review perl dependencies minimum version
- Add subpackages amavisd-new-zeromq and amavisd-new-snmp-zeromq

* Mon Oct 20 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.10.0-0.1.rc2
- Update to 2.10.0-rc2

* Wed Aug 20 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.9.1-3
- Add ExecReload and Wants=postfix.service to systemd unit

* Sun Aug 03 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.9.1-2
- Add patch to fix releasing mail from sql quarantine

* Sat Jun 28 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.9.1-1
- New version 2.9.1

* Fri Jun 27 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.9.0-4
- Change permissions of /var/spool/amavisd folders to 750. Fix bug #906396

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.9.0-2
- Service unit files hardening

* Sun May 11 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.9.0-1
- Update to version 2.9.0
- Rework amavisd-conf.patch
- Enable and start timer units

* Wed Mar 19 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.8.1-3
- Use systemd timer units instead of cronjobs
- Add PrivateDevices to service unit

* Mon Feb 17 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.8.1-2
- Move clamd socket to /var/run/clamd.amavisd
- Add permissions to clamupdate to notify clamd

* Wed Feb 12 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.8.1-1
- Update to version 2.8.1
- Add systemd service units
- Add missing dependencies
- Start clamd using instantiated service
- Place tmpfiles conf in _tmpfilesdir
- Use _localstatedir macro

* Mon Dec 02 2013 Robert Scheck <robert@fedoraproject.org> - 2.8.0-8
- Commented ripole(1) decoder as the binary is not packaged
- Commented tnef(1) decoder as the perl module is a dependency

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.8.0-6
- Perl 5.18 rebuild

* Fri May 10 2013 Adam Williamson <awilliam@redhat.com> - 2.8.0-5
- init_network.patch: don't source /etc/sysconfig/network in initscript

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Robert Scheck <robert@fedoraproject.org> - 2.8.0-3
- Added requirements to lrzip and unzoo for unpacking

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Robert Scheck <robert@fedoraproject.org> - 2.8.0-1
- Upgrade to 2.8.0

* Fri Jun 29 2012 Robert Scheck <robert@fedoraproject.org> - 2.6.6-3
- Various minor spec file cleanups

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 18 2011 Steven Pritchard <steve@kspei.com> - 2.6.6-1
- Update to 2.6.6.
- Make /var/spool/amavisd g+x (BZ 548234).
- %%ghost /var/run/amavisd and add /etc/tmpfiles.d/amavisd-new-tmpfiles.conf
  (BZ 656544, 676430, 710984, 734271).
- Also add /var/run/clamd.amavisd (which seems to be a bug itself).  Fixes
  BZ 696725.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  9 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.4-2
- 561389 patch from Sandro Janke - change stderr to stdout

* Mon Aug 10 2009 Steven Pritchard <steve@kspei.com> - 2.6.4-1
- Update to 2.6.4.
- Make a snmp sub-package for amavisd-snmp-subagent.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Robert Scheck <robert@fedoraproject.org> - 2.6.2-3
- Re-diffed amavisd-new configuration patch for no fuzz

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Steven Pritchard <steve@kspei.com> - 2.6.2-1
- Update to 2.6.2.
- Drop smtpdaemon dependency (BZ# 438078).

* Tue Jul 15 2008 Steven Pritchard <steve@kspei.com> - 2.6.1-1
- Update to 2.6.1.
- Require Crypt::OpenSSL::RSA, Digest::SHA, Digest::SHA1, IO::Socket::SSL,
  Mail::DKIM, Net::SSLeay, NetAddr::IP, and Socket6.

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5.2-3
- fix license tag
- fix db patch to apply with fuzz=0

* Sun Aug 12 2007 Steven Pritchard <steve@kspei.com> - 2.5.2-2
- Fix pre/preun/post dependencies and improve scriptlets a bit.
- Drop dependencies on DBD::mysql and Mail::SPF::Query.
- Add dependencies on IO::Socket::INET6, Mail::SPF, and altermime.

* Sun Jul 08 2007 Steven Pritchard <steve@kspei.com> - 2.5.2-1
- Update to 2.5.2.

* Fri Jun 22 2007 Steven Pritchard <steve@kspei.com> - 2.5.2-0.1.rc2
- Update to 2.5.2-rc2.

* Fri Jun 22 2007 Steven Pritchard <steve@kspei.com> - 2.5.1-1
- Update to 2.5.1.
- Fix amavis-clamd.conf (bug #237252).
- Update amavisd-conf.patch.
- Require p7zip and tar.
- Improve pre/preun/post scripts.

* Thu Feb 22 2007 Steven Pritchard <steve@kspei.com> - 2.4.5-1
- Update to 2.4.5.

* Mon Dec 18 2006 Steven Pritchard <steve@kspei.com> - 2.4.4-2
- Fix the path to amavisd.sock in amavisd-release.

* Tue Dec 05 2006 Steven Pritchard <steve@kspei.com> - 2.4.4-1
- Update to 2.4.4.

* Fri Dec 01 2006 Steven Pritchard <steve@kspei.com> - 2.4.3-5
- Add missing amavisd-release script.

* Tue Nov 14 2006 Steven Pritchard <steve@kspei.com> - 2.4.3-4
- Rebuild.

* Tue Nov 14 2006 Steven Pritchard <steve@kspei.com> - 2.4.3-3
- Add dependency on file. (#215492)

* Sat Oct 14 2006 Steven Pritchard <steve@kspei.com> - 2.4.3-2
- Fix permissions on the cron.daily script.

* Tue Oct 10 2006 Steven Pritchard <steve@kspei.com> - 2.4.3-1
- Update to 2.4.3.
- Add quarantine directory and instructions for enabling it.
- Add tmpwatch cron script.

* Thu Sep 28 2006 Steven Pritchard <steve@kspei.com> - 2.4.2-4
- Drop lha dependency and add arj.

* Sun Sep 17 2006 Steven Pritchard <steve@kspei.com> - 2.4.2-3
- Rebuild.

* Wed Aug 02 2006 Steven Pritchard <steve@kspei.com> - 2.4.2-2
- Fix path to clamd socket in amavisd-conf.patch.

* Mon Jul 31 2006 Steven Pritchard <steve@kspei.com> - 2.4.2-1
- Update to 2.4.2
- Fix permissions on README.fedora (bug #200769)

* Tue Jun 20 2006 Steven Pritchard <steve@kspei.com> - 2.4.1-1
- Update to 2.4.1
- Drop zoo dependency due to Extras maintainer security concerns

* Tue Apr 25 2006 Steven Pritchard <steve@kspei.com> - 2.4.0-1
- Update to 2.4.0

* Thu Feb 02 2006 Steven Pritchard <steve@kspei.com> - 2.3.3-5
- Add dist to Release

* Wed Sep 21 2005 Steven Pritchard <steve@kspei.com> - 2.3.3-4
- Add TODO and amavisd.conf-* to %%doc

* Mon Sep 19 2005 Steven Pritchard <steve@kspei.com> - 2.3.3-3
- Add amavisd-db.patch to fix the path to the db directory in
  amavisd-agent and amavisd-nanny.  (Thanks to Julien Tognazzi.)

* Fri Sep 02 2005 Steven Pritchard <steve@kspei.com> - 2.3.3-2
- Requires: perl(Compress::Zlib) >= 1.35

* Thu Sep 01 2005 Steven Pritchard <steve@kspei.com> - 2.3.3-1
- Update to 2.3.3
- Remove explicit dependencies on core perl modules

* Fri Aug 19 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-10
- Recommend using 127.0.0.1 instead of localhost in README.fedora
- .deb support requires ar

* Wed Aug 17 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-9
- Set $virus_admin, $mailfrom_notify_admin, $mailfrom_notify_recip,
  and $mailfrom_notify_spamadmin to undef in the default config to
  turn off notification emails

* Fri Aug 12 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-8
- Add dependencies for freeze, lzop, nomarch, zoo, cabextract

* Wed Jul 27 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-7
- Add README.fedora with simplified Postfix instructions

* Mon Jul 25 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-6
- Create /var/spool/amavisd/db

* Thu Jul 21 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-5
- Add perl(Mail::SPF::Query) (now packaged for Extras) dependency
- Drop /var/log/amavisd since we weren't using it
- Fix paths for clamd.sock and amavisd.pid in a couple of places

* Tue Jul 12 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-4
- Add a bunch of other missing Requires (both actually required modules
  and optional modules)

* Tue Jul 12 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-3
- Add missing Requires: perl(Convert::TNEF)

* Wed Jul 06 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-2
- Fix init script ordering
- Don't enable amavisd by default

* Wed Jul 06 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-1
- Update to 2.3.2

* Wed Jun 29 2005 Steven Pritchard <steve@kspei.com> - 2.3.2-0.1.rc1
- Update to 2.3.2-rc1
- Fedora Extras clamav integration
- Drop amavisd-syslog.patch (Unix::Syslog is in Extras)

* Mon Feb 23 2004 Steven Pritchard <steve@kspei.com> - 0.20030616.p7-0.fdr.0.1
- Add amavisd-syslog.patch to eliminate Unix::Syslog dependency
- Add in clamd helper
- Fix up init script
- Initial package
