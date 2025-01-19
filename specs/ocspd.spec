# % global alphatag	rc1
%global revision	%{?alphatag:-}%{?alphatag}


Name:		ocspd
Version:	1.9.0
Release:	33%{?alphatag:.}%{?alphatag}%{?dist}
Summary:	OpenCA OCSP Daemon
License:	Apache-1.0
Source:		http://downloads.sourceforge.net/openca/openca-ocspd-%{version}%{revision}.tar.gz
Source1:	ocspd.service
Patch1:		ocspd-1.7.0-bufresponse.patch
Patch2:		ocspd-1.9.0-misc.patch
Patch3:		ocspd-1.7.0-openssl.patch
Patch4:		ocspd-1.7.0-podsyntax.patch
Patch5:		ocspd-1.7.0-badalgorcast.patch
Patch6:		ocspd-1.7.0-badcasts.patch
Patch7:		ocspd-1.7.0-deprecldap.patch
Patch8:		ocspd-1.7.0-threadinit.patch
Patch9:		ocspd-1.7.0-config.patch
Patch10:	ocspd-1.7.0-setgroups.patch
Patch11:	ocspd-1.9.0-stealthy.patch
Patch12:	ocspd-1.9.0-noformat.patch
Patch13:	ocspd-1.9.0-openssl11.patch
URL:		http://www.openca.org/projects/ocspd
Obsoletes:	openca-ocspd <= %{version}-%{release}
Provides:	openca-ocspd = %{version}-%{release}
Requires(pre):	shadow-utils
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:	openssl-devel-engine
%endif
BuildRequires:	openldap-devel
BuildRequires:	automake autoconf
BuildRequires:	perl-podlators
BuildRequires:	systemd-rpm-macros
Requires(post):	systemd
Requires(post):	systemd-sysv
Requires(preun):systemd
Requires(postun):systemd

%description
 The ocspd is an RFC2560 compliant OCSPD responder. It can be used to
verify the status of a certificate using OCSP clients (such as
Mozilla/Firefox/Thunderbird/Apache).


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q -n openca-ocspd-%{version}%{revision}
%patch -P1 -p1 -b .bufresponse
%patch -P2 -p1 -b .misc
%patch -P3 -p1 -b .openssl
%patch -P4 -p1 -b .podsyntax
%patch -P5 -p1 -b .badalgorcast
%patch -P6 -p1 -b .badcasts
%patch -P7 -p1 -b .deprecldap
%patch -P8 -p1 -b .threadinit
%patch -P9 -p1 -b .config
%patch -P10 -p1 -b .setgroups
%patch -P11 -p1 -b .stealthy
%patch -P12 -p1 -b .noformat
%patch -P13 -p1 -b .openssl11


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

#	Need automake/autoconf rebuild because of above patches.

aclocal
autoheader
automake --add-missing
autoconf


%ifarch alpha
	ARCH_FLAGS="--host=alpha-redhat-linux"
%endif


%configure ${ARCH_FLAGS} --enable-openssl-engine --with-ocspd-group=ocspd
make %{?_smp_mflags}


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

make DESTDIR="${RPM_BUILD_ROOT}" install

#	Remove SysV init scripts directory.

rm -rf "${RPM_BUILD_ROOT}%{_initrddir}"

#	Install systemd service script.

mkdir -p "${RPM_BUILD_ROOT}%{_unitdir}/"
cp -a "%{SOURCE1}" "${RPM_BUILD_ROOT}%{_unitdir}/"

#-------------------------------------------------------------------------------
%pre
#-------------------------------------------------------------------------------

getent group ocspd >/dev/null || groupadd -r ocspd
getent passwd ocspd >/dev/null ||
	useradd -r -g ocspd -d "%{_sysconfdir}/ocspd"			\
		-s /sbin/nologin -c "OCSP Responder" ocspd
exit 0


#-------------------------------------------------------------------------------
%post
#-------------------------------------------------------------------------------

%systemd_post ocspd.service


#-------------------------------------------------------------------------------
%preun
#-------------------------------------------------------------------------------

%systemd_preun ocspd.service


#-------------------------------------------------------------------------------
%postun
#-------------------------------------------------------------------------------

%systemd_postun_with_restart ocspd.service


#-------------------------------------------------------------------------------
%triggerun -- ocspd < 1.5.1-0.9
#-------------------------------------------------------------------------------

