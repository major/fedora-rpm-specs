# RHEL8 does not have libpskc, softhsm, ocserv yet
%if 0%{?rhel} && 0%{?rhel} == 8
%define use_tokens 0
%define use_ocserv 0
%define use_softhsm 0
%else
%define use_tokens 1
%define use_ocserv 1
%define use_softhsm 1
%endif

# Fedora has tss2-sys from F29 onwards, and RHEL from 8 onwards
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
%define use_tss2_esys 1
%else
%define use_tss2_esys 0
%endif

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		openconnect
Version:	9.12
Release:	7%{?relsuffix}%{?dist}
Summary:	Open multi-protocol SSL VPN client

License:	LGPL-2.1-or-later
URL:		http://www.infradead.org/openconnect.html
Source0:	https://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
Source1:	https://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz.asc
Source2:	gpgkey-BE07D9FD54809AB2C4B0FF5F63762CDA67E2F359.asc

BuildRequires:	make xdg-utils
BuildRequires:	pkgconfig(libxml-2.0) pkgconfig(libpcsclite) krb5-devel gnupg2
BuildRequires:	autoconf automake libtool gettext pkgconfig(liblz4)
BuildRequires:	pkgconfig(uid_wrapper) pkgconfig(socket_wrapper)
%if %{use_softhsm}
BuildRequires:	softhsm
%endif
Obsoletes:	openconnect-lib-compat < %{version}-%{release}
Requires:	vpnc-script

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 9
BuildRequires: glibc-langpack-cs
%endif
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(gnutls)
# Anywhere we use GnuTLS, there should be an ocserv package too
%if %{use_ocserv}
BuildRequires:	ocserv
%endif
%if %{use_tokens}
BuildRequires:  pkgconfig(stoken) pkgconfig(libpskc)
%endif
%if %{use_tss2_esys}
# https://bugzilla.redhat.com/show_bug.cgi?id=1638961
BuildRequires: pkgconfig(tss2-esys) libgcrypt-devel
%endif

%description
This package provides a multi-protocol VPN client for Cisco AnyConnect,
Juniper SSL VPN, Pulse/Ivanti Pulse Connect Secure, F5 BIG-IP, Fortinet
Palo Alto Networks GlobalProtect SSL VPN, Array Networks SSL VPN.

%package devel
Summary: Development package for OpenConnect VPN authentication tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the core HTTP and authentication support from
the OpenConnect VPN client, to be used by GUI authentication dialogs
for NetworkManager etc.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure	--with-vpnc-script=/etc/vpnc/vpnc-script \
		--disable-dsa-tests \
		--with-default-gnutls-priority="@OPENCONNECT,SYSTEM" \
		--without-gnutls-version-check \
		--htmldir=%{_pkgdocdir}

%make_build


%install
%make_install
mkdir -p $RPM_BUILD_ROOT/%{_pkgdocdir}
rm -f $RPM_BUILD_ROOT/%{_libdir}/libopenconnect.la
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/openconnect/tncc-wrapper.py
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/openconnect/hipreport-android.sh
%find_lang %{name}

