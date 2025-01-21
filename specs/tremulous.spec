Name:           tremulous
Version:        1.2.0
Release:        0.39.beta1%{?dist}
Summary:        First Person Shooter game based on the Quake 3 engine

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://tremulous.net
# To get the source tarball:
# svn export svn://svn.icculus.org/tremulous/tags/RELEASE_GPP1/ tremulous-1.2.beta1
# rm -rf tremulous-1.2.beta1/src/tools/lcc/
# tar -czf tremulous-1.2.0.beta1.tar.gz tremulous-1.2.beta1
Source0:        tremulous-1.2.0.beta1.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         tremulous-1.2.0-dll-overwrite.patch
Patch1:         tremulous-getstatus-dos.patch
Patch2:         tremulous-aarch64.patch
Patch3:         tremulous-i686.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  SDL-devel
BuildRequires:  speex-devel
%if ! 0%{?rhel}
BuildRequires:  speexdsp-devel
%endif
BuildRequires:  zlib-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       tremulous-data = %{version}
Requires:       hicolor-icon-theme opengl-games-utils

%description
Tremulous is a free, open source game that blends a team based FPS with elements
of an RTS. Players can choose from 2 unique races, aliens and humans. 
Players on both teams are able to build working structures in-game like an RTS.
These structures provide many functions, the most important being spawning.
The designated builders must ensure there are spawn structures or other players
 will not be able to rejoin the game after death. Other structures provide 
automated base defense (to some degree), healing functions and much more...

Player advancement is different depending on which team you are on.
As a human, players are rewarded with credits for each alien kill.
These credits may be used to purchase new weapons and upgrades from the Armoury
The alien team advances quite differently. Upon killing a human foe,
the alien is able to evolve into a new class. The more kills gained the more 
powerful the classes available.

The overall objective behind Tremulous is to eliminate the opposing team.
This is achieved by not only killing the opposing players but also 
removing their ability to respawn by destroying their spawn structures.

%prep
%setup -q -n tremulous-1.2.beta1
%patch -P0 -p1 -b .dll-overwrite
%patch -P1 -p1 -b .getstatus-dos
%patch -P2 -p1 -b .aarch64
%patch -P3 -p1 -b .i686

# Rip out the bundled libraries and use the
# system versions instead
rm -r src/SDL12 src/AL src/libcurl src/libspeex src/libs

%build
# This package uses top level ASM constructs which are incompatible with LTO.
# Top level ASMs are often used to implement symbol versioning.  gcc-10
# introduces a new mechanism for symbol versioning which works with LTO.
# Converting packages to use that mechanism instead of toplevel ASMs is
# recommended.
# Disable LTO
%define _lto_cflags %{nil}

# the CROSS_COMPILING=1 is a hack to not build q3cc and qvm files
# since we've stripped out q3cc as this is not Free Software.
make %{?_smp_mflags} \
    OPTIMIZE="$RPM_OPT_FLAGS -fno-strict-aliasing -ffast-math" \
    DEFAULT_BASEDIR=%{_datadir}/%{name} USE_CODEC_VORBIS=1 \
    USE_LOCAL_HEADERS=0 BUILD_GAME_SO=0 GENERATE_DEPENDENCIES=0 \
    CROSS_COMPILING=1 USE_INTERNAL_SPEEX=0 USE_INTERNAL_ZLIB=0

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 build/release-linux-*/tremded.* \
  $RPM_BUILD_ROOT%{_bindir}/tremded
install -m 0755 build/release-linux-*/tremulous.* \
  $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

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
EmailAddress: #tremulous on freenode
SentUpstream: 2014-09-23
-->
<application>
  <id type="desktop">tremulous.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Tremulous is a free, open source game that blends a team based FPS with
      elements of an RTS.
    </p>
    <p>
      Players can choose from 2 unique races, aliens and humans.
      Players on both teams are able to build working structures in-game like an
      RTS.
    </p>
  </description>
  <url type="homepage">http://www.tremulous.net</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/b.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/c.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/d.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/e.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/tremulous.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/tremulous.desktop

%files
%license COPYING GPL
%{_bindir}/%{name}*
%{_bindir}/tremded
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.39.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-0.38.beta1
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.37.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.36.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.35.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.34.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.33.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Daniel Rusek <mail@asciiwolf.com> - 1.2.0-0.32.beta1
- Set PrefersNonDefaultGPU to true

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.31.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.30.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.29.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 AsciiWolf <mail@asciiwolf.com> - 1.2.0-0.28.beta1
- Update desktop file

* Fri Aug 21 2020 AsciiWolf <mail@asciiwolf.com> - 1.2.0-0.27.beta1
- Use new icon

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.26.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Jeff Law <law@redhat.com> - 1.2.0-0.25.beta1
- Disable LTO

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.24.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.23.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.22.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.21.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.20.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.19.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.18.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.17.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.16.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Pete Walter <pwalter@fedoraproject.org> - 1.2.0-0.15.beta1
- Fix FTBFS (#1240076)
- Spec clean up
- Validate appdata and desktop files

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.14.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.2.0-0.13.beta1
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.12.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-0.11.beta1
- Add patch for aarch64 support

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.10.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.9.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.8.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.2.0-0.7.beta1
- Remove vendor tag from desktop file
- spec clean up

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.6.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Jan Kaluza <jkaluza@redhat.com> - 1.2.0-0.5.beta1
- fix #806980 - fixed CVE-2010-5077

* Thu Feb 23 2012 Jan Kaluza <jkaluza@redhat.com> - 1.2.0-0.4.beta1
- fix #796362 - fixed CVE-2011-2764 and CVE-2011-3012

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 17 2010 Jan Kaluza <jkaluza@redhat.com> - 1.2.0-0.1.beta1
- update to 1.2.0 beta
- fix #602374 - tremulous works on x86_64 now

* Sun Aug 16 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.1.0-10
- Switch to openal-soft

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-7
- Fix Patch0:/%%patch mismatch.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-6
- Autorebuild for GCC 4.3

* Wed Sep 26 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.0-5
- Update syslibs patch to make the system libjpeg use tremulous' Malloc and
  Free functions, instead of the libc ones

* Mon Sep 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.0-4
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.0-3
- Update License tag for new Licensing Guidelines compliance

* Mon Sep  4 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.0-2
- Various small packaging improvements (see bug 204121)

* Fri Aug 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.0-1
- Initial Fedora packaging (based on work from Matthias and Wart)
