Name:           xblast
Version:        2.10.4
Release:        42%{?dist}
Summary:        Lay bombs and Blast the other players of the field (SDL version)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://xblast.sourceforge.net
Source0:        http://downloads.sourceforge.net/xblast/xblast-%{version}.tar.gz
Source1:        xblast.sh
Source2:        xblast.desktop
Source3:        xblast-32.png
Source4:        xblast-48.png
Source5:        xblast-128.png
Source6:        xblast.appdata.xml
Patch0:         xblast-2.10.4-sdl-fixes.patch
Patch1:         xblast-2.10.4-manpage.patch
Patch2:         xblast-2.10.4-fcommon-fix.patch
Patch3:         xblast-2.10.4-font-config-fix.patch
BuildRequires:  gcc make
BuildRequires:  libXt-devel gettext gawk desktop-file-utils SDL_gfx-devel
BuildRequires:  SDL_image-devel SDL_ttf-devel SDL_mixer-devel SDL_net-devel
BuildRequires:  libappstream-glib
Requires:       %{name}-data >= 2.10.0, %{name}-common = %{version}-%{release}
Requires:       font(dejavusans)
Provides:       %{name}-engine = %{version}-%{release}

%description
This is the new SDL version of XBlast, a multi-player game where the "purpose"
is to Blast the other players of the game-field by laying bombs close to them.
While at the same time you must avoid being blown up yourself.


%package x11
Summary:        Lay bombs and Blast the other players of the field (X11 version)
Requires:       %{name}-data >= 2.10.0, %{name}-common = %{version}-%{release}
Requires:       xorg-x11-fonts-ISO8859-1-75dpi
Provides:       %{name}-engine = %{version}-%{release}

%description x11
This is the original X11 version of XBlast, a multi-player game where the
"purpose" is to Blast the other players of the game-field by laying bombs close
to them. While at the same time you must avoid being blown up yourself.


%package common
Summary:        Files common to both the X11 and SDL version of XBlast
Requires:       %{name}-engine = %{version}-%{release}, hicolor-icon-theme

%description common
Files common to both the X11 and SDL version of XBlast, a multi-player game
where the "purpose" is to Blast the other players of the game-field by laying
bombs close to the other player.


%prep
%autosetup -p1
sed -i 's|$(game_datadir)/locale|%{_datadir}/locale|g' Makefile.in
# stop rpmlint from complaining about executable source files in the -debuginfo
chmod -x chat.* version.c
# stop autoxxx from rerunning because of strange timestamps in the tarbal
touch aclocal.m4 configure Makefile.in config.h.in


%build
# first build the SDL version
%configure --with-otherdatadir=%{_datadir}/%{name} --enable-admin --enable-sdl
make %{?_smp_mflags}
mv xblast xblast-sdl

# and then the X11 version
make distclean
%configure --with-otherdatadir=%{_datadir}/%{name} --enable-admin --enable-sound
make %{?_smp_mflags}


%install
make install localedir=%{_datadir}/locale DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}-x11
install -m 755 xblast-sdl $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 644 %{name}.man $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE5} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%{_bindir}/%{name}-sdl

%files x11
%{_bindir}/%{name}-x11
%{_bindir}/xbsndsrv

%files -f %{name}.lang common
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.10.4-41
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Hans de Goede <hdegoede@redhat.com> - 2.10.4-35
- Fix xblast-x11 crashing with BadFont error after using xblast-sdl (#2107144)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar  4 2020 Hans de Goede <hdegoede@redhat.com> - 2.10.4-30
- Fix xblast not starting because of dejavu-sans-fonts path changes
- Replace 128x128 icon with a better version
- Add 32x32 and 48x48 icons for cases where we need a lower res icon

* Wed Feb 19 2020 Hans de Goede <hdegoede@redhat.com> - 2.10.4-29
- Fix FTBFS (rhbz#1800265)
- Replace icon with 128x128 pixel version
- Add appdata
- Change font Requires to font(dejavusans) instead of a file-path (rhbz#1731705)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.10.4-23
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 2.10.4-16
- Rebuild for new SDL_gfx

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.10.4-13
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Hans de Goede <hdegoede@redhat.com> - 2.10.4-10
- Rebuild for new SDL_gfx

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  1 2008 Hans de Goede <hdegoede@redhat.com> 2.10.4-6
- Replace bitstream-vera with dejave font (rh 473563)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.10.4-5
- Autorebuild for GCC 4.3

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.10.4-4
- Update License tag for new Licensing Guidelines compliance

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 2.10.4-3
- Rebuild against SDL_gfx 2.0.16.

* Thu Mar  1 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.10.4-2
- Use sf.net sourceforge URL from the Guidelines (bz 229476)
- Keep timestamp while installing the wrapper (bz 229476)
- Sanitize and install the manpage (bz 229476)
- Add "Requires: xorg-x11-fonts-ISO8859-1-75dpi" to xblast-x11 (bz 229476)
- Make xblast look for translations under /usr/share/locale (bz 229476)

* Thu Feb  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.10.4-1
- Initial Fedora Extras package
