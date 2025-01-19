Name: dsda-doom
Summary: Speedrun-oriented Doom source port

# Most of the files are covered by GPL v2.
# * BSD:
#   - prboom2/src/gl_sky.c
#   - prboom2/src/scanner.cpp
#   - prboom2/src/scanner.h
# * LGPL v2.0 or later:
#   - prboom2/src/umapinfo.cpp
#   - prboom2/src/umapinfo.h
# * LGPL v2.1 or later:
#   - prboom2/src/gl_vertex.c
# * Public domain:
#   - prboom2/src/SDL/SDL_windows_main.c
#   - prboom2/src/md5.c
#   - prboom2/src/md5.h
#   - prboom2/src/win_opendir.c
#   - prboom2/src/win_opendir.h
# * zlib:
#   - prboom2/src/SDL/SDL_windows.h
#
# Note regarding gl_vertex.c: the file has a conditional licensing clause.
# Check the discussion at: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/310
License: GPL-2.0-or-later AND BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND Zlib

Version: 0.28.3
Release: 1%{?dist}

URL: https://github.com/kraflab/dsda-doom
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz

# Fix missing includes.
#
# Submitted upstream: https://github.com/kraflab/dsda-doom/pull/578/
Patch1: 0001-missing-includes.patch

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fluidsynth
BuildRequires: gcc-c++
BuildRequires: libzip-tools
BuildRequires: make
BuildRequires: rubygem-rspec

BuildRequires: dumb-devel
BuildRequires: portmidi-devel

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libpcre2-32)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(SDL2_net)
BuildRequires: pkgconfig(vorbisfile)

Requires: %{name}-data = %{version}-%{release}


%description
DSDA-Doom is a source port of the 1993 classic DOOM game.
DSDA-Doom is a fork of prboom+, with many added features, including:
- In-game console and scripting
- Full controller support
- Palette-based lightmode for opengl
- Debugging features for testing
- Strict mode for speedrunning
- Various quality of life improvements
- Advanced tools for TASing
- Rewind feature


%package data
Summary: Data files for DSDA-Doom
BuildArch: noarch

%description data
This package contains data files needed to run DSDA-Doom.


%prep
%autosetup -p1


%build
pushd prboom2/
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebugInfo \
	-DCMAKE_FIND_PACKAGE_PREFER_CONFIG=OFF \
	-DDOOMWADDIR=%{_datadir}/doom \
	-DDSDAPWADDIR=%{_datadir}/%{name} \

%cmake_build


%install
pushd prboom2/
	%cmake_install
	desktop-file-install --dir=%{buildroot}%{_datadir}/applications ICONS/%{name}.desktop
	install -Dpm 644 ICONS/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
popd

# docs
ln prboom2/AUTHORS ./
install -m 755 -d %{buildroot}%{_pkgdocdir}
cp -a docs patch_notes AUTHORS README.md %{buildroot}%{_pkgdocdir}


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop


%files data
%license prboom2/COPYING
%doc %{_pkgdocdir}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png


%changelog
* Fri Jan 17 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.28.3-1
- Update to v0.28.3

* Thu Jan 16 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.28.2-4
- Fix FTBFS

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 21 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.28.2-2
- Add a patch to fix undefined behaviour (rhbz#2333687)

* Mon Oct 28 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.28.2-1
- Update to v0.28.2

* Sun Aug 18 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.28.1-1
- Update to v0.28.1

* Sun Aug 11 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.28.0-1
- Update to v0.28.0

* Mon Jan 29 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.27.5-1
- Update to v0.27.5

* Sun Nov 19 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.27.4-1
- Update to v0.27.4

* Tue Nov 14 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.27.3-1
- Update to v0.27.3

* Mon Oct 30 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.27.2-1
- Update to v0.27.2

* Sat Oct 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.27.0-1
- Update to v0.27.0
- Move data to a subpackage

* Sun Jun 04 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.26.2-1
- Update to v0.26.2

* Tue May 30 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.26.0-1
- Update to v0.26.0

* Mon Apr 03 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.25.6-1
- Update to v0.25.6
- Review license tag and migrate to SPDX
- Include the docs in the package

* Wed Jan 11 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.25.4-1
- Initial packaging
