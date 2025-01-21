# vavoom's CMakefiles are a mess, force in-source building
%global _vpath_builddir .

Name:           vavoom
Version:        1.33
Release:        46%{?dist}
Summary:        Enhanced Doom, Heretic, Hexen and Strife source port - meta package
Source0:        http://downloads.sourceforge.net/vavoom/%{name}-%{version}.tar.bz2
Source1:        doom.autodlrc
Source2:        heretic.autodlrc
Source3:        hexen.autodlrc
Source4:        strife.autodlrc
Source5:        doom-shareware.sh
Source6:        heretic-shareware.sh
Source7:        hexen-demo.sh
Source8:        strife-demo.sh
Source9:        doom-shareware.desktop
Source10:       heretic-shareware.desktop
Source11:       hexen-demo.desktop
Source12:       strife-demo.desktop
Source13:       vavoom.desktop
Source14:       doom-shareware.appdata.xml
Source15:       heretic-shareware.appdata.xml
Source16:       hexen-demo.appdata.xml
Source17:       strife-demo.appdata.xml
Source18:       vavoom.appdata.xml
Source19:       vavoom.png
Source20:       doom-logo.png
Source21:       tux-b2f.png
Source22:       vavoom.6
Patch0:         vavoom-1.21-datadir.patch
Patch1:         vavoom-1.27-CMakeLists.patch
Patch2:         vavoom-1.33-format-security.patch
Patch3:         vavoom-1.33-dont-override-delete.patch
Patch4:         vavoom-1.33-default-iwaddir.patch
Patch5:         vavoom-1.33-gcc6.patch
Patch6:         vavoom-1.33-misc-fixes.patch
# Incomplete patch to build with -std=c++11 not used as this crashes on exit
Patch7:         vavoom-1.33-cx11.patch
# Hack for crash on exit when building with -std=c++11, not used
Patch8:         vavoom-1.33-crash-on-exit.patch
Patch9:         vavoom-1.33-wxwidgets3.0.patch
URL:            http://vavoom-engine.com/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel SDL_net-devel libpng-devel libjpeg-devel
BuildRequires:  libvorbis-devel mikmod-devel flac-devel openal-soft-devel
BuildRequires:  libGLU-devel wxGTK-devel desktop-file-utils cmake
BuildRequires:  libappstream-glib
Requires:       %{name}-engine = %{version}-%{release}
Requires:       %{name}-doom-shareware = %{version}-%{release}
Requires:       %{name}-heretic-shareware = %{version}-%{release}
Requires:       %{name}-hexen-demo = %{version}-%{release}
Requires:       %{name}-strife-demo = %{version}-%{release}

%description
Vavoom is an enhanced open-source port of Doom. The "vavoom" meta-package
installs vavoom-engine, and launchers / menu-entries to download and play
doom-shareware, heretic-shareware, hexen-demo and strife-demo.


%package engine
Summary:        Enhanced Doom, Heretic, Hexen and Strife game engine
Requires:       timidity++-patches hicolor-icon-theme

%description engine
Vavoom is an enhanced open-source port of Doom. Allowing you to play not only
the classic 3D first-person shooter Doom, but also the Doom derived classics
Heretic, Hexen and Strife. Compared to the original games it adds extra
features such as translucency and freelook support and ofcourse the capability
to play these classics under Linux.


%package doom-shareware
Summary:        Doom shareware installer
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release}
Requires:       autodownloader unzip

%description doom-shareware
Doom is id Software's classic first person shooter follow-up to
Wolfenstein 3D. The Doom engine is Open Source. The original Doom datafiles
however are not Open Source. There is a gratis, but not Open Source shareware
version available on the internet.

This package contains an applications menu entry for playing Doom shareware
using the vavoom engine.  The first time you click this menu entry, it will
offer to download and install the Doom shareware datafiles for you.


%package heretic-shareware
Summary:        Heretic shareware installer
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release}
Requires:       autodownloader unzip

%description heretic-shareware
Heretic is Raven's classic dark fantasy first person shooter using a
modified Doom engine. The Heretic engine is Open Source. The original
Heretic datafiles however are not Open Source. There is a gratis, but not
Open Source shareware version available on the internet.

This package contains an applications menu entry for playing Heretic
shareware using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Heretic shareware
datafiles for you.


%package hexen-demo
Summary:        Hexen demo installer
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release}
Requires:       autodownloader unzip

%description hexen-demo
Hexen: Beyond Heretic is Raven's classic dark fantasy first person shooter
follow-up to Heretic. The Hexen engine is Open Source. The original Hexen
datafiles however are not Open Source. There is a gratis, but not Open
Source demo version available on the internet.

