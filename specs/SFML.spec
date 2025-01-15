Name:           SFML
Version:        2.6.2
Release:        1%{?dist}
Summary:        Simple and Fast Multimedia Library

# Assets used by SFML's example projects.
#
# All assets are under public domain (CC0):
#
# | Name                            | Author                    | Link                       |
# | ------------------------------- | ------------------------- | -------------------------- |
# | Tuffy 1.1 font                  | Thatcher Ulrich           | [Ulrich's fonts][1]        |
# | sounds/resources/doodle_pop.ogg | MrZeusTheCoder            | [public-domain][2]         |
# | tennis/resources/ball.wav       | MrZeusTheCoder            | [public-domain][2]         |
# | opengl/resources/background.jpg | Nidhoggn                  | [Open Game Art][3]         |
# | shader/resources/background.jpg | Arcana Dea                | [Public Domain Images][4]  |
# | shader/resources/devices.png    | Kenny.nl                  | [Game Icons Pack][5]       |
# | sound/resources/ding.flac       | Kenny.nl                  | [Interface Sounds Pack][6] |
# | sound/resources/ding.mp3        | Kenny.nl                  | [Interface Sounds Pack][6] |
# | win32/resources/image1.jpg      | Kenny.nl                  | [Toon Character Pack][7]   |
# | win32/resources/image2.jpg      | Kenny.nl                  | [Toon Character Pack][7]   |
# | sound/resources/killdeer.wav    | US National Park Services | [Bird sounds][8]           |
#
# [1]: http://tulrich.com/fonts/
# [2]: https://github.com/MrZeusTheCoder/public-domain
# [3]: https://opengameart.org/content/backgrounds-3
# [4]: https://www.publicdomainpictures.net/en/view-image.php?image=10979&picture=monarch-butterfly
# [5]: https://www.kenney.nl/assets/game-icons
# [6]: https://www.kenney.nl/assets/interface-sounds
# [7]: https://www.kenney.nl/assets/toon-characters-1
# [8]: https://www.nps.gov/subjects/sound/sounds-killdeer.htm

License:        Zlib AND LicenseRef-Fedora-Public-Domain
URL:            http://www.sfml-dev.org/
# for SFML 2.6.0 we've removed all the unclear/non-free assets from the source.
# See the asset_licenses.md for more details: https://github.com/SFML/SFML/blob/2.6.1/examples/asset_licenses.md
# And here's the PR that changed (most) of the things: https://github.com/SFML/SFML/pull/1718

Source0:        https://www.sfml-dev.org/files/%{name}-%{version}-sources.zip

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  libvorbis-devel
BuildRequires:  flac-devel
BuildRequires:  systemd-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  glew-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  openal-devel
#BuildRequires:  vulkan-headers
BuildRequires:  stb_image-devel >= 2.27-0.7
BuildRequires:  stb_image_write-devel

%description
SFML is a portable and easy to use multimedia API written in C++. You can see
it as a modern, object-oriented alternative to SDL.
SFML is composed of several packages to perfectly suit your needs. You can use
SFML as a minimal windowing system to interface with OpenGL, or as a
fully-featured multimedia library for building games or interactive programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
# fixup non needed executable permission on regular files
find -type f -print0 | xargs -0 chmod -x

# use system-wide extlibs; so, delete everything except glad, minimp3 and vulkan header files
pushd extlibs
shopt -s extglob
rm -r !(headers)
cd headers/
rm -r !(glad|minimp3|vulkan)
shopt -u extglob
popd


%build
%cmake -DSFML_BUILD_DOC=TRUE
%cmake_build


%install
%cmake_install

