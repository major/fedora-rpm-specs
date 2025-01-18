Summary: Fish Fillets Next Generation, a puzzle game with 70 levels
Name: fillets-ng
Version: 1.0.1
Release: 37%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://fillets.sourceforge.net/
Source0: https://downloads.sf.net/fillets/fillets-ng-%{version}.tar.gz
Source1: fillets.desktop
# fillets.svg is based on doc/html/img/icon.png from upstreams fillets-ng-data.
# inkscape was used to smooth things out and the outer boundries were converted 
# to exact cirles.
Source2: fillets.svg
# compilation fix for gcc >= 4.3
Patch0: fillets-ng-0.8.1-gcc43.patch
# compilation fix for lua >= 5.2
# http://sourceforge.net/p/fillets/bugs/7/
Patch1: fillets-ng-1.0.1-lua-5.2.patch
# compilation fix for lua >= 5.4
Patch2: fillets-ng-1.0.1-lua-5.4.patch
Patch3: fillets-ng-1.0.1-f35-startup-crash.patch
Requires: fillets-ng-data >= 1.0.1-4
Requires: hicolor-icon-theme
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: SDL-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(lua)
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Fish Fillets is strictly a puzzle game. The goal in every of the
seventy levels is always the same: find a safe way out. The fish utter
witty remarks about their surroundings, the various inhabitants of
their underwater realm quarrel among themselves or comment on the
efforts of your fish. The whole game is accompanied by quiet,
comforting music.


%prep
%setup -q
%patch -P0 -p1 -b .gcc43
%patch -P1 -p0 -b .lua52
%patch -P2 -p1 -b .lua54
%patch -P3 -p1 -b .f35crash


%build
%configure --datadir=%{_datadir}/fillets-ng
%make_build


%install
%make_install

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor="" \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}

# Install themeable icon
install -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/icons//hicolor/scalable/apps/fillets.svg

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_metainfodir}
cat > %{buildroot}%{_metainfodir}/fillets.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: ivo@danihelka.net
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">fillets.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>solve the puzzle and help the fish escape</summary>
  <description>
    <p>
      Fish Fillets is a puzzle game where the player has to guide a fish through a series
      of obstacles to escape the maze.
      Fish Fillets features over 70 levels of puzzles and a comforting soundtrack.
    </p>
  </description>
  <url type="homepage">http://fillets.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://fillets.sourceforge.net/img/screenshot/ffng-pyramid.png</screenshot>
    <screenshot>http://fillets.sourceforge.net/img/screenshot/ffng-chest.png</screenshot>
  </screenshots>
</application>
EOF


%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/fillets.appdata.xml



%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/fillets
%{_metainfodir}/fillets.appdata.xml
%{_datadir}/applications/fillets.desktop
%{_datadir}/icons/hicolor/scalable/apps/fillets.svg
%{_mandir}/man6/fillets.6*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.1-36
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Nikolay Nikolov <nickysn@gmail.com> - 1.0.1-28
- Fixed crash on startup in Fedora 35

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Nikolay Nikolov <nickysn@gmail.com> - 1.0.1-26
- Documented the patches
- Replaced make %%{?_smp_mflags} with %%make_build
- Replaced make install DESTDIR=%%{buildroot} with %%make_install
- Replaced %%{__mkdir_p} with mkdir -p
- Replaced %%{__install} with install

* Thu Apr 29 2021 Nikolay Nikolov <nickysn@gmail.com> - 1.0.1-25
- Added BuildRequires: make
- Don't use macro for invoking make
- Replaced BuildRequires: /usr/bin/appstream-util with libappstream-glib
- Replaced $RPM_BUILD_ROOT with %%{buildroot} for consistency
- Use %%{_metainfodir} instead of %%{_datadir}/appdata
- Source URL switched to https

* Thu Apr 29 2021 Nikolay Nikolov <nickysn@gmail.com> - 1.0.1-24
- Fixed compilation with lua 5.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.0.1-19
- Remove obsolete requirements for %%post/%%postun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-15
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 David King <amigadave@amigadave.com> - 1.0.1-10
- Use license macro for COPYING
- Remove obsolete clean and defattr statements
- Use pkgconfig for BuildRequires
- Use lua 5.2 patch from upstream bugtracker
- Depend on hicolor-icon-theme for icon directory ownership
- Validate AppData during check

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Bruno Wolff III <bruno@wolff.to> = 1.0.1-8
- Replace 32x32 icon with an svg icon (bz 1157529)

* Fri May 08 2015 Bruno Wolff III <bruno@wolff.to> = 1.0.1-7
- The lua 5.2 patch wasn't working, switch to using compat version for 5.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0.1-5
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- lua 5.2 fix

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 12 2009 Matthias Saou <http://freshrpms.net/> 0.9.1-1
- Update to 0.9.1.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Matthias Saou <http://freshrpms.net/> 0.8.1-1
- Update to 0.8.1.
- Update gcc43 patch (still applied with fuzz, but...).
- Add LogicGame category to the desktop file (#485349).

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 0.8.0-2
- Add coreutils requirement for scriplets (#475931).
- Enclose gtk-update-icon-cache scriplet calls in "ifs".

* Sun Feb 24 2008 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Update to 0.8.0.
- Include patch to fix build with gcc 4.3.
- Include patch to fix build with fribidi 0.19.1.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 0.7.4-3
- Rebuild for new BuildID feature.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 0.7.4-2
- Update License field.

* Wed Jun 20 2007 Matthias Saou <http://freshrpms.net/> 0.7.4-1
- Update to 0.7.4.
- Switch to using downloads.sf.net source URL.
- Switch to using the DESTDIR install method.
- Remove the fedora desktop file prefix.
- Remove all patches, no longer required, don't autoreconf anymore either.
- Force datadir to be the new location of our fillets-ng-data package's files.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.7.3-5
- FC6 rebuild.
- Add libX11 patch, link against X11 even when SDL isn't (#204594, #204600).

* Wed May 31 2006 Matthias Saou <http://freshrpms.net/> 0.7.3-4
- Add patch to change lua detection from lua-config to pkgconfig since the
  latest lua packages no longer provide the config script.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.7.3-3
- FC5 rebuild.

* Wed Feb  8 2006 Matthias Saou <http://freshrpms.net/> 0.7.3-2
- Rebuild for new gcc/glibc.

* Wed Oct 12 2005 Matthias Saou <http://freshrpms.net/> 0.7.3-1
- Update to 0.7.3.
- Enable fribidi support.

* Tue Aug 23 2005 Richard Henderson <rth@redhat.com> 0.7.1-1
- Update to version 0.7.1.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.6.0-2
- rebuilt

* Tue Feb  1 2005 Matthias Saou <http://freshrpms.net/> 0.6.0-1
- Split sources into separate source rpms (for data to be noarch).
- Minor spec file tweaks.
- Include icon from 0.6.1 data for the desktop entry.
- Remove unneeded explicit vorbis dependency.
- Added update-desktop-database calls.

* Sun Aug 22 2004 Michal Ambroz (O_O) <rebus@seznam.cz>
- rebuild 0.5.1 for Fedora Core 2

* Thu Jul 15 2004 Michal Ambroz (O_O) <rebus@seznam.cz>
- rebuild 0.4.1 for Fedora Core 2

* Thu Jul 15 2004 Michal Ambroz (O_O) <rebus@seznam.cz>
- rebuild 0.4 for Fedora Core 2

* Mon May 10 2004 Michal Ambroz (O_O) <rebus@seznam.cz>
- initial build for Fedora Core 2

