Name:		denemo
Version:	2.6.0
Release:	16%{?dist}
Summary:	Graphical music notation program
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later

Source:		https://ftp.gnu.org/gnu/denemo/denemo-%{version}.tar.gz
Source1:	%{name}-feta.metainfo.xml
Source2:	%{name}-emmentaler.metainfo.xml
Source3:	%{name}-music.metainfo.xml
Patch1:		%{name}-%{version}-configure.patch
# Upstream patch: https://savannah.gnu.org/bugs/index.php?63720
Patch2:		%{name}-%{version}-c99.patch
Patch3:		%{name}-guile-3.0.patch

URL: http://www.denemo.org/

BuildRequires: gcc libtool
BuildRequires: portaudio-devel aubio-devel guile30-devel
BuildRequires: gettext libxml2-devel fftw-devel desktop-file-utils
BuildRequires: libtool-ltdl-devel jack-audio-connection-kit-devel
BuildRequires: fontpackages-devel lash-devel libsamplerate-devel
BuildRequires: fluidsynth-devel librsvg2-devel gtk3-devel
BuildRequires: chrpath libsndfile-devel atril-devel gtksourceview3-devel
BuildRequires: portmidi-devel intltool rubberband-devel
BuildRequires: make autoconf automake gtk-doc

Requires: lilypond
Requires: denemo-music-fonts = %{version}-%{release}
Requires: denemo-emmentaler-fonts = %{version}-%{release}
Requires: denemo-feta-fonts = %{version}-%{release}


%description
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

%package music-fonts
Summary:	Denemo Denemo fonts
BuildArch:	noarch
Requires:	fontpackages-filesystem
Requires:	denemo-fonts-common = %{version}-%{release}

%description music-fonts 
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

These are the Denemo.ttf fonts derived from FreeSerif.ttf and FreeSans.ttf. 

%package emmentaler-fonts
Summary:	Denemo emmentaler fonts
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
BuildArch:	noarch
Requires:	fontpackages-filesystem
Requires:	denemo-fonts-common = %{version}-%{release}

%description emmentaler-fonts 
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

These are the emmentaler.ttf fonts derived from lilypond's fonts.

%package feta-fonts
Summary:	Denemo feta fonts
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
BuildArch:	noarch
Requires:	fontpackages-filesystem
Requires:	denemo-fonts-common = %{version}-%{release}

%description feta-fonts 
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

These are the feta.ttf fonts derived from lilypond's fonts.

%package fonts-common
Summary:	Denemo fonts common dir
BuildArch:	noarch
Requires:	fontpackages-filesystem

%description fonts-common
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

This contains the directory common to all Denemo fonts.

%prep
%autosetup -p1

%build
autoupdate
autoreconf -if
%configure --enable-jack=yes --disable-binreloc --enable-guile_3_0=yes

