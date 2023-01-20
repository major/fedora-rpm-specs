%global debug_package %{nil}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           blobwars
Version:        2.00
Release:        10%{?dist}
Summary:        Mission and Objective based 2D Platform Game
# Code and gfx is all GPLv2+. Music is all CC-BY-SA. SFX are a mix, see readme
License:        GPLv2+ and CC-BY-SA and CC-BY and BSD and Public Domain
URL:            http://www.parallelrealities.co.uk/p/blob-wars-metal-blob-solid.html
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         blobwars-2.00-Werror.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  zlib-devel
BuildRequires: make
Requires:       bitstream-vera-sans-fonts
Requires:       hicolor-icon-theme

%description
Blob Wars : Metal Blob Solid. This is Episode I of the Blob Wars Saga.
You must undertake the role of fearless Blob solider, Bob, as he infiltrates
various enemy installations and hideouts in an attempt to rescue as many
MIAs as possible.

%prep
%autosetup

# fix permissions
chmod 0644 Makefile*

# SED-FIX-OPENSUSE -- Fix paths and libraries
sed -i -e 's|USEPAK ?= 0|USEPAK ?= 1|;
           s|$(PREFIX)/games|$(PREFIX)/bin|;
           s|$(PREFIX)/share/games|$(PREFIX)/share|;
           s| -Werror||;
           s|$(CXX) $(LIBS) $(GAMEOBJS) -o $(PROG)|$(CXX) $(GAMEOBJS) $(LIBS) -o $(PROG)|;
           s|$(CXX) $(LIBS) $(PAKOBJS) -o pak|$(CXX) $(PAKOBJS) $(LIBS) -o pak|;
           s|$(CXX) $(LIBS) $(MAPOBJS) -o mapeditor|$(CXX) $(MAPOBJS) $(LIBS) -o mapeditor|' Makefile

# SED-FIX-OPENSUSE -- Fix pak
sed -i -e 's|gzclose(pak)|gzclose((gzFile)pak)|;
           s|gzclose(fp)|gzclose((gzFile)fp)|' src/pak.cpp

%build
%make_build RELEASE=1 DOCDIR=%{_pkgdocdir}/

%install
%make_install DOCDIR=%{_pkgdocdir}/
%find_lang %{name}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: hdegoede@redhat.com
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">blobwars.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Mission and Objective based 2D Platform Game</summary>
  <description>
    <p>
      Blob Wars: Metal Blob Solid is a 2D side scrolling platformer where you control
      Bob, (a blob secret agent) through 25 missions to rescue other blobs and stop
      the evil alien leader: Galdov.
    </p>
  </description>
  <url type="homepage">http://www.parallelrealities.co.uk/p/blob-wars-metal-blob-solid.html</url>
  <screenshots>
    <screenshot type="default">http://3.bp.blogspot.com/-VGOFb5wKQkE/T4RuJznkWkI/AAAAAAAAA10/u1pyXxBa1yw/s1600/03.jpg</screenshot>
    <screenshot>http://3.bp.blogspot.com/-oBB_IbOXWEI/T4RuI6G3Y5I/AAAAAAAAA1s/_Tb2v1YrINk/s1600/02.jpg</screenshot>
    <screenshot>http://3.bp.blogspot.com/-s0v-Lr5WBa0/T4RuH7DbgKI/AAAAAAAAA1k/58HXOP40NIk/s1600/01.jpg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files -f %{name}.lang
%{_pkgdocdir}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.00-1
- Update to 2.00 fixes rhbz#1284212
- Rewrite spec file (cleanup and modernization)

* Fri Jul 05 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.19-21
- Rebuilt do fix FTBFS rhbz#1423279 rhbz#1603496 and rhbz#1674703

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.19-17
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.19-11
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.19-10
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.19-7
- Install docs to %%{_pkgdocdir} where available (#993685).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.19-5
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Hans de Goede <hdegoede@redhat.com> - 1.19-1
- New upstream version 1.19

* Sun Feb 13 2011 Hans de Goede <hdegoede@redhat.com> - 1.18-1
- New upstream version 1.18
  - From new sf.net upstream by the Debian and Fedora blobwars packagers
  - With new Free music
  - Sound effects are back! (and Free this time)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 07 2009 Rafał Psota <rafalzaq@gmail.com> 1.11-1
- update to 1.11 (bz 488584)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09b2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Rafał Psota <rafalzaq@gmail.com> 1.09b2-2
- FONT_ERROR patch (thanks to Michał Bentkowski)

* Fri Aug 29 2008 Rafał Psota <rafalzaq@gmail.com> 1.09b2-1
- remove nonfree sounds and music

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.07-2
- Autorebuild for GCC 4.3

* Sun Sep 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.07-1
- New upstream version 1.07 (bz 292391)

* Sun Aug  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.06-2
- Update License tag for new Licensing Guidelines compliance

* Tue Apr 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.06-1
- New upstream release 1.06-2

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.05-3
- FE6 Rebuild

* Thu Jun  1 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.05-2
- remove extreanous BR SDL-devel and ImageMagick
- remove extreanous "export" in %%build section
- remove extreanous "-n %%{name}-%%{version}" under %%setup
- cleanup .desktop file

* Sun May 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.05-1
- initial Fedora Extras package
