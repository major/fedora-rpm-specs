Name:           netpanzer
Version:        0.8.7
Release:        27%{?dist}
Summary:        An Online Multiplayer Tactical Warfare Game

License:        GPL-2.0-or-later
URL:            http://www.netpanzer.info
Source0:	http://www.netpanzer.info/Download/NetPanzer/Releases/0.8.7/netpanzer-0.8.7-source.zip
Source1:	netpanzer.desktop
Patch4:         netpanzer-0.8.2-MapSelectionView-memory.patch
Patch6:         netpanzer-0.8.7-ccflags.patch
Patch8:		netpanzer-0.8.7-syslibs.patch
Patch9:         netpanzer-python3.patch

BuildRequires:  gcc-c++
BuildRequires:  physfs-devel >= 0.1.9, desktop-file-utils, doxygen, python3-scons
BuildRequires:  SDL-devel >= 1.2.5, SDL_mixer-devel >= 1.2, SDL_image-devel >= 1.2
BuildRequires:  compat-lua-devel
Obsoletes:      netpanzer-data <= 0.8
Provides:       netpanzer-data = %{version}-%{release}


%description
netPanzer is an online multiplayer tactical warfare game designed for FAST
ACTION combat. Gameplay concentrates on the core -- no resource management is
needed. The game is based on quick tactical action and unit management in
real-time. Battles progress quickly and constantly as destroyed players respawn
with a set of new units. Players can join or leave multiplayer games at any
time.

%prep
%setup -qcn netpanzer-0.8.7
%patch -P4 -p0
%patch -P6 -p1
%patch -P8 -p1
%patch -P9 -p0
rm -r src/Lib/lua src/Lib/physfs

%build
CCFLAGS="%{optflags} -std=c++14" scons datadir=%{_datadir}/netpanzer %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 netpanzer $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr cache/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr maps/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr pics/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr powerups/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr scripts/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr units/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr wads/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr sound/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/

# Install desktop item
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/netpanzer.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/netpanzer.xpm

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mv netpanzer.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

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
<!-- Copyright 2014 William Moreno Reyes <williamjmoreno@gmail.com> -->
<!--
EmailAddress: admin@netpanzer.info
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">netpanzer.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Multiplayer war game in real time</summary>
  <description>
    <p>
      Play a on line tactical game over the internet or a LAN, with one vs one
      option using a direct connect or modem.
      netPanzer in designed for a fast game mode, without the need of collect
      resources, any player can play until his last unit is destroyed.
    </p>
  </description>
  <url type="homepage">http://netpanzer.berlios.de</url>
  <screenshots>
    <screenshot type="default">http://www.netpanzer.info/public/netpanzer.info/images/netpanzer-game/screenshot63.jpg</screenshot>
  </screenshots>
</application>
EOF


%files
%doc COPYING README* docs/
%{_bindir}/netpanzer
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/netpanzer.desktop
%{_datadir}/icons/hicolor/48x48/apps/netpanzer.png
%{_datadir}/netpanzer

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.7-22
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 0.8.7-15
- Use C++14 as this code is not C++17 ready

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.7-13
- Fix FTBTS.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.8.7-11
- Remove obsolete requirements for %%post/%%postun scriptlets

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.8.7-8
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.8.7-2
- OPT_FLAGS fix, BZ 1402803.

* Mon Nov 14 2016 Jon Ciesla <limburgher@gmail.com> - 0.8.7-1
- 0.8.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.4-12
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.8.4-11
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.8.4-8
- Don't ship svn files

* Wed Mar 26 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.8.4-7
- Build with system compat-lua instead of bundled one

* Tue Mar 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.8.4-6
- Build with system physfs instead of bundled one (#1076808)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.4-4
- Drop desktop vendor tag.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for c++ ABI breakage

* Thu Jan 05 2012 Jon Ciesla <limburgher@gmail.com> - 0.8.4-1
- 0.8.4.
- Patch for gcc 4.7.0.

* Mon Feb 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.8.3.svn612010-4
- Build with $RPM_OPT_FLAGS (#580241).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3.svn612010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Jon Ciesla <limb@jcomserv.net> 0.8.3-2
- Correct checkout for 0.8.3 per upstream, BZ598120.
- Scons fixes.
- Added sound back in.

* Wed Mar 31 2010 Jon Ciesla <limb@jcomserv.net> 0.8.3-1
- New upstream release.
- Several patches upstreamed.
- Moved from jam to scons.

* Tue Aug 25 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.8.2-8
- Rebuild for new libphysfs API bump to fix broken deps

* Thu Aug 20 2009 Jon Ciesla <limb@jcomserv.net> 0.8.2-7
- Rebuild for openal-soft.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Jon Ciesla <limb@jcomserv.net> 0.8.2-4
- Fixed coreutils deps, BZ 475920.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> 0.8.2-3
- GCC 4.3 rebuild.

* Thu Jan 10 2008 Jon Ciesla <limb@jcomserv.net> 0.8.2-2
- Added memory, algorithm patches.

* Wed Aug 29 2007 Jon Ciesla <limb@jcomserv.net> 0.8.2-1
- Bumped to 0.8.2.
- Merged in and obsoleted/provided netpanzer-data to follow upstream.
- Patch to correct upstream .desktop file.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> 0.8.1-2
- License tag correction.

* Thu Mar 01 2007 Jon Ciesla <limb@jcomserv.net> 0.8.1-1
- Bumped to upstream
- Pulled gcc 4.1 patch, fixed upstream
- Pulled CVE 2006-2575, 2005-2295 patches, fixed upstream
- Updated netpanzer-data RQ to allow update of app without update of data.

* Wed Sep 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-5
- Rebuilt for FC6

* Thu Jun  8 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-4
- Fix Remote Server Termination vulnerability (CVE 2006-2575)
- Add proper packet size check (CVE 2005-2295) (patch from Gentoo)

* Thu May  4 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-3
- Changed netpanzer.png to comply with freedesktop.org standards.
- Added scripts to update the icon cache after installing

* Mon May  1 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-2
- Changed Package's RPM Group
- Fixed Changelog entries to specify versions
- Stripped '\r' EOL from RELNOTES file
- Added COPYING file

* Mon May  1 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-1
- Initial RPM release
