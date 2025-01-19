## lyx-fonts
%global fontname lyx
BuildRequires: fontpackages-devel

%global _without_included_boost --without-included-boost

# Do we need to rebuild configuration files?
%global autotools 0

# Trim changelog to a reasonable size
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    lyx
Version: 2.4.2.1
Release: 2%{?dist}
Summary: WYSIWYM (What You See Is What You Mean) document processor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url:     https://www.lyx.org/
Source0: http://ftp.lyx.org/pub/lyx/stable/2.4.x/lyx-%{version}.tar.xz

Source1: lyxrc.dist

# font metainfo file
Source20: %{fontname}.metainfo.xml

%if 0%{?autotools}
BuildRequires: automake libtool
%endif
# weird but necessary to compare the supported qt version
# see http://comments.gmane.org/gmane.editors.lyx.devel/137498
BuildRequires: bc

%if 0%{?_without_included_boost:1}
BuildRequires: boost-devel
%endif

%if 0%{?fedora}
BuildRequires: libappstream-glib
%endif

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: enchant2-devel
BuildRequires: file-devel
BuildRequires: gettext
BuildRequires: hunspell-devel
BuildRequires: mythes-devel
BuildRequires: python3-devel

%if 0%{?fedora}
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: libxkbcommon-devel
%else
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5X11Extras)
%endif

BuildRequires: texlive-texmf-fonts
BuildRequires: tex(dvips)
BuildRequires: tex(latex)
BuildRequires: zlib-devel

Requires(post): texlive
Requires(postun): texlive
Requires: %{name}-common = %{version}-%{release}
Requires: %{fontname}-fonts = %{version}-%{release}
Requires: hicolor-icon-theme
Requires: python3

Recommends: texlive-collection-latexrecommended

%if 0%{?fedora}
# convert doc files to lyx (bug #193858)
Requires: wv
%endif

# required for file conversions
Requires: ImageMagick
Requires: xdg-utils
Requires: ghostscript
## produce PDF files directly from DVI files
Requires: tex-dvipdfmx
## convert eps to pdf
Requires: tex-epstopdf
## checking the quality of the generated latex
Requires: tex-chktex
## instant preview
Requires: tex-dtl
Requires: tex(cprotect.sty)
# LaTeX packages required to compile the User's Manual
Requires: tex(dvips)
Requires: tex(esint.map)
Requires: tex(esint.sty)
Requires: tex(latex)
Requires: tex(nomencl.sty)
Requires: tex(simplecv.cls)
Requires: tex(ulem.sty)
Requires: tex(xcolor.sty)

%description
LyX is a modern approach to writing documents which breaks with the
obsolete "typewriter paradigm" of most other document preparation
systems.

It is designed for people who want professional quality output
with a minimum of time and effort, without becoming specialists in
typesetting.

The major innovation in LyX is WYSIWYM (What You See Is What You Mean).
That is, the author focuses on content, not on the details of formatting.
This allows for greater productivity, and leaves the final typesetting
to the backends (like LaTeX) that are specifically designed for the task.

With LyX, the author can concentrate on the contents of his writing,
and let the computer take care of the rest.

%package common
Summary:  Common files of %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description common
%{Summary}.

%package fonts
Summary: Lyx/MathML fonts
# The actual license says "The author of these fonts, Basil K. Malyshev, has
# kindly granted permission to use and modify these fonts."
# One of the font files (wasy10) is separately licensed GPL+.
License: LicenseRef-Fedora-UltraPermissive AND GPL-1.0-or-later
Requires: fontpackages-filesystem
Provides:  mathml-fonts = 1.0-50
Provides:  lyx-cmex10-fonts = %{version}-%{release}
Provides:  lyx-cmmi10-fonts = %{version}-%{release}
Provides:  lyx-cmr10-fonts = %{version}-%{release}
Provides:  lyx-cmsy10-fonts = %{version}-%{release}
BuildArch: noarch
%description  fonts
A collection of Math symbol fonts for %{name}.


%prep

%autosetup -p1

# prefer xdg-open over alternatives in configuration
for prog in xv firefox kghostview pdfview xdvi
do
    sed -i -e "s/'$prog'/'xdg-open', '$prog'/" lib/configure.py
done

%if 0%{?autotools}
./autogen.sh
%endif


