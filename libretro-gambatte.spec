%global commit  e00db0d2c645b0074a5bd7261ede2b2f7c6791e8
%global date    20230825
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename gambatte

Name:           libretro-%{corename}
Version:        0
Release:        0.9.%{date}git%{shortcommit}.%autorelease
Summary:        Libretro implementation of libgambatte

License:        GPLv2
URL:            https://github.com/libretro/gambatte-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
Gambatte is an accuracy-focused, open-source, cross-platform Game Boy Color
emulator written in C++. It is based on hundreds of corner case hardware tests,
as well as previous documentation and reverse engineering efforts.

The core emulation code is contained in a separate library back-end
(libgambatte) written in platform-independent C++. There is currently a GUI
front-end (gambatte_qt) using Trolltech's Qt4 toolkit, and a simple command-line
SDL front-end (gambatte_sdl).

The GUI front-end contains platform-specific extensions for video, sound and
timers. It should work on MS Windows, Linux/BSD/UNIX-like OSes, and Mac OS X.

The SDL front-end should be usable on all platforms with a working SDL port. It
should also be quite trivial to create new (simple) front-ends (note that the
library API should in no way be considered stable).


%prep
%autosetup -n %{corename}-libretro-%{commit}
iconv -f iso8859-1 -t utf-8 README.md > README.md.conv && mv -f README.md.conv README.md


%build
%set_build_flags
%make_build


%install
%make_install core_installdir=%{_libdir}/libretro
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license COPYING
%doc README.md
%{_libdir}/libretro/


%changelog
%autochangelog