%make_build
chrpath -d src/denemo
chmod 644 actions/*.scm

%install
%make_install

desktop-file-install --vendor=""\
	--dir=%{buildroot}/%{_datadir}/applications\
	--add-category=X-Notation\
	%{buildroot}/%{_datadir}/applications/org.denemo.Denemo.desktop

%find_lang %{name}
install -m 0755 -d %{buildroot}/%{_datadir}/denemo/fonts
install -m 0755 -d %{buildroot}%{_fontdir}
rm -f %{buildroot}/%{_bindir}/denemo-lilypond.bat


install -m 0644 -p fonts/*.ttf %{buildroot}%{_fontdir}
rm -rf %{buildroot}/%{_datadir}/fonts/truetype
rm -rf %{buildroot}/%{_includedir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}-feta.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/appdata/%{name}-emmentaler.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
	%{buildroot}%{_datadir}/appdata/%{name}-music.metainfo.xml

%files -f %{name}.lang
%license COPYING
%doc ChangeLog
%dir %{_datadir}/denemo
%{_datadir}/denemo/*
%{_datadir}/pixmaps/org.denemo.Denemo.png
%{_datadir}/applications/org.denemo.Denemo.desktop
%{_bindir}/*
%{_datadir}/appdata/org.denemo.Denemo.appdata.xml

%_font_pkg -n feta feta.ttf
%{_datadir}/appdata/%{name}-feta.metainfo.xml

%_font_pkg -n emmentaler emmentaler.ttf
%{_datadir}/appdata/%{name}-emmentaler.metainfo.xml

%_font_pkg -n music Denemo.ttf
%{_datadir}/appdata/%{name}-music.metainfo.xml

%files fonts-common
%license COPYING
%doc AUTHORS
%defattr(0644,root,root,0755)


%changelog
* Thu Jan 09 2025 Michel Lind <salimma@fedoraproject.org> - 2.6.0-16
- Rebuilt for rubberband 4

* Mon Sep 30 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2.6.0-15
- Build against guile 3.0
- Spec file cleanups

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.0-14
- convert license to SPDX

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.0-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Roy Rankin <rrankin@ihug.com.au> - 2.6.0-11
- Use atril rather than evince. This fixes invalid pointer issue and makes proofreading work properly.

* Thu Feb 01 2024 Roy Rankin <rrankin@ihug.com.au> - 2.6.0-10
- Add patch for invalid pointer

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Nikita Popov <npopov@redhat.com> - 2.6.0-6
- Port sffile.c to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 14 2022 Roy Rankin <rrankin@ihug.com.au> - 2.6.0-4
> - fix jack-audio dependency, configure issue

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 23 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-2
- Prepare for new libtool

* Fri Mar 11 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-1
- 2.6.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-4
- License tag fixes.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-2
- Fluidsynth rebuild.

* Wed Mar 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-1
- 2.5.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 29 2020 Roy Rankin <rrankin@ihug.com.au> - 2.4.0-3
- use guile 2.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.4.0-1
- 2.4.0

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.3.0-4
- Rebuild against fluidsynth2

* Tue Feb 04 2020 Roy Rankin <rrankin@ihug.com.au> - 2.3.0-3
- Add patch for gcc 10.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.3.0-1
- 2.3.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Adam Williamson <awilliam@redhat.com> - 2.2.0-4
- Rebuild for new aubio

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.2.0-1
- 2.2.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.1-1
- 2.1, BZ 1435491.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Jon Ciesla <limburgher@gmail.com> - 2.0.14-2
- Fix FTBFS.

* Wed Nov 30 2016 Jon Ciesla <limburgher@gmail.com> - 2.0.14-1
- 2.0.14, BZ1400117

* Thu Oct 06 2016 Jon Ciesla <limburgher@gmail.com> - 2.0.12-1
- 2.0.12, patch for desktop error.

* Sun Apr 17 2016 Roy Rankin <rrankin@ihug.com.au> - 2.0.6-1
- Upstream update to 2.0.6

* Sat Feb 13 2016 Roy Rankin <rrankin@ihug.com.au> - 2.0.2-1
- Upstream update to 2.0.2 with evince and gtk3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Roy Rankin <rrankin@ihug.com.au> - 2.0.0-4
- restore tooltips and disable evince

* Tue Nov 17 2015 Roy Rankin <rrankin@ihug.com.au> - 2.0.0-3
- patch readlink bug, and modify font paths

* Sun Nov 15 2015 Roy Rankin <rrankin@ihug.com.au> - 2.0.0-2
- Upstream update to 2.0.0
  create /usr/share/denemo/fonts directory to denemo dose not complain
  patchout all use of tooltip

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.1.6-3
- Add metainfo file to show this font in gnome-software

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Roy Rankin <rrankin@ihug.com.au> - 1.1.6-1
- Fix /usr/bin ownership issue

* Tue Jul 01 2014 Roy Rankin <rrankin@ihug.com.au> - 1.1.6-0
- Update for upstream release. 

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Roy Rankin <rrankin@ihug.com.au> - 1.0.0-0
  - run autoconf for arm, cleanup configure options
    Update for upstream release. For new features see
    https://savannah.gnu.org/forum/forum.php?forum_id=7540

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 0.9.4-2
- Rebuilt for gtksourceview3 soname bump

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Roy Rankin <rrankin@ihug.com.au> - 0.9.4-0
 - Update for upstream release. For new features see
   http://savannah.gnu.org/forum/forum.php?forum_id=7281

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 06 2011 Roy Rankin <rrankin@ihug.com.au> - 0.9.2-1
 - Patch for glib include restriction

* Tue Oct 25 2011 Roy Rankin <rrankin@ihug.com.au> - 0.9.2-0
 - Update for upstream release. For new features see
   http://savannah.gnu.org/forum/forum.php?forum_id=6962
 - Additional font sub-packages created.

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9.0-0.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 0.9.0-0.1
- rebuild with new gmp

* Sat May 07 2011 Roy Rankin <rrankin@ihug.com.au> - 0.9.0-0
 - Update for upstream release. For new features see
   http://savannah.gnu.org/forum/forum.php?forum_id=6804

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 06 2010 Roy Rankin <rrankin@ihug.com.au> - 0.8.20-1
-Update for Denemo release 0.8.20  For new features see
  http://savannah.gnu.org/forum/forum.php?forum_id=6558

* Mon Jul 12 2010 Roy Rankin <rrankin@ihug.com.au> - 0.8.18-2
- Require lilypond, patch bug if lilypond not found

* Sun Jul 11 2010 Roy Rankin <rrankin@ihug.com.au> - 0.8.18-1
-License change GPLV2 to GPLV3+
-Update for Denemo release 0.8.18  For now features see
  http://savannah.gnu.org/forum/forum.php?forum_id=6422

* Sun May 23 2010 Roy Rankin <rrankin@ihug.com.au> - 0.8.16-1
-Update for Denemo release 0.8.16  For now features see
  http://www.denemo.org/index.php/Denemo_0.8.16_Release! 

* Sat Feb 06 2010 Roy Rankin <rrankin@ihug.com.au> - 0.8.12-1
-Update for Denemo release 0.8.12  For now features see
  http://www.denemo.org/index.php/Denemo_0.8.12_Release! 

* Mon Oct 12 2009 Roy Rankin <rrankin@ihug.com.au> - 0.8.8-1
-Update for Denemo release 0.8.8 

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8.4-3
- Update desktop file according to F-12 FedoraStudio feature

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 30 2009 Roy Rankin <rrankin@ihug.com.au> - 0.8.4-1
-Update for Denemo release 0.8.4 
  fix fedora bugzilla 499692
  new features
	custom prolog
	tagged directives
	print preview pane
	genereal edit object action
	background printing

* Fri Feb 27 2009 Roy Rankin <rrankin@ihug.com.au> - 0.8.2-3
- font subpackage needs same version as main package, use noarch
 
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Roy Rankin <rrankin@ihug.com.au> - 0.8.2-1
-Update for Denemo release 0.8.2
	improve MIDI input
	more scripting support
	better menu organization
-Spec file fix unowned directories (Bugzilla 483337)

* Sat Jan 10 2009 Roy Rankin <rrankin@ihug.com.au> - 0.8.0-2
-Font split into seperate RPM package (Bugzilla 477375)

* Sun Nov 30 2008 Roy Rankin <rrankin@ihug.com.au> - 0.8.0-1
-Update for Denemo release 0.8.0

* Wed Sep 03 2008 Roy Rankin <rrankin@ihug.com.au> - 0.7.9-5
-Add Patches assert undo crash, un-needed messages on start up
* Mon Aug 18 2008 Roy Rankin <rrankin@ihug.com.au> 0.7.9-4
-Simplify Requires
* Sat Aug 16 2008 Roy Rankin <rrankin@ihug.com.au> 0.7.9-3
-Remove defines and fixup BuildRoot path
* Sun Aug  3 2008 Roy Rankin <rrankin@ihug.com.au> 0.7.9-2
-Additional BuildRequires from Mock testing, 
 fixed desktop-file-install usage
* Fri Jul 25 2008 Roy Rankin <rrankin@ihug.com.au> 0.7.9-1
-Update for 0.7.9 and Fedora 8
* Fri Dec 14 2001 Adam Tee <ajtee@ajtee.uklinux.net>
-Update for 0.5.8
* Sun Nov 12 2000 Matt Hiller <mhiller@pacbell.net>
- Update for 0.5.5
* Wed Jun 21 2000 Sourav K. Mandal <smandal@mit.edu>
- Initial release of RPM package
