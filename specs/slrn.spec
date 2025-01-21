Summary: A threaded Internet news reader
Name: slrn
Version: 1.0.3a
Release: 18%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://slrn.sourceforge.net/
Source0: http://jedsoft.org/releases/%{name}/%{name}-%{version}.tar.bz2
Source1: slrn-pull-expire
Source2: slrnpull.log
Source4: README.rpm-slrnpull
Source5: http://jedsoft.org/releases/%{name}/%{name}-%{version}.tar.bz2.asc
# 2016-06-09:
# Merged GPG keys from https://rg3.github.io/youtube-dl/download.html in one file
# gpg --export  --export-options export-minimal "428D F5D6 3EF0 7494 BB45 5AC0 EBF0 1804 BCF0 5F6B" \
# "ED7F 5BF4 6B3B BED8 1C87 368E 2C39 3E0F 18A9 236D" \
# "7D33 D762 FD6C 3513 0481 347F DB4B 54CB A482 6A18" > youtube-dl-gpgkeys.gpg
Source6: %{name}-gpgkeys.gpg
# Do not strip binaries by make install
Patch1: slrn-1.0.2-Do-not-strip-binaries.patch
Patch2: slrn-0.9.9pre108-sendmail.patch
Patch3: fix-FSF-address.patch
Patch4: slrn-configure-c99.patch
# Patch4: slrn-dont-limit-signatures.patch
BuildRequires: make
BuildRequires: inews
BuildRequires: openssl-devel, gcc
BuildRequires: slang-devel >= 2.2.3
# Some s-lang scripts (smime.sl) use slsh interpreter
Requires:      slang-slsh
Requires(pre): shadow-utils
# For source verification with gpgv
BuildRequires:  gnupg2

%description
SLRN is a threaded Internet news reader. SLRN is highly customizable
and allows users to design complex filters for sorting or killing news
articles. SLRN works well over slow network lines. A helper utility
for reading news offline is provided in the slrn-pull package.

%package pull
Summary: Offline news reading support for the SLRN news reader
Requires: slrn%{?_isa} = %{version}-%{release}
Requires: crontabs

%description pull
The slrn-pull package provides the slrnpull utility, which allows you
to set up a small news spool for offline news reading using the SLRN
news reader. You also need to have the slrn package installed to use
the slrnpull utility.

%prep
%define shortver %(echo %{version}|tr -d 'a')
gpgv2 --quiet --keyring %{SOURCE6} %{SOURCE5} %{SOURCE0}
%setup -q -n %{name}-%{shortver}
%patch -P1 -p1 -b .nostrip
%patch -P2 -p1 -b .sendmail
%patch -P3 -p1 -b .FSFaddress
%patch -P4 -p1
#%#patch4 -p1 -b .longsignatures

for i in changes.txt; do
  iconv -f iso8859-1 -t utf8 -o ${i}{_,} && touch -r ${i}{,_} && mv -f ${i}{_,}
done

chmod 644 doc/slrnpull/* contrib/*

%build
%configure \
    --with-ssl=%{_prefix} \
    --without-nss-compat \
    --with-slrnpull=%{_var}/spool/slrnpull \
    --without-x \
    --enable-charmap \
    --enable-emph-text \
    --enable-inews \
    --enable-nls \
    --enable-nntp \
    --disable-rpath \
    --enable-setgid-code \
    --enable-spoilers \
    --enable-warnings
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m644 doc/slrn.rc $RPM_BUILD_ROOT%{_sysconfdir}/slrn.rc

# slrnpull stuff
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{cron.daily,logrotate.d}
install -d $RPM_BUILD_ROOT%{_var}/spool/slrnpull/out.going
install -p doc/slrnpull/slrnpull.conf $RPM_BUILD_ROOT%{_var}/spool/slrnpull
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/slrn-pull
install -p -m644 %{SOURCE4} doc/slrnpull/README.rpm

%find_lang %{name}

# remove unpackaged files from the buildroot
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/slrn

# Static UID and GID defined by /usr/share/doc/setup-*/uidgid
%pre
getent group news >/dev/null || groupadd -r -g 13 news
getent passwd news >/dev/null || \
  useradd -r -u 9 -g news -d / -s /sbin/nologin -c "news user" news
exit 0

