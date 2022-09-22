%global fwsnortlogdir /var/log/fwsnort

Summary: Translates Snort rules into equivalent iptables rules
Name: fwsnort
Version: 1.6.5
Release: 25%{?dist}
License: GPLv2+
Url: http://www.cipherdyne.org/%{name}/
Source0: http://www.cipherdyne.org/%{name}/download/%{name}-%{version}.tar.gz
Source1: logrotate.fwsnort
BuildArch: noarch 
BuildRequires: perl-generators
Requires: iptables
Requires: perl(NetAddr::IP)
Requires: perl(IPTables::Parse) 
Requires: logrotate 
Requires: wget
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
fwsnort translates Snort rules into equivalent iptables rules and generates
a Bourne shell script that implements the resulting iptables commands.

In addition, fwsnort (optionally) uses the IPTables::Parse module to parse the
iptables ruleset on the machine to determine which Snort rules are applicable
to the specific iptables policy.

fwsnort is able to translate approximately 60% of all rules from the
Snort-2.3.3 IDS into equivalent iptables rules. 

%prep
%setup -q 
mv deps/snort_rules/VERSION SNORT-RULES-VERSION
cp -p %SOURCE1 .

%build

%install
rm -rf $RPM_BUILD_ROOT
### log directory
mkdir -p $RPM_BUILD_ROOT%{fwsnortlogdir}

### fwsnort config
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT%{_sbindir}

install -m 755 fwsnort $RPM_BUILD_ROOT%{_sbindir}/
install -m 644 fwsnort.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
install -m 644 fwsnort.8 $RPM_BUILD_ROOT%{_mandir}/man8/

### install snort rules files
cp -r deps/snort_rules $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -p -m 644  logrotate.fwsnort $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

%pre
### not used

%post
### not used

%preun
### not used

%files
%doc LICENSE VERSION README CREDITS TODO SNORT-RULES-VERSION
%dir %{fwsnortlogdir}
%{_sbindir}/*
%{_mandir}/man8/*

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/fwsnort.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%dir %{_sysconfdir}/%{name}/snort_rules
%config(noreplace) %{_sysconfdir}/%{name}/snort_rules/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-24
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-21
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-18
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-17
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-14
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-11
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-8
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-6
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-3
- Perl 5.22 rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.5-2
- Perl 5.22 rebuild

* Tue Sep 09 2014 Guillermo Gómez <gomix@fedoraproject.org> - 1.6.5-1
- Updated version.

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.4-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Guillermo Gómez <gomix@fedoraproject.org> - 1.6.4-1
- CVE-2014-0039 fwsnort: configuration file can be loaded from
cwd when run as a non-root user

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.6.3-3
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Guillermo Gómez <gomix@fedoraproject.org> - 1.6.3-1
- Updated version.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.6.2-2
- Perl 5.16 rebuild

* Sun May 26 2012 Guillermo Gómez <gomix@fedoraproject.org> - 1.6.2-1
- Update to version 1.6.2
- Replaced Net::IPv4Addr with NetAddr::IP module which has support for IPv6
  address network parsing and comparisons.
- wget added as required to support default configuration.

* Fri Sep 02 2011 Guillermo Gómez <gomix@fedoraproject.org> - 1.6.1-1
- Update to version 1.6.1
- Bug fix for 'Couldn't load target' error
- Bug fix for fast_pattern interpretation for relative matches
- Updated to the latest Emerging Threats rule set

* Mon Aug 01 2011 Guillermo Gómez <gomix@fedoraproject.org - 1.6-1
- Update to major release version 1.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Guillermo Gomez <gomix@fedoraproject.org> - 1.5-0
- Upgrade to major release version 1.5-0
- WARNING: Compatibility issue with 1.0.6 fwsnort.conf, previous
  fwsnort.conf renamed as /etc/fwsnort/fwsnort.conf.rpmsave.

* Wed Dec 29 2010 Guillermo Gomez <gomix@fedoraproject.org>
- Upgrade to major prerelease version 1.5pre

* Tue Oct 12 2010 Mark Chappell <tremble@tremble.org.uk> - 1.0.6-8
- Replace the perl dependencies with the virtual modules rather than
  the package name

* Sun May 16 2010 Guillermo Gómez <ggomez@neotechgw.com> - 1.0.6-7
- Ownership of /etc/logrotate.d corrected and requires logrotate instead which
  provides it

* Sun Apr 25 2010 Guillermo Gómez <ggomez@neotechgw.com> - 1.0.6-6
- Macros use improved for consistency

* Thu Feb 04 2010 Guillermo Gómez <ggomez@neotechgw.com> - 1.0.6-5
- Removed unnecesary macro definition

* Thu Feb 04 2010 Guillermo Gómez <ggomez@neotechgw.com> - 1.0.6-4
- Description shortened

* Thu Feb 04 2010 Guillermo Gómez <ggomez@neotechgw.com> - 1.0.6-3
- License adjusted to GPLv2+

* Wed Feb 03 2010 Guillermo Gómez <ggomez@neotechgw.com> - 1.0.6-2
- documentation included, LICENSE VERSION README CREDITS TODO
  SNORT-RULES-VERSION

* Sat Jan 2 2010 Guillermo Gómez <ggomez@neotechgw.com> - 1.0.6-1
- First Fedora spec compliant version, several modifications
- No deps included
- Free snort rules included
