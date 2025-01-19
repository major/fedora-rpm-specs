# The version of MuseScore itself
%global musescore_ver             4.3.2
%global musescore_maj             %(cut -d. -f-2 <<< %{musescore_ver})
%global giturl                    https://github.com/musescore/MuseScore

# Font versions.  Use otfinfo -v to extract these values.
%global mscore_font_ver           2.002
%global mscoretext_font_ver       1.0
%global musescoreicon_font_ver    1.0
%global mscorebc_font_ver         1.0
%global mscoretabulature_font_ver 001.000
%global musejazz_font_ver         1.0
%global gootville_font_ver        1.3
%global gootville_text_font_ver   1.2
%global soundfont_ver             0.2.0

# NOTE: The Release tag can be reset to one only if ALL version numbers above
# increase.  This is unlikely to happen.  Resign yourself to bumping the release
# number indefinitely.
Name:           musescore
Summary:        Music Composition & Notation Software
Version:        %{musescore_ver}
Release:        17%{?dist}

# The MuseScore project itself is GPL-3.0-only WITH Font-exception-2.0.  Other
# licenses in play:
# GPL-2.0-or-later
# - thirdparty/beatroot
# (GPL-2.0-only OR GPL-3.0-only)
# - thirdparty/KDDockWidgets
# GPL-3.0-or-later:
# - share/plugins/courtesy_accidentals/
# - share/plugins/intervals/
# - share/plugins/tuning/
# - share/plugins/tuning_modal/
# LGPL-3.0-only
# - share/wallpapers/paper5.png
# LGPL-2.1-or-later
# - thirdparty/fluidsynth
# - thirdparty/rtf2html
# (LGPL-2.1-or-later AND GPL-3.0-or-later)
# - src/braille/thirdparty/liblouis/
# MIT
# - thirdparty/intervaltree
# - src/framework/global/thirdparty/deto_async/LICENSE
# - src/framework/global/thirdparty/haw_logger/LICENSE
# - src/framework/global/thirdparty/haw_profiler/LICENSE
# - thirdparty/fluidsynth/fluidsynth-2.1.4/src/bindings/fluid_rtkit.c
# - thirdparty/fluidsynth/fluidsynth-2.1.4/src/bindings/fluid_rtkit.h
# BSL-1.0
# - code from the utf8cpp header-only library
# BSD-2-Clause
# - code from the picojson header-only library
# Unlicense OR MIT-0
# - code from the dr_libs header-only library
# Unlicense OR MIT
# - code from the stb_vorbis header-only library
License:        GPL-3.0-only WITH Font-exception-2.0 AND GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND GPL-3.0-or-later AND LGPL-3.0-only AND LGPL-2.1-or-later AND (LGPL-2.1-or-later AND GPL-3.0-or-later) AND MIT AND BSD-2-Clause AND (Unlicense OR MIT-0) AND (Unlicense OR MIT)
URL:            https://musescore.org/
VCS:            git:%{giturl}.git

%global fontorg         org.musescore
%global fontdocs        fonts/README.md

%global fontfamily1     MScore
%global fontsummary1    MuseScore base music font
%global fontlicense1    GPL-3.0-or-later WITH Font-exception-2.0
%global fonts1          fonts/mscore/mscore.ttf
%global fontconfs1      %{SOURCE1}
%global fontdescription1 %{expand:
This package contains the base MuseScore music font.  It is derived from
the Emmentaler font created for Lilypond, but has been modified for
MuseScore.}
%global fontpkgheader1  %{expand:
Epoch:          1
Version:        %{mscore_font_ver}
}

