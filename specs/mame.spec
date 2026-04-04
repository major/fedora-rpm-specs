#The debug build is disabled by default, please use # --with debug to override
%bcond_with debug

%global baseversion 287

%undefine _auto_set_build_flags

Name:           mame
Version:        0.%{baseversion}
Release:        %autorelease
Summary:        Multiple Arcade Machine Emulator

#From COPYING:
#MAME as a whole is made available under the terms of the GNU General
#Public License.  Individual source files may be made available under
#less restrictive licenses, as noted in their respective header
#comments.

License:        GPL-2.0-or-later
URL:            http://mamedev.org/
Source0:        https://github.com/mamedev/%{name}/archive/%{name}0%{baseversion}/%{name}-%{name}0%{baseversion}.tar.gz
Source1:        https://mamedev.org/releases/whatsnew_0%{baseversion}.txt
Patch0:         %{name}-fortify.patch
Patch1:         0001-Hack-allowing-bgfx-to-initialise-in-absence-of-dx9-s.patch

# %%{arm}:
# https://bugzilla.redhat.com/show_bug.cgi?id=1627625
# %%{ix86}
# https://bugzilla.redhat.com/show_bug.cgi?id=1884122
ExcludeArch:    %{arm} %{ix86}

BuildRequires:  asio-static
BuildRequires:  expat-devel
BuildRequires:  flac-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  jack-audio-connection-kit
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libzstd-devel
BuildRequires:  lua-devel >= 5.3.0
BuildRequires:  make
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=91420
%ifarch riscv64
BuildRequires:  mold
%endif
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
BuildRequires:  pugixml-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  qt6-qtbase-devel
BuildRequires:  rapidjson-devel
BuildRequires:  SDL3_ttf-devel
BuildRequires:  sqlite-devel
BuildRequires:  utf8proc-devel
BuildRequires:  zlib-devel
Requires:       %{name}-data = %{version}-%{release}

Provides:       bundled(asmjit) = 1.20
#bx and bgfx are not made to be linked to dynamically as per http://forums.bannister.org/ubbthreads.php?ubb=showflat&Number=104437
Provides:       bundled(bgfx)
Provides:       bundled(bimg)
Provides:       bundled(bx)
#fedora contains linenoise package but it is not compatible
Provides:       bundled(linenoise)
#Below have no fedora packages ATM and are very tiny
Provides:       bundled(lsqlite3)
#check if lua can be unbundled
Provides:       bundled(lua) = 5.4.7
Provides:       bundled(luafilesystem)
Provides:       bundled(lua-linenoise)
Provides:       bundled(lua-zlib)
#lzma is not made to be linked dynamically
Provides:       bundled(lzma-sdk) = 23.01
#minimp3 is just two header files
Provides:       bundled(minimp3)
#softfloat is not made to be linked dynamically
Provides:       bundled(softfloat)


%description
MAME stands for Multiple Arcade Machine Emulator.  When used in conjunction
with an arcade game's data files (ROMs), MAME will more or less faithfully
reproduce that game on a PC.

The ROM images that MAME utilizes are "dumped" from arcade games' original
circuit-board ROM chips.  MAME becomes the "hardware" for the games, taking
the place of their original CPUs and support chips.  Therefore, these games
are NOT simulations, but the actual, original games that appeared in arcades.

MAME's purpose is to preserve these decades of video-game history.  As gaming
technology continues to rush forward, MAME prevents these important "vintage"
games from being lost and forgotten.  This is achieved by documenting the
hardware and how it functions, thanks to the talent of programmers from the
MAME team and from other contributors.  Being able to play the games is just
a nice side-effect, which doesn't happen all the time.  MAME strives for
emulating the games faithfully.

%package tools
Summary:        Additional tools for MAME
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
%{summary}.

%package data
Summary:        Data files used by MAME

BuildArch:      noarch

%description data
%{summary}.

%package data-software-lists
Summary:        Software lists used by MAME
Requires:       %{name}-data = %{version}-%{release}

BuildArch:      noarch

%description data-software-lists
%{summary}. These are split from the main -data
subpackage due to relatively large size.

