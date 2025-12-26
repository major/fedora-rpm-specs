%global commit  8d91fbdff8f4db6e256370f030a9f6ac8c7f2c62
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20251216

%global corename pcsx-rearmed
%global filename pcsx_rearmed

Name:           libretro-%{corename}
Version:        15
Release:        0.17.%{date}git%{shortcommit}.%autorelease
Summary:        ARM optimized PCSX fork

# Public domain
# ----------------------------
# deps/flac-1.3.2/
# deps/lzma-16.04/
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# deps/flac-1.3.2/
# deps/libchdr/
#
# Expat License
# -------------
# frontend/vita/
# libretro-common/
# plugins/dfsound/
#
# GNU General Public License
# --------------------------
# deps/flac-1.3.2/
#
# GNU General Public License (v2 or later)
# ----------------------------------------
# frontend/cspace_arm.S
# libpcsxcore/gte_arm.S
# plugins/dfxvideo/draw_pl.c
#
# GNU Lesser General Public License (v2 or later)
# -----------------------------------------------
# deps/flac-1.3.2/include/share/getopt.h
#
# GNU Lesser General Public License (v2.1 or later)
# -------------------------------------------------
# deps/flac-1.3.2/include/share/grabbag.h
#
# GPL (v2 or later)
# -----------------
# deps/flac-1.3.2/include/share/grabbag/picture.h
# libpcsxcore/cdriso.c
# plugins/gpu_neon/psx_gpu/vector_ops.h
#
# Automatically converted from old format: GPLv2 and Public Domain and BSD and MIT - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT

URL:            https://github.com/libretro/pcsx_rearmed
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{filename}.libretro
ExcludeArch:    armv7hl

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  pkgconfig(zlib)

Supplements:    gnome-games
Supplements:    retroarch

# All hardcoded
#   * https://github.com/libretro/pcsx_rearmed/blob/3558dd33fb337a29fb6c57a5e88a473153e6202e/Makefile#L219
Provides:       bundled(crypto)
Provides:       bundled(flac) = 1.3.2
Provides:       bundled(libchdr)
Provides:       bundled(lzma) = 22.01

%description
PCSX ReARMed is yet another PCSX fork based on the PCSX-Reloaded project, which
itself contains code from PCSX, PCSX-df and PCSX-Revolution. This version was
originally ARM architecture oriented (hence the name) with its MIPS->ARM dynamic
recompilation and assembly optimizations, but more recently it targets other
architectures too. A fork of this emulator was used in PS Classic (without any
coordination or even notification).


%prep
%autosetup -n %{filename}-%{commit}

# wrong-file-end-of-line-encoding
sed -i 's/\r$//' ChangeLog


%build
%set_build_flags
%make_build -f Makefile.libretro \
    GIT_VERSION=%{shortcommit}   \
    HAVE_CHD=1                   \
    WANT_ZLIB=0                  \
    %{nil}


%install
install -Dpm 0755 %{filename}_libretro.so %{buildroot}%{_libdir}/libretro/%{filename}_libretro.so
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{filename}.libretro


%files
%license COPYING
%doc README.md AUTHORS NEWS ChangeLog
%{_libdir}/libretro/


%changelog
%autochangelog
