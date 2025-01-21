%global pkgname sysusage

Name:           sysusage
Version:        5.7
Release:        23%{?dist}
Summary:        System monitoring based on Perl, rrdtool, and sysstat
License:        GPL-3.0-or-later
URL:            https://sysusage.darold.net/
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{pkgname}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
Source2:        %{name}.cron
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Need them during building to determine the path.
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:  hostname
BuildRequires:  procps-ng
%else
BuildRequires:  net-tools
BuildRequires:  procps
%endif
BuildRequires:  sysstat
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-rsysusage = %{version}-%{release}
Requires:       crontabs
# For ping plugin (plugin-sample2.pl)
Requires:       perl(Time::HiRes)
Requires:       rrdtool
Requires:       sysstat
BuildArch:      noarch

%description
SysUsage continuously monitor your systems information and generate
periodic graphical reports using rrdtool or JavaScript jqplot library.
All reports are shown through a web interface.

SysUsage grabs all system activities using Sar and system commands allowing
you to keep tracks of your computer or server activity during its life.
It is a great help for performance analysis and resources management. The
threshold notification can alarm you when the system capabilities are
reached by sending SMTP messages or through Nagios reports.

By default it will monitor all you need to know on your server activity, it
is written in Perl and should works on all Unix like platforms. It doesn't
require a Database system like MySQL or PostgreSQL but relies on rrdtool. In
addition you can embedded your own plugins written in any programming language.

Since release 5.0 SysUsage can be run from a centralized place where
collected statistics will be stored and where graphics will be rendered.
Unlike other monitoring tools with lot of administration work, SysUsage is
design to have the least possible things to configure and a high level of admin
system knowledge. Each server can also be self monitored and you just have to
connect your browser to the web interface to know its health level.

SysUsage is design with simplicity in mind. providing all relevant statistics
from the servers within an intuitive web interface and without spending too
much time to configure it, if you know Nagios, you know what I mean. You will
especially like SysUsage for that.

%package        common
Summary:        Common files for %{name}

%description    common
This package provides common files shared between %{name}
and the rsysusage package

%package        httpd
Summary:        Apache configuration for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       httpd

%description    httpd
This package provides the Apache configuration for
applications using an Alias to %{name}.

%package        rsysusage
Summary:        Remote utility for %{name}
Requires:       %{name}-common = %{version}-%{release}
Requires:       sysstat

%description    rsysusage
This package provides the tools needed to run %{name}
on remote servers without needing to install sysusage
and it's dependencies.

%prep
%setup -qn %{pkgname}-%{version}

%build
perl Makefile.PL \
    INSTALLDIRS=vendor \
    QUIET=1 \
    BINDIR=%{_bindir} \
    CONFDIR=%{_sysconfdir} \
    PIDDIR=%{_localstatedir}/run \
    BASEDIR=%{_localstatedir}/lib/%{name} \
    PLUGINDIR=%{_datadir}/%{name}/plugins \
    HTMLDIR=%{_localstatedir}/www/%{name} \
    MANDIR=%{_mandir}/man1 \
    DOCDIR=%{_pkgdocdir} \
    DESTDIR='$DESTDIR'

make %{?_smp_mflags}

%install
export DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}

install -pDm644 %{S:1} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -pDm644 %{S:2} \
    %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -pDm644 doc/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1

# Remove redundant files.
find %{buildroot} -name perllocal.pod -type f -delete
find %{buildroot} -name .packlist -type f -delete

%files
%doc ChangeLog README TODO
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_bindir}/sysusage*
%{_datadir}/%{name}
%{_localstatedir}/www/%{name}
%{_mandir}/man1/%{name}.1*

%files common
%license LICENSE
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%dir %{_localstatedir}/lib/%{name}
%{perl_vendorlib}/SysUsage

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%files rsysusage
%{_bindir}/rsysusage

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.7-18
- Add BR perl-generators to automatically generates run-time dependencies

* Mon Nov 21 2022 Frank Crawford <frank@crawford.emu.id.au> - 5.7-17
- SPDX license update

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.7-15
- Perl 5.36 rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.7-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.7-9
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Frank Crawford <frank@crawford.emu.id.au> - 5.7-7
- Bump version due to koji/bodhi issue

