Name: fetch-crl
Version: 3.0.22
Release: 5%{?dist}
Summary: Downloads Certificate Revocation Lists

License: ASL 2.0
URL: https://wiki.nikhef.nl/grid/FetchCRL3
Source0: https://dist.eugridpma.info/distribution/util/fetch-crl3/fetch-crl-%{version}.tar.gz

# systemd files.
Source1: fetch-crl.service
Source2: fetch-crl.timer

BuildArch: noarch

Requires: openssl
%if 0%{?el7}
Requires: perl(File::Basename)
Requires: perl(File::Temp)
Requires: perl(Getopt::Long)
Requires: perl(IO::Select)
Requires: perl(IPC::Open3)
Requires: perl(LWP)
Requires: perl(POSIX)
Requires: perl(Sys::Syslog)
Requires: perl(Time::Local)
%endif

Requires: perl(LWP::Protocol::https)

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildRequires:    perl-generators
BuildRequires:    systemd
BuildRequires: make

%description
This tool and associated timer entry ensure that Certificate Revocation
Lists (CRLs) are periodically retrieved from the web sites of the respective
Certification Authorities.
It assumes that the installed CA files follow the hash.crl_url convention.

%prep
%setup -q
cp -p %{SOURCE1} fetch-crl.service
cp -p %{SOURCE2} fetch-crl.timer

# The perl script contains some modules inside of
# it. These end up being rpm required but are
# not rpm provided. This is quite correct since they
# are private to this script.
# Consequence we must filter the requires of the script.
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(CRL)/d' |\
sed -e '/perl(CRLWriter)/d' |\
sed -e '/perl(ConfigTiny)/d' |\
sed -e '/perl(FCLog)/d' |\
sed -e '/perl(OSSL)/d' |\
sed -e '/perl(TrustAnchor)/d' |\
sed -e '/perl(base64)/d'
EOF

%global __perl_requires %{_builddir}/fetch-crl-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
# Nothing to build.

%install
make install PREFIX=$RPM_BUILD_ROOT%{_usr} ETC=$RPM_BUILD_ROOT%{_sysconfdir} CACHE=$RPM_BUILD_ROOT%{_var}/cache
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644  %{name}.service $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -p -m 644  %{name}.timer $RPM_BUILD_ROOT%{_unitdir}/%{name}.timer

# Remove some files that have been duplicated as docs.
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%post
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.timer

%postun
%systemd_postun_with_restart %{name}.timer

%files
%{_sbindir}/%{name}
%{_sbindir}/clean-crl
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%dir %{_var}/cache/%{name}
%dir %{_sysconfdir}/grid-security
%dir %{_sysconfdir}/grid-security/certificates
%dir %{_sysconfdir}/%{name}.d
%doc %{_mandir}/man8/%{name}.8.gz
%doc %{_mandir}/man8/clean-crl.8.gz
%doc CHANGES NOTICE README fetch-crl.cnf.example
%config(noreplace) %{_sysconfdir}/%{name}.conf
%license LICENSE

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Steve Traylen <steve.traylen@cern.ch> - 3.0.22-1
- Update to version 3.0.22

* Mon Aug 02 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.0.21-3
- rhbz#1983391 - Fix broken timer unit file with new systemd

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 8 2021 Steve Traylen <steve.traylen@cern.ch> - 3.0.21-1
- Update version extra perl R for https

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.20-10
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Steve Traylen <steve.traylen@cern.ch> - 3.0.20-6
- Mark License file as %%license.

* Fri Oct 11 2019 Steve Traylen <steve.traylen@cern.ch> - 3.0.20-5
- Fix bogus date in changelog

* Fri Oct 11 2019 Steve Traylen <steve.traylen@cern.ch> - 3.0.20-4
- Fix bogus date in changelog

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Steve Traylen <steve.traylen@cern.ch> - 3.0.20-2
- Change cron for timer in description.

