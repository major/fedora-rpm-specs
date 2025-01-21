%global app_defaults_dir %{_datadir}/X11/app-defaults

Summary: An X Window System tool for drawing basic vector graphics
Name: xfig
Version: 3.2.9
Release: 6%{?dist}
License: MIT
URL:     https://en.wikipedia.org/wiki/Xfig
Source0: http://downloads.sourceforge.net/mcj/xfig-%{version}.tar.xz
Source1: xfig-icons.tar.gz
Source2: xfig.desktop
Source3: xfig.appdata.xml
# https://sourceforge.net/p/mcj/tickets/165/
# https://bugzilla.redhat.com/show_bug.cgi?id=2252679
# https://sourceforge.net/p/mcj/xfig/ci/68403622a6f6c7d74f73e38989cfc0ed86fb83fc/
Patch0:  Sanitize-a-call-to-realloc-ticket-165.patch
# https://sourceforge.net/p/mcj/tickets/163/
# https://sourceforge.net/p/mcj/xfig/ci/a4a2f3f3aa29ec7fc84f9d782306b37bbe75025c/
Patch1:  Fix-exporting-only-active-layers-ticket-163.patch
# https://sourceforge.net/p/mcj/tickets/159/
# https://bugzilla.redhat.com/show_bug.cgi?id=2260359
# https://sourceforge.net/p/mcj/xfig/ci/1e2d842875502b4ce0e74ec779454304c71efe54/
Patch2: 0001-Map-symbol-and-dingbat-glyphs-to-their-unicode-locat.patch
# compile fix for above patch
Patch3: xfig-3.2.9-compile-fix.patch
#Patch0: xfig-3.2.5a-default-apps.patch
#Patch1: xfig-3.2.5-urwfonts.patch

BuildRequires: make
BuildRequires: gcc libtool
BuildRequires: transfig
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXaw-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libXpm-devel
BuildRequires: libXt-devel
BuildRequires: Xaw3d-devel
BuildRequires: man2html-core ImageMagick
BuildRequires: desktop-file-utils libappstream-glib
# For eps preview generation
Requires: ghostscript
Requires: transfig
# Used in the UI
Requires: xorg-x11-fonts-misc
# For scalable fonts, inc. Bookman, New Century Schoolbook and Palatino
Requires: urw-base35-fonts-legacy

# We used to have seperate Xaw3d and non Xaw3d pkgs, now we only have Xaw3d
Obsoletes: %{name}-common < %{version}-%{release}
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-plain < %{version}-%{release}
Provides:  %{name}-plain = %{version}-%{release}
Obsoletes: %{name}-Xaw3d < %{version}-%{release}
Provides:  %{name}-Xaw3d = %{version}-%{release}

%description
Xfig is an X Window System tool for creating basic vector graphics,
including bezier curves, lines, rulers and more.  The resulting
graphics can be saved, printed on PostScript printers or converted to
a variety of other formats (e.g., X11 bitmaps, Encapsulated
PostScript, LaTeX).

You should install xfig if you need a simple program to create vector
graphics.


%prep
%autosetup -p1 -a 1
for i in doc/html/japanese/button_frame.fig doc/html/japanese/japanese.ps \
         doc/html/animate.js; do
  sed -i.orig 's/\r//' $i; touch -r $i.orig $i; rm $i.orig
done
autoreconf -i


%build
# Fedora's Xaw3d is built with -DXAW_ARROW_SCROLLBARS
export CFLAGS="-DXAW_ARROW_SCROLLBARS $RPM_OPT_FLAGS -fno-strength-reduce -fno-strict-aliasing"
%configure
%make_build


%install
%make_install INSTALL="install -p"
cp -p README CHANGES FIGAPPS $RPM_BUILD_ROOT%{_docdir}/%{name}