* Wed Dec 25 2019 Frank Crawford <frank@crawford.emu.id.au> - 5.7-6
- Update for new HTTPS for URLs
- Initial build for EPEL-8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.7-4
- Perl 5.30 rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 22 2018 Frank Crawford <frank@crawford.emu.id.au> - 5.7-2
- Updated sample crontab to use sysusagejqgraph as sysusagegraph is deprecated

* Sat Sep 22 2018 Frank Crawford <frank@crawford.emu.id.au> - 5.7-1
- Upstream release 5.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.5-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.5-5
- Escape macros in %%changelog

* Tue Jan 09 2018 Frank Crawford <frank@crawford.emu.id.au> - 5.5-4
- Push to F27

* Tue Jul 18 2017 Frank Crawford <frank@crawford.emu.id.au> - 5.5-3
- Updated spec file to remove buildroot macro from the %%build step

* Sat Jul 15 2017 Frank Crawford <frank@crawford.emu.id.au> - 5.5-2
- Updated spec file with results from Fedora review

* Sun Feb 12 2017 Frank Crawford <frank@crawford.emu.id.au> - 5.5-1
- Upstream release 5.5

* Thu Dec 29 2016 Frank Crawford <frank@crawford.emu.id.au> - 5.4-1
- Upstream release 5.4

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.3-11
- Perl 5.24 rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.3-8
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.3-7
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 5.3-5
- Move www content to /var/www/sysusage (RHBZ # 1028722)

* Mon Nov 11 2013 Peter Robinson <pbrobinson@fedoraproject.org> 5.3-4
- Split rsysusage out to sub package
- Add a common subpackage for utils shared between rsysusage and main package

* Mon Nov 11 2013 Peter Robinson <pbrobinson@fedoraproject.org> 5.3-3
- Fix typo in sysusage-httpd.conf
- Add EL conditionals for some package deps to ease maintenance

* Fri Nov  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 5.3-2
- Fix localstatedir var for PID location

* Mon Aug 05 2013 Christopher Meng <rpm@cicku.me> - 5.3-1
- Major Upgrade(BZ#991637).
- Fix wrong cron Requires(BZ#989123).
- Fix broken httpd 2.4 configuration(BZ#871489).
- SPEC cleanup.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0:2.10-13
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0:2.10-11
- The requirement on vixie-cron is not correct anymore. The dailyjobs will be
  used as virtual requirement since now. #879550

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0:2.10-9
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0:2.10-7
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0:2.10-6
- Perl 5.14 mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0:2.10-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.10-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  2 2009 Rob Myers <rmyers@fedoraproject.org> 0:2.10-1
- include many fixes from Jason Corley (Thanks!)
- update to 2.10
- update url to reflect upstream change to sourcefourge
- add requirement on vixie-cron
- remove source1 in favor of now included in tarball config file
- change to installing apache config commented out
- change description to most recent website blurb
- change README.Fedora to README.RPM (for EPEL)
- fix cronjob

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 15 2008 Rob Myers <rob.myers@gtri.gatech.edu> 0:2.9-1
- update to 2.9
- move webdir /var/www/sysusage (resolves #465652)

* Wed Jul  2 2008 Rob Myers <rob.myers@gtri.gatech.edu> 0:2.6-4
- include missing versioned MODULE_COMPAT Requires (#453586)

* Thu Nov 15 2007 Rob Myers <rob.myers@gtri.gatech.edu> 0:2.6-3
- fix minor license issue
- add a default crontab entry
- add a default httpd configuration
- add README.Fedora

* Fri Nov  9 2007 Rob Myers <rob.myers@gtri.gatech.edu> 0:2.6-2
- seds really belong in prep

* Thu Nov  8 2007 Rob Myers <rob.myers@gtri.gatech.edu> 0:2.6-1
- move seds to build section
- remove perl requires
- update to 2.6

* Mon Jul 16 2007 Rob Myers <rob.myers@gtri.gatech.edu> 0:2.5-3
- define vname and wname in case this package should be renamed to
  perl-%%{uname}-%%{vname}

* Fri Jul 13 2007 Rob Myers <rob.myers@gtri.gatech.edu> 0:2.5-2
- change /var/db/sysusage to /var/lib/sysusage
- change perl_vendorarch to perl_vendorlib to build noarch
- update license
- add dist tag
- misc spec changes and/or cleanups

* Fri Jul  6 2007 Jason Corley <jason.corley@gmail.com> 0:2.5-1
- first packaging attempt

