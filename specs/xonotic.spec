%global _hardened_build 1
%global dpver 20230620

%global dqmirror1 http://distcache.freebsd.org/ports-distfiles/quake-data/quakesw-1.0.6.tar.gz
%global dqmirror2 https://www.libsdl.org/projects/quake/data/quakesw-1.0.6.tar.gz

Summary: Multiplayer, deathmatch oriented first person shooter
Name: xonotic
Version: 0.8.6
Release: 5%{?dist}
License: GPL-2.0-or-later and LGPL-2.0-or-later
URL: http://www.xonotic.org/
# Custom tarball:
# wget http://dl.xonotic.org/xonotic-%{version}.zip
# unzip xonotic-%{version}.zip
# cd Xonotic/source/
# cp ../misc/logos/icons_png/xonotic_256.png darkplaces/
# tar -cJf darkplaces-%{version}.tar.xz darkplaces/
Source0: darkplaces-%{version}.tar.xz
Source1: %{name}.desktop
Source10: darkplaces-quake.sh
Source11: darkplaces-quake.autodlrc
Source12: darkplaces-quake.desktop
Patch0: %{name}-gcc11.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: file
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: libjpeg-devel
%else
BuildRequires: libjpeg-turbo-devel
%endif
BuildRequires: libXext-devel 
BuildRequires: libXpm-devel
BuildRequires: libXxf86dga-devel
BuildRequires: libXxf86vm-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel
Requires: xonotic-data = %{version}
Requires: darkplaces = %{dpver}-%{release}
Requires: opengl-games-utils

%description
Xonotic is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.

%package server
Summary: Dedicated server for the Xonotic first person shooter
Requires: xonotic-data = %{version}
Requires: darkplaces-server = %{dpver}-%{release}


%description server
Xonotic is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.

This is the Xonotic dedicated server required to host network games.

%package -n darkplaces
Summary: Modified Quake engine
Version: %{dpver}
# This is necessary as these libraries are loaded during runtime
# and therefore it isn't picked up by RPM during build
Requires: zlib libvorbis libjpeg curl
Recommends: d0_blind_id

%description -n darkplaces
DarkPlaces is a modified Quake engine.

%package -n darkplaces-server
Summary: Quake engine server
Version: %{dpver}
# This is necessary as these libraries are loaded during runtime
# and therefore it isn't picked up by RPM during build
Requires: zlib curl

%description -n darkplaces-server
DarkPlaces Quake engine server.

%package -n darkplaces-quake
Summary: Multiplayer, deathmatch oriented first person shooter
Version: %{dpver}
Requires: autodownloader
Requires: opengl-games-utils
Requires: darkplaces = %{dpver}-%{release}

%description -n darkplaces-quake
Rage through levels of sheer terror and fully immersive sound and
lighting.  Arm yourself against the cannibalistic Ogre, fiendish Vore
and indestructible Schambler using letal nails, fierce Thunderbolts
and abominable Rocket and Grenade Launchers.

%package -n darkplaces-quake-server
Summary: Dedicated DarkPlaces Quake server
Version: %{dpver}
Requires: darkplaces-server = %{dpver}-%{release}

%description -n darkplaces-quake-server
DarkPlaces server required for hosting multiplayer network Quake games.


%prep
%setup -q -n darkplaces

cp %{SOURCE11} .
sed -i 's,MIRROR1,%{dqmirror1},g' $(basename %{SOURCE11})
sed -i 's,MIRROR2,%{dqmirror2},g' $(basename %{SOURCE11})

sed -i 's/\r//' darkplaces.txt
sed -i 's,/usr/X11R6/,/usr/,g' makefile makefile.inc
sed -i 's/nexuiz/xonotic/g' makefile makefile.inc

%patch -P 0 -p2

%build
export DP_FS_BASEDIR=%{_datadir}/xonotic
#export DP_CRYPTO_STATIC_LIBDIR="." 
#export DP_CRYPTO_RIJNDAEL_STATIC_LIBDIR="."
make release OPTIM_RELEASE="$RPM_OPT_FLAGS -std=gnu17" STRIP=:
make cl-xonotic OPTIM_RELEASE="$RPM_OPT_FLAGS -std=gnu17" STRIP=:
make sdl-xonotic OPTIM_RELEASE="$RPM_OPT_FLAGS -std=gnu17" STRIP=:
make sv-xonotic OPTIM_RELEASE="$RPM_OPT_FLAGS -std=gnu17" STRIP=:

%install
rm -rf %{buildroot}

# Install the main programs
mkdir -p %{buildroot}%{_bindir}
for i in darkplaces xonotic; do
        install -pm 0755 $i-glx %{buildroot}%{_bindir}/$i-glx
        install -pm 0755 $i-sdl %{buildroot}%{_bindir}/$i-sdl
        install -pm 0755 $i-dedicated %{buildroot}%{_bindir}/$i-dedicated
done
install -pm 0755 darkplaces-dedicated %{buildroot}%{_bindir}/darkplaces-dedicated

# Install the desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE12}

for s in 16 24 32 48 64 72 ; do
       install -Dpm 0644 darkplaces${s}x${s}.png \
       %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/darkplaces.png
done
install -Dpm 0655 xonotic_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/xonotic.png

ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/xonotic-sdl-wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/darkplaces-sdl-wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/darkplaces-quake-sdl-wrapper

for i in glx sdl dedicated ; do
    install -Dpm 755 %{SOURCE10} %{buildroot}%{_bindir}/darkplaces-quake-$i
done