%files -f %{name}.lang
%license COPYING COPYRIGHT
%doc changes.txt NEWS README
%doc doc/FAQ doc/FIRST_STEPS doc/README.* doc/THANKS doc/*.txt doc/slrn*.html
%doc doc/score.sl contrib
%config(noreplace) %{_sysconfdir}/slrn.rc
%{_bindir}/slrn
%{_datadir}/slrn
%{_mandir}/man1/slrn.1*

%files pull
%doc doc/slrnpull/*
%config(noreplace) %{_sysconfdir}/cron.daily/slrn-pull-expire
%config(noreplace) %{_sysconfdir}/logrotate.d/slrn-pull
%{_bindir}/slrnpull
%attr(775,news,news) %dir %{_var}/spool/slrnpull
%attr(3777,news,news) %dir %{_var}/spool/slrnpull/out.going
%attr(644,news,news) %config(noreplace) %{_var}/spool/slrnpull/slrnpull.conf
%{_mandir}/man1/slrnpull.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3a-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 04 2023 Florian Weimer <fweimer@redhat.com> - 1.0.3a-13
- Port configure script to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.3a-9
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Matěj Cepl <mcepl@redhat.com> - 1.0.3a-1
- Upgrade to the latest upstream release.

* Mon Feb 19 2018 Matěj Cepl <mcepl@redhat.com> - 1.0.2-9
- Add gcc as BuildRequires and remove obsolete Groups, and remove one
  FSF address.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Petr Pisar <ppisar@redhat.com> - 1.0.2-2
- Use OpenSSL instead of NSS for cryptography

* Thu Dec 11 2014 Petr Pisar <ppisar@redhat.com> - 1.0.2-1
- 1.0.2 bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 1.0.1-4
- Handle crontab files according to new guidelines
- slrnpull-expire crontab file renamed to slrn-pull-expire

* Tue Mar 05 2013 Petr Pisar <ppisar@redhat.com> - 1.0.1-3
- Require slang-slsh

* Mon Feb 11 2013 Petr Pisar <ppisar@redhat.com> - 1.0.1-2
- Improve README.rpm-slrnpull spelling
- Create news user and group on installation
- Rotate log as news user (bug #909660)
- Run slrnpull-expire cron job with a shell (bug #909661)

* Tue Jan 08 2013 Petr Pisar <ppisar@redhat.com> - 1.0.1-1
- 1.0.1 bump

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9p1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9p1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9p1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9p1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 30 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.9.9p1-1
- update to 0.9.9p1

* Tue Aug 26 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.9.9-1
- update to 0.9.9

* Mon Jun 09 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.9.9-0.1.pre108
- update to 0.9.9-pre108
- enable inews support
- remove -D_GNU_SOURCE from CFLAGS

* Wed Feb 13 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.9.8.1pl1-8.20070716cvs
- fix building with new glibc headers

* Wed Jan 30 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.9.8.1pl1-7.20070716cvs
- convert changes.txt to utf8, rename logrotate file, remove
  setgid from slrnpull, fix source URL (#226422)

* Tue Jan 15 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.9.8.1pl1-6.20070716cvs
- add release to slrn-pull requirement (#226422)

* Fri Nov 02 2007 Miroslav Lichvar <mlichvar@redhat.com> 0.9.8.1pl1-5.20070716cvs
- drop asearch patch (#363781)

* Tue Oct 16 2007 Miroslav Lichvar <mlichvar@redhat.com> 0.9.8.1pl1-4.20070716cvs
- don't use gethostbyname

* Fri Aug 24 2007 Miroslav Lichvar <mlichvar@redhat.com> 0.9.8.1pl1-3.20070716cvs
- update license tag
- update from CVS
- switch from OpenSSL to NSS

* Thu Feb 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 0.9.8.1pl1-2
- fix author search (#229597)
- spec cleanup

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9.8.1pl1-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9.8.1pl1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9.8.1pl1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Nov 26 2005 Jindrich Novy <jnovy@redhat.com> 0.9.8.1pl1-1
- update to the latest slrn-0.9.8.1pl1 with slang2 support

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 0.9.8.1-7
- rebuilt against new openssl (again)

* Wed Nov  9 2005 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-6
- rebuild to fix broken dependencies to libssl and libcrypto

* Wed Jul 27 2005 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-5
- apply official bugfix patches (#164363)
  - fixes slrnpull problem with group containing no headers
  - fixes last character removal editor problem

* Mon Mar  7 2005 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-4
- fix type confusions reported by gcc4
- add RPM_OPT_FLAGS to CFLAGS
- rebuilt with gcc4

* Mon Dec 27 2004 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-3
- package contrib subdir because of slrn-conv script (#73451)
- slrnpull.conf is now %%config(noreplace), original config
  won't be overwritten (#56001)
- include slrnpull man page

* Fri Nov 26 2004 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-2
- include translations to srln package (#140870)
- remove upstreamed patches

* Mon Oct 11 2004 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-1
- update to 0.9.8.1

* Wed Oct 06 2004 Jindrich Novy <jnovy@redhat.com> 0.9.8.0-1
- update to 0.9.8.0
- execute runuser instead of su in slrnpull-expire #134597

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.9.7.4-8
- rebuild

* Fri Jan 03 2003 Florian La Roche <Florian.LaRoche@redhat.de> 0.9.7.4-7
- make /etc/slrn.rc mode 0644

* Fri Dec 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- use openssl pkg-config data, if available

* Wed Dec 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.9.7.4-6
- configure with --with-ssl-includes=%%{_includedir} and
  --with-ssl-library=%%{_libdir}, for multilib systems

* Wed Dec 11 2002 Tim Powers <timp@redhat.com>
- remove unpackaged files from the buildroot

* Tue Jul  9 2002 Bill Nottingham <notting@redhat.com> 0.9.7.4-5
- fix it to build and work with utf-8 slang

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jun 14 2002 Bill Nottingham <notting@redhat.com> 0.9.7.4-3
- rebuild against new slang

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Mar 14 2002 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.4

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Dec  4 2001 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.3, reorganize specfile some
- note that slrn.rc moves from /usr/lib/slrn to /etc

* Wed Aug 29 2001 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.2

* Mon Jul 23 2001 Bill Nottingham <notting@redhat.com>
- add openssl buildprereq (#49699)

* Sat Jul 21 2001 Tim Powers <timp@redhat.com>
- remove the applnk file. It's cluttering our menus

* Wed Jul 18 2001 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.1

* Mon Apr 16 2001 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.0a, tweak URLs

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Nov 28 2000 Bill Nottingham <notting@redhat.com>
- update to 0.9.6.4
- enable SSL
- plug some possible buffer overflows (#12750)
- install sample macros in /usr/lib/slrn

* Wed Aug 16 2000 Bill Nottingham <notting@redhat.com>
- tweak summary/description

* Fri Aug  4 2000 Bill Nottingham <notting@redhat.com>
- add translation to desktop entry

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Bill Nottingham <notting@redhat.com>
- make slrnpull root.news, not news.news (#12428)

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- fix startup (#11658)
- fix manpage (#11973)

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig -> desktop

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix descriptions
- man pages are compressed

* Thu Jan  6 2000 Bill Nottingham <notting@redhat.com>
- fix typo in slrn.rc file

* Thu Dec 30 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.6.2

* Mon Dec 20 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.6.0

* Wed Jul 21 1999 Bill Nottingham <notting@redhat.com>
- fix perms on slrnpull logrotate

* Fri Jul 16 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.7

* Mon May 17 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.6

* Thu May  6 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.5

* Fri Apr 23 1999 Bill Nottingham <notting@redhat.com>
- make slrnpull setgid news

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- make slrnpull/log missingok

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- return of wmconfig

* Mon Nov  9 1998 Bill Nottingham <notting@redhat.com>
- add bugfix patch from jed

* Fri Nov  6 1998 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.4

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- built for Raw Hide
- added bugfix patch

* Tue Sep 8 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.3-2]
- Fixed a couple of stupid things I did.
- Took out -fno-strength-reduce. AFAIK, gcc on RH5.1 doesn't have this bug. I
  use egcs which shouldn't have this bug. And if you have this bug, *and* are
  recompiling on your own machin, you should have -fno-strength-reduce in your
  RPM_OPT_FLAGS anyway.

* Tue Sep 8 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.3-1]
- Updated to 0.9.5.3

* Mon Jun 1 1998 Manoj Kasichainula <manojk+rpm@io.com>
- added translations from RH 5.1 (still none for slrn-pull package)

* Mon May 4 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.2-1]
- updated to 0.9.5.2

* Wed Apr 22 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.1-1]
- updated to 0.9.5.1

* Sun Apr 12 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.4.6-3]
- updated to require slang 1.2.1

* Sun Apr 12 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.4.6-2]
- updated to require slang 1.2.0

* Wed Feb 11 1998 Manoj Kasichainula <manojk+rpm@io.com>
(my unreleased 0.9.4.6-1)
- updated to 0.9.4.6

* Tue Feb 3 1998 Manoj Kasichainula <manojk+rpm@io.com>
- docs are now forced to 644 to prevent including /bin/sh as a requirement
- added macros in the doc directory
- should now be buildable by non-root

* Thu Jan 29 1998 Bill Nottingham <wen1@cec.wustl.edu>
- updated to 0.9.4.5
- added wmconfig entry

* Sat Sep 13 1997 Manoj Kasichainula <manojk+rpm@io.com> (0.9.4.3-2)
- Fixes from JED
- default mode for slrnpull posts set to 0640, so slrnpull can read it as
  non-root
- lots of pre-setup for slrnpull
  - directories set up
  - automatic daily expiration
  - moved slrnpull directory to /var/spool/slrnpull, to match (most) docs
  - more
- minor spec file changes

* Sat Jul 12 1997 Manoj Kasichainula <manojk+rpm@io.com> (0.9.4.3-1)
- Initial release for 0.9.4.3
