Name:           enigma
Version:        1.30
Release:        %autorelease
Summary:        Game where you control a marble with the mouse

License:        GPLv2+
URL:            http://www.nongnu.org/enigma/
Source0:        https://github.com/Enigma-Game/Enigma/releases/download/%{version}/Enigma-%{version}-src.tar.gz
Patch0001:      0001-Clean-up-.desktop-file-categories.patch
Patch0002:      0002-build-use-system-zipios.patch
Patch0003:      0003-prevent-ImageMagick-inserting-timestamps-to-PNGs.patch
Patch0004:      0004-quoting-inside-AM_COND_IF.patch
Patch0005:      0005-Unbreak-the-build-on-modern-gcc-Werror-format-securi.patch

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
BuildRequires:  zipios++-devel
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
License:        GPLv2+
BuildArch:      noarch

%description data
Data files (levels, graphics, sound, music) and documentation for Enigma.

%prep
%autosetup -S git_am
rm -r lib-src/zipios++ lib-src/enet/*

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