%files
%doc %{_datadir}/doc/%{name}/readme.md
%license %{_datadir}/doc/%{name}/license.md
%{_libdir}/*.so.*

%files devel
%doc %{_datadir}/doc/%{name}/html/*
%doc %{_datadir}/doc/%{name}/SFML.tag
%{_libdir}/cmake/%{name}/*.cmake
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/sfml-*.pc
%{_libdir}/libsfml-*.so


%changelog
* Mon Jan 13 2025 Sérgio Basto <sergio@serjux.com> - 2.6.2-1
- Update SFML to 2.6.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 06 2023 Sérgio Basto <sergio@serjux.com> - 2.6.1-2
- Fix License tag

* Sat Nov 04 2023 Sérgio Basto <sergio@serjux.com> - 2.6.1-1
- Update SFML to 2.6.1 with soname bump
- Benjamin A. Beasley <code@musicinmybrain.net>
  Unbundle stb libraries. Updated stb_image patches CVE-2021-28021,
  CVE-2021-42715, and CVE-2021-42716
  Remove obsolete ldconfig_scriptlets macro

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 24 2023 Sérgio Basto <sergio@serjux.com> - 2.5.1-14
- Migrate to SPDX license format

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.5.1-12
- Rebuilt for flac 1.4.0
- Add license tag

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 2020 Wim Taymans <wtaymans@redhat.com> - 2.5.1-7
- Fix build with cmake out-of-source builds
- Fixes rhbz#1884368

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Pranav Kant <pranvk@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1
- Drop unnecessary patches
- Remove usage of -DSFML_INSTALL_PKGCONFIG_FILES=ON

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Pranav Kant <pranvk@fedoraproject.org> - 2.4.2-2
- Rename SFML-2.4.2-clean directory to SFML-2.4.2 before compressing

* Fri Feb 17 2017 Pranav Kant <pranvk@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2
- Patch for -Wstrict-aliasing

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 05 2017 Pranav Kant <pranvk@fedoraproejct.org> - 2.4.1-2
- Add missing update change log entry here

* Sun Feb 05 2017 Pranav Kant <pranvk@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Sat Mar 19 2016 Pranav Kant <pranvk@fedoraproject.org> - 2.3.2-4
- Remove copyright/trademark content - rhbz#1310387

* Sat Feb 27 2016 Hans de Goede <hdegoede@redhat.com> - 2.3.2-3
- Fix unresolved __cpu_model symbol in sfml-graphics.so

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Pranav Kant <pranvk@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Mon Jun 22 2015 Pranav Kant <pranvk@fedoraproject.org> - 2.3-1
- Update to 2.3

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Hans de Goede <hdegoede@redhat.com> - 2.1-1
- Update to version 2.1 (rhbz#1033924)

* Mon Nov 18 2013 Hans de Goede <hdegoede@redhat.com> - 2.0-6
- Really move cmake file to proper location (rhbz#997679)
- Remove non free font from source tarbal (rhbz#1003569)

* Mon Nov 18 2013 Hans de Goede <hdegoede@redhat.com> - 2.0-5
- Drop changes to make parallel installable with 1.6, instead compat-SFML16
  has now been changed to avoid the conflicts (rhbz#997679)
- Move cmake file to proper location and put it in -devel

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 2.0-4
- rebuilt for GLEW 1.10

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Hans de Goede <hdegoede@redhat.com> - 2.0-2
- Make parallel installable with 1.6 (avoid conflict with compat-SFML16)
- Fix rpmlint warnings
- Fix Source0 URL

* Wed May 01 2013 Julian Sikorski <belegdol@fedoraproject.org> - 2.0-1
- Updated to 2.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.6-9
- rebuild due to "jpeg8-ABI" feature drop

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.6-8
- Rebuild for glew 1.9.0

* Fri Jul 27 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-7
- Rebuilt for glew-1.7

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-4
- Fixed the License tag

* Thu Jan 12 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-3
- Use one patch and variables in place of sed to fix the makefile
- Fixed building with libpng-1.5 using a patch from Gentoo
- Updated the gcc patch for gcc-4.7

* Fri Dec 23 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-2
- s/libSOIL/SOIL
- Fixed the shared libs usage

* Wed Nov 30 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-1
- Initial RPM release based on Debian package

