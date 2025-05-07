Name:       flare
Version:    1.14
Release:    %autorelease
Summary:    A single player, 2D-isometric, action Role-Playing Game

%global forgeurl https://github.com/flareteam/flare-game
%global tag v%{version}
%forgemeta

# See: https://github.com/flareteam/flare-game/blob/master/distribution/org.flarerpg.Flare.appdata.xml
License:    GPL-3.0-or-later AND CC-BY-SA-3.0
URL:        http://www.flarerpg.org
Source:     %{forgesource}
# Backport patch for CMake 4.x
# https://github.com/flareteam/flare-game/commit/5b61dfd69f4ecbaca6439caa9ae41b3168e4d21a
Patch:      0001-Minimum-CMake-version-3.5.patch

BuildArch:  noarch

BuildRequires: cmake
BuildRequires: libappstream-glib
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: font(liberationsans)

Requires:   %{name}-engine%{?_isa} = %{version}
Requires:   font(liberationsans)

Obsoletes:  %{name}-data <= 0.18


%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine built to
handle a very specific kind of game: single-player 2D action RPGs. Flare is not
a re-implementation of an existing game or engine. It is a tribute to and
exploration of the action RPG genre.

Rather than building a very abstract, robust game engine, the goal of this
project is to build several real games and harvest an engine from the common,
reusable code. The first game, in progress, is a fantasy dungeon crawl.

Flare uses simple file formats (INI style configuration files) for most of
the game data, allowing anyone to easily modify game contents. Open formats are
preferred (png, ogg). The game code is C++.

%prep
%forgeautosetup -p1


%build
# Do not use /usr/games or /usr/share/games/
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBINDIR="bin" -DDATADIR="share/%{name}/"
%cmake_build


%install
%cmake_install

# Use system font
rm %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Regular.ttf
rm %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Bold.ttf
rm %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Italic.ttf
%if %{fedora} >= 41
ln -s %{_datadir}/fonts/liberation-sans-fonts/LiberationSans-Regular.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Regular.ttf
ln -s %{_datadir}/fonts/liberation-sans-fonts/LiberationSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Bold.ttf
ln -s %{_datadir}/fonts/liberation-sans-fonts/LiberationSans-Italic.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Italic.ttf
%else
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Regular.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Regular.ttf
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Bold.ttf
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Italic.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Italic.ttf
%endif

# Marck Script is not packaged in Fedora's repos, so it is removed without making a symlink
# The game engine will fall back to LiberationSans-Regular.tff
rm %{buildroot}%{_datadir}/%{name}/mods/empyrean_campaign/fonts/MarckScript-Regular.ttf

LEFT_FONT_FILES=$(find %{buildroot}%{_datadir}/%{name}/ -type f -name "*.ttf" -o -name "*.otf")
if [ -n "$LEFT_FONT_FILES" ]
then
    echo "Found remaining (non-symlinked) fonts: $LEFT_FONT_FILES"  1>&2
    echo "Failing build!" 1>&2
    exit 1
fi

BROKEN_SYMLINKS=$(find %{buildroot}%{_datadir}/%{name}/ -type l ! -exec test -e {} \; -print)
if [ -n "$BROKEN_SYMLINKS" ]
then
    echo "Found broken symlinks: $BROKEN_SYMLINKS" 1>&2
    echo "Failing build!" 1>&2
    exit 1
fi

# Validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%doc README CREDITS.txt
%license LICENSE.txt

%{_metainfodir}/*.appdata.xml
%{_datadir}/%{name}/mods/*/


%changelog
%autochangelog
