%define _default_patch_fuzz 2

# GCC 10 uses -fno-common by default, turn it off for now
%define _legacy_common_support 1

%global dbtopdir  %{_var}/%{name}
%global dbhomedir %{_var}/%{name}/blacklists
%global cgibin    /var/www/cgi-bin

Name:           squidGuard
Version:        1.6.0
Release:        2%{?dist}
Summary:        Filter, redirector and access controller plugin for squid

License:        GPL-2.0-only
URL:            http://www.squidguard.org/

# Take sources from what Debian watches, squidguard.org is dead
Source0:        https://www.joonet.de/sources/squidguard/squidguard-%{version}.tar.gz

Source1:        squidGuard.logrotate
Source2:        http://squidguard.mesd.k12.or.us/blacklists.tgz
Source3:        http://cuda.port-aransas.k12.tx.us/squid-getlist.html

# K12LTSP stuff
Source100:      squidGuard.conf
Source101:      update_squidguard_blacklists
Source104:      squidGuard.service
Source105:      transparent-proxying.service
Source106:      squidGuard-helper
Source107:      transparent-proxying-helper

Patch2:         squid-getlist.html.patch
Patch3:         squidGuard-perlwarning.patch
Patch5:         squidGuard-makeinstall.patch
Patch14:        squidGuard-1.4-declarations.patch
# https://sources.debian.org/src/squidguard/1.6.0-6/debian/patches/11_fix-configure-check.patch
Patch15:        squidGuard-1.6.0-fix-configure-check.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros

BuildRequires:  openldap-devel
BuildRequires:  libdb-devel

Requires:       squid
%{?systemd_requires}

%description
squidGuard can be used to
- limit the web access for some users to a list of accepted/well known
  web servers and/or URLs only.
- block access to some listed or blacklisted web servers and/or URLs
  for some users.
- block access to URLs matching a list of regular expressions or words
  for some users.
- enforce the use of domainnames/prohibit the use of IP address in
  URLs.
- redirect blocked URLs to an "intelligent" CGI based info page.
- redirect unregistered user to a registration form.
- redirect popular downloads like Netscape, MSIE etc. to local copies.
- redirect banners to an empty GIF.
- have different access rules based on time of day, day of the week,
  date etc.
- have different rules for different user groups.
- and much more..

Neither squidGuard nor Squid can be used to
- filter/censor/edit text inside documents
- filter/censor/edit embeded scripting languages like JavaScript or
  VBscript inside HTML

%prep
%setup -q -n squidguard-%{version}
cp -p %{SOURCE3} .
%patch -P2 -p0
%patch -P3 -p2
%patch -P5 -p1
%patch -P14 -p1
%patch -P15 -p1

cp -p %{SOURCE100} ./squidGuard.conf.k12ltsp.template
cp -p %{SOURCE101} ./update_squidguard_blacklists.k12ltsp.sh

%build
./autogen.sh
%configure \
    --with-sg-config=%{_sysconfdir}/squid/squidGuard.conf \
    --with-sg-logdir=%{_var}/log/squidGuard \
    --with-sg-dbhome=%{dbhomedir} \
    --with-ldap=yes

%make_build

pushd contrib
%make_build
popd

%install
# "make install" is broken since 1.2.1, install by hand
install -p -D -m 0755 src/squidGuard %{buildroot}%{_bindir}/squidGuard

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/squidGuard
install -p -D -m 0644 samples/sample.conf %{buildroot}%{_sysconfdir}/squid/squidGuard.conf
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{dbtopdir}/blacklists.tar.gz

# Don't use SOURCE3, but use the already patched one #165689
install -p -D -m 0755 squid-getlist.html %{buildroot}%{_sysconfdir}/cron.daily/squidGuard

install -p -d %{buildroot}%{cgibin}
install -p -m 0755 samples/squid*cgi %{buildroot}%{cgibin}
install -p -m 0644 samples/babel.* %{buildroot}%{cgibin}

install -p -m 0755 contrib/hostbyname/hostbyname %{buildroot}%{_bindir}
install -p -m 0755 contrib/sgclean/sgclean %{buildroot}%{_bindir}

install -p -D -m 0644 %{SOURCE104} %{buildroot}%{_unitdir}/squidGuard.service
install -p -D -m 0644 %{SOURCE105} %{buildroot}%{_unitdir}/transparent-proxying.service

