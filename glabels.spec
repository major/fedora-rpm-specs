Name:		glabels
Version:	3.4.1
Release:	19%{?dist}
Summary:	A program for creating labels and business cards for GNOME

License:	GPLv3+
URL:		http://www.glabels.org

Source0:	http://ftp.gnome.org/pub/GNOME/sources/glabels/3.4/glabels-%{version}.tar.xz
Patch01:	glabels-externs.patch

## TODO: GNU Barcode unfortunately only provides a static library at this
## If/when Barcode provides a shared library in the future, we'll
## use that package here instead of barcode-static.
BuildRequires:	barcode-static
BuildRequires:	desktop-file-utils
BuildRequires:	evolution-data-server-devel >= 3.45.1
BuildRequires:	gettext
BuildRequires:	gtk3-devel
BuildRequires:	gtk-doc
BuildRequires:	iec16022-devel
BuildRequires:	intltool
BuildRequires:	libxml2 >= 2.6
BuildRequires:	librsvg2-devel
BuildRequires:	libtool
BuildRequires:	perl(XML::Parser)
BuildRequires:	qrencode-devel
BuildRequires:	zint-devel
BuildRequires:	itstool
BuildRequires: make

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-doc = %{version}-%{release}
Requires:	%{name}-templates = %{version}-%{release}

%description
gLabels is a lightweight program for creating labels and
business cards for the GNOME desktop environment.
It is designed to work with various laser/ink-jet peel-off
label and business card sheets that you'll find at most office
supply stores.


%package	devel
Summary:	Development files and documentation for %{name}
License:	LGPLv3+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation for
libglabels. 


%package 	doc
License:	CC-BY-SA
Summary:	Runtime documentation for %{name}

%description	doc
This package contains the runtime documentation and manual pages for %{name}. 


%package 	libs
License:	LGPLv3+
Summary:	Development files and documentation for %{name}

%description	libs
This package contains the shared libraries for %{name}. 


%package 	templates
License:	MIT
Summary:	The %{name} template database 
## Needs the glabels-libs subpackage for proper ownership of the top-level
## libglabels-3.0 directory in %%_datadir.
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	templates
This package contains the template database for %{name}.


%prep
%setup -q
%patch01 -p1 -b .externs

%build
%configure --enable-gtk-doc
make LIBTOOL=%{_bindir}/libtool %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
desktop-file-install					\
	--dir %{buildroot}%{_datadir}/applications	\
	--delete-original				\
	%{buildroot}%{_datadir}/applications/glabels-3.0.desktop
%find_lang glabels-3.0


%ldconfig_scriptlets	libs

%files -f glabels-3.0.lang
%doc AUTHORS ChangeLog COPYING COPYING.README_FIRST NEWS README TODO
%{_bindir}/glabels-3*
%{_datadir}/applications/*glabels-3.0.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.glabels-3.gschema.xml
%{_datadir}/icons/hicolor/*/apps/glabels-3.0.png
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-glabels.png
%{_datadir}/mime/packages/glabels-3.0.xml
%{_datadir}/appdata/glabels-3.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/glabels-3.0.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-glabels.svg

%files	devel
%doc AUTHORS COPYING-LIBS
%{_includedir}/libglabels-3.0/
%{_includedir}/libglbarcode-3.0/
%{_libdir}/libglabels-3.0.so
%{_libdir}/libglbarcode-3.0.so
%{_libdir}/pkgconfig/libglabels-3.0.pc
%{_libdir}/pkgconfig/libglbarcode-3.0.pc

