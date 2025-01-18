%global patchlevel 302

Summary:       The quintessential all-purpose communications program
Name:          ckermit
Version:       9.0.%{patchlevel}
Release:       36%{?dist}
# Most of the package is under a three-clause BSD license, but the file
# ckaut2.h appears to be covered by three licenses:
#   The blanket license in COPYING.TXT and ckcmai.c, which is BSD three-clause
#   BSD four-clause (w/ advertising)
#   MIT Old Style (no advertising without permission)
License:       BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND BSD-4-Clause-UC AND NTP AND X11
Source0:       ftp://ftp.kermitproject.org/kermit/archives/cku%{patchlevel}.tar.gz
Source1:       ckermit.ini
Source2:       cku-%{name}.local.ini
Source3:       cku-%{name}.modem.generic.ini
Source4:       cku-%{name}.locale.ini
Source5:       cku-%{name}.phone
Source6:       README.fedora
# See: https://bugs.gentoo.org/669332
Patch0:        ckermit-9.0.302-fix_build_with_glibc_2_28_and_earlier.patch
Patch1:        ckermit-9.0.302-printw.patch
# C99 fixes - unneeded for ckermit 10
Patch2:        ckermit-9.0.302-fedora-c99.patch
URL:           http://www.kermitproject.org/ck90.html
BuildRequires: gcc
BuildRequires: pam-devel
BuildRequires: pkgconfig
BuildRequires: openssl-devel >= 0.9.7
BuildRequires: gmp-devel >= 3.1.1
BuildRequires: ncurses-devel
BuildRequires: lockdev-devel >= 1.0.1-8
BuildRequires: make

Requires:      lockdev >= 1.0.1-8
# NB There used to be a spurious "Obsoletes: gkermit" line here, but ckermit
# does NOT obsolete gkermit. They are independent programs with different
# purposes.

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, cross-platform
approach to connection establishment, terminal sessions, file transfer
and management, character-set translation, and automation of
communication tasks.

%prep
%setup -q -c
cp %{SOURCE6} .
%patch -P 0 -p 1 -b .glibc2_28
%patch -P 1 -p 1 -b .printw
%patch -P 2 -p 1 -b .c99

%build
%make_build linux \
        KFLAGS="-O0 $RPM_OPT_FLAGS -Wall -DOPENSSL_097 -Dsdata=s_data -DHAVE_OPENPTY -D'krb5_init_ets(__ctx)=' -DMAINTYPE=int" \
        LNKFLAGS="%{?optflags} %{?__global_ldflags}" \
        K4LIB= \
        K4INC= \
        K5LIB=-lutil \
        K5INC=-I%{_includedir}/et \
        SSLLIB= \
        SSLINC= \
;

# convert doc file from ISO-8859-1 to UTF-8 encoding
for f in ckc%{patchlevel}.txt ; do
    iconv -fiso88591 -tutf8 $f >$f.new
    touch -r $f $f.new
    mv $f.new $f
done

%install
install -D -m 0755 wermit %{buildroot}%{_bindir}/kermit
install -D -m 0644 ckuker.nr %{buildroot}%{_mandir}/man1/kermit.1
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/kermit/ckermit.ini
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/kermit/ckermit.local.ini
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/kermit/ckermit.modem.ini
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/kermit/ckermit.locale.ini
install -D -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/kermit/ckermit.phone

