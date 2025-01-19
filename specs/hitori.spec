Name:		hitori
Version:	44.0
Release:	6%{?dist}
Summary:	Logic puzzle game for GNOME
Summary(de):	Logikpuzzle für GNOME

# The executable is licensed under GPLv3+, while the user manual is CC-BY-SA.
License:	GPL-3.0-or-later and CC-BY-SA-3.0
URL:		https://wiki.gnome.org/Apps/Hitori
Source0:	https://download.gnome.org/sources/hitori/3.38/hitori-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	/usr/bin/appstream-util
BuildRequires:	/usr/bin/xmllint

%description
A small application written to allow one to play the Hitori puzzle game,
which is similar in theme to more popular puzzles such as Sudoku.

It has full support for playing the game (i.e. it checks all three rules are
satisfied). It has undo/redo support, can give hints, and allows for cells
to be tagged with one of two different tags, to aid in solving the puzzle.
It has support for anything from 5×5 to 10×10 grids.

%description -l de
Ein kleines Programm zum Spielen des Hitori-Puzzles, das thematisch
populäreren Puzzlespielen wie beispielsweise Sudoku ähnelt.

Das Programm unterstützt die Spielregeln vollständig. Es wird in
jedem Fall überprüft, ob die drei Ausschlussregeln angewendet sind.
Das Zurücknehmen und Wiederholen von Zügen ist ebenso möglich wie das
Kennzeichnen von Feldern mit einer oder mehreren Markierungen, um den Weg zur
Lösung zu erleichtern. Mögliche Spielfeldgrößen reichen von 5x5 bis hin zu
10x10 Feldern. 

%prep
%setup -q

%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Hitori.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Hitori.desktop


%files -f %{name}.lang
%license COPYING COPYING-DOCS
%doc AUTHORS MAINTAINERS NEWS README.md
%{_bindir}/hitori
%{_datadir}/applications/org.gnome.Hitori.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.hitori.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Hitori.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Hitori-symbolic.svg
%{_metainfodir}/org.gnome.Hitori.appdata.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 11 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.38.4-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 04 2022 David King <amigadave@amigadave.com> - 3.38.4-1
- Update to 3.38.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Kalev Lember <klember@redhat.com> - 3.38.3-1
- Update to 3.38.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Fri Mar 05 2021 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Thu Sep 03 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Wed Aug 19 2020 Kalev Lember <klember@redhat.com> - 3.37.0-1
- Update to 3.37.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Feb 24 2020 Kalev Lember <klember@redhat.com> - 3.35.0-1
- Update to 3.35.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Fri Aug 23 2019 Kalev Lember <klember@redhat.com> - 3.33.0-1
- Update to 3.33.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.0-1
- Update to 3.31.0
- Switch to the meson build system

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.22.4-2
- Remove obsolete scriptlets

* Thu Oct 12 2017 Kalev Lember <klember@redhat.com> - 3.22.4-1
- Update to 3.22.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Kalev Lember <klember@redhat.com> - 3.22.3-1
- Update to 3.22.3

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2

* Tue Feb 14 2017 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1
- Validate appdata file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Don't set group tags

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Kalev Lember <klember@redhat.com> - 3.19.1-1
- Update to 3.19.1
- Update urls
- Use make_install macro
- Move desktop file validation to %%check

* Thu Nov 19 2015 Kalev Lember <klember@redhat.com> - 3.16.2-1
- Update to 3.16.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1
- Include new symbolic icon

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Wed Mar 04 2015 Kalev Lember <kalevlember@gmail.com> - 3.14.3-1
- Update to 3.14.3
- Use the %%license macro for the COPIYNG files

* Thu Dec 18 2014 Richard Hughes <rhughes@redhat.com> - 3.14.2.1-1
- Update to 3.14.2.1

* Sun Oct 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0.1-1
- Update to 3.14.0.1

* Wed Sep 17 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90
- Use %%find_lang --with-gnome for finding the help documentation
- Drop huge ChangeLog file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-2
- Add rpm scripts for glib-compile-schemas

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Mario Blättermann <mariobl@fedoraproject.org> - 0.4.0-1
- New upstream release
- Drop gettext from BR
- Some cleanup
- Add patch for German translations

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild


* Mon May 28 2012 Mario Blättermann <mariobl@fedoraproject.org> - 0.3.2-1
- New upstream version
- Removed the patch because it doesn't depend on libm anymore
- Tweaked the description

* Sat Mar  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-4
- Merge F-16 to master as it's a newer version
- Fix FTBFS

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.1-2
- Rebuild for new libpng

* Sun Jun 19 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.3.1-1
- New upstream version
- Fixes GNOME bug #652399 (l10n doesn't work)

* Sun Jun 12 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.3.0-1
- New upstream version

* Fri Feb 18 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.2.6-3
- Changed native English and German description
- Added ChangeLog to %%doc

* Tue Feb 15 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.2.6-2
- Added German summary and description

* Sun Jan 30 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.2.6-1
- Bumped version to 0.2.6
- Added COPYING-DOCS again, see GNOME upstream bug #640905

* Sat Jan 29 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.2.5-4
- some fixes to licensing
- moved icon cache macros to their right places
- revamped file list

* Sat Jan 29 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.2.5-3
- locale dir dropped from filelist
- changed license according to the mixed usage of licenses for executables
  and docs
- added macros for updating the icon cache
- dropped COPYING-DOCS from filelist because it is obsolete

* Tue Jan 25 2011 Mario Blättermann <mariobl@fedoraproject.org> 0.2.5-2
- added find_lang macro
- changed summary and description
- changed group
- added desktop file handling
- added new Requires and BuildRequires

* Sun Nov 07 2010 Mario Blättermann <mariobl@fedoraproject.org> 0.2.5-1
- initial package
