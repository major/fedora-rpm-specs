#
# Fedora spec file for package funguloids
#
# Adapted from the openSUSE spec file and patches, which are:
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           funguloids
Version:        1.06
Release:        47%{?dist}
Summary:        Space-Flying-Mushroom-Picking-Simulator game
License:        zlib
URL:            http://funguloids.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-linux-%{version}-4.tar.bz2
# From Debian, as the openSUSE srpm has v1.4, which lacks a clear license
Source1:        mpak.py
# README.openSUSE modified for Fedora
Source2:        README.Fedora
Source3:        funguloids.desktop
Source4:        funguloids.png
# Shamelessly borrowed from Debian
Source5:        funguloids.6
# All the below patches where taken from the openSUSE srpm
# funguloids-ogre-1.6.patch has been extended with some bits from the more
# complete ogre-1.6.1.patch from Debian
Patch0:         %{name}-size_chunks_reverse.patch
Patch1:         %{name}-alc_error.patch
Patch2:         %{name}-missing_includes.patch
Patch3:         %{name}-ogre-1.6.patch
Patch4:         %{name}-lua.patch
Patch5:         %{name}-destdir.patch
Patch6:         %{name}-honor_autotools_paths.patch
Patch7:         %{name}-strcmp.patch
Patch8:         %{name}-optional_cg.patch
Patch9:         %{name}-ogre-1.7.0.patch
Patch10:        %{name}-gcc47.patch
Patch11:        %{name}-ogre-1.8.patch
# Fix for Lua 5.2
Patch12:	%{name}-lua-5.2.patch
# Build with ogre-1.9
Patch13:        %{name}-ogre-1.9.patch
BuildRequires:  automake desktop-file-utils gcc-c++ python3
BuildRequires:  freealut-devel libvorbis-devel lua-devel
BuildRequires:  ogre-devel >= 1.9 ois-devel openal-devel
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Never before has collecting mushrooms been this mildly entertaining. At least
not in outer space. It's more of a lifestyle than a game, really. Now with
graphics and sound, too!

Seriously though, we like to think the game as a
space-flying-mushroom-picking-simulator. Well no, "Those Funny Funguloids!" is
actually a nice little piece of entertainment. You collect mushrooms, bring them
back to your home base and profit! That's the basic idea in a nutshell. It has
smooth, appealing 3d graphics and nice atmospheric sound effects. Go ahead and
try it out - it has sounds too!


%prep
%setup -q -n %{name}
%patch -P0
%patch -P1
%patch -P2
%patch -P3
%patch -P4
%patch -P5
%patch -P6
%patch -P7
%patch -P8
%patch -P9
%patch -P10
%patch -P11
%patch -P12 -p1
%patch -P13 -p1
autoreconf -fi
# docs fixup
sed -i 's/\r$//' bin/docs/stylesheet.css
sed -i 's/\r$//' README
# mpk file fixup
%{SOURCE1} -e -f bin/bootstrap.mpk -p _bootstrap
%{SOURCE1} -e -f bin/funguloids.mpk -p _gamedata
sed -ri '/^[A-Z]/ s/(.*)/overlay \1/' _bootstrap/*.overlay _gamedata/*.overlay
sed -ri '/^[A-Z]/ s/(.*)/particle_system \1/' _gamedata/*.particle
# This last one looks like a bug in ogre, should be removed when fixed
# The problem is that green and blue mushrooms have a square instead of a glow
sed -ri 's/^(\t\t\t)(texture_unit) 1/\1\2\n\1{\n\1}\n\1\2/' _gamedata/materials.material
%{SOURCE1} -c -f bin/bootstrap.mpk _bootstrap/*
%{SOURCE1} -c -f bin/funguloids.mpk _gamedata/*
rm -rf _bootstrap _gamedata


%build
%configure --docdir=%{_pkgdocdir} --without-mad --without-fmod
make %{?_smp_mflags}


%install
%make_install
cp -p README %{SOURCE2} $RPM_BUILD_ROOT%{_pkgdocdir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{48x48,256x256}/apps
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man6

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
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/funguloids/support-requests/2/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">funguloids.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>3D casual game</summary>
  <description>
    <p>
      Those Funny Funguloids! 3d is a casual game where you must travel through
      various worlds offered by the game and capture all the mushrooms you find.
      Beware of enemies, they will do anything to make you fail!
    </p>
  </description>
  <url type="homepage">http://funguloids.sourceforge.net</url>
  <screenshots>
    <screenshot type="default">http://funguloids.sourceforge.net/shot02.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot01.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot03.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot04.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot06.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot07.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot05.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot08.jpg</screenshot>
  </screenshots>
</application>
EOF


%files
%doc %{_pkgdocdir}
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.06-32
- Rebuilt for Boost 1.69

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.06-31
- Rebuild with fixed binutils

* Mon Jul 30 2018 Hans de Goede <hdegoede@redhat.com> - 1.06-30
- Renable debuginfo now that the elfutils bug causing issues has been fixed

* Sun Jul 29 2018 Hans de Goede <hdegoede@redhat.com> - 1.06-29
- Convert mpak.py util to python3 (and adjust BuildRequires to match)
- This fixes the Fedora 29 FTBFS (rhbz#1604019)
- Disable debuginfo generation for now to work around rhbz#1609577

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.06-27
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.06-25
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.06-24
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 1.06-21
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 1.06-19
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.06-17
- Rebuilt for Boost 1.60
- Add %%license.

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.06-16
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 1.06-15
- Rebuilt for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Bruno Wolff III <bruno@wolff.to> - 1.06-13
- Verify that funguloids is no longer FTBFS

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.06-12
- Add an AppData file for the software center

* Wed Feb 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.06-11
- Rebuild for boost-1.57.0.
- Use %%_pkgdocdir instead of %%_maindocdir.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Hans de Goede <hdegoede@redhat.com> - 1.06-9
- Rebuild for ogre 1.9

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.06-7
- rebuild for boost 1.55.0

* Sun Sep 15 2013 Hans de Goede <hdegoede@redhat.com> - 1.06-6
- Fix docdir for unversioned docdir F-20 change (rhbz#993763)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 1.06-3
- Rebuild for boost 1.54.0

* Wed May 29 2013 Tom Callaway <spot@fedoraproject.org> - 1.06-2
- fix build against lua-5.2 (patch should also be compat with lua 5.1)

* Mon May 13 2013 Hans de Goede <hdegoede@redhat.com> - 1.06-1
- Initial Fedora package based on openSUSE pkg + some Debian bits
