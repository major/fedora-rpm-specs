%global         _tarname SuperTux-v%{version}-Source

Name:           supertux
Version:        0.6.3
Release:        15%{?dist}
Summary:        Jump'n run like game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.supertux.org
Source0:        https://github.com/SuperTux/%{name}/releases/download/v%{version}/%{_tarname}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2056887
Patch0:         supertux-0.6.3-build-fix.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2082179
Patch1:         supertux-0.6.3-squirrel-CVE-2022-30292.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1833368
ExcludeArch:    s390x

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  sed
BuildRequires:  pkgconfig(raqm)
BuildRequires:  pkgconfig(sdl2) >= 2.0.1
BuildRequires:  pkgconfig(SDL2_image) >= 2.0.0
BuildRequires:  boost-devel
BuildRequires:  freetype-devel
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  libcurl-devel
BuildRequires:  libGLU-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-devel
BuildRequires:  physfs-devel
BuildRequires:  zlib-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
Requires:       hicolor-icon-theme

# Bundled version of squirrel 3 (only version 2 in Fedora).
Provides:       bundled(squirrel) = 3.1
# Bundled (and forked) version of tinygettext.
Provides:       bundled(tinygettext) = 0.1.20160606git

%description
SuperTux is a jump'n run like game, Run and jump through multiple worlds,
fighting off enemies by jumping on them or bumping them from below.
Grabbing power-ups and other stuff on the way.


%prep
%autosetup -p1 -n %{_tarname}


%build
%cmake -DINSTALL_SUBDIR_SHARE=share/supertux2 -DINSTALL_SUBDIR_BIN=bin \
    -DENABLE_BOOST_STATIC_LIBS=OFF
%cmake_build


%install
%cmake_install
rm -r %{buildroot}%{_docdir}/supertux2

# Icon stuff
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{buildroot}%{_datadir}/pixmaps/supertux.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/supertux2.png
rm %{buildroot}%{_datadir}/pixmaps/supertux.xpm

install -Dpm 644 man/man6/supertux2.6 %{buildroot}%{_mandir}/man6/supertux2.6


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/supertux2.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/supertux2.desktop


%files
%doc README.md NEWS.md
%license LICENSE.txt
%{_bindir}/supertux2
%{_datadir}/supertux2
%{_datadir}/applications/supertux2.desktop
%{_datadir}/icons/hicolor/48x48/apps/supertux2.png
%{_datadir}/icons/hicolor/scalable/apps/supertux2.svg
%{_datadir}/metainfo/supertux2.appdata.xml
%{_mandir}/man6/supertux2.6*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.3-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.6.3-11
- Rebuilt for Boost 1.83

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.6.3-9
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 11 2022 Thomas Rodgers <trodgers@redhat.com> - 0.6.3-6
- Rebuilt for Boost 1.78

