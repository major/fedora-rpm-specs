%global forgeurl https://github.com/tildearrow/furnace
Version:        0.6.8.3
%forgemeta

Name:           furnace
Release:        %autorelease
Summary:        a multi-system chiptune tracker compatible with DefleMask modules

# The applications is mainly under GPL-2.0-or-later license, except the bundled libraries:
# SAASound - BSD-3-Clause
# vgsound_emu-modified - ZLib
# adpcm - Unlicense
# opn - LGPL-2.1-or-later
# Nuked-PSG - GPL-2.0-only
# opm - LGPL-2.1-or-later
# Nuked-OPLL - GPL-2.0-or-later
# opl - LGPL-2.1-or-later
# YM3812-LLE - GPL-2.0-or-later
# ESFMu - LGPL-2.1-or-later
# pwrnoise - MIT
# adpcm-xq - BSD-3-Clause
License:        GPL-2.0-or-later AND BSD-3-Clause AND Zlib AND Unlicense AND LGPL-2.1-or-later AND GPL-2.0-only AND MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
# download adpcm bundled library from the specfic commit
Source1:        https://github.com/superctr/adpcm/archive/ef7a217154badc3b99978ac481b268c8aab67bd8.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(sdl2)

BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
%{summary}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
This package contains documentation for %{name}.

%prep
%autosetup -p1

tar xf %{SOURCE1} -C extern/adpcm --strip-components=1

%build
%cmake -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_FREETYPE=ON \
    -DSYSTEM_FFTW=ON \
    -DSYSTEM_FMT=ON \
    -DSYSTEM_FREETYPE=ON \
    -DSYSTEM_LIBSNDFILE=ON \
    -DSYSTEM_PORTAUDIO=ON \
    -DSYSTEM_RTMIDI=ON \
    -DSYSTEM_ZLIB=ON \
    -DSYSTEM_SDL2=ON

%cmake_build

%install
%cmake_install
%find_lang furnace

rm -r %{buildroot}%{_datadir}/icons/hicolor/1024x1024

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f furnace.lang
%license LICENSE
%{_bindir}/furnace
%{_datadir}/applications/furnace.desktop
%{_datadir}/icons/hicolor/*/apps/furnace.png
%dir %{_datadir}/furnace
%{_datadir}/furnace/instruments/
%{_datadir}/furnace/wavetables/
%{_datadir}/mime/packages/furnace.xml

%files doc
%{_datadir}/doc/furnace/

%changelog
%autochangelog
