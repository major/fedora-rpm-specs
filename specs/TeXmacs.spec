Name:           TeXmacs
Version:        2.1.2
Release:        10%{?dist}
Summary:        Structured WYSIWYG scientific text editor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.texmacs.org
Source:         http://www.texmacs.org/Download/ftp/tmftp/source/TeXmacs-%{version}-src.tar.gz
# Make plugins/mathematica/bin/realpath.py Python 3 compatible
Patch0:         https://github.com/texmacs/texmacs/pull/73.patch
Requires:       ghostscript
Requires:       texmacs-fedora-fonts = %{version}-%{release}
BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  compat-guile18-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl-generators
BuildRequires:  freetype-devel
BuildRequires:  libICE-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
BuildRequires:  qt5-qtsvg-devel
# For pathfix
BuildRequires:  python3-devel
Provides:       texmacs = %{version}-%{release}
Requires:       fig2ps

%description
GNU TeXmacs is a free scientific text editor, which was both inspired
by TeX and GNU Emacs. The editor allows you to write structured
documents via a WYSIWYG (what-you-see-is-what-you-get) and user
friendly interface.  New styles may be created by the user. The
program implements high-quality typesetting algorithms and TeX fonts,
which help you to produce professionally looking documents.

The high typesetting quality still goes through for automatically
generated formulas, which makes TeXmacs suitable as an interface for
computer algebra systems. TeXmacs also supports the Guile/Scheme
extension language, so that you may customize the interface and write
your own extensions to the editor.

In the future, TeXmacs is planned to evolve towards a complete
scientific office suite, with spreadsheet capacities, a technical
drawing editor and a presentation mode.


%package devel
Summary:        Development files for TeXmacs
Requires:       %{name} = %{version}-%{release}

%description devel
Development files required to create TeXmacs plugins.

%package -n texmacs-fedora-fonts
Summary:        Fonts for TeXmacs
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%description -n texmacs-fedora-fonts
TeXmacs font.

%prep
%autosetup -p1 -n TeXmacs-%{version}-src
%{py3_shebang_fix} plugins/mathematica/bin/realpath.py

%build
%cmake
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/texmacs.desktop

rm -f %{buildroot}%{_bindir}/fig2ps
rm -f %{buildroot}%{_mandir}/man*/fig2ps*

# link installed fonts with Fedora
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_datadir}/TeXmacs/fonts/type1/ec/
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/ec/$i
done
cd ../la
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/la/$i
done
cd ../math
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/math/$i
done
popd
rm -f %{buildroot}%{_datadir}/icons/gnome/icon-theme.cache
find %{buildroot}%{_datadir}/mime/ -type f -maxdepth 1 -print | xargs rm -f


%if ( 0%{?rhel} && 0%{?rhel} <= 7 )
%post
/usr/bin/update-desktop-database /usr/share/applications > /dev/null 2>&1 || :
/bin/touch --no-create %{_datadir}/mime/packages &> /dev/null || :
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%postun
/usr/bin/update-desktop-database /usr/share/applications > /dev/null 2>&1 || :
if [ $1 -eq 0 ]; then
    /bin/touch --no-create %{_datadir}/mime/packages &> /dev/null || :
    /usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif


