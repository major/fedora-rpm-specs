%global forgeurl https://github.com/sarah-walker-pcem/pcem
%global metadata_forgeurl https://github.com/X-m7/flathub
%global metadata_commit ad9aafaaf2f3c1faccc3a99c11d62daca8520d02

# Relax due to incompatible pointer issues
%global build_type_safety_c 2

Name:           pcem
Version:        17
Release:        %autorelease
Summary:        IBM PC emulator

# PCem itself is GPLv2, the other licenses come from bundled libraries
License:        GPL-2.0-or-later and MIT and BSD-3-Clause
URL:            https://pcem-emulator.co.uk
Source:         %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source:         %{metadata_forgeurl}/archive/%{metadata_commit}/flathub-%{metadata_commit}.tar.gz
# Define HAVE_UNISTD_H in config.h for the benefit of slrip/debug.c
# Already fixed upstream with the switch to CMake
Patch:          pcem-c99.patch
# Workaround Wayland issues by forcing X11 for now
# Backport of https://github.com/sarah-walker-pcem/pcem/pull/222
Patch:          pcem-wayland-hack.patch

# checking for cpu... configure: error: Unsupported CPU.
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    armv7hl i686 ppc64le s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  alsa-lib-devel
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2-devel
BuildRequires:  wxGTK-devel

Requires:       8088_bios
Requires:       xtideuniversalbios

# These projects are bundled, trimmed down and modified
Provides:       bundled(dosbox) = 20140227
Provides:       bundled(minivhd) = 20201114
Provides:       bundled(resid-fp) = 0.16vice
Provides:       bundled(slirp) = 0.9.0

# minivhd itself also bundles modified and trimmed down copies of these
Provides:       bundled(cwalk) = 1.2.1
Provides:       bundled(libxml2) = 20190613

%description
PCem (short for PC Emulator) is an IBM PC emulator that specializes in running
old operating systems and software that are designed for IBM PC compatibles.

%prep
%autosetup -p1 -b 1

# Use our build flags
sed -i configure.ac \
  -e 's:CFLAGS="-O3 -fcommon":CFLAGS="-fcommon %{build_cflags}":' \
  -e 's:CXXFLAGS="-O3 -fcommon":CXXFLAGS="-fcommon %{build_cxxflags}":'
echo 'pcem_LDFLAGS = %{build_ldflags}' >> src/Makefile.am

# Reorganize bundled project licenses
cp -p src/minivhd/CREDITS.md CREDITS.minivhd
cp -p src/minivhd/LICENSE LICENSE.minivhd
cp -p src/resid-fp/COPYING LICENSE.resid-fp
cp -p src/slirp/COPYRIGHT.txt LICENSE.slirp

%build
autoreconf -ivf
%configure --enable-release-build --enable-alsa --enable-networking
%make_build

%install
%make_install

# Install roms
install -Ddpm0755 %{buildroot}%{_datadir}/%{name}/roms/xi8088
ln -s ../../../8088_bios/bios-xi8088.bin %{buildroot}%{_datadir}/%{name}/roms/xi8088/
ln -s ../../xtideuniversalbios/ide_xt.bin %{buildroot}%{_datadir}/%{name}/roms/
ln -s ../../xtideuniversalbios/ide_at.bin %{buildroot}%{_datadir}/%{name}/roms/

# Install desktop files
install -Dpm0644 -t %{buildroot}%{_datadir}/pixmaps \
  ../flathub-%{metadata_commit}/uk.co.pcem_emulator.pcem.svg
desktop-file-install \
  --add-category="System;Emulator" \
  --dir=%{buildroot}%{_datadir}/applications \
  ../flathub-%{metadata_commit}/uk.co.pcem_emulator.pcem.desktop
install -Dpm0644 -t %{buildroot}%{_metainfodir} \
  ../flathub-%{metadata_commit}/uk.co.pcem_emulator.pcem.metainfo.xml

%check
desktop-file-validate \
  %{buildroot}/%{_datadir}/applications/uk.co.pcem_emulator.pcem.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/uk.co.pcem_emulator.pcem.metainfo.xml

%files
%license COPYING CREDITS.minivhd LICENSE.minivhd LICENSE.resid-fp LICENSE.slirp
%doc README.md TESTED.md readme.html tested.html
%{_bindir}/%{name}
%{_datadir}/%{name}/roms/
%{_datadir}/applications/uk.co.pcem_emulator.pcem.desktop
%{_datadir}/pixmaps/uk.co.pcem_emulator.pcem.svg
%{_metainfodir}/uk.co.pcem_emulator.pcem.metainfo.xml

%changelog
%autochangelog
