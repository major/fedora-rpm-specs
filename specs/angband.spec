Name:    angband
Version: 4.2.6
Release: %autorelease
Summary: Popular roguelike role playing game

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://rephial.org/
Source0: angband-%{version}-norestricted.tar.gz
# angband contains assets and code that don't comply to Fedora's 
# licensing restrictions. Therefore we use this script to download 
# and remove the restricted files before shipping it.
# Invoke this script to download and generate a patched tarball:
# ./generate-tarball.sh
Source1: generate-tarball.sh
# The fix-restricted.patch file is used by generate-tarball.sh to fix
# the source to work without the restricted assets.
Source2: fix-restricted.patch
# Add warning when running on gnome desktop
Source3: angband-sdl
# Add launcher to pick where to save to
Source4: angband-launcher

# Specific Fedora restriction on chown usage during install process
Patch0: angband-4.2.4-1-chown_fix.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: python3-docutils

Requires: hicolor-icon-theme
Requires: freetype >= 2.11.0-3
Requires: xorg-x11-fonts-misc
Requires: zenity
Requires: %{name}-data = %{version}-%{release}

%description
A roguelike game where you explore a very deep dungeon, kill monsters, try to
equip yourself with the best weapons and armor you can find, and finally face
Morgoth - "The Dark Enemy".


%package data
Summary: Angband data files
License: GPL-2.0-only AND CC-BY-3.0 AND CC-BY-4.0
BuildArch: noarch

%description data
Data files for the Angband game


%package doc
Summary: Angband doc files

%description doc
Documentation about the Angband game


%prep
%autosetup -p1
./autogen.sh

# file-not-utf8 fix
iconv -f iso8859-1 -t utf-8 \
    docs/version.rst > docs/version.rst.conv && \
    mv -f docs/version.rst.conv docs/version.rst
desktop-file-edit \
    --set-key="Exec" --set-value="angband-sdl" \
    --set-key="TryExec" --set-value="angband-sdl" \
    lib/icons/angband-sdl2.desktop
cp lib/icons/angband-sdl2.desktop \
    lib/icons/angband-launcher.desktop
desktop-file-edit \
    --set-name="Angband Launcher" \
    --set-key="Exec" --set-value="angband-launcher" \
    --set-key="TryExec" --set-value="angband-launcher" \
    lib/icons/angband-launcher.desktop


%build
%configure \
    --with-private-dirs \
    --with-gamedata-in-lib \
    --enable-sdl2 \
    --enable-sdl2-mixer
%make_build PROGNAME=%{name}_homedir

%configure \
    --with-setgid=games \
    --with-gamedata-in-lib \
    --enable-sdl2 \
    --enable-sdl2-mixer
%make_build


%install
%make_install
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}/scores
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}/archive
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}/save
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}/panic

# Install desktop files
desktop-file-install \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    lib/icons/angband-launcher.desktop
desktop-file-install \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    lib/icons/angband-x11.desktop
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/angband.metainfo.xml

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6/
install -p -m 644 src/angband.man $RPM_BUILD_ROOT%{_mandir}/man6/angband.6
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/angband-sdl
install -p -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/angband-launcher
install -p -m 755 src/%{name}_homedir $RPM_BUILD_ROOT/%{_bindir}/%{name}_homedir


%files
%license docs/copying.rst
%attr(2755,root,games) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}-sdl
%attr(0755,root,root) %{_bindir}/%{name}-launcher
%attr(0755,root,root) %{_bindir}/%{name}_homedir
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-x11.desktop
%{_datadir}/applications/%{name}-launcher.desktop
%{_metainfodir}/angband.metainfo.xml
%dir %{_sysconfdir}/angband
%dir %{_sysconfdir}/angband/customize
%config(noreplace) %{_sysconfdir}/angband/customize/*
%dir %attr(0775,root,games) %{_var}/games/%{name}
%dir %attr(2775,root,games) %{_var}/games/%{name}/scores
%dir %attr(2775,root,games) %{_var}/games/%{name}/archive
%dir %attr(2775,root,games) %{_var}/games/%{name}/save
%dir %attr(2775,root,games) %{_var}/games/%{name}/panic
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_mandir}/man6/angband.*


%files data
%license docs/copying.rst
%{_datadir}/angband


%files doc
%license docs/copying.rst
%doc docs/*.rst


%changelog
%autochangelog
