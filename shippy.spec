Name:           shippy
Version:        1.5.0
Release:        8%{?dist}
Summary:        Space invaders / Galaxians like game with power-ups
License:        GPL+
URL:            http://identicalsoftware.com/shippy1984/
Source0:        http://identicalsoftware.com/shippy1984/shippy-%{version}.tgz
Source1:        shippy.png
Source2:        shippy.desktop
Source3:        shippy.sh
Source4:        %{name}.appdata.xml
# Patch to add/keep the shared highscore support Fedora patched into 1.3.3.7
# so that people do not loose their highscores
Patch0:         shippy-1.5.0-shared-highscores.patch
Patch1:         shippy-1.5.0-warning-fixes.patch
Patch2:         shippy-1.5.0-sdl2-fs-toggle.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  dumb-devel SDL2_mixer-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       %{name}-common = %{version}
Provides:       %{name}-engine = %{version}

%description
Shippy1984 is a small, portable game designed to bring back nostalgia for the
ways games used to be made--addicting as hell! Mash buttons on your way to the
high score! Shippy1984 is designed from the ground up for the avid casual
gamer who feels left behind by the technological overload of today's games!
No longer! Shippy1984 is the game you have been waiting for!


%package allegro
Summary:        Shippy1984 Allegro version
Requires:       %{name}-common = %{version}
Provides:       %{name}-engine = %{version}

%description allegro
Alternative version of Shippy1984 compiled to use the allegro display library.


%package common
Summary:        Shippy1984 common files
Requires:       %{name}-engine = %{version}
Requires:       hicolor-icon-theme

%description common
Data files, desktop entry and icon, docs and wrapper-script for the
Shippy1984 game.


%prep
%autosetup -p1
mv docs html
#see comment in %%install
rm data/scores.lst


%build
make %{?_smp_mflags} SDL2=1 \
 CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DDATADIR=\\\"%{_datadir}/%{name}/\\\"" \
 LDFLAGS="-g `sdl2-config --libs` -lSDL2_mixer"
mv %{name} %{name}-sdl

make %{?_smp_mflags} ALLEGRO=1 \
 CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DDATADIR=\\\"%{_datadir}/%{name}/\\\"" \
 LDFLAGS="-g -laldmb -ldumb `allegro-config --libs`"
mv %{name} %{name}-allegro


%install
# no make install target so DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 755 %{name}-sdl %{name}-allegro $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -p -m 644 data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
# scores.lst is a binary file which is different on MSB vs LSB, so we just
# create an empty file, then the game will use its identical internal defaults
# and fill it with data in platform format after the first run.
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/games
touch $RPM_BUILD_ROOT%{_var}/lib/games/%{name}.hs
# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%attr(2755,root,games) %{_bindir}/%{name}-sdl

%files allegro
%attr(2755,root,games) %{_bindir}/%{name}-allegro

%files common
%doc NOTES.txt html
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%config(noreplace) %attr (0664,root,games) %{_var}/lib/games/%{name}.hs


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Hans de Goede <hdegoede@redhat.com> - 1.5.0-1
- New upstream: http://identicalsoftware.com/shippy1984/
- New upstream release 1.5.0
- SDL version now uses SDL2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.3.7-25
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Hans de Goede <hdegoede@redhat.com> - 1.3.3.7-20
- Backport splashscreen improvements from upstream devel version
- Add appdata, .desktop file keywords

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.3.7-15
- Remove --vendor from desktop-file-install on F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 16 2011 Hans de Goede <hdegoede@redhat.com> - 1.3.3.7-11
- Rebuild for new allegro-4.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.3.7-7
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3.7-6
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3.7-5
- Update License tag for new Licensing Guidelines compliance
- Fix invalid desktop file (fix building with latest desktop-file-utils)

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3.7-4
- FE6 Rebuild

* Thu Jul  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3.7-3
- Rebuild against new allegro to remove executable stack requirement caused
  by previous versions of allegro.
- Merged all patches into one and put a few parts between #ifdef __unix__
  (I send this upstream for merging).

* Thu Mar 30 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3.7-2
- Fix reversed joy directions in allegro version
- Improve support for analog joysticks in the allegro version
- Add support for joysticks to the SDL version

* Mon Mar 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3.7-1
- Initial Fedora Extras package
- Todo: add joystick support to SDL version