This package contains an applications menu entry for playing Hexen
demo using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Hexen demo
datafiles for you.


%package strife-demo
Summary:        Strife demo installer
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release}
Requires:       autodownloader unzip

%description strife-demo
Strife is Rogue Entertainment's classic first person shooter with
role-playing game elements. The Strife engine is Open Source. The original
Strife datafiles however are not Open Source. There is a gratis, but not
Open Source demo version available on the internet.

This package contains an applications menu entry for playing Strife
demo using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Strife demo
datafiles for you.


%prep 
%setup -q
%patch -P0 -p1 -b .datadir
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P9 -p1


%build
# Build with -std=gnu++98, c++11 causes issues on exit, likely due to
# bad interactions with the new / delete overloading in vc_object.cpp
export CXXFLAGS="$RPM_OPT_FLAGS -std=gnu++98 -fno-strict-aliasing -Wno-unused -Wno-unused-but-set-variable -Wno-unused-result -Wno-sign-compare -Wno-reorder"
%cmake -DWITH_LIBMAD:BOOL=OFF

# This one line sed command is easier than trying to muck with the Makefile
# to add the proper -D definition.
sed -i "s|#define FL_BASEDIR.*|#define FL_BASEDIR \"%{_datadir}/%{name}\"|" source/files.h
sed -i "s|#define CONFIG_FILE.*|#define CONFIG_FILE \"%{_sysconfdir}/timidity.cfg\"|" source/timidity/timidity.h

# source/CMakeLists.txt lacks dependencies to generate svnrev.h, force it
make -C source revision_check
make linespec
# no -j# because there are more dependency issues in source/CMakeLists.txt
make VERBOSE=1

%install
make install \
        DESTDIR=$RPM_BUILD_ROOT \
        INSTALL_PARMS="-m 0755" \
        INSTALL_EXEPARMS="-m 0755" \
        INSTALL_DIRPARMS="-m 0755 -d"

mv $RPM_BUILD_ROOT%{_bindir}/%{name}.* $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_bindir}/%{name}-dedicated.* $RPM_BUILD_ROOT%{_bindir}/%{name}-dedicated

# rm obsolete icon
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.png

# install autodl files and wrapper scripts
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/%{name}

install -p -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/doom-shareware
install -p -m 755 %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/heretic-shareware
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/hexen-demo
install -p -m 755 %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/strife-demo

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
for i in %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13}; do
  desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications "$i"
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
for i in %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18}; do
  install -p -m 644 "$i" $RPM_BUILD_ROOT%{_datadir}/appdata
  appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_datadir}/appdata/$(basename "$i")
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{48x48,96x96}/apps
install -p -m 644 %{SOURCE19} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/96x96/apps/
install -p -m 644 %{SOURCE20} %{SOURCE21} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{_mandir}/man6

%files
# no files, meta-package

