Name: easyrpg-player
Summary: Game interpreter for RPG Maker 2000/2003 and EasyRPG games
URL: https://easyrpg.org

# EasyRPG Player itself is GPLv3+.
# The program's logos are CC-BY-SA 4.0.
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
# rang files - licensed under the Unlicense:
# - src/external/rang.hpp
# Note that both dr_wav and rang are un-bundled and replaced with versions
# provided by Fedora packages. However, since these are header-only libraries,
# their licenses are still included in the License tag.
#
# PicoJSON is used only for Emscripten builds (and unbundled before build).
# --
# The program also uses a couple of 3rd-party fonts. Since these are not
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
License: GPL-3.0-or-later AND CC-BY-SA-4.0 AND BSD-3-Clause AND (Unlicense OR MIT-0) AND Unlicense AND Baekmuk AND LicenseRef-Fedora-Public-Domain AND MIT AND GPL-2.0-or-later WITH Font-exception-2.0

Version: 0.8
Release: 11%{?dist}

%global repo_owner EasyRPG
%global repo_name Player
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/%{version}/%{repo_name}-%{version}.tar.gz

# Unbundle libraries
Patch1: 0001-unbundle-picojson.patch
Patch2: 0002-unbundle-dr_wav.patch
Patch3: 0003-unbundle-rang.patch

# Fix compilation errors when building against fmt v10
# Backport of upstream commit: https://github.com/EasyRPG/Player/commit/a4672d2e30db4e4918c8f3580236faed3c9d04c1.patch
Patch4: 0004-update-for-fmt10.patch

BuildRequires: cmake >= 3.13
BuildRequires: desktop-file-utils
BuildRequires: fluidsynth
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libappstream-glib
BuildRequires: rubygem-asciidoctor

# This library doesn't have pkgconfig info
# Version 0.13.17 fixes a possible crash when reading from MS-ADPCM encoded
# files; we want this fix since such crashes may represent security issues.
BuildRequires: dr_wav-devel >= 0.13.17

BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(liblcf) >= 0.8
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxmp)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(rang)
BuildRequires: pkgconfig(sdl2) >= 2.0.5
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(wildmidi)
BuildRequires: pkgconfig(zlib)

Requires: hicolor-icon-theme


%description
EasyRPG Player is a game interpreter for RPG Maker 2000/2003 and EasyRPG games.

To play a game, run the "%{name}" executable inside
a RPG Maker 2000/2003 game project folder (same place as RPG_RT.exe).


%prep
%autosetup -n %{repo_name}-%{version} -p1

# These are all un-bundled and can be removed
rm src/external/dr_wav.h src/external/picojson.h src/external/rang.hpp


%build
%cmake \
	-DPLAYER_BUILD_EXECUTABLE=ON \
	-DPLAYER_BUILD_LIBLCF=OFF \
	-DPLAYER_ENABLE_TESTS=ON \
	-DPLAYER_TARGET_PLATFORM=SDL2 \
	-DCMAKE_FIND_PACKAGE_PREFER_CONFIG=OFF \
	-DCMAKE_BUILD_TYPE=Release

%cmake_build
%cmake_build --target man


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%cmake_build --target check


%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8-10
- Rebuilt with dr_wav 0.13.17

* Fri Aug 09 2024 Marcin Radomski <marcin@mradomski.pl> - 0.8-9
- rhbz#2300634: Fix fedpkg build "missing libz.a" error

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8-4
- Add a patch to fix compilation errors when building against fmt10

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8-3
- Rebuilt due to fmt 10 update.

* Sun Jun 04 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8-2
- Unbundle rang

* Tue May 02 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8-1
- Update to v0.8
- Drop Patch0 (unbundle dirent - dependency removed upstream)
- Drop Patch3 (fix GCC13 build errors - merged upstream)
- Convert License tag to SPDX

* Thu Jan 19 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.0-6
- Add a patch to fix build failures under GCC13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
