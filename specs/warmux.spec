Name:           warmux
Version:        11.04.1
Release:        41%{?dist}
Summary:        2D turn-based artillery game

# fixedpoint library seems to be under BSD license
# Some parts of src/tool/xml_document.cpp are taken from libxml2 (released under the MIT license)
# Automatically converted from old format: GPLv2+ and BSD and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            http://gna.org/projects/warmux/
Source0:        http://download.gna.org/warmux/warmux-%{version}.tar.bz2

# Remove Superman logo due to copyright
Source1:        superman.png
Source2:        supertux_ico.png
Source3:        supertux.png

Patch1:         warmux-zlib.patch
Patch2:         warmux-gcc47.patch
Patch3:         warmux-gcc60.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL_image-devel SDL_gfx-devel SDL_mixer-devel
BuildRequires:  SDL_ttf-devel SDL_net-devel curl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)

BuildRequires:  gettext libxml++-devel desktop-file-utils
BuildRequires:  zlib-devel
Requires:       warmux-data = %{version}
Requires:       hicolor-icon-theme

Provides:       wormux = %{version}-%{release}
Obsoletes:      wormux < 0.9.2.1-9

%description
Let's begin the WAR of Mascots from UniX!
They'll represent your favorite free software titles while battling it out
in the arena using dynamite, grenades, baseball bats and other bazookas...
Exterminate your opponent in a 2D environment with toon-style scenery.
Each player controls the team of his choice (penguin, gnu, firefox, wilber,...)
and must destroy his adversary using more or less casual weapons.
Although a minimum of strategy is required to vanquish, WarMUX is pre-eminently
a "convivial mass murder" game where, turn by turn, each member of each team.

The project was started as Wormux, and was renamed to Warmux in November 2010.


%package data
Summary: Data files for warmux
Requires: %{name} = %{version}
BuildArch: noarch
Provides:  wormux-data = %{version}-%{release}
Obsoletes: wormux-data < 0.9.2.1-9

%description data
Data files for warmux


%prep
%setup -q -n warmux-11.04
%patch -P1 -p1 -b .zlib
%patch -P2 -p1 -b .gcc47
%patch -P3 -p0 -b .gcc60

# Remove a backup file
rm -f data/game_mode/rope_objects.xml~
rm -f data/game_mode/skin_viewer.xml~

%build
%configure --enable-fribidi
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

sed -i -e 's/Icon=.*/Icon=warmux/' \
        %{buildroot}%{_datadir}/applications/warmux.desktop

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications/ \
        --remove-category=Application \
        --remove-category=ArcadeGame \
        --add-category=StrategyGame \
        --delete-original \
        %{buildroot}%{_datadir}/applications/warmux.desktop

install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m 644 data/icon/warmux_128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/warmux.png

install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/warmux/weapon/supertux/superman.png
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/warmux/weapon/supertux/supertux_ico.png
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/warmux/weapon/supertux/supertux.png

rm -f %{buildroot}%{_datadir}/applications/warmux_files.desktop
rm -f %{buildroot}%{_datadir}/warmux/.nomedia

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
SentUpstream: Dead!
-->
<application>
  <id type="desktop">warmux.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      WarMUX is a free and open-source turn-based game and can be played online
      in public or private mode.
    </p>
    <p>
      Players can play together each one in the commande of a team in a senario
      that puts free software mascots in a battle using dynamite, grenades,
      baseball bats, and bazookas.
    </p>
  </description>
  <url type="homepage">http://sourceforge.net/projects/warmux/</url>
  <screenshots>
    <screenshot type="default">http://a.fsdn.com/con/app/proj/warmux.mirror/screenshots/Warmux.jpg</screenshot>
    <screenshot>http://a.fsdn.com/con/app/proj/warmux.mirror/screenshots/warmux.png</screenshot>
    <screenshot>http://a.fsdn.com/con/app/proj/warmux.mirror/screenshots/Warmux1.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/warmux