%package doc
Summary:        Documentation for MAME

BuildArch:      noarch

%description doc
HTML documentation for MAME.


%prep
%autosetup -n %{name}-%{name}0%{baseversion} -p1

#remove system libs or document themes to ensure system ones are used
#remove 3rdparty code not needed on Linux
rm -rf \
    3rdparty/asio \
    3rdparty/compat \
    3rdparty/dxsdk \
    3rdparty/expat \
    3rdparty/glm \
    3rdparty/flac \
    3rdparty/libjpeg \
    3rdparty/portaudio \
    3rdparty/portmidi \
    3rdparty/pugixml \
    3rdparty/rapidjson \
    3rdparty/sqlite3 \
    3rdparty/tap-windows6 \
    3rdparty/utf8proc \
    3rdparty/zlib \
    3rdparty/zstd \
    docs/themes

install -pm 644 %{SOURCE1} whatsnew_0%{baseversion}.txt

# Create ini files
# mame.ini
cat > %{name}.ini << EOF
# Define core search paths
homepath                  \$XDG_CONFIG_HOME/%{name};\$HOME/.config/%{name}
rompath                   %{_datadir}/%{name}/roms;%{_datadir}/%{name}/chds;\$XDG_DATA_HOME/%{name}/roms;\$HOME/.local/share/%{name}/roms;\$XDG_DATA_HOME/%{name}/chds;\$HOME/.local/share/%{name}/chds
hashpath                  %{_datadir}/%{name}/hash
samplepath                %{_datadir}/%{name}/samples
artpath                   %{_datadir}/%{name}/artwork;%{_datadir}/%{name}/effects
ctrlrpath                 %{_datadir}/%{name}/ctrlr
inipath                   \$XDG_CONFIG_HOME/%{name};\$HOME/.config/%{name};\$HOME/.%{name}/ini;%{_sysconfdir}/%{name}
fontpath                  %{_datadir}/%{name}/fonts
cheatpath                 %{_datadir}/%{name}/cheat
crosshairpath             %{_datadir}/%{name}/crosshair
pluginspath               %{_datadir}/%{name}/plugins
languagepath              %{_datadir}/%{name}/language
swpath                    %{_datadir}/%{name}/software

# Set core output paths for local storage
cfg_directory             \$XDG_CONFIG_HOME/%{name}/cfg;\$HOME/.config/%{name}/cfg;\$HOME/.%{name}/cfg
nvram_directory           \$XDG_STATE_HOME/%{name}/nvram;\$HOME/.local/state/%{name}/nvram;\$HOME/.%{name}/nvram
input_directory           \$XDG_CONFIG_HOME/%{name}/inp;\$HOME/.config/%{name}/inp;\$HOME/.%{name}/inp
state_directory           \$XDG_STATE_HOME/%{name}/sta;\$HOME/.local/state/%{name}/sta;\$HOME/.%{name}/sta
snapshot_directory        \$XDG_STATE_HOME/%{name}/snap;\$HOME/.local/state/%{name}/snap;\$HOME/.%{name}/snap
diff_directory            \$XDG_CONFIG_HOME/%{name}/diff;\$HOME/.config/%{name}/diff;\$HOME/.%{name}/diff
comment_directory         \$XDG_CONFIG_HOME/%{name}/comments;\$HOME/.config/%{name}/comments;\$HOME/.%{name}/comments
share_directory           \$XDG_DATA_HOME/%{name}/share;\$HOME/.local/share/%{name}/share;\$HOME/.%{name}/share

# Define bgfx path
bgfx_path                 %{_datadir}/%{name}/bgfx

# Fedora custom defaults
autosave           1
EOF

