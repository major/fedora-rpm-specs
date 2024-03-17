# src/types.h is set to issue error on i386 and warning on other architectures
# when trying to enable position-independent code. It is not recommended for
# performance reasons
%undefine _hardened_build

%global unstable 1

Name:           mednafen
Version:        1.32.0
%if %{unstable} == 1
Release:        %autorelease -p -e UNSTABLE
%else
Release:        %autorelease
%endif
Summary:        A multi-system emulator utilizing OpenGL and SDL
#mednafen incorporates several emulators hence the colourful licensing
License:        GPLv2+ and BSD and ISC and LGPLv2+ and MIT and zlib 
URL:            https://mednafen.github.io/
%if %{?unstable} == 1
Source0:        https://mednafen.github.io/releases/files/%{name}-%{version}-UNSTABLE.tar.xz
%else
Source0:        https://mednafen.github.io/releases/files/%{name}-%{version}.tar.xz
%endif

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libmpcdec-devel
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac) => 1.3.0
BuildRequires:  pkgconfig(jack) => 1.0.2
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(sdl2) => 2.0.5
BuildRequires:  pkgconfig(zlib)

%description
A portable, utilizing OpenGL and SDL, argument(command-line)-driven multi-system
emulator. Mednafen has the ability to remap hotkey functions and virtual system
inputs to a keyboard, a joystick, or both simultaneously. Save states are
supported, as is real-time game rewinding. Screen snapshots may be taken, in the
PNG file format, at the press of a button. Mednafen can record audiovisual
movies in the QuickTime file format, with several different lossless codecs
supported.

The following systems are supported(refer to the emulation module documentation
for more details):

* Apple II/II+
* Atari Lynx
* Neo Geo Pocket (Color)
* WonderSwan
* GameBoy (Color)
* GameBoy Advance
* Nintendo Entertainment System
* Super Nintendo Entertainment System/Super Famicom
* Virtual Boy
* PC Engine/TurboGrafx 16 (CD)
* SuperGrafx
* PC-FX
* Sega Game Gear
* Sega Genesis/Megadrive
* Sega Master System
* Sega Saturn (experimental, x86_64 only)
* Sony PlayStation

Due to the threaded model of emulation used in Mednafen, and limitations of SDL,
a joystick is preferred over a keyboard to play games, as the joystick will have
slightly less latency, although the latency differences may not be perceptible
to most people. 


%prep
%autosetup -p1 -n %{name}

# Permission cleanup
find \( -name \*.c\* -or -name \*.h\* -or -name \*.inc \) -exec chmod -x {} \;


%build
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful in pure
# LTO mode.  We can use -ffat-lto-objects to force code generation.
#
# -ffat-lto-objects is the default for F33, but is expected to be removed
# in F34.  So we list it explicitly here.
%define _lto_cflags -flto=auto -ffat-lto-objects

CFLAGS="$RPM_OPT_FLAGS -Wl,-z,relro -Wl,-z,now"
CXXFLAGS="$RPM_OPT_FLAGS -Wl,-z,relro -Wl,-z,now"

export CFLAGS
export CXXFLAGS

%configure --disable-rpath \
    --with-external-lzo \
    --with-external-mpcdec

#to be added once dependencies become available
#    --with-external-tremor
#    --with-external-trio
%make_build


%install
%make_install

# Documentation cleanup
rm -rf Documentation/*.def Documentation/*.php Documentation/generate.sh \
    Documentation/Makefile.* Documentation/docgen.inc

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc ChangeLog TODO Documentation/*
%{_bindir}/%{name}


%changelog
%autochangelog
