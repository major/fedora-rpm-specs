Summary: Arcade 2D shoot-them-up game
Name:           powermanga
Version:        0.93.1
Release:        6%{?dist}
License:        GPL-3.0-or-later
URL:            http://linux.tlk.fr/games/Powermanga/


Source0: http://linux.tlk.fr/games/Powermanga/download/powermanga-%{version}.tgz
Source1: powermanga.png
Source2: powermanga.desktop

# install to directories common for Fedora
Patch0:         powermanga-0.93.1-install.patch

# The resulting binary requires libmikmod.so.3 according to ldd, but the
# automatic dependency isn't generated (#577509)
Requires:       libmikmod
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libmikmod-devel
BuildRequires:  gawk
BuildRequires:  libXt-devel, libXxf86dga-devel, libXxf86vm-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils

%description
Powermanga is a vertical scrolling arcade style 2D shoot-them-up game with
41 levels and more than 200 sprites.


%prep
%autosetup -p 1
autoreconf -v -i

%build
# The original configure script sets that mandatory -std=c99
%configure
%make_build


%install
%make_install

# Allow stripping, g+s will be set back in %%files
%{__chmod} g-s %{buildroot}%{_bindir}/powermanga

# Install pixmap for the menu entry
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/powermanga.png

# Install menu entry
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE2}

# Default to English
echo "Lang=en" > \
    %{buildroot}%{_datadir}/powermanga/texts/config.ini

%files
%doc AUTHORS CHANGES README
%license COPYING
%attr(2755,root,games) %{_bindir}/powermanga
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/powermanga.png
# No _datadir/powermanga/ single line to avoid including config.ini twice
%dir %{_datadir}/powermanga/
%{_datadir}/powermanga/data/
%{_datadir}/powermanga/graphics/
%{_datadir}/powermanga/sound/
%{_datadir}/powermanga/sounds/
%dir %{_datadir}/powermanga/texts/
%{_datadir}/powermanga/texts/*.txt
%config(noreplace) %{_datadir}/powermanga/texts/config.ini
%{_mandir}/man6/powermanga.6*
%{_mandir}/{fr}/man6/powermanga.6*
%config(noreplace) %attr(664,root,games) %{_var}/games/powermanga/powermanga.hi
%config(noreplace) %attr(664,root,games) %{_var}/games/powermanga/powermanga.hi-easy
%config(noreplace) %attr(664,root,games) %{_var}/games/powermanga/powermanga.hi-hard


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 26 2023 Michal Ambroz <rebus _AT seznam.cz> - 0.93.1-2
- bump to 0.93.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.90-22
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 21 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.90-17
- Don't overide CFLAGS in configure (Fix F23FTBFS, RHBZ#1239795).
- Modernize spec.
- Add %%license.
- Pass CFLAGS to %%configure.
- Fix bogus %%changelog entry dates.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun  7 2010 Matthias Saou <http://freshrpms.net/> 0.90-8
- Add dist tag to allow backport of the #577509 fix to F-13 (#600940).

* Wed Apr 28 2010 Matthias Saou <http://freshrpms.net/> 0.90-8
- Add explicit libmikmod requirement (#577509).
- Add -lm to our CFLAGS, required for sqrt in powermanga-display.o.

* Tue Dec  8 2009 Matthias Saou <http://freshrpms.net/> 0.90-7
- Remove coreutils scriplet requirements : Current guidelines don't require it,
  as we have "|| :" anyway.
- Clean up desktop file.
- Fix the build warning about config.ini being listed twice.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 0.90-4
- Add coreutils requirement for scriplets (#475928).
- Enclose gtk-update-icon-cache scriplet calls in "ifs".

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Mon Oct 22 2007 Matthias Saou <http://freshrpms.net/> 0.90-2
- Update to latest upstream sources... same filename, different content!
- Update install patch for it to still apply.

* Mon Sep  3 2007 Matthias Saou <http://freshrpms.net/> 0.90-1
- Update to 0.90.
- Update License field (changed to GPLv3+).
- Update install patch, include fix for "fonts" directory.
- No longer manually install texts, but install the config.ini.
- Add gawk and libpng-devel build requirements.

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 0.80-6
- Rebuild for new BuildID feature.

* Sat Aug  4 2007 Matthias Saou <http://freshrpms.net/> 0.80-5
- Update License field.
- Remove dist tag, since the package will seldom change.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 0.80-4
- Move binary to _bindir and data to _datadir, removing "games" prefixes since
  the guidelines now say so. This should fix prelink's problems (#218280).
- Include patch to acheive the above, move the man6 hack to there too.
- Externalize the desktop file.
- Move icon from pixmaps to 48x48 hicolor, add scriplets.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.80-3
- FC6 rebuild.

* Fri Apr 21 2006 Matthias Saou <http://freshrpms.net/> 0.80-2
- Add a workaround to include the "texts" directory and files, since the game
  won't run without, and they don't get installed automatically! (#188901).

* Tue Apr 11 2006 Matthias Saou <http://freshrpms.net/> 0.80-1
- Update to 0.80, fixes crash at level 35 boss (#184076, Hugo Cisneiros).
- Add new zlib-devel build requirement.
- Add `sdl-config --cflags` to CXXFLAGS, otherwise SDL_mixer.h isn't found.
- Add missing libXt-devel build requirement to get modular X detected.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.79-8
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 0.79-7
- Rebuild for new gcc/glibc and modular X.

* Mon Nov  7 2005 Matthias Saou <http://freshrpms.net/> 0.79-6
- Fix stripping (when g+s is set, it doesn't happen) and add wrapper script in
  $PATH (#165313, Ville Skyttä).
- Let SDL-devel pull in X devel files.
- Remove old freedesktop build conditional.

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 0.79-5
- add patch from Ignacio to fix build on x86_64 (#158464)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.79-4
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.79-3
- rebuilt

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 0.79-2
- Bump release to provide Extras upgrade path.

* Tue Aug 10 2004 Matthias Saou <http://freshrpms.net/> 0.79-1
- Spec file cleanup.
- Included the menu pixmap from the Mandrake package.
- Update to 0.79.

* Wed Dec 20 2000 Matthias Saou <http://freshrpms.net/> 0.71c-2
- Initial RPM release.