# ui.ini
cat > ui.ini << EOF
# Define ui search paths
historypath               %{_datadir}/%{name}/history;%{_datadir}/%{name}/dats;\$XDG_DATA_HOME/%{name}/history;\$HOME/.local/share/%{name}/history;\$XDG_DATA_HOME/%{name}/dats;\$HOME/.local/share/%{name}/dats
categorypath              %{_datadir}/%{name}/folders;\$XDG_DATA_HOME/%{name}/folders;\$HOME/.local/share/%{name}/folders
cabinets_directory        %{_datadir}/%{name}/cabinets;%{_datadir}/%{name}/cabdevs;\$XDG_DATA_HOME/%{name}/cabinets;\$HOME/.local/share/%{name}/cabinets;\$XDG_DATA_HOME/%{name}/cabdevs;\$HOME/.local/share/%{name}/cabdevs
cpanels_directory         %{_datadir}/%{name}/cpanel;\$XDG_DATA_HOME/%{name}/cpanel;\$HOME/.local/share/%{name}/cpanel
pcbs_directory            %{_datadir}/%{name}/pcb;\$XDG_DATA_HOME/%{name}/pcb;\$HOME/.local/share/%{name}/pcb
flyers_directory          %{_datadir}/%{name}/flyers;\$XDG_DATA_HOME/%{name}/flyers;\$HOME/.local/share/%{name}/flyers
titles_directory          %{_datadir}/%{name}/titles;\$XDG_DATA_HOME/%{name}/titles;\$HOME/.local/share/%{name}/titles
ends_directory            %{_datadir}/%{name}/ends;\$XDG_DATA_HOME/%{name}/ends;\$HOME/.local/share/%{name}/ends
marquees_directory        %{_datadir}/%{name}/marquees;\$XDG_DATA_HOME/%{name}/marquees;\$HOME/.local/share/%{name}/marquees
artwork_preview_directory %{_datadir}/%{name}/"artwork preview";%{_datadir}/%{name}/artpreview;\$XDG_DATA_HOME/%{name}/"artwork preview";\$HOME/.local/share/%{name}/"artwork preview";\$XDG_DATA_HOME/%{name}/artpreview;\$HOME/.local/share/%{name}/artpreview
bosses_directory          %{_datadir}/%{name}/bosses;\$XDG_DATA_HOME/%{name}/bosses;\$HOME/.local/share/%{name}/bosses
logos_directory           %{_datadir}/%{name}/logo;\$XDG_DATA_HOME/%{name}/logo;\$HOME/.local/share/%{name}/logo
scores_directory          %{_datadir}/%{name}/scores;\$XDG_DATA_HOME/%{name}/scores;\$HOME/.local/share/%{name}/scores
versus_directory          %{_datadir}/%{name}/versus;\$XDG_DATA_HOME/%{name}/versus;\$HOME/.local/share/%{name}/versus
gameover_directory        %{_datadir}/%{name}/gameover;\$XDG_DATA_HOME/%{name}/gameover;\$HOME/.local/share/%{name}/gameover
howto_directory           %{_datadir}/%{name}/howto;\$XDG_DATA_HOME/%{name}/howto;\$HOME/.local/share/%{name}/howto
select_directory          %{_datadir}/%{name}/select;\$XDG_DATA_HOME/%{name}/select;\$HOME/.local/share/%{name}/select
icons_directory           %{_datadir}/%{name}/icons;\$XDG_DATA_HOME/%{name}/icons;\$HOME/.local/share/%{name}/icons
covers_directory          %{_datadir}/%{name}/covers;\$XDG_DATA_HOME/%{name}/covers;\$HOME/.local/share/%{name}/covers
ui_path                   \$XDG_CONFIG_HOME/%{name}/ui;\$HOME/.config/%{name}/ui;\$HOME/.%{name}/ui
EOF

#ensure genie uses $RPM_OPT_FLAGS and $RPM_LD_FLAGS
sed -i "s@-Wall -Wextra -Os \$(MPARAM)@$RPM_OPT_FLAGS@" 3rdparty/genie/build/gmake.linux/genie.make
sed -i "s@-s -rdynamic@$RPM_LD_FLAGS -rdynamic@" 3rdparty/genie/build/gmake.linux/genie.make

