%define pkgverdir %(echo %version|sed s/\\\\\./_/)

Name:           openmsx
Version:        20.0
Release:        3%{?dist}
Summary:        An emulator for the MSX home computer system
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://openmsx.org/
Source0:        https://github.com/openMSX/openMSX/releases/download/RELEASE_%{pkgverdir}/%{name}-%{version}.tar.gz
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  docbook-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel >= 2.1.0
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_ttf-devel
# OpenMSX does not build with Tcl 9.0
BuildRequires:  tcl-devel < 1:9
BuildRequires:  zlib-devel
Requires:       cbios-%{name}
Requires:       hicolor-icon-theme

# Catapult is no longer maintained
Obsoletes:      %{name}-catapult <= 19.1

%description
openMSX is an emulator for the MSX home computer system. Its goal is to emulate
all aspects of the MSX with high accuracy. In addition to emulating MSX, MSX2,
MSX2+, MSX Turbo R and many of it's peripherals, it also support emulating the
ColecoVision game console and the SpectraVideo SVI-318 and SVI-328 home
computer systems.


%prep
%autosetup


%build
# Make the custom flavour module, so we can use RPM OPT FLAGS here
cat > build/flavour-rpm.mk << EOF
# Opt flags.
CXXFLAGS+=%{optflags} -DNDEBUG
LINK_FLAGS+=%{__global_ldflags}

# Dont strip exe, let rpm do it and save debug info
OPENMSX_STRIP:=false
EOF

cat > build/custom.mk << EOF
PYTHON:=python3
INSTALL_BASE:=%{_prefix}
VERSION_EXEC:=false
SYMLINK_FOR_BINARY:=false
INSTALL_CONTRIB:=false
INSTALL_SHARE_DIR=%{_datadir}/%{name}
INSTALL_DOC_DIR=%{_docdir}/%{name}
EOF

%configure
%make_build OPENMSX_FLAVOUR=rpm

# Build desktop icon
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=openMSX
GenericName=MSX Emulator
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
Keywords=emulator;msx;openmsx;
EOF

# Build the man page
docbook2man doc/openmsx.sgml -o ./


%install
%make_install OPENMSX_FLAVOUR=rpm V=1

