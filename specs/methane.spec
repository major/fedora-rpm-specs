Name:           methane
Version:        1.5.1
Release:        37%{?dist}
Summary:        Super Methane Brothers
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://methane.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch1:         methane-highscore.patch
Patch2:         methane-fullscreen.patch
Patch3:         methane-1.5.1-clanlib-23.patch
Patch4:         methane-1.5.1-gcc5.patch
BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  ClanLib-devel >= 2.3 desktop-file-utils
Requires:       hicolor-icon-theme opengl-games-utils

%description
Super Methane Brothers is a platform game converted from the Amiga by
its original author.


%prep
%autosetup -p1


%build
make CXXFLAGS="$RPM_OPT_FLAGS"


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/games
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a resources $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
touch $RPM_BUILD_ROOT%{_var}/games/%{name}.scores

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

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
<!-- Copyright 2014 William Moreno Reyes <williamjmorenor@gmail.com> -->
<!--
UpstreamURL:  Upstream is dead, private email
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">methane.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Platform Arcade Game similar to Bubble Bubble</summary>
  <description>
    <p>
      Super Methane Brothers is a platform arcade game Puff and Blow each have a
      Methane Gas Gun which fires a cloud of immobilising gas.
      If this comes into contact with a bad guy, he will be absorbed into the gas
      and then float around the screen for a limited time.
      Bad guys are harmless in this state.
      Puff and Blow must suck the floating gas clouds into their guns and blast
      them out against a vertical surface.
      bThe Bad guys then turn into bonuses which can be collected.
    </p>
  </description>
  <url type="homepage">http://methane.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://methane.sourceforge.net/gamepic.gif</screenshot>
  </screenshots>
</application>
EOF

%files
%doc authors.txt docs history.txt readme.txt
%license copying.txt
%attr(2755,root,games) %{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%verify(not md5 size mtime) %config(noreplace) %attr(664,root,games) %{_var}/games/%{name}.scores


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.1-36
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Hans de Goede <hdegoede@redhat.com> - 1.5.1-22
- Fix FTBFS (rhbz#1606822)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.1-19
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Hans de Goede <hdegoede@redhat.com> - 1.5.1-14
- Drop the help .desktop file, having 2 menu entries for methane is
  undesirable, and methane was the only app with a separate help .desktop

* Fri Jun 19 2015 Hans de Goede <hdegoede@redhat.com> - 1.5.1-13
- Fix FTBFS
- Fix help .desktop file not working

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.5.1-11
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug  1 2013 Hans de Goede <hdegoede@redhat.com> - 1.5.1-8
- Don't request no-decorations in fullscreen mode, as this breaks fullscreen

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5.1-7
- Remove the --vendor flag for desktop-file-install

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.5.1-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.5.1-4
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Hans de Goede <hdegoede@redhat.com> - 1.5.1-1
- New upstream release 1.5.1
- Improve (make high res) icons

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.5.0-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 16 2009 Hans de Goede <hdegoede@redhat.com> 1.5.0-2
- Hide cursor in fullscreen mode
- Add support for OpenGL 1 (versus 2)
- Disable opengl support by default, even the OpenGL 1 code is having issues
  with foss drivers

* Wed Nov 11 2009 Hans de Goede <hdegoede@redhat.com> 1.5.0-1
- New upstream release 1.5.0
- Hiscore save file format has changed, this means all
  highscores will be reset to 0 when updating from 1.4.7

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Hans de Goede <hdegoede@redhat.com> 1.4.7-7
- Rebuild for new ClanLib

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Hans de Goede <hdegoede@redhat.com> 1.4.7-5
- Update description for new trademark guidelines

* Sun Feb 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.7-4
- Rebuild for new libmikmod
- Rebuild with gcc 4.3
- Try pulseaudio (esd) before oss (mikmod doesn't support alsa)

* Tue Sep 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.7-3
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.7-2
- Update License tag for new Licensing Guidelines compliance

* Thu Jan 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.7-1
- Initial Fedora Extras package, based on the SUSE srpm