%build
#standard -g caused problems with OOM or relocation overflows
RPM_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed "s@-g@-g1@")
#disable -D_GLIBCXX_ASSERTIONS as it causes issues and friction with upstream
#1st issue
#https://bugzilla.redhat.com/show_bug.cgi?id=1927012
#https://github.com/mamedev/mame/issues/7760
#2nd issue
#https://github.com/mamedev/mame/issues/7967
#3rd issue
#https://bugzilla.redhat.com/show_bug.cgi?id=1970764
#https://github.com/mamedev/mame/issues/8186
#4th issue
#https://bugzilla.redhat.com/show_bug.cgi?id=2035572
#FPC guidelines exception request
#https://pagure.io/packaging-committee/issue/1075
RPM_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed "s@ -Wp,-D_GLIBCXX_ASSERTIONS@@")

# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=91420
%ifarch riscv64
RPM_LD_FLAGS+=" -fuse-ld=mold"
%endif

#mame fails to build with LTO enabled
#according to upstream LTO would not help much anyway:
#https://github.com/mamedev/mame/issues/7046
%define _lto_cflags %{nil}

%make_build \
%if %{with debug}
    DEBUG=1 \
%endif
    NOWERROR=1 \
    OPTIMIZE=2 \
    OSD=sdl3 \
    PYTHON_EXECUTABLE=python3 \
    QT_HOME=%{_libdir}/qt6 \
    VERBOSE=1 \
    USE_SYSTEM_LIB_ASIO=1 \
    USE_SYSTEM_LIB_EXPAT=1 \
    USE_SYSTEM_LIB_FLAC=1 \
    USE_SYSTEM_LIB_GLM=1 \
    USE_SYSTEM_LIB_JPEG=1 \
    USE_SYSTEM_LIB_PORTAUDIO=1 \
    USE_SYSTEM_LIB_PORTMIDI=1 \
    USE_SYSTEM_LIB_PUGIXML=1 \
    USE_SYSTEM_LIB_RAPIDJSON=1 \
    USE_SYSTEM_LIB_SQLITE3=1 \
    USE_SYSTEM_LIB_UTF8PROC=1 \
    USE_SYSTEM_LIB_ZLIB=1 \
    USE_SYSTEM_LIB_ZSTD=1 \
    USE_WAYLAND=1 \
    SDL_INI_PATH="%{_sysconfdir}/%{name};" \
    TOOLS=1 \
    LDOPTS="$RPM_LD_FLAGS" \
    OPT_FLAGS="$RPM_OPT_FLAGS"

pushd docs
    %make_build html
popd


%install
rm -rf $RPM_BUILD_ROOT

# create directories
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
for folder in cfg comments diff inp ui
do
    install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel/.config/%{name}/$folder
done
for folder in nvram snap sta
do
    install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel/.local/state/%{name}/$folder
done
for folder in chds roms share
do
    install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel/.local/share/%{name}/$folder
done
for folder in artpreview "artwork preview" bosses cabdevs cabinets covers \
    cpanel dats ends flyers folders gameover history howto icons logo marquees \
    pcb scores select titles versus
do
    install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel/.local/share/%{name}/$folder
done

install -d $RPM_BUILD_ROOT%{_bindir}
for folder in artwork bgfx chds cheat crosshair ctrlr effects fonts hash \
    keymaps language plugins roms samples shader software
do
    install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/$folder
done
# This bunch of dirs goes to the same folder that the previous one, but mantain ui ones separated to easy future changes.
for folder in artpreview "artwork preview" bosses cabdevs cabinets covers \
    cpanel dats ends flyers folders gameover history howto icons logo marquees \
    pcb scores select titles versus
do
    install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/$folder
done
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man6

# install files
install -pm 644 %{name}.ini $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -pm 644 ui.ini $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%if %{with debug}
install -pm 755 %{name}d $RPM_BUILD_ROOT%{_bindir}/%{name}d
%else
install -pm 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
%endif
install -pm 755 castool chdman floptool imgtool jedutil ldresample ldverify \
    nltool nlwav pngcmp romcmp unidasm $RPM_BUILD_ROOT%{_bindir}
for tool in regrep split srcclean
do
    install -pm 755 $tool $RPM_BUILD_ROOT%{_bindir}/%{name}-$tool
