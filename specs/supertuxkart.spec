%global __cmake_in_source_build 1
#global rctag rc1

%global __global_ldflags %(echo "%{__global_ldflags} -lX11")

Name:           supertuxkart
Version:        1.4
Release:        11%{?dist}
Summary:        Kids 3D go-kart racing game featuring Tux
# Font licensing
# [unbundled] GNU FreeFont - GPLv3
# wqyMicroHei - GPLv3 with exception and ASL 2.0
# Noto Naskh Arabic UI - ASL 2.0
# [unbundled] Cantarell - SIL 1.1 (OFL)
# SigmarOne - SIL 1.1 (OFL)
License:        GPL-2.0-or-later AND GPL-3.0-only AND CC-BY-1.0 AND CC-BY-3.0 AND CC-BY-4.0 AND OFL-1.1 AND Apache-2.0 AND Zlib
URL:            https://supertuxkart.net/Main_Page
Source0:        https://github.com/%{name}/stk-code/releases/download/%{version}/SuperTuxKart-%{version}%{?rctag:-%{rctag}}-src.tar.xz
Source1:        %{name}.6
Source2:        supertuxkart-0.7.3-license-clarification.txt
Patch0:         0c2b81ac1f9ff29f5012a98f530880b87f416337.patch
Patch1:         8544f19b59208ae93fc3db0cf41bd386c6aefbcb.patch
Patch2:         stk-gcc13.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires:  git-core
BuildRequires:  cmake
# For fonts rpm macro
BuildRequires:  fontpackages-devel
BuildRequires:  freetype-devel
BuildRequires:  libvorbis-devel freeglut-devel desktop-file-utils
BuildRequires:  openal-soft-devel freealut-devel >= 1.1.0-10 libtool
BuildRequires:  libcurl-devel fribidi-devel
BuildRequires:  pkgconfig(libenet)
BuildRequires:  wiiuse-devel bluez-libs-devel
BuildRequires:  libpng-devel libjpeg-turbo-devel
BuildRequires:  libXrandr-devel
BuildRequires:  angelscript-devel
BuildRequires:  pkgconfig(glew)
BuildRequires:  openssl-devel
BuildRequires:  libsquish-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  wayland-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  SDL2-devel
BuildRequires:  libgamerzilla-devel
BuildRequires:  libshaderc-devel
Requires:       hicolor-icon-theme opengl-games-utils
Requires:       %{name}-data = %{version}

# Bundled bullet with their patch
Provides:       bundled(bullet) = 2.87
Provides:       bundled(libtinygettext) = 0.1.0

%description
3D go-kart racing game for kids with several famous OpenSource mascots
participating. Race as Tux against 3 computer players in many different fun
race courses (Standard race track, Dessert, Mathclass, etc). Full information
on how to add your own race courses is included. During the race you can pick
up powerups such as: (homing) missiles, magnets and portable zippers.

%package data
Summary:        %{summary}
Requires:       gnu-free-sans-fonts
Requires:       abattis-cantarell-fonts
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
This package contains the data files for SuperTuxKart.

%prep
%autosetup -n SuperTuxKart-%{version}%{?rctag:-%{rctag}}-src -p1
cp -p %{SOURCE2} .
# Delete bundled libs
#rm -rf lib/enet lib/wiiuse lib/angelscript lib/glew
#sed -i -e '/setAnimationStrength/s/^/\/\//' src/karts/kart_model.cpp
mkdir build

%build
pushd build
  %cmake ../ -DUSE_SYSTEM_ANGELSCRIPT=ON -DBUILD_RECORDER=FALSE
  %make_build VERBOSE=1
popd

%install
pushd build
  %cmake_install
popd

# Remove a too large icon that goes outside of hicolor-icon-theme spec and breaks flatpak builds
rm %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/supertuxkart.png

ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name}-wrapper
ln -sf %{_fontbasedir}/abattis-cantarell-fonts/Cantarell-Regular.otf %{buildroot}%{_datadir}/%{name}/Cantarell-Regular.otf
ln -sf %{_fontbasedir}/abattis-cantarell-fonts/Cantarell-Bold.otf %{buildroot}%{_datadir}/%{name}/Cantarell-Bold.otf
ln -sf %{_fontbasedir}/gnu-free/FreeSans.ttf %{buildroot}%{_datadir}/%{name}/FreeSans.ttf
ln -sf %{_fontbasedir}/gnu-free/FreeSansBold.ttf %{buildroot}%{_datadir}/%{name}/FreeSansBold.ttf

# add the manpage (courtesy of Debian)
mkdir -p %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man6

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*%{name}.desktop

%files
%license COPYING supertuxkart-0.7.3-license-clarification.txt
%doc CHANGELOG.md README.md
%{_bindir}/%{name}*
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%exclude %{_includedir}/wiiuse.h
%exclude %{_libdir}/libwiiuse.a

%files data
%{_datadir}/%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4-7
- migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4.5
- Patch for https://github.com/supertuxkart/stk-code/issues/4834

* Fri Dec 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4-4
- Fix cantarell fonts symlinks.

* Tue Nov 22 2022 Pete Walter <pwalter@fedoraproject.org> - 1.4-3
- Rebuild for angelscript 2.35.1

* Mon Nov 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4-2
- Patch to fix soccer ball rolling.

* Tue Nov 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4-1
- 1.4

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.3-3
- Add libgamerzilla support.

* Wed Oct 06 2021 Kalev Lember <klember@redhat.com> - 1.3-2
- Fix appdata to pass validation
- Build bundled tinygettext as static library

