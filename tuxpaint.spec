Name:           tuxpaint
Version:        0.9.28
Release:        3%{?dist}

Epoch:          1
Summary:        Drawing program designed for young children

License:        GPLv2+
URL:            http://www.tuxpaint.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-sdl2.tar.gz
Patch1:         tuxpaint-0.9.21-fix-desktop-file.patch
Patch2:         tuxpaint-0.9.21-makej.patch
Patch3:         desktop.patch
Patch4:         sdl2.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  SDL2_gfx-devel
BuildRequires:  SDL2_Pango-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel >= 2.0
BuildRequires:  gettext
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  netpbm-devel
BuildRequires:	fribidi-devel
BuildRequires:	gperf
BuildRequires:  ImageMagick
BuildRequires:  libimagequant-devel
BuildRequires:  xdg-utils

# This should guarantee the proper permissions on
# all of the /usr/share/icons/hicolor/* directories.
Requires:       hicolor-icon-theme

%description
"Tux Paint" is a free drawing program designed for young children
(kids ages 3 and up). It has a simple, easy-to-use interface,
fun sound effects, and a cartoon mascot who helps you along.

%package devel
Summary:	Development files for tuxpaint extensions/plugins
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files for tuxpaint extensions/plugins

%prep
%setup -qn %{name}-%{version}-sdl2
%patch1 -p0 -b .fixdesktopfile
%patch2 -p1 -b .makej
%patch3 -p0 -b .desktop
%patch4 -p0 -b .sdl2

sed -i -e '/\/gnome\/apps\/Graphics/d' Makefile
find docs -type f -exec perl -pi -e 's/\r\n/\n/' {} \;
find docs -type f -perm /100 -exec chmod a-x {} \;

make PREFIX=/usr MAGIC_PREFIX=%{_libdir}/tuxpaint/plugins tp-magic-config

%build
make %{?_smp_mflags} \
    PREFIX=/usr \
    CFLAGS="$RPM_OPT_FLAGS -I/usr/include/freetype2" \
    MAGIC_PREFIX=%{_libdir}/tuxpaint/plugins

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
make install PKG_ROOT=$RPM_BUILD_ROOT PREFIX=%{_usr} \
    X11_ICON_PREFIX=$RPM_BUILD_ROOT%{_datadir}/pixmaps/ \
    GNOME_PREFIX=/usr \
    KDE_PREFIX="" \
    KDE_ICON_PREFIX=/usr/share/icons \
    MAGIC_PREFIX=$RPM_BUILD_ROOT%{_libdir}/tuxpaint/plugins
find $RPM_BUILD_ROOT -type d|xargs chmod 0755
%find_lang %{name}

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
    --add-category KidsGame \
    --delete-original \
    src/tuxpaint.desktop

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
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://sourceforge.net/p/tuxpaint/feature-requests/172/
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">tuxpaint.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A drawing program for children</summary>
  <description>
    <p>
      Tux Paint is a free, award-winning drawing program for children ages 3 to
      12.
      Tux Paint is used in schools around the world as a computer literacy
      drawing activity.
      It combines an easy-to-use interface, fun sound effects, and an
      encouraging cartoon mascot who guides children as they use the program.
    </p>
    <p>
      Kids are presented with a blank canvas and a variety of drawing tools to
      help them be creative.
    </p>
  </description>
  <url type="homepage">http://tuxpaint.org/</url>
  <screenshots>
    <screenshot type="default">http://tuxpaint.org/screenshots/starter-coloringbook.png</screenshot>
    <screenshot>http://tuxpaint.org/screenshots/example_simple.png</screenshot>
    <screenshot>http://tuxpaint.org/screenshots/example_space.png</screenshot>
  </screenshots>
  <updatecontact>tuxpaint-devel@lists.sourceforge.net</updatecontact>
</application>
EOF

