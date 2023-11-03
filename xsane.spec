# if you rebuild, please change bugtracker_url accordingly:
%global bugtracker_url http://bugzilla.redhat.com

%global gimpplugindir %(%___build_pre; gimptool --gimpplugindir 2>/dev/null || echo INVALID)/plug-ins
%global iconrootdir %{_datadir}/icons/hicolor

# needed for off-root building
%global _configure ../configure

Name: xsane
Summary: X Window System front-end for the SANE scanner interface
Version: 0.999
Release: 48%{?dist}
Source0: http://www.xsane.org/download/%{name}-%{version}.tar.gz
Source1: xsane-256x256.png
# use "xdg-open" instead of "netscape" to launch help browser
# submitted to upstream (Oliver Rauch) via email, 2013-06-04
Patch0: xsane-0.995-xdg-open.patch
# submitted to upstream (Oliver Rauch) via email, 2009-08-18
Patch1: xsane-0.995-close-fds.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=504344
# distro-specific(?), upstream won't accept it: "don't show license dialog"
# submitted to upstream (Oliver Rauch) anyway via email, 2013-06-04
Patch2: xsane-0.996-no-eula.patch
# enable off-root building
# submitted to upstream (Oliver Rauch) via email, 2010-06-23
Patch3: xsane-0.997-off-root-build.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=608047
# https://bugzilla.redhat.com/show_bug.cgi?id=621778
# submitted to upstream (Oliver Rauch) via email, 2013-07-05
Patch4: xsane-0.999-no-file-selected.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=198422
# submitted to upstream (Oliver Rauch) via email, 2010-06-29
Patch5: xsane-0.997-ipv6.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=624190
# fix from: https://bugs.launchpad.net/ubuntu/+source/xsane/+bug/370818
# submitted to upstream (Oliver Rauch) via email, 2011-06-01
Patch6: xsane-0.998-preview-selection.patch
# fix building with libpng >= 1.5
# submitted to upstream (Oliver Rauch) via email, 2011-11-21
Patch7: xsane-0.998-libpng.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=795085
# set program name/wmclass so GNOME shell picks appropriate high resolution
# icon file
# submitted to upstream (Oliver Rauch) via email, 2013-06-04
Patch8: xsane-0.998-wmclass.patch
# partly distro-specific: customize desktop file
# submitted to upstream (Oliver Rauch) via email, 2013-06-04
Patch9: xsane-0.998-desktop-file.patch
# man page: update command line options
# submitted to upstream (Oliver Rauch) via email, 2013-07-08
Patch10: xsane-0.999-man-page.patch
# avoid producing PDFs with bpp > 8
# submitted to upstream (Oliver Rauch) via email, 2013-09-09
Patch11: xsane-0.999-pdf-no-high-bpp.patch
# build against lcms 2.x
# submitted to upstream (Oliver Rauch) via email, 2013-09-23
Patch12: xsane-0.999-lcms2.patch
# fix issues found during static analysis that don't require far-reaching
# refactoring
# submitted to upstream (Oliver Rauch) via email, 2014-04-02
Patch13: xsane-0.999-coverity.patch
# update lib/snprintf.c to the latest version from LPRng that has a Free license
# submitted to upstream (Oliver Rauch) via email, 2014-05-29
Patch14: xsane-0.999-snprintf-update.patch
# fix signal handling (#1073698)
# submitted to upstream (Oliver Rauch) via email, 2014-07-03
Patch15: xsane-0.999-signal-handling.patch

# autoconf-generated files
Patch100: xsane-0.999-7-autoconf.patch.bz2

Patch101: xsane-configure-c99.patch

# LGPL-3.0-or-later is due of using gimp libraries
# src/* - GPL2+
# lib/* (copies from glibc) - LGPL2+
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL: http://www.xsane.org/

# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses make
BuildRequires: make
%if 0%{?rhel} <= 8 || 0%{?fedora}
BuildRequires: gimp-devel
%endif
BuildRequires: gtk2-devel
BuildRequires: lcms2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: sane-backends-devel >= 1.0.19-15
BuildRequires: desktop-file-utils >= 0.2.92
BuildRequires: libtiff-devel
BuildRequires: gettext-devel
Requires: xsane-common
Requires: hicolor-icon-theme

