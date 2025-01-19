#
# spec file for package lbdb
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Red Hat, Inc
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugzilla.redhat.com
#

Name:           lbdb
Summary:        Address Database for mutt
Version:        0.41
Release:        21%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            http://www.spinnaker.de/lbdb/
Source:         http://www.spinnaker.de/debian/lbdb_%{version}.tar.gz
# change default modules list
Patch0: 0001-Change-default-methods.patch
# fix path of evolution-addressbook-export
Patch1: 0002-Look-up-evolution-addressbook-export-in-libexec-rath.patch
# fix hostname lookup if multiple domains are listed in resolv.conf
Patch2: 0003-Fix-hostname-lookup-if-multiple-domains-are-listed-i.patch


BuildRequires:  gcc
BuildRequires: /usr/bin/pod2man
BuildRequires:  abook
BuildRequires:  gnupg2
BuildRequires:  finger
BuildRequires:  perl-generators
BuildRequires: make
Requires:       perl(Net::LDAP)
Requires:       perl(Getopt::Long)

%description
The Little Brother's Database (lbdb) consists of a set of small tools
that collect mail addresses from several sources and offer these
addresses to the external query feature of the Mutt mail reader.


%prep
%setup -q -n lbdb-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1


%build
# lbdb uses libdir in most of its helper programs to find the absolute path
# to these binaries, that's why it's forcefully set to %_libexecdir/lbdb.
# Another option would be to s/libdir/libexecdir in the helpers, but there
# are about 15 programs to patch, so this approach is easier.
%configure --libdir=%{_libexecdir}/lbdb --with-evolution-addressbook-export=auto --with-gpg=/usr/bin/gpg2
make %{?_smp_mflags}


%install
BUILD_ROOT=${RPM_BUILD_ROOT} make \
        install_prefix=${RPM_BUILD_ROOT} \
        sysconfdir=%{_sysconfdir} \
        mandir=%{_mandir} \
        libdir=%{_libexecdir}/lbdb \
        install


%files
%doc README COPYING INSTALL TODO
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_libexecdir}/lbdb/*
%dir %{_libexecdir}/lbdb
%doc %{_mandir}/man?/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.41-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 09 2016 Christophe Fergeau <cfergeau@redhat.com> - 0.41-1
- Update to upstream release 0.41
  Resolves: rhbz#1259881

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 28 2014 Christophe Fergeau <cfergeau@redhat.com> 0.39-1
- Update to lbdb 0.39

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 10 2013 Omair Majid <omajid@redhat.com> - 0.38-8
- Add BuildRequires: abook to include abook support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.38-6
- Perl 5.18 rebuild

* Wed Mar 06 2013 Christophe Fergeau <cfergeau@redhat.com> - 0.38-5
- Add BuildRequires: pod2man, this has been split to a separate package in
  rawhide and is no longer available in the build roots by default

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 04 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.38-2
- add %%{?dist} in release
- remove use of BuildRoot:
- remove use of %%defattr
- remove usage instruction from %%description
- comment patches

* Mon Sep 19 2011 Christophe Fergeau <cfergeau@redhat.com> - 0.38-1
- new version 0.38
  * adapt the spec file for fedora use

* Tue Feb  8 2011 lnussel@suse.de
- Suggest perl(Net::LDAP) (bnc#669969)
* Wed May 19 2010 lnussel@suse.de
- new version 0.37
  * Fix bashisms in m_bbdb
  * Fix query shell functions to catch non-zero exit status in case they
    get invoked in set -e context.
  * m_evolution: support line breaks and long lines.
  * Fix documentation concerning the quotes on lbdbq call
- fix path to evolution-addressbook-export
* Tue Nov  3 2009 coolo@novell.com
- updated patches to apply with fuzz=0
* Thu Oct  2 2008 lnussel@suse.de
- new version 0.36
  * Remove duplicate "See also: mutt" from lbdbq.man.
  * Update configure using autconf 2.61.
  * Apply charset conversation patch by Peter Colberg based on code by
    Tobias Schlemmer.
  * Remove duplicate declaration of $ignorant.
  * Handle mail addresses in mutt_ldap_query correct. Thanks to Colin
    Watson <cjwatson@debian.org> for providing a patch.
  * Mention ldapi URIs in mutt_ldap_query man page.
  * Protect "make distclean" by checking whether makefile exists.
  * Upgrade to Standards-Version 3.8.0:
  - Fix Homepage header in control file.
  * Add copyright holders to debian/copyright file.
  * Remove outdated override.Lintian.
* Fri Aug 10 2007 lnussel@suse.de
- new version 0.35.1
  * supports ldaps
* Wed May 16 2007 lnussel@suse.de
- new version 0.34
  * vcquery: avoid free() on unallocated memory if fullname is not set.
  * vcquery: Use value of concatenated N fields if FN field is missing.
- fix hostname lookup if multiple domains are listed in resolv.conf
* Mon Oct 16 2006 lnussel@suse.de
- new version 0.33
  * Add SORT_OUTPUT=reverse_comment to do reverse sort by the third column
    (most recent m_inmail timestamp at the top).
  * Comment out LDAP_NICKS in lbdb.rc because this should only be an
    example and if it is set there it overrides other LDAP settings
* Thu Aug 24 2006 lnussel@suse.de
- new version 0.32
- fix path to evolution-addressbook-export
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon May  9 2005 lnussel@suse.de
- update to version 0.30
* Fri Feb 27 2004 lnussel@suse.de
- run configure similar to the original debian package to reduce
  neededforbuild and to fix evolution addressbook query
- add gpg to default address query methods
* Thu Feb 26 2004 lnussel@suse.de
- update to version 0.29
* Sun Feb  8 2004 lnussel@suse.de
- update to version 0.28.2
- use %%optflags, fix aliasing problems
* Wed Feb 12 2003 lnussel@suse.de
- new version 0.26.2
  * new ldap option $ignorant
  * support for multiple abook address books
* Fri Aug 16 2002 ro@suse.de
- removed emtpy post/postun scripts (#17916)
* Thu Apr 25 2002 lnussel@suse.de
- new version 0.26
- now uses m_getent instead of m_passwd (lbdb.rc.dif)
- moved files from %%{_prefix}/lib to %%{_libdir}/lbdb
* Tue Jul 24 2001 lnussel@suse.de
- new version 0.25
* Tue Mar 20 2001 lnussel@suse.de
- new version 0.24
- added finger to neededforbuild
* Wed Feb  7 2001 lnussel@suse.de
- new version 0.23
- neededforbuild: ypbind -> yp-tools
* Thu Nov 30 2000 ro@suse.de
- neededforbuild: ypclient -> ypbind
* Thu Oct 12 2000 lnussel@suse.de
- new version 0.21.1
- cleaned up spec file
- changed Group to Applications/Mail
* Tue Aug 29 2000 lnussel@suse.de
- initial check in
