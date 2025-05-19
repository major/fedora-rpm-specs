%bcond_with debug

# Workaround for rhbz#2044028
%undefine _package_note_file

Name:          crawl
Summary:       Roguelike dungeon exploration game
Version:       0.33.0
Release:       %autorelease
# Main license : GPLv2+
# 2-clause BSD: all contributions by Steve Noonan and Jesse Luehrs
# Public Domain|CC0: most of tiles, perlin.cc, perlin.h
# The majority of Crawl's tiles and artwork are released under the CC0 license
# MIT: json.cc and worley.cc
# ASL 2.0: pcg.cc 
## According to the 'license.txt' file,
## This program can be redistribute under GPLv2+ license; MIT and BSD are GPL compatible.
License:       GPL-2.0-or-later AND Apache-2.0 AND BSD-2-Clause AND CC0-1.0
URL:           https://crawl.develz.org/
Source0:       https://github.com/%{name}/%{name}/archive/%{name}/%{name}-%{version}.tar.gz

## These patches fix installation paths
Patch0:        %{name}_bin.patch
Patch1:        %{name}_tiles.patch
Patch2:        %{name}-rltiles_cflags.patch

# See https://github.com/crawl/crawl/issues/1372
Patch3:        %{name}-add_iswalnum_reference.patch

Patch4:        %{name}-use_lua5.patch

BuildRequires: advancecomp
BuildRequires: bison
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: flex
BuildRequires: fdupes
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(lua-5.1)
#BuildRequires: pkgconfig(lua)
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-devel
BuildRequires: python3-pyyaml
BuildRequires: pngcrush

Requires: %{name}-common-data = %{version}-%{release}
Requires(pre): shadow-utils

%description
This is the Console (ncurses) version of %{name}.

Dungeon Crawl Stone Soup is a free roguelike game of exploration
and treasure-hunting in dungeons filled with dangerous and unfriendly
monsters in a quest for the mystifyingly fabulous Orb of Zot.

Dungeon Crawl Stone Soup has diverse species and many different character
backgrounds to choose from, deep tactical game-play, sophisticated magic,
religion and skill systems, and a grand variety of monsters to fight and
run from, making each game unique and challenging.

####################
%package common-data
Summary: Common data files of %{name}
BuildArch: noarch
Requires: hicolor-icon-theme

%description common-data
Data files for tiles and console versions of %{name}.

####################
%global fonts font(bitstreamverasans)
%global fonts %{fonts} font(bitstreamverasansmono)
%package tiles
Summary:  Roguelike dungeon exploration game with tiles
BuildRequires: fontconfig %{fonts}
Requires: %{name}-common-data = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: %{fonts}
Obsoletes: %{name}-tiles-data < 0:0.27.0

%description tiles
This is the tiles (graphical) version of %{name}.

Dungeon Crawl Stone Soup is a free roguelike game of exploration
and treasure-hunting in dungeons filled with dangerous and unfriendly
monsters in a quest for the mystifyingly fabulous Orb of Zot.

Dungeon Crawl Stone Soup has diverse species and many different character
backgrounds to choose from, deep tactical game-play, sophisticated magic,
religion and skill systems, and a grand variety of monsters to fight and
run from, making each game unique and challenging.
####################

%prep
%autosetup -n %{name}-%{version} -N

cat > crawl-ref/source/util/release_ver <<EOF
%{version}
EOF

## Remove unused/bundled files
rm -rf MSVC
rm -rf webserver

