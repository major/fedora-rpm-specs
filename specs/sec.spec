Name:           sec
Version:        2.9.3
Release:        2%{?dist}
Summary:        Simple Event Correlator script to filter log file entries
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://simple-evcorr.github.io/
Source0:        https://github.com/simple-evcorr/sec/releases/download/%{version}/sec-%{version}.tar.gz
Source1:        sec.service
Source2:        sec@.service
Source3:        sec.logrotate
Source4:        sec.sysconfig
Source5:        conf.README
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  systemd

Requires:       logrotate

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
SEC is a simple event correlation tool that reads lines from files, named
pipes, or standard input, and matches the lines with regular expressions,
Perl subroutines, and other patterns for recognizing input events.
Events are then correlated according to the rules in configuration files,
producing output events by executing user-specified shell commands, by
writing messages to pipes or files, etc.

%prep
%setup -q

%build

%install
# Install SEC and its associated files
install -D -m 0755 -p sec        %{buildroot}%{_bindir}/sec
install -D -m 0644 -p sec.man    %{buildroot}%{_mandir}/man1/sec.1
install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_unitdir}/sec.service
install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_unitdir}/sec@.service
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/sec
install -D -m 0644 -p %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/sec
install -D -m 0644 -p %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/README

# Remove executable bits because these files get packed as docs
chmod 0644 contrib/convert.pl contrib/swatch2sec.pl

%post
%systemd_post sec.service

%preun
%systemd_preun sec.service

%postun
%systemd_postun_with_restart sec.service

%files
%doc ChangeLog COPYING README contrib/convert.pl contrib/itostream.c contrib/swatch2sec.pl
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/sec
%config(noreplace) %{_sysconfdir}/sysconfig/sec
%{_bindir}/sec
%{_mandir}/man1/sec.1*
%{_unitdir}/sec.service
%{_unitdir}/sec@.service

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 02 2024 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.9.3-1
- New upstream release

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9.2-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.9.2-1
- New upstream release

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.9.1-1
- New upstream release

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 13 2021 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.9.0-1
- New upstream release

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.8.3-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 2 2020 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.8.3-1
- New upstream release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 3 2019 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.8.2-1
- New upstream release
- Clean up spec file
- Added an environment file /etc/sysconfig/sec in order to specify command line options

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 3 2018 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.8.1-0
- New upstream release

* Sun Sep 2 2018 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.8.0-0
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.12-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.12-0
- New upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.11-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 5 2017 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.11-0
- New upstream release

* Fri Jun 24 2016 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.10-0
- New upstream release

* Sat Apr 2 2016 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.9-0
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 6 2015 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.8-0
- New upstream release

* Wed Oct 14 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.7-2
- While rotating logfiles do not do a full restart of the sec instance

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.7-0
- New upstream release

* Tue Jul 15 2014 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.6-0
- New upstream release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.5-0
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.4-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 29 2013 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.4-0
- New upstream release

* Sun Jun 2 2013 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.3-0
- New upstream release

* Mon Apr 15 2013 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.2-0
- New upstream release

* Fri Mar 15 2013 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.7.1-0
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 17 2012 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.6.2-2
- Apply latest packaging guidelines (systemd scriptlets for F18+)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 5 2012 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.6.2-0
- New upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.6.1-0
- New upstream release

* Sat Jun 11 2011 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.6.0-2
- Upgrade to systemd

* Sun Mar 20 2011 Stefan Schulze Frielinghaus <stefansf@fedoraproject.org> - 2.6.0-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 10 2009 Stefan Schulze Frielinghaus <stefan@seekline.net> - 2.5.3-0
- New upstream release

* Tue Sep 29 2009 Stefan Schulze Frielinghaus <stefan@seekline.net> - 2.5.2-1
- New upstream release
- SPEC file cleanup
- Init script cleanup
- Removed some examples because of licensing issues. Upstream has clarified
  and changed most of the license tags to GPLv2. Additionally, upstream
  will include the examples in the next release.
- Removed a provide statement since a period was in the name and no other
  package required that special name.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.1-2
- fix license tag

* Mon May 28 2007 Chris Petersen <rpm@forevermore.net>                  2.4.1-1
- Update to 2.4.1

* Wed Dec 06 2006 Chris Petersen <rpm@forevermore.net>                  2.4.0-1
- Update to 2.4.0

* Mon Jun 12 2006 Chris Petersen <rpm@forevermore.net>                  2.3.3-4
- Change group to keep rpmlint happy
- Fix permissions on the logrotate script

* Thu Jun 08 2006 Chris Petersen <rpm@forevermore.net>                  2.3.3-3
- Clean up spec
- Add ghost file entries for the default logfile and pid
- Add logrotate script
- Add more bleedingsnort examples
- Add pid to sec.sysconfig and completely rewrite to handle multiple instances
- Fix download URL
- Fix echo log command in 001_init.sec
- Rewrite sysV init script to handle multiple instances (based loosely on vsftpd)

* Mon May 01 2006 Didier Moens <Didier.Moens@dmbr.UGent.be>             2.3.3-2
- Change init script to not start by default in any runlevel

* Fri Apr 28 2006 Didier Moens <Didier.Moens@dmbr.UGent.be>             2.3.3-1
- Upgrade to upstream 2.3.3
- Add status to init script

* Thu Sep 22 2005 Didier Moens <Didier.Moens@dmbr.UGent.be>             2.3.2-4
- Update Source locations

* Thu Sep 22 2005 Didier Moens <Didier.Moens@dmbr.UGent.be>             2.3.2-3
- Change permissions on /usr/bin/sec

* Thu Sep 22 2005 Didier Moens <Didier.Moens@dmbr.UGent.be>             2.3.2-2
- Create initial startup rulesets
- Add examples
- Refine init script

* Wed Sep 21 2005 Didier Moens <Didier.Moens@dmbr.UGent.be>             2.3.2-1
- First build