done
pushd artwork
    find -type d -exec install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/artwork/{} \;
    find -type f -exec install -pm 644 {} $RPM_BUILD_ROOT%{_datadir}/%{name}/artwork/{} \;
popd
pushd bgfx
    find -type d -a ! -wholename \*dx\* -a ! -wholename \*metal\* -exec install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/bgfx/{} \;
    find -type f -a ! -wholename \*dx\* -a ! -wholename \*metal\* -exec install -pm 644 {} $RPM_BUILD_ROOT%{_datadir}/%{name}/bgfx/{} \;
popd
install -pm 644 hash/* $RPM_BUILD_ROOT%{_datadir}/%{name}/hash
install -pm 644 keymaps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/keymaps
pushd language
    find -type d -exec install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/language/{} \;
    find -type f -name \*.mo -exec install -pm 644 {} $RPM_BUILD_ROOT%{_datadir}/%{name}/language/{} \;
    # flag the translation files as %%lang
    grep -r --include=*.po \"Language: | sed -r 's@(.*)/strings\.po:"Language: ([[:alpha:]]{2}(_[[:alpha:]]{2})?)\\n"@%lang(\2) %{_datadir}/%{name}/language/\1@' > ../%{name}.lang
popd
pushd plugins
    find -type d -exec install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/{} \;
    find -type f -exec install -pm 644 {} $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/{} \;
popd
pushd src/osd/modules/opengl
    install -pm 644 shader/*.?sh $RPM_BUILD_ROOT%{_datadir}/%{name}/shader
popd
pushd docs/man
install -pm 644 castool.1 chdman.1 imgtool.1 floptool.1 jedutil.1 ldresample.1 \
    ldverify.1 romcmp.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 mame.6 $RPM_BUILD_ROOT%{_mandir}/man6
popd

#make sure only html documentation is installed
rm -f docs/.buildinfo
rm -rf docs/build/html/_sources

find $RPM_BUILD_ROOT%{_datadir}/%{name} -name LICENSE -exec rm {} \;


%check
./%{name} -validate


%files
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.ini
%config(noreplace) %{_sysconfdir}/%{name}/ui.ini
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/skel/.config/%{name}
%{_sysconfdir}/skel/.local/state/%{name}
%{_sysconfdir}/skel/.local/share/%{name}
%if %{with debug}
%{_bindir}/%{name}d
%else
%{_bindir}/%{name}
%endif
%{_mandir}/man6/mame.6*

%files tools
%{_bindir}/castool
%{_bindir}/chdman
%{_bindir}/floptool
%{_bindir}/imgtool
%{_bindir}/jedutil
%{_bindir}/ldresample
%{_bindir}/ldverify
%{_bindir}/nltool
%{_bindir}/nlwav
%{_bindir}/pngcmp
%{_bindir}/%{name}-regrep
%{_bindir}/romcmp
%{_bindir}/%{name}-split
%{_bindir}/%{name}-srcclean
%{_bindir}/unidasm
%{_mandir}/man1/castool.1*
%{_mandir}/man1/chdman.1*
%{_mandir}/man1/floptool.1*
%{_mandir}/man1/imgtool.1*
%{_mandir}/man1/jedutil.1*
%{_mandir}/man1/ldresample.1*
%{_mandir}/man1/ldverify.1*
%{_mandir}/man1/romcmp.1*

%files data -f %{name}.lang
%doc README.md whatsnew*.txt
%license COPYING docs/legal/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/artwork
%{_datadir}/%{name}/bgfx
%{_datadir}/%{name}/chds
%{_datadir}/%{name}/cheat
%{_datadir}/%{name}/ctrlr
%{_datadir}/%{name}/dats
%{_datadir}/%{name}/effects
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/history
%{_datadir}/%{name}/keymaps
%dir %{_datadir}/%{name}/language
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/roms
%{_datadir}/%{name}/samples
%{_datadir}/%{name}/shader
%{_datadir}/%{name}/software

%files data-software-lists
%{_datadir}/%{name}/hash

%files doc
%doc docs/build/html/*


%changelog
%autochangelog
