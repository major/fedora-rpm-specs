Name:       flare
Version:    1.13.04
Release:    2%{?dist}
Summary:    A single player, 2D-isometric, action Role-Playing Game
License:    CC-BY-SA and CC-BY and CC0 and Public Domain
URL:        http://www.flarerpg.org
Source0:    https://github.com/flareteam/flare-game/releases/download/v%{version}/%{name}-game-v%{version}.tar.gz

Requires:   %{name}-engine%{?_isa} = %{version}
Requires:   liberation-sans-fonts

Obsoletes:   %{name}-data <= 0.18

BuildRequires: cmake
BuildRequires: libappstream-glib
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: liberation-sans-fonts

BuildArch: noarch


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
%setup -q -n %{name}-game-v%{version}


%build
# Do not use /usr/games or /usr/share/games/
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBINDIR="bin" -DDATADIR="share/%{name}/"
%cmake_build


%install
%cmake_install

# Use system font
rm %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Regular.ttf
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Regular.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Regular.ttf
rm %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Bold.ttf
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Bold.ttf
rm %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Italic.ttf
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Italic.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Italic.ttf

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
%doc README LICENSE.txt CREDITS.txt

%{_metainfodir}/*.appdata.xml
%{_datadir}/%{name}/mods/*/


%changelog
* Thu Aug 25 2022 Sandro <gui1ty@penguinpee.nl> - 1.13.04-2
- Fixed %cmake in spec file (#2059201)

* Wed Aug 24 2022 Sandipan Roy <bytehackr@fedoraproject.org> - 1.13.04-1
- Updated to 1.13.04 (#2003478)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 31 2022 Justin Jacobs <jajdorkster@gmail.com> - 1.13-1
- Update to 1.13 and fix font symlinks

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Erik Schilling <git@ablu.org> - 1.07-7
- Fixes for
  https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds#Migration

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Erik Schilling <ablu.erikschilling@googlemail.com> - 1.07-1
- Updated to 1.07

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.19-9
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.19-4
- Add an AppData file for the software center

* Tue Sep 2 2014 Marcos Paulo de Souza <marcos.souza.org@gmail.com> - 0.19-3
- Fixed desktop file by removing TryExec args

* Wed Aug 20 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.19-2
- Fixed cmake dependency

* Tue Aug 19 2014 Erik Schilling <ablu.erikschilling@googlemail.com> 0.19-1
- New release
- Splitted out engine code into flare-engine package

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 0.18-5
- Rebuild for new SDL_gfx

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 1 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.18-2
- Adapted to the newly updated release tar
- Since the old one was kind of broken and incomplete a new one was generated

* Mon Apr 1 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.18-1
- New upstream release
- Breaks compatibillity with old save files

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-8
- Simplified directiory permissions

* Mon Nov 12 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-7
- Fixed directory ownership

* Sun Nov 11 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-6
- Spell-fix: reimplementation --> re-implementation
- Mark translation files with %%lang

* Fri Nov 02 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-5
- Dropped / between path makros
- Made use of %%{name} makro in Source1
- Made sure that the binary links against system SDL_gfx parts
- Replaced unifont use with dejavu since the font was not packaged

* Thu Oct 25 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-4
- Fixed require of binaries in -data package
- Fixed update icon cache
- Fixed trailing slash of url
- Fixed license from GPLv3 to GPLv3+

* Sat Oct 6 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-3
- Do not install to /usr/share/games but /usr/share (https://fedoraproject.org/wiki/SIGs/Games/Packaging)

* Sat Oct 6 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-2
- Added BuildArch: noarch for data package

* Fri Oct 5 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-1
- Initial packaging
