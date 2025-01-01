Name: fheroes2
Version: 1.1.5
Release: %autorelease
Summary: Free implementation of the popular game engine
# ./src/thirdparty/libsmacker is under LGPL-2.1-or-later
# The rest is under GPL-2.0-or-later
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://github.com/ihhub/fheroes2
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.autodlrc
Source2: %{name}.sh
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_net-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: libpng-devel
BuildRequires: make
Requires: autodownloader
Requires: hicolor-icon-theme
Requires: unzip
Provides: bundled(libsmacker) = 1.2.0

%description
This open source multiplatform project, written from scratch, is designed to
reproduce the original game with significant improvements in gameplay, graphics
and logic (including support for high-resolution graphics, improved AI,
numerous fixes and user interface improvements), breathing new life into one of
the most addictive turn-based strategy games.

%prep
%autosetup -p1

%build
%cmake \
    -DFHEROES2_DATA="%{_datadir}/%{name}" \
    -DUSE_SDL_VERSION=SDL2 \
    -DENABLE_IMAGE=ON

%cmake_build

# make man-page
cd docs
FHEROES2_DATA=%{_datadir}/%{name}/data make
cd -

%install
%cmake_install

install -D -p -m 0644 docs/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/%{name}.autodlrc
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.bin
install -Dpm 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}

# Remove files we'll install differently
rm -f  %{buildroot}%{_docdir}/%{name}/LICENSE
rm -f  %{buildroot}%{_docdir}/%{name}/README.txt
rm -f  %{buildroot}%{_docdir}/%{name}/changelog.txt
rm -f  %{buildroot}%{_docdir}/%{name}/demo/download_demo_version.sh
rm -f  %{buildroot}%{_docdir}/%{name}/homm2/extract_homm2_resources.sh
rm -d  %{buildroot}%{_docdir}/%{name}/demo/
rm -d  %{buildroot}%{_docdir}/%{name}/homm2/

mkdir -p %{buildroot}%{_datadir}/%{name}/{anim,data,lang,maps}/

%files
%doc README.md changelog.txt
%license LICENSE
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/anim/
%dir %{_datadir}/%{name}/data/
%dir %{_datadir}/%{name}/files/
%dir %{_datadir}/%{name}/files/data/
%dir %{_datadir}/%{name}/files/lang/
%dir %{_datadir}/%{name}/maps/
%{_bindir}/%{name}
%{_bindir}/%{name}.bin
%{_datadir}/%{name}/%{name}.autodlrc
%{_datadir}/%{name}/files/data/resurrection.h2d
%{_datadir}/%{name}/files/lang/*.mo
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6.*
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
