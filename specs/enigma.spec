%global forgeurl https://github.com/Enigma-Game/Enigma
%global version0 1.30
# top of 'master' branch as of 2025-03-22
%global commit ab9967a7c7440ce5d3908c8b6eb63cb5a22cfef1
%forgemeta

Name:           enigma
Version:        %forgeversion
Release:        %autorelease
Summary:        Game where you control a marble with the mouse
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/enigma/
Source0:        %forgesource
# https://github.com/Enigma-Game/Enigma/pull/105
Patch1:         0001-etc-enigma.desktop-use-standard-specified-Categories.patch

Requires:       %{name}-data = %{version}-%{release}

# automate finding font paths at build time
%global fonts font(dejavusans)
Requires:       %{fonts}
BuildRequires:  fontconfig %{fonts}

BuildRequires:  gcc-c++
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  gettext
BuildRequires:  libpng-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  zlib-devel
BuildRequires:  xerces-c-devel
BuildRequires:  curl-devel
BuildRequires:  ImageMagick
BuildRequires:  git
BuildRequires:  autoconf automake
BuildRequires:  pkgconfig(libenet)
BuildRequires:  texi2html
BuildRequires:  make

%description
Enigma is a tribute to and a re-implementation of one of the most
original and intriguing computer games of the 1990's: Oxyd.  Your
objective is easily explained: find and uncover all pairs of identical
Oxyd stones in each landscape.  Sounds simple?  It would be, if it
weren't for hidden traps, vast mazes, insurmountable obstacles and
innumerable puzzles blocking your direct way to the Oxyd stones...

%package data
Summary:        Data for Enigma game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
BuildArch:      noarch

%description data
Data files (levels, graphics, sound, music) and documentation for Enigma.

%prep
%forgeautosetup -p1
rm -r attic/ dlls/ lib-src/enet/*

%build
aclocal -I m4 && autoheader && automake --add-missing --foreign --copy && autoconf
%configure --enable-optimize --with-system-enet
%make_build

%install
%make_install

# Use system fonts instead of bundling our own
ln -f -s $(fc-match -f "%{file}" "dejavusans:condensed") \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/DejaVuSansCondensed.ttf
ln -f -s $(fc-match -f "%{file}" "dejavusans") \

desktop-file-install \
  --remove-key Version \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications            \
  $RPM_BUILD_ROOT%{_datadir}/applications/enigma.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/enigma.appdata.xml

%files
%{_bindir}/enigma
%{_mandir}/man?/enigma.*
%{_datadir}/icons/hicolor/48x48/apps/enigma.png
%{_datadir}/pixmaps/enigma.png
%{_datadir}/applications/enigma.desktop
%{_datadir}/appdata/enigma.appdata.xml

%files data
%{_pkgdocdir}
%{_datadir}/enigma

%changelog
%autochangelog