%files	doc
## Manual ("man") pages are automatically marked as %%doc by RPM.
%doc AUTHORS COPYING-DOCS
%doc %{_datadir}/help/*/glabels-3.0/
%{_mandir}/man?/glabels-3*
%{_datadir}/gtk-doc/html/libglabels-3.0/
%{_datadir}/gtk-doc/html/libglbarcode-3.0/

%files	libs
%doc AUTHORS COPYING-LIBS
%dir %{_datadir}/libglabels-3.0/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_datadir}/glabels-3.0/
%{_libdir}/libglabels-3.0.so.*
%{_libdir}/libglbarcode-3.0.so.*

%files templates
%doc AUTHORS COPYING-TEMPLATES
%{_datadir}/libglabels-3.0/dtd/
%{_datadir}/libglabels-3.0/templates/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 3.4.1-17
- Rebuilt for evolution-data-server soname version bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 3.4.1-14
- Rebuilt for evolution-data-server soname version bump

* Tue Feb 02 2021 Martin Gieseking <martin.gieseking@uos.de> - 3.4.1-13
- Rebuilt for libzint.so.2.9.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 3.4.1-9
- Rebuilt for evolution-data-server soname version bump

* Mon Feb 03 2020 Milan Crha <mcrha@redhat.com> - 3.4.1-8
- Add patch to fix broken build (define shared variables as extern)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Martin Gieseking <martin.gieseking@uos.de> - 3.4.1-6
- Rebuilt for libzint.so.2.6 (zint 2.6.6: ABI changes without soname bump)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 3.4.1-4
- Rebuilt (libqrencode.so.4)

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 3.4.1-3
- Rebuilt for evolution-data-server soname bump

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.4.1-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 3.4.0-9
- Rebuilt for evolution-data-server soname bump

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Milan Crha <mcrha@redhat.com> - 3.4.0-6
- Rebuild for newer libzint

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Milan Crha <mcrha@redhat.com> - 3.4.0-4
- Rebuild for newer evolution-data-server

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 3.4.0-3
- Rebuild for newer evolution-data-server

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 3.4.0-2
- Rebuild for newer evolution-data-server

* Wed May 25 2016 Peter Gordon <peter@thecodergeek.com> - 3.4.0-1
- Update to new upstream release (3.4.0)
  * Fixes many bugs, including missing contacts on vcard import, potential
    crashes on "Select All", delayed rotation/flipping, and incorrect
    sensitivity of first handle of line objects.
  * Additional enhancements include auto-detection of CSV file encoding,
    object-dragging enhancements, added properties dialog, and a GS1 input
    mode for Datamatrix barcodes.
  * Many new templates and fixes to existing product templates.
  * Updated UI and documentation translations.
- Resolves: #1339690 (New upstream version available).

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> - 3.2.1-8
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Milan Crha <mcrha@redhat.com> - 3.2.1-6
- Rebuild for newer evolution-data-server

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> - 3.2.1-5
- Rebuild for newer evolution-data-server

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 3.2.1-3
- Rebuild for newer evolution-data-server

* Tue Feb 17 2015 Milan Crha <mcrha@redhat.com> - 3.2.1-2
- Rebuild for new evolution-data-server.

* Wed Nov 12 2014 Peter Gordon <peter@thecodergeek.com> - 3.2.1-1
- Update to new upstream release (3.2.1)
- Fixes "new label" crash with GTK+ 3.14
- Resolves bug #1161836 (Glabels is crashing when clicking on File New.)

* Wed Sep 24 2014 Milan Crha <mcrha@redhat.com> - 3.2.0-9
- Rebuild against newer evolution-data-server.

* Tue Sep 09 2014 Rex Dieter <rdieter@fedoraproject.org> 3.2.0-8
- update scriptlets, tighten subpkg deps

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Milan Crha <mcrha@redhat.com> - 3.2.0-6
- Rebuild for new evolution-data-server.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Peter Gordon <peter@thecodergeek.com> - 3.2.0-4
- Rebuild for new evolution-data-server (libcamel).

* Wed Jan 22 2014 Peter Gordon <peter@thecodergeek.com> - 3.2.0-3
- Rebuild for new evolution-data-server (libcamel dependency).

* Wed Dec 4 2013 Maxim Burgerhout <maxim@wzzrd.com> - 3.2.0-2
- Remove dependency on gnome-doc-utils and gnome-doc-utils-stylesheets

* Tue Nov 19 2013 Peter Gordon <peter@thecodergeek.com> - 3.2.0-1
- Update to new upstream release (3.2.0)
  * Fixes many bugs, including: object editor no longer remains active after
    object is deleted; text directly embedded to printstream rather than
    outline; and a workaround for pango kerning bug (pango-cairo bug #700592).
  * Includes AppData metadata (for Software Center, et al.)
  * Documentation updates.
  * New templates and fixes
- Add BR: itstool
- Drop evolution-data-server build fix (applied upstream):
  - new-eds.patch
- Fix bogus dates (days of week) in older %%changelog entries.

* Sat Oct 26 2013 Peter Gordon <peter@thecodergeek.com> - 3.0.1-11
- Rebuild for new libcamel.

* Sat Aug 24 2013 Peter Gordon <peter@thecodergeek.com> - 3.0.1-10
- Rebuild for new evolution-data-server.

* Sat Jul 27 2013 Bruno Wolff III <bruno@wolff.to> - 3.0.1-9
- Rebuild for libcamel soname bump

* Sat May 11 2013 Maxim Burgerhout <maxim@wzzrd.com> - 3.0.1-8
- Rebuild for new evolution-data-server

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 3.0.1-7
- Drop desktop vendor tag.

* Sun Mar 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.1-6
- Add BR gtk-doc to fix FTBFS on ARM

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 25 2012 Bruno Wolff III <bruno@wolff.to> - 3.0.1-4
- Rebuild for libcamel soname bump

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 3.0.1-3
- Rebuild for libcamel soname bump

* Thu Oct 25 2012 Maxim Burgerhout <maxim@wzzrd.com> - 3.0.1-2
- Rebuild for new evolution-data-server (libcamel dependency)

* Tue Sep 18 2012 Maxim Burgerhout <maxim@wzzrd.com> - 3.0.1-1
- Update to new upstream release 3.0.1 for bugfixes, new templates
- Close #858375

* Wed Aug 29 2012 Maxim Burgerhout <maxim@wzzrd.com> - 3.0.0-17
- Rebuilt with glabels-3.0.0-new-eds.patch to solve build problems
- Resolves: #852687 (Build break patch for F18 and Rawhide)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Peter Gordon <peter@thecodergeek.com> - 3.0.0-15
- Fix %%doc files conflict between the glabels-devel and glabels-doc
  subpackages.
- Resolves: #831384 (glabels-devel-3.0.0-14.fc17.i686 doc file conflict)

* Tue Mar 20 2012 Peter Gordon <peter@thecodergeek.com> - 3.0.0-14
- Add patch to fix child schemas in the gschema.xml file:
  + fix-child-schemas.patch
- Resolves: #795241 (glabels has invalid schema file)

* Wed Jan 04 2012 Peter Gordon <peter@thecodergeek.com> - 3.0.0-13
- Rebuild for GCC 4.7

* Thu Nov 24 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-12
- Rebuild for new evolution-data-server (libebook dependency).

* Sun Nov 06 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-11
- Rebuild for new libpng.

* Sat Oct 29 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-10
- Rebuild for new evolution-data-server (libcamel and
  libedataserver dependencies).

* Sat Sep 03 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-9
- Rebuild for new evolution-data-server (libcamel dependency).

* Sun Aug 28 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-8
- Rebuild for new evolution-data-server (libebook and
  libedataserver dependencies).

* Tue Aug 16 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-7
- Rebuild for new evolution-data-server (libebook and
  libedataserver dependencies).

* Sat Jul 30 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-6
- Make the glabels-devel subpackage dependency on glabels-libs be
  arch-specific, in accordance with updated packaging guidelines.

* Mon Jul 25 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-5
- Rebuild for new evolution-data-server (libcamel dependency).

* Tue Jul 05 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-4
- Rebuild for new evolution-data-server (libcamel dependency).

* Mon Jun 20 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-3
- Switch BuildRequires barcode-devel to barcode-static, since GNU Barcode
  provides only a static library to build against. This is to comply with the
  Fedora guidelines for packaging of static libraries.
- Resolves: #714350 (glabels : does not adhere to Static Library Packaging
  Guidelines)

* Tue Jun 14 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-2
- Rebuild for new evolution-data-server (libebook and libcamel dependencies).

* Thu Jun 09 2011 Peter Gordon <peter@thecodergeek.com> - 3.0.0-1
- Update to new upstream development release (3.0.0).
  * Ported to GTK+ 3 and gsettings.
  * Documentation ported to Mallard.
  * Adds native SVG support.
  * Vastly reworked and improved barcode handling.
  * Updated logo and theme-friendly icons.
  * Adds many new templates and updated translations.
  * Undo/Redo capability (from 2.3.0).
  * Updated license from GPLv2+ to GPLv3+ (from 2.3.0).
  * Lots of UI enhancements (from 2.3.0).
- Add glabels-templates subpackage (MIT/X11 License).
- Remove %%defattr lines in %%files listings, and fix scriptlets and buildroot
  usage in accordance with updated packaging guidelines.
- Update Source0 and homepage URLs.
- Remove fix for encodings (now UTF-8 from upstream).
- Other minor (aesthetic) spec fixes.
- Resolves: #706635 (New upstream version available).

* Sun May 15 2011 Maxim Burgerhout <wzzrd@fedoraproject.org> - 2.2.8-5
- Remove XML_PARSE_HUGE patch (closes #676839)
- Resolves: #676839 (obsolete patch in srpm).
- Rebuild for Rawhide against new evolution-data-server for libcamel dependency

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 Caolán McNamara <caolanm@redhat.com> - 2.2.8-3
- Rebuild for new evolution 

* Sat Jun 26 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.2.8-2
- Rebuild for new evolution 

* Mon May 24 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.2.8-1
- New upstream release 

* Sat Apr 10 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.2.7-1
- New upstream release 

* Wed Nov 25 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.2.6-1
- New upstream release which fixes bug 528352

* Mon Oct 12 2009 Peter Gordon <peter@thecodergeek.com> - 2.2.5-2
- Apply backported patch from upstream git as a fix for recent changes in
  libxml behavior:
  + libxml-XML_PARSE_HUGE.patch
- Thanks to Ralf Corsepius for the bug report and patch.
- Resolves: #528352 (glabels can't read saved projects)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Peter Gordon <peter@thecodergeek.com> - 2.2.5-1
- Update to new upstream bug-fix release (2.2.5):
  * Fixed spinbutton/adjustment bugs that made glabels unusable with Gtk 2.16.
  * Fixed default preview colors in color combos.
  * Updated german translation.
  * New templates.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 07 2009 Peter Gordon <peter@thecodergeek.com> - 2.2.4-1
- Update to new upstream bug-fix release (2.2.4):
  * Corrected button order in "Open" and "Save as" dialogs.
  * Fixed performance problem when large number of fonts are installed.
  * Corrected several i18n problems.
  * Fixed "paste" bug that created phantom object views.
  * Fixed performance problem when many objects are selected.
  * New templates.  

* Tue Aug 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.3-2
- fix license tag (again)

* Thu Aug 21 2008 Peter Gordon <peter@thecodergeek.com> - 2.2.3-1
- Update to new upstream bug-fix release (2.2.3).
- Drop glabels-batch segfault patch (fixed upstream).
  - fix-batch-segfault.patch 

* Fri Aug 08 2008 Peter Gordon <peter@thecodergeek.com> - 2.2.2-3
- Add patch from Casey Harkins to fix a segfault in glabels-batch:
  + fix-batch-segfault.patch
- Resolves: bug #458473.

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.2-2
- fix license tag

* Tue Mar 04 2008 Peter Gordon <peter@thecodergeek.com> - 2.2.2-1
- Update to new upstream bug-fix release (2.2.2).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.1-2
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Peter Gordon <peter@thecodergeek.com> - 2.2.1-1
- Update to new upstream bug-fix release (2.2.1).

* Mon Jan 14 2008 Peter Gordon <peter@thecodergeek.com> - 2.2.0-1
- Update to new upstream release (2.2.0 Final); Yay!

* Sun Dec 16 2007 Peter Gordon <peter@thecodergeek.com> - 2.1.5-1
- Update to new upstream development snapshot (2.1.5).

* Tue Aug 21 2007 Peter Gordon <peter@thecodergeek.com> - 2.0.4-7
- Rebuild with new BuildID-enabled binutils. 

* Fri Aug 03 2007 Peter Gordon <peter@thecodergeek.com> - 2.0.4-6
- Update License tagging (GPLv2+). This necessitates a split of two
  subpackages:
  (1) glabels-doc: Runtime documentation for gLabels (GFDLv1.1+)
  (2) glabels-libs: Shared libraries for gLabels (LGPLv2+)
- Fix version in previous %%changelog entry.
- Lots and lots of aesthetic spec file changes.
- Remove X-Fedora category from desktop-file-install invocation.
- Add TODO to installed %%doc files. 

* Sun Aug 27 2006 Peter Gordon <peter@thecodergeek.com> - 2.0.4-5
- Add BR: perl(XML::Parser)

* Sun Aug 27 2006 Peter Gordon <peter@thecodergeek.com> - 2.0.4-4
- Mass FC6 rebuild

* Wed Jul 05 2006 Peter Gordon <peter@thecodergeek.com> - 2.0.4-3
- Add BuildRequires: gettext (#197633)

* Sat Feb 18 2006 Jef Spaleta <jspaleta@gmail.com> - 2.0.4-2
- Bump for fe5 rebuild

* Sun Jan 01 2006 Jef Spaleta <jspaleta@gmail.com> - 2.0.4-1
- Update to new stable upstream version

* Thu Aug 18 2005 Jef Spaleta <jspaleta@gmail.com> - 2.0.3-3
- rebuild

* Thu Jul 7 2005 Jef Spaleta <jspaleta@gmail.com> - 2.0.3-2
- use Source0

* Tue Jul 5 2005 Jef Spaleta <jspaleta@gmail.com> - 2.0.3-1
- Initial fedora extras build