%description
XSane is an X based interface for the SANE (Scanner Access Now Easy)
library, which provides access to scanners, digital cameras, and other
capture devices. XSane is written in GTK+ and provides control for
performing the scan and then manipulating the captured image.

%if 0%{?rhel} <= 8 || 0%{?fedora}
%package gimp
Summary: GIMP plug-in providing the SANE scanner interface
Requires: gimp >= 2:2.2.12-4
Requires: xsane-common

%description gimp
This package provides the regular XSane frontend for the SANE scanner
interface, but it works as a GIMP plug-in. You must have GIMP
installed to use this package.
%endif

%package common
Summary: Common files for xsane packages

%description common
This package contains common files needed by other xsane packages.

%prep
%setup -q

# convert some files to UTF-8
for doc in xsane.{CHANGES,PROBLEMS,INSTALL}; do
    iconv -f ISO-8859-1 -t utf8 "$doc" -o "$doc.new" && \
    touch -r "$doc" "$doc.new" && \
    mv "$doc.new" "$doc"
done

%patch -P 0 -p1 -b .xdg-open
%patch -P 1 -p1 -b .close-fds
%patch -P 2 -p1 -b .no-eula
%patch -P 3 -p1 -b .off-root-build
%patch -P 4 -p1 -b .no-file-selected
%patch -P 5 -p1 -b .ipv6
%patch -P 6 -p1 -b .preview-selection.patch
%patch -P 7 -p1 -b .libpng
%patch -P 8 -p1 -b .wmclass
%patch -P 9 -p1 -b .desktop-file
%patch -P 10 -p1 -b .man-page
%patch -P 11 -p1 -b .pdf-no-high-bpp
%patch -P 12 -p1 -b .lcms2
%patch -P 13 -p1 -b .coverity
%patch -P 14 -p1 -b .snprintf-update
%patch -P 15 -p1 -b .signal-handling

%patch -P 100 -p1 -b .autoconf
%patch -P 101 -p1 -b .c99

# in-root config.h breaks off-root building
rm include/config.h

mkdir build-with-gimp
mkdir build-without-gimp

%build
CFLAGS='%optflags -fno-strict-aliasing -DXSANE_BUGTRACKER_URL=\"%{bugtracker_url}\"'
export CFLAGS

%if 0%{?rhel} <= 8 || 0%{?fedora}
pushd build-with-gimp
%configure --enable-gimp
%make_build
popd
%endif

pushd build-without-gimp
%configure --disable-gimp
make
popd

cp %{SOURCE1} src/

%install

pushd build-without-gimp
%make_install
popd

%if 0%{?rhel} <= 8 || 0%{?fedora}
# install GIMP plugin
install -m 0755 -d %{buildroot}%{gimpplugindir}
install -m 0755 build-with-gimp/src/xsane %{buildroot}%{gimpplugindir}
%endif

# install customized desktop file
rm %{buildroot}%{_datadir}/applications/xsane.desktop
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    src/xsane.desktop

# icon files in multiple resolutions
for res in 16 32 48 256; do
    tdir="%{buildroot}%{iconrootdir}/${res}x${res}/apps"
    install -m 0755 -d "$tdir"
    install -m 0644 src/xsane-${res}x${res}.png "${tdir}/xsane.png"
done

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
EmailAddress: Oliver.Rauch@xsane.org
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">xsane.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Scan images with a scanner</summary>
  <description>
    <p>
      XSane is an application to scan images using a hardware scanner attached
      to your computer.
      It is able to save in a variety of image formats, including TIFF and JPEG
      and can even save your scan as a PDF.
      XSane also has support for scanning multiple pages and merging them into
      a single document.
    </p>
  </description>
  <url type="homepage">http://www.xsane.org/</url>
  <screenshots>
    <screenshot type="default">http://www.xsane.org/doc/xsane-save.jpg</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name} XSANE.lang

%if 0%{?rhel} <= 8 || 0%{?fedora}
%pre gimp
# remove obsolete gimp-plugin-mgr managed symlink
if [ -L "%{gimpplugindir}/xsane" ]; then
    rm -f "%{gimpplugindir}/xsane"
fi
%endif

