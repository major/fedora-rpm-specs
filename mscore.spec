%global upname MuseScore
%global shortver 3.6

Name:          mscore
Summary:       Music Composition & Notation Software
Version:       %{shortver}.2
Release:       10%{?dist}
# The MuseScore project itself is GPLv2.  Other licenses in play:
# - rtf2html is LGPLv2+
# - paper4.png and paper5.png are LGPLv3
# - Soundfont is MIT
License:       GPLv2 and LGPLv2+ and LGPLv3 and MIT
URL:           https://musescore.org/

%global foundry         %{name}
%global fontorg         org.musescore
%global fontdocs        fonts/README.md

%global fontfamily1     MScore
%global fontsummary1    MuseScore base music font
%global fontlicense1    GPLv3+ with exceptions
%global fonts1          fonts/mscore/mscore.ttf
%global fontconfs1      %{SOURCE11}
%global fontdescription1 %{expand:
This package contains the base MuseScore music font.  It is derived from
the Emmentaler font created for Lilypond, but has been modified for
MuseScore.}

%global fontfamily2     MScoreText
%global fontsummary2    MuseScore base text font
%global fontlicense2    OFL
%global fonts2          fonts/mscore/MScoreText.ttf
%global fontconfs2      %{SOURCE12}
%global fontdescription2 %{expand:
This package contains the base MuseScore text font.}

