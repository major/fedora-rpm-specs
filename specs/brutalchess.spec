%global pre     alpha

Name:           brutalchess
Version:        0.5.2
Release:        %autorelease
Summary:        Chess game with impressive 3D graphics

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sf.net/projects/%{name}
# we don't want the original fonts due to legal reasoning
# http://sf.net/projects/%{name}/files/%{name}-%{pre}/%{name}-%{pre}-%{version}/%{name}-%{pre}-%{version}-src.tar.gz
Source0:        %{name}-%{pre}-%{version}-nofonts.tar.xz
Source1:        %{name}-nofonts.sh

Patch0:         https://sf.net/p/%{name}/patches/8/attachment/%{name}-freetype2.patch
# fonts: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=584416
Patch1:         https://sf.net/p/%{name}/patches/7/attachment/%{name}-fonts.diff

# PGN resembling console output, http://sourceforge.net/p/brutalchess/patches/3
Patch2:         http://sf.net/p/%{name}/patches/_discuss/thread/96f1a752/0dc4/attachment/pgn-moveprint.diff
# Fix -l option, http://sourceforge.net/p/brutalchess/patches/2
Patch3:         http://sf.net/p/%{name}/patches/_discuss/thread/b91b1843/e6b7/attachment/fix-player2opt.diff

# FIXME crafty, https://sf.net/p/brutalchess/patches/4
# patch can't be applied cause of any potential security risk, there is currently no crafty package in Fedora

# extensions from slack to let the package actually be usable and build
Source10:       http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}.desktop
Source11:       http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}.png
Patch10:        http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}-%{version}-fix-FTBFS.patch
Patch11:        http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}-%{version}-gcc4.3.patch
Patch12:        http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}-%{version}-gcc4.7.patch

# disable feature: quake pieces are not available, http://bugs.debian.org/732227
Patch20:        brutalchess-noquake.patch

ExcludeArch:    %{ix86}
BuildRequires:  gcc-c++
BuildRequires:  SDL-devel SDL_image-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  freetype-devel
BuildRequires:  doxygen
BuildRequires:  desktop-file-utils
BuildRequires:  make

Requires:       gnu-free-sans-fonts

# -doc subpkg was < 100k, not worth splitting out (yet) -- rex
Obsoletes: brutalchess-doc < 0.5.2-0.4
Provides:  %{name}-doc = %{version}-%{release}

%description
BrutalChess features full 3D graphics, an advanced particle engine, 
and several different levels of intelligent AI, inspired by the once 
popular "Battle Chess" released by Interplay circa 1988.


%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P10
%patch -P11
%patch -P12 -p1
%patch -P20 -p1
# update Doxyfile
doxygen -u
# proper font license
sed -i s,fonts,, Makefile.in
sed -i 's,\(fontsdir=\).*,\1"\${datadir}/fonts/",' configure
sed -i s,ZEROES__.TTF,gnu-free/FreeSans.ttf, src/gamecore.cpp
# W: wrong-file-end-of-line-encoding
sed -i 's/\r$//' NEWS README


%build
%configure
make %{?_smp_mflags}
doxygen


%install
%make_install

# misplaced content
rm -rv %{buildroot}%{_datadir}/%{name}/doc

# desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE10}
install -d %{buildroot}%{_datadir}/pixmaps
cp -p %{SOURCE11} %{buildroot}%{_datadir}/pixmaps


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc doc/html
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/


%changelog
%autochangelog
