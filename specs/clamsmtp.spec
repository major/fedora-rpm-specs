Summary:                A SMTP virus scanning system
Name:                   clamsmtp
Version:                1.10
Release:                46%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:                LicenseRef-Callaway-BSD
URL:                    http://memberwebs.com/stef/software/clamsmtp/

Source0:                http://thewalter.net/stef/software/clamsmtp/clamsmtp-%{version}.tar.gz
Source1:                clamsmtpd.service
Source2:                clamsmtpd.conf
Source5:                clamsmtp-clamd.logrotate
Source6:                clamsmtp-clamd.service
Source7:                clamsmtp-clamd.conf
Source8:                clamsmtp-tmpfile.conf

Patch0:                 clamsmtp-man.patch
Patch1:                 clamsmtp-readme.patch
Patch2:                 clamsmtp-include_order.patch
Patch3:                 clamsmtp-autoconf-c99.patch

BuildRequires:          clamav-devel gcc gcc-c++ systemd
BuildRequires:          make autoconf automake

Requires(pre):          shadow-utils
Requires(preun):        systemd
Requires(post):         systemd

Requires:               clamd

%description
ClamSMTP is an SMTP filter that allows you to check for 
viruses using the ClamAV anti-virus software. It accepts 
SMTP connections and forwards the SMTP commands and 
responses to another SMTP server. The 'DATA' email body 
is intercepted and scanned before forwarding.

It aims to be lightweight, reliable, and simple 
rather than have a myriad of options. It's written in C 
without major dependencies. If you need more options then 
you could use something big like AMaViS which is written 
in PERL and can do almost anything.

Written with the Postfix mail server in mind it can be 
configured as a Postfix Content Filter. It can also 
be used as a transparent proxy to filter an entire network's 
SMTP traffic at the router.

%prep

%setup -q
%patch 0 -p0 -b .man
%patch 1 -p0 -b .readme
%patch 2 -p1 -b .include_order
%patch 3 -p1 -b .autoconf-c99

%build
autoreconf -vi
%configure 
%{make_build}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_var}/run/clamd.clamsmtp
mkdir -p $RPM_BUILD_ROOT%{_var}/log/clamd.clamsmtp
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/clamd.clamsmtp
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/clamd.clamsmtp
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/clamsmtpd
install -Dp -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/clamsmtpd.service
install -Dp -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/clamsmtpd.conf
install -Dp -m0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/clamsmtp

install -Dp -m0644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/clamsmtp-clamd.service
install -Dp -m0644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/clamd.d/clamsmtp.conf

install -Dp -m0644 %{SOURCE8} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/clamsmtp.conf

%post
%systemd_post clamsmtpd-clamd.service clamsmtpd.service

%preun
%systemd_preun clamsmtpd-clamd.service clamsmtpd.service

%postun
%systemd_postun_with_restart clamsmtpd-clamd.service clamsmtpd.service

%pre
getent passwd clamsmtp >/dev/null || useradd -r -g mail -d %{_var}/lib/clamd.clamsmtp -s /sbin/nologin -c 'User to own clamsmtp directories and default processes' clamsmtp
exit 0

