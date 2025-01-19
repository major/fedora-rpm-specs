%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary:       Painting program for creating icons and pixel-based artwork
Name:          mtpaint
Version:       3.50
Release:       15%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://mtpaint.sourceforge.net/
Source0:       http://downloads.sf.net/mtpaint/mtpaint-%{version}.tar.bz2
Source1:       http://downloads.sf.net/mtpaint/mtpaint_handbook-%{version}.zip
Patch0:        mtpaint-3.50-xdg-open.patch
Patch1:        mtpaint-3.31-png.patch
Patch2:        mtpaint-3.40-strip.patch
Patch3:        mtpaint-3.40-yad.patch
Patch4:        mtpaint-configure-c99.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: giflib-devel
BuildRequires: gtk3-devel
BuildRequires: lcms2-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: openjpeg2-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: dos2unix
Requires:      ImageMagick
Requires:      /usr/bin/yad

%description 
mtPaint is a simple painting program designed for creating icons and
pixel-based artwork. It can edit indexed palette or 24 bit RGB images
and offers basic painting and palette manipulation tools. Its main
file format is PNG, although it can also handle JPEG, GIF, TIFF, BMP,
XPM, and XBM files.

%package       handbook
Summary:       Handbook for the mtpaint painting application
License:       GFDL
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description   handbook
Install this package is want to read the handbook for the painting
application mtpaint.

%prep
%autosetup -p1 -a 1
chmod 0755 mtpaint_handbook-%{version}/docs/{en_GB,img,files,cs}
dos2unix -k mtpaint_handbook-%{version}/docs/index.html
dos2unix -k mtpaint_handbook-%{version}/docs/{en_GB,cs}/*.html

%build
# This is not a "normal" configure
export CFLAGS="%{optflags} -fPIC -fcommon"
export LDFLAGS="%{?__global_ldflags} -fPIC"
./configure \
    --prefix=%{_prefix} \
    --docdir=%{_pkgdocdir} \
    cflags asneeded intl man thread gtk3 GIF tiff jpeg jp2v2 imagick lcms2
make %{?_smp_mflags}

%install
make install MT_PREFIX=%{buildroot}%{_prefix}            \
             MT_MAN_DEST=%{buildroot}%{_mandir}          \
             MT_LANG_DEST=%{buildroot}%{_datadir}/locale \
             MT_DATAROOT=%{buildroot}%{_datadir}         \
             BIN_INSTALL=%{buildroot}%{_bindir}

desktop-file-install --delete-original         \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

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
EmailAddress: mtpaint-devel@lists.sourceforge.net
SentUpstream: 2014-09-22
-->
<application>
  <id type="desktop">mtpaint.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Create pixel art</summary>
  <description>
    <p>
      MTPaint is an application for creating images, with a specific focus on pixel art. It features a wide range
      of tools to help you create pixel art, including: a pixel-perfect grid, tools to make pixel gradients with
      the use of dithering, pixel brushes, and pixel line and shape tools.
    </p>
  </description>
  <url type="homepage">http://mtpaint.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/mtpaint/a.png</screenshot>
  </screenshots>
</application>
EOF

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_mandir}/man1/mtpaint.1*
%{_bindir}/mtpaint
%{_datadir}/appdata/mtpaint.appdata.xml
%{_datadir}/applications/mtpaint.desktop
%{_datadir}/pixmaps/mtpaint.png

%files handbook
%doc %{name}_handbook-%{version}/docs/*
%license %{name}_handbook-%{version}/COPYING

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.50-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 23 2024 Terje Rosten <terje.rosten@ntnu.no> - 3.50-12
- Rebuilt for new openjpeg2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Florian Weimer <fweimer@redhat.com> - 3.50-7
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 3.50-5
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Terje Rosten <terje.rosten@ntnu.no> - 3.50-1
- 3.50

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 01 2020 Terje Rosten <terje.rosten@ntnu.no> - 3.49.13-9
- Add GCC 10 workaround

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 3.49.13-5
- Add C compiler

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 3.49.13-3
- Rebuild (giflib)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Sandro Mani <manisandro@gmail.com> - 3.49.13-1
- Update to latest version
- Switch to openjpeg2
- Drop obsolete Group
- Use %%license for license files

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.40-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Terje Rosten <terje.rosten@ntnu.no> - 3.40-18
- fix build issue

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.40-17
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.40-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.40-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Terje Rosten <terje.rosten@ntnu.no> - 3.40-14
- New doc location

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.40-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Terje Rosten <terje.rosten@ntnu.no> - 3.40-12
- Print with yad

* Mon May 27 2013 Terje Rosten <terje.rosten@ntnu.no> - 3.40-11
- Add req. on kprinter (bz #964588)

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.40-10
- remove --vendor flag from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.40-8
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.40-7
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Terje Rosten <terje.rosten@ntnu.no> - 3.40-5
- Rebuilt for new libtiff

* Sun Feb 12 2012 Terje Rosten <terje.rosten@ntnu.no> - 3.40-4
- Rebuilt for new openjpeg

* Sun Feb 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 3.40-3
- Fix ld flags

* Sun Feb 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 3.40-2
- Don't strip bins (bz #787462)

* Sun Jan 29 2012 Terje Rosten <terje.rosten@ntnu.no> - 3.40-1
- Update to 3.40

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 3.31-6
- Add png patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 11 2010 Terje Rosten <terje.rosten@ntnu.no> - 3.31-4
- Add DSO patch

* Wed Aug 19 2009 Christoph Wickert <cwickert@fedoraproject.org> - 3.31-3
- Update to 3.31
- Make handbook package noarch
- New gtk-update-icon-cache scriptlets

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 15 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.21-1
- 3.21
- add %%defattr on handbook

* Sat Feb  9 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.20-3
- Rebuild

* Wed Jan 23 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.20-2
- Unzip by %%setup
- Simplify %%post/postun
- Added COPYING to handbook

* Sat Dec 29 2007 Terje Rosten <terje.rosten@ntnu.no> - 3.20-1
- 3.20
- include patch now upstream
- handbook patch now upstream

* Wed Dec 19 2007 Terje Rosten <terje.rosten@ntnu.no> - 3.20-0.1.rc2
- 3.20RC2
- disable openjpeg support
- icon and desktop file now upstream

* Sun Dec 16 2007 Terje Rosten <terje.rosten@ntnu.no> - 3.19-1
- upgrade to 3.19
- misc fixes to be rpmlint clean
- fix debuginfo package
- handle translations
- fix license
- compile with correct flags
- add patch to compile
- add handbook subpackage (and fix app to find docs)
- add xdg-open patch
- dont' use %%makeinstall
- add icon and mimetypes to desktop file

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 3.11-1 - 5280/dries
- Updated to release 3.11.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.02-1
- Updated to release 3.02.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 3.01-1
- Updated to release 3.01.

* Wed May 31 2006 Dries Verachtert <dries@ulyssis.org> - 2.31-1
- Updated to release 2.31.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.30-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.30-1
- Updated to release 2.30.

* Sun Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.20-1
- Updated to release 2.20.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Sat Sep 24 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Initial package.
