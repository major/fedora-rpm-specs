%if ! 0%{?fedora} || 0%{?fedora} >= 41
%bcond gimp 0
%bcond pixbuf_extra_modules 1
%else
%bcond gimp 1
%bcond pixbuf_extra_modules 0
%endif

# if you rebuild, please change bugtracker_url accordingly:
%global bugtracker_url https://bugzilla.redhat.com

%if %{with gimp}
%global gimpplugindir %(%___build_pre; gimptool --gimpplugindir 2>/dev/null || echo INVALID)/plug-ins
%endif
%global iconrootdir %{_datadir}/icons/hicolor

# needed for off-root building
%global _configure ../configure

Name: xsane
Summary: X Window System front-end for the SANE scanner interface
Version: 0.999
Release: %{autorelease}
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
# https://gitlab.com/sane-project/frontend/xsane/-/commit/96424e369f67
Patch16: 0001-Follow-new-convention-for-registering-gimp-plugin.patch
# https://gitlab.com/sane-project/frontend/xsane/-/commit/bf9ef48ab57
Patch17: 0001-replace-gtk_timeout-with-g_timeout.patch
# https://gitlab.com/sane-project/frontend/xsane/-/merge_requests/32
Patch18: xsane-gcc15-c23.patch

# autoconf-generated files
Patch100: xsane-0.999-7-autoconf.patch.bz2

Patch101: xsane-configure-c99.patch

# LGPL-3.0-or-later is due of using gimp libraries
# src/* - GPL2+
# lib/* (copies from glibc) - LGPL2+
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL: http://www.xsane.org/

# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses make
BuildRequires: make
%if %{with gimp}
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
%if %{with pixbuf_extra_modules}
Requires: gdk-pixbuf2-modules-extra%{?_isa}
%endif
%if %{without gimp}
Obsoletes: xsane-gimp < %{version}-%{release}
%endif

%description
XSane is an X based interface for the SANE (Scanner Access Now Easy)
library, which provides access to scanners, digital cameras, and other
capture devices. XSane is written in GTK+ and provides control for
performing the scan and then manipulating the captured image.

%if %{with gimp}
%package gimp
Summary: GIMP plug-in providing the SANE scanner interface
Requires: gimp >= 2:2.2.12-4
Requires: xsane-common
%if %{with pixbuf_extra_modules}
Requires: gdk-pixbuf2-modules-extra%{?_isa}
%endif

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
%patch -P 16 -p1 -b .use-register
%patch -P 17 -p1 -b .replace-gtk-timeout
%patch -P 18 -p1 -b .gcc15-c23

%patch -P 100 -p1 -b .autoconf
%patch -P 101 -p1 -b .c99

# in-root config.h breaks off-root building
rm include/config.h

mkdir build-with-gimp
mkdir build-without-gimp

%build
CFLAGS='%optflags -fno-strict-aliasing -DXSANE_BUGTRACKER_URL=\"%{bugtracker_url}\"'
export CFLAGS

%if %{with gimp}
pushd build-with-gimp
%configure --enable-gimp
if grep -Fq '#undef HAVE_ANY_GIMP' include/config.h; then
    echo "The configure script didn’t detect GIMP" >&2
    exit 1
fi
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

%if %{with gimp}
# install GIMP plugin
install -m 0755 -d %{buildroot}%{gimpplugindir}
install -m 0755 build-with-gimp/src/xsane %{buildroot}%{gimpplugindir}/%{name}
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

%files -f XSANE.lang
%doc xsane.ACCELKEYS xsane.AUTHOR xsane.BEGINNERS-INFO xsane.BUGS xsane.CHANGES xsane.FAQ xsane.LANGUAGES xsane.LOGO xsane.NEWS xsane.ONLINEHELP xsane.PROBLEMS xsane.ROOT xsane.TODO
%license xsane.COPYING
%{_bindir}/xsane
%{_mandir}/man1/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/xsane.desktop
%{_datadir}/pixmaps/xsane.xpm
%{iconrootdir}/*/apps/%{name}.png

%if %{with gimp}
%files gimp
%{gimpplugindir}/%{name}
%endif

%files common
%doc xsane.AUTHOR
%license xsane.COPYING
%dir %{_datadir}/sane
%{_datadir}/sane/xsane

%changelog
%autochangelog
