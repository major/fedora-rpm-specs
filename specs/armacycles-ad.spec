%global forgeurl https://gitlab.com/armagetronad/armagetronad/
%global tag v0.2.9.2.3

%forgemeta

Name: armacycles-ad
Version: 0.2.9.2.3
Release: 3%{?dist}
Summary: A lightcycle game in 3D

License: GPL-2.0-or-later
URL: %{forgeurl}
Source0: %{forgesource}
Source1: armacycles-logo.jpg
Source2: armacycles-ad.desktop

BuildRequires: libxml2-devel >= 2.6.12, SDL_image-devel, SDL_mixer-devel
BuildRequires: libpng-devel, desktop-file-utils, autoconf, automake, gcc-c++
BuildRequires: make
Requires: libxml2 >= 2.6.12, hicolor-icon-theme

%description
In this game you ride a lightcycle; that is a sort of motorbike that
cannot be stopped and leaves a wall behind it. The main goal of the game
is to make your opponents' lightcycles crash into a wall while avoiding
the same fate.
The focus of the game lies on the multiplayer mode, but it provides
challenging AI opponents for a quick training match.


#dedicated server specification
%package dedicated
Summary: Dedicated server for Armacycles Advanced
requires: libxml2 >= 2.6.12

%Description dedicated
This is a special lightweight server for Armacycles Advanced; it can
be run on a low-spec machine and await connections from
the internet and/or the LAN.


%prep
%forgesetup

#insert modified logo
cp %{SOURCE1} textures/title.jpg
# remove krawall logo
rm -f armagetronad-0.2.8.2.1/textures/KGN*

./bootstrap.sh

%build
configure_flags="--disable-sysinstall --disable-games --disable-uninstall"

export progtitle="Armacycles Advanced"
export progname=armacyclesad

mkdir -p bindist
pushd bindist
# <sigh> %%configure really should support this in an easier way
echo -e '#!/bin/bash\nexec ../configure "$@"\n' > configure
chmod +x configure
%configure $configure_flags
make %{?_smp_mflags}
popd

mkdir -p bindist-dedicated
pushd bindist-dedicated
cp -a ../bindist/configure .
%configure $configure_flags --disable-glout
make %{?_smp_mflags}
popd


%install
pushd bindist
# uninstall_location=foobar works around a bug triggered by --disable-uninstall
make install DESTDIR=$RPM_BUILD_ROOT uninstall_location=foobar
rm -r $RPM_BUILD_ROOT%{_datadir}/armacyclesad/desktop
popd

pushd bindist-dedicated
make install DESTDIR=$RPM_BUILD_ROOT uninstall_location=foobar
rm -r $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/desktop
popd

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
BugReportURL: https://bugs.launchpad.net/armagetronad/+bug/1323628
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">armacycles-ad.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>3D motorcycle battle</summary>
  <description>
    <p>
      Armagetron is a 3D Tron-inspired game where the player controls a motorcycle
      that emits a immovable wall behind it.
      Gameplay consists of 2 of these cycles battling to trap each other to
      force their opponent to crash into the wall.
    </p>
  </description>
  <url type="homepage">http://armagetronad.sf.net</url>
  <screenshots>
    <screenshot type="default">http://armagetronad.org/screenshots/screenshot_2.png</screenshot>
    <screenshot>http://armagetronad.org/screenshots/screenshot_5.png</screenshot>
  </screenshots>
</application>
EOF

# Install icons and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 desktop/icons/16x16/armagetronad.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
install -p -m 644 desktop/icons/32x32/armagetronad.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 desktop/icons/48x48/armagetronad.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}

#remove extraneous scripts
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad/scripts/relocate
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad/language/update.py

rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/scripts/relocate
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/scripts/rcd_config
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/scripts/rcd_startstop
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/language/update.py