* Fri Jul 5 2019 Steve Traylen <steve.traylen@cern.ch> - 3.0.20-1
- Update to 3.0.20
- rhbz#1719355 - actually run timer every six hours
- Update URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Steve Traylen <steve.traylen@cern.ch>
- Migrate from cron to a systemd timer.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Steve Traylen <steve.trayen@cern.ch> - 3.0.19-1
- Remove .el6 and SysV support.
- New version 3.0.19.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Steve Traylen <steve.trayen@cern.ch> - 3.0.17-3
- rhbz#1299141 - Use enviroment file with -boot service.

* Mon Jan 18 2016 Steve Traylen <steve.trayen@cern.ch> - 3.0.17-2
- Perl dependencies corrected for el6 and el7.

* Thu Dec 17 2015 Steve Traylen <steve.trayen@cern.ch> - 3.0.17-1
- New version 3.0.17.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 1 2015 Steve Traylen <steve.trayen@cern.ch> - 3.0.16-1
- New version 3.0.16.

* Fri Jun 13 2014 Steve Traylen <steve.trayen@cern.ch> - 3.0.14-1
- New version 3.0.14.

* Fri Jun 13 2014 Steve Traylen <steve.trayen@cern.ch> - 3.0.13-1
- /etc/grid-security/certificates should be in package.
- Remove some obsolete RHEL5 items.
- Use new systemd macros rhbz#850108.
- New version 3.0.13.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 6 2013 Steve Traylen <steve.trayen@cern.ch> - 3.0.11-4
- rhbz#993749 Adapted for unversioned docs dir.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Steve Traylen <steve.trayen@cern.ch> - 3.0.11-2
- Update to 3.0.11
- Change BR to systemd from sytemd-units.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.0.8-6
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 1 2012 Steve Traylen <steve.traylen@cern.ch> - 3.0.8-2
- Add systemd support.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Steve Traylen <steve.traylen@cern.ch> - 3.0.8-1
- Upstream to 3.0.8.

* Tue Jun 28 2011 Steve Traylen <steve.traylen@cern.ch> - 3.0.7-1
- Upstream to 3.0.7.
- Remove manual perl requires since worked around upstream rhbs#699548

* Sun Mar 20 2011 Steve Traylen <steve.traylen@cern.ch> - 3.0.6-2
- Add lots of perl dependencies to workaround rhbz#699548.
- Remove false requirement on wget.

* Sun Mar 20 2011 Steve Traylen <steve.traylen@cern.ch> - 3.0.6-1
- Upstream to 3.0.6.

* Sun Feb 13 2011 Steve Traylen <steve.traylen@cern.ch> - 3.0.5-1
- Upstream to 3.0.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Steve Traylen <steve.traylen@cern.ch> - 3.0.4-2
- For EPEL6 obsolete EPEL5's fetch-crl3 package.

* Thu Oct 14 2010 Steve Traylen <steve.traylen@cern.ch> - 3.0.4-1
- New upstream 3.0.4
- Add empty directory /etc/fetch-crl.d since this is now supported.

* Thu Oct 14 2010 Steve Traylen <steve.traylen@cern.ch> - 3.0.3-1
- New upstream 3.0.3

* Mon Aug 16 2010 Steve Traylen <steve.traylen@cern.ch> - 3.0.0-2
- License changed from EU Datagrid to Apache 2 license.

* Mon Aug 16 2010 Steve Traylen <steve.traylen@cern.ch> - 3.0.0-1
- Add new /var/cache/fetch-crl directory package.
- Change homepage to new homepage.
- Filter out autogenerated requires that are actually internal.
- fetch-crl.cron and fetch-crl.sysconfig no longer created.
- Set new variable CACHE explicity.
- Remove fetch-crl-2.8.4-mktemp.patch, since upstream now.
- New upstream. 3.0.0-1

* Tue Apr 20 2010 Steve Traylen <steve.traylen@cern.ch> - 2.8.4-2
- Add fetch-crl-2.8.4-mktemp.patch. rhbz#407851, Jason Smith @ BNL.


