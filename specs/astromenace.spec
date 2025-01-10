Name: astromenace
Version:  1.4.2
Release:  11%{?dist}
Summary: Hardcore 3D space shooter with spaceship upgrade possibilities  

License: GPL-3.0-only
URL: http://www.viewizard.com/
Source0: https://github.com/viewizard/astromenace/archive/%{version}-1781/%{name}-%{version}.tar.gz
Source1: astromenace.desktop
Source2: astromenace.png
Patch0: includes.patch
Patch1: astromenace-gcc13.patch
Patch2: 39.patch
ExcludeArch: ppc64 s390x

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake, SDL2-devel, libogg-devel
BuildRequires: libvorbis-devel, libjpeg-devel, desktop-file-utils
BuildRequires: openal-soft-devel freealut-devel
BuildRequires: glew-devel
BuildRequires: libXinerama-devel
BuildRequires: freetype-devel
BuildRequires: linux-libertine-fonts
BuildRequires: ninja-build
Requires: linux-libertine-fonts
Requires: opengl-games-utils

%description
Space is a vast area, an unbounded territory where it seems there is a 
room for everybody, but reversal of fortune put things differently. The 
hordes of hostile creatures crawled out from the dark corners of the
universe, craving to conquer your homeland. Their force is compelling,
their legions are interminable. However, humans didn't give up without
a final showdown and put their best pilot to fight back. These malicious
invaders chose the wrong galaxy to conquer and you are to prove it! 
Go ahead and make alien aggressors regret their insolence.

%prep
%setup -qn %{name}-%{version}-1781

%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1

%build
%cmake %_vpath_srcdir -G Ninja -DDATADIR="%{_prefix}/share/astromenace"
%cmake_build

%__cmake_builddir/astromenace --pack --rawdata=./gamedata --dir=./

%install
mkdir -p  %{buildroot}%{_bindir}
install -m 755 %__cmake_builddir/astromenace %{buildroot}%{_bindir}/astromenace
mkdir -p %{buildroot}%{_datadir}/astromenace
install -m 644 gamedata.vfs %{buildroot}%{_datadir}/astromenace/
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

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
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
EmailAddress: viewizard@viewizard.com
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">astromenace.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fast paced and intense 3D scrolling space shooter</summary>
  <description>
    <p>
      Astromenace is a 3D scrolling space shooter with amazing graphics and
      intense gameplay.
    </p>
    <p>
      You have a range of vehicles to choose from and numerous weapons that can
      be upgraded as you repel wave after wave of spaceships and dodge space
      objects.
    </p>
  </description>
  <url type="homepage">http://www.viewizard.com/</url>
  <screenshots>
    <screenshot type="default">http://www.viewizard.com/astromenace/am3.jpg</screenshot>
    <screenshot>http://www.viewizard.com/astromenace/am6.jpg</screenshot>
    <screenshot>http://www.viewizard.com/astromenace/am10.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
%{_bindir}/astromenace
%{_bindir}/%{name}-wrapper
%doc CHANGELOG.md LICENSE.md README.md docs/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/astromenace.desktop
%{_datadir}/icons/hicolor/64x64/apps/astromenace.png
%{_datadir}/astromenace/

%changelog
* Wed Jan 08 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.4.2-11
- Patch for GCC 15

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4.2-6
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.4.2-1
- 1.4.2-1781

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-7
- CMake fixes from drizt72@zoho.eu

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-3
- Adapt for flatpak.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- 1.4.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.4.0-1
- 1.4.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.2-13
- Remove obsolete scriptlets

* Tue Aug 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.3.2-12
- Exclude s390x.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Jon Ciesla <limburgher@gmail.com> - 1.3.2-9
- Exclude ppc64.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.3.2-4
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Jon Ciesla <limburgher@gmail.com> - 1.3.2-1
- 1.3.2, Ubuntu fonts dropped upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.1-2
- Multiple minor fixes from 1.3.2, BZ 966772.

* Thu Mar 21 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.1-1
- 1.3.1.
- Drop desktop vendor tag.
- Obsolete/provide -data.
- Using modified tarball and patch to avoid Ubuntu Font License, non-free.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.2-19
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.2-18
- rebuild against new libjpeg

* Sun Sep 30 2012 Jon Ciesla <limburgher@gmail.com> - 1.2-17
- Patch for crash starting level 2, BZ 832142.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 18 2009 Hans de Goede <hdegoede@redhat.com> - 1.2-13
- Switch to openal-soft

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  8 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.2-11
- Build with $RPM_OPT_FLAGS (use %%cmake macro), parallel make.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 06 2008 Jon Ciesla <limb@jcomserv.net> - 1.2-9
- Update to 080519 source release.
- updated programmdir patch.

* Fri Feb 15 2008 Jon Ciesla <limb@jcomserv.net> - 1.2-8
- Update to 080115 source release.
- Dropped stuckmouse patch, fixed upstream.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 1.2-7
- GCC 4.3 rebuild.

* Tue Dec 11 2007 Jon Ciesla <limb@jcomserv.net> - 1.2-6
- Added patch to set default data path, BZ 393751.

* Fri Dec 07 2007 Jon Ciesla <limb@jcomserv.net> - 1.2-5
- Added patch to fix stuck mouse, BZ 327671.

* Thu Dec 06 2007 Jon Ciesla <limb@jcomserv.net> - 1.2-4
- Patch to fix default video mode issue.
- Update to 071105 source release.

* Mon Oct 08 2007 Jon Ciesla <limb@jcomserv.net> - 1.2-3
- Added support for opengl-games-utils, .desktop cleanup.

* Fri Oct 05 2007 Jon Ciesla <limb@jcomserv.net> - 1.2-2
- Used main upstream sources, not sf.net fork.
- Patched for gamelang paths.

* Tue Oct 02 2007 Jon Ciesla <limb@jcomserv.net> - 1.2-1
- create.