%global fontfamily3     Gootville
%global fontsummary3    Derivative of the Gonville font
%global fontlicense3    OFL
%global fonts3          fonts/gootville/*.otf
%global fontdocs3       fonts/gootville/readme.txt
%global fontconfs3      %{SOURCE13}
%global fontdescription3 %{expand:
Gootville is a derivative of the Gonville font created by Simon Tatham
for Lilypond.  The two fonts have common graphic aspects, but the
registration, glyph order, and other aspects of Gootville have been
modified for MuseScore.}

%global fontfamily4     MScore-BC
%global fontsummary4    Font with Basso Continuo digits and symbols
%global fontlicense4    OFL
%global fonts4          fonts/mscore-BC.ttf
%global fontconfs4      %{SOURCE14}
%global fontdescription4 %{expand:
This package contains a MuseScore font with Basso Continuo digits and
symbols, matching glyphs in the main MuseScore font.}

%global fontfamily5     MScoreTab
%global fontsummary5    Font with Renaissance-style tablatures
%global fontlicense5    OFL
%global fonts5          fonts/mscoreTab.ttf
%global fontconfs5      %{SOURCE15}
%global fontdescription5 %{expand:
This package contains a MuseScore font with Renaissance-style tablatures.}

%global fontfamily6     MuseJazz
%global fontsummary6    Handwritten font for text, chord names, and so forth
%global fontlicense6    OFL
%global fontlicenses6   fonts/musejazz/OFL.txt
%global fonts6          fonts/musejazz/*.otf
%global fontconfs6      %{SOURCE16}
%global fontdescription6 %{expand:
This package contains a MuseScore font with a handwritten look for text,
chord names, etc.}

%global fontfamily7     Edwin
%global fontsummary7    Font derived from URW for use with MuseScore
%global fontlicense7    OFL
%global fontlicenses7   fonts/edwin/COPYING.txt fonts/edwin/GPL_LICENSE.txt fonts/edwin/LICENSE.md
%global fontdocs7       fonts/edwin/README.md fonts/edwin/FONTLOG.txt
%global fonts7          fonts/edwin/*.otf
%global fontconfs7      %{SOURCE17}
%global fontdescription7 %{expand:
This package contains a MuseScore font derived from URW C059.}

%global fontfamily8     Leland
%global fontsummary8    Music font for use with MuseScore
%global fontlicense8    OFL
%global fontlicenses8   fonts/leland/LICENSE.txt
%global fontdocs8       fonts/leland/README.md fonts/leland/FONTLOG.txt
%global fonts8          fonts/leland/*.otf
%global fontconfs8      %{SOURCE18}
%global fontdescription8 %{expand:
This package contains a MuseScore music font.}

Source0:       https://github.com/musescore/%{upname}/archive/v%{version}/%{upname}-%{version}.tar.gz
Source1:       https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/VERSION
Source2:       https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General.sf3
Source3:       https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_License.md
Source4:       https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_Changelog.md
Source5:       https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_Readme.md
# For mime types
Source6:       %{name}.xml
# Fontconfig files
Source11:      65-%{fontpkgname1}.conf
Source12:      65-%{fontpkgname2}.conf
Source13:      65-%{fontpkgname3}.conf
Source14:      65-%{fontpkgname4}.conf
Source15:      65-%{fontpkgname5}.conf
Source16:      65-%{fontpkgname6}.conf
Source17:      65-%{fontpkgname7}.conf
Source18:      65-%{fontpkgname8}.conf
# We don't build the common files (font files, wallpapers, demo song, instrument
# list) into the binary executable to reduce its size. This is also useful to
# inform the users about the existence of different choices for common files.
# The font files need to be separated due to the font packaging guidelines.
Patch0:        %{name}-3.6.0-separate-commonfiles.patch
# Ensure CMake will use qmake-qt5
Patch1:        %{name}-3.6.0-fix-qmake-path.patch
# Unbundle gnu-free-{sans,serif}-fonts, kqoauth, marcsabatella-campania-fonts,
# QtSingleApplication, steinberg-bravura{,-text}-fonts, and
# steinberg-petaluma*-fonts
Patch2:        %{name}-3.6.0-unbundle.patch
# Fix some glitches in the aeolus code
Patch3:        %{name}-3.5.0-aeolus.patch
# Fix deprecation warnings with Qt 5.15.x
# https://github.com/musescore/MuseScore/pull/7388
Patch4:        %{name}-3.6.2-qt-deprecation.patch
# Update the AppData file to fix validation errors
Patch5:        %{name}-3.6.2-appdata.patch

BuildRequires: appstream
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fontforge
BuildRequires: fontpackages-devel
BuildRequires: gcc-c++
BuildRequires: gnu-free-sans-fonts
BuildRequires: gnu-free-serif-fonts
BuildRequires: lame-devel
BuildRequires: make
BuildRequires: marcsabatella-campania-fonts
BuildRequires: perl(Pod::Usage)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: pkgconfig(portaudiocpp)
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5UiTools)
%ifarch %{qt5_qtwebengine_arches}
BuildRequires: pkgconfig(Qt5WebEngine)
%endif
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(vorbis)
BuildRequires: portmidi-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qtsingleapplication-qt5-devel
BuildRequires: steinberg-bravura-fonts-all
BuildRequires: steinberg-petaluma-fonts-all

Requires:      %{name}-fonts-all = %{version}-%{release}
Requires:      gnu-free-sans-fonts
Requires:      gnu-free-serif-fonts
Requires:      hicolor-icon-theme
Requires:      marcsabatella-campania-fonts
Requires:      soundfont2
Requires:      soundfont2-default
Requires:      steinberg-bravura-fonts-all
Requires:      steinberg-petaluma-fonts-all

# For scripting
%{?_qt5:Requires: qt5-qtquickcontrols%{?_isa} = %{_qt5_version}}
%{?_qt5:Requires: qt5-qtquickcontrols2%{?_isa} = %{_qt5_version}}

Provides:      musescore = %{version}-%{release}
Provides:      bundled(beatroot-vamp) = 1.0
Provides:      bundled(intervaltree)
Provides:      bundled(rtf2html) = 0.2.0

%description
MuseScore is a free cross platform WYSIWYG music notation program. Some
highlights:

    * WYSIWYG, notes are entered on a "virtual note sheet"
    * Unlimited number of staves
    * Up to four voices per staff
    * Easy and fast note entry with mouse, keyboard or MIDI
    * Integrated sequencer and FluidSynth software synthesizer
    * Import and export of MusicXML and Standard MIDI Files (SMF)
    * Translated in 26 languages

%package       doc
Summary:       MuseScore documentation
License:       CC-BY
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description   doc
MuseScore is a free cross platform WYSIWYG music notation program.

This package contains the user manual of MuseScore in different languages.

%fontpkg -a

%fontmetapkg

%prep
%autosetup -p1 -n %{upname}-%{version}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} share/sound

# Remove bundled stuff
rm -rf thirdparty/{freetype,openssl,poppler,portmidi,singleapp}
rm -rf fonts/{bravura,campania,FreeS*}

# Force Fedora specific flags:
find . -name CMakeLists.txt -exec sed -i -e 's|-O3|%{optflags}|' {} \+

# Fix EOL encoding
for fil in thirdparty/rtf2html/README{,.ru} \
    share/sound/MuseScore_General_Changelog.md \
    share/sound/MuseScore_General_License.md; do
  sed -i.orig 's|\r||' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

# Font compatibility symlinks so we can use resource files in place
cd fonts
ln -s edwin %{name}-edwin-fonts
ln -s gootville %{name}-gootville-fonts
ln -s leland %{name}-leland-fonts
ln -s mscore %{name}-fonts
ln -s mscore %{name}-mscoretext-fonts
ln -s musejazz %{name}-musejazz-fonts

mkdir mscore-bc-fonts
ln -s ../mscore-BC.sfd mscore-bc-fonts/mscore-BC.sfd
ln -s ../mscore-BC.ttf mscore-bc-fonts/mscore-BC.ttf
ln -s ../fonts_figuredbass.xml mscore-bc-fonts/fonts_figuredbass.xml

mkdir mscore-mscoretab-fonts
ln -s ../mscoreTab.sfd mscore-mscoretab-fonts/mscoreTab.sfd
ln -s ../mscoreTab.ttf mscore-mscoretab-fonts/mscoreTab.ttf
ln -s ../fonts_tablature.xml mscore-mscoretab-fonts/fonts_tablature.xml
cd -

%build
# Build the actual program
%cmake \
    -DCMAKE_BUILD_TYPE=RELEASE         \
    -DCMAKE_CXX_FLAGS="%{optflags} -fsigned-char"    \
    -DCMAKE_CXX_FLAGS_RELEASE="%{optflags} -fPIC -DNDEBUG -DQT_NO_DEBUG -fsigned-char" \
    -DCMAKE_SKIP_RPATH=ON \
    -DAEOLUS=ON \
%if 0%{?__isa_bits} == 32
    -DBUILD_64=OFF \
%endif
%ifnarch %{qt5_qtwebengine_arches}
    -DBUILD_WEBENGINE=OFF \
%endif
    -DDOWNLOAD_SOUNDFONT=OFF \
    -DMUSESCORE_BUILD_CONFIG=release \
    -DOMR=ON \
    -DUSE_PATH_WITH_EXPLICIT_QT_VERSION=ON \
    -DUSE_SYSTEM_FREETYPE=ON \
    -DUSE_SYSTEM_POPPLER=ON \
    -DUSE_SYSTEM_QTSINGLEAPPLICATION=ON
PREFIX=%{_prefix} %cmake_build --target lrelease
PREFIX=%{_prefix} %cmake_build --target manpages
PREFIX=%{_prefix} VERBOSE=1 %cmake_build
PREFIX=%{_prefix} make -C %{_vpath_builddir}/rdoc referenceDocumentation

# Build the fonts
%fontbuild -a

%install
PREFIX=%{_prefix} %cmake_install
PREFIX=%{_prefix} %make_install -C %{_vpath_builddir}/rdoc

mkdir -p %{buildroot}%{_datadir}/applications
cp -a %{_vpath_builddir}/%{name}.desktop %{buildroot}%{_datadir}/applications

# mscz
install -pm 0644 share/templates/*.mscz %{buildroot}%{_datadir}/%{name}-%{shortver}/demos/
# symlinks to be safe
cd %{buildroot}%{_datadir}/%{name}-%{shortver}/demos/
for i in *.mscz; do
  ln -s ../demos/$i ../templates/$i
done
cd -

# Install fonts
%fontinstall -a
metainfo="%{buildroot}%{_metainfodir}/%{fontorg}.mscore-bc-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.mscore-edwin-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.mscore-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.mscore-gootville-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.mscore-leland-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.mscore-mscoretab-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.mscore-mscoretext-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.mscore-musejazz-fonts.metainfo.xml"

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,OFL,OFL-1.1,' \
    -e 's,updatecontact,update_contact,g' \
    -i %{buildroot}%{_metainfodir}/%{fontorg}.mscore-bc-fonts.metainfo.xml \
       %{buildroot}%{_metainfodir}/%{fontorg}.mscore-edwin-fonts.metainfo.xml \
       %{buildroot}%{_metainfodir}/%{fontorg}.mscore-gootville-fonts.metainfo.xml

sed -e 's,GPLv3+ with exceptions,GPL-3.0-or-later WITH Font-exception-2.0,' \
    -e 's,updatecontact,update_contact,g' \
    -i %{buildroot}%{_metainfodir}/%{fontorg}.mscore-fonts.metainfo.xml

sed -e 's,OFL,OFL-1.1-RFN,' \
    -e 's,updatecontact,update_contact,g' \
    -i %{buildroot}%{_metainfodir}/%{fontorg}.mscore-leland-fonts.metainfo.xml \
       %{buildroot}%{_metainfodir}/%{fontorg}.mscore-mscoretab-fonts.metainfo.xml \
       %{buildroot}%{_metainfodir}/%{fontorg}.mscore-mscoretext-fonts.metainfo.xml \
       %{buildroot}%{_metainfodir}/%{fontorg}.mscore-musejazz-fonts.metainfo.xml

# Install SMuFL metadata
cp -p fonts/mscore/metadata.json %{buildroot}%{_datadir}/fonts/mscore-fonts
cp -p fonts/gootville/metadata.json \
      %{buildroot}%{_datadir}/fonts/mscore-gootville-fonts
cp -p fonts/leland/metadata.json \
      %{buildroot}%{_datadir}/fonts/mscore-leland-fonts
cp -p fonts/musejazz/metadata.json \
      %{buildroot}%{_datadir}/fonts/mscore-musejazz-fonts

# Install MuseScore metadata
cp -p fonts/fonts_figuredbass.xml %{buildroot}%{_fontbasedir}/%{name}-bc-fonts
cp -p fonts/fonts_tablature.xml \
      %{buildroot}%{_fontbasedir}/%{name}-mscoretab-fonts

# Mime type
mkdir -p %{buildroot}%{_datadir}mime/packages
install -pm 644 %{SOURCE6} %{buildroot}%{_datadir}/mime/packages/

# Desktop file
# Reset desktop session environment variables so that the pre-mscore-3.5 import dialog renders more consistently.
# See <https://bugzilla.redhat.com/show_bug.cgi?id=1930759>
desktop-file-install \
   --dir=%{buildroot}%{_datadir}/applications \
   --add-category="X-Notation" \
   --remove-category="Sequencer" \
   --remove-category="AudioVideoEditing" \
   --add-mime-type="audio/midi" \
   --add-mime-type="application/xml" \
   --set-key="Exec" --set-value='env XDG_CURRENT_DESKTOP="" KDE_FULL_SESSION="" DESKTOP_SESSION="" mscore %F' \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

# Move images to the freedesktop location
for sz in 16 24 32 48 64 96 128 512; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/{apps,mimetypes}
  install -pm 644 assets/musescore-icon-round-${sz}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/%{name}.png
  install -pm 644 assets/musescore-icon-round-${sz}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes/%{name}.png
done
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/{apps,mimetypes}
install -pm 644 assets/musescore-icon-round.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -pm 644 assets/musescore-icon-round.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/%{name}.svg

# Validate appdata
appstreamcli validate --no-net $metainfo

# Manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 %{_vpath_builddir}/%{name}.1 %{buildroot}%{_mandir}/man1/

# There are many doc files spread around the tarball. Let's collect them
mv thirdparty/rtf2html/ChangeLog        ChangeLog.rtf2html
mv thirdparty/rtf2html/COPYING.LESSER   COPYING.LESSER.rtf2html
mv thirdparty/rtf2html/README           README.rtf2html
mv thirdparty/rtf2html/README.mscore    README.mscore.rtf2html
mv thirdparty/rtf2html/README.ru        README.ru.rtf2html
mv share/wallpaper/COPYRIGHT            COPYING.wallpaper
mv %{buildroot}%{_datadir}/%{name}-%{shortver}/sound/MuseScore_General_License.md \
   COPYING.MuseScore_General

# Do not duplicate files from qt5-qtwebengine
rm -f %{buildroot}%{_bindir}/QtWebEngineProcess
rm -fr %{buildroot}%{_prefix}/lib

# Move the soundfonts to where the rest of the system expects them to be
mv %{buildroot}%{_datadir}/%{name}-%{shortver}/sound \
   %{buildroot}%{_datadir}/soundfonts
ln -s ../soundfonts %{buildroot}%{_datadir}/%{name}-%{shortver}/sound

%check
# iotest seems outdated. Skipping.
# reftest needs the X server. Skipping.

# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck -a
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%files
%doc README*
%doc share/sound/MuseScore_General_Changelog.md
%doc share/sound/MuseScore_General_Readme.md
%license LICENSE.GPL COPYING* share/sound/MuseScore_General_License.md
%{_bindir}/%{name}
%{_bindir}/musescore
%{_datadir}/%{name}-%{shortver}/
%exclude %{_datadir}/%{name}-%{shortver}/manual/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/*.appdata.xml
%exclude %{_datadir}/mime/packages/musescore.xml
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/*
%{_datadir}/soundfonts/aeolus/
%{_datadir}/soundfonts/MuseScore_General.sf3

%files doc
%doc %{_datadir}/%{name}-%{shortver}/manual/

%fontfiles -z 1
%{_datadir}/fonts/mscore-fonts/metadata.json

%fontfiles -z 2

%fontfiles -z 3
%{_datadir}/fonts/mscore-gootville-fonts/metadata.json

%fontfiles -z 4
%{_datadir}/fonts/mscore-bc-fonts/fonts_figuredbass.xml

%fontfiles -z 5
%{_datadir}/fonts/mscore-mscoretab-fonts/fonts_tablature.xml

%fontfiles -z 6
%{_datadir}/fonts/mscore-musejazz-fonts/metadata.json

%fontfiles -z 7

%fontfiles -z 8
%{_datadir}/fonts/mscore-leland-fonts/metadata.json

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 3.6.2-9
- Fix doubled slashes in pathnames

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 3.6.2-9
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 3.6.2-8
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 3.6.2-7
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 3.6.2-4
- Add -appdata patch and use the upstream appdata file
- Fix Edwin font license (was mistakenly AGPLv3 with exceptions)
- Fix invalid font metainfo generated by the Fedora font macros

* Thu Apr 15 2021 Jerry James <loganjerry@gmail.com> - 3.6.2-4
- Update the soundfont (bz 1949861)

* Tue Mar 23 2021 Audrey Toskin <audrey@tosk.in> - 3.6.2-3
- Patch .desktop file to work around possible bug in Qt/KDE.
  See <https://bugzilla.redhat.com/show_bug.cgi?id=1930759>

* Sat Mar  6 2021 Jerry James <loganjerry@gmail.com> - 3.6.2-2
- Add upstream patch to silence Qt 5.15 deprecation warnings

* Mon Feb  8 2021 Jerry James <loganjerry@gmail.com> - 3.6.2-1
- Version 3.6.2

* Wed Jan 27 2021 Jerry James <loganjerry@gmail.com> - 3.6.1-1
- Version 3.6.1
- Drop upstreamed -qt5-5.15 patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Jerry James <loganjerry@gmail.com> - 3.6-1
- Version 3.6.0
- Drop upstreamed -edit-reset and -omr patches
- Add qt5-5.15 patch

* Mon Nov 23 07:54:01 CET 2020 Jan Grulich <jgrulich@redhat.com> - 3.5.2-4
- rebuild (qt5)

* Tue Nov 10 2020 Jerry James <loganjerry@gmail.com> - 3.5.2-3
- Unbundle the Campania font
- Convert font packaging to the latest guidelines
- Add -edit-reset patch to fix broken icon paths

* Mon Nov  2 2020 Jerry James <loganjerry@gmail.com> - 3.5.2-2
- Ensure a release build, not a dev build

* Mon Oct 19 2020 Jerry James <loganjerry@gmail.com> - 3.5.2-1
- Version 3.5.2

* Tue Oct  6 2020 Jerry James <loganjerry@gmail.com> - 3.5.1-1
- Version 3.5.1

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 3.5.0-2
- rebuild (qt5)

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 3.5.0-1
- Version 3.5.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.4.2-4
- rebuild (qt5)

* Sat Apr  4 2020 Jerry James <loganjerry@gmail.com> - 3.4.2-3
- Rebuild for updated Bravura fonts

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 3.4.2-2
- Desktop file should not claim LilyPond support (bz 1813797)

* Mon Feb 17 2020 Jerry James <loganjerry@gmail.com> - 3.4.2-1
- Version 3.4.2
- Drop the -user-default-soundfont patch; use a symlink instead
- R both qt5-qtquickcontrols and qt5-qtquickcontrols2; both seem to be used
- kQOAuth is no longer used, so drop unbundling

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.3.4-4
- Rebuild for poppler-0.84.0

* Sat Dec 14 2019 Jerry James <loganjerry@gmail.com> - 3.3.4-3
- Require QtQuick.Controls version 2

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.4-2
- rebuild (qt5)

* Wed Dec  4 2019 Jerry James <loganjerry@gmail.com> - 3.3.4-1
- Version 3.3.4

* Tue Nov 26 2019 Jerry James <loganjerry@gmail.com> - 3.3.3-1
- Version 3.3.3

* Fri Nov 22 2019 Jerry James <loganjerry@gmail.com> - 3.3.2-2
- Fix segfault in the aeolus destructor

* Thu Nov 14 2019 Jerry James <loganjerry@gmail.com> - 3.3.2-1
- Version 3.3.2

* Wed Nov 13 2019 Jerry James <loganjerry@gmail.com> - 3.3.1-1
- Version 3.3.1

* Fri Nov  1 2019 Jerry James <loganjerry@gmail.com> - 3.3.0-1
- Version 3.3.0
- Unbundle the bravura fonts

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 3.2.3-3
- rebuild (qt5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Jerry James <loganjerry@gmail.com> - 3.2.3-1
- Version 3.2.3
- Update URLs
- Drop upstreamed patches: -fix-files-for-precompiled-header,
  -fix-desktop-file, -fix-fonts_tablature, -missing-includes
- Unbundle gnu-free-{sans,serif}-fonts, kqoauth, and QtSingleApplication
- Remove "and OFL" from main package License; fonts are in -fonts subpackage
- Remove "and CC-BY" from main package License; applies to -doc subpackage

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 2.2.1-11
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 2.2.1-10
- rebuild (qt5)

* Thu Apr 25 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-9
- Fix build (#1702062)

* Mon Mar 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-9
- rebuild (qt5)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-7
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 2.2.1-6
- rebuild (qt5)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-4
- rebuild (qt5)

* Thu May 31 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.2.1-3
- Fix missing include for qt >= 5.11 (RHBZ#1584834)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-2
- rebuild (qt5)

* Wed Apr 04 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.2.1-1
- Update to 2.2.1

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 2.1.0-12
- rebuild (qt5)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-10
- Remove (hopefully) last dependency on qt4

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-9
- Remove obsolete scriptlets

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.1.0-8
- rebuild (qt5)

* Mon Dec 25 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-7
- Link against full template path

* Mon Dec 25 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-6
- Correct mscz link

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.0-5
- rebuild (qt5)

* Mon Nov 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-4
- Use proper qtsingleapplication (qt5)

* Sun Oct 29 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-3
- Use system libs

* Sat Oct 21 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-2
- Remove non-free scores
- Fix pch project depends
- Reorder patches

* Tue Oct 17 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-1
- Update to 2.1

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.3-10
- BR: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.0.3-7
- Removed BR: qt5-qtquick1-devel as it is no longer in Fedora

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.3-4
- Rebuild (Power64)

* Mon May 09 2016 Brendan Jones <brendan.jones.it@gmail.com> 2.0.3-3
- Font locations

* Fri May 06 2016 Brendan Jones <brendan.jones.it@gmail.com> 2.0.3-2
- correct load and font errors

* Sun Apr 24 2016 Brendan Jones <brendan.jones.it@gmail.com> 2.0.3-1
- Update to 2.0.3
- fix make job flags
- rename modified patches

* Sat Feb 27 2016 Brendan Jones <brendan.jones.it@gmail.com> 2.0.2-1
- Update to 2.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Brendan Jones <brendan.jones.it@gmail.com> 2.0.1-6
- Fix fonts_tabulature.xml location bug rhbz#1236965 rhbz#1262528

* Wed Sep 16 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.0.1-5
- added backport fixing compilation with Qt5.5 - rhbz#1263806

* Tue Jul 14 2015 Brendan Jones <brendan.jones.it@gmail.com> 2.0.1-4
- Rebuilt

* Tue Jun 30 2015 Brendan Jones <brendan.jones.it@gmail.com> 2.0.1-3
- Fix font locations

* Tue Jun 23 2015 Brendan Jones <bsjones@fedoraproject.org> - 2.0.1-2
- Clean up change log

* Tue Jun 23 2015 Brendan Jones <bsjones@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 - patches provided by Bodhi Zazen

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.0-3
- do not strip bits when installing (bz 1215956)

* Sat Apr 25 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.0-2
- add BR: doxygen
- add -fsigned-char for ARM

* Sat Apr 25 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Remove mp3 support to fix FTBFS
- Add pulseaudio-libs-devel to BR

* Tue Nov 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.3-8
- Add metainfo file to show mscore-MuseJazz font in gnome-software

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3-7
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Dan Horák <dan[at]danny.cz> - 1.3-4
- fix FTBFS (#992300)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Tom Callaway <spot@fedoraproject.org> - 1.3-2
- perl(Pod::Usage) needed for font generation

* Fri Apr 12 2013 Tom Callaway <spot@fedoraproject.org> - 1.3-1
- update to 1.3
- remove mscore/demos/prelude.mscx from source tarball (it is non-free, see bz951379)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-1
- Update to 1.2.

* Sat Mar 03 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.1-4
- Fix accidontals crash RHBZ#738044

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 28 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.1-1
- Update to 1.1.

* Tue Feb 08 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.0-1
- Update to 1.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 26 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.6.3-1
- Update to 0.9.6.3

* Thu Aug 19 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.6.2-1
- Update to 0.9.6.2

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.6.1-1
- Update to 0.9.6.1

* Mon Jun 14 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.6-1
- Update to 0.9.6
- Split documentation into its own package
- Move some gcc warning fixes into a patch

* Tue Dec 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.5-3
- Fix build flags on F-11

* Tue Dec 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.5-2
- Add default soundfont support for exported audio files
- Rebuild against new libsndfile for additional functionality
- Drop F-10 related bits from specfile
- Make fonts subpackage noarch
- Fix build failure on arm architecture

* Fri Aug 21 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.5-1
- Update to 0.9.5

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-6
- Update the .desktop file

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-4
- Font package cleanup for F-12 (RHBZ#493463)
- One specfile for all releases

* Mon Mar 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-3.fc10.1
- Add BR: tetex-font-cm-lgc for Fedora < 11

* Mon Mar 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-3
- Add Provides: musescore = %%{name}-%%{version}
- Replace "fluid-soundfont" requirement with "soundfont2-default"

* Fri Mar 06 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-2
- Add extra BR:tex-cm-lgc for F-11+. This is necessary to build the fonts from source
- Update icon scriptlets according to the new guidelines

* Sat Feb 21 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-1
- Initial Fedora build
