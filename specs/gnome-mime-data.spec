Summary: MIME type data files for GNOME desktop
Name: gnome-mime-data
Version: 2.18.0
Release: 36%{?dist}
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/gnome-mime-data/2.18/%{name}-%{version}.tar.bz2
# No license attribution, just COPYING.
License: GPL-1.0-or-later
BuildArch: noarch
BuildRequires:  gcc
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(XML::Parser)
BuildRequires: gettext
BuildRequires: make

# Fedora specific patches
Patch0: gnome-mime-data-2.2.0-openoffice.patch
Patch1: gnome-mime-data-2.2.0-rpminstall.patch
Patch2: gnome-mime-data-2.3.2-nohtmlcomponent.patch
Patch3: gnome-mime-data-2.4.1-default-applications.patch
Patch5: gnome-mime-data-2.4.0-OOo-startup.patch

%description
gnome-mime-data provides the file type recognition data files for gnome-vfs

%prep
%setup -q

%patch -P0 -p1 -b .openoffice
%patch -P1 -p1 -b .rpminstall
%patch -P2 -p1 -b .nohtmlcomponent
%patch -P3 -p1 -b .default-applications
%patch -P5 -p1 -b .OOo-startup

## be sure .keys is regenerated from patched .keys.in
rm gnome-vfs.keys

## no command line apps as bindings
perl -pi -e 's/,mpg123//g' gnome-vfs.keys.in
perl -pi -e 's/mpg123//g' gnome-vfs.keys.in

%build
%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %name

%files -f %{name}.lang
%doc COPYING ChangeLog README
%config %{_sysconfdir}/gnome-vfs-mime-magic
%{_datadir}/application-registry
%{_datadir}/mime-info/*.keys
%{_datadir}/mime-info/*.mime
%{_datadir}/pkgconfig/*

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.18.0-33
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.18.0-16
- BR: perl(Getopt::Long) (#1307548)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 06 2010 Parag Nemade <paragn AT fedoraproject.org> - 2.18.0-7
- Merge-review cleanup (#225824)

* Fri Sep 10 2010 Matthias Clasen <mclasen@redhat.com> - 2.18.0-6
- Don't own /usr/share/mime-data (#569435)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.18.0-3
- fix license tag
- fix patches to apply with fuzz=0

* Wed Apr 18 2007 - Bastien Nocera <bnocera@redhat.com> - 2.18.0-2
- Really make noarch

* Tue Apr 17 2007 - Bastien Nocera <bnocera@redhat.com> - 2.18.0-1
- Upgrade to 2.18.0 and make noarch

* Sun Nov 26 2006 Matthias Clasen <mclasen@redhat.com> - 2.4.3-2
- Own the /usr/share/mime-info directory (#216922)

* Wed Nov  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.4.3-1
- Update to 2.4.3
- Require pkgconfig

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-3.1
- rebuild

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.4.2-3
- Add a BuildRequires for gettext

* Tue Jun  6 2006 Matthias Clasen <mclasen@redhat.com> - 2.4.2-2
- Add a BuildRequires for perl-XML-Parser

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Jan 27 2005 Matthias Clasen <mclasen@redhat.com> - 2.4.2-1
- Update to 2.4.2

* Wed Sep 29 2004 GNOME <jrb@redhat.com> - 2.4.1-5
- bump release

* Tue Apr  6 2004 Alexander Larsson <alexl@redhat.com> 2.4.1-4
- make gedit default for text/plain

* Fri Mar 19 2004 Mark McLoughlin <markmc@redhat.com> 2.4.1-3
- Add back the default-applications patch

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 20 2004 Alexander Larsson <alexl@redhat.com> 2.4.1-1
- 2.4.1

* Fri Oct 17 2003 Alexander Larsson <alexl@redhat.com> 2.4.0-2
- Add startup notification support to OpenOffice.org

* Fri Oct  3 2003 Alexander Larsson <alexl@redhat.com> 2.4.0-1
- update to 2.4.0

* Tue Sep  9 2003 Alexander Larsson <alexl@redhat.com> 2.3.2-1
- update to 2.3.2
- set default action to component for x-directory/smb-share to make
  smb shares work

* Mon Aug 11 2003 Alexander Larsson <alexl@redhat.com> 2.3.1-1
- Update for gnome 2.3

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb  4 2003 Havoc Pennington <hp@redhat.com> 2.2.0-1
- migrate patches forward
- 2.2.0

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sun Nov 10 2002 Havoc Pennington <hp@redhat.com>
- 2.0.1

* Tue Oct  8 2002 Havoc Pennington <hp@redhat.com>
- ah, the real problem was noarch. pkgconfig files are no longer noarch

* Tue Oct  8 2002 Havoc Pennington <hp@redhat.com>
- rebuild to fix libdir

* Tue Sep  3 2002 Jonathan Blandford <jrb@redhat.com>
- fix the gimp to run 'gimp' instead of 'gimp-remote'

* Wed Aug 14 2002 Havoc Pennington <hp@redhat.com>
- ah, did not know about default_application_id. fix various things to
  work properly. also, change some unrelated stuff: bind openoffice to
  more file types, don't use gnumeric embedded control for gnumeric
  files.

* Wed Aug 14 2002 Havoc Pennington <hp@redhat.com>
- don't try to view html in-place, use htmlview as default html viewer
- remove mpg123 as a viewer, it's a command line app

* Wed Aug 14 2002 Alexander Larsson <alexl@redhat.com> 2.0.0-6
- Changed appname from redhat-install-package to redhat-install-packages

* Wed Aug 14 2002 Alexander Larsson <alexl@redhat.com> 2.0.0-5
- bind rpm to redhat-install-package

* Wed Aug  7 2002 Havoc Pennington <hp@redhat.com>
- bind openoffice to excel/word documents

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- remove empty NEWS/AUTHORS, #66082

* Sat Jun 15 2002 Havoc Pennington <hp@redhat.com>
- 2.0.0
- check file list, add icons and man pages

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- 1.0.8

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.0.7

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- 1.0.6

* Wed Feb 27 2002 Havoc Pennington <hp@redhat.com>
- 1.0.4
- make it noarch

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 1.0.3

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.0.2

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 1.0.1.90 cvs snap

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- add doc files

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- Initial build.