%{_bindir}/systemd-sysv-convert --save ocspd > /dev/null 2>&1 || :
/sbin/chkconfig --del ocspd > /dev/null 2>&1 || :
/bin/systemctl try-restart ocspd.service > /dev/null 2>&1 || :

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%doc AUTHORS COPYING ChangeLog README
%{_sbindir}/*
%dir %{_sysconfdir}/ocspd
%dir %{_sysconfdir}/ocspd/c*
%attr(700, ocspd, root) %dir %{_sysconfdir}/ocspd/private
%config(noreplace) %{_sysconfdir}/ocspd/ocspd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/*
%{_mandir}/*/*
%{_unitdir}/*


#-------------------------------------------------------------------------------
%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

#-------------------------------------------------------------------------------

* Tue Jul 23 2024 Patrick Monnerat <patrick@monnerat.net> 1.9.0-32
- BR openssl-devel-engine for Fedora >= 41.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 21 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.0-30
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Patrick Monnerat <patrick@monnerat.net> 1.9.0-26
- BR systemd-rpm-macros.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.9.0-22
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.0-20
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar  7 2018 Patrick Monnerat <patrick@monnerat.net> 1.9.0-13
- "Modernize" spec file.
- BR gcc.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 23 2017 Patrick Monnerat <patrick@monnerat.net> 1.9.0-9
- Patch "openssl11" to support openssl >= 1.1.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Patrick Monnerat <pm@datasphere.ch> 1.9.0-3
- Patch "noformat" fixes a printf format warning.

* Wed Dec  4 2013 Patrick Monnerat <pm@datasphere.ch> 1.9.0-2
- Patch "stealthy" fixes handling of stealthy connections.
  https://bugzilla.redhat.com/show_bug.cgi?id=1037717

* Tue Nov  5 2013 Patrick Monnerat <pm@datasphere.ch> 1.9.0-1
- New upstream release.

* Mon Nov  4 2013 Patrick Monnerat <pm@datasphere.ch> 1.7.0-1
- New upstream release.
- Patch "badcasts" to fix bad casting (ptr <--> int, ssize_t <--> int).
- Patch "deprecldap" to get rid of using deprecated ldap API.
- Patch "threadinit" to move thread initialization after scheduling.
- Patch "config" to add needed LDAP configuration parameters to default config.
- Patch "setgroups" to call setgroups() before setuid() (CERT POS36-C).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-0.16.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Patrick Monnerat <pm@datasphere.ch> 1.5.1-0.15.rc1
- Build requires "perl-podlators": pod2man moved to this package in F19.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-0.14.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Patrick Monnerat <pm@datasphere.ch> 1.5.1-0.13.rc1
- Patch "podsyntax" to fix man page pod syntax.
- Patch "badalgorcast" to fix a bad X509_ALGOR cast.
  https://bugzilla.redhat.com/show_bug.cgi?id=901793

* Fri Nov 16 2012 Patrick Monnerat <pm@datasphere.ch> 1.5.1-0.12.rc1
- Use new systemd scriptlet macros.
  https://bugzilla.redhat.com/show_bug.cgi?id=850238

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-0.11.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-0.10.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 12 2011 Patrick Monnerat <pm@datasphere.ch> 1.5.1-0.9.rc1
- Migration from SysV daemon handling to systemd (BZ# 720521).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 22 2009 Tomas Mraz <tmraz@redhat.com> - 1.5.1-0.7.rc1
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 1.5.1-0.4.rc1
- rebuild with new openssl

* Wed Oct  8 2008 Patrick Monnerat <pm@datasphere.ch> 1.5.1-0.3.rc1
- Use group "ocspd" for daemon.

* Tue Oct  7 2008 Patrick Monnerat <pm@datasphere.ch> 1.5.1-0.2.rc1
- Spec file section reworked.
- autoheader called.
- Patch "badcomment" to replace bad "#" comment marks in configure.in.
- Unimplemented configure option "--disable-shared" removed.
- System user creation reworked.

* Wed Jul  2 2008 Patrick Monnerat <pm@datasphere.ch> 1.5.1-0.1.rc1
- Package revision change and specs reworked according to Fedora standards.

* Mon Jun 30 2008 Patrick Monnerat <pm@datasphere.ch> 1.5.1-rc1.2
- Specific Fedora RPM spec file, obsolescing package "openca-ocspd".
- Patch "bufresponse" to output response in a single packet if possible.
- Patch "misc" to clean-up various things, such as suppressing the need of
  an unused CA certificate, use of regular Fedora directories, configuration
  files fixes, typos, configurable listen() queue length, configuration
  parameter names, autoconf 2.62 compatibility, etc.

* Sun Oct 15 2006 Massimiliano Pala <madwolf@openca.org>
-Fixed HTTP HEADERS parsing problem
-Tested behind an Apache Proxy
-Added '-debug' startup option to output the HTTP head and additional
informations to be pushed to stderr

* Fri Oct 13 2006 Massimiliano Pala <madwolf@openca.org>
-Completely changed the codebase in order to use threads instead
of fork().
-Fixed compilation under OpenSolaris (SunOS 5.11)
-Added chroot() capabilities
-Added options to set the number of threads to be pre-spawned
-Fixed Socket creation under Solaris (Accept)
-Moved from BIO_* interface to pure socket implementation for
better Network options management

* Tue Jul 18 2006 Massimiliano Pala <madwolf@openca.org>
-Removed required index file option in the configuration file (was not
used)

* Mon Apr 24 2006 Massimiliano Pala <madwolf@openca.org>
-Fixed invalidity date problem (no more empty ext added to responses)
-Added log reporting of returned status about a response when the
verbose switch is used (before it was enabled only in DEBUG mode)

* Mon Dec 19 2005 Massimiliano Pala <madwolf@openca.org>
-Added chroot facility to enhance server security

* Thu Nov  3 2005 Massimiliano Pala <madwolf@openca.org>
-Fixed compile against OpenSSL 0.9.8a
-Fixed HTTP downloading routines for CRLs and CA certs
-Fixed Solaris Port for Signal Handling on CRLs check and reloading

* Thu Oct  6 2005 Massimiliano Pala <madwolf@openca.org>
-Fixed variables init (for Solaris) and code cleanup

* Thu Apr 28 2005 Massimiliano Pala <madwolf@openca.org>
-Fixed RPM installation of man pages

* Wed Apr 27 2005 Massimiliano Pala <madwolf@openca.org>
-Fixed RPM creation on Fedora Distros

* Tue Apr 19 2005 Massimiliano Pala <madwolf@openca.org>
-Fixed child re-spawning when HSM is active
-Added support for CA/CRL downloading via HTTP

* Fri Jan 28 2005 Massimiliano Pala <madwolf@openca.org>
-Fixed SIGHUP problem when auto_crl_reload was enabled
-Fixed Solaris include for flock usage instead of semaphores
-Added --enable-flock and --enable-semaphores in configure script

* Tue Jan 18 2005 Massimiliano Pala <madwolf@openca.org>
- Fixed bug for nextUpdate and lastUpdate fields setting when reloading
  CRLs.
- Added CA certificate loading from LDAP.
- Added multiple CA certificate from the same cACertificate entry in LDAP.
- Fixed Solaris putenv issues in configure.c
- Added OS architecture specific targes in makefiles

* Wed May 19 2004 Massimiliano Pala <madwolf@openca.org>
- First support for new data structure for CRL lookup and multi CAs
  support (not working now)
- Fixed configure.in for correct generation of config.h
- Fixed configure.in for openldap ld options (for non-standard directories)

* Mon May 17 2004 Massimiliano Pala <madwolf@openca.org>
- Fixed compilation problems on Solaris
- Added support for exclusion of ldap usage (--disable-openldap)
- Added support for openldap directory specification
- Fixed signal handling and correct children death
- Added pre-spawning of processes()

* Thu May 13 2004 Massimiliano Pala <madwolf@openca.org>
- Fixed miscreation of responses when certificate is revoked
- Fixed crl loading checking (segmentation fault on loading fixed)

* Fri Jan 17 2003 Massimiliano Pala <madwolf@openca.org>
- Correclty lookup using loaded CRL
- Added extensions management from CRL to OCSP response

* Mon Jan 13 2003 Massimiliano Pala <madwolf@openca.org>
- Updated the sample (contrib/) configuration file
- Added CRL retrivial from LDAP server
- Added LDAP support (needs OpenLDAP libraries)
- Added CRL retrivial from file

* Wed Oct 16 2002 Massimiliano Pala <madwolf@openca.org>
- Fixed daemon description
- Fixed requirements (for ENGINE support)
- Added multi child spawning (max_childs_num)
- Fixed zombi child presence

* Mon Feb 25 2002 Massimiliano Pala <madwolf@openca.org>
  - Fixed response generation

* Tue Feb 20 2001 Massimiliano Pala <madwolf@openca.org>
- First RPM spec file
