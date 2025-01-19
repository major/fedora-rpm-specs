Name:		gtranslator
Version:	47.1
Release:	2%{?dist}
Summary:	Gettext po file editor for GNOME

# Sources are GPL-2.0-or-later and GPL-3.0-or-later, help is CC-BY-SA-3.0 and
# AppData is CC0-1.0.
License:	GPL-2.0-or-later AND GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:		https://wiki.gnome.org/Apps/Gtranslator
Source0:	https://download.gnome.org/sources/%{name}/47/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk4) >= 4.12.0
BuildRequires:	pkgconfig(gtksourceview-5)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libadwaita-1) >= 1.5.99
BuildRequires:	pkgconfig(libgda-6.0)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libspelling-1)
BuildRequires:	pkgconfig(libxml-2.0)

Requires:	hicolor-icon-theme
Requires:	gsettings-desktop-schemas
Requires:	libgda-sqlite%{?_isa}

%description
gtranslator is an enhanced gettext po file editor for the GNOME
desktop environment. It handles all forms of gettext po files and
features many comfortable everyday usage features like find and
replace functions, auto translation, and translation learning,

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/gtranslator
%{_datadir}/applications/org.gnome.Gtranslator*.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gtranslator*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.Gtranslator.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gtranslator.plugins.translation-memory.gschema.xml
%{_datadir}/gtksourceview-5/language-specs/gtranslator.lang
%{_datadir}/gtranslator/
%{_metainfodir}/org.gnome.Gtranslator.appdata.xml
%{_mandir}/man1/gtranslator.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 03 2024 nmontero <nmontero@redhat.com> - 47.1-1
- Update to 47.1

* Sat Oct 05 2024 Artem Polishchuk <ego.cordatus@gmail.com> - 47.0-1
- Update to 47.0 (#2316636)

* Fri Sep 13 2024 Carl George <carlwgeorge@fedoraproject.org> - 46.1-3
- Rebuild for libspelling soname bump rhbz#2312315

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 23 2024 David King <amigadave@amigadave.com> - 46.1-1
- Update to 46.1 (#2223755)

* Thu Mar 21 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 02 2023 Kalev Lember <klember@redhat.com> - 45.3-1
- Update to 45.3
- Switch to pkgconfig buildrequires

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 09 2022 Kalev Lember <klember@redhat.com> - 42.0-1
- Update to 42.0
- Switch to libgda 6 and libsoup 3

* Thu Aug 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 40.0-5
- libgda rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 29 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0
- Remove old obsoletes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0
- Remove unnecessary python byte compilation, fixing FTBFS (#1863841)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 14 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Aug 20 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Sat Nov 03 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0
- Switch to the meson build system
- Remove ldconfig scriptlets
- Remove group tags
- Remove gtranslator-devel subpackage, move docs to the main package
- Update upstream URLs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Bastien Nocera <bnocera@redhat.com> - 2.91.7-13
+ gtranslator-2.91.7-13
- Use the python3 libpeas loader

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.91.7-11
- Remove obsolete scriptlets

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 2.91.7-10
- Disable gnome-dictionary support
- Don't build opentran plugin as the service was shut down

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 Kalev Lember <klember@redhat.com> - 2.91.7-5
- Add missing dep on libgda-sqlite (#842050)

* Thu Aug 20 2015 Kalev Lember <klember@redhat.com> - 2.91.7-4
- Rebuilt for libgdict soname bump

* Sat Jul 04 2015 Kalev Lember <klember@redhat.com> - 2.91.7-3
- Require libpeas-loader-python for Python plugin support (#1226879)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Kalev Lember <kalevlember@gmail.com> - 2.91.7-1
- Update to 2.91.7
- Use %%license macro for the COPYING file

* Sun Mar 08 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.91.6-8
- Rebuild for libgdict

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.91.6-6
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 2.91.6-3
- Rebuilt for gtksourceview3 soname bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 2.91.6-1
- Update to 2.91.6

* Mon Oct 22 2012 Kalev Lember <kalevlember@gmail.com> - 2.91.5-5
- Rebuilt with libgda 5.1

* Wed Sep 26 2012 Kalev Lember <kalevlember@gmail.com> - 2.91.5-4
- Rebuilt for libgdl 3.6.0 soname bump

* Mon Jul 23 2012 Kalev Lember <kalevlember@gmail.com> - 2.91.5-3
- Rebuilt for libgdl 3.5.4 soname bump

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 2.91.5-1
- Update to 2.91.5

* Sat May 05 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 2.91.4-1
- Update to 2.91.4

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 2.91.3-3
- Silence rpm scriptlet output

* Mon Apr 23 2012 Kalev Lember <kalevlember@gmail.com> - 2.91.3-2
- Rebuilt for libgdl 3.4.2 soname bump

* Fri Apr 20 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 2.91.3-1
- Update to 2.91.3

* Mon Apr 09 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 2.91.2-1
- Update to 2.91.2

* Sat Mar 24 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 2.91.1-1
- Update to 2.91.1

* Mon Feb 06 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 2.90.8-1
- Update to 2.90.8

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 19 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 2.90.7-1
- Update to 2.90.7

* Thu Oct 13 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 2.90.6-1
- Update to 2.90.6

* Wed Jun 15 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.90.5-1
- Update to 2.90.5

* Wed May 18 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.90.4-1
- Update to 2.90.4

* Wed May  4 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.90.3-1
- Update to 2.90.3

* Wed Apr 27 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.90.2-1
- Update to 2.90.2

* Tue Apr 05 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 2.90.1-1
- Update to 2.90.1

* Fri Apr 01 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 2.90.0-1
- Update to 2.90.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 13 2010 Chen Lei <supercyper@163.com> - 1.9.12-1
- Update to 1.9.12

* Fri Jul 16 2010 Chen Lei <supercyper@163.com> - 1.9.11-3
- Disable debugging flags(-ggdb -DDEBUG)
- Fix to honor %%{optflags} correctly

* Fri Jul 16 2010 Chen Lei <supercyper@163.com> - 1.9.11-2
- Remove *.la files

* Fri Jul 16 2010 Chen Lei <supercyper@163.com> - 1.9.11-1
- Update to 1.9.11
- Clean up spec agaist latest guideline

* Fri Apr 30 2010 Caius 'kaio' Chance <me at kaio.net> - 1.9.10-3
- Remove scrollkeeper and desktop-file-utils.
- Rarian has placed scrollkeeper and no scriptlet needed for rarian.
  https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Scrollkeeper

* Thu Apr 29 2010 Caius 'kaio' Chance <me at kaio.net> - 1.9.10-2
- Update license info.
- Added requires of hicolor-icon-theme.
- Converted README.umtf to UTF-8.

* Fri Apr 23 2010 Gianluca Sforna <giallu gmail com> - 1.9.10-1
- new upstream release

* Thu Nov  5 2009 Bill Nottingham <notting@redhat.com> - 1.9.6-2
- Rebuild against newer libgdl

* Tue Sep 29 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.9.6-1
- Update to 1.9.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.9.5-2
- Update for new gdl and requiring libuuid directly

* Sat May 30 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.9.5-1
- Update to 1.9.5 with help of patch by Arkady Shane. New version required a bunch of changes:
- Dropped old patches
- Adjust Requires
- Added new scriplets
