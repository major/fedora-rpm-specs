Name:           libetpan
Version:        1.9.4
Release:        17%{?dist}
Summary:        Portable, efficient middle-ware for different kinds of mail access

# src/bsd/getopt.c BSD-4-Clause (not used)
# src/data-types/timeutils.c BSD-3-Clause-Attribution AND BSD-4-Clause
# SPDX confirmed
License:        BSD-3-Clause AND BSD-3-Clause-Attribution AND BSD-4-Clause
URL:            http://www.etpan.org/
Source0:        https://github.com/dinhviethoa/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# system crypto policy (see rhbz#1179310)
Patch10:        libetpan-1.9.2-cryptopolicy.patch
# Upstream patches
#
# CVE-2020-15953
# https://github.com/dinhvh/libetpan/issues/386
# Detect extra data after STARTTLS response and exit
# https://github.com/dinhvh/libetpan/pull/387
Patch101:       libetpan-1.9.4-0001-Detect-extra-data-after-STARTTLS-response-and-exit-3.patch
# Detect extra data after STARTTLS responses in SMTP and POP3 and exit
# https://github.com/dinhvh/libetpan/pull/388
Patch102:       libetpan-1.9.4-0002-Detect-extra-data-after-STARTTLS-responses-in-SMTP-a.patch
# https://github.com/dinhvh/libetpan/issues/420
Patch103:       libetpan-1.9.4-mailbox_data_status-info_list-invalid-free.patch
# https://github.com/dinhvh/libetpan/pull/423
Patch104:       libetpan-configure-c99.patch
# https://github.com/dinhvh/libetpan/pull/447
Patch105:		libetpan-pr447-fix-poll-logical-op.patch

BuildRequires:  gcc-c++
BuildRequires:  liblockfile-devel
BuildRequires:  libdb-devel < 5.4
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gnutls-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  autoconf automake
BuildRequires:  make
# disabled by default in configure.ac accidentally
# https://github.com/dinhviethoa/libetpan/issues/221
# libcurl and libexpat not needed by Claws Mail:
# http://lists.claws-mail.org/pipermail/users/2016-January/015665.html
#BuildRequires:  libcurl-devel expat-devel

%description
The purpose of this mail library is to provide a portable, efficient middle-ware
for different kinds of mail access. When using the drivers interface, the
interface is the same for all kinds of mail access, remote and local mailboxes.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the files needed for development
with %{name}.

%prep
%setup -q

#%patch0 -b .libetpan-config-script
sed -i.flags libetpan.pc.in \
    -e 's|-letpan@LIBSUFFIX@.*$|-letpan@LIBSUFFIX@|'
%patch -P10 -p1 -b .crypto-policy
%patch -P101 -p1 -b .CVE-2020-15953-1
%patch -P102 -p1 -b .CVE-2020-15953-2
%patch -P103 -p1 -b .CVE-2022-4121.tmp
%patch -P104 -p1 -b .c99
%patch -P105 -p1 -b .logical_op

# 2013-08-05 F20 development, bz 992070: The configure scripts adds some
# extra libs to the GnuTLS link options, which cause rebuilds to fail, since
# gnutls-devel no longer pulls in libgcrypt-devel libgpg-error-devel
# [The alternative fix is to BR those packages, of course.]
grep 'GNUTLSLIB="-lgnutls -lgcrypt -lgpg-error -lz"' configure.ac || exit -1
sed -i '\@GNUTLSLIB=@s!-lgcrypt -lgpg-error -lz!!g' configure.ac

env NOCONFIGURE=1 ./autogen.sh
cp -p %{_bindir}/libtool .

%build
#%global optflags %(echo %{optflags} | sed 's/-g /-g -Wno-format-truncation /')
# Use poll instead of select on F40 and above (bug 2283446)
%configure \
    --disable-static \
    --with-gnutls=yes \
    --with-openssl=no \
%if 0%{?fedora} >= 41
    --with-poll=yes \
%endif
    %{nil}

%make_build

cd doc
make doc

%install
%make_install

rm -rf $RPM_BUILD_ROOT%{_libdir}/libetpan.{,l}a

iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

%ldconfig_scriptlets

%files
%license COPYRIGHT
%doc ChangeLog NEWS
%{_libdir}/%{name}.so.20
%{_libdir}/%{name}.so.20.*

