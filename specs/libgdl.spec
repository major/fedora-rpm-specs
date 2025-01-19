Name:		libgdl
Epoch:		1
Version:	3.40.0
Release:	10%{?dist}
Summary:	GNOME docking library

License:	LGPL-2.1-or-later
URL:		https://gitlab.gnome.org/GNOME/gdl
Source0:	https://download.gnome.org/sources/gdl/3.40/gdl-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/gdl/-/merge_requests/4
Patch:		libgdl-3.40.0-libxml2-2.12.0-includes.patch

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	make
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -n gdl-%{version} -p1

%build
%configure \
  --disable-silent-rules \
  --disable-static \
  --enable-introspection=yes

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%find_lang gdl-3

%ldconfig_scriptlets

%files -f gdl-3.lang
%license COPYING
%doc AUTHORS
%doc MAINTAINERS
%doc NEWS
%doc README
%{_libdir}/%{name}-3.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gdl-3.typelib

%files devel
%{_libdir}/%{name}-3.so
%{_libdir}/pkgconfig/gdl-3.0.pc

%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gdl-3.gir

%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/gdl-3.0/

%dir %{_includedir}/%{name}-3.0
%{_includedir}/%{name}-3.0/gdl

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 David King <amigadave@amigadave.com> - 1:3.40.0-6
- Fix building against libxml2 2.12.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 1:3.40.0-1
- Update to 3.40.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Kalev Lember <klember@redhat.com> - 1:3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 1:3.28.0-1
- Update to 3.28.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Kalev Lember <klember@redhat.com> - 1:3.26.0-1
- Update to 3.26.0

* Fri Aug 25 2017 Kalev Lember <klember@redhat.com> - 1:3.25.91-1
- Update to 3.25.91

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 1:3.22.0-1
- Update to 3.22.0
- Don't set group tags
- Co-own gir directories instead of depending on gobject-introspection

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 1:3.20.0-1
- Update to 3.20.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 20 2015 Kalev Lember <klember@redhat.com> - 1:3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 21 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.0-1
- Update to 3.16.0
- Use license macro for the COPYING file

* Sun Sep 21 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.14.0-1
- Update to 3.14.0

* Sun Sep 14 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.92-1
- Update to 3.13.92
- Tighten subpackage deps with the _isa macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.12.0-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Richard Hughes <rhughes@redhat.com> - 1:3.12.0-1
- Update to 3.12.0

* Mon Mar 17 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.92-1
- Update to 3.11.92

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.10.0-1
- Update to 3.10.0

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.91-1
- Update to 3.9.91

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Richard Hughes <rhughes@redhat.com> - 1:3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.7.3-1
- Update to 3.7.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.2-1
- Update to 3.6.2

* Wed Sep 26 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.0-1
- Update to 3.6.0

