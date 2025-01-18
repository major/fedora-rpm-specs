# There is Gearhead 2 in development right now,
# and upstream always refers to the first game as "Gearhead 1",
# so let's stick with that and use "gearhead1" instead of just "gearhead"
Name: gearhead1
%global reponame gearhead-1
%global prettyname GearHead: Arena

%global about_game Roguelike mecha role-playing game
Summary: %{about_game}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2

Version: 1.310
Release: 17%{?dist}

URL: http://gearheadrpg.com
Source0: https://github.com/jwvhewitt/%{reponame}/archive/v%{version}/%{reponame}-%{version}.tar.gz

Source10: %{name}-icon-128px.png
Source11: %{name}-icon-96px.png
Source12: %{name}-icon-48px.png

Source20: %{name}-sdl.appdata.xml

# The program tries to load data from the current working directory.
# Change the file paths to point to %%{_datadir} instead.
Patch0: 0000-change-data-paths.patch

ExclusiveArch: %{fpc_arches}

BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: fpc
BuildRequires: fpc-srpm-macros
BuildRequires: glibc-devel
BuildRequires: libappstream-glib
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel

%global fontlist font(bitstreamverasans) font(bitstreamverasansmono) font(bitstreamveraserif)
BuildRequires: fontconfig
BuildRequires: %{fontlist}

Requires: %{name}-bin%{?_isa} = %{version}-%{release}
Suggests: %{name}-SDL%{?_isa} = %{version}-%{release}


%description
Set a century and a half after nuclear war, in this game you explore a world
where various factions compete to determine the future of the human race.

Features include random plot generation and over two hundred mecha designs.
Pilot a giant robot, a city smashing tank, a living jet fighter, or
anything else that can be built using the game's sophisticated design system.


%package textmode
Summary: %{about_game} (textmode version)
Provides: %{name}-bin%{?_isa} = %{version}-%{release}

Requires: %{name}-data = %{version}-%{release}

%description textmode
Textmode build of %{prettyname}.


%package SDL
Summary: %{about_game} (SDL version)
Provides: %{name}-bin%{?_isa} = %{version}-%{release}

Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-data-gfx = %{version}-%{release}

%description SDL
Graphical build of %{prettyname}, based on the SDL library.


%package data
Summary: Data files for %{name}
BuildArch: noarch

%description data
Data files required to play %{prettyname}.


%package data-gfx
Summary: Graphics and fonts for %{name}-SDL
BuildArch: noarch

Requires: %{name}-data = %{version}-%{release}

Requires: %{fontlist}
Requires: hicolor-icon-theme

%description data-gfx
Images and fonts required to play the graphical version of %{prettyname}.


%prep
%autosetup -p1 -n %{reponame}-%{version}
sed -e "s|__RPM_DATA_DIR__|'%{_datadir}/%{name}'|" -i gears.pp

# Convert files from \r\n to \n
find doc/ -type f -exec dos2unix '{}' ';'
dos2unix readme.md

# Copy over the icons
cp -a %{SOURCE10} %{SOURCE11} %{SOURCE12} ./

# Copy over the appdata.xml file
cp -a %{SOURCE20} ./

# Upsteam does not ship a desktop file
cat > %{name}-sdl.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{prettyname}
Comment=%{about_game}
Exec=%{name}-sdl
Icon=%{name}
Terminal=false
Categories=Game;
EOF


%build
%global buildflags -gw -O2
# -- build the terminal version of the game
fpc %{buildflags} -o'gharena-textmode' gharena.pas

# -- remove all compilation leftovers (the equivalent of "make clean")
rm *.a || true
rm *.o || true
rm *.ppu || true

# -- build the SDL version of the game
fpc %{buildflags} -d'SDLMODE' -o'gharena-sdl' gharena.pas


%install
install -m 755 -d %{buildroot}%{_bindir}
for BUILD in textmode sdl; do
	install -m 755  "gharena-${BUILD}"  "%{buildroot}%{_bindir}/%{name}-${BUILD}"
done

install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a Design doc GameData Image Series  %{buildroot}%{_datadir}/%{name}

# Replace the bundled Bitstream Vera fonts
# with symlinks to fonts provided by bitstream-vera-* packages
for FONT in  \
	"Vera/Sans:regular" "VeraBd/Sans:bold" "VeraIt/Sans:italic" "VeraBI/Sans:bold:italic"  \
	"VeraMono/Sans Mono:regular" "VeraMoBd/Sans Mono:bold" "VeraMoIt/Sans Mono:italic" "VeraMoBI/Sans Mono:bold:italic"  \
	"VeraSe/Serif:regular" "VeraSeBd/Serif:bold";
do
	FONT_FILE="$(echo "$FONT" | cut '-d/' -f1)"
	FONT_NAME="Bitstream Vera $(echo "$FONT" | cut '-d/' -f2-)"
	ln -sf  \
		"$(fc-match -f "%%{file}" "${FONT_NAME}")"  \
		"%{buildroot}%{_datadir}/%{name}/Image/${FONT_FILE}.ttf"
done

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 %{name}-sdl.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 %{name}-sdl.appdata.xml %{buildroot}%{_metainfodir}/

for SIZE in 128 96 48; do
	ICONDIR="%{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps"
	install -m 755 -d "${ICONDIR}"
	install -m 644 "%{name}-icon-${SIZE}px.png" "${ICONDIR}/%{name}.png"
done


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}-sdl.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-sdl.desktop


%files
# empty

%files textmode
%{_bindir}/%{name}-textmode

%files SDL
%{_bindir}/%{name}-sdl
%{_datadir}/applications/%{name}-sdl.desktop
%{_metainfodir}/%{name}-sdl.appdata.xml

%files data
%doc readme.md
%license license.txt
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/Image/

%files data-gfx
%{_datadir}/%{name}/Image/
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.310-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.310-9
- Add a patch to change program data paths, instead of using a wrapper script
- Fix installing documentation (it is used by program at run-time)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.310-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Artur Iwicki <fedora@svgames.pl> - 1.310-4
- Fix DOS line endings in files

* Fri May 15 2020 Artur Iwicki <fedora@svgames.pl> - 1.310-3
- Use fc-match to find system fonts instead of using hard-coded paths
- Add an appdata.xml file

* Wed Apr 22 2020 Artur Iwicki <fedora@svgames.pl> - 1.310-2
- Build both the SDL and the textmode version of the game
- Put the SDL and textmode versions in separate subpackages
- Move images and fonts out of -data into -data-gfx
- Fix one of the fonts being symlinked wrong
- Add some icons and a desktop file

* Sat Apr 11 2020 Artur Iwicki <fedora@svgames.pl> - 1.310-1
- Initial packaging