* Wed Sep 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.3-1
- 1.3

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2-2.2
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.2-2
- Upstream fix for SDL2 build.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.2-1
- 1.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Kalev Lember <klember@redhat.com> - 1.1-3
- Re-enable GLES support

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.1-2
- Drop GLES due to mesa change.

* Mon Jan 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.1-1
- 1.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.0-1
- 1.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.9.3-2.5
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.9.3-2.3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")
  I don't know why we're versioning like this but what the hell

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-2.1
- Remove obsolete scriptlets

* Tue Jan 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-2
- Rebuild for angelscript 2.32.0

* Mon Nov 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-6.1
- Rebuild for glew 2.0.0

* Sun Dec 18 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-6
- Rebuild for angelscript 2.31.2

* Mon Nov 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.2-5
- Rebuild for angelscript soname change

* Fri Oct 14 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.2-4
- Rebuild to fix broken deps on aarch64.

* Tue Jul 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-3
- Unbundle cantarell and gnu fonts

* Tue Jul 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-2
- Replace non-free ubuntu font with cantarell

* Fri Jul 01 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Mon Jun 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.2-0.3.rc1
- Rebuild for new angelscript

* Tue Jun 21 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-0.2.rc1
- Properly make an update

* Mon Jun 20 2016 Pete Walter <pwalter@fedoraproject.org> - 0.9.2-0.1.rc1
- Update to 0.9.2 RC1

* Thu Feb 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.1-5
- Fix FTBFS.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.1-3
- Rebuild for new wiiuse

* Tue Oct 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.1-2
- Rebuild for new angelscript

* Sun Oct 18 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.1-1
- Update to 0.9.1 (RHBZ #1208136)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9-1
- Update to 0.9
- Drop old patches

* Mon Apr 06 2015 Jon Ciesla <limburgher@gmail.com> - 0.8.1-11
- Fix FTBFS.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.8.1-10
- Add an AppData file for the software center

* Wed Oct 15 2014 Jon Ciesla <limburgher@gmail.com> - 0.8.1-9
- Re-bundling irrlicht and bullet per FPC 459.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.8.1-6
- Adding a Wiimote with other one alredy placed (asked Richard Shaw)

* Wed May 14 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.8.1-5
- fix building with old bullet

* Sun May 11 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.8.1-4
- enable wiimote support (asked in stk-owner@)

* Tue Apr 29 2014 Jon Ciesla <limburgher@gmail.com> - 0.8.1-3
- libenet rebuild.

* Sun Feb 09 2014 Rich Mattes <richmattes@gmail.com> - 0.8.1-2
- Rebuild for bullet-2.82

* Wed Nov 27 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.8.1-1
- Update to upstream 0.8.1

* Mon Nov 25 2013 Hans de Goede <hdegoede@redhat.com> - 0.8-2
- Drop no longer needed SDL and mikmod BuildRequires

* Mon Aug 05 2013 Hans de Goede <hdegoede@redhat.com> - 0.8-1
- New upstream release 0.8 (#886012)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.3-6
- License clariication, BZ 891890.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.3-5
- Drop desktop vendor tag.

* Mon Feb 04 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.3-4
- License clariication, BZ 891890.

* Thu Nov 15 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.3-3
- Use irrlicht 1.8 final.

* Fri Aug 24 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.3-2
- Post cleanup.

* Thu Aug 23 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.3-1
- Latest upstream, using irrlicht snapshot subpackage.  BZ 697169.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Jon Ciesla <limburgher@gmail.com> - 0.7-5
- Rebuild for new irrlicht.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Jon Ciesla <limb@jcomserv.net> - 0.7-1
- New upstream, BZ 587194.

* Thu Jan 14 2010 Jon Ciesla <limb@jcomserv.net> - 0.6.2-3
- Rebuild for new irrlicht.

* Thu Nov 19 2009 Jon Ciesla <limb@jcomserv.net> - 0.6.2-2
- Add in addon pack.
- Split data to noarch subpackage.

* Thu Sep 10 2009 Jon Ciesla <limb@jcomserv.net> - 0.6.2-1
- Bugfix release.

* Sun Aug 16 2009 Hans de Goede <hdegoede@redhat.com> - 0.6.1a-3
- Switch to openal-soft

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Jon Ciesla <limb@jcomserv.net> - 0.6.1a-1
- Patch release.
- Fixed symlink/dir replacement, BZ 506245.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Hans de Goede <hdegoede@redhat.com> 0.6.1-1
- New upstream release 0.6.1

* Sun Jan 25 2009 Hans de Goede <hdegoede@redhat.com> 0.6-1
- New upstream release 0.6

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 0.5-2
- Fix patch fuzz build failure

* Tue Jun  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5-1
- New upstream release 0.5

* Tue May 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-2
- Rebuild for new plib

* Mon Mar 10 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-1
- New upstream release 0.4
- Note this version includes a build in copy of the bullet physics library,
  this is a patched copy making use if a system version impossible

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3-4
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-3
- Fix compilation with gcc 4.3

* Mon Sep 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-2
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-1
- New upstream release 0.3
- Drop most patches (all fixed upstream)
- Update License tag for new Licensing Guidelines compliance

* Fri Oct  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-3
- replace some more coprighted images and sounds
- fix a bunch of joystick related bugs

* Mon Sep 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-2
- rename images-legal.txt to supertuxkart-images-legal.txt
- add a changelog entry for the previous release (and this one)

* Mon Sep 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-1
- initial Fedora Extras package (replacing regular tuxkart)