%files -f XSANE.lang
%doc xsane.ACCELKEYS xsane.AUTHOR xsane.BEGINNERS-INFO xsane.BUGS xsane.CHANGES xsane.FAQ xsane.LANGUAGES xsane.LOGO xsane.NEWS xsane.ONLINEHELP xsane.PROBLEMS xsane.ROOT xsane.TODO
%license xsane.COPYING
%{_bindir}/xsane
%{_mandir}/man1/*
%if %{with desktop_vendor_tag}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/fedora-xsane.desktop
%else
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/xsane.desktop
%endif
%{_datadir}/pixmaps/xsane.xpm
%{iconrootdir}/*/apps/%{name}.png

%if 0%{?rhel} <= 8 || 0%{?fedora}
%files gimp
%{gimpplugindir}/xsane
%endif

%files common
%doc xsane.AUTHOR
%license xsane.COPYING
%dir %{_datadir}/sane
%{_datadir}/sane/xsane

%changelog
* Wed Jul 26 2023 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-48
- SPDX migration

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 19 2023 Josef Ridky <jridky@redhat.com> - 0.999-46
- Migrate to SPDX license format

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Florian Weimer <fweimer@redhat.com> - 0.999-44
- Port configure script to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-39
- remove gimp plugin for eln, put explicit requirement for GTK2

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-38
- make is no longer in buildroot by default

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 0.999-36
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-33
- rebuilt again (because bodhi cannot remove builds from even unpushed updates)

* Mon Apr 08 2019 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-32
- rebuilt for gimp-2.10.10

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-30
- correcting license

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-28
- remove dependency on ImageMagick and netpbm-progs, because they were needed for
  tests during %%build phase, which were removed in commit SHA 0595c15da29

* Mon Apr 09 2018 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-27
- remove vendor tag, license needs to be in %%license (FPG)

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 0.999-26
- remove old stuff
- gcc is no longer in buildroot by default

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.999-24
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.999-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.999-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.999-18
- Add an AppData file for the software center

