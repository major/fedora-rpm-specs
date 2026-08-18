Name: chroma
%global rtld_name uk.org.level7.chroma

Summary: Abstract puzzle game
License: GPL-2.0-or-later

Version: 1.21
Release: 1%{?dist}

URL: https://www.level7.org.uk/chroma/
Source0: %{URL}download/chroma-%{version}.tar.bz2

Source10: %{rtld_name}.desktop
Source11: %{rtld_name}.metainfo.xml

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libappstream-glib
BuildRequires: make

BuildRequires: freetype-devel
BuildRequires: gettext-devel
BuildRequires: ncurses-devel
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel

%global fontlist font(dejavusans)
BuildRequires: fontconfig
BuildRequires: %{fontlist}

Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-data-gfx = %{version}-%{release}

%global desc %{expand:
Chroma is an abstract puzzle game. A variety of colourful shapes are arranged
in a series of increasingly complex patterns, forming fiendish traps that must
be disarmed and mysterious puzzles that must be manipulated in order to give up
their subtle secrets. Initially so straightforward that anyone can pick it up
and begin to play, yet gradually becoming difficult enough to tax even the
brightest of minds.}

%description %desc


%package curses
Summary: Abstract puzzle game (ncurses version)
Requires: %{name}-data = %{version}-%{release}

%description curses %{desc}

This package provides an ncurses-based build of the game,
which can be played in a terminal.


%package data
Summary: Data files for %{name}
BuildArch: noarch

%description data
This package provides data files (levels, translations, et cetera)
required to play %{name}.


%package data-gfx
Summary: Graphics for %{name}
BuildArch: noarch

Requires: %{fontlist}
Requires: hicolor-icon-theme
Requires: %{name}-data = %{version}-%{release}

%description data-gfx
This package contains graphics and fonts required to play %{name}.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install

# Install desktop & metainfo files
install -D -m 644 -p %{SOURCE10} %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
install -D -m 644 -p %{SOURCE11} %{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml

# Symlink icon from game resources directory to hicolor icon theme dir
ICONDIR="%{buildroot}%{_datadir}/icons/hicolor/48x48/apps"
install -m 755 -d "${ICONDIR}"
ln -srf "%{buildroot}%{_datadir}/%{name}/graphics/icon.png" "${ICONDIR}/%{name}.png"

# Remove bundled font and replace it with a symlink
ln -srf \
	"%{buildroot}$(fc-match -f '%%{file}' 'DejaVuSans')"  \
	"%{buildroot}/%{_datadir}/%{name}/graphics/font.ttf"


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{rtld_name}.desktop
%{_metainfodir}/%{rtld_name}.metainfo.xml


%files curses
%{_bindir}/%{name}-curses


%files data
%doc CHANGELOG README
%license COPYING

%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/graphics/


%files data-gfx
%{_datadir}/%{name}/graphics/
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Sat Aug 15 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.21-1
- Initial packaging
