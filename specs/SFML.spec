%global sheenbidi_version 3.0.0

Name:           SFML
Version:        3.1.0
Release:        %autorelease
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
#
# Apache-2.0:
#   - extlibs/headers/vulkan/
# CC0-1.0:
#   - extlibs/headers/minimp3/
# MIT:
#   - extlibs/headers/glad/include/glad/gl.h
# (MIT AND Apache-2.0):
#   - extlibs/headers/glad/include/glad/egl.h
#
License:        Zlib AND Apache-2.0 AND CC0-1.0 AND MIT AND (MIT AND Apache-2.0) AND LicenseRef-Fedora-Public-Domain
URL:            http://www.sfml-dev.org/
# for SFML 2.6.0 we've removed all the unclear/non-free assets from the source.
# See the asset_licenses.md for more details: https://github.com/SFML/SFML/blob/2.6.1/examples/asset_licenses.md
# And here's the PR that changed (most) of the things: https://github.com/SFML/SFML/pull/1718

Source0:        https://www.sfml-dev.org/files/%{name}-%{version}-sources.zip
Source1:        https://github.com/Tehreer/SheenBidi/archive/refs/tags/v%{sheenbidi_version}.zip#/SheenBidi-%{sheenbidi_version}-sources.zip

# Fedora doesn't have this yet, and upstream appears to assume bundling:
Provides:       bundled(SheenBidi) = %{sheenbidi_version}

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mbedtls)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  qoi-static
BuildRequires:  stb_image-devel >= 2.30^20251025gitf1c79c0-2
BuildRequires:  stb_image_write-devel
# BuildRequires:  vulkan-headers

%description
SFML is a portable and easy to use multimedia API written in C++. You can see
it as a modern, object-oriented alternative to SDL.
SFML is composed of several packages to perfectly suit your needs. You can use
SFML as a minimal windowing system to interface with OpenGL, or as a
fully-featured multimedia library for building games or interactive programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cmake

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -a 1
# fixup non needed executable permission on regular files
find -type f -print0 | xargs -0 chmod -x
#
sed -i "s/add_custom_target(doc/add_custom_target(doc ALL/" doc/CMakeLists.txt
sed -i "s/Doxygen::doxygen/\${DOXYGEN_EXECUTABLE}/" doc/CMakeLists.txt

# use system-wide extlibs; so, delete everything except cpp-unicodelib, glad, dr_mp3, miniaudio, and vulkan header files
pushd extlibs
shopt -s extglob
cd headers/
rm -r !(cpp-unicodelib|dr_mp3|glad|miniaudio|vulkan)
shopt -u extglob
popd


%build
%cmake -DSFML_BUILD_DOC=TRUE \
	-DFETCHCONTENT_SOURCE_DIR_SHEENBIDI:PATH=$(pwd)/SheenBidi-%{sheenbidi_version}
%cmake_build


%install
%cmake_install

%files
%doc %{_datadir}/doc/%{name}/readme.md
%license %{_datadir}/doc/%{name}/license.md
%{_libdir}/libsfml-*.so.3*

%files devel
%doc %{_datadir}/doc/%{name}/html/*
%doc %{_datadir}/doc/%{name}/SFML.tag
%{_libdir}/cmake/%{name}/*.cmake
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/sfml-*.pc
%{_libdir}/libsfml-*.so
#exclude bundled devel files:
%exclude %{_includedir}/SheenBidi/
%exclude %{_libdir}/cmake/SheenBidi/*.cmake
%exclude %{_libdir}/libSheenBidi.a
%exclude %{_libdir}/pkgconfig/sheenbidi.pc


%changelog
%autochangelog
