%global _hardened_build 1

Name:           up-imapproxy
Summary:        University of Pittsburgh IMAP Proxy
Version:        1.2.8
Release:        0.31.20250101svn15036%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.imapproxy.org
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r 15036 https://svn.code.sf.net/p/squirrelmail/code/trunk/imap_proxy squirrelmail-imap_proxy-1.2.8
#  tar cJvf squirrelmail-imap_proxy-20250101svn15036.tar.gz squirrelmail-imap_proxy-1.2.8
Source0:        squirrelmail-imap_proxy-20250101svn15036.tar.gz
Source1:        imapproxy.service
# handle aarch64 per RH BZ 926684
Patch0:         http://ausil.fedorapeople.org/aarch64/up-imapproxy/up-imapproxy-aarch64.patch
Patch1:         up-imapproxy-ssl.patch
Patch2:         up-imapproxy-configure-c99.patch
Patch3:         up-imapproxy-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openssl-devel ncurses-devel
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd

%description
imapproxy was written to compensate for webmail clients that are
unable to maintain persistent connections to an IMAP server. Most
webmail clients need to log in to an IMAP server for nearly every
single transaction. This behaviour can cause tragic performance
problems on the IMAP server. imapproxy tries to deal with this problem
by leaving server connections open for a short time after a webmail
client logs out. When the webmail client connects again, imapproxy
will determine if there's a cached connection available and reuse it
if possible.

%prep
%setup -q -n squirrelmail-imap_proxy-%{version}
# handle aarch64
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# Fixes/changes in default config
# - strip trailing spaces
# - change to Fedora default SSL path
# - use private user/group
# - use chroot in private chroot directory
# - run in foreground for systemd unit
sed -i \
    -e 's/  *$//' \
    -e 's!/usr/share/ssl!/etc/pki/tls!' \
    -e 's/^\(proc_username\) .*/\1 imapproxy/' \
    -e 's/^\(proc_groupname\) .*/\1 imapproxy/' \
    -e 's!^#*\(chroot_directory\) .*!\1 /var/lib/imapproxy!' \
    -e 's/^\(foreground_mode\) .*/\1 yes/' \
    scripts/imapproxy.conf

%build
%configure CFLAGS="%{optflags} -std=gnu17"
[ -d bin ] || mkdir bin
make %{?_smp_mflags}

%install
# The install-* Makefile targets don't support DESTDIR syntax, so work around.
install -D -m 0644 -p scripts/imapproxy.conf \
    $RPM_BUILD_ROOT%{_sysconfdir}/imapproxy.conf