%files engine
%doc docs/*.log docs/vavoom.txt
%license docs/gnu.txt
%{_bindir}/*
%{_mandir}/man6/%{name}.6*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/basev
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%files doom-shareware
%{_datadir}/%{name}/doom.autodlrc
%{_datadir}/appdata/doom-shareware.appdata.xml
%{_datadir}/applications/doom-shareware.desktop

%files heretic-shareware
%{_datadir}/%{name}/heretic.autodlrc
%{_datadir}/appdata/heretic-shareware.appdata.xml
%{_datadir}/applications/heretic-shareware.desktop

%files hexen-demo
%{_datadir}/%{name}/hexen.autodlrc
%{_datadir}/appdata/hexen-demo.appdata.xml
%{_datadir}/applications/hexen-demo.desktop

%files strife-demo
%{_datadir}/%{name}/strife.autodlrc
%{_datadir}/appdata/strife-demo.appdata.xml
%{_datadir}/applications/strife-demo.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.33-45
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.33-40
- Rebuilt for flac 1.4.0

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 1.33-39
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Hans de Goede <hdegoede@redhat.com> - 1.33-34
- Fix FTBFS (rhbz#1865603)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-33
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 1.33-30
- Make linespec explicitly to ensure it's built early enough
  as the generated Makefiles are missing dependencies

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Scott Talbert <swt@techie.net> - 1.33-27
- Rebuild with wxWidgets 3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.33-24
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Hans de Goede <hdegoede@redhat.com> - 1.33-21
- Fix FTBFS

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug  9 2016 Hans de Goede <hdegoede@redhat.com> - 1.33-19
- Fix a bunch of compiler warnings (and silence some others)
- Fix crash on exit:
  https://retrace.fedoraproject.org/faf/reports/1192370/

* Mon Feb 22 2016 Hans de Goede <hdegoede@redhat.com> - 1.33-18
- Fix FTBFS (rhbz#1308217)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Hans de Goede <hdegoede@redhat.com> - 1.33-16
- Split out the .desktop files, wrapper scripts and autodownloader files for:
  doom-shareware, heretic-shareware, hexen-demo and strife-demo into
  seperate sub-packages
- Add one .appdata.xml file per .desktop file

* Tue Jan  5 2016 Hans de Goede <hdegoede@redhat.com> - 1.33-15
- Make vavoom work better with iwads installed in system dirs
- Drop freedoom support again, this uses a builtin mapinfo.txt which is
  already out of date with the latest freedoom version; advice: use prboom
  to play freedoom instead
- Update mirror lists

* Mon Jan  4 2016 Hans de Goede <hdegoede@redhat.com> - 1.33-14
- Fix crash in mesa / i965_dri.so caused by globally overriding delete
- Add a manpage and support for freedoom (from Debian)
- Add appdata

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.33-12
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Hans de Goede <hdegoede@redhat.com> - 1.33-10
- Fix FTBFS (rhbz#1037375)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.33-7
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.33-6
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.33-5
- rebuild against new libjpeg

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.33-2
- Rebuild for new libpng

* Sat Aug 20 2011 Rahul Sundaram <sundaram@fedoraproject.org> 1.33-1
- New upstream release
- Drop definition of buildroot, defattr and clean stage
- Drop obsolete patches
- Remove no longer valid doom shareware mirror in doom.autodlrc
- Fixed sed line to apply to timidity.h instead of config.h which no longer exists

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.30-5
- rebuilt against wxGTK-2.8.11-2

* Fri Nov 20 2009 Hans de Goede <hdegoede@redhat.com> 1.30-4
- Fix building with cmake-2.8.x (#539127)

* Sun Aug 16 2009 Hans de Goede <hdegoede@redhat.com> 1.30-3
- Switch to openal-soft

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 20 2009 Hans de Goede <hdegoede@redhat.com> 1.30-1
- New upstream release 1.30
- Fix vavoom not working at all when compiled with gcc-4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Hans de Goede <hdegoede@redhat.com> 1.29-1
- New upstream release 1.29

* Mon Jun 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.28-1
- New upstream release 1.28

* Sun Apr 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.27.1-1
- New upstream bugfix release 1.27.1

* Wed Apr  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.27-1
- New upstream release 1.27

* Mon Mar  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.26-3
- Change Requires: timidity++ to timidity++-patches, as we just need the
  patches

* Sun Feb 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.26-2
- Rebuild for new libmikmod
- Rebuild with gcc 4.3

* Tue Jan 22 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.26-1
- New upstream release 1.26

* Tue Oct  9 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.25-1
- New upstream release 1.25

* Sat Sep 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.24-4
- Don't build with libmad support even if libmad happens to be on the system

* Fri Aug 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.24-3
- Fix some security issues in the server: CVE-2007-4533, CVE-2007-4534,
  CVE-2007-4535 (bz 256621)

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.24-2
- Update License tag for new Licensing Guidelines compliance

* Thu Jun 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.24-1
- New upstream release 1.24
- This also fixes bug 241611

* Sat May 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.23-2
- Add missing libjpeg-devel BuildRequires

* Wed May 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.23-1
- Update to 1.23
- No longer require freedoom, it doesn't seem to work with vavoom
- No longer require vavoom-vmdl, it has license issues
- Add --enable-debug to ./configure flags so that the bins don't get stripped
- Add .desktop files, wrapper scripts and autodownloader files for:
  doom-shareware, heretic-shareware, hexen-demo and strife-demo
- Submit for FE inclusion

* Sun Jul 23 2006 Wart <wart at kobold dot org> 1.21.1-1
- Update to 1.21.1

* Sun Jul 16 2006 Wart <wart at kobold dot org> 1.21-2
- Remove some comments from the spec file
- Remove shell script wrappers from /usr/bin
- Update datadir patch to 1.21

* Sat Jul 15 2006 Wart <wart at kobold dot org> 1.21-1
- Update to 1.21

* Fri Jun 16 2006 Wart <wart at kobold dot org> 1.20-2
- Added various fixes to conform to FHS.
- Added upstream patch to prevent cross-filesystem links when building
  glvis files.

* Sat Jun 3 2006 Wart <wart at kobold dot org> 1.20-1
- Initial Fedora Extras package
