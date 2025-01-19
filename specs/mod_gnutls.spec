%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
Name:      mod_gnutls
Version:   0.12.0
Release:   12%{?dist}
Summary:   GnuTLS module for the Apache HTTP server
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:   Apache-2.0
URL:       http://mod.gnutls.org/
Source0:   https://mod.gnutls.org/downloads/%{name}-%{version}.tar.bz2
Source1:   mod_gnutls.conf
ExcludeArch: %{ix86}  %{arm}
BuildRequires: make
BuildRequires: gnutls-devel, gnutls-utils, httpd-devel, apr-util-devel >= 1.3, libtool, autoconf, automake, softhsm-devel, python3, python3-pyyaml
Requires:  apr-util >= 1.3, gnutls-utils, httpd-mmn = %{_httpd_mmn}

%description
mod_gnutls uses the GnuTLS library to provide SSL 3.0, TLS 1.0 and TLS 1.1
encryption for Apache HTTPD.  It is similar to mod_ssl in purpose, but does
not use OpenSSL.  A primary benefit of using this module is the ability to
configure multiple SSL certificates for a single IP-address/port combination
(useful for securing virtual hosts).
    
Features
    * Support for SSL 3.0, TLS 1.0 and TLS 1.1.
    * Support for client certificates.
    * Support for RFC 5081 OpenPGP certificate authentication.
    * Support for Server Name Indication.
    * Distributed SSL Session Cache via Memcached
    * Local SSL Session Cache using DBM
    * Sets enviromental vars for scripts (compatible with mod_ssl vars)
    * Small and focused code base:
         Lines of code in mod_gnutls: 3,593
         Lines of code in mod_ssl: 15,324

%prep
%setup -q
cp %{SOURCE1} .

%build
rm -f configure
export APR_MEMCACHE_LIBS="`apu-1-config --link-ld`"
export APR_MEMCACHE_CFLAGS="`apu-1-config --includes`"
autoreconf -f -i

rm -rf autom4te.cache

%configure %{?_httpd_apxs:--with-apxs=%{_httpd_apxs}}
%{__make} %{?_smp_mflags}

%check
# missing dependencies for running test
# %{__make} check

%install
rm -rf %{buildroot}
%{__install} -m 755 -D src/.libs/mod_gnutls.so %{buildroot}%{_libdir}/httpd/modules/mod_gnutls.so
%{__install} -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_gnutls.conf

%pre
rm -fr %{_localstatedir}/cache/mod_gnutls

%files
%doc README NOTICE LICENSE 
%{_libdir}/httpd/modules/*.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_gnutls.conf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.12.0-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jiri Kastner <jkastner@fedoraproject.org> - 0.12.0-4
- exclude armhfp architecture

* Mon May 30 2022 Jiri Kastner <jkastner@fedoraproject.org> - 0.12.0-3
- exclude i686 architecture

* Mon May 30 2022 Jiri Kastner <jkastner@fedoraproject.org> - 0.12.0-2
- add missing build requirements

* Mon May 30 2022 Jiri Kastner <jkastner@fedoraproject.org> - 0.12.0-1
- update to 0.12.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Jiri Kastner <jkastner@redhat.com> - 0.9.0-1
- update to 0.9.0

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.8.4-3
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Jiri Kastner <jkastner@redhat.com> - 0.8.4-1
- update to 0.8.4

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.8.2-5
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Jiri Kastner <jkastner@redhat.com> - 0.8.2-1
- update to 0.8.2

* Wed Dec 21 2016 Jiri Kastner <jkastner@redhat.com> - 0.8.1-1
- update to 0.8.1

* Tue Dec 13 2016 Jiri Kastner <jkastner@redhat.com> - 0.8.0-1
- rebase to 0.8.0
- softhsm-devel added to dependency and comments to config file regarding selinux (rhbs#1250975)

* Mon Jun 13 2016 Jiri Kastner <jkastner@redhat.com> - 0.7.5-1
- rebase to 0.7.5 (rhbz#1339412)

* Sun Feb 14 2016 Jiri Kastner <jkastner@redhat.com> - 0.7.3-1
- rebase to 0.7.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Jiri Kastner <jkastner@redhat.com> - 0.7-2
- putting examples to mod_gnutls.conf (rhbz#1243837)

* Tue Jul 14 2015 Jiri Kastner <jkastner@redhat.com> - 0.7-1
- rebase to 0.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct  7 2014 Jiri Kastner <jkastner@redhat.com> - 0.6-1
- rebase to 0.6 (rhbz#1109115)

* Fri Oct  3 2014 Jiri Kastner <jkastner@redhat.com> - 0.5.10-14
- fix change to use system policy (rhbz#1109115) only on newer fedoras

* Fri Sep 12 2014 Jiri Kastner <jkastner@redhat.com> - 0.5.10-13
- config change to use system policy (rhbz#1109115)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 0.5.10-10
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar  7 2013 Tomáš Mráz <tmraz@redhat.com> - 0.5.10-8
- fix build with new GnuTLS

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Joe Orton <jorton@redhat.com> - 0.5.10-6
- fix build w/httpd 2.4

* Tue Mar 27 2012 Jiri Kastner <jkastner@redhat.com> - 0.5.10-5
- httpd 2.4 rebuild

* Mon Mar 19 2012 Jiri Kastner <jkastner@redhat.com> - 0.5.10-4
- removed httpd require

* Wed Mar 14 2012 Jiri Kastner <jkastner@redhat.com> - 0.5.10-3
- added dependency for httpd-mmn

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Jiri Kastner <jkastner@redhat.com> - 0.5.10-1
- apr_memcache.m4 modified for correct cheking of apr_memcache in apr-util
- removed /var/cache/mod_gnutls from 'files' and 'install' stanzas
- added 'pre' stanza for removal of old cache
- update to 0.5.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 17 2009 Erick Calder <rpm@arix.com> - 0.5.5-5
- removed use of define {ooo}

* Thu Sep 17 2009 Erick Calder <rpm@arix.com> - 0.5.5-4
- dependency generator missed need for httpd.  added by hand.
- abstracted Source0:

* Tue Sep 15 2009 Erick Calder <rpm@arix.com> - 0.5.5-3
- mention of SRP removed from description of package
- added httpd-devel to build requires
- fixed license (harmonized with httpd)

* Tue Sep 15 2009 Erick Calder <rpm@arix.com> - 0.5.5-2
- Added BuildRequires
- removed comments stating the specfile was generated by cpan2rpm
- added BuildRoot
- added install clean

* Fri Sep 11 2009 Erick Calder <rpm@arix.com> - 0.5.5-2
- Initial build

