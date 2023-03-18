%global forgeurl https://github.com/flareteam/flare-engine

%global shortname flare

Name:       flare-engine
Version:    1.14
Release:    %autorelease

%forgemeta

Summary:    A single player, 2D-isometric, action Role-Playing Engine

# cmake/FindSDL2* is BSD-3-Clause
# https://github.com/flareteam/flare-engine/commit/777b3da2179f3f39fa1b8afdd0cc284b2069d065
License:    GPL-3.0-or-later AND BSD-3-Clause
URL:        http://www.flarerpg.org
Source0:    %{forgesource}

Requires:   liberation-sans-fonts
Requires:   unifont-ttf-fonts

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: desktop-file-utils
BuildRequires: liberation-sans-fonts
BuildRequires: unifont-ttf-fonts

%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine built to
handle a very specific kind of game: single-player 2D action RPGs. Flare is not
a re-implementation of an existing game or engine. It is a tribute to and
exploration of the action RPG genre.

Rather than building a very abstract, robust game engine, the goal of this
project is to build several real games and harvest an engine from the common,
reusable code. The first game, in progress, is a fantasy dungeon crawl.

Flare uses simple file formats (INI style config files) for most of the game
data, allowing anyone to easily modify game contents. Open formats are
preferred (png, ogg). The game code is C++.

This package contains the engine only.


%prep
%setup -q -n %{name}-%{version}


%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBINDIR="bin" -DDATADIR="share/%{shortname}/"
%cmake_build


%install
%cmake_install

# Use system fonts
rm %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/LiberationSans-Regular.ttf
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Regular.ttf %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/LiberationSans-Regular.ttf
# slightly wrong version number, but should be fine, past releases shipped without it at all
rm %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/unifont-10.0.06.ttf
ln -s %{_datadir}/fonts/unifont/unifont.ttf %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/unifont-10.0.06.ttf

LEFT_FONT_FILES=$(find %{buildroot}%{_datadir}/%{shortname}/ -type f -name "*.ttf" -o -name "*.otf")
if [ -n "$LEFT_FONT_FILES" ]
then
    echo "Found remaining (non-symlinked) fonts: $LEFT_FONT_FILES"  1>&2
    echo "Failing build!" 1>&2
    exit 1
fi

BROKEN_SYMLINKS=$(find %{buildroot}%{_datadir}/%{shortname}/ -type l ! -exec test -e {} \; -print)
if [ -n "$BROKEN_SYMLINKS" ]
then
    echo "Found broken symlinks: $BROKEN_SYMLINKS" 1>&2
    echo "Failing build!" 1>&2
    exit 1
fi

# Validate desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{shortname}.desktop


%files
%doc README.engine.md CREDITS.engine.txt RELEASE_NOTES.txt
%license COPYING
%{_bindir}/%{shortname}
%{_datadir}/%{shortname}/
%{_datadir}/applications/%{shortname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{shortname}.svg
%{_mandir}/man6/%{shortname}.6*


%changelog
%autochangelog