%files
%license COPYING.TXT
%doc ckc%{patchlevel}.txt
%doc README.fedora
%{_bindir}/kermit
%dir %{_sysconfdir}/kermit
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kermit/*
%{_mandir}/man1/kermit.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 21 2023 David Cantrell <dcantrell@redhat.com> - 9.0.302-32
- Drop perl-interpreter BuildRequires
- Do not modify the ckermit.ini file in the source tree
- Use non-deprecated %%patch macro syntax in %%prep
- Convert license tag to SPDX

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 DJ Delorie <dj@redhat.com> - 9.0.302-30
- Fix C99 compatibility issue

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 David Cantrell <dcantrell@redhat.com> - 9.0.302-28
- Fix FTBFS (#2113148)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 David Cantrell <dcantrell@redhat.com> - 9.0.302-22
- Drop BR libtermcap-devel (#1799227)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 9.0.302-18
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jan 05 2019 Björn Esser <besser82@fedoraproject.org> - 9.0.302-17
- Add patch to fix build with glibc 2.28 and earlier (#1603648)
- Apply LDFLAGS properly
- Use %%make_build macro
- Mark COPYING file as %%license

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 9.0.302-14
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 9.0.302-11
- Add BR: perl (Fix F26FTBS).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.302-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.302-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.302-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.302-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.302-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.302-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.302-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.302-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Eric Smith <eric@brouhaha.com> - 9.0.302-1
- removed definition of HAVE_BAUDBOY from make invocation (#747923)
- updated to latest upstream (no changes that affect Fedora, but
  cku301 tarball is no longer available
- updated URL and Source tags for kermitproject.org
- added README.fedora

* Mon Jul 11 2011 Eric Smith <eric@brouhaha.com> - 9.0.301-1
- updated to final release

* Fri Jun 24 2011 Eric Smith <eric@brouhaha.com> - 9.0-0.1.beta2
- updated to upstream 9.0 beta 2 release

* Mon Jul 03 2006 Peter Vrabec <pvrabec@redhat.com> - 8.0.211-5
- fix requires (#195573)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 8.0.211-4.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 8.0.211-4.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov  8 2005 Tomas Mraz <tmraz@redhat.com> 8.0.211-4
- rebuilt with new openssl

* Wed Aug 31 2005 Peter Vrabec <pvrabec@redhat.com> 8.0.211-3
- use baudboy.h to create per-device lock(s) in /var/lock (#166155)

* Fri Jul 29 2005 Peter Vrabec <pvrabec@redhat.com> 8.0.211-2
- use openpty library (#156417,#164465)

* Wed Mar 15 2005 Nalin Dahyabhai <nalin@redhat.com> 8.0.211-1
- update to 211

* Mon Feb 28 2005 Nalin Dahyabhai <nalin@redhat.com>
- remove now-unnecessary use of krb5_init_ets()

* Thu Feb 08 2005 Peter Vrabec <pvrabec@redhat.com>
- rebuilt

* Tue Nov 02 2004 Peter Vrabec <pvrabec@redhat.com>
- fix ssh connection (#128349)

* Wed Oct 20 2004 Peter Vrabec <pvrabec@redhat.com>
- add BuildRequires: libtermcap-devel BuildRequires: ncurses-devel
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr  1 2004 Jeff Johnson <jbj@redhat.com> 8.0.209-7
- remove old copyright from description (#115952).

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 19 2004 Jeff Johnson <jbj@jbj.org> 8.0.209-5
- fix: printf arg lists cleaned up, (itsadir && !iswild(*xp)) (#113663)

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 8.0.209-4
- rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May  1 2003 Elliot Lee <sopwith@redhat.com> 8.0.209-2
- Define sdata=s_data to fix ppc64 build

* Mon Apr 21 2003 Jeff Johnson <jbj@redhat.com> 8.0.209-1
- update to 8.0.209.

* Wed Feb 26 2003 Jeff Johnson <jbj@redhat.com> 8.0.206-1.20030226
- build 20030226 snap shot (with errno fix) for raw hide.

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 8.0.206-0.6
- rebuild

* Tue Jan 21 2003 Jeff Johnson <jbj@redhat.com> 8.0.26-0.5
- remove "CLICK HERE" from description (#82133).

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 8.0.206-0.4
- rebuild

* Fri Jan  3 2003 Nalin Dahyabhai <nalin@redhat.com>
- Build using predefined redhat80 target
- Pass include and library paths for Kerberos and SSL directly to make
- Define OPENSSL_097 in KFLAGS to build with OpenSSL 0.9.7

* Thu Dec 12 2002 Elliot Lee <sopwith@redhat.com> 8.0.206-0.3
- Add patch2 to include errno.h
- Change cku-makefile to not build KRB4 & KRB524, because kerberosIV/des.h
  conflicts with openssl/des.h

* Fri Nov 29 2002 Jeff Johnson <jbj@redhat.com> 8.0.206-0.2
- obsolete gkermit

* Mon Nov 25 2002 Jeff Johnson <jbj@redhat.com> 8.0.206-0.1
- create (with thanks to PLD, who packaged C-Kermit before Red Hat did).
