Name:    dosbox-staging
Version: 0.79.1
Release: %autorelease
Summary: DOS/x86 emulator focusing on ease of use
URL:     https://dosbox-staging.github.io/

# Bundled dependencies bring their licenses with them.
# Breakdown is given here.
#
# src/libs/decoders/std.h is another bundled dependency,
# but apparently not used.
# It is removed in %%prep to be sure.
#
# Main license:      GPL-2.0-or-later
# archive:           Unlicense
# dr_libs:           MIT-0 OR Unlicense
# enet:              MIT
# gulrak-filesystem: MIT
# src/libs/gui_tk:   GPL-3.0-or-later
# libsidplayfp:      GPL-2.0-or-later
# src/lib/loguru:    LicenseRef-Fedora-Public-Domain
# src/lib/ppscale:   Fair
# src/lib/nuked:     LGPL-2.1-or-later
# stb_vorbis:        MIT OR Unlicense
# src/libs/whereami: MIT OR WTFPL
# xxhash.h:          BSD-2-Clause
License: GPL-2.0-or-later AND Unlicense AND (MIT-0 OR Unlicense) AND MIT AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain AND Fair AND LGPL-2.1-or-later AND (MIT OR Unlicense) AND (MIT OR WTFPL) AND BSD-2-Clause

Source: https://github.com/dosbox-staging/dosbox-staging/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/dosbox-staging/dosbox-staging/issues/1993
Patch:  https://github.com/dosbox-staging/dosbox-staging/pull/1999.patch
# This package is a drop-in replacement for dosbox
Provides:  dosbox = %{version}-%{release}
Obsoletes: dosbox < 0.74.4

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: fluidsynth-devel >= 2.0
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: gmock-devel
BuildRequires: gtest-devel
BuildRequires: iir1-devel
BuildRequires: libappstream-glib
BuildRequires: libatomic
BuildRequires: libpng-devel
BuildRequires: libslirp-devel
BuildRequires: make
BuildRequires: meson
BuildRequires: mt32emu-devel
BuildRequires: opusfile-devel
BuildRequires: SDL2-devel >= 2.0.5
BuildRequires: SDL2_net-devel
BuildRequires: speexdsp-devel

Requires: hicolor-icon-theme
Requires: fluid-soundfont-gm

# src/lib/enet
# Based on fork github.com/lsalzman/enet
Provides: bundled(enet)
# src/lib/ghc
Provides: bundled(gulrak-filesystem)
# src/lib/gui_tk
# Not in Fedora, upstream seems to have disappeared completely
Provides: bundled(gui_tk)
# src/lib/loguru
# Not in Fedora, upstream https://github.com/emilk/loguru
Provides: bundled(loguru)
# src/lib/nuked
# Not in Fedora, upstream https://github.com/nukeykt/Nuked-OPL3
Provides: bundled(nuked-opl3)
# src/lib/residfp
# Not the whole library, just the residfp part
Provides: bundled(libsidplayfp)
# src/lib/whereami
# Not in Fedora, upstream https://github.com/gpakosz/whereami
Provides: bundled(gpakosz-whereami)
# src/lib/decoders/archive.h
# Not in Fedora, upstream github.com/voidah/archive
Provides: bundled(archive)
# src/lib/decoders/dr_{flac,mp3,wav}.h
Provides: bundled(dr_libs)
# src/lib/decoders/stb_vorbis.h
Provides: bundled(stb_vorbis)
# src/lib/decoders/xxhash.h
Provides: bundled(xxhash)

# Automated Tests in Bodhi failed the textrel test for i686, see
# https://sourceware.org/annobin/annobin.html/Test-textrel.html
ExcludeArch: %{ix86}

%description
DOSBox Staging is full x86 CPU emulator (independent of host architecture),
capable of running DOS programs that require real or protected mode.

It features built-in DOS-like shell terminal, emulation of several PC variants
(IBM PC, IBM PCjr, Tandy 1000), CPUs (286, 386, 486, Pentium I), graphic
chipsets (Hercules, CGA, EGA, VGA, SVGA), audio solutions (Sound Blaster,
Gravis UltraSound, Disney Sound Source, Tandy Sound System), CD Digital Audio
emulation (also with audio encoded as FLAC, Opus, OGG/Vorbis, MP3 or WAV),
joystick emulation (supports modern game controllers), serial port emulation,
IPX over UDP, GLSL shaders, and more.

DOSBox Staging is highly configurable, well-optimized and fast enough to run
any old DOS game using modern hardware.


%prep
%autosetup -p1
# Remove unused file
rm src/libs/decoders/stb.h


%build
%meson
%meson_build


%install
%meson_install
# Install bash completion files
mkdir -p  %{buildroot}%{_datadir}/bash-completion/completions
cp contrib/linux/bash-completion/dosbox %{buildroot}%{_datadir}/bash-completion/completions


%check
%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml


%files
%license COPYING
%doc AUTHORS README THANKS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/dosbox
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/dosbox-staging.*
%{_metainfodir}/*


%changelog
%autochangelog