install -p -D -m 0744 %{SOURCE106} %{buildroot}%{_bindir}/squidGuard-helper
install -p -D -m 0744 %{SOURCE107} %{buildroot}%{_bindir}/transparent-proxying-helper

sed -i "s,dest/adult/,blacklists/porn/,g" %{buildroot}%{_sysconfdir}/squid/squidGuard.conf

mkdir -p %{buildroot}%{_localstatedir}/log/squidGuard
mkdir -p %{buildroot}%{_localstatedir}/log/squid
ln -s ../squidGuard/squidGuard.log %{buildroot}%{_localstatedir}/log/squid/squidGuard.log

%post
%systemd_post squidGuard.service transparent-proxying.service

%preun
%systemd_preun squidGuard.service transparent-proxying.service

%postun
%systemd_postun_with_restart squidGuard.service transparent-proxying.service

%files
%doc samples/*.conf
%doc samples/*.cgi
%doc samples/dest/blacklists.tar.gz
%doc COPYING GPL
%doc doc/*.txt doc/*.html doc/*.gif
%doc squidGuard.conf.k12ltsp.template
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/squid/squidGuard.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/squidGuard
%{_sysconfdir}/cron.daily/squidGuard
%{dbtopdir}/
%attr(0755,root,root) %{cgibin}/squidGuard-simple*.cgi
%attr(0755,root,root) %config(noreplace) %{cgibin}/squidGuard.cgi
%{cgibin}/babel.*
%{_unitdir}/squidGuard.service
%{_unitdir}/transparent-proxying.service
%attr(0755,squid,squid) %{_localstatedir}/log/squidGuard
%{_localstatedir}/log/squid/squidGuard.log

%changelog
* Tue Oct 06 2026 Bojan Smojver <bojan@rexursive.com> - 1.6.0-2
- Spec cleanup: drop obsolete _hardened_build, use %%make_build, plain
  install/cp and %%{buildroot} instead of %%{__*} macros
- Use systemd scriptlet macros, drop obsolete %%triggerun
- Fix duplicate %%files entry for squidGuard.cgi and %%attr on symlink
- Drop stray tar extraction from %%install
- Drop dead commented-out code

* Tue Oct 06 2026 Bojan Smojver <bojan@rexursive.com> - 1.6.0-1
- Use original source URL

* Mon Oct 05 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.6.0-1
- Update to v1.6.0

* Fri Jul 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jan 22 2025 Bojan Smojver <bojan@rexursive.com> - 1.4-50
- fix rawhide build

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4-45
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Florian Weimer <fweimer@redhat.com> - 1.4-43
- Fixes for building in strict(er) C99 mode (#2148639)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4-36
- Patch for 64-bit segfault.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Bojan Smojver <bojan@rexursive.com> - 1.4-32
- add gcc build requirement

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Bojan Smojver <bojan@rexursive.com> - 1.4-28
- Helper protocol patch (bug #1443273, bug #1418267)
- Fix logrotate configuration (bug #1394601)
- Fix typo in transparent-proxying.service

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 Jon Ciesla <limburgher@gmail.com> - 1.4-26
- Fix unitfile typo.

* Tue Jun 21 2016 Jon Ciesla <limburgher@gmail.com> - 1.4-25
- Patch for 20150201 (CVE-2015-8936).
- Fix log permissions.
- logrotate correction.
- Corrected config file.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 1.4-22
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4-18
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Bojan Smojver <bojan@rexursive.com> - 1.4-16
- Fix for Berkeley DB 5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Jon Ciesla <limburgher@gmail.com> - 1.4-14
- Build with LDAP support, BZ 834916.
- Dropped db4-isms.

* Tue Apr 17 2012 Jon Ciesla <limburgher@gmail.com> - 1.4-13
- Migrate to systemd.
- Stop messing with config noreplace for the config file in post.

* Mon Apr 16 2012 Jon Ciesla <limburgher@gmail.com> - 1.4-12
- Build against libdb again.

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 1.4-11
- Add hardened build.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 26 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-8
- Applying upstream patches for CVE-2009-3700, BZ 530862.

* Thu Sep 24 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-7
- Make squidGuard.cgi config(noreplace)
- Relocated logs, updated logrotate file.
- Updated blacklist URL.

* Wed Sep 09 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-6
- Include babel files, BZ 522038.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-4
- Initscript cleanup, BZ 247065.

* Tue Feb 24 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-3
- Drop chcon Req.

* Mon Feb 23 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-2
- Dropping selinux policy and chcon, BZ 486634.
- Fixed URL of Source0.

* Wed Feb 18 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-1
- Update to 1.4, BZ 485530.
- Building against compat-db46 until next version.

* Wed Feb 11 2009 Jon Ciesla <limb@jcomserv.net> - 1.3-1
- Update to 1.3.
- Dropped paths, sed patches, applied upstream.
- New SG-2008-06-13 patch.

* Wed Feb 11 2009 Jon Ciesla <limb@jcomserv.net> - 1.2.1-2
- Fix sg-2008-06-13, BZ 452467.

* Wed Feb 11 2009 Jon Ciesla <limb@jcomserv.net> - 1.2.1-1
- Update to 1.2.1, BZ 245377.
- Dropped upstream patch.
- Updated blacklists.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.0-18
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.2.0-17
- Rebuild for deps

* Fri Nov 16 2007 John Berninger <john at ncphotography dot com> 1.2.0-16
- Fix perms on cgi-bin files

* Mon Mar 26 2007 John Berninger <jwb at redhat dot com> 1.2.0-15
- Assert ownership of /var/squidGuard - bz 233915

* Tue Aug 29 2006 John Berninger <jwb at redhat dot com> 1.2.0-14
- Bump release 'cause I forgot to add a patch file that's required

* Tue Aug 29 2006 John Berninger <jwb at redhat dot com> 1.2.0-13
- general updates to confirm build on FC5/FC6
- updates to BuildRequires

* Fri Sep 09 2005 Oliver Falk <oliver@linux-kernel.at> - 1.2.0-12
- Make it K12LTSP compatible, so a possible upgrade doesn't break
  anything/much...
  - Add SELinux stuff
  - Move dbdir to /var/squidGuard/blacklists, instead of /var/lib/squidGuard
  - Added update script and template config from/for K12
  - Add perlwarnings and sed patch
  - Install cgis in /var/www/cgi-bin
  - Added initrd stuff
- Remove questionable -ldb from make
- Remove questionable db version check

* Tue Sep 06 2005 Oliver Falk <oliver@linux-kernel.at> - 1.2.0-11
- More bugs from Bug #165689
  Install cron script with perm 755
  Don't use SOURCE3 in install section, we need to use the patched one

* Mon Sep 05 2005 Oliver Falk <oliver@linux-kernel.at> - 1.2.0-10
- Include GPL in doc section

* Mon Sep 05 2005 Oliver Falk <oliver@linux-kernel.at> - 1.2.0-9
- More 'bugs' from Bug #165689
  Make changed on squid-getlist.html a patch, as sources should
  match upstream sources, so they are wget-able...

* Mon Sep 05 2005 Oliver Falk <oliver@linux-kernel.at> - 1.2.0-8
- Bug #165689

* Thu May 19 2005 Oliver Falk <oliver@linux-kernel.at> - 1.2.0-7
- Update blacklists
- Cleanup specfile

* Fri Apr 08 2005 Oliver Falk <oliver@linux-kernel.at> - 1.2.0-6
- Fix build on RH 8 with db 4.0.14, by not applying the db4 patch

* Mon Feb 21 2005 Oliver Falk <oliver@linux-kernel.at> - 1.2.0-5
- Specfile cleaning
- Make it build with db4 again, by adding the db4-patch

* Fri Apr 12 2002 Oliver Pitzeier <oliver@linux-kernel.at> - 1.2.0-4
- Tweaks

* Mon Apr 08 2002 Oliver Pitzeier <oliver@linux-kernel.at> - 1.2.0-3
- Rebuild

* Mon Apr 08 2002 Oliver Pitzeier <oliver@linux-kernel.at> - 1.2.0-2
- Updated the blacklists and put it into the right place
  I also descompress them
- Added a new "forbidden" script - the other ones are too
  old and don't work.

* Fri Apr 05 2002 Oliver Pitzeier <oliver@linux-kernel.at> - 1.2.0-1
- Update to version 1.2.0

* Fri Jun  1 2001 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- cleaned up for rhcontrib

* Fri Oct 13 2000 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- initial build
