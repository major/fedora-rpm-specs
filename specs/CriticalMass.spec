Name:           CriticalMass
Version:        1.5
Release:        39%{?dist}
Summary:        SDL/OpenGL space shoot'em up game also known as critter
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://criticalmass.sourceforge.net/critter.php
Source0:        http://downloads.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         CriticalMass-1.0.2-res-change-rh566533.patch
Patch1:         CriticalMass-1.5-libpng15.patch
Patch2:         CriticalMass-1.5-gcc47.patch
Patch3:         CriticalMass-1.5-cflags.patch
Patch4:         CriticalMass-1.5-gcc6.patch
Patch5:         CriticalMass-1.5-ftbfs.patch
BuildRequires:  gcc-c++
BuildRequires:  SDL_image-devel SDL_mixer-devel libpng-devel curl-devel
BuildRequires:  tinyxml-devel desktop-file-utils libtool
BuildRequires: make
Requires:       hicolor-icon-theme opengl-games-utils
# Also known as critter, so make "yum install critter" work
Provides:       critter = %{version}-%{release}

%description
Critical Mass (aka Critter) is an SDL/OpenGL space shoot'em up game. Your
world has been infested by an aggressive army of space critters. Overrun and
unprepared, your government was unable to defend its precious resources. As
a last effort to recapture some of the "goodies", you have been placed into
a tiny spacecraft and sent after them.


%prep
%autosetup -p1
sed -i 's/curl-gnutls/curl/g' configure.in
touch NEWS README AUTHORS ChangeLog
autoreconf -ivf


%build
%configure
make %{?_smp_mflags}


%install
%make_install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/critter-wrapper

# remove unwanted utility
rm $RPM_BUILD_ROOT%{_bindir}/Packer

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 critter.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps

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
EmailAddress: crittermail2005@telus.net
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">CriticalMass.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A top-down space shoot-em-up game</summary>
  <description>
    <p>
      Critical Mass (also known as Critter) is a top-down shoot-em-up game where your home world
      has been infested by an aggressive army of space critters and
      you are required to pilot a small spacecraft to destroy them all.
    </p>
  </description>
  <url type="homepage">http://criticalmass.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://criticalmass.sourceforge.net/images-critter/pics.v100/snap09.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap17.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap13.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap04.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap00.jpeg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%doc Readme.html TODO
%license COPYING
%{_bindir}/critter*
%{_datadir}/Critical_Mass
%{_mandir}/man6/critter.6*
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/critter.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-38
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 16 2019 Hans de Goede <hdegoede@redhat.com> - 1.5-24
- Fix FTBFS (rhbz#1674575)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-20
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb  2 2016 Hans de Goede <hdegoede@redhat.com> - 1.5-16
- Fix FTBFS with gcc6
- Add Keywords to .desktop file

* Thu Jun 18 2015 Hans de Goede <hdegoede@redhat.com> - 1.5-15
- Fix FTBFS with hardening by patching configure to not override the CFLAGS

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.5-13
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 1.5-9
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Wed May  1 2013 Hans de Goede <hdegoede@redhat.com> - 1.5-8
- run autoreconf for aarch64 support (rhbz#925196)

* Fri Feb 22 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5-7
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Hans de Goede <hdegoede@redhat.com> - 1.5-3
- Fix building with gcc-4.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 10 2011 Hans de Goede <hdegoede@redhat.com> - 1.5-1
- New upstream release 1.5 (rhbz#766117)

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.2-10
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 12 2010 Hans de Goede <hdegoede@redhat.com> 1.0.2-8
- Fix crash when trying to change resolution to a resolution too big for
  the monitor (#566533)
- Fix misdetection of available resolutions (they were all given the width
  of the highest resolution)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.2-5
- Force proper use of RPM_OPT_FLAGS during build

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2-4
- Autorebuild for GCC 4.3

* Fri Jan  4 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.2-3
- Fix build with gcc 4.3

* Sat Dec  1 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.2-2
- Use system version of tinyxml
- Some other small specfile cleanups
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Thu Nov 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.2-1
- Initial Fedora Package
