%define moddir	%(apxs -q LIBEXECDIR || echo be_happy_mock)
%define svn	20070129svn713

Summary: NTLM authentication for the Apache web server using winbind daemon
Name: mod_auth_ntlm_winbind
Version: 0.0.0
Release: 0.40.%{svn}%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: http://viewcvs.samba.org/cgi-bin/viewcvs.cgi/trunk/mod_auth_ntlm_winbind/?root=lorikeet

#
#   svn export svn://svnanon.samba.org/lorikeet/trunk/mod_auth_ntlm_winbind mod_auth_ntlm_winbind
# or:
#   wget -r -nH --cur-dirs=3 ftp://ftp.samba.org/pub/unpacked/lorikeet/mod_auth_ntlm_winbind
# then:
#   tar -cvf - mod_auth_ntlm_winbind/ | gzip -c -9 > mod_ntlm_winbind-VERSION-SVN.tar.gz
#
Source0: mod_auth_ntlm_winbind-%{version}-%{svn}.tar.gz

Source1: auth_ntlm_winbind.conf

BuildRequires: make
BuildRequires:  gcc
BuildRequires: httpd-devel >= 2.0.40, autoconf
Requires: httpd >= 2.0.40
Requires: httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing)
# requires samba-common for /usr/bin/ntlm_auth ...
Requires: samba-common
Requires(post): shadow-utils

Patch0: mod_auth_ntlm_winbind-20060510-connect_http10.patch
Patch1: mod_auth_ntlm_winbind-20070129-64bit.patch


%description
The %{name} module allows authentication and authorisation over
the Web against a Windows NT/AD domain controllers, using Samba on the same
machine Apache is running on.
It uses "ntlm_auth" helper utility to operate with local winbindd(8) daemon,
which are standard parts of the Samba distribution.

The same way Squid does NTLM authentication now.


%prep
%setup -q -n mod_auth_ntlm_winbind
%patch -P0 -p1
%patch -P1 -p1
autoconf


%build
%configure

# %{?_smp_mflags} is not needed -- only one file compiled
make


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{moddir}
make install DESTDIR=$RPM_BUILD_ROOT

# Install the config file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d



%post
/usr/sbin/usermod -a -G wbpriv apache >/dev/null 2>&1 || :
 

%files
%{moddir}/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%doc AUTHORS README


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.40.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.0-0.39.20070129svn713
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.38.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.37.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.36.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.35.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.34.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.33.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.32.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.31.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.30.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.29.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.28.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.27.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.26.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.25.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.24.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.23.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.22.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.21.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.20.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.19.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.18.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.17.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.16.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.15.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.14.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Dmitry Butskoy <Dmitry@Butskoy.name> 0.0.0-0.13.20070129svn713
- Rebuilt for new httpd

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.12.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.11.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.10.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-0.9.20070129svn713
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Apr  4 2008 Dmitry Butskoy <Dmitry@Butskoy.name> 0.0.0-0.8.20070129svn713
- note in config that Apache's "KeepAlive" must be "On" (#440446)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.0-0.7.20070129svn713
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.0-0.6.20070129svn713
- Rebuild for selinux ppc32 issue.

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to "ASL 2.0"

* Fri Jun 22 2007 Dmitry Butskoy <Dmitry@Butskoy.name> 0.0.0-0.5.20070129svn713
- avoid gcc warnings on 64 bit systems

* Wed Jun 20 2007 Dmitry Butskoy <Dmitry@Butskoy.name> 0.0.0-0.2.20070129svn713
- spec file cleanup
- accepted for Fedora (review by Jason Tibbitts <tibbs@math.uh.edu>)

* Wed Jun 13 2007 Dmitry Butskoy <Dmitry@Butskoy.name> 0.0.0-0.1.20070129svn713
- change release field properly

* Mon Mar 26 2007 Dmitry Butskoy <Dmitry@Butskoy.name> 0.0.0-0.svn713.1
- update to svn release 713
- special winbind's group is named "wbpriv" now

* Thu Dec 21 2006 Dmitry Butskoy <Dmitry@Butskoy.name> 0.0.0-0.svn692.1
- new initial release (svn version r692)
- add workaround patch for "CONNECT HTTP/1.0" proxy issue
- add post script for access to winbind's socket directory

