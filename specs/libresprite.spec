Name: libresprite
%global rtld_name io.github.libresprite.libresprite

Summary: Pixel art editor

# * LibreSprite itself is mostly GPLv2, with some parts being MIT:
#   - src/base/
#   - src/cfg/
#   - src/clip/
#   - src/css/
#   - src/doc/
#   - src/flic/
#   - src/ft/
#   - src/gen/
#   - src/gfx/
#   - src/net/
#   - src/render/
#   - src/script/
#   - src/she/
#   - src/undo/
#   - src/ui/
# * Bundled Delta (third_party/delta/) is MIT.
# * Bundled EasyTab (third_party/EasyTab/) is Unlicense.
# * Bundled MODP_B64 (third_party/modp_b64/) is BSD-3-Clause.
# * Bundled observable (third_party/observable/) is MIT.
# * Bundled quickjs (third_party/quickjs-amalgam/) is MIT.
# It also uses simpleini and qoi, which are static libraries subject to MIT.
License: GPL-2.0-only AND MIT AND Unlicense BSD-3-Clause

Version: 1.3
Release: 1%{?dist}

URL: https://github.com/LibreSprite/LibreSprite
Source0: %{URL}/archive/v%{version}/LibreSprite-v%{version}.tar.gz

# Build with system-provided simpleini.
Patch0: 0000-unbundle-libs.patch

# Add missing licensing info for the "Delta" library.
# https://github.com/LibreSprite/LibreSprite/commit/aac462b406818c2e827dcb89da9536ff2dec9a2b
Patch1: 0001-Delta-license.txt

# LibreSprite is a fork of Aseprite, made from the last GPLv2 commit before
# Aseprite became closed source. The original Aseprite split some of its code
# out into reusable components. With LibreSprite, most of those components are
# now part of the main repo, but some are still pulled in via git submodules.
# We need to download and unpack those separately.

%global flic_commit 876ef60df5fec606f8eb0638ee893e4967db4673
Source11: https://github.com/aseprite/flic/archive/%{flic_commit}/flic-%{flic_commit}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib

# CMakeLists check for these...
BuildRequires: cmake(PNG)
BuildRequires: cmake(SDL2)
BuildRequires: cmake(SimpleIni)
BuildRequires: cmake(tinyxml2)
BuildRequires: cmake(WebP)
BuildRequires: cmake(zlib)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: giflib-devel

# ...and these are just #include'd without checking anything.
BuildRequires: libXi-devel
BuildRequires: qoi-devel

%global fontlist font(notosans) font(notosansjp) font(notosanskr) font(notosanssc) font(notokufiarabic)
BuildRequires: fontconfig
BuildRequires: %{fontlist}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Requires: %{name}-data = %{version}-%{release}

Provides: bundled(EasyTab)
Provides: bundled(modp_b64) = 1.3
Provides: bundled(observable)

# Fedora does not package quickjs. It does package quickjs-ng, but that cannot
# be used here, as there are some API differences between the two.
Provides: bundled(quickjs) = 0.11.0

%global licensedir %{_defaultlicensedir}/%{name}

%description
LibreSprite lets you create 2D animations for videogames.
From sprites, to pixel-art, retro style graphics,
and whatever else you like about the 8-bit (and 16-bit) era.


%package data
Summary: Data files for LibreSprite

Requires: %{fontlist}
Requires: hicolor-icon-theme

BuildArch: noarch

%description data
This package contains data (fonts, translations, widgets, et cetera)
required for LibreSprite to work correctly.


%prep
%autosetup -N -n LibreSprite-%{version}
pushd src
	rm -rf flic
	tar xzf %{SOURCE11}
	mv flic-%{flic_commit} flic
popd
%autopatch -p1

# Replace bundled qoi with system-provided one
ln -sf %{_includedir}/qoi.h third_party/qoi/qoi.h


%build
%cmake \
	-DWITH_WEBP_SUPPORT=ON \
	-DWITH_DESKTOP_INTEGRATION=ON \
	-DUSE_SDL2_BACKEND=ON
%cmake_build


%install
%cmake_install

# Remove bundled fonts and replace them with symlinks.
FONTDIR="%{buildroot}%{_datadir}/%{name}/data/fonts"
ln -srf "%{buildroot}$(fc-match -f '%%{file}' "Noto Kufi Arabic")" "${FONTDIR}/font-ar.ttf"
ln -srf "%{buildroot}$(fc-match -f '%%{file}' "Noto Sans JP")"     "${FONTDIR}/font-jp.ttf"
ln -srf "%{buildroot}$(fc-match -f '%%{file}' "Noto Sans KR")"     "${FONTDIR}/font-kr.ttf"
ln -srf "%{buildroot}$(fc-match -f '%%{file}' "Noto Sans SC")"     "${FONTDIR}/font-zh.ttf"
ln -srf "%{buildroot}$(fc-match -f '%%{file}' "Noto Sans")"        "${FONTDIR}/font.ttf"
rm "${FONTDIR}/OFL.txt"

# Install the license files and documentation.
# This is done manually so the files end up in libresprite/ directory
# despite being part of libresprite-data package.
install -m 755 -d %{buildroot}%{licensedir}
install -m 644 -p LICENSE.txt                   %{buildroot}%{licensedir}/LibreSprite-GPLv2.txt
install -m 644 -p docs/licenses/MIT.txt         %{buildroot}%{licensedir}/LibreSprite-MIT.txt
install -m 644 -p third_party/delta/LICENSE.txt %{buildroot}%{licensedir}/delta.txt
install -m 644 -p third_party/EasyTab/LICENSE   %{buildroot}%{licensedir}/EasyTab.txt
install -m 644 -p third_party/modp_b64/LICENSE  %{buildroot}%{licensedir}/modp_b64.txt

install -m 755 -d %{buildroot}%{_pkgdocdir}
install -m 644 -t %{buildroot}%{_pkgdocdir}/ -p README.md
cp -t %{buildroot}%{_pkgdocdir}/ -a docs/files


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml


%files
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/aseprite.xml
%{_datadir}/thumbnailers/
%{_metainfodir}/%{rtld_name}.metainfo.xml

%files data
%license %{licensedir}
%doc %{_pkgdocdir}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/**/apps/%{name}.png


%changelog
* Sat Nov 14 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.3-1
- Update to v1.3

* Thu Oct 29 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2-2
- Fix license tag (missing "AND")

* Tue Sep 22 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2-1
- Update to v1.2

* Sat Jul 28 2018 Artur Iwicki <fedora@svgames.pl> - 1.0-1
- Initial packaging
