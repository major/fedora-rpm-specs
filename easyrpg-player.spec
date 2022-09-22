Name: easyrpg-player
Summary: Game interpreter for RPG Maker 2000/2003 and EasyRPG games
URL: https://easyrpg.org

# EasyRPG Player itself is GPLv3+.
# --
# The program bundles several 3rd-party libraries.
#
# FMMidi files - licensed under the 3-clause BSD license:
# - src/midisequencer.cpp
# - src/midisequencer.h
# - src/midisynth.cpp
# - src/midisynth.h
#
# dr_wav files - licensed under (Unlicense or MIT-0):
# - src/external/dr_wav.h
# Note that this file is removed and replaced by dr_wav.h provided
# by Fedora's "dr_wav-devel" package. Still, this is a header-only library,
# which means it's statically linked into the resulting executable.
#
# rang files - licensed under the Unlicense:
# - src/external/rang.hpp
#
# PicoJSON is used only for Emscripten builds (and unbundled before build).
# Dirent is used only for MS Windows builds (and unbundled before build).
# --
# The program also uses a couple of 3rd-party fonts. Since those are not
# loaded at runtime, but rather baked into the executable at compile time,
# their licenses are also added to the License tag.
#
# Baekmuk files - licensed under the Baekmuk license:
# - src/resources/shinonome/korean/
#
# Shinonome files - released into the public domain:
# - src/resources/shinonome/
#
# ttyp0 files - licensed under the ttyp0 license,
# a variant of the MIT license:
# - src/resources/ttyp0/
#
# WenQuanYi files - licensed under
# GPLv2-or-later with Font Embedding Exception:
# - src/resources/wenquanyi/
#
# The upstream tarball contains also "Teenyicons", under the MIT license,
# but those are used only for Emscripten builds.
License: GPLv3+ and BSD and Unlicense and (Unlicense or MIT-0) and Baekmuk and Public Domain and MIT and GPLv2+ with exceptions

Version: 0.7.0
Release: 4%{?dist}

%global repo_owner EasyRPG
%global repo_name Player
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/%{version}/%{repo_name}-%{version}.tar.gz

Patch0: 0000-unbundle-dirent.patch
Patch1: 0001-unbundle-picojson.patch
Patch2: 0002-unbundle-dr_wav.patch

BuildRequires: asciidoc
BuildRequires: cmake >= 3.7
BuildRequires: gcc-c++
BuildRequires: make

# This library doesn't have pkgconfig info
BuildRequires: dr_wav-devel

BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(liblcf) >= 0.7.0
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxmp)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(sdl2) >= 2.0.5
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(wildmidi)
BuildRequires: pkgconfig(zlib)


%description
EasyRPG Player is a game interpreter for RPG Maker 2000/2003 and EasyRPG games.

To play a game, run the "%{name}" executable inside
a RPG Maker 2000/2003 game project folder (same place as RPG_RT.exe).


%prep
%setup -q -n %{repo_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# These are all un-bundled and can be removed
rm src/external/dr_wav.h src/external/picojson.h


%build
%cmake \
	-DPLAYER_BUILD_EXECUTABLE=ON \
	-DPLAYER_BUILD_LIBLCF=OFF \
	-DPLAYER_ENABLE_TESTS=ON \
	-DPLAYER_TARGET_PLATFORM=SDL2 \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install


%check
%cmake_build --target check


%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/bash-completion/completions/%{name}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.0-3
- Fix CMake-related build error

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.0-1
- Update to v0.7.0
- Drop Patch2 (install the bash-completion file - merged upstream)
- Drop Patch3 (fix SIGSTKSZ usage - fixed upstream)
- Add Patch2 (unbundle dr_wav)

* Thu Jul 29 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.2.3-4
- Add missing BuildRequires (fixes rhbz#1987433)
- Add Patch3: fix SIGSTKSZ usage

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.2.3-1
- Update to v0.6.2.3
- Drop Patch2 (build static library - now default)
- Drop Patch3 (Freetype & Harfbuzz circular dependency - accepted upstream)
- Drop Patch4 (man page install issues - accepted upstream)
- Cherry-pick an upstream PR for installing the bash-completion file

* Sun Aug 09 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2.1-4
- Add missing (optional) build-time dependency on HarfBuzz

* Fri Aug 07 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2.1-3
- Add a patch to avoid creating libEasyRPG_Player.so
- Switch to BuildRequiring all libraries via pkgconfig()

* Mon Aug 03 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2.1-2
- Add missing BuildRequires on asciidoc (needed for man pages)
- Unbundle PicoJSON and Dirent before build
- Fix building and running tests during %%check

* Fri Jul 31 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2.1-1
- Initial packaging