%check
%if 0%{?rhel} >= 10
# RSA key exchange disabled in DEFAULT crypto config
make VERBOSE=1 check XFAIL_TESTS="obsolete-server-crypto pfs"
%elif 0%{?fedora} >= 34 || 0%{?rhel} >= 9
# 3DES and MD5 really are just gone.
make VERBOSE=1 check XFAIL_TESTS=obsolete-server-crypto
%else
make VERBOSE=1 check
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING.LGPL
%doc %{_pkgdocdir}
%{_libdir}/libopenconnect.so.5*
%{_sbindir}/openconnect
%{_libexecdir}/openconnect/
%{_mandir}/man8/*
%{_datadir}/bash-completion/completions/openconnect

%files devel
%{_libdir}/libopenconnect.so
%{_includedir}/openconnect.h
%{_libdir}/pkgconfig/openconnect.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 9.12-5
- Cleanup spec, drop EOL release consditionals

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 20 2023 David Woodhouse <dwmw2@infradead.org> - 9.12-1
- Update to 9.12 release

* Wed May 17 2023 David Woodhouse <dwmw2@infradead.org> - 9.11-1
- Update to 9.11 release

* Thu May 04 2023 David Woodhouse <dwmw2@infradead.org> - 9.10-1
- Update to 9.10 release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 9.01-2
- Compile with support for browser / xdg-open

* Fri Apr 29 2022 David Woodhouse <dwmw2@infradead.org> - 9.01-1
- Update to 9.01 release

* Tue Apr 19 2022 David Woodhouse <dwmw2@infradead.org> - 8.20-2
- Merge upstream patch to fix loglevel (OC #401).

* Sun Feb 20 2022 David Woodhouse <dwmw2@infradead.org> - 8.20-1
- Update to 8.20 release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 David Woodhouse <dwmw2@infradead.org> - 8.10-6
- Explicitly disable too-brittle system crypto policies (#1960763)
- Ignore with errors fetching Juniper landing page when login was successful anyway.

* Sun Feb 14 2021 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 8.10-5
- Rebuilt while skipping the (PKCS#11) failing tests

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 David Woodhouse <dwmw2@infradead.orG> - 8.10-1
- Update to 8.10 release (CVE-2020-12823)

* Sat May 2 2020 David Woodhouse <dwmw2@infradead.org> - 8.09-2
- Fix path to openconnect in bash completion script

* Wed Apr 29 2020 David Woodhouse <dwmw2@infradead.org> - 8.09-1
- Update to 8.09 release

* Mon Apr 6 2020 David Woodhouse <dwmw2@infradead.org> - 8.08-1
- Update to 8.08 release (CSD stderr handling, cert checking)

* Sat Apr 4 2020 David Woodhouse <dwmw2@infradead.org> - 8.07-1
- Update to 8.07 release (runtime check for GnuTLS)

* Tue Mar 31 2020 David Woodhouse <dwmw2@infradead.org> - 8.06-1
- Update to 8.06 release (Blacklist bad GnuTLS versions for insecure DTLS)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 David Woodhouse <dwmw2@infradead.org> - 8.05-1
- Update to 8.05 release (CVE-2019-16239)

* Sat Aug 10 2019 Kevin Fenzi <kevin@scrye.com> - 8.04-2
- Remove hipreport-android.sh from sources

* Fri Aug 09 2019 David Woodhouse <dwmw2@infradead.org> - 8.04-1
- Update to 8.04 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 David Woodhouse <dwmw2@infradead.org> - 8.03-1
- Update to 8.03 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Nikos Mavrogiannopoulos <nmav@redhat.com> - 8.02-2
- Removed python2 dependency (#1664029)

* Wed Jan 16 2019 David Woodhouse <dwmw2@infradead.org> - 8.02-1
- Update to 8.02 release
- Remove tncc-wrapper.py (#1664029)

* Sat Jan 05 2019 David Woodhouse <dwmw2@infradead.org> - 8.01-1
- Update to 8.01 release

* Sat Jan 05 2019 David Woodhouse <dwmw2@infradead.org> - 8.00-1
- Update to 8.00 release

* Wed Nov 07 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 7.08-9
- Corrected typo in the @OPENCONNECT priority string

* Mon Oct 22 2018 Michael Riss <Michael.Riss@gmail.com> - 7.08-9
- Add @OPENCONNECT priority string to allow a custom cipher suite for openconnect

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 4 2018 Iryna Shcherbina <ishcherb@redhat.com> - 7.08-7
- Remove build dependency on Python

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.08-5
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 David Woodhouse <dwmw2@infradead.org> - 7.08-1
- Update to 7.08 release

* Mon Jul 11 2016 David Woodhouse <David.Woodhouse@intel.com> - 7.07-2
- Enable Kerberos and PSKC support

* Mon Jul 11 2016 David Woodhouse <David.Woodhouse@intel.com> - 7.07-1
- Update to 7.07 release (#1268198)
- Enable PKCS#11 and Yubikey OATH support for OpenSSL (i.e. EL6) build

* Tue Mar 22 2016 David Woodhouse <David.Woodhouse@intel.com> - 7.06-7
- Switch to using GPGv2 for signature check

* Mon Mar 21 2016 David Woodhouse <David.Woodhouse@intel.com> - 7.06-6
- Check GPG signature as part of build

* Tue Feb 02 2016 Dennis Gilmore <dennis@ausil.us> - 7.06-4
- add upstream patch to fix ipv6 only setups

* Thu Oct 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 7.06-3
- Fix FTBFS by including packaged docs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 David Woodhouse <David.Woodhouse@intel.com> - 7.06-1
- Update to 7.06 release

* Wed Mar 11 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 7.05-2
- Utilize and enforce system-wide policies (#1179331)

* Tue Mar 10 2015 David Woodhouse <David.Woodhouse@intel.com> - 7.05-1
- Update to 7.05 release

* Sun Jan 25 2015 David Woodhouse <David.Woodhouse@intel.com> - 7.04-1
- Update to 7.04 release

* Fri Jan 09 2015 David Woodhouse <David.Woodhouse@intel.com> - 7.03-1
- Update to 7.03 release (#1179681)

* Fri Dec 19 2014 David Woodhouse <David.Woodhouse@intel.com> - 7.02-1
- Update to 7.02 release (#1175951)

* Sun Dec 07 2014 David Woodhouse <David.Woodhouse@intel.com> - 7.01-1
- Update to 7.01 release

* Thu Nov 27 2014 David Woodhouse <David.Woodhouse@intel.com> - 7.00-2
- Add upstreamed version of Nikos' curve patch with version.c fixed

* Thu Nov 27 2014 David Woodhouse <David.Woodhouse@intel.com> - 7.00-1
- Update to 7.00 release

* Tue Sep 16 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 6.00-2
- When compiling with old gnutls version completely disable ECDHE instead
  of disabling the curves.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 08 2014 David Woodhouse <David.Woodhouse@intel.com> - 6.00-1
- Update to 6.00 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 David Woodhouse <David.Woodhouse@intel.com> - 5.99-1
- Update to 5.99 release

* Wed Jan 01 2014 David Woodhouse <David.Woodhouse@intel.com> - 5.02-1
- Update to 5.02 release (#981911, #991653, #1031886)

* Sat Aug 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 5.01-4
- Fix install of docs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 David Woodhouse <David.Woodhouse@intel.com> - 5.01-2
- Build with stoken and OATH support.

* Sat Jun 01 2013 David Woodhouse <David.Woodhouse@intel.com> - 5.01-1
- Update to 5.01 release (#955710, #964329, #964650)

* Wed May 15 2013 David Woodhouse <David.Woodhouse@intel.com> - 5.00-1
- Update to 5.00 release

* Thu Feb 07 2013 David Woodhouse <David.Woodhouse@intel.com> - 4.99-1
- Update to 4.99 release

* Fri Aug 31 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.07-2
- Obsolete openconnect-lib-compat (#842840)

* Fri Aug 31 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.07-1
- Update to 4.07 release (Fix #845636 CSTP write stall handling)

* Mon Jul 23 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.06-1
- Update to 4.06 release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.05-1
- Update to 4.05 release (PKCS#11 fixes)

* Thu Jul 05 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.04-1
- Update to 4.04 release (Fix PKCS#8 password handling)

* Mon Jul 02 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.03-1
- Update to 4.03 release (#836558)

* Thu Jun 28 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.02-1
- Update to 4.02 release

* Thu Jun 28 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.01-1
- Update to 4.01 release

* Thu Jun 21 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.00-3
- Remove zlib from openconnect.pc dependencies

* Thu Jun 21 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.00-2
- Fix dependencies for RHEL[56]

* Wed Jun 20 2012 David Woodhouse <David.Woodhouse@intel.com> - 4.00-1
- Update to 4.00 release

* Wed Jun 20 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.99-8
- Add support for building on RHEL[56]

* Wed Jun 20 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.99-7
- Add OpenSSL encrypted PEM file support for GnuTLS

* Mon Jun 18 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.99-6
- Fix crash on cleanup when no client certificate is set (#833141)

* Sat Jun 16 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.99-5
- Enable building compatibility libopenconnect.so.1

* Thu Jun 14 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.99-4
- Last patch needs autoreconf

* Thu Jun 14 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.99-3
- Fix library not to reference OpenSSL symbols when linked against GnuTLS 2

* Thu Jun 14 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.99-2
- Fix GnuTLS BuildRequires

* Thu Jun 14 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.99-1
- Update to OpenConnect v3.99, use GnuTLS (enables PKCS#11 support)

* Sat May 19 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.20-2
- openconnect-devel package should require precisely matching openconnect

* Fri May 18 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.20-1
- Update to 3.20.

* Thu May 17 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.19-1
- Update to 3.19.

* Thu Apr 26 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.18-1
- Update to 3.18.

* Fri Apr 20 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.17-1
- Update to 3.17.

* Sun Apr 08 2012 David Woodhouse <David.Woodhouse@intel.com> - 3.16-1
- Update to 3.16.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.15-1
- Update to 3.15.

* Fri Sep 30 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.14-1
- Update to 3.14.

* Fri Sep 30 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.13-1
- Update to 3.13. (Add localisation support, --cert-expire-warning)

* Mon Sep 12 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.12-1
* Update to 3.12. (Fix DTLS compatibility issue with new ASA firmware)

* Wed Jul 20 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.11-1
- Update to 3.11. (Fix compatibility issue with servers requiring TLS)

* Thu Jun 30 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.10-1
- Update to 3.10. (Drop static library, ship libopenconnect.so.1)

* Tue Apr 19 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.02-2
- Fix manpage (new tarball)

* Tue Apr 19 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.02-1
- Update to 3.02.

* Thu Mar 17 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.01-2
- Provide openconnect-devel-static (#688349)

* Wed Mar  9 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.01-1
- Update to 3.01.

* Wed Mar  9 2011 David Woodhouse <David.Woodhouse@intel.com> - 3.00-1
- Update to 3.00.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.26-4
- Fix bug numbers in changelog

* Wed Sep 29 2010 jkeating - 2.26-3
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.26-1
- Update to 2.26. (#629979: SIGSEGV in nm-openconnect-auth-dialog)

* Thu Aug 12 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.25-2
- Rebuild for new libproxy

* Sat May 15 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.25-1
- Update to 2.25.

* Fri May  7 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.24-1
- Update to 2.24.

* Fri Apr  9 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.23-1
- Update to 2.23.

* Sun Mar  7 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.22-1
- Update to 2.22. (Works around server bug in ASA version 8.2.2.5)

* Sun Jan 10 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.21-1
- Update to 2.21.

* Mon Jan  4 2010 David Woodhouse <David.Woodhouse@intel.com> - 2.20-1
- Update to 2.20.

* Mon Dec  7 2009 David Woodhouse <David.Woodhouse@intel.com> - 2.12-1
- Update to 2.12.

* Tue Nov 17 2009 David Woodhouse <David.Woodhouse@intel.com> - 2.11-1
- Update to 2.11.

* Wed Nov  4 2009 David Woodhouse <David.Woodhouse@intel.com> - 2.10-1
- Update to 2.10.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.01-3
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 David Woodhouse <David.Woodhouse@intel.com> - 2.01-1
- Update to 2.01.

* Wed Jun  3 2009 David Woodhouse <David.Woodhouse@intel.com> - 2.00-1
- Update to 2.00.

* Wed May 27 2009 David Woodhouse <David.Woodhouse@intel.com> - 1.40-1
- Update to 1.40.

* Wed May 13 2009 David Woodhouse <David.Woodhouse@intel.com> - 1.30-1
- Update to 1.30.

* Fri May  8 2009 David Woodhouse <David.Woodhouse@intel.com> - 1.20-1
- Update to 1.20.

* Tue Apr 21 2009 David Woodhouse <David.Woodhouse@intel.com> - 1.10-2
- Require openssl0.9.8k-4, which has all required DTLS patches.

* Wed Apr  1 2009 David Woodhouse <David.Woodhouse@intel.com> - 1.10-1
- Update to 1.10.

* Wed Mar 18 2009 David Woodhouse <David.Woodhouse@intel.com> - 1.00-1
- Update to 1.00.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.99-2
- rebuild with new openssl

* Tue Dec 16 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.99-1
- Update to 0.99.
- Fix BuildRequires

* Mon Nov 24 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.98-1
- Update to 0.98.

* Thu Nov 13 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.97-1
- Update to 0.97. Add man page, validate server certs.

* Tue Oct 28 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.96-1
- Update to 0.96. Handle split-includes, MacOS port, more capable SecurID.

* Thu Oct 09 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.95-1
- Update to 0.95. A few bug fixes.

* Thu Oct 09 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.94-3
- Include COPYING.LGPL file

* Tue Oct 07 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.94-2
- Fix auth-dialog crash

* Mon Oct 06 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.94-1
- Take cookie on stdin so it's not visible in ps.
- Support running 'script' and passing traffic to it via a socket
- Fix abort when fetching XML config fails

* Sun Oct 05 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.93-1
- Work around unexpected disconnection (probably OpenSSL bug)
- Handle host list and report errors in NM auth dialog

* Sun Oct 05 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.92-1
- Rename to 'openconnect'
- Include NetworkManager auth helper

* Thu Oct 02 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.91-1
- Update to 0.91

* Thu Oct 02 2008 David Woodhouse <David.Woodhouse@intel.com> - 0.90-1
- First package
