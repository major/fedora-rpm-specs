Name: opensurge
Summary: 2D retro platformer inspired by Sonic games

# Most of the game's code is GPLv3.
# There are two files licensed under WTFPL2:
# - src/core/whereami/whereami.c
# - src/core/whereami/whereami.h
License: GPLv3 and WTFPL

Version: 0.6.0.3
Release: 2%{?dist}

URL: https://opensurge2d.org
Source0: https://github.com/alemart/opensurge/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: allegro5-devel
BuildRequires: allegro5-addon-acodec-devel
BuildRequires: allegro5-addon-audio-devel
BuildRequires: allegro5-addon-dialog-devel
BuildRequires: allegro5-addon-image-devel
BuildRequires: allegro5-addon-ttf-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: surgescript-devel

%global fontlist font(roboto)
BuildRequires: fontconfig
BuildRequires: %{fontlist}

Requires: %{name}-data = %{version}-%{release}

%description
Surge the Rabbit is a fun 2D retro platformer inspired by Sonic games,
and a game creation system that lets you unleash your creativity!

Surge the Rabbit is two projects in one: a game
and a game creation system (game engine).


%package data
Summary: Data files for opensurge
BuildArch: noarch

Requires: %{fontlist}

# Most of the game's assets are licensed under CC-BY 4.0.
# Some individual files are licensed under the older CC-BY 3.0,
# but also CC-BY-SA 3.0 and 4.0, CC0, Giftware, MIT, and Public Domain.
#
# There also bundled fonts (three variants of Google Roboto),
# but we un-bundle them, so they don't apply to the License tag here.
#
# For a detailed list, consult src/misc/copyright_data.csv
# inside the source archive.
License: CC-BY and CC-BY-SA and CC0 and Giftware and MIT and Public Domain

%description data
Data files (graphics, music, sounds) required by Open Surge.


%prep
%setup -q


%build
%cmake \
	-DALLEGRO_STATIC=OFF  \
	-DALLEGRO_MONOLITH=OFF  \
	-DGAME_BINDIR="%{_bindir}/" \
	-DGAME_DATADIR="%{_datadir}/%{name}"  \
	-DDESKTOP_INSTALL=ON  \
	-DDESKTOP_ENTRY_PATH="%{_datadir}/applications"  \
	-DDESKTOP_ICON_PATH="%{_datadir}/pixmaps"  \
	-DDESKTOP_METAINFO_PATH="%{_metainfodir}"  \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install

# Remove bundled fonts and replace them with symlinks
for ROBOTO in Black Bold Medium; do
	ln -sf  \
		"$(fc-match -f '%%{file}' "Roboto:${ROBOTO}")"  \
		"%{buildroot}/%{_datadir}/%{name}/fonts/Roboto-${ROBOTO}.ttf"
done

# The licenses are not readable inside the game,
# and since we un-bundle the fonts, we might as well remove their licenses
rm %{buildroot}%{_datadir}/%{name}/licenses/Apache2-license.txt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml


%files
%license licenses/GPL3-license.txt
%license licenses/WTFPL2-license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png


%files data
%license licenses/CC-BY-3.0-legalcode.txt
%license licenses/CC-BY-4.0-legalcode.txt
%license licenses/CC-BY-SA-3.0-legalcode.txt
%license licenses/CC-BY-SA-4.0-legalcode.txt
%license licenses/CC0-1.0-legalcode.txt
%license licenses/Giftware-license.txt
%license licenses/MIT-license.txt
%{_datadir}/%{name}/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0.3-1
- Update to v0.6.0.3

* Fri Sep 16 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0.2-1
- Update to v0.6.0.2

* Sat Sep 10 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0.1-1
- Update to v0.6.0.1

* Fri Sep 02 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0-1
- Update to v0.6.0

* Fri Jul 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.2.1-5
- Fix CMake-related FTBFS

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.2.1-1
- Update to v0.5.2.1

* Tue Jan 26 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.2-1
- Update to v0.5.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.2-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-8
- Update the spec to work properly with CMake out-of-source builds

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-6
- Move the Requires: on fonts from main package to -data subpackage
- Use different %%license files for the main package and -data subpackage

* Tue May 26 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-5
- Unbundle HanYang Gothic A1 fonts
- Use fc-match to find font files instead of relying on hard-coded paths
- Wrap description to 80 chars per line

* Mon Apr 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-4
- Unbundle surgescript
- Drop Source1 (updated CMakeLists.txt) - not needed since
  we no longer link surgescript statically
- Once again correct the License: tag on the -data subpackage
  and add a comment explaining the licensing breakdown
- Add a Provides: bundled() for the HanYang fonts

* Sun Apr 12 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-2
- Correct the License: tag on the -data subpackage
- Unbundle Roboto fonts

* Sat Apr 11 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-1
- Initial packaging
