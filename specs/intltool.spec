Name: intltool
Summary: Utility for internationalizing various kinds of data files
Version: 0.51.0
Release: 29%{?dist}
License: GPL-2.0-or-later WITH Autoconf-exception-generic
#VCS: bzr:https://code.edge.launchpad.net/~intltool/intltool/trunk
Source: https://edge.launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz
URL: https://launchpad.net/intltool
BuildArch: noarch
Requires: patch
# for /usr/share/aclocal
Requires: automake
Requires: gettext-devel
Requires: perl(Getopt::Long)
Requires: perl(XML::Parser)
BuildRequires: perl-generators
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(XML::Parser)
BuildRequires: gettext
BuildRequires: make
# http://bugzilla.gnome.org/show_bug.cgi?id=568845
# Dropping this patch per the last comment on that thread:
# Martin Pitt: As the reporter of the bug I close this, as the new API du jour is gsettings,
# which has a sensible gettext integration.
#Patch0: schemas-merge.patch
# Fix intltool-update to work with perl 5.26. Patch taken from
# Debian's intltool_0.51.0-4.debian.tar.xz
Patch1: intltool-perl5.26-regex-fixes.patch
# https://bugs.launchpad.net/intltool/+bug/1505260
# https://bugzilla.redhat.com/show_bug.cgi?id=1249051
Patch2: intltool-merge-Create-cache-file-atomically.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1318674
Patch3: intltool_distcheck-fix.patch

%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.

%prep
%setup -q
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1

%build
%configure

%make_build

%install
%make_install

%check
if ! make check; then
    find . -type f -name 'test-suite.log' | while read trs; do
	echo "BEGIN " ${trs}; cat ${trs} 1>&2;
    done
    echo  "Exiting abnormally due to make check failure above" 1>&2
    exit 1
