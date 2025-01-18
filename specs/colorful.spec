Name:          colorful
%global rtld pl.suve.colorful

Version:       2.2
Release:       2%{?dist}
Summary:       Side-view shooter game

# The game itself is GPLv3.
# The source archive also inluces Pascal units for SDL2.
# Said units are dual-licensed: MPLv2 or zlib.
License:       GPL-3.0-only AND (MPL-2.0 OR Zlib)

URL:           https://svgames.pl
Source0:       https://github.com/suve/LD25/releases/download/release-%{version}/colorful-%{version}-source.zip

Requires:      colorful-data = %{version}-%{release}
Requires:      hicolor-icon-theme

# Needed for compilation
BuildRequires: fpc >= 3.0.0
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: optipng
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: vorbis-tools

# Needed to properly build the RPM
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# FPC is not available on all architectures
ExclusiveArch:  %{fpc_arches}

%description
Colorful is a simple side-view shooter game, where the protagonist 
travels a maze of caves and corridors in order to collect color artifacts.


%package data
Summary:       Game data for Colorful
# The game uses separate licenses for code and assets
License:       zlib-acknowledgement
BuildArch:     noarch

%description data
Data files (graphics, maps, sounds) required to play Colorful.


%prep
%autosetup -p1 -n %{name}-%{version}-source


%build 
./configure.sh --assets=systemwide --flags="-g -gl -gw" --prefix=%{_prefix} --strip=false
%make_build


%install
%make_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rtld}.metainfo.xml


%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_mandir}/*/man6/%{name}.6*
%{_datadir}/applications/%{rtld}.desktop
%{_datadir}/metainfo/%{rtld}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc README.md
%license LICENCE-CODE.txt


%files data
%{_datadir}/suve/
%license LICENCE-ASSETS.txt


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 11 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.2-1
- Update to v2.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.1-1
- Update to v2.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0-1
- Update to v2.0

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

