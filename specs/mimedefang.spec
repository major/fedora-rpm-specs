Summary:        E-mail filtering framework using Sendmail's Milter interface
Name:           mimedefang
Version:        3.4.1
Release:        8%{?dist}
# {event{,_tcp}.{c,h},eventpriv.h} are GPL-2.0-or-later, rest is GPL-2.0-only
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://mimedefang.org/
Source0:        https://mimedefang.org/releases/%{name}-%{version}.tar.gz
Source1:        https://mimedefang.org/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/9F9B564003DFF9E4D904301E3B6DDB11E78FEBD2
Source3:        README.FEDORA
Source4:        mimedefang.service
Source5:        mimedefang-multiplexor.service
Source6:        mimedefang-wrapper
Source7:        mimedefang.tmpfilesd
Source8:        mimedefang.sysusersd
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Mail::DKIM)
BuildRequires:  perl(Mail::SPF)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(MIME::Tools) >= 5.410
BuildRequires:  perl(MIME::WordDecoder)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  systemd-rpm-macros
BuildRequires:  %{_sbindir}/sendmail
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  sendmail-milter-devel >= 8.12.0
Recommends:     perl(Mail::SpamAssassin) >= 1.6
%else
BuildRequires:  sendmail-devel >= 8.12.0
Requires:       perl(Mail::SpamAssassin) >= 1.6
%endif
Requires(post): perl(Digest::SHA)
%{?systemd_requires}
%{?sysusers_requires_compat}

# Testsuite in %%check
%if 0%{!?_without_tests:1}
BuildRequires:  %{_bindir}/prove
BuildRequires:  perl(HTML::Parser)
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  perl(Mail::DKIM::ARC::Signer) >= 0.44
%endif
BuildRequires:  perl(Mail::DKIM::Signer)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Most)
%endif

%description
MIMEDefang is an e-mail filter program which works with Sendmail 8.12
and later, or Postfix. It filters all e-mail messages sent via SMTP.
MIMEDefang splits multi-part MIME messages into their components and
potentially deletes or modifies the various parts. It then reassembles
the parts back into an e-mail message and sends it on its way.

There are some caveats users should be aware of before using MIMEDefang.
MIMEDefang potentially alters e-mail messages. This breaks a "gentleman's
agreement" that mail transfer agents do not modify message bodies. This
could cause problems, for example, with encrypted or signed messages.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
cp -pf %{SOURCE3} .

%build
%configure --with-milterlib=%{_libdir} --with-user=defang --disable-anti-virus
%make_build

%install
%make_install %{?el7:INSTALL='install -p'} INSTALL_STRIP_FLAG='' install-redhat

# Fix config file, create log directory and remove duplicate
sed -e '1d' -i $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/mail/sa-mimedefang.cf.example

# Install systemd unit files and tmpfiles
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/%{name}-multiplexor.service
install -D -p -m 0755 %{SOURCE6} $RPM_BUILD_ROOT%{_libexecdir}/%{name}-wrapper
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}

# Create a dummy file and install perl script for later executing
touch $RPM_BUILD_ROOT%{_sysconfdir}/mail/mimedefang-ip-key
sed -e '1s@^@#!%{_bindir}/perl\n@' gen-ip-validator.pl > gen-ip-validator.pl.new
install -m 0755 gen-ip-validator.pl.new $RPM_BUILD_ROOT%{_bindir}/gen-ip-validator.pl
touch -c -r gen-ip-validator.pl $RPM_BUILD_ROOT%{_bindir}/gen-ip-validator.pl

# Only for regression tests; depends on Test::Class, Test::Most and Net::SMTP
find $RPM_BUILD_ROOT \( -name Unit.pm -o -name "*::Unit.3" \) -exec rm -f {} \;

# ARC (Authenticated Received Chain) support requires Mail::DKIM >= 0.44
%if 0%{?rhel} == 7
rm -f t/arc.t
find $RPM_BUILD_ROOT \( -name ARC.pm -o -name "*::ARC.3" \) -exec rm -f {} \;
find $RPM_BUILD_ROOT%{_prefix} -type d -depth -exec rmdir {} 2> /dev/null \;
%endif

