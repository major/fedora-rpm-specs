%if 0%{?el10}
%global         _without_lirc  1
%endif

#global         snapshot    1
#global         date        20190824
#global         commit      894d90

Name:           xine-ui
Version:        0.99.14
Release:        10%{?snapshot:.%{date}hg%{commit}}%{?dist}
Summary:        A skinned xlib-based gui for xine-lib
License:        GPL-2.0-or-later
URL:            http://www.xine-project.org/
%if ! 0%{?snapshot}
Source0:        http://sourceforge.net/projects/xine/files/xine-ui/%{version}/xine-ui-%{version}.tar.xz
%else
Source0:        xine-ui-%{version}hg.tar.xz
%endif

# Sources for -skins.
Source1:        https://xine.sourceforge.net/skins/Antares.tar.gz
Source2:        https://xine.sourceforge.net/skins/Bambino-Black.tar.gz
Source3:        https://xine.sourceforge.net/skins/Bambino-Blue.tar.gz
Source4:        https://xine.sourceforge.net/skins/Bambino-Green.tar.gz
Source5:        https://xine.sourceforge.net/skins/Bambino-Orange.tar.gz
Source6:        https://xine.sourceforge.net/skins/Bambino-Pink.tar.gz
Source7:        https://xine.sourceforge.net/skins/Bambino-Purple.tar.gz
Source8:        https://xine.sourceforge.net/skins/Bambino-White.tar.gz
Source9:        https://xine.sourceforge.net/skins/blackslim2.tar.gz
Source10:       https://xine.sourceforge.net/skins/Bluton.tar.gz
Source11:       https://xine.sourceforge.net/skins/caramel.tar.gz
Source12:       https://xine.sourceforge.net/skins/CelomaChrome.tar.gz
Source13:       https://xine.sourceforge.net/skins/CelomaGold.tar.gz
Source14:       https://xine.sourceforge.net/skins/CelomaMdk.tar.gz
Source15:       https://xine.sourceforge.net/skins/Centori.tar.gz
Source16:       https://xine.sourceforge.net/skins/cloudy.tar.gz
Source17:       https://xine.sourceforge.net/skins/concept.tar.gz
Source18:       https://xine.sourceforge.net/skins/Crystal.tar.gz
Source19:       https://xine.sourceforge.net/skins/Galaxy.tar.gz
Source20:       https://xine.sourceforge.net/skins/gudgreen.tar.gz
Source21:       https://xine.sourceforge.net/skins/KeramicRH8.tar.gz
Source22:       https://xine.sourceforge.net/skins/Keramic.tar.gz
Source23:       https://xine.sourceforge.net/skins/lcd.tar.gz
Source24:       https://xine.sourceforge.net/skins/mp2k.tar.gz
Source25:       https://xine.sourceforge.net/skins/mplayer.tar.gz
Source26:       https://xine.sourceforge.net/skins/OMS_legacy.tar.gz
Source27:       https://xine.sourceforge.net/skins/pitt.tar.gz
Source28:       https://xine.sourceforge.net/skins/Polaris.tar.gz
Source29:       https://xine.sourceforge.net/skins/Sunset.tar.gz
Source30:       https://xine.sourceforge.net/skins/xinium.tar.gz
Source31:       default.ogv

# AppStream data
Source90:       xine.appdata.xml

# Script to make a xine-ui snapshot
Source100:      make_xineui_snapshot.sh

# Patch to use UTF-8 documentation, BZ #512598
Patch1:         xine-ui-0.99.13-utf8doc.patch

Patch2:         xine-ui-configure-c99.patch

BuildRequires:  aalib-devel >= 1.2.0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel >= 7.10.2
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libcaca-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel >= 1.5
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXv-devel
BuildRequires:  libXxf86vm-devel
%{!?_without_lirc:BuildRequires:  lirc-devel}
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  xine-lib-devel >= 1.1.0
BuildRequires:  xorg-x11-proto-devel

# For dir ownership
Requires:       hicolor-icon-theme
#
Requires:       xine-lib-extras


%description
xine-ui is the traditional, skinned GUI for xine-lib. 


