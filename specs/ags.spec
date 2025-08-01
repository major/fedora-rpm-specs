%bcond_without openal

%global fver v%{version}
# avoid building bundled libraries as shared
%undefine _cmake_shared_libs

Name: ags
Summary: Engine for creating and running videogames of adventure (quest) genre
Version: 3.6.2.12
URL:     http://www.adventuregamestudio.co.uk/site/ags/
Release: 2%{?dist}
Source0: https://github.com/adventuregamestudio/ags/archive/%{fver}/ags-%{fver}.tar.gz
# https://github.com/richgel999/miniz/issues/249
Source1: FindMiniz.cmake
Patch0: ags-use-system-libraries.patch
# Most code is under Artistic-2.0, except:
# Common/libsrc/aastr-0.1.1: LicenseRef-Fedora-UltraPermissive
# Common/libsrc/alfont-2.0.9: FTL
# Engine/libsrc/apeg-1.2.1: MPEG-SSG
# Engine/libsrc/glad: Apache-2.0 AND MIT-Khronos-old
# Engine/libsrc/libcda-0.5: Zlib
# Plugins/agsblend/agsblend: MIT
# Plugins/agspalrender/agspalrender/raycast.{cpp,h}: BSD-2-Clause
# Plugins/AGSSpriteFont: CC0-1.0
# libsrc/allegro: Giftware
License: Artistic-2.0 AND LicenseRef-Fedora-UltraPermissive AND FTL AND MPEG-SSG AND Apache-2.0 AND MIT-Khronos-old AND Zlib AND MIT AND BSD-2-Clause AND CC0-1.0 AND Giftware
# incorrect rendering with new FT: https://github.com/adventuregamestudio/ags/issues/1528
Provides: bundled(freetype) = 2.1.3
%if %{with openal}
BuildRequires: openal-soft-devel
%else
# https://github.com/icculus/mojoAL (zlib)
Provides: bundled(mojoal)
%endif
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glad
BuildRequires: glm-devel
# for KHR/khrplatform.h
BuildRequires: libglvnd-devel
BuildRequires: libogg-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: make
BuildRequires: miniz-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_sound-devel
BuildRequires: tinyxml2-devel
# https://web.archive.org/web/20050323070052/http://www.inp.nsk.su/~bukinm/dusty/aastr/ (Giftware)
# dead upstream, might be possible to use aastr2:
# https://www.allegro.cc/resource/Libraries/Graphics/AASTR2
Provides: bundled(aastr) = 0.1.1
# bundled alfont is patched
Provides: bundled(alfont) = 2.0.9
# bundled allegro is stripped and patched
Provides: bundled(allegro) = 4.4.3
# http://kcat.strangesoft.net/apeg.html (Public Domain)
Provides: bundled(apeg) = 1.2.1
# https://web.archive.org/web/20040104090747/http://www.alphalink.com.au/~tjaden/libcda/index.html (zlib)
# dead upstream
Provides: bundled(libcda) = 0.5

%description
Adventure Game Studio (AGS) - is the IDE and the engine meant for creating and
running videogames of adventure (aka "quest") genre. It has potential, although
limited, support for other genres as well.

Originally created by Chris Jones back in 1999, AGS was opensourced in 2011 and
since continued to be developed by contributors.

%prep
%setup -q
%patch 0 -p1 -b .orig
cp -p %{S:1} CMake/
# delete unused bundled stuff
pushd Common/libinclude
rm -r ogg
rm -r theora
rm -r vorbis
popd
pushd Common/libsrc
rmdir googletest
popd
pushd Engine/libsrc
rm -r glad{,-gles2}/{src,include}
glad --reproducible --out-path=glad       --profile="compatibility" --api="gl=2.1"    --generator="c" --spec="gl" --extensions="GL_EXT_framebuffer_object"
glad --reproducible --out-path=glad-gles2 --profile="core"          --api="gles2=2.0" --generator="c" --spec="gl" --extensions=""
rm -r ogg
rm -r theora
rm -r vorbis
popd
pushd libsrc
rm -r glm
rm -r miniz
%if %{with openal}
rm -r mojoAL
%endif
rm -r tinyxml2
popd
iconv -o Changes.txt.utf-8 -f iso8859-1 -t utf-8 Changes.txt && \
touch -r Changes.txt Changes.txt.utf-8 && \
mv Changes.txt.utf-8 Changes.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DAGS_USE_LOCAL_SDL2=TRUE \
    -DAGS_USE_LOCAL_SDL2_SOUND=TRUE \
    -DAGS_USE_LOCAL_OGG=TRUE \
    -DAGS_USE_LOCAL_VORBIS=TRUE \
    -DAGS_USE_LOCAL_THEORA=TRUE \
    -DAGS_USE_SYSTEM_GLM=TRUE \
    -DAGS_USE_SYSTEM_TINYXML2=TRUE \
    -DAGS_USE_SYSTEM_MINIZ=TRUE \