* Mon Jul 23 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.4-1
- Update to 3.5.4
- Dropped the pkgconfig patch, now upstream

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.3-2
- Fix multilib conflicts in -devel by using html docs from the tarball,
  instead of rebuilding them every time (#831409)

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.3-1
- Update to 3.5.3
- Sync summary and description from doap file

* Sun Apr 22 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.4.2-1
- Update to 3.4.2

* Wed Apr 11 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.4.1-1
- Update to 3.4.1
- Avoid depending on gtk-doc for directory ownership (#604383)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 04 2011 Kalev Lember <kalevlember@gmail.com> - 1:3.2.0-1
- Update to 3.2.0

* Wed Jun 15 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.1.2-1
- Update to 3.1.2

* Tue Apr 26 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.0.0-2
- Fix gtk-doc requires

* Tue Apr 05 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.0.0-1
- Update to 3.0.0

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com>  - 1:2.91.4-4
- Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.91.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 1:2.91.4-2
- Rebuild against newer gtk

* Tue Jan 11 2011 Rakesh Pandit <rakesh@fedoraproject.org> - 1:2.91.1-1
- Updated to 2.91.4

* Thu Oct 07 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1:2.30.1-1
- revert to 2.30.1, bump epoch to 1
- see: https://bugzilla.redhat.com/show_bug.cgi?id=635333

* Thu Aug 05 2010 Debarshi Ray <rishi@fedoraproject.org> - 2.31.3-1
- Version bump to 2.31.3.
  * GNOME Goal: use accessor functions instead direct access. (GNOME Bugzilla
    #612497)
  * http://download.gnome.org/sources/gdl/2.31/gdl-2.31.3.news
  * http://download.gnome.org/sources/gdl/2.31/gdl-2.31.2.news
- Enabled GObject Introspection.

* Sun May 23 2010 Debarshi Ray <rishi@fedoraproject.org> - 2.31.1-1
- Version bump to 2.31.1.
  * GNOME Goal: removed deprecated Gtk+ symbols. (GNOME Bugzilla #577469)
  * Removed gdl_dock_layout_get_items_ui and gdl_dock_layout_get_ui from the
    header as they were never defined in the sources. (GNOME Bugzilla #603466)
  * Fixed missing return values. (GNOME Bugzilla #603600)
  * Show icons too when the dock switcher style is set to tabs. (GNOME
    Bugzilla #615113)
- Added 'BuildRequires: gtk-doc' for Fedora 15 too.

* Mon Apr 26 2010 Debarshi Ray <rishi@fedoraproject.org> - 2.30.0-2
- Added 'BuildRequires: gtk-doc' for Fedora 14 too.

* Mon Apr 26 2010 Debarshi Ray <rishi@fedoraproject.org> - 2.30.0-1
- Version bump to 2.30.0.
  * Add a "selected" signal to GdlDockItem.
  * Iconify button now iconifies entire switcher, not just that particular
    item.
  * Do not make dock windows transient. (GNOME Bugzilla #570263)
  * Changed license notice in gdl.h to LGPLv2+. (GNOME Bugzilla #603041)
  * http://download.gnome.org/sources/gdl/2.29/gdl-2.29.92.news
- Mixed source licensing changed to LGPLv2+, and restored COPYING.

* Thu Jan 21 2010 Debarshi Ray <rishi@fedoraproject.org> - 2.28.2-1
- Version bump to 2.28.2.
  * Fix for Gtk+ client-side windows.
  * http://download.gnome.org/sources/gdl/2.28/gdl-2.28.2.news

* Fri Oct 30 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.28.1-2
- Added 'BuildRequires: gtk-doc' for Fedora 13 onwards.

* Fri Oct 30 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.28.1-1
- Version bump to 2.28.1.
  * Added new GdlSwitcherStyle name GDL_SWITCHER_STYLE_NONE. (GNOME Bugzilla
    #589317)
  * Translation updates.
  * http://download.gnome.org/sources/gdl/2.28/gdl-2.28.1.news
  * http://download.gnome.org/sources/gdl/2.27/gdl-2.27.92.news
- Simplified mixed source licensing. There are no GPLv2 files left.

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.27.3-3
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.27.3-1
- Version bump to 2.27.3.
  * Fixed soname generation.
  * Private API hidden.
  * Fixed invisible buttons in HighContrastInverse theme. (GNOME Bugzilla
    #471317)
  * Removed GdlComboButton. Use GtkMenuToolButton instead. (GNOME Bugzilla
    #560820)
  * Optional grip handle hatching. (GNOME Bugzilla #577001)
  * Fixed layout bug in the grip widget headers. (GNOME Bugzilla #577107)
  * GNOME Goal: removed deprecated Gtk+ symbols. (GNOME Bugzilla #577469)
  * Implemented gdl_dock_item_grip_remove. (GNOME Bugzilla #578967)
  * gdl_dock_placeholder_new takes a const gchar*. (GNOME Bugzilla #577938)
  * Fixed grip layout bug where negative rectangles are possible. (GNOME
    Bugzilla #579057)
  * Get rid of libgnome. (GNOME Bugzilla #580860)
  * Ported to GtkBuilder. (GNOME Bugzilla #582511)
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/2.27/gdl-2.27.3.news
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/2.27/gdl-2.27.2.news
- Fix to show objects docked to a GdlDockPaned accepted by upstream.
- Replaced 'BuildRequires: libglade2-devel' with
  'BuildRequires: gtk2-devel libxml2-devel'.

* Fri Jul 10 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.26.2-1
- Version bump to 2.26.2.
  * Translation updates: ar, be, ca@valencia, el, jp and sk.
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/2.26/gdl-2.26.2.news
- Ensure that objects docked to a GdlDockPaned are shown. (GNOME Bugzilla
  #584418)

* Tue Mar 31 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.26.0-1
- Version bump to 2.26.0.
  * Fixed Valgrind violation. (GNOME Bugzilla #574172)
  * Translation updates: el, pl, gl, he, gu, te, cs and or.

* Tue Mar 10 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.25.92-1
- Version bump to 2.25.92.
  * Fixed locked layout mode. (GNOME Bugzilla #573522)
  * Fixed dock/undock/reset behaviour. (GNOME Bugzilla #566801)
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/2.25/gdl-2.25.92.news
- Replaced 'BuildRequires: libgnomeui-devel' with
  'BuildRequires: libglade2-devel'.
- Dropped COPYING because it contains GPLv3, which does not tally with the
  license notices in the source code.

* Wed Feb 25 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.25.91-1
- Version bump to 2.25.91.
  * Updated documentation.
- Removed 'Provides: anjuta-gdl' and 'Obsoletes: anjuta-gdl'.
- Removed 'Requires: gtk2-devel pkgconfig' from libgdl-devel. Let rpm-4.6
  autogenerate them.

* Tue Oct 28 2008 Debarshi Ray <rishi@fedoraproject.org> - 2.24.0-2
- Updated Source0 URL.

* Fri Oct 24 2008 Debarshi Ray <rishi@fedoraproject.org> - 2.24.0-1
- Version bump to 2.24.0.
  * Smaller icons to waste less space.
  * Ported to GLib IO. (GNOME Bugzilla #513845)
  * Ported to GtkTooltip. (GNOME Bugzilla #457562)
  * Translation updates: da, tr, el, it, zh_TW, zh_HK, ru, ar, vi, bg, th, ps,
    sq, pt_BR and mr.
- Rpaths removed by upstream.
- libgdl-gnome-1.so has been dropped.

* Tue Mar 18 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.7.11-1
- Version bump to 0.7.11. (Red Hat Bugzilla #437556)
  * Translation updates: hu, pt_BR, fr, mk, es, lt, hi, uk and cs.
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/0.7/gdl-0.7.11.news

* Sun Mar 02 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.7.10-1
- Version bump to 0.7.10.
  * Added gtk-doc documentation (12% coverage).
  * Avoided critical warnings from GLib.
  * Translation updates: si, sv, pt, fi, ne, ca, gl, pl, en_GB, es, eu, ar,
    nl, th tr and de.
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/0.7/gdl-0.7.10.news
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/0.7/gdl-0.7.9.news
- Added 'BuildRequires: gtk-doc' on Fedora 7.
- Added 'Requires: gtk-doc' for libgdl-devel.
- Replaced 'BuildRequires: chrpath' with 'BuildRequires: libtool' for removing
  rpaths.

* Sun Feb 03 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.7.8-2
- Omitted unused direct shared library dependencies.

* Mon Jan 28 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.7.8-1
- Version bump to 0.7.8.
  * Smaller icons to waste less space.
  * Backported several small improvements from MonoDevelop.
  * Translation updates: es, vi, ar, sl, bg, ko, nb, oc, ar, eu, sv and uk.
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/0.7/gdl-0.7.8.news
- Fixed gdl-1.0.pc.in and gdl-gnome-1.0.pc.in by trimming 'Requires' list.

* Sat Dec 15 2007 Debarshi Ray <rishi@fedoraproject.org> - 0.7.7-1
- Initial build. Imported SPEC from Rawhide and renamed as libgdl from
  anjuta-gdl.
  * Fixed crash when maximizing already removed widget. (GNOME Bugzilla
    #317004)
  * Fixed crash in button layout.
  * http://ftp.gnome.org/pub/GNOME/sources/gdl/0.7/gdl-0.7.7.news
