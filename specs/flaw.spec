%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		flaw
Version:	1.3.2a
Release:	34%{?dist}
Summary:	Free top-down wizard battle game
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://flaw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
#patch to build on aarch64, upstream notified to use autoconf 2.69
Patch0:		flaw-aarch64.patch

BuildRequires:  gcc-c++
BuildRequires:	SDL_image-devel SDL_mixer-devel SDL_ttf-devel SDL-devel gnu-free-serif-fonts 
BuildRequires:	SDL_gfx-devel desktop-file-utils gnu-free-sans-fonts gettext intltool
BuildRequires:	gcc
BuildRequires: make
Requires:	gnu-free-sans-fonts gnu-free-serif-fonts

%description
FLAW is a free top-down wizard battle game.
It can be played by up to 5 players simultaneously. The goal of the game is to
survive as long as possible while more and more fireballs appear in the arena.
Game play is simple and self-explanatory. It's all about evading the fireballs
and knocking your opponents down. In addition there are collectible magic gems
that provide special abilities.

%prep
%autosetup

# Fix spurious executable permissions
chmod 644 src/*.cc
chmod 644 src/*.h

# Remove deprecated tag Enconding from flaw.desktop
sed -i -e '2d' data/flaw.desktop

%build
%configure --docdir=%{_pkgdocdir}
%make_build

%install
%make_install

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/flaw/feature-requests/3/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">flaw.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Casual Wizards Battle Game</summary>
  <description>
    <p>
      Flaw is a game where you control a wizard and your goal is to survive as
      much as you can.
    </p>
    <p>
      In addition to the fireballs that arise increasingly in larger quantities,
      there are other wizards trying to kill you.
    </p>
    <p>
      The game has some items that give you special abilities to defend yourself or attack your enemies.
    </p>
    <p>
      Flaw can be played on single-player mode or with your friends.
    </p>
  </description>
  <url type="homepage">http://flaw.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://flaw.sourceforge.net/images/ingame1.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/ingame3.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/ingame2.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/menu.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%{_bindir}/flaw
%{_datadir}/flaw
%{_datadir}/pixmaps/flaw.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/flaw.desktop
%exclude %{_pkgdocdir}/INSTALL
%doc %{_pkgdocdir}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.2a-33
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.2a-18
- added gcc as BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.2a-11
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.3.2a-10
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 1.3.2a-8
- Rebuild for new SDL_gfx

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 09 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.2a-6
- Fix rhbz #925345 (now build on aarch64) and spec clean up

* Sat Nov 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.3.2a-5
- Install docs to %%{_pkgdocdir} where available (#993753).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Filipe Rosset <rosset.filipe@gmail.com> 1.3.2a-3
- Fix for #890228

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Filipe Rosset <filiperosset@fedoraproject.org> - 1.3.2a-1
- Updated to version 1.3.2a upstream