install -D -m 0755 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/imapproxy.service
install -d -m 0755 $RPM_BUILD_ROOT%{_sbindir}
install -D -m 0755 bin/* $RPM_BUILD_ROOT%{_sbindir}

# Use a private chroot directory, also home directory for private user
install -d -m 0755 $RPM_BUILD_ROOT/var/lib/imapproxy

%pre
getent group imapproxy >/dev/null || groupadd -r imapproxy
getent passwd imapproxy >/dev/null || \
    useradd -r -g imapproxy -d /var/lib/imapproxy -s /sbin/nologin \
    -c "IMAP proxy service" imapproxy
exit 0

%post
%systemd_post imapproxy.service

%preun
%systemd_preun imapproxy.service

%postun
%systemd_postun_with_restart imapproxy.service 

%files
%doc COPYING ChangeLog README README.ssl
%doc copyright
%config(noreplace) %{_sysconfdir}/imapproxy.conf
%{_unitdir}/imapproxy.service
%{_sbindir}/in.imapproxyd
%{_sbindir}/pimpstat
%dir /var/lib/imapproxy

%changelog
* Tue Jan 21 2025 Chris Adams <linux@cmadams.net> - 1.2.8-0.31.20250101svn15036
- update to latest SVN
- explicitly set C level (due to config function handling)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.30.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 10 2024 Chris Adams <linux@cmadams.net> - 1.2.8-0.29.20171022svn14722
- update license to SPDX version
- update patch application to non-deprecated format

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.28.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.27.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.26.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Florian Weimer <fweimer@redhat.com> - 1.2.8-0.25.20171022svn14722
- C99 port

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.24.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.23.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2.8-0.22.20171022svn14722
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.21.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.8-0.20.20171022svn14722
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.19.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.18.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.17.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.16.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.15.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.14.20171022svn14722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Chris Adams <linux@cmadams.net> - 1.2.8-0.13.20171022svn14722
- clean up spec file and remove conditionals - spec file is for F28+
- remove tcp-wrappers (obsolete, use iptables to control access)
- add gcc BR for future Fedora
- switch to private user, fix default config parse (BZ 1543142)
- switch to foreground for systemd unit

* Mon Oct 23 2017 Chris Adams <linux@cmadams.net> - 1.2.8-0.12.20171022svn14722
- one more service update

* Mon Oct 23 2017 Chris Adams <linux@cmadams.net> - 1.2.8-0.11.20171022svn14722
- actually update systemd service file

* Sun Oct 22 2017 Chris Adams <linux@cmadams.net> - 1.2.8-0.8.20171022svn14722
- update to new upstream snapshot
- fix SSL to build against newer OpenSSL (works with older too)
- update default config to have Fedora SSL path
- update systemd service file to restart on failure
- sync Fedora and EPEL SRPMS, drop EPEL 5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-0.7.20130726svn14389
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-0.6.20130726svn14389
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-0.5.20130726svn14389
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-0.4.20130726svn14389
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild


* Tue Oct 1 2013 Manuel Wolfshant <wolfy@fedoraproject.org> 1.2.8-0.3.20130726svn14389
- Install correct initscript in SysV distros ( thanks Chris Adams )

* Sun Sep 22 2013 Manuel Wolfshant <wolfy@fedoraproject.org> 1.2.8-0.2.20130726svn14389
- Conditionalize BuildRequires for tcp wrappers for EL5/rest of the builds

* Tue Sep 17 2013 Chris Adams <linux@cmadams.net> - 1.2.8-0.1.20130726svn14389
- Update to upstream Subversion snapshot to get bug fixes
- Apply autoconf patch to handle aarch64
- Update spec to latest startup script handling, also conditionalize
  RHEL SysV init handle for EPEL to make it easier to handle both

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.7-4
- Migrate to systemd, BZ 722450.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Rakesh Pandit <rakesh@fedoraproject.org> 1.2.7-1
- Updated to 1.2.7

* Fri Dec 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.2.7-0.7.rc3
- Updated to 1.2.7-0.7.rc3

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.7-0.6.rc1
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.2.7-0.3.rc1
- Patched buggy init script (David Rees, Bug 477096)

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> 1.2.7-0.2.rc1
- rebuild with new openssl

* Thu Oct 23 2008 Rakesh Pandit <rakesh@fedoraproject.org> 1.2.7-0.1.rc1
- fixed version and release fields (acc. to guidelines)

* Thu Oct 23 2008 Rakesh Pandit <rakesh@fedoraproject.org> 1.2.7.rc1-1
- updated to 1.2.7.rc1 - security updates, buffer overflow etc.

* Thu Aug 28 2008 Rakesh Pandit <rakesh@fedoraproject.org> 1.2.6-2
- fixed initscript to follow guidelines

* Thu Aug 28 2008 Rakesh Pandit <rakesh@fedoraproect.org> 1.2.6-1
- Update to 1.2.6
- Remove old patches (already upstream), Remove README.known_issues
- Tidy init script (Tim Jackson)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4-9
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.2.4-8
 - Rebuild for deps

* Thu Sep 14 2006 Jeff Carlson <jeff@ultimateevil.org> - 1.2.4-7
- Force rebuild for FC-6.

* Thu Apr 27 2006 Jeff Carlson <jeff@ultimateevil.org> - 1.2.4-6
- Patch to fix changes in OpenSSL.
- Thanks to Paul W. Frields for providing the patch.

* Mon Dec 26 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.4-5
- Rebuild against new OpenSSL in devel (fc5 only).

* Tue Oct 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.4-4
- Fix for CAN-2005-2661 (#170220, from Debian).

* Fri Sep  9 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.4-3
- Same as -2.

* Fri Sep  9 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.4-2
- No-op release bump to get a new buildsys tag.

* Fri Sep  9 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.4-1
- Bump to current upstream release.
- Upstream includes a new doc (copyright), included.

* Fri Sep  9 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.3-6
- Another change to the init script.

* Sat Sep  3 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.3-5
- Preserve certain timestamps.

* Thu Sep  1 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.3-4
- Fix rpmlint complaints.
- Paul also provided a replacement init script.
- Fixed some redundant BuildReqs.
- Tuned Requires, install, and files.
- Many thanks to Paul Howarth.

* Wed Aug 31 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.3-3
- Added BuildRequires.

* Fri Aug 12 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.3-2
- Multiple fixups recommended by spot.

* Mon Jul 18 2005 Jeff Carlson <jeff@ultimateevil.org> - 1.2.3-1
- Initial build.
