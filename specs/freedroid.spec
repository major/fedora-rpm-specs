Name:           freedroid
Summary:        Clone of the C64 game Paradroid
License:        GPL-2.0-or-later

Version:        1.2.3
Release:        1%{?dist}

%global git_tag %{name}-%{version}.apk

URL:            https://github.com/ReinhardPrix/FreedroidClassic/
Source0:        %{URL}archive/%{git_tag}/%{git_tag}.tar.gz

Source1:        %{name}.desktop
Patch0:         0000-vorbisfile.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  desktop-file-utils
Requires:       %{name}-data = %{version}

%description
This is a clone of the classic game "Paradroid" on Commodore 64
with some improvements and extensions to the classic version.
In this game, you control a robot, depicted by a small white ball with
a few numbers within an interstellar spaceship consisting of several
decks connected by elevators.
The aim of the game is to destroy all enemy robots, depicted by small
black balls with a few numbers, by either shooting them or seizing
control over them by creating connections in a short subgame of
electric circuits.

%package        data
Summary:        Game data files for Freedroid
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    data
This package contains game data files for Freedroid.


%prep
%autosetup -p1 -n FreedroidClassic-%{git_tag}
./autogen.sh


%build
export CFLAGS="${CFLAGS} -fcommon -std=c99"
%configure --disable-dependency-tracking
%make_build


%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_datadir}/freedroid/mac-osx
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
install -Dpm 644 graphics/paraicon_48x48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/freedroid.png




%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/freedroid
%{_datadir}/applications/*freedroid.desktop
%{_datadir}/icons/hicolor/48x48/apps/freedroid.png
%{_mandir}/man6/freedroid.6*

%files data
%{_datadir}/freedroid/


%changelog
* Sun Jan 26 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.3-1
- Switch source repo to another fork
- Update to v1.2.3

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.2-43
- migrated to SPDX license

* Fri Jan 27 2023 Florian Weimer <fweimer@redhat.com> - 1.0.2-42
- Fix C99 compatibility issues

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.0.2-35
- Fix FTBFS.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-29
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.2-20
- Drop desktop vendor tag.

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.0.2-19
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.0.2-18
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 1.0.2-15
- Rebuild for libpng 1.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-12
- Split data files into a subpackage, make it noarch for Fedora >= 10.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-10
- Improve icon cache refresh scriptlets (#475927).

* Sat Feb  9 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-9
- Fix libvorbis(file) linkage.
- Point source tarball URL to downloads.sourceforge.net.

* Mon Aug 13 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-8
- License: GPLv2+

* Sun Jul  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-7
- Apply partial CPU hogging fix from upstream CVS.
- Desktop entry improvements.

* Tue Aug 29 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-6
- Move data files from %%{_datadir}/games/freedroid to %%{_datadir}/freedroid.

* Tue Feb 21 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-5
- Fix crash when the config file cannot be read/written to (#182280).
- Install icon to %%{_datadir}/icons/hicolor, update GTK icon cache at
  post(un)install time.
- Build with dependency tracking disabled.
- List installed files explicitly.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-4
- Rebuild, cosmetics.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2-3
- rebuilt

* Sat Nov 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0.2-0.fdr.2
- BuildRequires desktop-file-utils.

* Mon Aug 25 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0.2-0.fdr.1
- Update to 1.0.2.

* Tue May 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0.1-0.fdr.1
- First Fedora release.

* Wed Apr 30 2003 Ted Cipicchio <ted@thereisnospork.com> 1.0.1-1mdk
- 1.0.1

* Mon Apr 28 2003 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-5mdk
- fix buildrequires

* Mon Apr 28 2003 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-4mdk
- fix distriblint warning

* Sat Apr 26 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.4-3mdk
- dropped Prefix tag
- compile with $RPM_OPT_FLAGS
- added icons

* Fri Dec 20 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-2mdk
- add the manual to the docs

* Fri Dec 20 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-1mdk
- initial package