%files
%license COPYING
%doc AUTHORS README
%{_unitdir}/clamsmtpd.service
%{_unitdir}/clamsmtp-clamd.service
%config(noreplace) %{_sysconfdir}/logrotate.d/clamsmtp
%config(noreplace) %{_sysconfdir}/clamsmtpd.conf
%config(noreplace) %{_sysconfdir}/clamd.d/clamsmtp.conf
%{_prefix}/lib/tmpfiles.d/clamsmtp.conf
%dir %attr(755,clamsmtp,mail) %{_localstatedir}/run/clamd.clamsmtp
%dir %attr(755,clamsmtp,mail) %{_localstatedir}/run/clamsmtpd
%attr(755,root,root) %{_sbindir}/clamsmtpd
%attr(755,clamsmtp,mail) %{_var}/lib/clamd.clamsmtp
%attr(755,clamsmtp,mail) %{_var}/log/clamd.clamsmtp
%{_mandir}/man5/clamsmtpd.conf.5.gz
%{_mandir}/man8/clamsmtpd.8.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10-45
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 8 2024 Nathanael Noblet <nathanael@gnat.ca> - 1.10-43
- Removed deprecated patch macros

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Peter Fordham <peter.fordham@gmail.com> - 1.10-38
- Fix check in acsite.m4 to be C99 compatible.
- Add autoreconf step to build to flush non C99 compatible checks from configure.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.10-34
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Nathanael Noblet <nathanael@gnat.ca> - 1.10-31
- clamav-server was renamed to clamd

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.10-27
- Use %%license, Remove remanents of sys-v migrations

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Nathanael Noblet <nathanael@gnat.ca> - 1.10-25
- Fixed fail to build bug with newer kernel headers by adding a patch

* Tue Feb 20 2018 Nathanael Noblet <nathanael@gnat.ca> - 1.10-24
- Include gcc and gcc-c++ as BuildRequires now

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Nathanael Noblet <nathanael@gnat.ca> - 1.10-20
- Updated logrotate script to pass stdout + stderr to /dev/null
- Fixes #1381211

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Nathanael Noblet <nathanael@gnat.ca> - 1.10-18
- updated readme url links
- Fixes Bug #1322048

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Nathanael Noblet <nathanael@gnat.ca> - 1.10-13
- Updated to use systemd post/preun/postun macros

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 31 2012 Nathanael Noblet <nathanael@gnat.ca> - 1.10-9
- Fix logrotate script

* Tue May 15 2012 Nathanael Noblet <nathanael@gnat.ca> - 1.10-8
- Fix typo in clamsmtpd.service file

* Mon May 14 2012 Nathanael Noblet <nathanael@gnat.ca> - 1.10-7
- Fix tmpfiles for F17

* Thu Jan 5 2012 Nathanael Noblet <nathanael@gnat.ca> - 1.10-6
- Added native systemd files provided by Johann
- Removed /var/run/clamd.clamsmtp

* Mon Nov 21 2011 Nathanael Noblet <nathanael@gnat.ca> - 1.10-5
- Fix log rotation

* Sun Sep 11 2011 Nathanael Noblet <nathanael@gnat.ca> - 1.10-4
- Fix bug #670569

* Tue May 24 2011 Nathanael Noblet <nathanael@gnat.ca> - 1.10-3
- Added tmpfiles.d entry

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 12 2010 Nathanael Noblet <nathanael@gnat.ca> - 1.10-1
- Use integer for release ver
- Unified Requires(foo) style
- Added missing Requires
- Consistent macro useage
- Remove dot from initscript filename

* Mon Jul 19 2010 Nathanael Noblet <nathanael@gnat.ca> - 1.10-0.2
- Cleaned up the directories and init script names
- Added Requires(postun)
- Fixed logrotate script

* Mon Jan 18 2010 Nathanael Noblet <nathanael@gnat.ca> - 1.10-0.1
- Cleaned up for fedora guidelines
- Updated to version 1.10

* Mon Nov 1 2004 Rubio Vaughan <rubio@passim.net> 1.1-1mdk
- Updated to version 1.1

* Sat Oct 30 2004 Rubio Vaughan <rubio@passim.net> 1.0-1mdk
- Updated to version 1.0
- Added virusheader patch

* Mon Sep 27 2004 Rubio Vaughan <rubio@passim.net> 0.9-1mdk
- Updated to version 0.9
- Removed droppriv patch since it's integrated in the main
  ClamSMTP distribution now.

* Sun Sep 12 2004 Rubio Vaughan <rubio@passim.net> 0.8-2mdk
- Added droppriv patch to run clamsmtpd under a different user
- Added Mandrake init script

* Sun Sep 12 2004 Rubio Vaughan <rubio@passim.net> 0.8-1mdk
- Created clamsmtp.spec file

