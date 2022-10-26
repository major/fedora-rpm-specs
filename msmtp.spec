Name:		msmtp
Version:	1.8.22
Release:	1%{?dist}
Summary:	SMTP client
License:	GPLv3+
URL:		https://marlam.de/%{name}/
Source0:	https://marlam.de/%{name}/releases/%{name}-%{version}.tar.xz

BuildRequires: make
%if 0%{?el5}
BuildRequires:	openssl-devel
%else
BuildRequires:	gnutls-devel
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	libidn-devel
BuildRequires:	libgsasl-devel
BuildRequires:	libsecret-devel

Requires(post):		%{_sbindir}/alternatives
Requires(postun):	%{_sbindir}/alternatives

%description
It forwards messages to an SMTP server which does the delivery.
Features include:
  * Sendmail compatible interface (command line options and exit codes).
  * Authentication methods PLAIN,LOGIN,CRAM-MD5,DIGEST-MD5,GSSAPI,and NTLM
  * TLS/SSL both in SMTP-over-SSL mode and in STARTTLS mode.
  * Fast SMTP implementation using command pipe-lining.
  * Support for Internationalized Domain Names (IDN).
  * DSN (Delivery Status Notification) support.
  * RMQS (Remote Message Queue Starting) support (ETRN keyword).
  * IPv6 support.

%prep
%autosetup -p1

%build
autoreconf -ivf
%configure --disable-rpath --with-libsecret --with-libgsasl %{?el5:--with-ssl=openssl}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
rm -f scripts/Makefile*
%find_lang %{name}
rm -f %{buildroot}%{_infodir}/dir

# setup dummy files for alternatives
touch %{buildroot}%{_bindir}/msmtp

%post
%{_sbindir}/update-alternatives --install %{_sbindir}/sendmail mta %{_bindir}/msmtp 40 \
  --slave %{_prefix}/lib/sendmail mta-sendmail %{_bindir}/msmtp \
  --slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man1/msmtp.1.gz \
  --slave %{_bindir}/mailq mta-mailq %{_bindir}/msmtp \
  --slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/msmtp.1.gz

%postun
if [ $1 -eq 0 ] ; then
	%{_sbindir}/update-alternatives --remove mta %{_bindir}/msmtp
fi

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README THANKS scripts
%doc doc/msmtprc-system.example doc/msmtprc-user.example
%{_bindir}/%{name}*
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}*.1*

%changelog
* Mon Oct 24 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.8.22-1
- Ver. 1.8.22 (rhbz#2116156)

* Sun Aug  7 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.8.21-1
- Ver. 1.8.21 (rhbz#2116131)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr  6 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.8.20-1
- Ver. 1.8.20 (rhbz#2067470)

* Thu Jan 27 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.8.19-1
- Ver. 1.8.19 (rhbz#2003823)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr  3 2021 Peter Lemenkov <lemenkov@gmail.com> - 1.8.14-1
- Ver. 1.8.14 (rhbz#1938231)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.8.14-1
- Ver. 1.8.14 (rhbz#1910357)

* Tue Nov 24 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.8.13-1
- Ver. 1.8.13 (rhbz#1897609)

* Tue Oct 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.8.12-1
- Ver. 1.8.12 (rhbz#1843697)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.8.10-1
- Ver. 1.8.10 (rhbz#1827068)

* Sat Apr 18 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.8.8-1
- Ver. 1.8.8 (rhbz#1823187)

* Thu Feb 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.8.7-1
- Ver. 1.8.7 (rhbz#1786781)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.8.6-1
- Upstream release rhbz#1756345

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.8.5-1
- Upstream release rhbz#1729541

* Wed Apr 24 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.8.4-1
- Upstream release rhbz#1702798

* Tue Feb 12 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.8.3-1
- Upstream release rhbz#1675527

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.8.2-1
- Upstream release rhbz#1670013

* Sat Jul 14 2018 Gerald Cox <gbcox@fedoraproject.org> - 1.6.7-3
- Adjust alternatives priority rhbz#1598386

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Gerald Cox <gbcox@fedoraproject.org> - 1.6.7-1
- Upstream release 1.6.7 rhbz#1594450

* Fri Jun 22 2018 Gerald Cox <gbcox@fedoraproject.org> - 1.6.6-6
- Add alternatives rhbz#1367858

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.6-1
- Ver. 1.6.6

* Mon Jun  6 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.5-1
- Ver. 1.6.5

* Sat Feb 20 2016 Niels de Vos <devos@fedoraproject.org> - 1.6.4-1
- Update to version 1.6.4 (#1303788)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Niels de Vos <devos@fedoraproject.org> - 1.6.3-1
- Update to version 1.6.3 (#1286308)
- TLS: use system crypto policy (#1179321)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Niels de Vos <devos@fedoraproject.org> - 1.6.2-1
- Update to version 1.6.2 (#1170995)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Niels de Vos <devos@fedoraproject.org> - 1.4.32-1
- Ver. 1.4.32 (#1074922)

* Mon Sep 02 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4.31-1
- Ver. 1.4.31

* Thu Aug  1 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.4.29-3
- Fix build with unversioned %%{_docdir_fmt}.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.29-1
- New upstream release

* Tue Aug 07 2012 Ian Weller <iweller@redhat.com> - 1.4.27-3
- BR: libgnome-keyring-devel (fixes RHBZ 838330)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 28 2012 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.27-1
- New upstream release
- install the helper scripts in package's docir
- minor spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 15 2011 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.23-1
- New upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 12 2010 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.19-1
- new upstream release
- fix source0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 1 2009 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.17-1
- Msmtp now also reads SYSCONFDIR/netrc if the password wasn't found in ~/.netrc.
- Support for the GNOME keyring was added by Satoru SATOH.
- Added BuildRequires for gnome-keyring-devel due to the new feature.
- Added PDF version of the manual.

* Tue Jul 29 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.16-1
- new upstream release - 1.4.16

* Fri Jun 27 2008 Nikolay Vladimriov <nikolay@vladimiroff.com> - 1.4.15-1
- new upstream release
- rebuild for new gnutls 

* Sat Apr 19 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.14-1
- new upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.13-4
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.13-3
- rebuild for ppc32 selinux fix

* Thu Aug 2 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.13-2
- License tag changed

* Thu Aug 2 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.13-1
- 1.4.13
- license changed to GPLv3

* Sat Jun 30 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.12-7
- timestamps fix

* Sat Jun 30 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.12-6
- minor spec fixes

* Thu Jun 28 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.12-5
- removed provides for sendmail
- added BuildRequires for libgsasl

* Fri Jun 22 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.12-4
- not using alternatives

* Wed Jun 20 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.12-3
- now using alternatives 
- added provides for sendmail 
- edited description 

* Tue Jun 19 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.12-2
- fixed source0
- removed openssl-devel from BuildRequires
- added BuildRequires for gettext
- added more doc files

* Tue Jun 19 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.12-1
- new version 
- changed Summary and description

* Mon Jun 11 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.11-2
- fixed URL, Summary and description

* Mon Jun 11 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.11-1
- initial release