%global fontfamily2     MScoreText
%global fontsummary2    MuseScore base text font
%global fontlicense2    OFL-1.1-RFN
%global fonts2          fonts/mscore/MScoreText.ttf
%global fontconfs2      %{SOURCE2}
%global fontdescription2 %{expand:
This package contains the base MuseScore text font.}
%global fontpkgheader2  %{expand:
Version:        %{mscoretext_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-mscoretext-fonts < 4.0
Provides:       mscore-mscoretext-fonts = %{musescore_ver}-%{release}
}

%global fontfamily3     MusescoreIcon
%global fontsummary3    MuseScore icon set
%global fontlicense3    GPL-3.0-or-later WITH Font-exception-2.0
%global fonts3          fonts/mscore/MusescoreIcon.ttf
%global fontconfs3      %{SOURCE3}
%global fontdescription3 %{expand:
This package contains a set of MuseScore icons.}
%global fontpkgheader3  %{expand:
Version:        %{musescoreicon_font_ver}
}

%global fontfamily4     MScoreBC
%global fontsummary4    Font with Basso Continuo digits and symbols
%global fontlicense4    OFL-1.1-RFN
%global fonts4          fonts/mscore-BC.ttf
%global fontconfs4      %{SOURCE4}
%global fontdescription4 %{expand:
This package contains a MuseScore font with Basso Continuo digits and
symbols, matching glyphs in the main MuseScore font.}
%global fontpkgheader4  %{expand:
Version:        %{mscorebc_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-bc-fonts < 4.0
Provides:       mscore-bc-fonts = %{musescore_ver}-%{release}
}

%global fontfamily5     MScoreTabulature
%global fontsummary5    Font with Renaissance-style tabulatures
%global fontlicense5    OFL-1.1-RFN
%global fonts5          fonts/mscoreTab.ttf
%global fontconfs5      %{SOURCE5}
%global fontdescription5 %{expand:
This package contains a MuseScore font with Renaissance-style tabulatures.}
%global fontpkgheader5  %{expand:
Version:        %{mscoretabulature_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-mscoretab-fonts < 4.0
Provides:       mscore-mscoretab-fonts = %{musescore_ver}-%{release}
}

%global fontfamily6     MuseJazz
%global fontsummary6    Handwritten font for text, chord names, and so forth
%global fontlicense6    OFL-1.1
%global fontlicenses6   fonts/musejazz/OFL.txt
%global fonts6          fonts/musejazz/MuseJazz.otf
%global fontconfs6      %{SOURCE6}
%global fontdescription6 %{expand:
This package contains a MuseScore font with a handwritten look for text,
chord names, etc.}
%global fontpkgheader6  %{expand:
Version:        %{musejazz_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-musejazz-fonts < 4.0
Provides:       mscore-musejazz-fonts = %{musescore_ver}-%{release}
}

%global fontfamily7     MuseJazz Text
%global fontsummary7    Text font to complement MuseJazz
%global fontlicense7    OFL-1.1
%global fontlicenses7   fonts/musejazz/OFL.txt
%global fonts7          fonts/musejazz/MuseJazzText.otf
%global fontconfs7      %{SOURCE7}
%global fontdescription7 %{expand:
The MuseJazz Text font is designed to complement the MuseJazz font.}
%global fontpkgheader7  %{expand:
Version:        %{musejazz_font_ver}
}

%global fontfamily8     Gootville
%global fontsummary8    Derivative of the Gonville font
%global fontlicense8    OFL-1.1
%global fonts8          fonts/gootville/Gootville.otf
%global fontdocs8       fonts/gootville/readme.txt
%global fontconfs8      %{SOURCE8}
%global fontdescription8 %{expand:
Gootville is a derivative of the Gonville font created by Simon Tatham
for Lilypond.  The two fonts have common graphic aspects, but the
registration, glyph order, and other aspects of Gootville have been
modified for MuseScore.}
%global fontpkgheader8  %{expand:
Version:        %{gootville_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-gootville-fonts < 4.0
Provides:       mscore-gootville-fonts = %{musescore_ver}-%{release}
}

%global fontfamily9     Gootville Text
%global fontsummary9    Text font to complement Gootville
%global fontlicense9    OFL-1.1
%global fonts9          fonts/gootville/GootvilleText.otf
%global fontdocs9       fonts/gootville/readme.txt
%global fontconfs9      %{SOURCE9}
%global fontdescription9 %{expand:
The Gootville Text font is designed to complement the Gootville font.}
%global fontpkgheader9  %{expand:
Version:        %{gootville_text_font_ver}
}

Source0:        %{giturl}/archive/v%{musescore_ver}/MuseScore-%{musescore_ver}.tar.gz
# Fontconfig files
Source1:        65-%{fontpkgname1}.conf
Source2:        65-%{fontpkgname2}.conf
Source3:        65-%{fontpkgname3}.conf
Source4:        65-%{fontpkgname4}.conf
Source5:        65-%{fontpkgname5}.conf
Source6:        65-%{fontpkgname6}.conf
Source7:        65-%{fontpkgname7}.conf
Source8:        65-%{fontpkgname8}.conf
Source9:        65-%{fontpkgname9}.conf

# Ensure CMake will use qmake-qt5
Patch:          %{name}-fix-qmake-path.patch
# Unbundle dr_libs, flac, freetype, gtest, lame, opusenc, and stb
# We cannot unbundle KDDockWidgets because the Fedora package builds the
# QtWidgets version, but MuseScore needs the QtQuick version.
# See https://bugzilla.redhat.com/show_bug.cgi?id=2227098
Patch:          %{name}-unbundle-libs.patch
# Unbundle the fonts to comply with the font packaging guidelines
Patch:          %{name}-unbundle-fonts.patch
# FIXME: a translucent background leads to an invisible splash screen.
# Why?  I don't know, but make the background opaque for now.
Patch:          %{name}-splashscreen.patch
# Help the compiler find the ffmpeg headers
Patch:          %{name}-ffmpeg.patch
# Fix invalid AppData
# - Remove an invalid <icon> tag
# - Remove duplicated <release> data
# https://github.com/musescore/MuseScore/pull/21482
Patch:          %{name}-appdata.patch
# Avoid calling localtime in multithreaded code
# https://github.com/musescore/MuseScore/pull/21178
Patch:          %{name}-localtime.patch
# Workaround to avoid an out-of-bounds vector access that causes crashes.
# This patch treats the symptom, not the actual disease.  We need to find
# and fix the underlying cause.
Patch:          %{name}-vector.patch
# Fix a build failure due to a missing include
Patch:          %{name}-qvariantmap.patch
# Fix a build failure due to a missing include
Patch:          %{name}-qeventloop.patch
# Fix a build failure due to a missing include
Patch:          %{name}-qpainter.patch
# Fix a build failure due to a missing include
Patch:          %{name}-qxmlstreamreader.patch
# Fix a build failure due to a missing include
Patch:          %{name}-qvariantlist.patch
# Fix a build failure due to a missing include
Patch:          %{name}-qtcore.patch
# Fix an abort when ALSA is shutdown but was never initialized
# https://github.com/musescore/MuseScore/pull/21376
Patch:          %{name}-alsa-shutdown.patch
# Fix a crash when built with the undefined behavior sanitizer
Patch:          %{name}-null-staff.patch
# Fix a data race inside kors_profiler
# https://github.com/igorkorsukov/kors_profiler/pull/1
Patch:          %{name}-kors-profiler-race.patch
# Fix a data race in the modularity code
Patch:          %{name}-modularity-race.patch
# Add compatibility with FFMPEG 7.0
# https://github.com/musescore/MuseScore/commit/d0ceb71115c13a24542afae49d3739836d22340d
Patch:          0001-Add-compatibility-with-FFMPEG-7.0.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickTemplates2)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  cmake(tinyxml2)
BuildRequires:  desktop-file-utils
BuildRequires:  dr_libs-static
BuildRequires:  font(finalebroadway)
BuildRequires:  font(finalebroadwaytext)
BuildRequires:  font(finalemaestro)
BuildRequires:  font(finalemaestrotext)
BuildRequires:  fontforge
BuildRequires:  fonts-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  hardlink
BuildRequires:  lame-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  marcsabatella-campania-fonts
BuildRequires:  mesa-dri-drivers
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libopusenc)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  qt5-qhelpgenerator
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  stb_vorbis-static
BuildRequires:  steinberg-bravura-fonts-all
BuildRequires:  steinberg-petaluma-fonts-all
BuildRequires:  utf8cpp-static

Requires:       gootville-fonts = %{gootville_font_ver}-%{release}
Requires:       gootville-text-fonts = %{gootville_text_font_ver}-%{release}
Requires:       mscore-fonts = 1:%{mscore_font_ver}-%{release}
Requires:       mscorebc-fonts = %{mscorebc_font_ver}-%{release}
Requires:       mscoretabulature-fonts = %{mscoretabulature_font_ver}-%{release}
Requires:       mscoretext-fonts = %{mscoretext_font_ver}-%{release}
Requires:       musejazz-fonts = %{musejazz_font_ver}-%{release}
Requires:       musejazz-text-fonts = %{musejazz_font_ver}-%{release}
Requires:       musescoreicon-fonts = %{musescoreicon_font_ver}-%{release}
Requires:       %{name}-data = %{musescore_ver}-%{release}
Requires:       %{name}-soundfont = %{soundfont_ver}-%{release}

Requires:       font(edwin)
Requires:       font(finalebroadway)
Requires:       font(finalebroadwaytext)
Requires:       font(finalemaestro)
Requires:       font(finalemaestrotext)
Requires:       font(leland)
Requires:       font(lelandtext)
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
Requires:       hicolor-icon-theme
Requires:       marcsabatella-campania-fonts
Requires:       qt5-qtquickcontrols%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}
Requires:       soundfont2
Requires:       soundfont2-default
Requires:       steinberg-bravura-fonts-all
Requires:       steinberg-petaluma-fonts-all

# The following products have been modified from their upstream versions,
# or MuseScore uses internal (non-public) APIs
Provides:       bundled(beatroot-vamp) = 1.0
Provides:       bundled(fluidsynth) = 2.3.3
Provides:       bundled(liblouis) = 3.24.0
Provides:       bundled(intervaltree) = 0.1
Provides:       bundled(rtf2html) = 0.2.0
Provides:       bundled(KDDockWidgets) = 1.5.0

# FIXME: it might be possible to unbundle these
Provides:       bundled(deto_async)
Provides:       bundled(haw_logger)
Provides:       bundled(haw_profiler)
Provides:       bundled(kors_logger) = 1.3
Provides:       bundled(picojson) = 1.3.0

# This can be removed when F42 reaches EOL
Obsoletes:      mscore < 4.0
Provides:       mscore = %{musescore_ver}-%{release}
Obsoletes:      mscore-fonts-all < 4.0
Provides:       mscore-fonts-all = %{musescore_ver}-%{release}
Obsoletes:      mscore-doc < 4.0
Provides:       mscore-doc = %{musescore_ver}-%{release}

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

%package        data
Summary:        Common data for MuseScore
Version:        %{musescore_ver}
License:        GPL-3.0-only WITH Font-exception-2.0
BuildArch:      noarch

%description    data
Shared data for all MuseScore installations.

%package        soundfont
Summary:        Basic soundfont for MuseScore
Version:        %{soundfont_ver}
License:        MIT
BuildArch:      noarch

%description    soundfont
This is a scaled-down version of MuseScore_General-HQ.sf2 that replaces
some of the larger instruments to save memory and CPU on older PCs.
This SoundFont is currently a work-in-progress.  Some samples are
derived from FluidR3Mono.

%fontpkg -a

%prep
%autosetup -n MuseScore-%{musescore_ver} -p1

%conf
# Remove bundled stuff
rm -rf thirdparty/{dr_libs,dtl,flac,freetype,googletest,lame,opus*,singleapp,stb}
rm -rf src/framework/global/thirdparty/{tinyxml,utfcpp*}

# Fix EOL encoding
%linuxtext -n share/sound/MS_Basic_Changelog.md share/sound/MS\ Basic_License.md thirdparty/rtf2html/README{,.ru}

# Build in release mode
sed -i '/MUSESCORE_BUILD_MODE/s/dev/release/' CMakeLists.txt

# Font compatibility symlinks so we can use resource files in place
cd fonts
ln -s edwin %{name}-edwin-fonts
ln -s gootville %{name}-gootville-fonts
ln -s gootville %{name}-gootville-text-fonts
ln -s leland %{name}-leland-fonts
ln -s leland %{name}-leland-text-fonts
ln -s mscore %{name}-fonts
ln -s mscore %{name}-mscoretext-fonts
ln -s musejazz %{name}-musejazz-fonts
ln -s musejazz %{name}-musejazz-text-fonts

mkdir %{name}-mscorebc-fonts
ln -s ../mscore-BC.sfd %{name}-mscorebc-fonts/mscore-BC.sfd
ln -s ../mscore-BC.ttf %{name}-mscorebc-fonts/mscore-BC.ttf

mkdir %{name}-mscoretabulature-fonts
ln -s ../mscoreTab.sfd %{name}-mscoretabulature-fonts/mscoreTab.sfd
ln -s ../mscoreTab.ttf %{name}-mscoretabulature-fonts/mscoreTab.ttf
cd ..

%build
# Build the actual program
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RELEASE         \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING='%{build_cxxflags} -fPIC -DNDEBUG -DQT_NO_DEBUG' \
    -DMUE_BUILD_CRASHPAD_CLIENT:BOOL=OFF \
    -DMUE_BUILD_VIDEOEXPORT_MODULE:BOOL=ON \
    -DMUE_COMPILE_USE_PCH:BOOL=OFF \
    -DMUE_COMPILE_USE_SYSTEM_FLAC:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_FREETYPE:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_OPUSENC:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_TINYXML:BOOL=ON \
    -DMUE_DOWNLOAD_SOUNDFONT:BOOL=OFF \
    -DMUE_ENABLE_LOGGER_DEBUGLEVEL:BOOL=OFF \
    -DMUE_ENABLE_STRING_DEBUG_HACK:BOOL=OFF
PREFIX=%{_prefix} %cmake_build --target lrelease
PREFIX=%{_prefix} VERBOSE=1 %cmake_build
PREFIX=%{_prefix} %cmake_build --target manpages

# Build the fonts
%fontbuild -a

%install
PREFIX=%{_prefix} %cmake_install

# Delete files that we don't want to install
rm -rf %{buildroot}%{_includedir} %{buildroot}%{_libdir}

# Install fonts
%fontinstall -a
mkdir -p %{buildroot}%{_datadir}/mscore-%{musescore_maj}/fonts
cp -p fonts/*.xml %{buildroot}%{_datadir}/mscore-%{musescore_maj}/fonts

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -i 's,updatecontact,update_contact,g' \
  %{buildroot}%{_metainfodir}/%{fontorg}.gootville-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.gootville-text-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.mscore-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.mscorebc-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.mscoretabulature-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.mscoretext-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.musejazz-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.musejazz-text-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.musescoreicon-fonts.metainfo.xml

# Install SMuFL metadata
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/mscore
cp -p fonts/mscore/metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/mscore
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/mscore/mscore.json
ln -s mscore %{buildroot}%{_datadir}/SMuFL/Fonts/Emmentaler
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/Gootville
cp -p fonts/gootville/metadata.json \
      %{buildroot}%{_datadir}/SMuFL/Fonts/Gootville
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/Gootville/Gootville.json
ln -s Gootville %{buildroot}%{_datadir}/SMuFL/Fonts/Gonville
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/MuseJazz
cp -p fonts/musejazz/metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/MuseJazz
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/MuseJazz/MuseJazz.json

# Validate the desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/org.musescore.MuseScore.desktop

# Validate appdata
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.musescore.MuseScore.appdata.xml

# There are many doc files spread around the tarball. Let's collect them
mv thirdparty/rtf2html/ChangeLog        ChangeLog.rtf2html
mv thirdparty/rtf2html/COPYING.LESSER   COPYING.LESSER.rtf2html
mv thirdparty/rtf2html/README           README.rtf2html
mv thirdparty/rtf2html/README.mscore    README.mscore.rtf2html
mv thirdparty/rtf2html/README.ru        README.ru.rtf2html
mv share/wallpapers/COPYRIGHT           COPYING.wallpapers
mv %{buildroot}%{_datadir}/mscore-%{musescore_maj}/sound/MS\ Basic_License.md .

# Put a link to the soundfont from the system soundfont directory
mkdir -p %{buildroot}%{_datadir}/soundfonts
ln -s ../mscore-%{musescore_maj}/sound/MS\ Basic.sf3 \
   %{buildroot}%{_datadir}/soundfonts

# Hardlink duplicate files
hardlink -t %{buildroot}%{_datadir}/mscore-%{musescore_maj}

%check
%fontcheck -a

# We would like to do this, but upstream's test suite does not properly
# initialize the font provider, and 9 of the tests subsequently segfault
# as a direct result.  How are the tests supposed to be run?
#%%global __ctest xvfb-run -d /usr/bin/ctest
#export XDG_RUNTIME_DIR=/tmp/runtime-mockbuild
#mkdir -m 0700 $XDG_RUNTIME_DIR
#%%ctest
#rm -fr $XDG_RUNTIME_DIR

%files
%doc README* share/sound/MS?Basic_Readme.md share/sound/MS_Basic_Changelog.md
%license LICENSE.txt share/sound/MS?Basic_License.md
%{_bindir}/mscore
%{_mandir}/man1/mscore.1*
%{_mandir}/man1/musescore.1*
%{_datadir}/icons/hicolor/*/apps/mscore.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/applications/org.musescore.MuseScore.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_metainfodir}/*.appdata.xml

%files data
%{_datadir}/mscore-%{musescore_maj}/
%exclude %{_datadir}/mscore-%{musescore_maj}/sound

%files soundfont
%{_datadir}/mscore-%{musescore_maj}/sound
%{_datadir}/soundfonts/*.sf3

%fontfiles -z 1
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
%{_datadir}/SMuFL/Fonts/mscore/
%{_datadir}/SMuFL/Fonts/Emmentaler

%fontfiles -z 2

%fontfiles -z 3

%fontfiles -z 4

%fontfiles -z 5

%fontfiles -z 6
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
%{_datadir}/SMuFL/Fonts/MuseJazz/

%fontfiles -z 7

%fontfiles -z 8
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
%{_datadir}/SMuFL/Fonts/Gootville/
%{_datadir}/SMuFL/Fonts/Gonville

%fontfiles -z 9

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 4.3.2-16
- Rebuild with dr_flac 0.12.43, dr_mp3 0.6.40, and dr_wav 0.13.17

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 4.3.2-15
- rebuild for tinyxml2

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 4.3.2-14
- Rebuild for ffmpeg 7

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Jerry James <loganjerry@gmail.com> - 4.3.2-12
- Version 4.3.2

* Fri Jun  7 2024 Jerry James <loganjerry@gmail.com> - 4.3.1-11
- Version 4.3.1

* Tue May  7 2024 Jerry James <loganjerry@gmail.com> - 4.3.0-10
- Version 4.3.0

* Sat May 04 2024 Robert-André Mauchin <zebob.m@gmail.com> - 4.2.1-10
- Add patch for FFMPEG 7 compatibility

* Wed Mar 20 2024 Jerry James <loganjerry@gmail.com> - 4.2.1-9
- Add patch to avoid crash with the undefined behavior sanitizer
- Add patch to avoid data race inside kors_profiler
- Add patch to avoid data race in the modularity code

* Mon Feb  5 2024 Jerry James <loganjerry@gmail.com> - 4.2.1-8
- Version 4.2.1
- Add patch to avoid races in localtime()
- Add patch to avoid out-of-bounds vector accesses
- Disable jack support; it interferes with pulseaudio support

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Jerry James <loganjerry@gmail.com> - 4.2.0-5
- Version 4.2.0
- Drop upstreamed neon patch

* Fri Oct 20 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-4
- Another attempt at fixing font metadata loading (bz 2244606)

* Tue Oct 17 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-3
- Link metadata to SMuFL-compliant names (bz 2244606)
- Fix misspelling of mscoretabulature that breaks font loading

* Thu Aug 31 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-2
- Fix Gootville font config file error

* Wed Aug 30 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-1
- Version 4.1.1
- Rename from mscore to musescore
- Unbundle the Leland and Edwin fonts
- Unbundle gtest, tinyxml2, and utf8cpp
- Install SMuFL files in a standard place
- Move large noarch data into data subpackage
- Hardlink duplicate files

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Jerry James <loganjerry@gmail.com> - 3.6.2-13
- Fix 100% CPU after restarting sound devices (bz 2055986)
- Fix Aeolus crash at exit
- Do not swizzle license names after SPDX conversion

* Tue Nov 29 2022 Jerry James <loganjerry@gmail.com> - 3.6.2-12
- Convert License tags to SPDX

* Fri Sep 23 2022 Jan Grulich <jgrulich@redhat.com> - 3.6.2-12
- Bring back dependencies on qtquickcontrols

* Fri Sep 23 2022 Jan Grulich <jgrulich@redhat.com> - 3.6.2-11
- Drop hardcoded Qt version requirement

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

