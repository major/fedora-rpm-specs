%global appname         com.github.tkashkin.%{name}
%global short_version   0.16.3
%global minor_version   2
%global dev_version     %{short_version}-%{minor_version}-master

# Upstream recommendation disabling all optimizations due to known bugs
#   * https://github.com/tkashkin/GameHub/pull/169
%global optflags %{optflags} -O0

Name:           gamehub
Version:        %{short_version}.%{minor_version}
Release:        %autorelease
Summary:        All your games in one place

License:        GPL-3.0-or-later
URL:            https://github.com/tkashkin/GameHub
Source0:        %{url}/archive/%{dev_version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.60
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(manette-0.2)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(unity)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme
Requires:       polkit

Recommends:     dosbox
Recommends:     file-roller
Recommends:     innoextract
Recommends:     wine
Recommends:     wine-dxvk
# Requires for GOG DOSBox games
Recommends:     libcaca
# Interpreter for several adventure games
Recommends:     scummvm

%description
GameHub is a unified library for all your games. It allows you to store your
games from different platforms into one program to make it easier for you to
manage your games. Features

With GameHub, you can:

  * store your games in one place
  * login to multiple platforms
  * install games from the supported sources
  * download game installers, DLCs and bonus content
  * automatically find artwork for games on SteamGridDB
  * setup emulators and automatically import emulated games

GameHub also has features like:

  * Overlays — multiple directories applied on top of each other. Each overlay
    is stored separately and doesn't affect other overlays. Overlays can be
    useful to manage DLCs and mods
  * Tweaks — environment variable and command line overrides that can be
    applied to games automatically

GameHub supports:

  * native games for Linux
  * multiple compatibility layers:
    - Wine
    - Proton
    - DOSBox
    - RetroArch
    - ScummVM
    - WineWrap — a set of preconfigured wrappers for supported games;
    - custom emulators
  * multiple game platforms:
    - Steam
    - GOG
    - Humble Bundle (including Humble Trove)
    - itch.io


%prep
%autosetup -p1 -n GameHub-%{dev_version}


%build
branch=master
commit=9327885393f022fd1cccb219a19c0f87ae5e0f5a
commit_short="$(c=${commit}; echo ${c:0:7})"
%meson                                      \
    --buildtype=debug                       \
    -Dgit_branch="${branch}"                \
    -Dgit_commit="${commit}"                \
    -Dgit_commit_short="${commit_short}"    \
    %{nil}
%meson_build


%install
%meson_install
%find_lang %{appname}

# No HiDPI icons version yet
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{appname}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_bindir}/%{appname}-overlayfs-helper
%{_bindir}/%{name}
%{_datadir}/%{appname}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/polkit-1/actions/*.policy
%{_metainfodir}/*.appdata.xml


%changelog
%autochangelog
