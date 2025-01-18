Name:    angband
Version: 4.2.5
Release: 6%{?dist}
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

# Specific Fedora restriction on chown usage during install process
Patch0: angband-4.2.4-1-chown_fix.patch
# https://github.com/angband/angband/pull/5751
Patch1: angband-4.2.5-1-desktop_fix.patch

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
Requires: %{name}-data = %{version}-%{release}

%description
A roguelike game where you explore a very deep dungeon, kill monsters, try to
equip yourself with the best weapons and armor you can find, and finally face
Morgoth - "The Dark Enemy".


%package data
Summary: Angband data files
# Automatically converted from old format: GPLv2 and CC-BY - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-CC-BY
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


%build
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

# Install both x11 and sdl2 desktop files
rm ${RPM_BUILD_ROOT}%{_datadir}/applications/angband.desktop
desktop-file-install \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    lib/icons/angband-sdl2.desktop
desktop-file-install \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    lib/icons/angband-x11.desktop
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/angband.metainfo.xml

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6/
install -p -m 644 src/angband.man $RPM_BUILD_ROOT%{_mandir}/man6/angband.6


%files
%license docs/copying.rst
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/applications/*.desktop
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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.5-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 7 2023 Diego Herrera <dherrera@redhat.com> 4.2.5-1
- Updated version to 4.2.5
- Upstreamed assets
- Enable x11 support

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 23 2022 Diego Herrera <dherrera@redhat.com> 4.2.4-3
- Fixed information on metainfo file

* Tue Feb 22 2022 Diego Herrera <dherrera@redhat.com> 4.2.4-2
- Removed scalable image

* Tue Feb 22 2022 Diego Herrera <dherrera@redhat.com> 4.2.4-1
- Updated version to 4.2.4
- Removed upstreamed patches
- Added metainfo file

* Tue Jan 25 2022 Diego Herrera <dherrera@redhat.com> 4.2.3-6
- Update desktop file
- Use icons provided by source
- Changed freetype minimal required version

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Diego Herrera <dherrera@redhat.com> 4.2.3-4
- Added make as an expicit BuildRequires
- Removed Requires that can be autodetected
- Fixed licensing description
- Use macros when needed
- Separated doc files into a separate package
- Added license to subpackages
- Added some missing folders in the installation process

* Mon Dec 13 2021 Diego Herrera <dherrera@redhat.com> 4.2.3-3
- Move customize folder to sysconfdir
- Add patch to keep the gamedata folder to datadir
- Add references to upstream patches

* Sun Dec 12 2021 Diego Herrera <dherrera@redhat.com> 4.2.3-2
- Restored Adam Bolt's tileset
- Fix typos and descriptions

* Sat Dec 11 2021 Diego Herrera <dherrera@redhat.com> 4.2.3-1
- Update to 4.2.3
- Use setgid mode with games group
- Change default renderer to SDL2
- Apply upstream fixes to SDL2 implementation
- Remove more restricted assets
- Move game data to datadir

* Sun Aug 25 2019 Wart <wart at kobold dot org> 4.2.0-1
- Update to 4.2.0
- Fix group creation
- Fix desktop file
- Update license naming
- Add man page
- Remove restricted tileset

* Tue Aug 13 2019 Wart <wart at kobold dot org> 4.1.3-4
- Use recommended dynamic allocation for the group

* Sat Aug 10 2019 Wart <wart at kobold dot org> 4.1.3-3
- Minor spec file cleanup

* Wed Jul 24 2019 Wart <wart at kobold dot org> 4.1.3-2
- Enable shared scoreboard file

* Sun Jul 21 2019 Wart <wart at kobold dot org> 4.1.3-1
- Update to 4.1.3

* Sun Jul 21 2019 Wart <wart at kobold dot org> 3.0.6-5
- Updates to build for Fedora 30

* Wed Apr 4 2007 Wart <wart at kobold dot org> 3.0.6-4
- Add BR: to allow X11 support

* Tue Apr 3 2007 Wart <wart at kobold dot org> 3.0.6-3
- Add icon name to .desktop files
- Fix License tag
- Move game data to /var/games/angband
- Remove non-working -graphics desktop file

* Mon Apr 2 2007 Wart <wart at kobold dot org> 3.0.6-2
- Use custom group for setgid as added protection
- Install extra graphics files
- Add vendor to .desktop file installation

* Thu Mar 29 2007 Wart <wart at kobold dot org> 3.0.6-1
- Update to 3.0.6
- Updated spec to Fedora Extras standards (again)

* Sat Feb 25 2006 Wart <wart at kobold dot org> 3.0.3-5
- Update. spec to Fedora Extras standards
