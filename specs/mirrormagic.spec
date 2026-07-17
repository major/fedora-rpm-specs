Name:           mirrormagic
Version:        3.3.1
Release:        1%{?dist}
Summary:        Puzzle game where you steer a beam of light using mirrors
License:        GPL-2.0-only
URL:            https://www.artsoft.org/mirrormagic/
Source0:        https://www.artsoft.org/RELEASES/linux/%{name}/%{name}-%{version}-linux.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
BuildRequires:  gcc make
BuildRequires:  SDL2_image-devel SDL2_mixer-devel SDL2_net-devel
BuildRequires:  zlib-devel
BuildRequires:  libappstream-glib desktop-file-utils
Requires:       hicolor-icon-theme

%description
MirrorMagic is a game where you shoot around obstacles to collect energy using
your beam. It is similar to "Mindbender" (Amiga) from the same author. The goal
is to work out how to get around obstacles to shoot energy containers with your
beam, thereby opening the path to the next level. Included are many levels
familiar from the games "Deflektor" and "Mindbender".


%prep
%autosetup -p1
rm levels/Classic_Games/classic_mindbender/*.level.orig
rm levels/Classic_Games/classic_mindbender/tapes/*.tape.orig
# Remove pre-built binary and bundled libraries
rm %{name}
rm -r lib


%build
# parallel build has been disabled because for some unknown reason
# it leads to unknown symbols during the linking of the mirrormagic binary
make PROGBASE=%{name} BASE_PATH=%{_datadir}/%{name} \
  OPTIONS="$RPM_OPT_FLAGS" \
  EXTRA_LDFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS"


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a graphics levels music sounds $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc CREDITS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%changelog
* Tue Jul 14 2026 Michal Schorm <mschorm@redhat.com> - 3.3.1-1
- Rebase to upstream version 3.3.1
- Update 'Source0' URL: upstream moved from '/unix/' to '/linux/' path
  and changed the tarball naming convention to include '-linux' suffix
- Drop all three patches, merged upstream:
  'mirrormagic-3.0.0-yesno.patch' (Y/N key handling),
  'mirrormagic-3.0.0-fcommon-fix.patch' (-fcommon multiple definitions),
  'mirrormagic-3.0.0-c23.patch' (C23 compatibility)
- Update build flags: replace 'RO_GAME_DIR' with 'BASE_PATH',
  drop removed 'sdl2' make target (now auto-detected),
  drop unused '-DUSE_USERDATADIR_FOR_COMMONDATA' flag
- Add 'zlib-devel' BuildRequires (new upstream zip support via bundled minizip)
- Remove pre-built binary and bundled shared libraries in '%prep'
- Drop iconv CREDITS conversion (file is now UTF-8 upstream)
- Correct License to 'GPL-2.0-only' (COPYING contains GPL-2.0 text; the prior
  'GPL-1.0-or-later' was a mechanical SPDX conversion from the old 'GPL+' tag)
- Update URL to HTTPS

* Sat Jan 24 2026 Hans de Goede <johannes.goede@oss.qualcomm.com> - 3.0.0-22
- Fix FTBFS (rhbz#2340868, rhbz#2385191)

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun  17 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.0-17
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 23 2023 Hans de Goede <hdegoede@redhat.com> - 3.0.0-13
- Fix FTBFS (rhbz#2171614)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar  7 2020 Hans de Goede <hdegoede@redhat.com> - 3.0.0-6
- Fix FTBFS (rhbz#1799656)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Hans de Goede <hdegoede@redhat.com> - 3.0.0-1
- New upstream release 3.0.0 (rhbz#1568608)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-23
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Hans de Goede <hdegoede@redhat.com> - 2.0.2-18
- Fix FTBFS
- Add appdata file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Hans de Goede <hdegoede@redhat.com> - 2.0.2-15
- Fix building with -Werror=format-security (rhbz#1037200)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0.2-12
- Remove --vendor from .desktop on F19+

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.2-5
- Autorebuild for GCC 4.3

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.2-4
- Update License tag for new Licensing Guidelines compliance

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.2-3
- Splitoff 3 seperate patches from patch0 for upstream merging
- Fixup .desktop file categories for games-menus usage

* Sat Sep 30 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.2-2
- Add a patch which fixes running (startup) on 64 bit archs

* Fri Sep 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.2-1
- Initial Fedora Extras package
