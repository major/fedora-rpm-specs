# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007-2021 Hans de Goede <hdegoede@redhat.com>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to us at the above email addresses

Name:           bolzplatz2006
Version:        1.0.3
Release:        61%{?dist}
Summary:        Slam Soccer 2006 is a funny football game in 3D-comic-style
Summary(fr):    Coup de Foot 2006 est un jeu comique en 3D
Summary(de):    Bolzplatz 2006 ist ein spaßiges Fußballspiel im 3D-Comic-Stil
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.bolzplatz2006.de
Source0:        http://downloads.sourceforge.net/bp2k6/%{name}-%{version}-src.zip
Source1:        %{name}.png
Source2:        %{name}.sh
Source3:        %{name}-settings.sh
Source4:        %{name}.desktop
Source5:        %{name}.appdata.xml
Source6:        %{name}-jirr-no-crash.patch
Source7:        %{name}-functions.sh
Source8:        %{name}.autodlrc
Source9:        input.xml
Patch0:         %{name}-irrlicht.i.patch
Patch1:         %{name}-irrlicht-extra-qualification-error.patch
Patch2:         %{name}-irrlicht-use-systemlibs.patch
Patch3:         %{name}-irrlicht-png-64bit.patch
Patch4:         %{name}-lwjgl-nofmod.patch
Patch5:         %{name}-lwjgl-openal11.patch
Patch6:         %{name}-lwjgl-Makefile.patch
Patch7:         %{name}-no-xrandr.patch
Patch8:         %{name}-versioned-openal.patch
Patch9:         %{name}-1.0.3-libpng15.patch
Patch10:        %{name}-use-system-extgl.patch
Patch11:        %{name}-gcc6.patch
Patch12:        %{name}-openjdk11.patch
BuildRequires:  gcc-c++ make
BuildRequires:  ant sdljava dom4j vecmath1.2 swig xml-commons-apis
BuildRequires:  libGLU-devel DevIL-devel libXxf86vm-devel libjpeg-devel
BuildRequires:  libpng-devel libXext-devel libXrandr-devel libXcursor-devel
BuildRequires:  libXt-devel libXrender-devel libvorbis-devel desktop-file-utils
BuildRequires:  java-devel
BuildRequires:  libappstream-glib
Requires:       sdljava dom4j vecmath1.2 java jpackage-utils
Requires:       hicolor-icon-theme autodownloader
# These are dynamically opened by lwjgl:
Requires:       openal-soft
# Bolzplatz2006 is a mix of java + native code, so it can only run on java_arches
ExclusiveArch:  %{java_arches}

%description
Slam Soccer 2006 is a funny football game in
3D-comic-style - and it's for free!

* Freeware and open source
* Funny 3d-comic-style
* Enthralling stadium atmosphere
* Keyboard and gamepad control
* 2-player mode
* Career and world cup
* Register in the online hall of fame
* Build your own stadium

* 80 teams
* 20 stadiums
* 10 weather conditions
* 50 adboards
* 10 referees
* 9 commentators (5 German, 2 English, 2 French)

* 3 languages: German, English, French

%description -l de
Bolzplatz 2006 ist ein spaßiges Fußballspiel
im 3D-Comic-Stil für lau.

* Kostenlos und Open-Source
* Witzige 3D-Comic-Grafik
* Packende Stadionatmosphäre
* Steuerung mit Tastatur oder Gamepad
* 2-Spieler-Modus
* Karriere und Weltmeisterschaft
* Eintrag in die Hall of Fame
* Baue Dein eigenes Stadion

* 80 Teams
* 20 Stadien
* 10 Wetterverhältnisse
* 50 Werbebanden
* 10 Schiedsrichter
* 9 Kommentatoren (5xDeutsch, 2xEnglisch, 2xFranzösisch)

* 3 Sprachen: Deutsch, Englisch und Französisch

%description -l fr
Coup de Foot 2006 est un jeu comique en 3D.
Gratuit et open-source.

* Graphiques 3D en style cartoon
* Ambiance de stade presqu'originale
* A commander par clavier ou gamepad
* Mode 2 joueurs
* Mode Carrière et Coupe du Monde
* Inscription au Hall of Fame
* Construis tes propres stades

* 80 équipes
* 20 stades
* 10 conditions atmosphériques différentes
* 50 panneaux publicitaires
* 10 arbitres
* 9 commentateurs

* 3 langues: allemand, anglais et français


%prep
%autosetup -c -p1
cp %{SOURCE6} libsrc/jirr-dev/diff.txt
cp %{SOURCE7} .
sed -i 's/\r//' license.txt
# we use the system versions of these
rm -r libsrc/irrlicht-0.14-patched/libpng libsrc/irrlicht-0.14-patched/zlib \
  libsrc/irrlicht-0.14-patched/jpeglib libsrc/irrlicht-0.14-patched/glext.h


%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
export JAVA_HOME=/usr/lib/jvm/java-openjdk

# special case ix86 as all of ix86 should look in the i386 jre lib subdir
%ifarch %{ix86}
export JAVA_ARCH=i386
%endif
# special case x86_64 as it should be mapped to amd64
%ifarch x86_64
export JAVA_ARCH=amd64
%endif
# All other archs
if [ -z "$JAVA_ARCH" ]; then
  export JAVA_ARCH=%{_arch}
fi