find crawl-ref/source -name '*.py' | xargs %{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -pn

#%%patch 4 -p1 -b .use_lua5
%patch -P 3 -p1 -b .add_iswalnum_reference

cp -a crawl-ref/source crawl-ref/crawl-tiles

%if %{without debug}
%patch -P 0 -p1 -b .crawl_bin
%patch -P 1 -p1 -b .crawl_tiles
%patch -P 2 -p1 -b .rltiles_cflags
%endif

%build
%if %{with debug}
%make_build all V=1 debug -C crawl-ref/crawl-tiles \
%else
%make_build all -C crawl-ref/crawl-tiles \
 CFOPTIMIZE_L="%{build_cxxflags} `%{_bindir}/libpng16-config --cflags` -DUSE_TILE" \
 CFOTHERS="%{build_cxxflags} `%{_bindir}/libpng16-config --cflags` -DUSE_TILE" \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" \
%endif
 GAME=crawl-tiles \
 TILES=y SOUND=y V=y MONOSPACED_FONT=y \
 DATADIR=%{_datadir}/%{name}-tiles \
 PROPORTIONAL_FONT=$(fc-match -f "%{file}" "bitstreamverasans") \
 MONOSPACED_FONT=$(fc-match -f "%{file}" "bitstreamverasansmono") \
 COPY_FONTS=n prefix=%{_prefix}

%if %{with debug}
%make_build all V=1 debug -C crawl-ref/source \
%else
%make_build all -C crawl-ref/source \
 CFOPTIMIZE_L="%{build_cxxflags} `%{_bindir}/libpng16-config --cflags`" \
 CFOTHERS="%{build_cxxflags} `%{_bindir}/libpng16-config --cflags`" \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" \
%endif
 SOUND=y V=y MONOSPACED_FONT=y \
 DATADIR=%{_datadir}/%{name} \
 PROPORTIONAL_FONT=$(fc-match -f "%{file}" "bitstreamverasans") \
 MONOSPACED_FONT=$(fc-match -f "%{file}" "bitstreamverasansmono") \
 COPY_FONTS=n prefix=%{_prefix}

%install
%if %{with debug}
%make_install debug -C crawl-ref/source \
%else
%make_install -C crawl-ref/source \
 CFOPTIMIZE_L="%{build_cxxflags} `%{_bindir}/libpng16-config --cflags`" \
 CFOTHERS="%{build_cxxflags} `%{_bindir}/libpng16-config --cflags`" \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" \
%endif
 SOUND=y V=y MONOSPACED_FONT=y \
 DATADIR=%{_datadir}/%{name} \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" \
 PROPORTIONAL_FONT=$(fc-match -f "%{file}" "bitstreamverasans") \
 MONOSPACED_FONT=$(fc-match -f "%{file}" "bitstreamverasansmono") \
 COPY_FONTS=n prefix=%{_prefix}

%if %{with debug}
%make_install install-xdg-data debug -C crawl-ref/crawl-tiles \
%else
%make_install install-xdg-data -C crawl-ref/crawl-tiles \
 CFOPTIMIZE_L="%{build_cxxflags} `%{_bindir}/libpng16-config --cflags`" \
 CFOTHERS="%{build_cxxflags} `%{_bindir}/libpng16-config --cflags`" \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" \
%endif
 GAME=crawl-tiles \
 TILES=y SOUND=y V=y MONOSPACED_FONT=y \
 DATADIR=%{_datadir}/%{name}-tiles \
 EXTERNAL_LDFLAGS="%{__global_ldflags}" \
 PROPORTIONAL_FONT=$(fc-match -f "%{file}" "bitstreamverasans") \
 MONOSPACED_FONT=$(fc-match -f "%{file}" "bitstreamverasansmono") \
 COPY_FONTS=n prefix=%{_prefix}

# Move doc files into /usr/share/crawl/docs (bz#1498448)
mkdir -p %{buildroot}%{_datadir}/%{name}/docs
mv %{buildroot}%{_pkgdocdir}/*.txt %{buildroot}%{_datadir}/%{name}/docs/
mv %{buildroot}%{_pkgdocdir}/quickstart.md %{buildroot}%{_datadir}/%{name}/docs/
mv %{buildroot}%{_pkgdocdir}/develop %{buildroot}%{_datadir}/%{name}/docs/
install -pm 644 crawl-ref/CREDITS.txt %{buildroot}%{_pkgdocdir}/
install -pm 644 README* %{buildroot}%{_pkgdocdir}/

# rhbz#2015328
cp -a %{buildroot}%{_datadir}/%{name}/docs %{buildroot}%{_datadir}/%{name}-tiles/

# Links to system's font
ln -sf $(fc-match -f "%{file}" "bitstreamverasansmono") %{buildroot}%{_datadir}/%{name}-tiles/dat/tiles/VeraMono.ttf
ln -sf $(fc-match -f "%{file}" "bitstreamverasans") %{buildroot}%{_datadir}/%{name}-tiles/dat/tiles/Vera.ttf

# Install manpage
mkdir -p %{buildroot}%{_mandir}/man6
install -pm 644 crawl-ref/docs/crawl.6 %{buildroot}%{_mandir}/man6/

# Instal icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -Dpm 644 crawl-ref/crawl-tiles/dat/tiles/stone_soup_icon-32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -Dpm 644 crawl-ref/crawl-tiles/dat/tiles/stone_soup_icon-512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps

# Install desktop file
mv %{buildroot}%{_datadir}/applications/org.develz.Crawl_tiles.desktop %{buildroot}%{_datadir}/applications/%{name}-tiles.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

# Install appdata file
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
mv %{buildroot}%{_metainfodir}/org.develz.Crawl_tiles.appdata.xml %{buildroot}%{_metainfodir}/%{name}-tiles.appdata.xml

# Remove duplicated files
%fdupes -s %{buildroot}%{_datadir}

%files
%{_bindir}/crawl
%{_mandir}/man6/crawl*
%{_datadir}/%{name}/

%files common-data
%license LICENSE
%{_pkgdocdir}/
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/512x512/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg

%files tiles
%{_bindir}/crawl-tiles
%{_datadir}/%{name}-tiles/
%{_datadir}/applications/%{name}-tiles.desktop
%{_metainfodir}/%{name}-tiles.appdata.xml

%changelog
%autochangelog
