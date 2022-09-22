%global repo_name LD25
%global repo_commit e5ecbe39b719f12a1268bcc641eae9ba364221c9 

Name:          colorful
Version:       1.3
Release:       15%{?dist}
Summary:       Side-view shooter game
License:       zlib with acknowledgement

URL:           https://svgames.pl
Source0:       https://github.com/suve/%{repo_name}/archive/%{repo_commit}.tar.gz#/%{repo_name}-%{repo_commit}.tar.gz

# On 32-bit architectures, FPC defaults to generating stabs-format debuginfo.
# This patch modifies the Makefile to explicitly ask the compiler
# to generate debuginfo in DWARF format.
Patch0:        colorful-DWARF.patch

Requires:      colorful-data = %{version}-%{release}
Requires:      hicolor-icon-theme
Requires:      opengl-games-utils

# Needed for compilation
BuildRequires: make, fpc >= 3.0, glibc-devel, SDL-devel, SDL_image-devel, SDL_mixer-devel, mesa-libGL-devel

# Needed to properly build the RPM
BuildRequires: desktop-file-utils, libappstream-glib

# FPC is not available on all architectures
ExclusiveArch:  %{fpc_arches}

%description
Colorful is a simple side-view shooter game, where the protagonist 
travels a maze of caves and corridors in order to collect color artifacts.


%package data
Summary:       Game data for Colorful
BuildArch:     noarch
# BuildRequires: 
# Requires:

%description data
Data files (graphics, maps, sounds) required to play Colorful.


%prep
%setup -q -n %{repo_name}-%{repo_commit}
%patch0 -p1

# According to the readme, these files are only needed when
# building with FPC < 3.0.0 and can otherwise be removed.
rm src/jedi-sdl.inc src/sdl_mixer_bundled.pas

# We're going to use the OpenGL Wrapper, so we have to edit the desktop file.
sed -e 's/^Exec=colorful$/Exec=colorful-wrapper/' -i pkg/%{name}.desktop

%build 
cd src/
make clean
make package

%install
install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_mandir}/man6/
install -m 755 -d %{buildroot}/%{_mandir}/pl/man6/
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 755 -d %{buildroot}/%{_datadir}/appdata/

install -m 755 -p src/%{name} %{buildroot}/%{_bindir}/%{name}
ln -s opengl-game-wrapper.sh %{buildroot}/%{_bindir}/%{name}-wrapper

install -m 644 -p pkg/%{name}-english.man  %{buildroot}/%{_mandir}/man6/%{name}.6
install -m 644 -p pkg/%{name}-polish.man   %{buildroot}/%{_mandir}/pl/man6/%{name}.6

desktop-file-install                            \
  --dir=%{buildroot}/%{_datadir}/applications/  \
  pkg/%{name}.desktop

appstream-util validate-relax --nonet pkg/%{name}.appdata.xml
install -m 644 -p pkg/%{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

install -m 644 -p pkg/%{name}-32x32.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


# For the -data subpackage
install -m 755 -d %{buildroot}/%{_datadir}/suve/%{name}/
install -m 755 -d %{buildroot}/%{_datadir}/suve/%{name}/gfx/
install -m 755 -d %{buildroot}/%{_datadir}/suve/%{name}/sfx/
install -m 755 -d %{buildroot}/%{_datadir}/suve/%{name}/intro/
install -m 755 -d %{buildroot}/%{_datadir}/suve/%{name}/map/org/
install -m 755 -d %{buildroot}/%{_datadir}/suve/%{name}/map/tut/

cp -a ./gfx/   %{buildroot}/%{_datadir}/suve/%{name}/
cp -a ./sfx/   %{buildroot}/%{_datadir}/suve/%{name}/
cp -a ./intro/ %{buildroot}/%{_datadir}/suve/%{name}/
cp -a ./map/   %{buildroot}/%{_datadir}/suve/%{name}/


%files
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_mandir}/man6/%{name}.6*
%{_mandir}/*/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%doc README.md
%license LICENCE.txt


%files data
%{_datadir}/suve/
%license LICENCE.txt


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3-5
- Remove obsolete scriptlets

* Mon Aug 07 2017 Artur Iwicki <fedora@svgames.pl> 1.3-4
- Fix debuginfo-related build failures on i686 and armv7hl

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Artur Iwicki <fedora@svgames.pl> 1.3-1
- Update to new upstream release
- Employ the OpenGL Wrapper (as detailed on Games SIG Packaging Guidelines page)
- Use wildcard to future-proof against more translated man pages

* Sat Jul 08 2017 Artur Iwicki <fedora@svgames.pl> 1.2-13.20170707.git.4db365a
- Update to the most recent upstream snapshot
- Remove the ppc64-fixes patch (issues fixed upstream)
- Remove the "find --exec chmod" call from %%install (issue fixed upstream)
- Remove the bundled-sdl-mixer patch (delete the files in %%prep instead)
- Mark README.md as documentation
- Use the %%{fpc_arches} macro in ExclusiveArch tag
- Add hicolor-icon-theme as dependency

* Sat Jul 08 2017 Artur Iwicki <fedora@svgames.pl> 1.2-12.20170412.git.ee1ca09
- Modify release number to include snapshot info

* Wed Jun 07 2017 Artur Iwicki <fedora@svgames.pl> 1.2-11
- Rename the SDL_Mixer-removing patch to a more descriptive name
- Add a patch file that addresses build failures on ppc64
- Add an equal-release requirement for the -data package in Requires
- Omit architectures where build fails due to FPC being unavailable
  (done by copy-paste'ing the ExclusiveArch list from fpc.spec)

* Sat May 20 2017 suve <veg@svgames.pl> 1.2-10
- Remove /usr/share/suve/colorful/ from files-list 
  (alredy covered by /usr/share/suve)
- Remove the executable bit from all files in the -data subpackage

* Sat Apr 15 2017 suve <veg@svgames.pl> 1.2-9
- Use the -a option (preserve timestamps & symlinks) instead of -R with cp
- Use the -p option (preserve timestamps) with install
- Fix wrong desktop file install dir (had package name at the end)
- Add an equal-version requirement for the -data package
- Use a patch to avoid using the bundled version of SDL_Mixer
- Add /usr/share/suve to files list (for ownership)

* Fri Apr 14 2017 suve <veg@svgames.pl> 1.2-8
- Validate appstream file during install

* Wed Apr 12 2017 suve <veg@svgames.pl> 1.2-7
- Use fresher upstream commit
- Merge the specs for the main package and -data

* Tue Apr 11 2017 suve <veg@svgames.pl> 1.2-6
- Use desktop-file-validate for the .desktop file
- Add an AppData file
- Add the icon cache scriptlets

* Mon Apr 10 2017 suve <veg@svgames.pl> 1.2-5
- Use the GitHub tarball as Source0
- List the manpage and desktop file as Sources instead of putting them in Patch0
- Reduce amount of stuff put in Patch0
- Add license in the files section 
- Use the binary release from the site in -data Source0
- Only list the main directory in -data files listing

