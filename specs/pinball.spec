# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Name:           pinball
Version:        0.3.4
Release:        18%{?dist}
Summary:        Emilia 3D Pinball Game
# core license is GPLv2+
# gnu table licenses are (GFDL or Free Art or CC-BY-SA) and GPLv3 and CC-BY-SA
# hurd table license is GPLv2+
License: GPL-2.0-or-later AND FSFAP AND LGPL-2.0-or-later AND GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            http://pinball.sourceforge.net
Source0:        https://github.com/sergiomb2/pinball/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libXt-devel
BuildRequires:  freeglut-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  gettext-devel
Requires:   hicolor-icon-theme
Requires:   opengl-games-utils
Requires:   timidity++-patches

%description
The Emilia Pinball project is an open source pinball simulator for linux
and other unix systems. The current release features a number of tables:
tux, professor, professor2, gnu and hurd and is very addictive.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files for development with %{name}.
May be used in pinball-pinedit.


%prep
%setup -q
sed -i 's/Exec=pinball/Exec=pinball-wrapper/' pinball.desktop
./bootstrap


%build
%configure --disable-static
%make_build


%install
%make_install
%find_lang %{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
# remove unused test module
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/libModuleTest.*
# .la files are needed for ltdl

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --set-key='Keywords' --set-value='Game;Arcade;Pinball;' \
  pinball.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pinball.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 pinball.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc README ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*so.*
%{_libdir}/%{name}/*la
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files devel
%{_bindir}/%{name}-config
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.a
%{_includedir}/%{name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3.4-13
- migrate to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 0.3.4-10
- Disable automatic .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Sérgio Basto <sergio@serjux.com> - 0.3.4-1
- Update to 0.3.4
- Add gettext-devel for translations
- Added devel package for pinball-edit
- Fix License tag
- libtool already requires autoconf and automake

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan  9 2016 Hans de Goede <hdegoede@redhat.com> - 0.3.2-3
- Add Keywords field to desktop file

* Mon Dec 14 2015 Jon Ciesla <limburgher@gmail.com> - 0.3.2-2
- Fix license tag, BZ 1290935.

* Mon Oct 26 2015 Hans de Goede <hdegoede@redhat.com> - 0.3.2-1
- Switch to new github upstream
- Update to 0.3.2 release
- Add an appdata file
- Add Requires: timidity++-patches so that the music works

* Fri Aug 21 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.3.1-27
- Let configure honor CFLAGS (Add pinball-0.3.1-cflags.patch)
  (Fix F23FTBS, RHBZ#1239792).
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3.1-24
- Run autoreconf to fix FTBFS on aarch64 (#926341)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.3.1-21
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-19
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Jon Ciesla <limb@jcomserv.net> - 0.3.1-16
- Fix FTBFS, BZ 631379.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Jon Ciesla <limb@jcomserv.net> - 0.3.1-14
- Patch for strict prototypes.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jon Ciesla <limb@jcomserv.net> - 0.3.1-12
- Cleaned up summary.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.1-11
- Autorebuild for GCC 4.3

* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-10
- Drop the bogus -devel package (also fixing the multilib conficts caused by
  it, bz 342881)

* Mon Sep 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-9
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-8
- Update License tag for new Licensing Guidelines compliance

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-7
- Fixup .desktop file categories for games-menus usage

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-6
- FE6 Rebuild

* Thu Aug 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-5
- Add missing rm -rf $RPM_BUILD_ROOT to %%install

* Fri Aug  4 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-4
- Make building use / honor $RPM_OPT_FLAGS
- Add missing BR: libtool-ltdl-devel
- Remove %%{?_smp_mflags} as that breaks building when actually set

* Thu Aug  3 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-3
- Cleaned up specfile for Fedora Extras submission, based on Che's newrpms spec
- Use system ltdl

* Sat Apr 05 2003 che
- upgrade to version 0.2.0a

* Mon Mar 03 2003 Che
- upgrade to version 0.1.3

* Mon Nov 04 2002 Che
- upgrade to version 0.1.1

* Wed Oct 30 2002 Che
- initial rpm release