%package skins
Summary:        Extra skins for xine-ui
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description skins
This package contains extra skins for xine-ui.


%package aaxine
Summary:        ASCII art player for terminals
Requires:       %{name} = %{version}-%{release}
Requires:       xine-lib-extras

%description aaxine
This package contains the ASCII art player for terminals like the vt100.
It also contains the color ascii art and framebuffer versions.


%prep
# Setup xine
%setup -q -n %{name}-%{version}%{?snapshot:hg}
# Setup skins
%setup -T -q -c -n %{name}-%{version}%{?snapshot:hg}/fedoraskins -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30
# Restore directory
%setup -T -D -n %{name}-%{version}%{?snapshot:hg}

%patch -P1 -p1
%patch -P2 -p1

# By default aaxine dlopen()'s a nonversioned libX11.so, however in Fedora
# it's provided by libX11-devel => version the dlopen()
libx11so=$(ls -1 %{_libdir}/libX11.so.? | tail -n 1)
if [ -n "$libx11so" -a -f "$libx11so" ] ; then
    sed -i -e "s/\"libX11\\.so\"/\"$(basename $libx11so)\"/" src/aaui/main.c
fi

# Fix file encoding
for f in doc/man/{de,es,fr}/*.1* ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 && \
    touch -r $f $f.utf8 && \
    mv $f.utf8 $f
done
for f in doc/man/pl/*.1* src/xitk/xine-toolkit/README ; do
    iconv -f iso-8859-2 -t utf-8 $f > $f.utf8 && \
    touch -r $f $f.utf8 && \
     mv $f.utf8 $f
done

cp -a src/xitk/xine-toolkit/README doc/README.xitk

# Clean out skins
find fedoraskins/ -type d -name "CVS" -exec rm -rf {} \; || :
find fedoraskins/ -type d -name ".xvpics" -exec rm -rf {} \; || :


%build
./autogen.sh noconfig
%if 0%{!?_without_lirc}
export LIRC_CFLAGS="-llirc_client"
export LIRC_LIBS="-llirc_client"
%endif
export XINE_DOCPATH=%{_docdir}/%{name}-%{version}
%configure --disable-dependency-tracking \
           --enable-vdr-keys \
           --with-aalib
%make_build


%install
%make_install
%find_lang 'xi\(ne-ui\|tk\)'

desktop-file-install --remove-category="Application" --vendor="" \
    --add-category="Audio" --add-category="Video" \
    --dir %{buildroot}%{_datadir}/applications misc/desktops/xine.desktop

install -D -m0644 %{SOURCE90} %{buildroot}%{_metainfodir}/xine.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/xine.appdata.xml

# Remove automatically installed documentation (listed in %%doc)
rm -rf %{buildroot}%{_docdir}/

# Remove misdesigned xine-check
rm -f %{buildroot}%{_bindir}/xine-bugreport
rm -f %{buildroot}%{_mandir}/*/man1/xine-bugreport.*
rm -f %{buildroot}%{_mandir}/man1/xine-bugreport.*
rm -f %{buildroot}%{_bindir}/xine-check
rm -f %{buildroot}%{_mandir}/*/man1/xine-check.*
rm -f %{buildroot}%{_mandir}/man1/xine-check.*

# Install extra skins
cp -a fedoraskins/* %{buildroot}%{_datadir}/xine/skins/


%files -f 'xi\(ne-ui\|tk\)'.lang
%license COPYING
%doc ChangeLog doc/README*
%{_bindir}/xine
%{_bindir}/xine-remote
%dir %{_datadir}/xine/
%dir %{_datadir}/xine/skins/
%{_datadir}/xine/skins/xinetic/
%{_datadir}/xine/skins/missing.png
%{_datadir}/xine/skins/xine_64.png
%{_datadir}/xine/skins/xine_splash.png
%{_datadir}/xine/skins/xine-ui_logo.mpg
%{_datadir}/xine/skins/xine-ui_logo.png
%{_datadir}/xine/oxine/
%{_datadir}/xine/visuals/
%{_datadir}/mime/packages/xine-ui.xml
%{_datadir}/applications/*xine.desktop
%{_datadir}/icons/hicolor/*x*/apps/xine.png
%{_datadir}/icons/hicolor/scalable/apps/xine.svgz
%{_datadir}/pixmaps/xine.xpm
%{_datadir}/pixmaps/xine_32.xpm
%{_mandir}/man1/xine*
%{_metainfodir}/xine.appdata.xml
%lang(de) %{_mandir}/de/man1/xine*
%lang(es) %{_mandir}/es/man1/xine*
%lang(fr) %{_mandir}/fr/man1/xine*
%lang(nl) %{_mandir}/nl/man1/xine*
%lang(pl) %{_mandir}/pl/man1/xine*