rm $RPM_BUILD_ROOT%{_docdir}/%{name}/GPL.txt

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/machines/*.txt \
   $RPM_BUILD_ROOT%{_docdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/settings.xml \
   $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
ln -s --target-directory=$RPM_BUILD_ROOT%{_datadir}/%{name} \
   ../../../etc/openmsx/settings.xml

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 0644 OPENMSX.1 $RPM_BUILD_ROOT%{_mandir}/man1/openmsx.1

# Install icon set and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64,128x128}/apps
for i in 16 32 48 64 128; do
install -pm 0644 share/icons/openMSX-logo-"$i".png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/"$i"x"$i"/apps/%{name}.png
done

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
                     %{name}.desktop

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
BugReportURL: BUGTRACKER DEAD
SentUpstream: 2014-09-25
-->
<component type="desktop">
  <id>openmsx.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-2.0</project_license>
  <name>openMSX</name>
  <summary>Emulate all aspects of the MSX with high accuracy</summary>
  <description>
    <p>
      OpenMSX is an emulator for the MSX home computer system. MSX is an old
      Z80-based family of home computers as an attempt to establish
      a single standard in home computing similar to VHS in video.
    </p>
    <p>
      The MSX standard has been designed by a company called ASCII in Cooperation
      with Microsoft which has provided a firmware version of its extended BASIC
      (called "MicroSoft eXtended BASIC") for the machine, which explains the
      MSX name.
    </p>
    <p>
     In addition to emulating MSX, MSX2, MSX2+, MSX Turbo R and many of it's
     peripherals, openMSX also support emulating the ColecoVision game console
     and the SpectraVideo SVI-318 and SVI-328 home computer systems.
    </p>
  </description>
  <url type="homepage">http://openmsx.org/</url>
  <url type="help">http://openmsx.org/manual/user.html</url>
  <screenshots>
    <screenshot type="default">http://openmsx.org/images/screenshots/mlimit3.png</screenshot>
    <screenshot>http://openmsx.org/images/screenshots/ide.png</screenshot>
    <screenshot>http://openmsx.org/images/screenshots/tb-underwater.png</screenshot>
  </screenshots>
  <updatecontact>jwrdegoede_at_fedoraproject.org</updatecontact>
</component>
EOF
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc %{_docdir}/%{name}
%license doc/GPL.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/settings.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sat Feb 01 2025 Andrea Musuruane <musuruan@gmail.com> - 20.0-3
- OpenMSX does not build with Tcl 9.0 (BZ #2337744)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Andrea Musuruane <musuruan@gmail.com> - 20.0-1
- New upstream version 20.0

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 19.1-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 02 2023 Andrea Musuruane <musuruan@gmail.com> - 19.1-1
- New upstream version 19.1

* Thu Jul 27 2023 Andrea Musuruane <musuruan@gmail.com> - 19.0-1
- New upstream version 19.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 04 2023 Andrea Musuruane <musuruan@gmail.com> - 18.0-3
- Fix compiling with GCC 13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 06 2022 Andrea Musuruane <musuruan@gmail.com> - 18.0-1
- New upstream version 18.0 (rhbz#2096090)

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 17.0-3
- Rebuild with wxWidgets 3.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Robert de Rooy <robert.de.rooy@gmail.com> - 17.0-1
- New upstream version 17.0

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 16.0-5
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Robert de Rooy <robert.de.rooy@gmail.com> - 16.0-1
- New upstream version 16.0 (rhbz#1886301)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Hans de Goede <hdegoede@redhat.com> - 0.15.0-5
- Add upstream "build" dir changes to build with python3
- Change BuildRequires to python3 (rhbz#1807947)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Hans de Goede <hdegoede@redhat.com> - 0.15.0-2
- Extend spec-file and appdata description to mention that openMSX now also
  supports emulating the ColecoVision and SpectraVideo SVI-3x8 systems

* Tue Feb 19 2019 Hans de Goede <hdegoede@redhat.com> - 0.15.0-1
- New upstream version 0.15.0 (rhbz#1657547)
- Fix FTBFS (rhbz#1675581)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Scott Talbert <swt@techie.net> - 0.14.0-9
- Rebuild with wxWidgets 3.0

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.14.0-8
- Rebuilt for glew 2.1.0

* Thu Aug  2 2018 Hans de Goede <hdegoede@redhat.com> - 0.14.0-7
- Fix FTBFS (rhbz#1605324)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.14.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.14.0-4
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.0-2
- Remove obsolete scriptlets

* Thu Aug 31 2017 Hans de Goede <hdegoede@redhat.com> - 0.14.0-1
- New upstream release 0.14.0 (rhbz#1478320)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.13.0-2
- Rebuild for glew 2.0.0

* Thu Aug 11 2016 Hans de Goede <hdegoede@redhat.com> - 0.13.0-1
- New upstream release 0.13.0 (rhbz#1353901)
- Include catapult graphical frontend (in a new -catapult subpackage)
- Move .desktop file to the -catapult subpackage and make it launch Catapult

* Sun Feb 21 2016 Hans de Goede <hdegoede@redhat.com> - 0.12.0-1
- New upstream release 0.12.0 (rhbz#1306725)
- Fix FTBFS (rhbz#1307827)
- Improve appdata a bit

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Adam Jackson <ajax@redhat.com> 0.11.0-6
- Add explicit python2 BuildRequires

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.11.0-5
- Rebuild for glew 1.13

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.11.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.11.0-2
- Add an AppData file for the software center

* Fri Nov 21 2014 Hans de Goede <hdegoede@redhat.com> - 0.11.0-1
- New upstream release 0.11.0 (rhbz#1163192)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Fri May 02 2014 Hans de Goede <hdegoede@redhat.com> - 0.10.1-1
- New upstream release 0.10.1 (rhbz#1093671)

* Sat Mar 08 2014 Hans de Goede <hdegoede@redhat.com> - 0.10.0-1
- New upstream release 0.10.0 (rhbz#1048800)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.9.1-2
- rebuilt for GLEW 1.10

* Fri Aug 09 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.1-1
- New upstream release 0.9.1 (rhbz#861857)
- Use unversioned docdir (rhbz#993995)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.0-4
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.9.0-2
- Rebuild for glew 1.9.0

* Sat Aug 18 2012 Hans de Goede <hdegoede@redhat.com> - 0.9.0-1
- New upstream release 0.9.0 (rhbz#847653)

* Sat Jul 28 2012 Hans de Goede <hdegoede@redhat.com> - 0.8.2-4
- Fix FTBFS

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for c++ ABI breakage

* Fri Jan 27 2012 Hans de Goede <hdegoede@redhat.com> - 0.8.2-1
- New upstream release 0.8.2 (rhbz#784831)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.1-1
- New upstream release 0.8.1
- Fix building with libpng-1.5

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.2-5
- Rebuild for new libpng

* Mon Jun 20 2011 ajax@redhat.com - 0.7.2-4
- Rebuild for new glew soname

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul  3 2009 Hans de Goede <hdegoede@redhat.com> 0.7.2-1
- New upstream release 0.7.2

* Fri Apr 10 2009 Hans de Goede <hdegoede@redhat.com> 0.7.0-1
- New upstream release 0.7.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Hans de Goede <hdegoede@redhat.com> 0.6.3-6
- Fix building with gcc-4.4

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.3-5
- Rebuild for Python 2.6

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 0.6.3-4
- Fix patch fuzz build failure

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.3-3
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.3-2
- Rebuild for new glew version in devel

* Wed Jan 09 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.3-1
- Upgrade to 0.6.3
- Use the icons now supplied with openmsx instead of our own
- Harmless permission fix
- Some spec optimisations
- Updated datadir patch

* Sat Jan  5 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.6.2-5
- Rebuild for new Tcl 8.5

* Mon Aug 27 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.2-4
- License field corrected

* Sun Aug 26 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.2-3
- Migration to Fedora
- License field changed due to new guidelines

* Sun May 06 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.2-2
- Rebuild for glew 1.4.0

* Fri Apr 27 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.2-1
- Upgrade to 0.6.2
- Increased compilation verbosity

* Sun Mar 11 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.1-2
- Dropped dribble-menus requirement, due to be obsoleted
- Changed .desktop category to Game;Emulator;
- Create the desktop icon from the skins (instead of using our own)

* Sun Aug 06 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.1-1
- Initial release