fi

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/intltool*
%{_datadir}/intltool
%{_datadir}/aclocal/intltool.m4
%{_mandir}/man8/intltool*.8*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 6 2024 Manish Tiwari <matiwari@redhat.com> - 0.51.0-28
- CI gating tests migration to tmt

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 21 2023 Jens Petersen <petersen@redhat.com> - 0.51.0-24
- SPDX migration of license tag

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.51.0-12
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Kalev Lember <klember@redhat.com> - 0.51.0-10
- Fix intltool-update to work with perl 5.26 (#1462217)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.51.0-7
- fix usage of distcheck for some packages rhbz (#1318674)

* Tue Feb 16 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.51.0-6
- Depend on perl(Getopt::Long) (#1307638)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Colin Walters <walters@redhat.com> - 0.51.0-4
- Add patch to hopefully close race condition in systemd builds
- Related to https://bugzilla.redhat.com/show_bug.cgi?id=1249051
- And the test suite is failing but the logs are hidden under
  test-suite.log, so copy some code I had in dbus.spec to cat them.

* Mon Jul 13 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.51.0-3
- Add intltool-0.51.0-perl-5.22.patch (Address RHBZ#1233444)
- Remove unnecessary %%debug_package.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 09 2015 David King <amigadave@amigadave.com> - 0.51.0-1
- Update to 0.51.0
- Use license macro for COPYING
- Preserve timestamps during install
- Use parallel make flags
- Update man page glob in files section

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.50.2-6
- Perl 5.18 rebuild

* Fri Feb  8 2013 Matthias Clasen <mclasen@redhat.com> - 0.50.2-5
- Update url (#908562)

* Sun Oct 21 2012 Matthias Clasen <mclasen@redhat.com> - 0.50.2-3
- Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 0.50.2-2
- Clean up previous change and fix Requires/BuildRequires (#225902)

* Fri Apr 06 2012 Jon Ciesla <limburgher@gmail.com> - 0.50.2-1
- Latest stable release.
- Merge review BZ 225902 fixes:
- Removed Obsoletes/Provides for xml-i18n-tools.
- Swapped gettext/gettext-devel Requires, BuildRequires.
- Added %%check section.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Alon Levy <alevy@redhat.com>
- Update to 0.50.0
- Drop patch carried for bz#568845 (schemas-merge) per last comment
  in that bug.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 28 2010 Matthias Clasen <mclasen@redhat.com> - 0.41.1-1
- Update to 0.41.1

* Wed Aug 12 2009 Matthias Clasen <mclasen@redhat.com> - 0.41.0-1
- Update to 0.41.0

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.40.6-4
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Matthias Clasen <mclasen@redhat.com> - 0.40.6-2
- Don't merge translations back into GConf schemas

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 0.40.6-1
- Update to 0.40.6

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Matthias Clasen <mclasen@redhat.com> - 0.40.5-2
- turn noarch

* Sun Oct 19 2008 Matthias Clasen <mclasen@redhat.com> - 0.40.5-1
- Update to 0.40.5

* Sun Sep 21 2008 Matthias Clasen <mclasen@redhat.com> - 0.40.4-1
- Update to 0.40.4

* Wed Aug  6 2008 Matthias Clasen <mclasen@redhat.com> - 0.40.3-3
- Require gettext-devel

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.40.3-2
- fix license tag

* Fri Jul 25 2008 Matthias Clasen <mclasen@redhat.com> - 0.40.3-1
- Update to 0.40.3

* Mon Jul 21 2008 Matthias Clasen <mclasen@redhat.com> - 0.40.1-1
- Update to 0.40.1

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 0.40.0-1
- Update to 0.40.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 0.37.1-1
- Update to 0.37.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.37.0-3
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Matthias Clasen <mclasen@redhat.com> - 0.37.0-2
- Require gettext 

* Mon Dec 17 2007 Matthias Clasen <mclasen@redhat.com> - 0.37.0-1
- Update to 0.37.0

* Thu Dec 13 2007 Matthias Clasen <mclasen@redhat.com> - 0.36.3-1
- Update to 0.36.3

* Sun Sep 16 2007 Matthias Clasen <mclasen@redhat.com> - 0.36.2-1
- Update to 0.36.2

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 0.36.1-1
- Update to 0.36.1

* Fri Aug  3 2007 Matthias Clasen <mclasen@redhat.com> - 0.36.0-1
- Update to 0.36.0
- Update license field
- Drop patch rejected, obsolete and upstreamed patches
- Some spec file cleanups
- Require automake

* Tue Jul 31 2007 David Zeuthen <davidz@redhat.com> - 0.35.5-5
- Add support for PolicyKit .policy files (b.g.o #462312)

* Sat Jul 28 2007 Matthias Clasen <mclasen@redhat.com> - 0.35.5-4
- Don't produce useless debuginfo (#249969)

* Wed Mar 21 2007 Ray Strode <rstrode@redhat.com> - 0.35.5-3
- don't store a translation if it is equal to the original
  string

* Mon Mar 19 2007 Bill Nottingham <notting@redhat.com> - 0.35.5-2
- add upstream changeset 674 (GNOME bz#413461 - fix intltool-extract path)

* Sat Feb 24 2007 Matthias Clasen <mclasen@redhat.com> - 0.35.5-1
- Update to 0.35.5

* Wed Jan 10 2007 Matthias Clasen <mclasen@redhat.com> - 0.35.4-1
- Update to 0.35.4

* Thu Dec 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.35.2-1
- Update to 0.35.2

* Tue Aug  1 2006 Matthias Clasen <mclasen@redhat.com> - 0.35.0-2
- Add a missing BuildRequires: gettext

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.35.0-1.1
- rebuild

* Tue May 16 2006 Matthias Clasen <mclasen@redhat.com> 0.35.0-1
- Update to 0.35.1

* Tue May  9 2006 Matthias Clasen <mclasen@redhat.com> 0.34.90.cvs20060509-1
- Update to a cvs snapshot to allow building gnome 2.15

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.34.2-1.1
- bump again for double-long bug on ppc(64)

* Mon Feb  6 2006 Matthias Clasen <mclasen@redhat.com> 0.34.2-1
- Update to 0.34.2

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Aug  4 2005 Matthias Clasen <mclasen@redhat.com> - 0.34.1-1
- New upstream version

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> - 0.33-2
- Rebuild with gcc4

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> - 0.33-1
- Upgrade to 0.33

* Thu Jan 13 2005 Jeremy Katz <katzj@redhat.com> - 0.31.2-3
- fix intltool local mode (upstream 163981)

* Wed Nov  3 2004  <jrb@redhat.com> - 0.31.2-1
- add BuildRequires on perl-XML-Parser, #132622

* Thu Sep 23 2004 Jonathan Blandford <jrb@redhat.com> 0.31.2-1
- bump version

* Tue Aug  3 2004 Owen Taylor <otaylor@redhat.com> - 0.31.1-1
- Upgrade to 0.31.1

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar 12 2004 Alex Larsson <alexl@redhat.com> 0.30-1
- update to 0.30

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 19 2004 Jonathan Blandford <jrb@redhat.com> 0.29-1
- new version

* Mon Aug 25 2003 Alexander Larsson <alexl@redhat.com> 0.27.2-1
- update

* Mon Aug 11 2003 Havoc Pennington <hp@redhat.com> 0.27-1
- 0.27

* Wed Jul 30 2003 Havoc Pennington <hp@redhat.com> 0.26-1
- rebuild

* Wed Jul  9 2003 Havoc Pennington <hp@redhat.com> 0.26-1
- 0.26

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan  6 2003 Havoc Pennington <hp@redhat.com>
- 0.25

* Fri Nov  8 2002 Havoc Pennington <hp@redhat.com>
- 0.23

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 09 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Sun Jun  9 2002 Havoc Pennington <hp@redhat.com>
- 0.22
- remove perl patch, perl is fixed

* Thu Jun  6 2002 Nalin Dahyabhai <nalin@redhat.com>
- tweak the perl5 check to not bomb with perl 5.8

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- update to 0.18

* Thu Mar 14 2002 Jeremy Katz <katzj@redhat.com>
- update to 0.17

* Thu Feb 21 2002 Jeremy Katz <katzj@redhat.com>
- rebuild in new environment

* Tue Feb 12 2002 Havoc Pennington <hp@redhat.com>
- 0.15
- remove dbm patch, dbm no longer used upstream
- shorten summary line, #56739

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 0.14
- Try again on DBM fix
- Patch to use AnyDBM_File rather than NDBM_File for caching
- Version 0.14

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 0.12.90 cvs snap

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- 0.12 tarball

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap, no longer noarch

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- intltool specfile, based on xml-i18n-tools (but fixed up)
- obsolete/provide xml-i18n-tools

* Tue Aug 14 2001 Alexander Larsson <alexl@redhat.com> 0.9-2
- Require patch

* Wed Aug  8 2001 Jonathan Blandford <jrb@redhat.com>
- Fix bug #45699 and #50634 by upgrading version.

* Mon Jul 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Shorter summary
- Remove empty post/postun scripts
- Don't define name and ver on the top and use this in the headers later

* Tue Jul 10 2001 Tim Powers <timp@redhat.com>
- cleaned up files list so that there aren't non-standard dirs and so
  that it owns the xml-i18n-tools dir

* Tue Apr 17 2001 Jonathan Blandford <jrb@redhat.com>
- Cleaned up spec file a little for Red Hat.

* Thu Mar 01 2001 Maciej Stachowiak <mjs@eazel.com>
- removed devel subpackage

* Tue Jan 04 2000 Robin * Slomkowski <rslomkow@eazel.com>
- created this thing
