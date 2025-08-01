Name: easyrpg-player
Summary: Game interpreter for RPG Maker 2000/2003 and EasyRPG games
URL: https://easyrpg.org

# EasyRPG Player itself is GPLv3+.
# The program's logos are CC-BY-SA 4.0.
# --
# The program makes use of some header-only libraries:
# * dr_wav: Unlicense OR MIT-0
# * nlohmann_json: MIT AND CC0-1.0
# --
# The program bundles several 3rd-party libraries.
#
# FMMidi files - licensed under the 3-clause BSD license:
# - src/midisequencer.cpp
# - src/midisequencer.h
# - src/midisynth.cpp
# - src/midisynth.h
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
License: GPL-3.0-or-later AND CC-BY-SA-4.0 AND (Unlicense OR MIT-0) AND (MIT AND CC0-1.0) AND BSD-3-Clause AND Baekmuk AND LicenseRef-Fedora-Public-Domain AND MIT AND GPL-2.0-or-later WITH Font-exception-2.0

Version: 0.8.1.1
Release: 3%{?dist}

%global repo_owner EasyRPG
%global repo_name Player
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/%{version}/%{repo_name}-%{version}.tar.gz

# Unbundle libraries
Patch2: 0002-unbundle-dr_wav.patch

# Update dr_wav to 0.14, adapting to API changes
# https://github.com/EasyRPG/Player/pull/3456
#
# We don’t need to update the bundled dr_wav since we will not use it, so we
# just cherry-pick the following commits:
#
# Adapt to API changes in dr_wav 0.14
# https://github.com/EasyRPG/Player/pull/3456/commits/4420531dfd1726f8f127800344ae3a31df39a6af
# dr_wav: Conditional support for old dr_wav 0.13.x
# https://github.com/EasyRPG/Player/pull/3456/commits/081a06f22cbcd9e115950f09c3e8f8e2e98f40af
Patch3: 0003-dr_wav-0.14.patch

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
BuildRequires: pkgconfig(liblcf) >= 0.8.1
BuildRequires: pkgconfig(liblhasa)
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxmp)
BuildRequires: pkgconfig(nlohmann_json) >= 3.9.1
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(sdl3)
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
rm src/external/dr_wav.h


%build
%cmake \
	-DPLAYER_BUILD_EXECUTABLE=ON \
	-DPLAYER_BUILD_LIBLCF=OFF \
	-DPLAYER_ENABLE_TESTS=ON \
	-DPLAYER_WITH_LHASA=ON \
	-DPLAYER_TARGET_PLATFORM=SDL3 \
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
* Tue Jul 29 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.1.1-3
- Patch for compatibility with dr_wav 0.14

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8.1.1-1
- Update to v0.8.1.1

* Mon Apr 07 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8.1-1
- Update to v0.8.1
- Drop Patch1 (unbundle picojson - replaced with nlohmann_json upstream)
- Drop Patch3 (unbundle rang - dependency dropped upstream)
- Drop Patch4 (libfmt10 compatibility - backport from this release)

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
