# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007 Hans de Goede <j.w.r.degoede@hhs.nl>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

Name:           BlockOutII
Version:        2.5
Release:        31%{?dist}
Summary:        A free adaptation of the original BlockOut DOS game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.blockout.net/blockout2/
Source0:        http://downloads.sourceforge.net/blockout/bl25-src.tar.gz
Source1:        http://downloads.sourceforge.net/blockout/bl25-linux-x86.tar.gz
Source2:        %{name}.desktop
Patch0:         BlockOutII-2.3-syslibs.patch
Patch1:         BlockOutII-2.3-bl2Home.patch
Patch2:         BlockOutII-2.3-restore-resolution.patch
Patch3:         BlockOutII-2.3-libpng15.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1037001
Patch4:         BlockOutII-2.3-format-security.patch
Patch5:		BlockOutII-c99.patch
BuildRequires:  SDL_mixer-devel alsa-lib-devel libpng-devel
BuildRequires:  make gcc-c++ desktop-file-utils ImageMagick
Requires:       hicolor-icon-theme opengl-games-utils

%description
BlockOut II is a free adaptation of the original BlockOut
DOS game edited by California Dreams in 1989. BlockOut II
has the same features than the original game with few graphic
improvements. The score calculation is also nearly similar to
the original game. BlockOut II has been designed by an addicted
player for addicted players. BlockOut II is an open source
project available for both Windows and Linux.

Blockout is a registered trademark of Kadon Enterprises, Inc.,
used by permission for the BlockOut II application by Jean-Luc
Pons.

%prep
%setup -q -n BL_SRC -a 1
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

# Convert the README and put it somewhere we can use it from %%doc
iconv -f ISO8859-1 -t UTF8 BlockOut/README.txt > t;
sed -i 's/\r//' t
touch -r BlockOut/README.txt t
mv t BlockOut/README.txt

# Remove bundled png library
rm -r ImageLib/src/png/png ImageLib/src/png/zlib


%build
pushd ImageLib/src
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -Dlinux -c" \
    CXXFLAGS="$RPM_OPT_FLAGS -Dlinux -c"
popd

pushd BlockOut
make %{?_smp_mflags} \
    CXXFLAGS="$RPM_OPT_FLAGS -Dlinux `sdl-config --cflags` -I../ImageLib/src -c" \
    ADD_LIBS="-L../ImageLib/src -limagelib -lpng -lz"
popd

convert BlockOut/block_icon.ico BlockOutII.png
convert BlockOutII-2.png -resize 64x64 BlockOutII-64x64.png


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/images
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

install -m 755 BlockOut/blockout $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
install -p -m 644 blockout/images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images
install -p -m 644 blockout/sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
install -D -p -m 644 %{name}-1.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -D -p -m 644 %{name}-0.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -p -m 644 %{name}-2.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -p -m 644 %{name}-64x64.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: jlp_38@yahoo.com
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">BlockOutII.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A free adaptation of the original BlockOut game</summary>
  <description>
    <p>
      BlockOut II is a game where the player moves and rotate 3D polycubes
      that are constantly falling with the objective of clearing layers of
      blocks.
      It is a free adaptation of the original BlockOut game released in 1989.
    </p>
  </description>
  <url type="homepage">http://www.blockout.net/blockout2/</url>
  <screenshots>
    <screenshot type="default">http://www.blockout.net/blockout2/screenshots/scr1.jpg</screenshot>
    <screenshot>http://www.blockout.net/blockout2/screenshots/scr2.jpg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF


%files
%doc BlockOut/README.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5-29
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  2 2023 Florian Weimer <fweimer@redhat.com> - 2.5-22
- C99 compatibility fix (#2157594)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Hans de Goede <hdegoede@redhat.com> - 2.5-19
- Fix FTBFS (rhbz#1987351)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5-10
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb  2 2016 Hans de Goede <hdegoede@redhat.com> - 2.5-6
- Add Keywords to .desktop file

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 2.5-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.5-3
- Add an AppData file for the software center

* Mon Oct 27 2014 Hans de Goede <hdegoede@redhat.com> - 2.5-2
- Found a better 48x48 icon

* Mon Oct 27 2014 Hans de Goede <hdegoede@redhat.com> - 2.5-1
- New upstream release 2.5
- Include a larger (128x128) icon (rhbz#1157498)

* Wed Oct 22 2014 Hans de Goede <hdegoede@redhat.com> - 2.4-10
- Fix crash when showing the highscore screen (rhbz#1154305)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Hans de Goede <hdegoede@redhat.com> - 2.4-7
- Fix building with -Werror=format-security (rhbz#1037001)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.4-5
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Hans de Goede <hdegoede@redhat.com> - 2.4-1
- Update to 2.4
- Fix building with new libpng

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.3-9
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3-5
- Autorebuild for GCC 4.3

* Sat Dec  1 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-4
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Thu Nov 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-3
- Fix restoration of resolution when leaving fullscreen
- Don't use macros in cvs co instructions

* Mon Nov 26 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-2
- Add missing libpng-devel BR (bz 398791)
- Add include date in CVS tarbal reproduction instructions (bz 398791)

* Sat Nov 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-1
- Initial Fedora Package based on the packman package