%{_bindir}/warmux-list-games
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/warmux.desktop
%{_datadir}/icons/hicolor/128x128/apps/warmux.png
%{_datadir}/pixmaps/warmux*.png
%{_mandir}/man6/*.6.gz

%files data
%{_datadir}/warmux

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 11.04.1-40
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Filipe Rosset <rosset.filipe@gmail.com> - 11.04.1-28
- Rebuilt for fribidi-devel fix

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.04.1-24
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 10 2016 Bruno Wolff III <bruno@wolff.to> - 11.04.1-20
- gcc 6.0 is more fussy

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11.04.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.04.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 11.04.1-17
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 11.04.1-16
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.04.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Fridolin Pokorny <fpokorny@redhat.com> - 11.04.1-14
- Remove superman logo from images (#1071866)

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 11.04.1-13
- Rebuild for new SDL_gfx

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.04.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Jiri Popelka <jpopelka@redhat.com> - 11.04.1-11
- BuildRequires: pkgconfig(foo) instead of foo-devel

* Fri Sep 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 11.04.1-10
- correct wormux-data obs_ver

* Tue Sep 10 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 11.04.1-9
- correct wormux obs_ver

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.04.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.04.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Jiri Popelka <jpopelka@redhat.com> - 11.04.1-6
- www.wormux.org seems to no longer work

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.04.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Jiri Popelka <jpopelka@redhat.com> - 11.04.1-4
- don't install warmux_files.desktop file (#812533)

* Mon Feb 27 2012 Jiri Popelka <jpopelka@redhat.com> - 11.04.1-3
- fixed building with gcc 4.7 (by Bruno Wolff III)

* Mon Jan 16 2012 Jiri Popelka <jpopelka@redhat.com> - 11.04.1-2
- fixed problems from Package Review (#773419)

* Wed Jan 11 2012 Jiri Popelka <jpopelka@redhat.com> - 11.04.1-1
- wormux renamed to warmux
- updated to 11.04.1

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.2.1-6
- Rebuild for new libpng

* Tue Jul 26 2011 Bruno Wolff III <bruno@wolff.to> - 0.9.2.1-5
- Rebuild for SDL_gfx soname bump.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.9.2.1-3
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Wart <wart@kobold.org> 0.9.2.1-2
- Re-add french translations that had gone missing

* Sun Sep 12 2010 Wart <wart@kobold.org> 0.9.2.1-1
- Update to 0.9.2.1 with fix for 64-bit builds

* Sat Sep 11 2010 Wart <wart@kobold.org> 0.9.2-1
- Update to 0.9.2

* Sat Feb 6 2010 Wart <wart@kobold.org> 0.9.0-1
- Update to 0.9.0

* Sat Oct 10 2009 Wart <wart@kobold.org> 0.8.5-1
- Update to 0.8.5

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Wart <wart@kobold.org> 0.8.4-1
- Update to 0.8.4

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.8.3-2
- Build with $RPM_OPT_FLAGS.

* Wed May 6 2009 Wart <wart@kobold.org> 0.8.3-1
- Update to 0.8.3
- Make -data subpackage noarch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Wart <wart@kobold.org> 0.8.2-4
- Yet another font package rename

* Thu Jan 1 2009 Wart <wart@kobold.org> 0.8.2-3
- Fix font package name for F11

* Wed Dec 24 2008 Wart <wart@kobold.org> 0.8.2-2
- Add coreutils requirement for rpm post scripts
- Replace bundled font with a symlink to an identical system font (BZ #477484)

* Fri Nov 7 2008 Wart <wart@kobold.org> 0.8.2-1
- Update to 0.8.2

* Thu May 29 2008 Wart <wart@kobold.org> 0.8-1
- Update to 0.8

* Fri Feb 8 2008 Wart <wart@kobold.org> 0.7.9-6
- Rebuild for gcc 4.3

* Tue Aug 21 2007 Wart <wart@kobold.org> 0.7.9-5
- License tag clarification

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 0.7.9-4
- Rebuild against SDL_gfx 2.0.16.

* Wed Mar 28 2007 Wart <wart@kobold.org> 0.7.9-3
- Enable use of $RPM_OPT_FLAGS

* Fri Mar 9 2007 Wart <wart@kobold.org> 0.7.9-2
- Clean up desktop file categories
- Use upstream's desktop file and icon

* Sat Feb 17 2007 Wart <wart@kobold.org> 0.7.9-1
- Update to 0.7.9

* Fri Sep 1 2006 Wart <wart@kobold.org> 0.7.4-1
- Update to 0.7.4

* Fri Aug 04 2006 Wart <wart@kobold.org> 0.7.2-6
- Add 'ArcadeGame' category to .desktop file

* Fri Jun 09 2006 Wart <wart@kobold.org> 0.7.2-5
- Improve grammar in description

* Fri Jun 09 2006 Wart <wart@kobold.org> 0.7.2-4
- Fix broken path to desktop icon
- Fix typo in description

* Fri Jun 09 2006 Wart <wart@kobold.org> 0.7.2-3
- Use RPM_BUILD_ROOT consistently
- Put the wormux icon in a size-specific directory
- Removed INSTALL from the documentation files

* Fri Jun 09 2006 Wart <wart@kobold.org> 0.7.2-2
- Expanded the description
- Separated game data into a subpackage

* Fri Jun 02 2006 Wart <wart@kobold.org> 0.7.2-1
- Initial Fedora Extras package