* Mon Dec 08 2014 David King <amigadave@amigadave.com> - 0.999-17
- Depend on hicolor-icon-theme for icon directories (#1171826)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.999-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Nils Philippsen <nils@redhat.com> - 0.999-15
- make signal-handling patch work with older glib versions
- use consistent name for snprintf patch

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.999-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Tom Callaway <spot@fedoraproject.org> - 0.999-13
- update to newer snprintf implementation from LPRng that resolves license 
  issue (#1102523)

* Thu Apr 03 2014 Nils Philippsen <nils@redhat.com> - 0.999-12
- don't unnecessarily recreate 32px icon (#966301)
- ship 16px icon

* Wed Apr 02 2014 Nils Philippsen <nils@redhat.com> - 0.999-11
- fix coverity patch: ensure directories exist instead of indiscriminately
  attempting to create them (#1079586)

* Wed Mar 19 2014 Nils Philippsen <nils@redhat.com> - 0.999-10
- fix signal handling (#1073698)
- fix issues found during static analysis that don't require far-reaching
  refactoring

* Mon Sep 23 2013 Nils Philippsen <nils@redhat.com> - 0.999-7
- get rid of ancient compat cruft
- build against lcms2

* Mon Sep 09 2013 Nils Philippsen <nils@redhat.com> - 0.999-6
- avoid producing PDFs with bpp > 8

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.999-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Nils Philippsen <nils@redhat.com> - 0.999-4
- man page: update command line options

* Fri Jul 05 2013 Nils Philippsen <nils@redhat.com> - 0.999-3
- fix no-file-selected patch: change working directories (#621778, fix by Pavel
  Polischouk)

* Thu Jun 27 2013 Nils Philippsen <nils@redhat.com> - 0.999-2
- ensure correct autoconf patch is used

* Tue Jun 04 2013 Nils Philippsen <nils@redhat.com> - 0.999-1
- version 0.999
- remove obsolete patches
- update/fix patch comments
- fix changelog dates

* Fri May 17 2013 Nils Philippsen <nils@redhat.com> - 0.998-21
- don't dereference NULL preview objects when quitting (#963696)
- fix vendor tag logic in a prettier way

* Tue May 14 2013 Jon Ciesla <limburgher@gmail.com> - 0.998-20
- Re-fix vendor tag logic.

* Fri Mar 08 2013 Nils Philippsen <nils@redhat.com> - 0.998-19
- fix vendor tag retaining logic (thanks to Toshio Kuratomi)

* Thu Mar 07 2013 Nils Philippsen <nils@redhat.com> - 0.998-18
- retain vendor tag up to Fedora 18

* Mon Feb 11 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.998-17
- Add BR: ImageMagick for identify

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.998-16
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Wed Jan 30 2013 Nils Philippsen <nils@redhat.com> - 0.998-15
- build with -fno-strict-aliasing
- tidy up desktop file
- catch errors when determining the %%gimpplugindir macro
- use netpbm pipeline to create 32px PNG icon instead of convert (which embeds
  timestamps in the resulting file)

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.998-14
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.998-13
- rebuild against new libjpeg

* Mon Sep 03 2012 Nils Philippsen <nils@redhat.com> - 0.998-12
- calculate minimum window size better for multi-head setups
- correct man page (#675437)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.998-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 26 2012 Nils Philippsen <nils@redhat.com> - 0.998-10
- add icon cache update scriptlets

* Fri May 25 2012 Nils Philippsen <nils@redhat.com> - 0.998-9
- install and use higher resolution icons (#795085)

* Tue Apr 03 2012 Nils Philippsen <nils@redhat.com> - 0.998-8
- rebuild against gimp 2.8.0 release candidate

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 0.998-7
- rebuild for gcc 4.7

* Fri Dec 16 2011 Nils Philippsen <nils@redhat.com> - 0.998-6
- rebuild for GIMP 2.7

* Mon Nov 21 2011 Nils Philippsen <nils@redhat.com> - 0.998-5
- patch and rebuild for libpng-1.5

* Wed Jun 01 2011 Nils Philippsen <nils@redhat.com> - 0.998-4
- fix a problem in mouse event processing that interferes with selecting the
  scan rectangle in the preview window (#624190, patch by Reinhard Fössmeier)

* Mon Apr 04 2011 Nils Philippsen <nils@redhat.com> - 0.998-3
- don't dereference unset xsane.preview (#693224)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.998-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Nils Philippsen <nils@redhat.com> - 0.998-1
- version 0.998
- patch desktop file instead of copying it over

* Tue Jul 13 2010 Nils Philippsen <nils@redhat.com> - 0.997-10
- don't crash if no files are selected, take two

* Mon Jul 12 2010 Nils Philippsen <nils@redhat.com> - 0.997-9
- distribute license and other documentation with xsane-common

* Tue Jun 29 2010 Nils Philippsen <nils@redhat.com> 0.997-8
- support IPv6 (#198422)

* Mon Jun 28 2010 Nils Philippsen <nils@redhat.com> 0.997-7
- work around old %%configure macro

* Mon Jun 28 2010 Nils Philippsen <nils@redhat.com> 0.997-6
- don't crash if no files are selected (#608047)

* Wed Jun 23 2010 Nils Philippsen <nils@redhat.com> 0.997-5
- don't use gimp-plugin-mgr anymore
- use off-root builds

* Thu Feb 25 2010 Nils Philippsen <nils@redhat.com> 0.997-4
- quote RPM macros in changelog

* Tue Aug 18 2009 Nils Philippsen <nils@redhat.com>
- explain patches

* Wed Aug 05 2009 Nils Philippsen <nils@redhat.com> 0.997-3
- Merge Review (#226658):
  - replace %%desktop_vendor macro with "fedora"
  - fix xsane-gimp requirements
  - move EULA and documentation into -common subpackage

* Mon Aug 03 2009 Nils Philippsen <nils@redhat.com> 0.997-2
- remove ExcludeArch: s390 s390x

* Fri Jul 31 2009 Nils Philippsen <nils@redhat.com> 0.997-1
- version 0.997
- drop obsolete sane-backends-1.0.20 patch

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Nils Philippsen <nils@redhat.com> 0.996-9
- don't show EULA, mention bugzilla in about dialog (#504344)

* Mon Jul 20 2009 Nils Philippsen <nils@redhat.com> 0.996-8
- don't use obsolete SANE_CAP_ALWAYS_SETTABLE macro (#507823)

* Tue Jul  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> 0.996-7
- don't own %%{_datadir}/applications/ (filesystem package owns it)

* Fri May 29 2009 Nils Philippsen <nils@redhat.com>
- Merge review (#226658):
  - convert documentation files to UTF-8
  - don't BR: sed
  - don't own %%{_datadir}/applications, %%{_sysconfdir}/gimp,
    %%{_sysconfdir}/gimp/plugins.d
  - don't package unnecessary documentation

* Mon Mar 02 2009 Nils Philippsen <nils@redhat.com> - 0.996-6
- rebuild against new sane-backends (just in case)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Nils Philippsen <nphilipp@redhat.com> - 0.996-3
- pickup changed desktop file, close-fds patch in F9, F10

* Tue Jan 20 2009 Nils Philippsen <nphilipp@redhat.com> - 0.996-2
- BR: lcms-devel

* Sun Jan 18 2009 Nils Philippsen <nphilipp@redhat.com> - 0.996-1
- version 0.996
- don't use %%makeinstall
- use shipped xsane.xpm as application icon

* Fri Jul 18 2008 Nils Philippsen <nphilipp@redhat.com> - 0.995-5
- fix fd leak prevention (#455450)

* Tue Jul 15 2008 Nils Philippsen <nphilipp@redhat.com> - 0.995-4
- don't leak file descriptors to help browser process (#455450)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.995-3
- Autorebuild for GCC 4.3

* Thu Nov 29 2007 Nils Philippsen <nphilipp@redhat.com> - 0.995-2
- make EULA, license dialogs be viewable on 800x600 displays

* Fri Nov 23 2007 Nils Philippsen <nphilipp@redhat.com> - 0.995-1
- version 0.995
- remove obsolete gimp2.0, medium-definitions, showeulaonce patches

* Thu Nov 15 2007 Nils Philippsen <nphilipp@redhat.com>
- explicitely enable building the gimp plugin in configure call
- reorder spec file sections

* Wed Sep 05 2007 Nils Philippsen <nphilipp@redhat.com> - 0.994-4
- fix "Category" entries in desktop file

* Wed Sep 05 2007 Nils Philippsen <nphilipp@redhat.com>
- change license to GPLv2+

* Tue Apr 24 2007 Nils Philippsen <nphilipp@redhat.com> - 0.994-3
- don't include obsolete Application category in desktop file (#226658)

* Wed Apr 04 2007 Nils Philippsen <nphilipp@redhat.com> - 0.994-2
- save prefs when EULA is accepted to ensure that EULA is only shown once at
  startup (#233645)

* Tue Apr 03 2007 Nils Philippsen <nphilipp@redhat.com> - 0.994-1
- version 0.994 (#235038)

* Fri Mar 30 2007 Nils Philippsen <nphilipp@redhat.com> - 0.993-2
- fix summaries and buildroot, don't remove buildroot on %%prep, mark dirs and
  config files, don't reference %%buildroot in %%build, use double-%% in
  changelog entries (#226658)

* Fri Mar 02 2007 Nils Philippsen <nphilipp@redhat.com> - 0.993-1
- version 0.993 (#230706)

* Wed Oct 25 2006 Nils Philippsen <nphilipp@redhat.com> - 0.991-4
- fix typo in scriptlet (#212063)

* Mon Oct 23 2006 Nils Philippsen <nphilipp@redhat.com> - 0.991-3
- really don't barf on missing gimp-plugin-mgr when updating (#208159)

* Mon Oct 02 2006 Nils Philippsen <nphilipp@redhat.com> - 0.991-2
- don't barf on missing gimp-plugin-mgr when updating (#208159)

* Mon Aug 28 2006 Nils Philippsen <nphilipp@redhat.com> - 0.991-1
- version 0.991
- remove obsolete buffer patch

* Wed Aug 16 2006 Nils Philippsen <nphilipp@redhat.com> - 0.99-6
- revamp scheme for integrating external GIMP plugins (#202545)
- use disttag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.99-5.1
- rebuild

* Thu Jun 08 2006 Nils Philippsen <nphilipp@redhat.com> - 0.99-5
- re-add desktop file (#170835)
- use %%buildroot consistently
- add automake, autoconf build requirements

* Wed Apr 05 2006 Nils Philippsen <nphilipp@redhat.com> - 0.99-4
- use XSANE.lang instead of xsane.lang to avoid %%doc multilib regression

* Tue Apr 04 2006 Nils Philippsen <nphilipp@redhat.com> - 0.99-3
- fix medium-definitions patch to not barf on obsolete options in config file
  (#185269, by Aldy Hernandez)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.99-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.99-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 16 2006 Nils Philippsen <nphilipp@redhat.com> 0.99-2
- fix buffer overflow

* Fri Jan 13 2006 Nils Philippsen <nphilipp@redhat.com> 0.99-1
- version 0.99

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 24 2005 Nils Philippsen <nphilipp@redhat.com> 0.98a-1
- version 0.98a

* Tue Oct 04 2005 Nils Philippsen <nphilipp@redhat.com> 0.97-1
- version 0.97

* Mon Jun 20 2005 Tim Waugh <twaugh@redhat.com> 0.95-4
- Build requires gettext-devel (bug #160994).

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 0.95-3
- Rebuild for new GCC.

* Wed Dec  8 2004 Tim Waugh <twaugh@redhat.com> 0.95-2
- Fix crash on start (bug #142148).

* Fri Dec  3 2004 Tim Waugh <twaugh@redhat.com> 0.95-1
- 0.95.
- No longer need badcode patch.
- Enable translations again.
- New method of installing GIMP plug-in due to Nils Philippsen.

* Mon Jun 28 2004 Tim Waugh <twaugh@redhat.com> 0.92-13
- Build requires libtiff-devel (bug #126564).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jun  4 2004 Tim Waugh <twaugh@redhat.com> 0.92-11
- Fix GIMP plug-in package (bug #125254).

* Wed Apr 21 2004 Seth Nickell <snickell@redhat.com> 0.92-10
- Remove .desktop file

* Wed Mar 31 2004 Tim Waugh <twaugh@redhat.com> 0.92-9
- Rebuilt.

* Thu Mar 18 2004 Nils Philippsen <nphilipp@redhat.com> 0.92-8
- Rebuild against new gimp.

* Tue Mar  9 2004 Tim Waugh <twaugh@redhat.com> 0.92-7
- Fix desktop file Name (bug #117370).

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Tim Waugh <twaugh@redhat.com> 0.92-5
- Fixed %%post scriptlet.

* Sun Jan 25 2004 Tim Waugh <twaugh@redhat.com> 0.92-4
- Gimp patch updated.

* Fri Jan 23 2004 Tim Waugh <twaugh@redhat.com> 0.92-3
- Translations are broken -- turn them off for the time being.
- Really apply the patch this time.
- Fix up post/postun scriptlets.

* Fri Jan 23 2004 Tim Waugh <twaugh@redhat.com> 0.92-2
- Apply patch for building against new gimp.

* Mon Dec 15 2003 Tim Waugh <twaugh@redhat.com> 0.92-1
- 0.92.

* Thu Nov 27 2003 Thomas Woerner <twoerner@redhat.com> 0.91-2
- removed rpath

* Wed Oct  8 2003 Tim Waugh <twaugh@redhat.com>
- Avoid undefined behaviour in xsane-preview.c (bug #106314).

* Thu Jul 24 2003 Tim Waugh <twaugh@redhat.com> 0.91-1
- 0.91.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr  9 2003 Tim Waugh <twaugh@redhat.com> 0.90-2
- Set default HTML viewer to htmlview (bug #88318).

* Thu Mar 20 2003 Tim Waugh <twaugh@redhat.com> 0.90-1
- 0.90.

* Sat Feb  1 2003 Matt Wilson <msw@redhat.com> 0.89-3
- use %%{_libdir} for gimp plugin path

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Oct 25 2002 Tim Waugh <twaugh@redhat.com> 0.89-1
- 0.89.
- Use %%find_lang.

* Fri Aug 30 2002 Tim Waugh <twaugh@redhat.com> 0.84-8
- Don't require gimp-devel (cf. bug #70754).

* Tue Jul 23 2002 Tim Waugh <twaugh@redhat.com> 0.84-7
- Desktop file fixes (bug #69555).

* Mon Jul 15 2002 Tim Waugh <twaugh@redhat.com> 0.84-6
- Use desktop-file-install.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.84-5
- automated rebuild

* Wed Jun 12 2002 Tim Waugh <twaugh@redhat.com> 0.84-4
- Rebuild to fix bug #66132.

* Thu May 23 2002 Tim Powers <timp@redhat.com> 0.84-3
- automated rebuild

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 0.84-2
- Rebuild in new environment.

* Wed Jan 23 2002 Tim Waugh <twaugh@redhat.com> 0.84-1
- 0.84.
- Remove explicit sane-backends dependency, since it is automatically
  found by rpm.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 0.83-2
- automated rebuild

* Tue Jan  8 2002 Tim Waugh <twaugh@redhat.com> 0.83-1
- 0.83.

* Tue Dec 11 2001 Tim Waugh <twaugh@redhat.com> 0.82-3.1
- 0.82.
- Some extra patches from Oliver Rauch.
- Require sane not sane-backends since it's available throughout 7.x.
- Built for Red Hat Linux 7.1, 7.2.

* Tue Jul 24 2001 Tim Waugh <twaugh@redhat.com> 0.77-4
- Build requires libpng-devel, libjpeg-devel (#bug 49760).

* Tue Jul 17 2001 Preston Brown <pbrown@redhat.com> 0.77-3
- add an icon to the desktop entry

* Tue Jun 19 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add ExcludeArch: s390 s390x

* Mon Jun 11 2001 Tim Waugh <twaugh@redhat.com> 0.77-1
- 0.77.

* Sun Jun  3 2001 Tim Waugh <twaugh@redhat.com> 0.76-2
- Require sane-backends, not all of sane.

* Wed May 23 2001 Tim Waugh <twaugh@redhat.com> 0.76-1
- 0.76.

* Thu May  3 2001 Tim Waugh <twaugh@redhat.com> 0.75-1
- 0.75
- Fix summary/description to match specspo.

* Mon Jan  8 2001 Matt Wilson <msw@redhat.com>
- fix post script of gimp subpackage to install into the correct location

* Mon Dec 25 2000 Matt Wilson <msw@redhat.com>
- rebuilt against gimp 1.2.0

* Thu Dec 21 2000 Matt Wilson <msw@redhat.com>
- rebuilt against gimp 1.1.32
- use -DGIMP_ENABLE_COMPAT_CRUFT=1 to build with compat macros

* Thu Oct 12 2000 Than Ngo <than@redhat.com>
- 0.62

* Wed Aug 23 2000 Matt Wilson <msw@redhat.com>
- rebuilt against gimp-1.1.25

* Mon Aug 07 2000 Than Ngo <than@redhat.de>
- added swedish translation (Bug #15316)

* Fri Aug 4 2000 Than Ngo <than@redhat.de>
- fix, shows error dialogbox if no scanner exists (Bug #15445)
- update to 0.61

* Wed Aug  2 2000 Matt Wilson <msw@redhat.com>
- rebuilt against new libpng

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul  3 2000 Matt Wilson <msw@redhat.com>
- rebuilt against gimp 1.1.24
- make clean before building non gimp version

* Fri Jun 30 2000 Preston Brown <pbrown@redhat.com>
- made gimp subpkg

* Wed Jun 14 2000 Preston Brown <pbrown@redhat.com>
- desktop entry added

* Tue Jun 13 2000 Preston Brown <pbrown@redhat.com>
- fixed gimp link
- FHS paths

* Tue May 30 2000 Karsten Hopp <karsten@redhat.de>
- update to 0.59

* Sat Jan 29 2000 TIm Powers <timp@redhat.com>
- fixed bug 8948

* Thu Dec 2 1999 Tim Powers <timp@redhat.com>
- updated to 0.47
- gzip man pages

* Mon Aug 30 1999 Tim Powers <timp@redhat.com>
- changed group

* Mon Jul 26 1999 Tim Powers <timp@redhat.com>
- update to 0.30
- added %%defattr
- built for 6.1

* Thu Apr 22 1999 Preston Brown <pbrown@redhat.com>
- initial RPM for PowerTools 6.0
