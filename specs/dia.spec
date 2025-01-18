Name:           dia
Version:        0.97.3
Release:        29%{?dist}
Epoch:          1
Summary:        Diagram drawing program
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Dia
Source0:        https://download.gnome.org/sources/dia/0.97/%{name}-%{version}.tar.xz
# Upstream from https://gitlab.gnome.org/GNOME/dia/-/commit/baa2df853f9fb770eedcf3d94c7f5becebc90bb9
Patch0:         https://gitlab.gnome.org/GNOME/dia/-/commit/baa2df853f9fb770eedcf3d94c7f5becebc90bb9.patch#/dia-0.97.3-cve-2019-19451.patch
# Downstream patch
Patch1:         dia-configure-c99.patch
# Backport from https://gitlab.gnome.org/GNOME/dia/-/commit/f57ea2685034ddbafc19f35d9b525a12283d7c24
Patch2:         dia-0.97.3-get_data_size.patch
# Upstream from https://gitlab.gnome.org/GNOME/dia/-/commit/e5557aa1d396bc3ca80240f7b5c0a1831a5cf209
Patch3:         https://gitlab.gnome.org/GNOME/dia/-/commit/e5557aa1d396bc3ca80240f7b5c0a1831a5cf209.patch#/dia-0.97.3-const-ft_vector.patch
# Backport from https://gitlab.gnome.org/GNOME/dia/-/commit/caddfcab250fe677ecf294fad835b71e6b10cf26
Patch4:         dia-0.97.3-g_test_add_data_func_1.patch
# Backport from https://gitlab.gnome.org/GNOME/dia/-/commit/9c481f649414190bf8d6741cbca1777e9766756b
Patch5:         dia-0.97.3-g_test_add_data_func_2.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libart-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  freetype-devel
BuildRequires:  intltool
BuildRequires:  docbook-utils
BuildRequires:  docbook-style-dsssl
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
The Dia drawing program can be used to draw different types of diagrams,
and includes support for UML static structure diagrams (class diagrams),
entity relationship modeling, and network diagrams.  Dia can load and
save diagrams to a custom XML format and export diagrams to formats like
EPS, SVG, XFIG, PDF, PNG and others.


%prep
%autosetup -p1

sed -i 's|libdia_la_LDFLAGS = -avoid-version|libdia_la_LDFLAGS = -avoid-version $(shell pkg-config --libs gtk+-2.0 libxml-2.0 libart-2.0)|' \
  lib/Makefile.*
chmod -x `find objects/AADL -type f`
iconv -f WINDOWS-1252 -t UTF8 doc/en/usage-layers.xml > usage-layers.xml.UTF-8
mv usage-layers.xml.UTF-8 doc/en/usage-layers.xml

# run in single window mode (--integrated) by default (#910275)
sed -i 's|Exec=dia|Exec=dia --integrated|' dia.desktop.in.in

%build
%configure --enable-db2html --disable-silent-rules
%make_build


%install
%make_install
%find_lang %{name} --with-man

# below is the desktop file and icon stuff.
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
  --remove-category Application                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -f samples/Makefile*

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=710955
SentUpstream: 2013-10-27
-->
<application>
  <id type="desktop">dia.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Dia is a GTK+ based diagram creation program</summary>
  <description>
    <p>
      Dia is roughly inspired by the commercial Windows program 'Visio,' though
      more geared towards informal diagrams for casual use.
      It can be used to draw many different kinds of diagrams.
      It currently has special objects to help draw entity relationship diagrams,
      UML diagrams, flowcharts, network diagrams, and many other diagrams.
      It is also possible to add support for new shapes by writing simple XML files,
      using a subset of SVG to draw the shape.
    </p>
    <p>
      It can load and save diagrams to a custom XML format (gzipped by default,
      to save space), can export diagrams to a number of formats, including EPS,
      SVG, XFIG, WMF and PNG, and can print diagrams (including ones that span
      multiple pages).
    </p>
  </description>
  <url type="homepage">https://wiki.gnome.org/Apps/Dia</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/dia/a.png</screenshot>
  </screenshots>
  <updatecontact>dia-list@gnome.org</updatecontact>