* Thu May 05 2022 David King <amigadave@amigadave.com> - 0.6.3-5
- Fix CVE-2022-30292 (#2082179)

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.6.3-4
- Rebuilt for Boost 1.78

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.6.3-3
- Rebuild for glew 2.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 David King <amigadave@amigadave.com> - 0.6.3-1
- Update to 0.6.3 (#2031711)

* Mon Aug 09 2021 Jonathan Wakely <jwakely@redhat.com> - 0.6.2-7
- Patched and rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.6.2-4
- Rebuilt for Boost 1.75

* Thu Jul 30 2020 David King <amigadave@amigadave.com> - 0.6.2-3
- Use %%cmake_build and %%cmake_install

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.6.2-2
- Rebuilt for Boost 1.73

* Mon May 18 2020 David King <amigadave@amigadave.com> - 0.6.2-1
- Update to 0.6.2 (#1392733)

* Fri May 08 2020 David King <amigadave@amigadave.com> - 0.6.1-1
- Update to 0.6.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Jan Beran <jaberan@redhat.com> - 0.6.0-4
- Use %{_docdir} macro instead of hardcoded /usr/share/doc

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-2
- Rebuilt for Boost 1.69

* Fri Dec 28 2018 Pete Walter <pwalter@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0
- Drop opengl-game-wrapper.sh use
- Update URL
- Spec file cleanup
- Remove ExcludeArch: ppc64le

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-13
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-10
- Rebuilt for Boost 1.66

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-9
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-6
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-5
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-2
- Rebuilt for Boost 1.63

* Tue Jan 24 2017 David King <amigadave@amigadave.com> - 0.5.1-1
- Update to 0.5.1
- Add ExcludeArch ppc64le

* Wed Sep 28 2016 David King <amigadave@amigadave.com> - 0.5.0-1
- Update to 0.5.0 (#1380088)

* Wed Sep 14 2016 David King <amigadave@amigadave.com> - 0.5.0-0.3.rc4-1
- Update to 0.5.0-rc.4

* Mon Sep 12 2016 David King <amigadave@amigadave.com> - 0.5.0-0.3.rc3-1
- Update to 0.5.0-rc.3

* Sat Aug 13 2016 David King <amigadave@amigadave.com> - 0.5.0-0.2.rc2-1
- Update for bundled physfs

* Sat Aug 13 2016 David King <amigadave@amigadave.com> - 0.5.0-0.1.rc2-1
- Update to 0.5.0-rc.2 (#1365227)

* Thu Aug 04 2016 David King <amigadave@amigadave.com> - 0.4.0-5
- Use bundled squirrel 3.0.7 (#1295185)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.4.0-3
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.4.0-2
- Rebuild for glew 1.13

* Mon Dec 21 2015 David King <amigadave@amigadave.com> - 0.4.0-1
- Update to 0.4.0 (#1293182)

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.3.5a-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5a-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.3.5a-3
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 David King <amigadave@amigadave.com> - 0.3.5a-1
- Update to 0.3.5a (#1219849)

* Mon Apr 13 2015 David King <amigadave@amigadave.com> - 0.3.5-1
- Update to 0.3.5
- Validate AppData during check
- Install man page

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.3.4-2
- Rebuild for boost 1.57.0

* Tue Nov 11 2014 David King <amigadave@amigadave.com> - 0.3.4-1
- Update to 0.3.4 (#999396)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.3.3-15
- Rebuild for boost 1.55.0

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.3.3-14
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.3.3-12
- Rebuild for boost 1.54.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.3.3-10
- Rebuild for glew 1.9.0

* Thu Jul 26 2012 Hans de Goede <hdegoede@redhat.com> - 0.3.3-9
- Rebuilt for new GLEW

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-7
- Rebuilt for c++ ABI breakage

* Sun Jan 15 2012 Dan Horák <dan@danny.cz> - 0.3.3-6
- rebuilt with squirrel 2.2.5

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Tom Callaway <spot@fedoraproject.org> - 0.3.3-4
- rebuild for physfs2

* Thu Jun 30 2011 Nils Philippsen <nils@redhat.com> - 0.3.3-3
- include cstddef header to fix build

* Wed Jun 29 2011 Nils Philippsen <nils@redhat.com> - 0.3.3-3
- fix building with current libcurl

* Mon Jun 20 2011 ajax@redhat.com - 0.3.3-3
- Rebuild for new glew soname

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr  6 2010 Hans de Goede <hdegoede@redhat.com> 0.3.3-1
- New upstream release 0.3.3
- As upstream consistently calls this supertux2, do the same
  (rather then renaming it to supertux)
- Move the icon to the FDO icon dir

* Tue Aug 25 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.3.1-9
- Rebuild for new openal

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.3.1-7
- Fix build with GCC 4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Hans de Goede <hdegoede@redhat.com> 0.3.1-5
- Update description for new trademark guidelines

* Sun Jan 18 2009 Lubomir Rintel <lkundrak@v3.sk> 0.3.1-4
- Fix parsing of translations (#477497)
- Disable debugging console

* Thu Jul 10 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-3
- Fix building with gcc-4.3 (bz 434445)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.1-2
- Autorebuild for GCC 4.3

* Tue Jan 08 2008 Steven Pritchard <steve@kspei.com> 0.3.1-1
- Update to 0.3.1.
- Upstream is calling this release "supertux2", so we get rid of the "2".
- Update License.

* Fri Oct 19 2007 Nils Philippsen <nphilipp@redhat.com> 0.3.0-3
- use opengl-games-wrapper.sh from Fedora 7 on (#335701)

* Fri Oct 19 2007 Nils Philippsen <nphilipp@redhat.com> 0.3.0-2
- use opengl-games-wrapper.sh from Fedora 8 on (#335701)

* Tue Feb 13 2007 Steven Pritchard <steve@kspei.com> 0.3.0-1
- Update to 0.3.0.
- Update URL.
- Drop compile fix patch.
- BR: physfs-devel, openal-devel, libvorbis-devel.
- BR: gettext, flex, bison, jam.
- Build uses jam instead of make now.
- Update doc list.
- Minor spec cleanup.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 0.1.3-5
- Rebuild

* Sat Jun 03 2006 Steven Pritchard <steve@kspei.com> 0.1.3-4
- BR: libGLU-devel to fix rawhide build

* Tue Feb 07 2006 Steven Pritchard <steve@kspei.com> 0.1.3-3
- Patch to fix compile on rawhide

* Tue Sep 06 2005 Steven Pritchard <steve@kspei.com> 0.1.3-2
- Avoid second .desktop file (#167579)

* Thu Sep 01 2005 Steven Pritchard <steve@kspei.com> 0.1.3-1
- Update to 0.1.3

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.1.2-3
- rebuild on all arches

* Fri Apr 08 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Oct 03 2004 Panu Matilainen <pmatilai@welho.com> 0:0.1.2-1
- update to 0.1.2

* Sat May 15 2004 Panu Matilainen <pmatilai@welho.com> 0:0.1.1-0.fdr.2
- add buildrequires libtiff-devel

* Thu May 13 2004 Panu Matilainen <pmatilai@welho.com> 0:0.1.1-0.fdr.1
- Initial RPM release.