install -Dpm 644 $(basename %{SOURCE11}) %{buildroot}%{_datadir}/darkplaces/quake.autodlrc

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/darkplaces-quake.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: Bug reports not accepted
-->
<application>
  <id type="desktop">darkplaces-quake.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fast paced deathmatch oriented first person shooter (FPS)</summary>
  <description>
    <p>
      Darkplaces-quake is a fast paced, multiplayer, deathmatch oriented shooter
      similar to the popular FPS game Quake.
    </p>
  </description>
  <url type="homepage">http://www.xonotic.org/</url>
</application>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: http://www.xonotic.org/team/contact/
SentUpstream: 2014-09-23
-->
<application>
  <id type="desktop">xonotic.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Xonotic is a free and fast-paced first person shooter which combines
      addictive, arena-style gameplay with rapid movement and a wide array of
      weapons.
    </p>
    <p>
      Xonotic is easy to learn, but hard to master! Besides thrilling action for
      the casual player, the game also provides e-sport opportunities for those
      interested in its competitive aspects.
      From mapping contests and monthly quick cups to sponsored tournaments,
      Xonotic allows every e-sport enthusiast to participate in competitions
      hosted by its open-minded community.
    </p>
    <p>
      Features such as simple items, fully customizable configs and servers, a
      functioning anticheat system, the spectator mode, and the opportunity to
      watch and record games makes Xonotic attractive to competitive players.
    </p>
  </description>
  <url type="homepage">http://www.xonotic.org/</url>
  <screenshots>
    <screenshot type="default">http://www.xonotic.org/m/uploads/2012/07/frontpage_005.jpg</screenshot>
    <screenshot>http://www.xonotic.org/m/uploads/2012/07/frontpage_006.jpg</screenshot>
    <screenshot>http://www.xonotic.org/m/uploads/2012/07/frontpage_007.jpg</screenshot>
    <screenshot>http://www.xonotic.org/m/uploads/2012/07/frontpage_008.jpg</screenshot>
    <screenshot>http://www.xonotic.org/m/uploads/2012/07/frontpage_003.jpg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%{_bindir}/xonotic-sdl-wrapper
%{_bindir}/xonotic-glx
%{_bindir}/xonotic-sdl
#%{_bindir}/blind_id
%{_datadir}/icons/hicolor/*/apps/xonotic.png
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop

%files server
%{_bindir}/xonotic-dedicated

%files -n darkplaces
%{_bindir}/darkplaces-sdl-wrapper
%{_bindir}/darkplaces-glx
%{_bindir}/darkplaces-sdl
%doc COPYING darkplaces.txt
%{_datadir}/icons/hicolor/*/apps/darkplaces.png

%files -n darkplaces-server
%doc COPYING darkplaces.txt
%{_bindir}/darkplaces-dedicated

%files -n darkplaces-quake
%{_bindir}/darkplaces-quake-glx
%{_bindir}/darkplaces-quake-sdl
%{_bindir}/darkplaces-quake-sdl-wrapper
%{_datadir}/darkplaces/
%{_datadir}/appdata/*darkplaces-quake.appdata.xml
%{_datadir}/applications/*darkplaces-quake.desktop

%files -n darkplaces-quake-server
%doc COPYING darkplaces.txt
%{_bindir}/darkplaces-quake-dedicated


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.6-1
- 0.8.6

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.5-4
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.8.5-2
- Correct date.

* Fri Jul 29 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.8.5-1
- 0.8.5

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Daniel Rusek <mail@asciiwolf.com> - 0.8.2-17
- Set PrefersNonDefaultGPU to true

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.2-13
- Implement support for generating & sending UUID

* Tue Dec 08 2020 Jeff Law <law@redhat.com> - 0.8.2-12
- Fix alignment vs size diagnostic for gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.2-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.8.2-2
- Re-enable xonotic-dedicated server.

* Tue Apr 04 2017 Kalev Lember <klember@redhat.com> - 0.8.2-1
- Update to 0.8.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Kalev Lember <klember@redhat.com> - 0.8.1-4
- Bump darkplaces version

* Fri Sep 11 2015 Jon Ciesla <limburgher@gmail.com> - 0.8.1-3
- Bump release to attempt a fix for rel-eng 6249.

* Thu Sep 10 2015 Jon Ciesla <limburgher@gmail.com> - 0.8.1-2
- Drop release Requires from dpver, BZ 1261993.

* Wed Sep 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.8.1-1
- Update to 0.8.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.8.0-3
- Add an AppData file for the software center

* Thu Mar 19 2015 Jon Ciesla <limburgher@gmail.com> - 0.8.0-2
- Temporarily disable xonotic-dedicated server to fix FTBFS.

* Sat Jan 17 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- 0.8.0 (RHBZ #1183203)

* Thu Dec 25 2014 François Cami <fcami@fedoraproject.org> - 0.7.0-5
- Fix darkplaces-quake download urls: use placeholders and variables in spec file.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-1
- 0.7.0, BZ 974029.

* Thu Feb 28 2013 Dan Horák <dan[at]danny.cz> - 0.6.0-8
- Fix build on non-x86 arches

* Fri Feb 22 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.0-7
- Fix server O/P.

* Wed Feb 20 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.0-6
- Drop sse flags to allow buildon ARM.

* Wed Feb 20 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.0-5
- Removed more macros.
- Enabled parallel build, then re-disabled, unreliable.
- Fixed server file ownership.

* Fri Feb 08 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.0-4
- Drop nexuiz name completely.
- Added jpeg BRs, neatened BRs.
- De-macroized many commands.
- Dropped dektop vendor tag.
- Preserved timestamps.

* Thu Dec 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.6.0-2
- add d0_blind_id.

* Mon Mar 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.6.0-1
- New upstream.

* Thu Jan 26 2012 Jon Ciesla <limburgher@gmail.com> - 0.5.0-1
- Initial version, based on Nexuiz 2.5.2 package.