%files
%license LICENSE
%doc COPYING TeXmacs/README TeXmacs/TEX_FONTS
%{_bindir}/*
%{_mandir}/man*/*
%{_prefix}/lib/*
%{_datadir}/TeXmacs
%exclude %{_datadir}/TeXmacs/examples/plugins
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/128x128/apps/TeXmacs.png
%{_datadir}/icons/hicolor/16x16/apps/TeXmacs.png
%{_datadir}/icons/hicolor/22x22/apps/TeXmacs.png
%{_datadir}/icons/hicolor/24x24/apps/TeXmacs.png
%{_datadir}/icons/hicolor/256x256/apps/TeXmacs.png
%{_datadir}/icons/hicolor/32x32/apps/TeXmacs.png
%{_datadir}/icons/hicolor/48x48/apps/TeXmacs.png
%{_datadir}/icons/hicolor/512x512/apps/TeXmacs.png
%{_datadir}/icons/hicolor/64x64/apps/TeXmacs.png
%{_datadir}/icons/hicolor/scalable/apps/TeXmacs.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/text-x-texmacs.svg

%files devel
%{_includedir}/*
%{_datadir}/TeXmacs/examples/plugins

%_font_pkg -n fedora *


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 14 2024 Orion Poplawski <orion@nwra.com> - 2.1.2-9
- Add patch for Python 3 compatibility (rhbz#2244835)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.2-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Jindrich Novy <jnovy@redhat.com> - 2.1.2-2
- Update to 2.1.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 16 2021 Orion Poplawski <orion@nwra.com> - 2.1-1
- Update to 2.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Orion Poplawski <orion@nwra.com> - 1.99.13-5
- Add patch for Qt 5.15 support

* Wed Sep 23 2020 Orion Poplawski <orion@nwra.com> - 1.99.13-4
- Use new cmake macros (FTBFS bz#1863124)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.13-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jindrich Novy <jnovy@redhat.com> - 1.99.13-1
- update to 1.99.13

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Orion Poplawski <orion@nwra.com> - 1.99.12-1
- Update to 1.99.12

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1.99.8-3
- Append curdir to CMake invokation. (#1668512)

* Sun Oct 21 2018 Orion Poplawski <orion@nwra.com> - 1.99.8-2
- Revert to Guile 1.8

* Tue Oct 09 2018 Orion Poplawski <orion@nwra.com> - 1.99.8-1
- Update to 1.99.8
- Use cmake
- Build with Guile 2.0 and Qt 5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 02 2016 Orion Poplawski <orion@cora.nwra.com> - 1.99.2-9
- Add patch to fix rpm builds
- Add gtk-update-icon-cache snippets
- Drop update-mime-database snippets on Fedora 24+
- Drop update-desktop-database snippets on Fedora 25+
- Use %%license

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.99.2-7
- Rebuild for poppler-0.40.0

* Mon Aug 10 2015 Orion Poplawski <orion@cora.nwra.com> - 1.99.2-6
- Update conffix patch to fix overwriting of CXXFLAGS.  Fixes FTBFS bug #1239354

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.99.2-4
- Fix qreal-to-double casting error (#1105932)

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 1.99.2-3
- update mime scriptlets

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Jindrich Novy <novyjindrich@gmail.com> - 1.99.2-1
- update to 1.99.2

* Thu Jul 31 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.99.1-2
- Add missing -lz to link (#1105932)

* Tue Jun 24 2014 Jindrich Novy <novyjindrich@gmail.com> - 1.99.1-1
- update to 1.99.1 (#928733)
- fix configure script to detect/compile against Guile-1.8
- compiling against Guile-1.8 fixes crashes on startup (#957417, #1028754)
- add HAS_GS_EXE option (#1105932) - thanks to Yaakov Selkowitz

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 24 2013 Jindrich Novy <novyjindrich@gmail.com> - 1.0.7.21-1
- update to 1.0.7.21

* Tue Oct 15 2013 Jindrich Novy <novyjindrich@gmail.com> - 1.0.7.20-1
- update to 1.0.7.20

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.7.19-3
- Perl 5.18 rebuild

* Tue Jun 11 2013 Jindrich Novy <novyjindrich@gmail.com> - 1.0.7.19-2
- don't own files owned by shared-mime-info (#973089)

* Sun Apr 28 2013 Jindrich Novy <jnovy@redhat.com> - 1.0.7.19-1
- update to 1.0.7.19

* Mon Feb 18 2013 Jindrich Novy <jnovy@redhat.com> - 1.0.7.18-1
- update to 1.0.7.18 (#895930)

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.0.7.16-3
- Remove vendor tag from desktop file
- spec clean up

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Jindrich Novy <jnovy@redhat.com> - 1.0.7.16-1
- update to 1.0.7.16 (#895930)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 29 2011 Jindrich Novy <jnovy@redhat.com> - 1.0.7.11-1
- update to 1.0.7.11 (#733837)

* Mon Mar  7 2011 Jindrich Novy <jnovy@redhat.com> - 1.0.7.10-1
- update to 1.0.7.10

* Wed Feb 16 2011 Jindrich Novy <jnovy@redhat.com> - 1.0.7.9-3
- first attempt to package fonts according to fedora font
  packaging guidelines (#477464)

* Fri Feb 11 2011 Jindrich Novy <jnovy@redhat.com> - 1.0.7.9-2
- fix CVE-2010-3394 (#638428)

* Thu Feb 10 2011 Jindrich Novy <jnovy@redhat.com> - 1.0.7.9-1
- update to 1.0.7.9 (#593625)
- fix Requires
- fix build -> broken util.h usage
- fix desktop categories
- remove BuildRoot

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Gerard Milmeister <gemi@bluewin.ch> - 1.0.7.2-1
- new release 1.0.7.2

* Fri Jan  2 2009 Gerard Milmeister <gemi@bluewin.ch> - 1.0.7.1-1
- new release 1.0.7.1

* Sun Oct 19 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.7-1
- new release 1.0.7

* Sat Aug 16 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.15-1
- new release 1.0.6.15

* Tue Jul 22 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.14-2
- fix for Maxima 5.15

* Thu Mar 20 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.14-1
- new release 1.0.6.14

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.6.12-3
- Autorebuild for GCC 4.3

* Mon Nov  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.12-1
- new release 1.0.6.12
- split off devel package

* Mon Oct  8 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.11-2
- patch for maxima 5.13.0

* Mon Sep 10 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.11-1
- new release 1.0.6.11

* Fri Jun 29 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.10-3
- ps generation fix

* Mon May 14 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.10-1
- new version 1.0.6.10

* Mon Feb 12 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.9-1
- new version 1.0.6.9

* Sun Feb 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.8-2
- build with optflags (bugzilla 228152)

* Fri Jan 19 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.8-1
- new version 1.0.6.8

* Tue Dec 12 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.7-1
- new version 1.0.6.7

* Mon Aug 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.6-1
- new version 1.0.6.6

* Mon Aug  7 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.5-1
- new version 1.0.6.5

* Mon Jun 19 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.3-1
- new version 1.0.6.3

* Mon May 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.2-1
- new version 1.0.6.2

* Fri May 12 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6.1-1
- new version 1.0.6.1

* Thu May 11 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6-8
- added buildreq for gmp-devel

* Thu May 11 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6-7
- rebuilt for guile-1.8

* Mon Mar 20 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6-6
- fix problems with gcc41 (TeXmacs-gcc41.patch)

* Sat Feb 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6-4
- Temporary fix for compiling problem (TeXmacs-event.patch)

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6-3
- Rebuild for Fedora Extras 5

* Sat Dec 31 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.6-1
- New Version 1.0.6

* Mon Nov  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.12-1
- New Version 1.0.5.12

* Fri Nov  4 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.11-3
- remove fig2ps and require it

* Tue Nov  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.11-2
- replace XFree86-devel by xorg-x11-devel

* Tue Nov  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.11-1
- New Version 1.0.5.11

* Tue Oct 11 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.10-2
- Patch for tm_maxima to recognize maxima 5.9.1.9 versions

* Mon Oct 10 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.10-1
- New Version 1.0.5.10

* Wed Sep 28 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.9
- New Version 1.0.5.9

* Tue Sep 20 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.8
- New Version 1.0.5.8

* Mon Aug 22 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.7
- New Version 1.0.5.7

* Mon Jul 25 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.6
- New Version 1.0.5.6

* Tue Jul  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.5
- New Version 1.0.5.5

* Tue Jun 21 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.4
- New Version 1.0.5.4

* Wed Jun 15 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5.3
- New Version 1.0.5.3

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0.5-3
- rebuild on all arches

* Thu Apr 28 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.5-1
- New Version 1.0.5

* Mon Apr  4 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.0.4.7-1
- New Version 1.0.4.7

* Mon Feb 21 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.4.6-1
- New Version 1.0.4.6

* Mon Dec  6 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.4.5-0.fdr.1
- New Version 1.0.4.5

* Mon Nov 15 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.4.4-0.fdr.1
- New Version 1.0.4.4
- Added support for new mime system

* Sun Oct 24 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.4.3-0.fdr.1
- New Version 1.0.4.3

* Tue Aug 31 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.4.2-0.fdr.1
- New Version 1.0.4.2

* Mon Aug  9 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.4.1-0.fdr.1
- New Version 1.0.4.1

* Sat Jul 17 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.3.11-0.fdr.1
- New Version 1.0.3.11

* Sun May 23 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.3.9-0.fdr.1
- New Version 1.0.3.9

* Sun Apr  4 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.3.6-0.fdr.1
- New Version 1.0.3.6

* Mon Dec  1 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.2.9-0.fdr.1
- New Version 1.0.2.9

* Fri Nov 14 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.2.7-0.fdr.1
- New Version 1.0.2.7

* Wed Nov  5 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.0.2.6-0.fdr.1
- First Fedora release
