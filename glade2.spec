%global po_package glade-2.0

Summary:        User Interface Designer for GTK+ 2, legacy version
Name:           glade2
Version:        2.12.2
Release:        37%{?dist}
License:        GPLv2+ and GFDL
URL:            http://glade.gnome.org/
Source:         http://download.gnome.org/sources/glade/2.12/glade-%{version}.tar.bz2
# Fedora specific patches
Patch0:         gnome-i18n.patch
Patch1:         gtk-includes.patch
# https://fedoraproject.org/wiki/Format-Security-FAQ
Patch2:         glade-2.12.2-format-security.patch

BuildRequires:  gcc
BuildRequires: glib2-devel 
BuildRequires: pango-devel
BuildRequires: gtk2-devel
BuildRequires: libgnomeui-devel
BuildRequires: libbonobo-devel
BuildRequires: libbonoboui-devel
BuildRequires: gnome-vfs2-devel 
BuildRequires: libgnomecanvas-devel 
BuildRequires: desktop-file-utils 
BuildRequires: scrollkeeper
BuildRequires: gettext
BuildRequires: perl(XML::Parser)
BuildRequires: make

%description
The glade2 package contains a legacy version of Glade for GTK+ 2.x. Do not use
it for new projects, use glade (for GTK+ 3.x) or glade3 (for GTK+ 2.x) instead.

Glade is a free user interface builder for GTK+ and the GNOME GUI
desktop. Glade can produce C source code. Support for C++, Ada95,
Python, and Perl is also available, via external tools which process
the XML interface description files output by GLADE.

%prep
%setup -q -n glade-%{version}
%patch0 -p1 -b .gnome-i18n
%patch1 -p1 -b .gtk-includes
%patch2 -p1 -b .format-security

# Fix the warnings from desktop-file-install 
sed -i 's|Icon=glade-2.png|Icon=glade-2|g' glade-2.desktop.in
sed -i 's|MimeType=application/x-glade|MimeType=application/x-glade;|g' glade-2.desktop.in

# It's sr@latin, not sr@Latn
mv -f po/sr@Latn.po po/sr@latin.po
sed -i 's|sr@Latn|sr@latin|g' po/LINGUAS

%build
%configure --disable-gnome-db 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

desktop-file-install --vendor gnome --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --add-category X-Red-Hat-Base                             \
  $RPM_BUILD_ROOT%{_datadir}/applications/*

rm -rf $RPM_BUILD_ROOT/var/scrollkeeper

%find_lang %po_package --all-name --with-gnome

%files -f %{po_package}.lang
%doc AUTHORS COPYING README NEWS TODO
%{_datadir}/glade-2
%{_datadir}/applications/gnome-glade-2.desktop
%{_datadir}/pixmaps/*
%{_bindir}/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-33
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.12.2-23
- Remove obsolete libgnomeprint deps (#1307536)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Nils Philippsen <nils@redhat.com>
- use %%global instead of %%define

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Nils Philippsen <nils@redhat.com> - 2.12.2-18
- use correct name for Serbian language in Latin script (#1053545)

* Tue Dec 03 2013 Nils Philippsen <nils@redhat.com> - 2.12.2-17
- use string literals as format strings (#1037088)

* Thu Aug 15 2013 Nils Philippsen <nils@redhat.com> - 2.12.2-16
- don't require bonobo-activation-devel for building (#992382)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Nils Philippsen <nils@redhat.com> - 2.12.2-13
- mark as legacy (#882557)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 2.12.2-11
- rebuild for gcc 4.7

* Mon Nov 07 2011 Nils Philippsen <nils@redhat.com> - 2.12.2-10
- rebuild (libpng)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 06 2010 Parag Nemade <paragn AT fedoraproject.org> - 2.12.2.8
- Merge-review cleanup (#225803)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct  1 2008 Matthias Clasen  <mclasen@redhat.com> - 2.12.2-5
- Make it build

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.12.2-3
- fix license tag

* Fri Feb  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.12.2-2
- Rebuild for gcc 4.3

* Thu Dec 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.2-1
- Update to 2.12.2

* Wed Oct 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.1-10
- Rebuild

* Sat Aug 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.1-9
- Fix the build 

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.1-8
- Update the license field
- Use %%find_lang for help files

* Wed May  2 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.1-7
- Fix typos in macros in the BuildRequires section (#238322)

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.1-6
- Don't install INSTALL

* Fri Sep  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-5
- Fix directory ownership issues
- Add missing BuildRequires

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-4.1
- rebuild

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-4
- Add missing  BuildRequires

* Thu Jun  1 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-3
- Rebuild

* Sat Feb 11 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-2
- Remove requires for gail-devel that has been unnecessary
  since 2002

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Oct 12 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.1-1
- Update to 2.12.1

* Thu Sep 29 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.0-1
- Update to 2.12.0

* Tue Aug 16 2005 Matthias Clasen <mclasen@redhat.com> 
- Rebuilt

* Thu Apr 21 2005 Matthias Clasen <mclasen@redhat.com> - 2.10.0-1
- Update to 2.10.0

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.0-2
- Rebuild with gcc4

* Fri Feb  4 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.0-1
- Update to 2.9.0

* Mon Jan 10 2005 Matthias Clasen <mclasen@redhat.com> - 2.6.8-1
- Update to 2.6.8

* Mon Jun 21 2004 Matthias Clasen <mclasen@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr  2 2004 Mark McLoughlin <markmc@redhat.com> 2.5.0-1
- Update to 2.5.0

* Fri Mar 12 2004 Alex Larsson <alexl@redhat.com> 2.0.1-1
- update to 2.0.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jul 30 2003 Havoc Pennington <hp@redhat.com> 2.0.0-2
- rebuild

* Mon Jul  7 2003 Havoc Pennington <hp@redhat.com> 2.0.0-1
- 2.0.0
- remove "stockfix" patch now upstream

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 14 2003 Havoc Pennington <hp@redhat.com> 1.1.3-3
- no buildreq Xft

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec  9 2002 Havoc Pennington <hp@redhat.com>
- 1.1.3

* Wed Aug 14 2002 Havoc Pennington <hp@redhat.com>
- require gail-devel #67084

* Thu Aug  8 2002 Havoc Pennington <hp@redhat.com>
- move from CVS snap to final release

* Tue Jun 25 2002 Owen Taylor <otaylor@redhat.com>
- Fix missing po files

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 1.1.0.90 cvs snap
- use desktop-file-install

* Thu Jun 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in different environment

* Thu Jun 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- fix a scrollkeeper validation bug

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu May 23 2002 Havoc Pennington <hp@redhat.com>
- move to glade 2, based on glade 1 specfile
