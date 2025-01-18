Name: gearhead2
%global reponame gearhead-2
%global prettyname GearHead II

%global about_game Roguelike mecha role-playing game - in space!
Summary: %{about_game}

# license.txt is LGPL v2.1. readme.txt says simply "LGPL".
# In source code files, the license headers say:
# "either version 2.1 of the License, or (at your option) any later version".
License: LGPLv2+

%global git_date   20201130
%global git_commit 86d17e191529733c06d05c333d7f3e820b8645d4
%global git_commit_short %(c="%{git_commit}"; echo "${c:0:7}")

Version: 0.701
Release: 8.%{git_date}git%{git_commit_short}%{?dist}

URL: http://gearheadrpg.com
Source0: https://github.com/jwvhewitt/%{reponame}/archive/%{git_commit}/%{reponame}-%{git_commit}.tar.gz

Source10: %{name}-icon-512px.png
Source11: %{name}-icon-256px.png
Source12: %{name}-icon-128px.png
Source13: %{name}-icon-64px.png

Source20: %{name}-sdl.appdata.xml

# The program looks for data files in the current directory.
# Change paths to search in %%{_datadir} instead.
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

%global fontlist font(bitstreamverasans) font(bitstreamverasansmono)
BuildRequires: fontconfig
BuildRequires: %{fontlist}

Requires: %{name}-bin%{?_isa} = %{version}-%{release}
Suggests: %{name}-SDL%{?_isa} = %{version}-%{release}


%description
The sequel to GearHead: Arena. Five years after the Typhon Incident,
tensions are high in the L5 region as all sides prepare for a possible war
between Earth and Luna. The arrival of a mysterious new pirate fleet
has further destabilized this vulnerable region.


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
%autosetup -p1 -n %{reponame}-%{git_commit}
sed -e "s|__RPM_DATA_DIR__|'%{_datadir}/%{name}'|" -i gears.pp

# Convert files from \r\n to \n
find ./ -name '*.txt' -exec dos2unix '{}' ';'

# Copy over the icons
cp -a %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} ./

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
%global buildflags -Cg -gl -gw3 -O2

# -- build the terminal version of the game
fpc %{buildflags} -d'ASCII' -o'gh2-textmode' gearhead2.pas

# -- remove all compilation leftovers (the equivalent of "make clean")
rm *.a || true
rm *.o || true
rm *.ppu || true

# -- build the SDL version of the game
fpc %{buildflags} -o'gh2-sdl' gearhead2.pas


%install
install -m 755 -d %{buildroot}%{_bindir}
for BUILD in textmode sdl; do
	install -m 755 "gh2-${BUILD}"  "%{buildroot}%{_bindir}/%{name}-${BUILD}"
done

install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a design doc gamedata image series  %{buildroot}%{_datadir}/%{name}

# Replace the bundled Bitstream Vera fonts
# with symlinks to fonts provided by bitstream-vera-* packages
for FONT in "VeraBd/Sans:bold" "VeraMoBd/Sans Mono:bold"; do
	FONT_FILE="$(echo "$FONT" | cut '-d/' -f1)"
	FONT_NAME="Bitstream Vera $(echo "$FONT" | cut '-d/' -f2-)"
	ln -sf  \
		"$(fc-match -f "%%{file}" "${FONT_NAME}")"  \
		"%{buildroot}%{_datadir}/%{name}/image/${FONT_FILE}.ttf"
done

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 %{name}-sdl.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 %{name}-sdl.appdata.xml %{buildroot}%{_metainfodir}/

for SIZE in 512 256 128 64; do
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
%doc readme.txt
%license license.txt
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/image/

%files data-gfx
%{_datadir}/%{name}/image/
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.701-8.20201130git86d17e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.701-7.20201130git86d17e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.701-6.20201130git86d17e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.701-5.20201130git86d17e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.701-4.20201130git86d17e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.701-3.20201130git86d17e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.701-2.20201130git86d17e1
- Build the executables in PIC mode

* Sat Jun 18 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.701-1.20201130git86d17e1
- Initial packaging