%build
%configure \
  --disable-dependency-tracking \
  --disable-rpath \
  --disable-silent-rules \
  --enable-build-type=release \
  --enable-optimization="%{optflags}" \
  --without-included-boost \
%if 0%{?fedora}
  --enable-qt6 \
%endif
  --with-enchant \
  --with-hunspell

%make_build


%install
%make_install

%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/lyx2lyx

# misc/extras
install -p -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/%{name}/lyxrc.dist

# Set up the lyx-specific class files where TeX can see them
mkdir -p %{buildroot}%{_texmf}/tex/latex/
mv %{buildroot}%{_datadir}/%{name}/tex \
   %{buildroot}%{_texmf}/tex/latex/%{name}

# icon
install -p -D -m644 lib/images/lyx.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

install -p -D -m644 lib/images/lyx.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# ghost'd files
touch %{buildroot}%{_datadir}/%{name}/lyxrc.defaults
touch %{buildroot}%{_datadir}/%{name}/{packages,textclass}.lst

# fonts
install -m 0755 -d %{buildroot}%{_fontdir}
mv %{buildroot}%{_datadir}/%{name}/fonts/*.ttf %{buildroot}%{_fontdir}/
rm -rf %{buildroot}%{_datadir}/%{name}/fonts

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE20} \
        %{buildroot}%{_metainfodir}/%{fontname}.metainfo.xml

%find_lang %{name}

# bash completion
install -p -D -m 0644 lib/scripts/bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml ||:
# tests/test_filetools error bogus ( see http://bugzilla.redhat.com/723938 )
make -k check ||:


%postun common
if [ $1 -eq 0 ] ; then
  texhash >& /dev/null
fi

%posttrans common
texhash >& /dev/null

%files
%doc ANNOUNCE lib/CREDITS NEWS README
%license COPYING
%{_bindir}/*

%files common -f %{name}.lang
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/%{name}/
%config(noreplace) %{_datadir}/%{name}/lyxrc.dist
%ghost %{_datadir}/%{name}/lyxrc.defaults
%ghost %{_datadir}/%{name}/*.lst
%{_texmf}/tex/latex/%{name}/
%{_metainfodir}/org.%{name}.LyX.metainfo.xml
%{_sysconfdir}/bash_completion.d/%{name}

%_font_pkg
%{_fontdir}/*.ttf
%license lib/fonts/BaKoMaFontLicense.txt
%{_metainfodir}/%{fontname}.metainfo.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 José Matos <jamatos@fedoraproject.org> - 2.4.2.1-1
- Update to 2.4.2.1

* Thu Sep 19 2024 José Matos <jamatos@fedoraproject.org> - 2.4.2-0
- Update to 2.4.2
- remove upstream patch

* Sun Aug 25 2024 José Matos <jamatos@fedoraproject.org> - 2.4.1-4
- Fix code to be compatible with Python 3.13 (upstream patch)

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul  5 2024 José Matos <jamatos@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Thu May 30 2024 José Matos <jamatos@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Sat May 18 2024 José Matos <jamatos@fedoraproject.org> - 2.3.8-1
- Update to 2.3.8

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 23 2023 José Matos <jamatos@fedoraproject.org> - 2.3.7-1
- Update to 2.3.7
- Remove patch that has been applied upstream

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb  4 2022 José Matos <jamatos@fedoraproject.org> - 2.3.6.1-6
- remove long unused provides (more than 10 years old)

* Thu Feb  3 2022 José Matos <jamatos@fedoraproject.org> - 2.3.6.1-5
- fix #1965118

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 2021 José Matos <jamatos@fedoraproject.org> - 2.3.6.1-1
- update to 2.3.6.1
- replace patch to configure.py with sed script
- update the minimal set of latex packages required (rhbz #1827988)

* Sat Nov 28 2020 José Matos <jamatos@fedoraproject.org> - 2.3.6-2
- Apply upstream patch to solve #1773650

* Fri Nov 27 2020 José Matos <jamatos@fedoraproject.org> - 2.3.6-1
- update to 2.3.6

* Thu Jul  2 2020 José Matos <jamatos@fedoraproject.org> - 2.3.5.2-2
- Add patch to show the application icon in Wayland (rhbz#1822478) (lyx#11847)

* Wed Jul  1 2020 José Matos <jamatos@fedoraproject.org> - 2.3.5.2-1
- update to 2.3.5.2

* Wed Jun 24 2020 José Matos <jamatos@fedoraproject.org> - 2.3.5-3
- use py_bytecompile to bytecompile lyx2lyx files

* Tue Jun  2 2020 José Matos <jamatos@fedoraproject.org> - 2.3.5-2
- rebuild with boost 1.73 (for Fedora 33+)

* Tue Jun  2 2020 José Matos <jamatos@fedoraproject.org> - 2.3.5-1
- update to 2.3.5

* Thu Feb 13 2020 José Matos <jamatos@fedoraproject.org> - 2.3.4.2-1
- update to 2.3.4.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 José Matos <jamatos@fedoraproject.org> - 2.3.4-1
- update to 2.3.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 José Matos <jamatos@fedoraproject.org> - 2.3.3-1
- update to 2.3.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2.3.2-2
- Rebuilt for Boost 1.69

* Mon Dec 10 2018 José Matos <jamatos@fedoraproject.org> - 2.3.2-1
- update to 2.3.2
- transition to python3 by default

* Thu Nov 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-4
- workaround/fix cases of: #!/usr/bin/env python (#1649919)
- make qt5 unconditional
- use %%license %%make_build %%make_install, %%metainfodir
- simplify scriptlets (mostly remove, due to nice triggers these days)

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 2.3.1-3
- rebuild for hunspell 1.7.0

* Mon Oct 15 2018 José Matos <jamatos@fedoraproject.org> - 2.3.1-2
- add patch to fix issues with dead key accents (lyxbug 11183).

* Sun Sep 16 2018 José Matos <jamatos@fedoraproject.org> - 2.3.1-1
- update to 2.3.1
- remove patch because it is already incorporated in current version

* Sun Jul 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.3.0-4
- backport upstream FTBFS fix (#1604768)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Feb 25 2018 José Matos <jamatos@fedoraproject.org> - 2.3.0-0
- Rebuild for 2.3.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2.2.3-6
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 2.2.3-3
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.2.3-2
- Rebuilt for Boost 1.64

* Sun May  7 2017 José Matos <jamatos@fedoraproject.org> - 2.2.3-1
- update to 2.2.3
- require mythes-devel

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.2.2-3
- Rebuilt for Boost 1.63

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.2.2-2
- Rebuild for hunspell 1.5.x

* Fri Nov  4 2016 José Matos <jamatos@fedoraproject.org> - 2.2.2-1
- update to 2.2.2

* Fri Jul 22 2016 José Matos <jamatos@fedoraproject.org> - 2.2.1-1
- update to 2.2.1

* Fri May 27 2016 José Matos <jamatos@fedoraproject.org> - 2.2.0-1
- update to final 2.2.0

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 2.1.4-9
- Rebuilt for linker errors in boost (#1331983)

* Mon Apr 18 2016 Caolán McNamara <caolanm@redhat.com> - 2.1.4-8
- rebuild for hunspell 1.4.0

* Wed Apr 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.1.4-7
- use upstream .desktop file (#1326636)
- drop runtime/versioned qt dep

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.1.4-5
- Rebuilt for Boost 1.60

* Sat Sep 12 2015 José Matos <jamatos@fedoraproject.org> - 2.1.4-4
- Upstream respun sources (no changes for linux)
- Apply patch to fix #1260976 and #1262038

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.1.4-3
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Fri Jul 24 2015 José Matos <jamatos@jamatos> - 2.1.4-1
- Update to 2.1.4
- Remove upstreamed patches
- Update xdg-open patch (we really need a better solution :-( )

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.1.3-7
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.3-5
- Recommends: texlive-collection-latexrecommended (f21+, #1058062)

* Wed May 20 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-4
- epel7 fixes
- don't own %%_datadir/appdata
- %%check: validate appdata

* Mon May 18 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.3-3
- backport gcc5 fix (#1209353)

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 2.1.3-2
- Use better AppData screenshots

* Thu Feb 12 2015 José Matos <jamatos@fedoraproject.org> - 2.1.3-1
- update to 2.1.3

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.1.2.2-2
- Rebuild for boost 1.57.0

* Sun Dec 07 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.2.2-1
- 2.1.2.2 (#1159499)

* Wed Nov 19 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.1.2-2
- Add metainfo file to show this font in gnome-software

* Fri Sep 26 2014 José Matos <jamatos@fedoraproject.org> - 2.1.2-1
- update to 2.1.2

* Wed Sep 24 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-4
- don't own /etc/bash_completion.d/

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Rex Dieter <rdieter@fedoraproject.org> - 2.1.1-2
- cleanup/sort deps
- make some runtime deps fedora only (currently missing on epel7)
- .spec cleanup
- --disable-silent-rules

* Fri Jul  4 2014 José Matos <jamatos@fedoraproject.org> - 2.1.1-1
- update to 2.1.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 2.1.0-3
- Rebuild for boost 1.55.0

* Thu May  1 2014 José Matos <jamatos@fedoraproject.org> - 2.1.0-2
- update to latest from the stable series picking several important
  fixes in the process (current 2.1.x source)

* Thu Apr 17 2014 José Matos <jamatos@fedoraproject.org> - 2.1.0-1
- 2.1.0 is a stable release so set release number to 1

* Tue Apr 15 2014 José Matos <jamatos@fedoraproject.org> - 2.1.0-0
- update to 2.1.0
- install appdata.xml file and become a co-owner of that directory
- add support for epel 7
- add hicolor-icon-theme as a dependency

* Wed Feb  5 2014 José Matos <jamatos@fedoraproject.org> - 2.0.7-3
- add dependencies for change tracking, a core feature of lyx (bug #907163)
- install svg icon to have a more scalable icon (bug #1018425)

* Sat Jan 25 2014 José Matos <jamatos@fedoraproject.org> - 2.0.7-2
- new sources for release (the changes do not apply to linux)
- add chktex as requirement to fix [bug 1051933]

* Sat Dec 21 2013 José Matos <jamatos@fedoraproject.org> - 2.0.7-1
- update to 2.0.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 2.0.6-2
- Rebuild for boost 1.54.0

* Sat May  4 2013 José Matos <jamatos@fedoraproject.org> - 2.0.6-1
- update to 2.0.6
- update xdg-open patch

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2.0.5.1-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2.0.5.1-2
- Rebuild for Boost-1.53.0

* Fri Jan  4 2013 José Matos <jamatos@fedoraproject.org> - 2.0.5.1-1
- New stable micro release (Fix: babel not loaded for English documents)

* Mon Nov 26 2012 José Matos <jamatos@fedoraproject.org> - 2.0.5-3
- Install bash completion (#802149)

* Sun Nov 25 2012 José Matos <jamatos@fedoraproject.org> - 2.0.5-2
- New texlive packaging for Fedora 18+

* Sun Nov 25 2012 José Matos <jamatos@fedoraproject.org> - 2.0.5-1
- New bugfix release

* Thu Aug 09 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-3
- rebuild (boost)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-1
- lyx-2.0.4
- Omitted backslash in code for floatingfootnote, after export to latex, and re-import (#811719)

* Mon Mar  5 2012 José Matos <jamatos@fedoraproject.org> - 2.0.3-1
- New bugfix release

* Wed Feb 29 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-4
- hack around gcc-4.7 ftbfs for now

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for c++ ABI breakage

* Sat Jan  7 2012 José Matos <jamatos@fedoraproject.org> - 2.0.2-2
- Require ImageMagick (#753626)

* Thu Dec  1 2011 José Matos <jamatos@fedoraproject.org> - 2.0.2-1
- New stable release.

* Tue Nov 22 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-3
- rebuild (boost)

* Mon Sep  5 2011 José Matos <jamatos@fedoraproject.org> - 2.0.1-2
- Update xdg_open patch for version 2.0.1

* Mon Sep  5 2011 José Matos <jamatos@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-5
- rebuild (boost)

* Wed Jun  1 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-4
- LaTeXConfig.lyx is no longer a ghost (#684428)

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-3
- fix hunspell support (use pkgconfig)

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-2
- rebuild (hunspell)

* Fri Apr 29 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0 final

* Mon Apr 11 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.21.rc3
- Update to rc3

* Thu Apr  7 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.20.rc2
- Rebuild for new boost (just applies to F16)

* Tue Mar 29 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.19.rc2
- New upstream release (rc2)

* Mon Mar 14 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.18.rc1
- Rebuild for boost upgrade

* Sat Mar 12 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.17.rc1
- Add thesaurus and hunspell paths to lyxrc.dist thus fixing
  http://www.lyx.org/trac/ticket/7253
- Simplified the content of lyxrc.dist leaving only the relevant
  options and updating the format to the current one

* Fri Mar 11 2011 José Matos <jamatos@fedoraproject.org> - 2.0.0-0.16.rc1
- Update for rc1 and add a dependency to ensure that math instant
  preview works by default
- Removed patch applied upstream for gcc 4.6 fixes
- Renamed patch for xdg_open to be in sync with current version (rc1)

* Fri Feb 11 2011 Orion Poplawski <orion@cora.nwra.com> 2.0.0-0.15.beta4
- Get gcc46 fixes from svn

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.14.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-0.13.beta4
- 2.0.0-beta4

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> 2.0.0-0.12.beta3
- rebuild for new boost

* Tue Jan 11 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-0.11.beta3
- lyx-2.0.0-beta3

* Wed Dec 08 2010 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-0.10.beta2
- lyx-2.0.0-beta2

* Wed Nov 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.9.beta1
- lyx-2.0.0-beta1 (#651488)

* Tue Nov 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.8.alpha6
- lyx-2.0.0-alpha6 (#651488)

* Wed Nov 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.7.alpha5
- drop %%triggers, *may* affect selinux labels (#632944)

* Thu Aug 05 2010 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-0.6.alpha5
- Rebuild for newer boost

* Wed Jul 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.5.alpha5
- lyx-2.0.0-alpha5

* Thu Jun 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.4.alpha4
- lyx-2.0.0-alpha4

* Thu May 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.3.alpha3
- lyx-2.0.0-alpha3

* Sat Apr 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.2.alpha2
- lyx-2.0.0-alpha2

* Sat Apr 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-0.1.alpha1
- lyx-2.0.0-alpha1

* Sun Feb 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.5-5
- FTBFS lyx-1.6.5-4.fc13: ImplicitDSOLinking (#565009)

* Thu Jan 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.5-4
- -fonts: Provides: lyx-{cmex10,cmmi10,cmr10,cmsy10}-fonts

* Sat Jan 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.5-3
- rebiuld (boost)
- use simple font template

* Wed Dec  9 2009 José Matos <jamatos@fc.up.pt> - 1.6.5-2
- Add patch for autoconf 2.65 (F13+)

* Wed Dec  9 2009 José Matos <jamatos@fc.up.pt> - 1.6.5-1
- lyx-1.6.5

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 1.6.4-3
- LyX supports autoconf 2.64 (should be upstream for 1.6.5)

* Thu Sep 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.4-2
- use enchant instead of aspell (#524046)

* Sat Aug 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.4-1
- lyx-1.6.4
- handle fonts manually (now EPEL-5 compatible)

* Mon Aug 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.3-3
- add lyx-*-fonts subpkgs (#452357, #514549)
- -common (noarch) subpkg
- trim %%changelog

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.3-1
- lyx-1.6.3

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.2-2
- scriptlet optimization

* Sun Mar 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.2-1
- lyx-1.6.2
- use --without-included-boost unconditionally

* Wed Mar 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-3
- --without-included-boost (f11+)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-1
- lyx-1.6.1

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.0-2
- Rebuild for Python 2.6

* Fri Nov 07 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-1
- lyx-1.6.0(final)

* Tue Oct 28 2008 José Matos <jamatos@fc.up.pt> - 1.6.0-0.11.rc5
- lyx-1.6.0rc5

* Fri Oct 24 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.10.rc4
- lyx-1.6.0rc4

* Tue Sep 30 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.9.rc3
- lyx-1.6.0rc3

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.8.rc3
- lyx-1.6.0rc3-svn26576

* Fri Sep 12 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.7.rc2
- lyx-1.6.0rc2

* Wed Aug 06 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.6.rc1
- lyx-1.6.0rc1

* Sun Aug 03 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-0.5.beta4
- Requires: dvipdfm (f9+, #448647)
- add (optional) minimal qt4 dep
- make Req: tex-simplecv fedora only
- drop file deps (texhash)

* Wed Jul 16 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.0-0.4.beta4
- Changelog has been removed from the distribution

* Wed Jul 16 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.0-0.3.beta4
- icon has changed from xpm to png

* Wed Jul 16 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.0-0.2.beta4
- revert to use pre instead of devrel.
- require tex-simplecv (#428526)

* Wed Jul 16 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.0-0.1.beta4
- lyx-1.6.0beta4
- --enable-build-type=release disables extra debug information (no
    warnings, debug, assertions, concept-checks and stdlib-debug).

* Mon May 12 2008 Rex Dieter <rdieter@fedoraproject.org> 1.5.5-1
- lyx-1.5.5

* Mon Feb 25 2008 Rex Dieter <rdieter@fedoraproject.org> 1.5.4-1
- lyx-1.5.4 (#434689)
- reintroduce xdg-utils patch (reverted upstream).
- omit bakoma ttf fonts

* Mon Feb 11 2008 José Matos <jamatos[AT]fc.up.pt> - 1.5.3-2
- Rebuild for gcc 4.3

* Mon Dec 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.3-1
- lyx-1.5.3

* Tue Dec 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.2-2
- drop scriptlet optimization hack

* Mon Oct 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.2-1
- lyx-1.5.2

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.1-2
- respin (BuildID)

* Thu Aug 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.1-1
- lyx-1.5.1
- License: GPLv2+

* Wed Jul 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-1
- lyx-1.5.0(final)

* Sun Jul 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.10.rc2
- upstream patch for 'lyx --export latex' crasher (#248282)

* Thu Jun 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.9.rc2
- scriptlet optmization

* Thu Jun 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.8.rc2
- lyx-1.5.0rc2

* Fri Jun 01 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.7.rc1
- lyx-1.5.0rc1

* Fri May 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.6.beta3
- lyx-1.5.0beta3

* Sun Apr 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.5.beta2
- lyx-1.5.0beta2

* Mon Apr 02 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.4.beta1
- fix qt-4.3 crasher

* Tue Mar 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.3.beta1
- stop omitting -fexceptions

* Wed Mar 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.2.beta1
- +Requires: tetex-IEEEtran (#232840)

* Mon Mar 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.5.0-0.1.beta1
- lyx-1.5.0beta1
- tweak lyxrc.dist

* Thu Feb 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.4.4-2
- biffed sources, respin

* Wed Feb 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.4.4-1
- lyx-1.4.4
- .desktop's: -Category=Application
- mark -xforms as deprecated

* Sun Oct 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.3-3
- sync .desktop files with upstream
- use xdg-open as default helper, +Requires: xdg-utils

* Thu Sep 21 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.3-1
- lyx-1.4.3

* Thu Sep 07 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.2-5
- fc6 respin

* Thu Aug 17 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.2-4
- owowned files, incomplete package removal (bug #201197)

* Thu Jul 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.2-2
- 1.4.2

* Wed Jun 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-9
- Requires(hint): wv (bug #193858)
- fix dependancy -> dependency

* Thu Jun 15 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-8
- BR: gettext
- fc4: restore Requires(hint): tetex-preview

* Thu May 25 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-7.1
- fc4: drop Requires: tetex-preview, it's not ready yet.

* Wed May 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-7
- use serverpipe "~/.lyx/lyxpipe" instead, that was the old default
  and what pybibliographer expects.

* Tue May 23 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-6
- set defaults for (see %%{_datadir}/lyx/lyxrc.defaults.custom)
  screen_font_roman "Serif"
  screen_font_sans "Sans"
  screen_font_typewriter "Monospace"
  screen_zoom 100
  serverpipe "~/.lyx/pipe"
  (bug #192253)

* Mon May 22 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-5
- Requires(hint): tetex-preview

* Tue May 16 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-4
- add generic app icon (rh #191944)

* Fri Apr 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-3
- Requires(hint): tetex-dvipost
  adds support for lyx's Document->Change Tracking

* Tue Apr 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.1-2
- 1.4.1

* Thu Mar 30 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.0-5
- %%trigger ImageMagick (#186319)

* Thu Mar 09 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.0-4
- fix stripping of -fexceptions from %%optflags

* Wed Mar 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.0-3
- include beamer.layout

* Wed Mar 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.4.0-2
- 1.4.0(final)
- drop boost bits