%files skins
%{_datadir}/xine/skins/*
%exclude %{_datadir}/xine/skins/xinetic/
%exclude %{_datadir}/xine/skins/missing.png
%exclude %{_datadir}/xine/skins/xine_64.png
%exclude %{_datadir}/xine/skins/xine_splash.png
%exclude %{_datadir}/xine/skins/xine-ui_logo.mpg
%exclude %{_datadir}/xine/skins/xine-ui_logo.png

%files aaxine
%{_bindir}/aaxine
%{_bindir}/cacaxine
%{_bindir}/fbxine
%{_mandir}/man1/aaxine*
%lang(de) %{_mandir}/de/man1/aaxine*
%lang(es) %{_mandir}/es/man1/aaxine*
%lang(nl) %{_mandir}/nl/man1/aaxine*
%lang(pl) %{_mandir}/pl/man1/aaxine*


%changelog
* Fri Dec 20 2024 Xavier Bachelot <xavier@bachelot.org> - 0.99.14-10
- Disable lirc support for EL10

* Tue Jul 30 2024 Xavier Bachelot <xavier@bachelot.org> - 0.99.14-9
- Fix build with rpm >= 4.20 (RHBZ#2301375)
- Drop EL7-only scriptlets

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 09 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0.99.14-7
- Add AppStream metadata

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Florian Weimer <fweimer@redhat.com> - 0.99.14-5
- Fix C compatibility issues in the configure script

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Xavier Bachelot <xavier@bachelot.org> - 0.99.14-3
- Fix skins URLs

* Wed Mar 08 2023 Xavier Bachelot <xavier@bachelot.org> - 0.99.14-2
- Use SPDX License: tag
- Drop useless conditionals
- Drop useless comments
- Add EL7 cond for %%post/%%postun
- Escape unescaped %% in %%changelog
- Drop very old Obsoletes:/Provides: for xine/xine-skins

* Sat Jan 07 2023 Xavier Bachelot <xavier@bachelot.org> - 0.99.14-1
- Update to 0.99.14
- Enable lirc and libcaca for EL9

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.99.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Tue Mar 08 2022 Xavier Bachelot <xavier@bachelot.org> - 0.99.13-4
- Add support for EL9

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.99.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Xavier Bachelot <xavier@bachelot.org> - 0.99.13-2
- Fix build on armv7hl, ppc64le and aarch64
- Fix build with libcaca >= 0.99.beta20

* Mon Dec 13 2021 Xavier Bachelot <xavier@bachelot.org> - 0.99.13-1
- Update to 0.99.13

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.99.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.99.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.99.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.99.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Xavier Bachelot <xavier@bachelot.org> - 0.99.12-1
- Update to 0.99.12.
- Drop now unneeded logo tweaks.
- Re-enable lirc support for EL8.
- Conditionalize snippets needed only for older than EL8 releases.
- Clean up file encoding fix.
- Fix obsolete BR: libtermcap-devel, BR: ncurses-devel instead.

* Sat Aug 24 2019 Xavier Bachelot <xavier@bachelot.org> - 0.99.11-1.20190824hg894d90
- Update to 0.99.11.
- Move cacaxine and fbxine to aaxine subpackage.
- Allow to build from snapshot.
- Use %%make_build and %%make_install.
- Re-order specfile preamble.
- Disable lirc support for EL8.

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.99.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.99.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.99.10-5
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.99.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 20 2018 Xavier Bachelot <xavier@bachelot.org> - 0.99.10-3
- Add BR: gcc.

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.99.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Xavier Bachelot <xavier@bachelot.org> - 0.99.10-1
- Update to 0.99.10.
- Drop obsolete conditionals.
- Drop Group: tags.
- Add %%license and Changelog to %%doc.

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.99.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.99.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Xavier Bachelot <xavier@bachelot.org> - 0.99.9-3
- Fix conditional BR on lirc-devel for EL7.

* Thu Oct 20 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.99.9-2
- Fix man files (rfbz#4297)

* Fri Aug 22 2014 Xavier Bachelot <xavier@bachelot.org> - 0.99.9-1
- Update to 0.99.9.
- Modernize specfile.

* Thu Mar 13 2014 Xavier Bachelot <xavier@bachelot.org> - 0.99.8-2
- Fix xine-skins Obsoletes:/Provides:.
- Remove explicit Requires: xine-lib.
- Own %%{_datadir}/xine.
- Fix conditionnal around BR: lirc-devel.
- Spec cosmetic cleanup.
- Add patch to update french translation.
- Add patch to fix crash on exit.

* Wed Mar 12 2014 Xavier Bachelot <xavier@bachelot.org> - 0.99.8-1
- Update to 0.99.8.
- Remove spurious tabs in specfile.

* Wed Oct 23 2013 Xavier Bachelot <xavier@bachelot.org> - 0.99.7-9
- Rebuild for xine-lib 1.2.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Michael J Gruber <mjg@fedoraproject.org> 0.99.7-7
- remove xine-check because it requires bits from the devel package

* Fri Mar 08 2013 Michael J Gruber <mjg@fedoraproject.org> 0.99.7-6
- add xine-lib-extras R because xine-0.99.7 needs an image decoder for the logo

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.99.7-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.99.7-3
- rebuild against new libjpeg

* Fri Oct 05 2012 Michael J Gruber <mjg@fedoraproject.org> 0.99.7-2.5
- add xine-lib-extras R because xine-0.99.7 needs an image decoder for the logo (unmerged)

* Thu Aug 30 2012 Michael J Gruber <mjg@fedoraproject.org> 0.99.7-2
- add libjpeg-turbo-devel BR
- utf8 fix (xine-ui is partly utf8 only)

* Thu Aug 30 2012 Michael J Gruber <mjg@fedoraproject.org> 0.99.7-1
- xine-ui-0.99.7
- dump patch10, patch11, patch12 (upstreamed)
- dump patch0 (obsolete before)
- fix source entry in spec

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Michael J Gruber <mjg@fedoraproject.org> 0.99.6-29
- fix build with libpng-1.5

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.99.6-28.1
- Rebuild for new libpng

* Sun Aug 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.99.6-27.1
- Rebuilt for rpm (#728707)

* Thu Jul 21 2011 Michael J Gruber <mjg@fedoraproject.org> 0.99.6-27
- fix build with newer curl (curl/types.h gone MIA)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 02 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.99.6-25
- fix help crash #579021

* Sun Apr 18 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.99.6-24
- replaced default.avi with default.ogv #572378

* Fri Apr 16 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.99.6-23
- subpkg aaxine to prevent xine-lib-extras for xine-ui

* Sun Apr 11 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.99.6-2
- readded skins

* Sun Apr 11 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.99.6-1
- xine-ui-0.99.6

* Thu Dec 17 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.99.6-0.1.20091217hg
- Switch to development branch by suggestion of upstream to fix some bugs.

* Thu Sep 03 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.99.5-16
- Move xine-ui_logo.mpv to main package from -skins.

* Sat Jul 25 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.99.5-15
- Move xine_splash.png to main package from -skins.
- Fix EPEL build.

* Thu Jul 23 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.99.5-14
- Fix build in rawhide.

* Mon Jul 20 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.99.5-13
- Added -skins subpackage.

* Wed Jul 15 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.99.5-12
- Added BR: xorg-x11-proto-devel.

* Sun May 17 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 0.99.5-11
- Added missing icon cache update to %%post section.

* Sun May 17 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 0.99.5-10
- Use desktop-install --remove-category instead of sed.

* Sat May 16 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 0.99.5-9
- More desktop file fixes.
- Fix aaxine by adding Requires: xine-lib-extras.

* Fri May 15 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 0.99.5-8
- Conserve time stamps.
- Drop unnecessary desktop file patch.
- Drop unnecessary versioning of dlopen'd libX11.so.
- Add mime type update and fix icon cache update.

* Fri May 15 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 0.99.5-7
- Fixes for inclusion into Fedora.

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.99.5-6
- rebuild for new F11 features

* Wed Oct 29 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.99.5-5
- rebuilt

* Sun Oct 26 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.99.5-4
- rebuilt

* Mon Aug 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.99.5-2
- rebuild

* Sat Jul 14 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.99.5-1
- 0.99.5, lots of patches made obsolete.
- Update icon cache and desktop database.
- Patch {aa,caca}xine to dlopen libX11.so.* instead of libX11.so at runtime.
- Patch to look for linux/kd.h instead of linux/kd.hb during build.
- Don't run autotools during build.

* Thu Mar 01 2007 Thorsten Leemhuis <fedora at leemhuis.info> - 0.99.4-11
- rebuild for new curl

* Tue Nov  7 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.99.4-10
- Re-enable VDR keys and patch, patched xine-lib not required (#1241).

* Thu Nov  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.99.4-9
- Drop X-Livna and Application desktop entry categories.

* Thu Nov  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.99.4-8
- Make VDR support optional, disabled by default, fixes #1238.

* Thu Apr 20 2006 Dams <anvil[AT]livna.org> - 0.99.4-7
- Added patch8 to fix up buffer overflow describe in #926

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Fri Jan 20 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.99.4-0.lvn.6
- %%langify non-English manpages, really convert all (and more docs) to UTF-8.
- Improve summary and description.

* Tue Jan  3 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.99.4-0.lvn.5
- Adapt to modular X.
- Drop pre-FC5 workarounds and rpmbuild conditionals.

* Thu Sep 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.99.4-0.lvn.4
- Clean up obsolete pre-FC3 stuff (LIRC and CACA now unconditionally enabled).
- Drop zero Epochs.

* Thu Sep 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.4-0.lvn.3
- Apply sprintf, uifixups and xftfontsize patches from Alex Stewart/freshrpms.
- Fix fbxine crash when the tty mode can't be set (upstreamed).
- Fix fbxine usage message and options (upstreamed).
- Make vdr support conditional (default enabled), require vdr-patched xine-lib
  if enabled, and build with it for FC4+.
- Build with gcc4 again on FC4+.

* Sun Aug 14 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.4-0.lvn.2
- Sync VDR patch with vdr-xine-0.7.5 (just for tracking purposes, no changes).

* Tue Aug  2 2005 Dams <anvil[AT]livna.org> - 0:0.99.4-0.lvn.1
- Updated to 0.99.4
- Fixed files section
- Dropped patch5 
- Dropped patch3

* Sun Jul 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.3-0.lvn.8
- Build with compat-gcc-32 for FC4 ("--with gcc32") as a temporary workaround
  for spurious directory creation attempts (#419) and possibly other issues.
- Use shared LIRC client libs, possibly enable LIRC support also on x86_64.
- Apply gcc4 menu crash fix, kudos for the patch to freshrpms.net and
  Alex Stewart, this'll be handy when we try with gcc4 again (#467).
- Clean up obsolete pre-FC2 stuff.

* Sat Jun  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.3-0.lvn.7
- Apply VDR support update patch from vdr-xine-0.7.4.

* Sat May 28 2005 Thorsten Leemhuis <fedora at leemhuis.info> - 0:0.99.3-0.lvn.6
- Fix typo

* Mon May  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.3-0.lvn.5
- Add support for CACA, rebuild with "--without caca" to disable (#380).

* Sat Apr 30 2005 Dams <anvil[AT]livna.org> - 0:0.99.3-0.lvn.4
- Fixed gcc4 build

* Wed Apr 13 2005 Dams <anvil[AT]livna.org> - 0:0.99.3-0.lvn.3
- Conditional lirc buildreq (default enabled)

* Sat Jan  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.3-0.lvn.2
- Enable support for VDR interaction keys.
- Enable curl unconditionally.
- Build with dependency tracking disabled.

* Wed Dec 29 2004 Dams <anvil[AT]livna.org> - 0:0.99.3-0.lvn.1
- Updated to 0.99.3

* Tue Jul  6 2004 Dams <anvil[AT]livna.org> 0:0.99.2-0.lvn.2
- Updated no-march/mcpu patch
- Updated mkinstalldirs patch

* Mon Jul  5 2004 Dams <anvil[AT]livna.org> 0:0.99.2-0.lvn.1
- Updated to 0.99.2

* Sun Jun 13 2004 Dams <anvil[AT]livna.org> 0:0.99.1-0.lvn.3
- Updated desktop entry for HID compliance

* Fri May 21 2004 Dams <anvil[AT]livna.org> 0:0.99.1-0.lvn.2
- Updated URL in Source0

* Sat Apr 17 2004 Dams <anvil[AT]livna.org> 0:0.99.1-0.lvn.1
- Updated to 0.99.1

* Thu Feb 26 2004 Dams <anvil[AT]livna.org> 0:0.9.23-0.lvn.2
- Updated xine-lib version requirement in build dependancy
- Hopefully fixed build for RH9

* Thu Dec 25 2003 Dams <anvil[AT]livna.org> 0:0.9.23-0.lvn.1
- s/fedora/livna/

* Thu Dec 25 2003 Dams <anvil[AT]livna.org> 0:0.9.23-0.fdr.1
- Updated patch for no march/mcpu from configure

* Wed Dec 24 2003 Dams <anvil[AT]livna.org> 0:0.9.23-0.fdr.1
- Updated to 0.9.23

* Sun Sep 28 2003 Dams <anvil[AT]livna.org> 0:0.9.22-0.fdr.4
- Added patch to fix po/Makefile for servern2 build

* Sun Aug 31 2003 Dams <anvil[AT]livna.org> 0:0.9.22-0.fdr.3
- Translated manpages iconv'ed into utf-8 encoding

* Sat Aug 23 2003 Dams <anvil[AT]livna.org> 0:0.9.22-0.fdr.2
- Conflict with old xine-skins packages
- Removed lirc conditionnal build requirement
- Added conditionnal Build dependencies for curl
- Added missing libtool BuildRequires

* Wed Aug 20 2003 Dams <anvil[AT]livna.org> 0:0.9.22-0.fdr.2
- No more -skins package
- No more url in Source0

* Fri Aug  8 2003 Dams <anvil[AT]livna.org> 0:0.9.22-0.fdr.1
- Updated to 0.9.22

* Tue Jul 15 2003 Dams <anvil[AT]livna.org> 0:0.9.21-0.fdr.3
- exporting SED=__sed seems to fix build to rh80

* Sun Jul  6 2003 Dams <anvil[AT]livna.org> 0:0.9.21-0.fdr.2
- Trying to avoid unowned directories
- Patch for configure not to set march/mcpu.
- Removed BuildArch.

* Sat May 17 2003 Dams <anvil[AT]livna.org> 0:0.9.21-0.fdr.1
- Updated to 0.9.21
- buildroot -> RPM_BUILD_ROOT
- Updated URL in Source0
- Updated BuildRequires

* Sat Apr 12 2003 Dams <anvil[AT]livna.org> 0:0.9.20-0.fdr.5
- Arch stuff

* Wed Apr  9 2003 Dams <anvil[AT]livna.org> 0:0.9.20-0.fdr.4
- Fixed typo
- Rebuild, linked against xine-lib 1 beta10

* Mon Apr  7 2003 Dams <anvil[AT]livna.org> 0:0.9.20-0.fdr.3
- Only one find_lang

* Mon Apr  7 2003 Dams <anvil[AT]livna.org> 0:0.9.20-0.fdr.2
- Added BuildRequires.
- Added --with directives.
- Added use of desktop-file-install
- Added more Requires tag.

* Thu Apr  3 2003 Dams <anvil[AT]livna.org> 
- Initial build.
