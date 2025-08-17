# No releases have been tagged on github, so we use a git checkout
%global commit  1d6759ec9771fbc6bdc71ec79b7a5a28711cd9fd
%global date    20190630
%global forgeurl https://github.com/geomview/geomview

# brp-compress compresses the png files in the infodir; compress manually
%global __brp_compress %{nil}

Name:           geomview
Summary:        Interactive 3D viewing program
Version:        1.9.5

%forgemeta

# LGPL-2.0-or-later: the project as a whole
# GPL-2.0-or-later:
# - src/bin/crayola/Crayola
# - src/bin/geomutil/math2oogl/OOGL.m
# - src/bin/labeler/Labeler
# - src/bin/nose/nose.c
# - src/lib/oogl/util/dbllist.h
# - src/lib/oogl/util/freelist.h
# - src/lib/oogl/util/iobuffer.{c,h}
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Release:        %autorelease
URL:            http://www.geomview.org/
VCS:            git:%{forgeurl}.git
Source0:        %{forgesource}
# app.desktop
Source1:        org.geomview.geomview.desktop
# metainfo
Source2:        org.geomview.geomview.metainfo.xml
# mime
Source10:       application_x-geomview.xml
#icons
Source20:       hi16-app-geomview.png
Source21:       hi22-app-geomview.png
Source22:       hi32-app-geomview.png
Source23:       hi48-app-geomview.png
Source24:       hi64-app-geomview.png
Source25:       hi128-app-geomview.png
Source26:       hisc-app-geomview.svg
# Update the autoconf files
Patch:          %{forgeurl}/pull/2.patch
# Modernize the C code to avoid a host of errors
Patch:          %{forgeurl}/pull/3.patch
# Fix a memset that doesn't set enough
Patch:          %{forgeurl}/pull/4.patch
# Fix texinfo errors
Patch:          %{forgeurl}/pull/5.patch
# Fedora-only change: link with zlib-ng instead of zlib
Patch:          %{name}-zlib-ng.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gzip
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  motif-devel
BuildRequires:  netpbm-progs
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  xdg-utils

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gzip
Requires:       netpbm-progs
Requires:       xdg-utils

%description
Geomview is an interactive 3D viewing program for Unix. It lets you view and
manipulate 3D objects: you use the mouse to rotate, translate, zoom in and out,
etc. It can be used as a standalone viewer for static objects or as a display
engine for other programs which produce dynamically changing geometry. It can
display objects described in a variety of file formats. It comes with a wide
selection of example objects, and you can create your own objects too.

%package        libs
Summary:        Geomview runtime libraries

%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%prep
%forgeautosetup -p1

%conf
# Fix a shebang
sed -i '1s,:,#!%{_bindir}/perl,' src/bin/geomutil/hvectext/hvectext.in

# Generate the configure script
autoreconf -fi .

%build
%configure \
  --enable-shared \
  --disable-static \
  --with-htmlbrowser=xdg-open \
  --with-pdfviewer=xdg-open \

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

# .desktop entry
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# metainfo
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/org.geomview.geomview.metainfo.xml

# mime
install -p -m644 -D %{SOURCE10} %{buildroot}%{_datadir}/mime/packages/x-geomview.xml

# app icons
install -p -m644 -D %{SOURCE20} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/geomview.png
install -p -m644 -D %{SOURCE21} %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/geomview.png
install -p -m644 -D %{SOURCE22} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/geomview.png
install -p -m644 -D %{SOURCE23} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/geomview.png
install -p -m644 -D %{SOURCE24} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/geomview.png
install -p -m644 -D %{SOURCE25} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/geomview.png
install -p -m644 -D %{SOURCE26} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/geomview.svg

# Unpackaged files
rm -fv %{buildroot}%{_infodir}/dir

# Fix the info file names
for f in %{buildroot}%{_infodir}/geomview*; do
  mv $f $f.info
done

# See note above about brp-compress
gzip -9v \
     %{buildroot}%{_infodir}/*.info \
     %{buildroot}%{_mandir}/man1/* \
     %{buildroot}%{_mandir}/man3/* \
     %{buildroot}%{_mandir}/man5/* \

# Deduplicate
%fdupes %{buildroot}%{_prefix}

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/anytooff
%{_bindir}/anytoucd
%{_bindir}/bdy
%{_bindir}/bez2mesh
%{_bindir}/clip
%{_bindir}/geomview
%{_bindir}/hvectext
%{_bindir}/math2oogl
%{_bindir}/offconsol
%{_bindir}/oogl2rib
%{_bindir}/oogl2vrml
%{_bindir}/oogl2vrml2
%{_bindir}/polymerge
%{_bindir}/remotegv
%{_bindir}/togeomview
%{_bindir}/ucdtooff
%{_bindir}/vrml2oogl
%{_docdir}/geomview/OOGL.m.txt
%{_docdir}/geomview/README.gvplot
%{_docdir}/geomview/geomview.pdf
%{_docdir}/geomview/geomview-pt_BR.pdf
%{_docdir}/geomview/html/
%{_datadir}/applications/org.geomview.geomview.desktop
%{_datadir}/geomview/
%{_datadir}/icons/hicolor/16x16/apps/geomview.png
%{_datadir}/icons/hicolor/22x22/apps/geomview.png
%{_datadir}/icons/hicolor/32x32/apps/geomview.png
%{_datadir}/icons/hicolor/48x48/apps/geomview.png
%{_datadir}/icons/hicolor/64x64/apps/geomview.png
%{_datadir}/icons/hicolor/128x128/apps/geomview.png
%{_datadir}/icons/hicolor/scalable/apps/geomview.svg
%{_datadir}/mime/packages/x-geomview.xml
%{_infodir}/figs/
%{_infodir}/geomview*
%{_mandir}/man1/animate.1gv*
%{_mandir}/man1/anytooff.1gv*
%{_mandir}/man1/anytoucd.1gv*
%{_mandir}/man1/bdy.1gv*
%{_mandir}/man1/bez2mesh.1gv*
%{_mandir}/man1/clip.1gv*
%{_mandir}/man1/geomview.1gv*
%{_mandir}/man1/hvectext.1gv*
%{_mandir}/man1/math2oogl.1gv*
%{_mandir}/man1/nose.1gv*
%{_mandir}/man1/offconsol.1gv*
%{_mandir}/man1/oogl2rib.1gv*
%{_mandir}/man1/oogl2vrml.1gv*
%{_mandir}/man1/polymerge.1gv*
%{_mandir}/man1/togeomview.1gv*
%{_mandir}/man1/ucdtooff.1gv*
%{_mandir}/man1/vrml2oogl.1gv*
%{_mandir}/man3/anytopl.3gv*
%{_mandir}/man3/bdy.3gv*
%{_mandir}/man3/fsaparse.3gv*
%{_mandir}/man3/geomutil.3gv*
%{_mandir}/man3/lisp.3gv*
%{_mandir}/man3/plcombine.3gv*
%{_mandir}/man3/plconsol.3gv*
%{_mandir}/man5/discgrp.5gv*
%{_mandir}/man5/geomview.5gv*
%{_mandir}/man5/oogl.5gv*
%{_libexecdir}/geomview/
%{_metainfodir}/org.geomview.geomview.metainfo.xml

%files libs
%{_libdir}/libgeomview-1.9.5.so

%files devel
%{_libdir}/libgeomview.so
%{_includedir}/geomview/

%changelog
%autochangelog