rm -r $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,64x64}/apps
convert %{name}16x16.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
convert %{name}32x32.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
convert %{name}64x64.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{app_defaults_dir}/Fig
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Hans de Goede <hdegoede@redhat.com> - 3.2.9-4
- Fix missing Dingbats and Symbol glyphs
- Resolves: rhbz#2260359

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.9-2
- Backport upstream patches for upstream 2 issues
  - Fix exporting only active layers
  - Sanitize a call to realloc (redhat #2252679)

* Sat Aug 26 2023 Ranjan Maitra <aarem@fedoraproject.org> - 3.2.9-1
- New upstream release 3.2.9

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 11 2021 Hans de Goede <hdegoede@redhat.com> - 3.2.8b-1
- New upstream release 3.2.8b

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 29 2021 Hans de Goede <hdegoede@redhat.com> - 3.2.8a-1
- New upstream release 3.2.8a

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7b-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Hans de Goede <hdegoede@redhat.com> - 3.2.7b-1
- New upstream release 3.2.7b

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Hans de Goede <hdegoede@redhat.com> - 3.2.7a-2
- Fix spline drawing (rhbz#1665237)

* Mon Oct 29 2018 Hans de Goede <hdegoede@redhat.com> - 3.2.7a-1
- New upstream release 3.2.7a
- Add Requires: transfig to make sure esp export works (rhbz#1642033)
- Switch back to URW fonts so that Bookman, New Century Schoolbook and
  Palatino work again. This uses the old version of the URW fonts which are
  now packaged as urw-base35-fonts-legacy (rhbz#1523624, rhbz#1551219)
- Trim the changelog

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Hans de Goede <hdegoede@redhat.com> - 3.2.6a-7
- Fix font issues take 2 (rhbz#1523624) :
 - It turns out the new urw fonts are completely unusuable as X11 core fonts,
   stop using them for now (see bug rhbz#1551219)
 - Add a patch to use the fallback fonts for non-scalable fonts too, so that
   we at least show something somewhat reasonable for Bookman, New Century
   Schoolbook and Palatino
 - This means that display of Zapf Chancery and Zapf Dingbats currently
   falls back to the "fixed" font, which is completely wrong for Dingbats

* Thu Mar 01 2018 Hans de Goede <hdegoede@redhat.com> - 3.2.6a-6
- Fix font issues (rhbz#1523624) :
 - Adjust xfig-3.2.5-urwfonts.patch for new font names in urw-base35-fonts
 - Except for the symbols font, use the old un-scalable Adobe PCF Symbol font
   for now as StandardSymbolsPS.otf from urw-base35-fonts is currently broken
 - Add a patch to deal with some fonts being scalable, while Symbol is not
 - Note the dingbats font is also broken in urw-base35-fonts, but there is no
   replacement for it, so that font is still broken, see rhbz#1534206
- ghostscript-core no longer exists, instead require ghostscript (rhbz#1536581)
- Remove obsolete icon-cache and desktop-database scriptlets
- Add a patch from Debian fixing some issues with arrows

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Adam Jackson <ajax@redhat.com> - 3.2.6a-4
- Drop unneeded BuildRequires: imake

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Hans de Goede <hdegoede@redhat.com> - 3.2.6a-1
- New upstream release 3.2.6a

* Sun Feb 12 2017 Hans de Goede <hdegoede@redhat.com> - 3.2.6-5
- Build with -DGSBIT to fix eps file preview generation (rhbz#1418560)
- Fix broken screenshot links in appdata

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Hans de Goede <hdegoede@redhat.com> - 3.2.6-3
- Switch to non -full (smaller) version of upstream sources,
  we package transfig seperately so we do not need the -full version

* Thu Aug 11 2016 Hans de Goede <hdegoede@redhat.com> - 3.2.6-2
- Make using metric units the default again

* Thu Aug 11 2016 Hans de Goede <hdegoede@redhat.com> - 3.2.6-1
- New upstream release 3.2.6
- Drop all patches, all fixes are upstream now
- Drop -plain subpackage, only build Xaw3d version
- Update appdata screenshots for xfig.org being gone
  (point to http://epb.lbl.gov/xfig/ for now)

* Sun Feb 28 2016 Hans de Goede <hdegoede@redhat.com> - 3.2.5-48.c
- Bring in various bugfixes from Debian
- Convert icons to png
- Add appdata

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-47.c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