%cmake_build

%install
%cmake_install

%files
%license License.txt
%doc Changes.txt Copyright.txt OPTIONS.md README.md
%{_bindir}/ags

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jul 19 2025 Dominik Mierzejewski <dominik@greysector.net> - 3.6.2.12-1
- update to 3.6.2.12
- switch back to bundled freetype per upstream recommendation

* Sun Jul 06 2025 Dominik Mierzejewski <dominik@greysector.net> - 3.6.2.11-1
- update to 3.6.2.11

* Fri May 09 2025 Dominik Mierzejewski <dominik@greysector.net> - 3.6.2.9-1
- update to 3.6.2.9
- regenerate glad sources

* Fri Feb 28 2025 Dominik Mierzejewski <dominik@greysector.net> - 3.6.2.7-1
- update to 3.6.2.7
- switch build system to cmake
- unbundle miniz
- update SPDX expression in License: field after review

* Thu Feb 27 2025 Dominik Mierzejewski <dominik@greysector.net> - 3.6.1.31-1
- update to 3.6.1.31
- fix build with C23 (resolves rhbz#2336273)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Dominik Mierzejewski <dominik@greysector.net> - 3.6.1.30-1
- update to 3.6.1.30
- drop obsolete patch

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.56-5
- rebuild for tinyxml2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.56-1
- update to 3.6.0.56
- fix build with GCC14

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.51-1
- update to 3.6.0.51

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 14 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.48-1
- update to 3.6.0.48 (#2192719)

* Tue Apr 04 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.47-1
- update to 3.6.0.47 stable release (#2183747)

* Mon Mar 27 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.46-1
- update to 3.6.0.46 (#2179689)

* Wed Mar 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.44-1
- update to 3.6.0.44 (#2172608)

* Mon Feb 06 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.42-1
- update to 3.6.0.42 (#2167149)
- drop obsolete patch

* Tue Jan 24 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.41-1
- update to 3.6.0.41 (#2161376)
- fix build with GCC 13

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.40-1
- update to 3.6.0.40 (#2158889)

* Tue Jan 03 2023 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.39-1
- update to 3.6.0.39 (#2156072)

* Tue Dec 06 2022 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.38-1
- update to 3.6.0.38 (#2143092)

* Mon Oct 10 2022 Dominik Mierzejewski <dominik@greysector.net> - 3.6.0.36-1
- update to 3.6.0.36 (#2108390)

* Thu Oct 06 2022 Dominik Mierzejewski <rpm@greysector.net> - 3.6.0.35-1
- update to 3.6.0.35 (#2108390)

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 3.6.0.33-2
- Rebuild for tinyxml2-9.0.0

* Sun Aug 14 2022 Dominik Mierzejewski <rpm@greysector.net> - 3.6.0.33-1
- update to 3.6.0.33 (#2108390)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Dominik Mierzejewski <rpm@greysector.net> - 3.6.0.30-1
- update to 3.6.0.30 (#2105677)

* Tue Jul 05 2022 Dominik Mierzejewski <rpm@greysector.net> - 3.6.0.29-1
- update to 3.6.0.29 (#2100149)

* Wed Jun 08 2022 Dominik Mierzejewski <rpm@greysector.net> - 3.6.0.27-1
- update to 3.6.0.27 (#2091478)

* Thu May 12 2022 Dominik Mierzejewski <rpm@greysector.net> - 3.6.0.25-1
- update to 3.6.0.25
- unbundle khrplatform.h header
- unbundle glm, ogg, theora, tinyxml2 and vorbis
- use openal-soft instead of bundled mojoAL

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 13 2021 Dominik Mierzejewski <rpm@greysector.net> - 3.5.0.32-1
- update to 3.5.0.32

* Thu Apr 08 2021 Dominik Mierzejewski <rpm@greysector.net> - 3.5.0.31-1
- update to 3.5.0.31
- drop obsolete patches

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Dominik Mierzejewski <rpm@greysector.net> - 3.5.0.25-1
- update to 3.5.0.25 (#1862828)
- fix compilation with GCC10 (missing cstdio includes)
- unbundle freetype
- fix linking against system libdumb
- fix compilation on big-endian (missing include)

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Dominik Mierzejewski <rpm@greysector.net> - 3.4.4.2-1
- use upstream source directly, offending files were removed upstream

* Wed Oct 02 2019 Dominik Mierzejewski <rpm@greysector.net> - 3.4.4.1-1
- initial Fedora package of 3.4.4.1 release
- remove non-free Engine/libsrc/libcda-0.5/{bcd.doc,djgpp.c} from tarball
- convert Changes.txt to UTF-8