%files devel
%doc doc/API.html doc/README.html doc/DOCUMENTATION
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/libetpan/
%{_includedir}/libetpan.h
%{_libdir}/%{name}.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 28 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.4-15
- Use poll instead of select on F41 (bug 2283446)
- Update spec file a bit, including keeping timestamps

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Florian Weimer <fweimer@redhat.com> - 1.9.4-10
- Port configure script to C99

* Wed Nov 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.4-9
- Workaround for CVE-2022-4121 (bug 2144914)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.4-4
- Address CVE-2020-15953 (bug 1861068)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.4-1
- 1.9.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.3-1
- Update to 1.9.3.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.2-1
- Update to 1.9.2.
- rebase cryptopolicies patch
- tests-snprintf patch not needed anymore

* Sun Dec  9 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.1-0.1
- merge SNI pull request 315 (segfault in TLS SNI code with OpenSSL
  in the case that callbacks are not used).

* Sun Nov  4 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.1-1.t1
- merge SNI commits

* Sun Sep 16 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.9.1-1
- Build 1.9.1 release.
- Compile with -Wno-format-truncation (rhbz#1606913 comment 5)
- Fix off-by-one buffer size in tests/frm-simple.c

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Michael Schwendt <mschwendt@fedoraproject.org> - 1.8-1
- Build 1.8 release.
- Use license macro, remove clean, use auto-clean buildroot in install section.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 1.7.2-1
- version upgrade (rhbz#1330524)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Michael Schwendt <mschwendt@fedoraproject.org>
- 1.6-6
- disable BR libcurl-devel expat-devel since the configure script
  accidentally disables the detection of those libs anyway
- clean up "libetpan-config --libs" output (shall fix rhbz#1279395)
  as to not respecify LDFLAGS and shared libs / also frees the -devel
  package from several dependencies

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1.6-4
- Rebuild for gnutls SONAME bump (to match gnutls used by Claws Mail).

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 03 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 1.6-2
- utilize system-wide crypto-policy (rhbz#1179310)

* Sat Nov 01 2014 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.6-1
- version upgrade (rhbz#1159493)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.5-1
- version upgrade
- drop obsoleted patches

* Mon Aug  5 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1-7
- apply AArch64 autotools config.* patch (#925714)
- fix FTBFS (#992070)
- use %%_isa in -devel package Requires
- drop %%defattr usage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.1-5
- Build against liblockfile to avoid internal locking code
- Fix build against newer berkley db and add guard to cause build failure an
  even newer versions

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.1-1
- version upgrade (soname 16.0.0)
- drop upstreamed build fix
- spec cleanup

* Sun Apr 10 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.0.1-0.2.20110312cvs
- add BR zlib

* Sat Mar 12 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.0.1-0.1.20110312cvs
- upgrade to cvs to fix imap/gmail issues

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 11 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.0-1
- version upgrade

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.58-1
- version upgrade

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.57-1
- version upgrade
- switch to gnutls (fixed upstream)

* Mon Sep 08 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.56-1
- version upgrade

* Tue Jun 17 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.54-1
- version upgrade
- fix #451025

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0.52-5
- Rebuilt for gcc43

* Sat Jan 05 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.52-4
- fix #342021 multiarch

* Thu Dec 06 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.52-3
- bump

* Mon Nov 19 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.52-2
- bump

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.52-1
- version upgrade

* Sun Feb 25 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.49-2
- bump

* Wed Jan 17 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.49-1
- version upgrade

* Mon Nov 06 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.48-1
- version upgrade

* Thu Oct 19 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.47-1
- version upgrade

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.46-2
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.46-1
- version upgrade

* Wed Sep 13 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.45-2
- FE6 rebuild

* Thu Mar 23 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.45-1
- version upgrade

* Wed Feb 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.42-2
- Rebuild for Fedora Extras 5

* Fri Feb 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.42-1
- version upgrade

* Sun Dec 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.41-1
- version upgrade

* Thu Nov 17 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.40-1
- version upgrade

* Fri Sep 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.39.1-1
- version upgrade

* Sat Aug 13 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.38-4
- add dist tag

* Mon Aug 08 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.38-3
- remove some doc
- build without gnutls

* Sun Jul 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.38-2
- add documentation
- add more Requires/BuildRequires
- build with gnutls support

* Sun Jul 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.38-1
- Initial Release
