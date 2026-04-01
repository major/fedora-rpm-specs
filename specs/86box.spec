Name:		86box
Version:	5.3
Release:	%autorelease
Summary:	Classic PC emulator
# The source tree contains files under various licenses.
# License breakdown based on licensecheck output:
# - GPL-2.0-only: COPYING, cassette.c, some other files.
# - GPL-2.0-or-later: majority of project files (including those without explicit headers).
# - BSD-3-Clause: nvr.c, crcspeed (majority), isartc.c, fdc_pii15xb.c, network, printer, softfloat3e, ymfm, gamemode_client.h, munt/sha1.
# - MIT: cJSON, minitrace, minivhd, ayumi.
# - Zlib: crcspeed.c.
# - BSD-2-Clause: getline.c.
# - (BSD-2-Clause OR GPL-2.0-or-later): lzf.h.
# - LGPL-2.0-or-later: fpu_trans.h, poly.h.
# - Khronos License (for Vulkan headers) is not included because those headers are not shipped in the binary package.
License: GPL-2.0-only AND GPL-2.0-or-later AND BSD-3-Clause AND MIT AND Zlib AND BSD-2-Clause AND (BSD-2-Clause OR GPL-2.0-or-later) AND LGPL-2.0-or-later
URL:		https://86box.net

Source0:	https://github.com/86Box/86Box/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: fluidsynth-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: libFAudio-devel
BuildRequires: libappstream-glib
BuildRequires: libatomic
BuildRequires: libevdev-devel
BuildRequires: libserialport-devel
BuildRequires: libslirp-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXi-devel
BuildRequires: ninja-build
BuildRequires: openal-soft-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: rtmidi-devel
BuildRequires: wayland-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-ng-compat-devel

Requires: hicolor-icon-theme
Recommends: fluid-soundfont-gm
Recommends: gamemode

Patch1: 01-fallthrough-fix.patch
Patch2: 02-png-module-fix.patch


Provides: bundled(cJSON)
Provides: bundled(minivhd)
Provides: bundled(softfloat3e)
Provides: bundled(ayumi)
Provides: bundled(munt)
Provides: bundled(resid-fp)
Provides: bundled(ymfm)
Provides: bundled(lzf)
Provides: bundled(minitrace)

%description
86Box is a hypervisor and IBM PC system emulator that specializes in
running old operating systems and software designed for IBM
PC systems and compatibles from 1981 through fairly recent
system designs based on the PCI bus.

It supports various models of PCs, graphics and sound cards, and CPUs.

%prep
%autosetup -p1 -n 86Box-%{version}

%build
%ifarch x86_64
  %cmake -DRELEASE=on -DUSE_QT6=on
%else
  %ifarch %{arm32} aarch64
    %cmake -DRELEASE=on -DNEW_DYNAREC=on -DUSE_QT6=on
  %else
    %cmake -DRELEASE=on -DDYNAREC=off -DUSE_QT6=on
  %endif
%endif
%cmake_build

%install
# install base package
%cmake_install

# install icons
for i in 48 64 72 96 128 192 256 512; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  cp -p src/unix/assets/${i}x${i}/net.86box.86Box.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
done

# install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications src/unix/assets/net.86box.86Box.desktop

# install metadata
mkdir -p %{buildroot}%{_metainfodir}
cp -p src/unix/assets/net.86box.86Box.metainfo.xml %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/net.86box.86Box.metainfo.xml

%files
%license COPYING
%license src/sound/ayumi/LICENSE
%license src/cpu/softfloat3e/COPYING.txt
%doc README.md README-UNIX-MODE-WITH-OSD.txt SECURITY.md
%{_bindir}/86Box
%{_datadir}/applications/net.86box.86Box.desktop
%{_metainfodir}/net.86box.86Box.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/net.86box.86Box.png

%changelog
%autochangelog
