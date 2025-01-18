%undefine __cmake_in_source_build

%global rev     415
%global date    20151113

%global readme  README.fedora

Name:           gnurobbo
Version:        0.68
Release:        26.%{date}svn%{rev}%{?dist}
Summary:        Port of an once famous game named Robbo from 1989

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://%{name}.sf.net/

# Make source tarball from svn with $ ./%{name}-svn-tarball.sh %{rev}
Source0:        %{name}-%{version}svn%{rev}.tar.xz
Source1:        %{name}-svn-tarball.sh

Patch0:         https://sf.net/p/%{name}/patches/12/attachment/%{name}-cmake.patch
Patch1:         https://sf.net/p/%{name}/patches/13/attachment/%{name}-hardening.patch
Patch2:         gnurobbo-remove-original-levels.patch
# Fix the build with -fno-common, the GCC 10 default
Patch3:         %{name}-fno-common.patch

# icons additionally
Source10:       https://svn.code.sf.net/p/%{name}/code/%{name}.16.png.bz2
Source11:       https://svn.code.sf.net/p/%{name}/code/%{name}.32.png.bz2
Source12:       https://svn.code.sf.net/p/%{name}/code/%{name}.48.png.bz2

# information about legal issues
Source20:       %{name}-%{readme}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL-devel SDL_image-devel
# FIXME fonts and sounds are disabled and so deps should be removed
BuildRequires:  SDL_ttf-devel SDL_mixer-devel

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

#Bug 1171461 - due to legal reasons only the tronic skin has left
#and therefore we need to depend on it unless someone finds a better solution
Requires:       %{name}-tronic = %{version}-%{release}
Suggests:       %{name}-skin

Obsoletes:      %{name}-data
Obsoletes:      %{name}-fonts

%description
GNU Robbo is a free open source port of Janusz Pelc's Robbo
which was distributed by LK Avalon in 1989.

Features (some of them cat not be provided due to legal reasons)
   + Graphical skin support: Oily, Original and Tronic
   + Sound skin support: Default, Free and Oily
   + Support for user supplied music
   + 1113 levels across 28 packs converted from Robbo and Robbo Konstruktor
   + A mouse/stylus driven level designer
   + Support for Alex (a Robbo clone) objects
   + Support for Robbo Millenium objects
   + In-game help
   + Reconfigurable options and controls
   + Support for the mouse/stylus throughout the game
   + Support for keyboards, analogue and digital joysticks
   + Centering of game within any resolution >= 240x240
   + Simple build system to maximize porting potential
   + Support for locales

The game-play of the original is faithfully reproduced with a few modifications
   + Lives has been removed and suicide replaced with level restart
   + Scoring has been removed: goal is level advancement
   + Bears don't endlessly spin around themselves
   + Capsules don't spawn from question marks
   + Solid laser fire is not left live after the gun has been destroyed

Take a look into %{readme} about legal issues cause of missing content.


%package tronic
Summary:        Tronic skin for the game %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-skin

%description tronic
Optional skin named tronic for the game %{name}:
Newly created skin with some vintage science fiction influences.


%prep
%autosetup -p0 -n%{name}-%{version}svn%{rev}
cp -p %SOURCE10 %SOURCE11 %SOURCE12 .
bunzip2 *.png.bz2
cp -p %SOURCE20 %{readme}

# do not distribute any illegal content
sed -i s,add_subdirectory.data.,, CMakeLists.txt


%build
# fonts and sounds are not redistributable, ignore them
%cmake -DUSE_FONTS=OFF -DDISABLE_MUSIC=ON
%cmake_build


%install
%cmake_install
# skip misplaced license texts, they get replaced via %license
rm -v %{buildroot}%{_pkgdocdir}/COPYING %{buildroot}%{_pkgdocdir}/LICENSE*

# legal content parts
install -d %{buildroot}%{_datadir}/%{name}
cp -pr data/locales data/levels data/skins data/rob -t%{buildroot}%{_datadir}/%{name}

# desktop
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=GNU Robbo
Comment=Port of the once famous ATARI game Robbo
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

# icons
install -d %{buildroot}%{_datadir}/icons/hicolor
for size in 16 32 48; do
 install %{name}.$size.png -D %{buildroot}%{_datadir}/icons/hicolor/$size'x'$size/apps/%{name}.png
done
#install -d %{buildroot}%{_datadir}/pixmaps
#ln -s ../icons/hicolor/48x48/apps/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop



%files
%license COPYING LICENSE-ttf LICENSE-sound
%doc AUTHORS Bugs ChangeLog NEWS README TODO
# distribution is only allowed for legal content
%doc %{readme}
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/levels/
%{_datadir}/%{name}/locales/
%{_datadir}/%{name}/rob/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
#%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}/skins

%files tronic
%{_datadir}/%{name}/skins/tronic/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-26.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.68-25.20151113svn415
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-24.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-23.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-22.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-21.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-20.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-19.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-18.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-17.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-16.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-15.20151113svn415
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-14.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb  7 2020 Jerry James <loganjerry@gmail.com> - 0.68-13.20151113svn415
- Add fno-common patch to fix FTBFS with GCC 10 (bz 1799432)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-13.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-12.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-11.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Björn Esser <besser82@fedoraproject.org> - 0.68-10.20151113svn415
- Append curdir to CMake invokation (#1667306)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-9.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-8.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.68-7.20151113svn415
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-6.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-5.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-4.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Raphael Groner <projects.rg@smart.ms> - 0.68-3.20151113svn415
- rebuild for koschei

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-2.20151113svn415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Raphael Groner <projects.rg@smart.ms> - 0.68-1.20151113svn415
- new version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-7.20141028svn412
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Jaromir Capik <jcapik@redhat.com> - 0.66-6.20141028svn412
- Removing original levels to avoid distributing possibly illegal content (#1157664)

* Fri Jan 02 2015 Jaromir Capik <jcapik@redhat.com> - 0.66-5.20141028svn412
- R: gnurobbo-tronic as it seems to be the only legal skin now (#1171461)

* Sat Nov 01 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.66-4.20141028svn412
- rebuilt for SCM
- preserve timestamps of icons
- cleanup package structure again

* Tue Oct 28 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.66-3.20141028svn412
- distribute legal content only (rhbz #1157664)
- use biggest desktop icon that we have (partly rhbz #1157534)
- Obsoletes old subpackage structure

* Mon Oct 27 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.66-2.20141027svn412
- data and fonts have legal issues, so remove original contents till we have alternatives
- R: hicolor-icon-theme

* Wed Oct 08 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.66-1.20141005svn412
- rebuilt for SCM import

* Tue Oct 07 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.66-0.4.20141005svn412
- use GPLv2+ (v2 or any later version, comply to licence text in sources)
- fix duplicated ownership
- fix mode of tarball script
- removed redundant sources

* Tue Oct 07 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.66-0.3.20141005svn412
- fix review issues

* Sun Oct 05 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.66-0.2.20141005svn412
- fix desktop file and icon cache
- fix version tag

* Sat Oct 04 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.66svn412-1
- initital