</application>
EOF

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
%endif


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog KNOWN_BUGS NEWS README THANKS
%doc doc/custom-shapes doc/diagram.dtd doc/shape.dtd doc/sheet.dtd samples/
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime-info/%{name}.*
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 03 2024 Robert Scheck <robert@fedoraproject.org> - 1:0.97.3-27
- Added upstream patches for -Wincompatible-pointer-types (#2261060)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec  2 2022 Florian Weimer <fweimer@redhat.com> - 1:0.97.3-22
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Robert Scheck <robert@fedoraproject.org> - 1:0.97.3-19
- Enabled cairo plugin/support (#2017863, thanks to Matteo Brancaleoni)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Robert Scheck <robert@fedoraproject.org> - 1:0.97.3-16
- Added upstream patch to avoid infinite loop on filenames with invalid
  encoding (CVE-2019-19451, #1778767)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1:0.97.3-14
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.97.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 08 2015 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.3-4
- no need for autoreconf as configure is now generated by Autoconf 2.69

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:0.97.3-2
- Add an AppData file for the software center

* Mon Sep 08 2014 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.3-1
- 0.97.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.2-11
- BuildRequires: pkgconfig(foo) instead of foo-devel

* Tue Feb 11 2014 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.2-10
- make it build with freetype >= 2.5.1

* Tue Feb 11 2014 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.2-9
- desktop file runs dia in single window mode (--integrated) (#910275)
- update URL

* Thu Jan 16 2014 Jaromír Končický <jkoncick@redhat.com> - 1:0.97.2-8
- Serbian translation in latin script moved from sr@Latn to sr@latin (#1053543)

* Thu Aug 15 2013 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.2-7
- Build without GNOME (2) support (#996759)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 02 2013 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.2-5
- GLib drop support for adding interfaces after class_init (Gnome #694025)

* Mon Mar 25 2013 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.2-4
- Run autoreconf prior to running configure (#925250)

* Sun Feb 17 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1:0.97.2-3
- De-vendorize desktop file on F19+ (https://fedorahosted.org/fesco/ticket/1077)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Jiri Popelka <jpopelka@redhat.com> - 1:0.97.2-1
- 0.97.2
- unregister vdx, xfig import filter during plugin unloading (#854368)
- do not own directories owned by filesystem package (#569446)

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 25 2012 Bruno Wolff III <bruno@wolff.to> - 1:0.97.1-3
- A couple of the test programs used glib with the more loose API
- Use the newer libpng 1.5 API

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:0.97.1-1
- 0.97.1

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1:0.97-7
- Rebuild for new libpng

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97-6
- Rebuilt for glibc bug#747377

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.97-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 15 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:0.97-4
- Add BR rarian-compat to fix FTBS for F13 branch

* Mon Nov 30 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:0.97-3
- Fix crash in bz #541319

* Wed Aug 05 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:0.97-2
- Disable --with-python

* Fri Jul 24 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:0.97-1
- update to 0.97
- drop old patches

* Tue Mar 31 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:0.96.1-17
- Resolves: rhbz#486726
- Version bump

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.96.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> 1:0.96.1-13
- Resolves: rhbz#483312

* Fri Jan 30 2009 Hans de Goede <hdegoede@redhat.com> 1:0.96.1-12
- Update description for new trademark guidelines

* Mon Jan 26 2009 Caolán McNamara <caolanm@redhat.com> 1:0.96.1-11
- Resolves: rhbz#481551 python modules search path

* Sat Jan 03 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> 1:0.96.1-10
- Patch so that plugins dont look for .la files

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:0.96.1-9
- Rebuild for Python 2.6

* Fri Oct 31 2008 Caolán McNamara <caolanm@redhat.com> 1:0.96.1-8
- kill the ".la"s

* Wed Oct 22 2008 Caolán McNamara <caolanm@redhat.com> 1:0.96.1-7
- Resolves: rhbz#464982 FTBFS, defuzz patches

* Fri Feb  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.96.1-6
- Fix svg export (bug 431184)

* Sun Dec  2 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.96.1-5
- Do not put dia in both the Office and the Graphics application menus
  (bz 408041)

* Tue Nov 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.96.1-4
- Fix help not showing due to an encoding error (bz 401291)

* Mon Aug  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.96.1-3
- Update License tag for new Licensing Guidelines compliance

* Sun Jun 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.96.1-2
- Remove yelp Requires again <sigh> (bz 243330)

* Sat Jun  9 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.96.1-1
- New upstream release 0.96.1
- Add yelp Requires so that the help will always work (bz 243330)

* Thu Mar 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.96-1
- New upstream release 0.96
- Drop upstreamed python-25 and sigpipe patches

* Tue Feb 20 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-8
- Upgrade to upstream bugfix release 0.95-1
- Drop upstreamed ungroup and formatstring patches
- Add a patch for python-2.5 support
- Fix exit due to sigpipe when entering an invalid print command (bz 229101)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-7
- FE6 Rebuild

* Sun Aug 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-6
- Fix weaksymbols in libdia.so (BZ 202330)

* Sat Jun 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-5
- Add BuildRequires: gettext to fix building with new stripped mock config.

* Tue Jun  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-4
- Add a patch from upstream which fixes a crash when ungrouping
  multiple selected groups at once (bz 194149):
  http://bugzilla.gnome.org/show_bug.cgi?id=334771

* Tue May 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-3
- Fix CVE-2006-2453.

* Sat May 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-2
- Fix CVE-2006-2480 (bz 192535, 192538).

* Tue Apr 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-1
- New upstream version 0.95 (final)
- Cleanup spec even more, correctly install the desktop file and icons,
  drop unneeded scrollkeeper-update in scripts (bz 189756)

* Fri Mar 31 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:0.95-0.pre7.1
- Taking over as FE maintainer (bz 185886)
- Cleanup spec to match FE packaging guidelines
- Bump to upstream 0.95-pre7 (bz 184548)
- Enable python plugin

* Tue Jan 03 2006 Caolan McNamara <caolanm@redhat.com> 1:0.94-19
- make buildable

* Tue Jan 03 2006 Caolan McNamara <caolanm@redhat.com> 1:0.94-18
- rh#176504# add BuildRequires

* Mon Dec 19 2005 Caolan McNamara <caolanm@redhat.com> 1:0.94-17
- rh#176003# rejig Pre/Post

* Thu Oct 20 2005 Caolan McNamara <caolanm@redhat.com> 1:0.94-16

* Mon Oct 17 2005 Caolan McNamara <caolanm@redhat.com>
- move to extras

* Sat Apr 16 2005 Caolan McNamara <caolanm@redhat.com>
- rebuild for new cairo soname

* Fri Apr  8 2005 Caolan McNamara <caolanm@redhat.com>
- rh#165337# crash on >= 1000% xoom

* Thu Apr  7 2005 Caolan McNamara <caolanm@redhat.com>
- rh#154087# non existing links

* Fri Mar 25 2005 Florian La Roche <laroche@redhat.com>
- add PreReq: for scrollkeeper-update

* Wed Mar 16 2005 Caolan McNamara <caolanm@redhat.com>
- rh#151207# add Requires

* Mon Mar 14 2005 Caolan McNamara <caolanm@redhat.com>
- rh#150942# add BuildRequires

* Wed Mar  9 2005 Caolan McNamara <caolanm@redhat.com>
- rh#150305# add dia-0.94-fallbacktoxpmicons.patch

* Wed Mar  2 2005 Caolan McNamara <caolanm@redhat.com>
- rebuild with gcc4
- gnome#169019# gcc4 patch

* Fri Sep 03 2004 Matthias Clasen <mclasen@redhat.com>
- Fix a problem with the help patch

* Fri Sep 03 2004 Matthias Clasen <mclasen@redhat.com>
- Update to final 0.94 tarball
- Make the help button work (#131622)

* Wed Aug 18 2004 Dan Williams <dcbw@redhat.com>
- Update to 0.94-pre6
- Fix RH #110738

* Thu Jul 22 2004 Dan Williams <dcbw@redhat.com>
- Update to 0.94-pre1
- Add BuildRequires: libpng-devel (RH #125287)

* Fri Jun 25 2004 Dan Williams <dcbw@redhat.com>
- Update to 0.93

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Alexander Larsson <alexl@redhat.com> 1:0.92.2-3
- fix freetype issue

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Dec  9 2003 Alexander Larsson <alexl@redhat.com> 1:0.92.2-1
- update to 0.92.2

* Mon Oct 13 2003 Alexander Larsson <alexl@redhat.com> 1:0.91-2
- Fix font size (backport from cvs). Fixes bug #106045
- Fix libxslt issue (bug #106863)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 28 2003 Alexander Larsson <alexl@redhat.com> 1:0.91-1
- Update to 0.91
- Remove printing patch, it doesn't nearly apply yet, and might
  not be needed since dia is all utf8:y now.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 10 2003 Alexander Larsson <alexl@redhat.com> 0.90-9
- Remove duplicate desktop files

* Fri Dec  6 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Tue Sep 03 2002 Akira TAGOH <tagoh@redhat.com> 0.90-8
- dia-0.90-printing.patch: applied to support CJK printing. (#67733)

* Thu Aug 29 2002 Owen Taylor <otaylor@redhat.com>
- Fix problems with the manual DTD

* Wed Aug 28 2002 Owen Taylor <otaylor@redhat.com>
- Pass --enable-db2html to configure so we get docs

* Fri Aug 23 2002 Alexander Larsson <alexl@redhat.com> 0.90-6
- Made desktopfile symlink absolute, fixes #71991

* Tue Aug 13 2002 Havoc Pennington <hp@redhat.com>
- remove libpng10 patches, now using libpng12, #71416

* Mon Jul 29 2002 Havoc Pennington <hp@redhat.com>
- put pristine upstream tarball back
- fix up desktop files

* Tue Jul 23 2002 Karsten Hopp <karsten@redhat.de>
- fix menu entry (#69564)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 root <alexl@redhat.com> 0.90-1
- Updated to 0.90 from upstream. Removed outdated patches, updated png10 patch.

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 30 2002 Bill Nottingham <notting@redhat.com>
- rebuild against png10

* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- rebuild in rawhide

* Thu Jul 19 2001 Havoc Penningtoon <hp@redhat.com>
- Add some more build requires, #44732

* Tue Jul 10 2001 Alexander Larsson <alexl@redhat.com>
- Disable doc generation, since it breaks.

* Mon Jul  9 2001 Alexander Larsson <alexl@redhat.com>
- Updated from upstream (0.88.1)
- Removed source1 (ja.po) since it was in upstream
- Disabled patch1 since it breaks 8bit non-multibyte locales.
- Updated patch 3

* Fri Jun 15 2001 Havoc Penningtoon <hp@redhat.com>
- add some BuildRequires

* Fri Feb 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify
- use %%{_tmppath}

* Fri Feb 09 2001 Akira TAGOH <tagoh@redhat.com>
- -2
- Fixed install po.
- Updated Japanese translation.
  Note: Please remove Source1: when release the next upstream version.
- Added Japanese patch.
- -3
- Fixed text render bug.

* Mon Jan 29 2001 Preston Brown <pbrown@redhat.com>
- upgraded to fix i18n issues (#24875)

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Fri Aug 04 2000 Havoc Pennington <hp@redhat.com>
- Whatever, 15321 was already fixed (it's under plain Applications),
  change the group back

* Fri Aug 04 2000 Havoc Pennington <hp@redhat.com>
- Put it in Applications/Graphics bug 15321

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 6 2000 Tim Powers <timp@redhat.com>
- fixed manpage location
- use %%makinstall

* Mon May  1 2000 Matt Wilson <msw@redhat.com>
- updates to 0.84, added alpha back in

* Mon Nov 8 1999 Tim Powers <timp@redhat.com>
- updated to 0.81

* Mon Aug 30 1999 Tim Powers <timp@redhat.com>
- changed group

* Tue Aug 17 1999 Tim Powers <timp@redhat.com>
- exludearch alpha dumps core when you do anything

* Mon Jul 12 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Wed Apr 28 1999 Preston Brown <pbrown@redhat.com>
- initial build for Powertools 6.0