%files
%doc %{_datadir}/doc/armacyclesad
%config(noreplace) %{_sysconfdir}/armacyclesad
%{_bindir}/armacyclesad
%{_datadir}/armacyclesad
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/armacycles-ad.desktop
%{_datadir}/icons/hicolor/*/apps/armagetronad.png

%files dedicated
%doc COPYING bindist-dedicated/src/doc/
%exclude %{_datadir}/doc/armacyclesad-dedicated
%config(noreplace) %{_sysconfdir}/armacyclesad-dedicated
%{_bindir}/armacyclesad-dedicated
%{_datadir}/armacyclesad-dedicated


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.2.9.2.3-1
- 0.2.9.2.3

* Tue Mar 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.2.9.2.1-1
- 0.2.9.2.1

* Mon Feb 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.2.9.1.1-4
- Patch to fix network play.

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.2.9.1.1-1
- 0.2.9.1.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.2.9.1.0-6
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.2.9.1-1
- 0.2.9.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.2.8.3.5-1
- 0.2.8.3.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.8.3.4-12
- Update to support flatpak.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.2.8.3.4-9
- Upstream patches to fix crash, cleanup.

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.2.8.3.4-8
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.8.3.4-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.4-1
- Upstream gcc fixes.

* Wed Aug 10 2016 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.3-4
- Fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.3-1
- Upstream security release.
- Dropped libpng16 patch.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.8.3.2-11
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.2.8.3.2-10
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.2-8
- Fix FTBFS, BZ 1105971.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.2-6
- Fix date and libpng for FTBFS.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.2-4
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.2-2
- Add hardened build.

* Mon Mar 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.2-1
- New upstream.
- gcc patch upstreamed.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3.1-8
- Rebuilt for c++ ABI breakage

* Wed Jan 18 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.1-7
- Patch for new gcc.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Jon Ciesla <limburgher@gmail.com> - 0.2.8.3.1-5
- Patch for new libpng.

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.8.3.1-4
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 15 2010 Jon Ciesla <limb@jcomserv.net> - 0.2.8.3.1-2
- Added license file to subpackage to meet new guidelines.

* Thu May 06 2010 Jon Ciesla <limb@jcomserv.net> - 0.2.8.3.1-1
- New upstream bugfix release.

* Fri Jan 22 2010 Jon Ciesla <limb@jcomserv.net> - 0.2.8.3-2
- New upstream, 0.2.8.3 final.

* Fri Oct 16 2009 Jon Ciesla <limb@jcomserv.net> - 0.2.8.3-1.rc4
- New upstream.

* Fri Sep 18 2009 Jon Ciesla <limb@jcomserv.net> - 0.2.8.3-1.rc3
- New upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3-1.rc2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Jon Ciesla <limb@jcomserv.net> - 0.2.8.3-1.rc2
- New upstream.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 04 2008 Jon Ciesla <limb@jcomserv.net> - 0.2.8.2.1-6
- string.h, cstdlib, memory patches.

* Fri Aug 31 2007 Jon Ciesla <limb@jcomserv.net> - 0.2.8.2.1-5
- Dropped extraneous script.
- Removed .desktop version, Application category.

* Thu Aug 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> - 0.2.8.2.1-4
- Use %%configure instead of calling Configure ourselves, this fixes the
  configuration files being put in /usr/etc (now in /etc)
- Wrap all lines > 80 chars
- Use URL for Source0
- Install all size icons
- Fix dedicated package Summary (CycleWeasel > Armacycles Ad)
- Don't use strange x.final.y release field, for final versions normal
  release fields should be used
- Add --disable-uninstall to %%configure flags, people should use yum / pirut
  to uninstall packages, not some upstream provided script
- Remove unused /usr/share/armacyclesad-dedicated/desktop dir
- Replace SDL_mixer, SDL_image, libpng BuildRequires by their -devel parts

* Tue Aug 14 2007 Jon Ciesla <limb@jcomserv.net> - 0.2.8.2.1-1.final.3
- Multiple review fixes.

* Thu Aug 09 2007 Jon Ciesla <limb@jcomserv.net> - 0.2.8.2.1-1.final.2
- Added desktop file and icon, fixed summary.

* Mon Jul 16 2007 Jon Ciesla <limb@jcomserv.net> - 0.2.8.2.1-1.final.1
- Initial package, based on upstream spec.