echo "export LD_LIBRARY_PATH=/usr/lib/jvm/jre-openjdk/lib/$JAVA_ARCH" >> \
  %{name}-functions.sh

# jbolzplatz ships with copies of several libraries, as these are heavily
# patched we use the bolzplatz versions and not the system ones

# build irrlicht-0.14
pushd libsrc/irrlicht-0.14-patched
make %{?_smp_mflags} CPP="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing" \
  CC="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing"
popd

# build jirr-0.6
pushd libsrc/jirr-dev
make CXX="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing -fpermissive" \
  CC="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing"
popd

# build lwjgl
pushd libsrc/lwjgl
ant jars
ant compile_native
popd

# build bolzplatz itself
mkdir classes
javac -d classes -encoding iso-8859-1 \
  -cp `build-classpath dom4j sdljava vecmath1.2`:./libsrc/jirr-dev/lib/irrlicht.jar:./libsrc/lwjgl/libs/lwjgl.jar \
  `find ./src -name '*.java'`
jar cf %{name}.jar -C classes .


%install
# dirs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

# jars
install -m 644 %{name}.jar libsrc/jirr-dev/lib/irrlicht.jar \
  libsrc/lwjgl/libs/lwjgl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}

# native libraries
install -m 755 libsrc/jirr-dev/libirrlicht_wrap.so \
  libsrc/lwjgl/libs/linux/liblwjgl.so $RPM_BUILD_ROOT%{_libdir}/%{name}

# startscripts
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}-settings

# icon and menu-entry
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

# needed "data" files
install -p -m 644 %{name}-functions.sh %{SOURCE8} %{SOURCE9} \
  $RPM_BUILD_ROOT%{_datadir}/%{name}


%files
%license license.txt
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_javadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3-60
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.0.3-58
- Rebuilt for java-21-openjdk as system jdk

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Hans de Goede <hdegoede@redhat.com> - 1.0.3-52
- Bolzplatz2006 is a mix of java + native code and the JDK is no longer
  build on i686, disable i686 builds (rhbz#2104023)

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.3-51
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec  2 2021 Hans de Goede <hdegoede@redhat.com> - 1.0.3-49
- Fix bolzplatz2006 not starting due to it failing to find its libraries
- Fix building with Java 17

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Hans de Goede <hdegoede@redhat.com> - 1.0.3-46
- Fix FTBFS (rhbz#1863284, rhbz#1859123)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-45
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.3-43
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-37
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Hans de Goede <hdegoede@redhat.com> - 1.0.3-34
- Fix FTBFS on armv7hl (rhbz#1423244)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.3-32
- Fix FTBFS with gcc6 (rhbz#1307359)
- Add higher-res icon
- Add appdata

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.3-29
- Rebuilt for GCC 5 C++11 ABI change

* Fri Oct 24 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.3-28
- Fix building with latest mesa

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0.3-24
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.0.3-22
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.0.3-21
- rebuild against new libjpeg

* Thu Jul 26 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.3-20
- Build all class files in 1.5 format or higher (rhbz#842580)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr  6 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.3-18
- Fix bolzplatz2006 not running due to openjdk-1.7 no longer setting
  LD_LIBRARY_PATH

* Fri Feb 17 2012 Deepak Bhole <dbhole@redhat.com> - 1.0.3-17
- Resolves rhbz#794501
- Patch from Omair Majid <omajid@redhat.com> , removed explicit Java 6 dependency

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Hans de Goede <hdegoede@redhat.com> - 1.0.3-15
- Fix building with new libpng

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.3-14
- Rebuild for new libpng

* Mon Feb 14 2011 Hans de Goede <hdegoede@redhat.com> - 1.0.3-13
- Fix building with gcc-4.6

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Adam Jackson <ajax@redhat.com> 1.0.3-11
- Remove explicit Requires: libGL, rpm finds the DSO dep for us.

* Wed Nov  4 2009 Hans de Goede <hdegoede@redhat.com> 1.0.3-10
- Fix building and running with latest vecmath1.2 package
  (hurray for coordination of changes)

* Wed Nov  4 2009 Hans de Goede <hdegoede@redhat.com> 1.0.3-9
- Fix hang on exit (by using XF86Vidmode instead of Xrandr)
- Do not crash when openal-soft-devel is not installed
  (dlopen versioned lib instead of .so devel symlink)
- Require openal-soft, as it is dlopened

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.3-6
- Fix missing prototype compiler warnings

* Fri Mar 14 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.3-5
- Adapt launch script and (Build)Requires for icedtea -> openjdk rename
- Drop ExclusiveArch now that openjdk also is available for ppc

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.3-4
- Autorebuild for GCC 4.3

* Thu Nov 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.3-3
- Add missing BuildRequires: libXxf86vm-devel, libGLU-devel, libjpeg-devel,
  libpng-devel, libXext-devel, libXrandr-devel, libXcursor-devel, libXt-devel
  libXrender-devel, libvorbis-devel, desktop-file-utils

* Mon Sep 17 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.3-2
- Switch to using autodownloader for the datafiles, upstream wanted to change
  the license of the datafiles to be free, but not all contributers have
  agreed to the license change :(

* Sat Sep  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.3-1
- Adapted Packman spec file for Fedora

* Mon Jun 18 2007 Toni Graffy <toni@links2linux.de> - 1.0.3-0.pm.1
- initial release 1.0.3
- repacked as tar.bz2
- added docs from binary-tarball