#purge bundled fonts
rm -rf $RPM_BUILD_ROOT%{_datadir}/tuxpaint/fonts/*

ln -s ../../fonts/dejavu-sans-fonts/DejaVuSans.ttf %{buildroot}/usr/share/tuxpaint/fonts/default_font.ttf

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%files -f %{name}.lang
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%doc docs
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_libdir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%{_sysconfdir}/bash_completion.d/tuxpaint-completion.bash

%files devel
%doc %{_datadir}/doc/%{name}-%{version}/
%{_includedir}/tuxpaint/

%changelog
* Tue Sep 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:0.9.28-3
- Build with SDL2_Pango

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:0.9.28-1
- 0.9.28

* Wed Apr 20 2022 Sérgio Basto <sergio@serjux.com> - 1:0.9.27-3
- Remove BR kdelibs as part of the plan of remove kde4

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:0.9.27-1
- 0.9.27

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:0.9.26-1
- 0.9.26

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:0.9.25-1
- 0.9.25

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:0.9.24-1
- 0.9.24

* Wed Feb 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:0.9.23-1
- 0.9.23

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Colin B. Macdonald <cbm@m.fsf.org> - 1:0.9.22-9
- Add dependency on gcc, gcc-c++ (see #1551327)
- Replace unversioned python calls with python2 (see #1585626)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Jon Ciesla <limburgher@gmail.com> - 1:0.9.22-2
- Drop bundled fonts, BZ 477471.

* Thu Jan 07 2016 Jon Ciesla <limburgher@gmail.com> - 1:0.9.22-1
- 0.9.22.
- Fixed bogus changelog dates.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:0.9.21-15
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Ralf Corsépius <corsepiu@fedoraproject.org> -  1:0.9.21-12
- Use find -perm /<mode> instead of obsolete +<mode> (FTBFS, RHBZ#992825).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 1:0.9.21-10
- Drop desktop vendor tag.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Tom Callaway <spot@fedoraproject.org> - 1:0.9.21-8
- fix compile against libpng15

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1:0.9.21-6
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1:0.9.21-4
- recompiling .py files against Python 2.7 (rhbz#623414)

* Wed Mar 3 2010 Lubomir Rintel <lkundrak@v3.sk> - 1:0.9.21-3
- Fix link with new linker
- Fix incorrect memset() arguments
- Fix parallel build

* Thu Nov 19 2009 Jon Ciesla <limb@jcomserv.net> - 1:0.9.21-2
- Corrected icon requires, BZ 533965.

* Fri Oct 23 2009 Jon Ciesla <limb@jcomserv.net> - 1:0.9.21-1
- New upstream.
- Corrected desktop patch.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:0.9.20-2
- Rebuild for Python 2.6

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.9.20-1
- update to 0.9.20

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.9.17-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.9.17-3
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1:0.9.17-2
- Rebuild for selinux ppc32 issue.

* Sat Jul 07 2007 Steven Pritchard <steve@kspei.com> 1:0.9.17-1
- Update to 0.9.17.
- BR librsvg2-devel and libpaper-devel.
- Add include path for glibconfig.h to CFLAGS.

* Tue Jan 30 2007 Steven Pritchard <steve@kspei.com> 1:0.9.16-4
- Honor $RPM_OPT_FLAGS.
- Fix various rpmlint warnings:
  - Expand tabs in spec.
  - Convert tuxpaint.1 to UTF-8.
  - Get rid of DOS line endings in docs.
  - Nothing in docs should be executable.

* Fri Oct 27 2006 Steven Pritchard <steve@kspei.com> 1:0.9.16-3
- Fix category in tuxpaint.desktop.

* Thu Oct 26 2006 Steven Pritchard <steve@kspei.com> 1:0.9.16-2
- Drop "--add-category X-Fedora".

* Tue Oct 24 2006 Steven Pritchard <steve@kspei.com> 1:0.9.16-1
- Update to 0.9.16.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9.15b-4
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Steven Pritchard <steve@kspei.com> 1:0.9.15b-3
- Explicitly link libpng.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 1:0.9.15b-2
- Rebuild.
- Update URL.

* Fri Jun 02 2006 Steven Pritchard <steve@kspei.com> 1:0.9.15b-1
- Update to 0.9.15b
- Convert tuxpaint.desktop to UTF-8
- Drop gnome-libs-devel and kdelibs build dependencies by providing
  appropriate variables to "make install"
- Add docs properly
- Indirectly require hicolor-icon-theme (so that directories are
  owned and have proper permissions)

* Mon Mar 13 2006 Steven Pritchard <steve@kspei.com> 1:0.9.15-1
- Update to 0.9.15
- Drop destdir patch

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1:0.9.13-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Jun 09 2004 Warren Togami <wtogami@redhat.com> 1:0.9.13-0.fdr.1
- Epoch bump to override old k12ltsp package

* Mon May 31 2004 Panu Matilainen <pmatilai@welho.com> 0:0.9.13-0.fdr.1
- update to 0.9.13
- take a private copy of desktop file and fix it..

* Sun May 30 2004 Panu Matilainen <pmatilai@welho.com> 0:0.9.12-0.fdr.3
- add missing buildrequires desktop-file-utils (#1667)

* Fri Oct 03 2003 Panu Matilainen <pmatilai@welho.com> 0:0.9.12-0.fdr.2
- add missing buildreq's: kdelibs, gnome-libs-devel, SDL_mixer-devel
- remove CVS directories from rpm

* Tue Aug 26 2003 Panu Matilainen <pmatilai@welho.com> 0:0.9.12-0.fdr.1
- Initial RPM release.