%if 0%{!?_without_tests:1}
%check
make test
%endif

%pre
%sysusers_create_compat %{SOURCE8}

%post
%systemd_post %{name}.service
if [ ! -f %{_sysconfdir}/mail/mimedefang-ip-key ]; then
  %{_bindir}/gen-ip-validator.pl > %{_sysconfdir}/mail/mimedefang-ip-key
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md README.{NONROOT,SECURITY,SOPHIE,SPAMASSASSIN,FEDORA}
%doc Changelog contrib/{word-to-html,linuxorg,fang.pl} examples/*filter*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/mail/mimedefang-filter
%ghost %config(noreplace) %{_sysconfdir}/mail/mimedefang-ip-key
%config(noreplace) %{_sysconfdir}/mail/sa-mimedefang.cf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/gen-ip-validator.pl
%{_bindir}/md-mx-ctrl
%{_bindir}/%{name}
%{_bindir}/%{name}.pl
%{_bindir}/%{name}-multiplexor
%{_bindir}/%{name}-release
%{_bindir}/%{name}-util
%{_bindir}/watch-%{name}
%{_bindir}/watch-multiple-%{name}s.tcl
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-multiplexor.service
%{_libexecdir}/%{name}-wrapper
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{perl_vendorlib}/Mail/MIMEDefang.pm
%{perl_vendorlib}/Mail/MIMEDefang/
%{_mandir}/man1/%{name}-util.1*
%{_mandir}/man3/Mail::MIMEDefang*.3*
%{_mandir}/man5/%{name}-filter.5*
%{_mandir}/man7/%{name}-notify.7*
%{_mandir}/man7/%{name}-protocol.7*
%{_mandir}/man8/md-mx-ctrl.8*
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}.pl.8*
%{_mandir}/man8/%{name}-multiplexor.8*
%{_mandir}/man8/%{name}-release.8*
%{_mandir}/man8/watch-%{name}.8*
%{_mandir}/man8/watch-multiple-%{name}s.8*
%dir %attr(0750,defang,defang) %{_localstatedir}/log/%{name}/
%dir %attr(0750,defang,defang) %{_localstatedir}/spool/MIMEDefang/
%dir %attr(0750,defang,defang) %{_localstatedir}/spool/MD-Quarantine/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.1-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.1-2
- Perl 5.38 rebuild

* Mon May 15 2023 Robert Scheck <robert@fedoraproject.org> 3.4.1-1
- Upgrade to 3.4.1 (#2203877)

* Thu Apr 27 2023 Robert Scheck <robert@fedoraproject.org> 3.4-1
- Upgrade to 3.4 (#2189708)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Robert Scheck <robert@fedoraproject.org> 3.3-1
- Upgrade to 3.3 (#2161362)

* Mon Oct 24 2022 Robert Scheck <robert@fedoraproject.org> 3.2-1
- Upgrade to 3.2 (#2136815)

* Wed Aug 24 2022 Robert Scheck <robert@fedoraproject.org> 3.1-1
- Upgrade to 3.1 (#2121227)

* Sat Aug 06 2022 Robert Scheck <robert@fedoraproject.org> 3.0-1
- Upgrade to 3.0 (#2097136)

* Sun Jul 31 2022 Robert Scheck <robert@fedoraproject.org> 2.86-4
- Added sysusers.d file to achieve user() and group() provides

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.86-2
- Perl 5.36 rebuild

* Fri Feb 11 2022 Robert Scheck <robert@fedoraproject.org> 2.86-1
- Upgrade to 2.86 (#2033718, #2053245)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 29 2021 Robert Scheck <robert@fedoraproject.org> 2.85-1
- Upgrade to 2.85 (#1998443)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-12
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.84-11
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-2
- Perl 5.28 rebuild

* Thu Mar 22 2018 Robert Scheck <robert@fedoraproject.org> 2.84-1
- Upgrade to 2.84 (#1559208)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.83-2
- Rebuilt for switch to libxcrypt

* Wed Nov 01 2017 Robert Scheck <robert@fedoraproject.org> 2.83-1
- Upgrade to 2.83 (#1508217)

* Mon Oct 09 2017 Robert Scheck <robert@fedoraproject.org> 2.82-1
- Upgrade to 2.82 (#1489992)

* Sun Sep 03 2017 Robert Scheck <robert@fedoraproject.org> 2.81-1
- Upgrade to 2.81 (#1487543, #1487804)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2.80-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Robert Scheck <robert@fedoraproject.org> 2.80-1
- Upgrade to 2.80 (#1474551)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.79-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Robert Scheck <robert@fedoraproject.org> 2.79-1
- Upgrade to 2.79 (#1380052)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.78-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.78-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Robert Scheck <robert@fedoraproject.org> 2.78-6
- Avoid chown-ing and chmod-ing /dev/null (#1296288 #c6)

* Sun Jan 03 2016 Robert Scheck <robert@fedoraproject.org> 2.78-5
- Provide native systemd service (#789768, #1279452)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.78-3
- Perl 5.22 rebuild

* Tue May 05 2015 Robert Scheck <robert@fedoraproject.org> 2.78-2
- Fix wrong interpreter of mimedefang-util script (#1218754)

* Thu Apr 23 2015 Robert Scheck <robert@fedoraproject.org> 2.78-1
- Upgrade to 2.78 (#1213639)

* Wed Apr 22 2015 Robert Scheck <robert@fedoraproject.org> 2.77-1
- Upgrade to 2.77 (#1213639)

* Sun Mar 29 2015 Robert Scheck <robert@fedoraproject.org> 2.76-1
- Upgrade to 2.76 (#1206857)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.75-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Robert Scheck <robert@fedoraproject.org> 2.75-1
- Upgrade to 2.75

* Sat Aug 31 2013 Robert Scheck <robert@fedoraproject.org> 2.74-1
- Upgrade to 2.74 (#971523, thanks to Philip Prindeville)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.73-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Robert Scheck <robert@fedoraproject.org> 2.73-3
- Re-enabled embedded perl feature (thanks to Alexander Dalloz)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Robert Scheck <robert@fedoraproject.org> 2.73-1
- Upgrade to 2.73 (#759805, thanks to Philip Prindeville)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011 Robert Scheck <robert@fedoraproject.org> 2.72-3
- Removed requirement on sendmail-cf for postfix (#754847)

* Sat Oct 08 2011 Robert Scheck <robert@fedoraproject.org> 2.72-2
- Added build requirement to perl(ExtUtils::MakeMaker)
- Reflected changed parameters to disable binary stripping

* Sat Oct 08 2011 Robert Scheck <robert@fedoraproject.org> 2.72-1
- Upgrade to 2.72

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 05 2010 Robert Scheck <robert@fedoraproject.org> 2.71-1
- Upgrade to 2.71

* Sun Mar 28 2010 Robert Scheck <robert@fedoraproject.org> 2.68-1
- Upgrade to 2.68

* Mon Dec 21 2009 Robert Scheck <robert@fedoraproject.org> 2.67-3
- Rebuilt against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 05 2009 Robert Scheck <robert@fedoraproject.org> 2.67-1
- Upgrade to 2.67

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.65-2
- Rebuilt against gcc 4.4 and rpm 4.6

* Thu Sep 04 2008 Robert Scheck <robert@fedoraproject.org> 2.65-1
- Upgrade to 2.65

* Sat Feb 09 2008 Robert Scheck <robert@fedoraproject.org> 2.64-1
- Upgrade to 2.64

* Wed Aug 29 2007 Robert Scheck <robert@fedoraproject.org> 2.63-1
- Upgrade to 2.63
- Updated the license tag according to the guidelines

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 2.62-2
- Changed sendmail build requirement slightly (#237157)

* Mon Apr 16 2007 Robert Scheck <robert@fedoraproject.org> 2.62-1
- Upgrade to 2.62

* Wed Feb 14 2007 Robert Scheck <robert@fedoraproject.org> 2.61-1
- Upgrade to 2.61 (#228757)

* Tue Dec 19 2006 Robert Scheck <robert@fedoraproject.org> 2.58-3
- Use Unix::Syslog over deprecated Sys::Syslog support (#219988)

* Sat Dec 16 2006 Robert Scheck <robert@fedoraproject.org> 2.58-2
- Include the /etc/mail/mimedefang-ip-key file (#219381)

* Wed Nov 08 2006 Robert Scheck <robert@fedoraproject.org> 2.58-1
- Upgrade to 2.58 (#212657)

* Tue Oct 03 2006 Robert Scheck <robert@fedoraproject.org> 2.57-5
- Rebuilt

* Sat Sep 16 2006 Robert Scheck <robert@fedoraproject.org> 2.57-4
- Removed two hardcoded versioned requirements (#196101 #c13)

* Mon Sep 11 2006 Robert Scheck <robert@fedoraproject.org> 2.57-3
- Disable stripping to have a non-empty -debuginfo package
- Added %%configure parameter for finding libmilter.a on x86_64

* Wed Jun 21 2006 Robert Scheck <robert@fedoraproject.org> 2.57-2
- Changes to match with Fedora Packaging Guidelines (#196101)

* Tue Jun 20 2006 Robert Scheck <robert@fedoraproject.org> 2.57-1
- Upgrade to 2.57

* Tue Mar 07 2006 Robert Scheck <robert@fedoraproject.org> 2.56-1
- Upgrade to 2.56

* Mon Feb 06 2006 Robert Scheck <robert@fedoraproject.org> 2.55-1
- Upgrade to 2.55

* Sat Dec 24 2005 Robert Scheck <robert@fedoraproject.org> 2.54-1
- Upgrade to 2.54

* Mon Sep 19 2005 Robert Scheck <robert@fedoraproject.org> 2.53-1
- Upgrade to 2.53

* Thu Jun 02 2005 Robert Scheck <robert@fedoraproject.org> 2.52-1
- Upgrade to 2.52

* Sun Mar 13 2005 Robert Scheck <robert@fedoraproject.org> 2.51-2
- Rebuilt against gcc 4.0

* Tue Feb 08 2005 Robert Scheck <robert@fedoraproject.org> 2.51-1
- Upgrade to 2.51

* Mon Dec 13 2004 Robert Scheck <robert@fedoraproject.org> 2.49-1
- Upgrade to 2.49

* Sun Nov 07 2004 Robert Scheck <robert@fedoraproject.org> 2.47-1
- Upgrade to 2.47 and some spec file cleanups

* Mon Oct 04 2004 Robert Scheck <robert@fedoraproject.org> 2.45-1
- Upgrade to 2.45 and lots of spec file cleanups

* Thu Jul 15 2004 Robert Scheck <robert@fedoraproject.org> 2.44-1
- Upgrade to 2.44
- Move sa-mimedefang.cf from /etc/mail/spamassassin to /etc/mail

* Mon May 10 2004 Robert Scheck <robert@fedoraproject.org> 2.43-1
- Upgrade to 2.43

* Wed Mar 31 2004 Robert Scheck <robert@fedoraproject.org> 2.42-1
- Upgrade to 2.42

* Thu Mar 18 2004 Robert Scheck <robert@fedoraproject.org> 2.41-1
- Upgrade to 2.41
- Few fixes and cleanup in the spec file

* Mon Mar 08 2004 Robert Scheck <robert@fedoraproject.org> 2.40-1
- Upgrade to 2.40

* Wed Jan 07 2004 Robert Scheck <robert@fedoraproject.org> 2.39-2
- Fixed spec file problems with chkconfig

* Sat Nov 29 2003 Robert Scheck <robert@fedoraproject.org> 2.39-1
- Upgrade to 2.39

* Sat Oct 11 2003 Robert Scheck <robert@fedoraproject.org> 2.38-1
- Upgrade to 2.38
- Initial spec file for Red Hat Linux
