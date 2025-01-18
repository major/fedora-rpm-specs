# Copyright (c) 2005 - 2020 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

# GStreamer support: Default on
%bcond_without  gstreamer

# GDal support: Default on
%bcond_without  gdal

# Inventor support: Default to Coin4
# These are mutually exclusive
%if 0%{?fedora}
%bcond_with     Inventor
%bcond_without  Coin4
%else
%bcond_with  Inventor
%bcond_with  Coin4
%endif

# Jasper support: Default on
%bcond_without  jasper

# OpenEXR support: Default on
%bcond_without  OpenEXR

# Collada support: Default on
%bcond_without  Collada

# Build wxWidgets example: Default on
%if 0%{?fedora}
%bcond_without wxWidgets
%else
%bcond_with wxWidgets
%endif

%if 0%{?fedora}
%bcond_without mingw
%else
%bcond_with mingw
%endif

Name:           OpenSceneGraph
Version:        3.6.5
Release:        32%{?dist}
Summary:        High performance real-time graphics toolkit

# The OSGPL is just the wxWidgets license.
License:        GPL-2.0-or-later WITH WxWindows-exception-3.1
URL:            http://www.openscenegraph.org/
Source0:        https://github.com/openscenegraph/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

Patch1:         0001-Cmake-fixes.patch
# Upstream deactivated building osgviewerWX for obscure reasons
# Reactivate for now.
Patch2:         0002-Activate-osgviewerWX.patch
# Unset DOT_FONTNAME
Patch3:         0003-Unset-DOT_FONTNAME.patch
# Re-add osgframerenderer
Patch4:         0004-Re-add-osgframerenderer.patch
# Force osgviewerWX to always use X11 backend (wxGLCanvas is broken on Wayland)
Patch5:         force-x11-backend.patch
# Minimal port to OpenEXR 3
# https://github.com/openscenegraph/OpenSceneGraph/issues/1075
Patch6:         OpenSceneGraph-openexr3.patch
# Fix build against recent asio
Patch7:         OpenSceneGraph_asio.patch
# Fix mingw build (symbol collision due to namespace ordering, narrowing conversion error)
Patch8:         OpenSceneGraph_mingw.patch
# Fix linking against gta
Patch9:         OpenSceneGraph_gta.patch

BuildRequires:  asio-devel
BuildRequires:  cmake
BuildRequires:  doxygen graphviz
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  gnuplot
BuildRequires:  libcurl-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblas-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvncserver-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXmu-devel
BuildRequires:  libX11-devel
BuildRequires:  make
BuildRequires:  openal-soft-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gta)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-x11-1.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.35
BuildRequires:  pkgconfig(xrandr)

# Used by osgmovie
BuildRequires:  SDL2-devel
# Used by SDL-examples
BuildRequires:  SDL-devel

# Optional
%{?with_OpenEXR:BuildRequires:    cmake(OpenEXR)}
%{?with_Collada:BuildRequires:    pkgconfig(collada-dom)}
%{?with_jasper:BuildRequires:     jasper-devel}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-base-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-app-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-audio-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-fft-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-video-1.0)}
%{?with_gdal:BuildRequires:       gdal-devel}
%{?with_Inventor:BuildRequires:   Inventor-devel}
%{?with_Coin4:BuildRequires:      Coin4-devel}
%{?with_wxWidgets:BuildRequires:  wxGTK-devel}

%if %{with mingw}
BuildRequires: mingw32-cairo
BuildRequires: mingw32-curl
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libpng
BuildRequires: mingw32-librsvg2
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-openal-soft
BuildRequires: mingw32-poppler-glib

# Optional
%{?with_OpenEXR:BuildRequires:    mingw32-openexr}
%{?with_jasper:BuildRequires:     mingw32-jasper}
%{?with_gstreamer:BuildRequires:  mingw32-gstreamer1}
%{?with_gdal:BuildRequires:       mingw32-gdal}

BuildRequires: mingw64-cairo
BuildRequires: mingw64-curl
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libpng
BuildRequires: mingw64-librsvg2
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-openal-soft
BuildRequires: mingw64-poppler-glib

# Optional
%{?with_OpenEXR:BuildRequires:    mingw64-openexr}
%{?with_jasper:BuildRequires:     mingw64-jasper}
%{?with_gstreamer:BuildRequires:  mingw64-gstreamer1}
%{?with_gdal:BuildRequires:       mingw64-gdal}
%endif

Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}


%description
The OpenSceneGraph is an OpenSource, cross platform graphics toolkit for the
development of high performance graphics applications such as flight
simulators, games, virtual reality and scientific visualization.
Based around the concept of a SceneGraph, it provides an object oriented
framework on top of OpenGL freeing the developer from implementing and
optimizing low level graphics calls, and provides many additional utilities
for rapid development of graphics applications.


%package libs
Summary:        Runtime libraries for OpenSceneGraph

%description libs
Runtime libraries files for OpenSceneGraph.


%if %{with gdal}
%package gdal
Summary:        OSG Gdal plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}

%description gdal
OSG Gdal plugin.
%endif


%if %{with Collada}
%package Collada
Summary:        OSG Collada plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}

%description Collada
OSG Collada plugin.
%endif

%if %{with OpenEXR}
%package OpenEXR
Summary:        OSG OpenEXR plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}

%description OpenEXR
OSG OpenEXR plugin.
%endif

%if %{with gstreamer}
%package gstreamer
Summary:        OSG gstreamer plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}

%description gstreamer
OSG gstreamer plugin.
%endif


%if %{with Inventor}
%package inventor
Summary:        OSG inventor plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}

%description inventor
OSG inventor plugin.
%endif


%package devel
Summary:        Development files for OpenSceneGraph
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}
Requires:       OpenThreads-devel%{?_isa} = %{version}-%{release}

%description devel
Development files for OpenSceneGraph.


%package examples
Summary:        Sample applications for OpenSceneGraph

%description examples
Sample applications for OpenSceneGraph


%package examples-SDL
Summary:        OSG sample applications using SDL

%description examples-SDL
OSG sample applications using SDL.


%package examples-fltk
Summary:        OSG sample applications using FLTK

%description examples-fltk
OSG sample applications using FLTK.


%package examples-gtk
Summary:        OSG sample applications using gtk

%description examples-gtk
OSG sample applications using gtk


%package -n OpenThreads
Summary:        OpenThreads

%description -n OpenThreads
OpenThreads is intended to provide a minimal & complete Object-Oriented (OO)
thread interface for C++ programmers.  It is loosely modeled on the Java
thread API, and the POSIX Threads standards.  The architecture of the
library is designed around "swappable" thread models which are defined at
compile-time in a shared object library.


%package -n OpenThreads-devel
Summary:        Devel files for OpenThreads
Requires:       OpenThreads%{?_isa} = %{version}-%{release}

%description -n OpenThreads-devel
Development files for OpenThreads.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%package -n mingw32-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}-tools
Tools for the MinGW Windows %{name} library.


%package -n mingw64-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}-tools
Tools for the MinGW Windows %{name} library.
%endif


%{?mingw_debug_package}

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}%{?pre:-%pre}

# Also look in /usr/share/fonts for fonts
sed -i -e 's,\.:/usr/share/fonts/ttf:,.:%{_datadir}/fonts:/usr/share/fonts/ttf:,' \
src/osgText/Font.cpp

iconv -f ISO-8859-1 -t utf-8 AUTHORS.txt > AUTHORS.txt~
mv AUTHORS.txt~ AUTHORS.txt

# Update doxygen
doxygen -u doc/Doxyfiles/doxyfile.cmake
doxygen -u doc/Doxyfiles/openthreads.doxyfile.cmake


%build
# Native build
%cmake -DBUILD_OSG_EXAMPLES=ON -DBUILD_DOCUMENTATION=ON \
  -DOSG_AGGRESSIVE_WARNING_FLAGS=OFF \
  -DLIB_POSTFIX=%(l=%{_lib}; echo ${l:3}) \
  %{?with_Collada:-DCOLLADA_INCLUDE_DIR=$(pkg-config collada-dom --variable=includedir)}
%cmake_build

make -C %{_vpath_builddir} doc_openscenegraph doc_openthreads

# MinGW build
# We are cross-compiling and TryRun fails
%if %{with mingw}
%mingw_cmake \
  -DOSG_AGGRESSIVE_WARNING_FLAGS=OFF \
  -DOSG_DETERMINE_WIN_VERSION=OFF
%mingw_make_build
%endif


%install
%cmake_install
# Supposed to take OpenSceneGraph data
mkdir -p %{buildroot}%{_datadir}/OpenSceneGraph

%if %{with mingw}
%mingw_make_install

%mingw_debug_install_post

%endif


%files
%{_bindir}/osgarchive
%{_bindir}/osgconv
%{_bindir}/osgversion
%{_bindir}/osgviewer
%{_bindir}/osgfilecache
%{_bindir}/present3D

%files libs
%doc AUTHORS.txt NEWS.txt README.md
%license LICENSE.txt
%dir %{_libdir}/osgPlugins-%{version}
%{_libdir}/osgPlugins-%{version}/osgdb_3dc.so
%{_libdir}/osgPlugins-%{version}/osgdb_3ds.so
%{_libdir}/osgPlugins-%{version}/osgdb_ac.so
%{_libdir}/osgPlugins-%{version}/osgdb_bmp.so
%{_libdir}/osgPlugins-%{version}/osgdb_bsp.so
%{_libdir}/osgPlugins-%{version}/osgdb_bvh.so
%{_libdir}/osgPlugins-%{version}/osgdb_cfg.so
%{_libdir}/osgPlugins-%{version}/osgdb_curl.so
%{_libdir}/osgPlugins-%{version}/osgdb_dds.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osg.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osganimation.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgfx.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgparticle.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgshadow.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgsim.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgterrain.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgtext.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgviewer.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgvolume.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgwidget.so
%{_libdir}/osgPlugins-%{version}/osgdb_dot.so
%{_libdir}/osgPlugins-%{version}/osgdb_dxf.so
%{_libdir}/osgPlugins-%{version}/osgdb_freetype.so
%{_libdir}/osgPlugins-%{version}/osgdb_gif.so
%{_libdir}/osgPlugins-%{version}/osgdb_gles.so
%{_libdir}/osgPlugins-%{version}/osgdb_glsl.so
%{_libdir}/osgPlugins-%{version}/osgdb_gta.so
%{_libdir}/osgPlugins-%{version}/osgdb_gz.so
%{_libdir}/osgPlugins-%{version}/osgdb_hdr.so
%{_libdir}/osgPlugins-%{version}/osgdb_ive.so
%{?with_jasper:%{_libdir}/osgPlugins-%{version}/osgdb_jp2.so}
%{_libdir}/osgPlugins-%{version}/osgdb_jpeg.so
%{_libdir}/osgPlugins-%{version}/osgdb_ktx.so
%{_libdir}/osgPlugins-%{version}/osgdb_las.so
%{_libdir}/osgPlugins-%{version}/osgdb_logo.so
%{_libdir}/osgPlugins-%{version}/osgdb_lua.so
%{_libdir}/osgPlugins-%{version}/osgdb_lwo.so
%{_libdir}/osgPlugins-%{version}/osgdb_lws.so
%{_libdir}/osgPlugins-%{version}/osgdb_md2.so
%{_libdir}/osgPlugins-%{version}/osgdb_mdl.so
%{_libdir}/osgPlugins-%{version}/osgdb_normals.so
%{_libdir}/osgPlugins-%{version}/osgdb_obj.so
%{_libdir}/osgPlugins-%{version}/osgdb_openflight.so
%{_libdir}/osgPlugins-%{version}/osgdb_osc.so
%{_libdir}/osgPlugins-%{version}/osgdb_osg.so
%{_libdir}/osgPlugins-%{version}/osgdb_osga.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgjs.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgshadow.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgterrain.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgtgz.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgviewer.so
%{_libdir}/osgPlugins-%{version}/osgdb_p3d.so
%{_libdir}/osgPlugins-%{version}/osgdb_pdf.so
%{_libdir}/osgPlugins-%{version}/osgdb_pic.so
%{_libdir}/osgPlugins-%{version}/osgdb_ply.so
%{_libdir}/osgPlugins-%{version}/osgdb_png.so
%{_libdir}/osgPlugins-%{version}/osgdb_pnm.so
%{_libdir}/osgPlugins-%{version}/osgdb_pov.so
%{_libdir}/osgPlugins-%{version}/osgdb_pvr.so
%{_libdir}/osgPlugins-%{version}/osgdb_resthttp.so
%{_libdir}/osgPlugins-%{version}/osgdb_revisions.so
%{_libdir}/osgPlugins-%{version}/osgdb_rgb.so
%{_libdir}/osgPlugins-%{version}/osgdb_rot.so
%{_libdir}/osgPlugins-%{version}/osgdb_scale.so
%{_libdir}/osgPlugins-%{version}/osgdb_sdl.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osg.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osganimation.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgfx.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgga.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgmanipulator.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgparticle.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgshadow.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgsim.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgterrain.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgtext.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgui.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgutil.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgviewer.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgvolume.so
%{_libdir}/osgPlugins-%{version}/osgdb_shp.so
%{_libdir}/osgPlugins-%{version}/osgdb_stl.so
%{_libdir}/osgPlugins-%{version}/osgdb_svg.so
%{_libdir}/osgPlugins-%{version}/osgdb_tf.so
%{_libdir}/osgPlugins-%{version}/osgdb_tga.so
%{_libdir}/osgPlugins-%{version}/osgdb_tgz.so
%{_libdir}/osgPlugins-%{version}/osgdb_tiff.so
%{_libdir}/osgPlugins-%{version}/osgdb_trans.so
%{_libdir}/osgPlugins-%{version}/osgdb_trk.so
%{_libdir}/osgPlugins-%{version}/osgdb_txf.so
%{_libdir}/osgPlugins-%{version}/osgdb_txp.so
%{_libdir}/osgPlugins-%{version}/osgdb_vnc.so
%{_libdir}/osgPlugins-%{version}/osgdb_vtf.so
%{_libdir}/osgPlugins-%{version}/osgdb_x.so
%exclude %{_libdir}/osgPlugins-%{version}/osgdb_zip.so
%{_libdir}/libosgAnimation.so.*
%{_libdir}/libosgDB.so.*
%{_libdir}/libosgFX.so.*
%{_libdir}/libosgGA.so.*
%{_libdir}/libosgManipulator.so.*
%{_libdir}/libosgParticle.so.*
%{_libdir}/libosgPresentation.so.*
%{_libdir}/libosgShadow.so.*
%{_libdir}/libosgSim.so.*
%{_libdir}/libosg.so.*
%{_libdir}/libosgTerrain.so.*
%{_libdir}/libosgText.so.*
%{_libdir}/libosgUI.so.*
%{_libdir}/libosgUtil.so.*
%{_libdir}/libosgViewer.so.*
%{_libdir}/libosgVolume.so.*
%{_libdir}/libosgWidget.so.*

%if %{with gdal}
%files gdal
%{_libdir}/osgPlugins-%{version}/osgdb_gdal.so
%{_libdir}/osgPlugins-%{version}/osgdb_ogr.so
%endif

%if %{with Collada}
%files Collada
%{_libdir}/osgPlugins-%{version}/osgdb_dae.so
%endif

%if %{with OpenEXR}
%files OpenEXR
%{_libdir}/osgPlugins-%{version}/osgdb_exr.so
%endif

%if %{with gstreamer}
%files gstreamer
%{_libdir}/osgPlugins-%{version}/osgdb_gstreamer.so
%endif

%if %{with Inventor}
%files inventor
%{_libdir}/osgPlugins-%{version}/osgdb_iv.so
%endif

%files devel
%doc %{_vpath_builddir}/doc/OpenSceneGraphReferenceDocs
%{_includedir}/osg
%{_includedir}/osgAnimation
%{_includedir}/osgDB
%{_includedir}/osgFX
%{_includedir}/osgGA
%{_includedir}/osgManipulator
%{_includedir}/osgParticle
%{_includedir}/osgPresentation
%{_includedir}/osgShadow
%{_includedir}/osgSim
%{_includedir}/osgTerrain
%{_includedir}/osgText
%{_includedir}/osgUI
%{_includedir}/osgUtil
%{_includedir}/osgViewer
%{_includedir}/osgVolume
%{_includedir}/osgWidget
%{_libdir}/libosgAnimation.so
%{_libdir}/libosgDB.so
%{_libdir}/libosgFX.so
%{_libdir}/libosgGA.so
%{_libdir}/libosgManipulator.so
%{_libdir}/libosgParticle.so
%{_libdir}/libosgPresentation.so
%{_libdir}/libosgShadow.so
%{_libdir}/libosgSim.so
%{_libdir}/libosg.so
%{_libdir}/libosgTerrain.so
%{_libdir}/libosgText.so
%{_libdir}/libosgUI.so
%{_libdir}/libosgUtil.so
%{_libdir}/libosgViewer.so
%{_libdir}/libosgVolume.so
%{_libdir}/libosgWidget.so
%{_libdir}/pkgconfig/openscenegraph-osgAnimation.pc
%{_libdir}/pkgconfig/openscenegraph-osgDB.pc
%{_libdir}/pkgconfig/openscenegraph-osgFX.pc
%{_libdir}/pkgconfig/openscenegraph-osgGA.pc
%{_libdir}/pkgconfig/openscenegraph-osgManipulator.pc
%{_libdir}/pkgconfig/openscenegraph-osgParticle.pc
%{_libdir}/pkgconfig/openscenegraph-osg.pc
%{_libdir}/pkgconfig/openscenegraph-osgShadow.pc
%{_libdir}/pkgconfig/openscenegraph-osgSim.pc
%{_libdir}/pkgconfig/openscenegraph-osgTerrain.pc
%{_libdir}/pkgconfig/openscenegraph-osgText.pc
%{_libdir}/pkgconfig/openscenegraph-osgUtil.pc
%{_libdir}/pkgconfig/openscenegraph-osgViewer.pc
%{_libdir}/pkgconfig/openscenegraph-osgVolume.pc
%{_libdir}/pkgconfig/openscenegraph-osgWidget.pc
%{_libdir}/pkgconfig/openscenegraph.pc

%files examples
%{_bindir}/osg2cpp
%{_bindir}/osganalysis
%{_bindir}/osganimate
%{_bindir}/osganimationeasemotion
%{_bindir}/osganimationhardware
%{_bindir}/osganimationmakepath
%{_bindir}/osganimationmorph
%{_bindir}/osganimationnode
%{_bindir}/osganimationskinning
%{_bindir}/osganimationsolid
%{_bindir}/osganimationtimeline
%{_bindir}/osganimationviewer
%{_bindir}/osgatomiccounter
%{_bindir}/osgautocapture
%{_bindir}/osgautotransform
%{_bindir}/osgbillboard
%{_bindir}/osgbindlesstext
%{_bindir}/osgblenddrawbuffers
%{_bindir}/osgblendequation
%{_bindir}/osgcallback
%{_bindir}/osgcamera
%{_bindir}/osgcatch
%{_bindir}/osgclip
%{_bindir}/osgcluster
%{_bindir}/osgcompositeviewer
%{_bindir}/osgcomputeshaders
%{_bindir}/osgcopy
%{_bindir}/osgcubemap
%{_bindir}/osgdatabaserevisions
%{_bindir}/osgdeferred
%{_bindir}/osgdepthpartition
%{_bindir}/osgdepthpeeling
%{_bindir}/osgdistortion
%{_bindir}/osgdrawinstanced
%{_bindir}/osgfadetext
%{_bindir}/osgfont
%{_bindir}/osgforest
%{_bindir}/osgfpdepth
%{_bindir}/osgframerenderer
%{_bindir}/osgfxbrowser
%{_bindir}/osggameoflife
%{_bindir}/osggeometry
%{_bindir}/osggeometryshaders
%{_bindir}/osggpucull
%{_bindir}/osggpx
%{_bindir}/osggraphicscost
%{_bindir}/osghangglide
%{_bindir}/osghud
%{_bindir}/osgimagesequence
%{_bindir}/osgimpostor
%{_bindir}/osgintersection
%{_bindir}/osgkdtree
%{_bindir}/osgkeyboard
%{_bindir}/osgkeyboardmouse
%{_bindir}/osgkeystone
%{_bindir}/osglauncher
%{_bindir}/osglight
%{_bindir}/osglightpoint
%{_bindir}/osglogicop
%{_bindir}/osglogo
%{_bindir}/osgmanipulator
%{_bindir}/osgmemorytest
%{_bindir}/osgmotionblur
%{_bindir}/osgmovie
%{_bindir}/osgmultiplemovies
%{_bindir}/osgmultiplerendertargets
%{_bindir}/osgmultitexture
%{_bindir}/osgmultitexturecontrol
%{_bindir}/osgmultitouch
%{_bindir}/osgmultiviewpaging
%{_bindir}/osgobjectcache
%{_bindir}/osgoccluder
%{_bindir}/osgocclusionquery
%{_bindir}/osgoit
%{_bindir}/osgoscdevice
%{_bindir}/osgoutline
%{_bindir}/osgpackeddepthstencil
%{_bindir}/osgpagedlod
%{_bindir}/osgparametric
%{_bindir}/osgparticle
%{_bindir}/osgparticleeffects
%{_bindir}/osgparticleshader
%{_bindir}/osgpdf
%{_bindir}/osgphotoalbum
%{_bindir}/osgpick
%{_bindir}/osgplanets
%{_bindir}/osgpoints
%{_bindir}/osgpointsprite
%{_bindir}/osgposter
%{_bindir}/osgprecipitation
%{_bindir}/osgprerender
%{_bindir}/osgprerendercubemap
%{_bindir}/osgreflect
%{_bindir}/osgrobot
%{_bindir}/osgSSBO
%{_bindir}/osgsampler
%{_bindir}/osgscalarbar
%{_bindir}/osgscreencapture
%{_bindir}/osgscribe
%{_bindir}/osgsequence
%{_bindir}/osgshadercomposition
%{_bindir}/osgshadergen
%{_bindir}/osgshadermultiviewport
%{_bindir}/osgshaderpipeline
%{_bindir}/osgshaders
%{_bindir}/osgshaderterrain
%{_bindir}/osgshadow
%{_bindir}/osgshape
%{_bindir}/osgsharedarray
%{_bindir}/osgsidebyside
%{_bindir}/osgsimpleshaders
%{_bindir}/osgsimplegl3
%{_bindir}/osgsimpleMDI
%{_bindir}/osgsimplifier
%{_bindir}/osgsimulation
%{_bindir}/osgslice
%{_bindir}/osgspacewarp
%{_bindir}/osgspheresegment
%{_bindir}/osgspotlight
%{_bindir}/osgstereoimage
%{_bindir}/osgstereomatch
%{_bindir}/osgteapot
%{_bindir}/osgterrain
%{_bindir}/osgtessellate
%{_bindir}/osgtessellationshaders
%{_bindir}/osgtext
%{_bindir}/osgtext3D
%{_bindir}/osgtexture1D
%{_bindir}/osgtexture2D
%{_bindir}/osgtexture3D
%{_bindir}/osgtexture2DArray
%{_bindir}/osgtexturecompression
%{_bindir}/osgtexturerectangle
%{_bindir}/osgthirdpersonview
%{_bindir}/osgthreadedterrain
%{_bindir}/osgtransferfunction
%{_bindir}/osgtransformfeedback
%{_bindir}/osguniformbuffer
%{_bindir}/osgunittests
%{_bindir}/osguserdata
%{_bindir}/osguserstats
%{_bindir}/osgvertexattributes
%{_bindir}/osgvertexprogram
%{?with_wxWidgets:%{_bindir}/osgviewerWX}
%{_bindir}/osgvirtualprogram
%{_bindir}/osgvnc
%{_bindir}/osgvolume
%{_bindir}/osgwidgetaddremove
%{_bindir}/osgwidgetbox
%{_bindir}/osgwidgetcanvas
%{_bindir}/osgwidgetframe
%{_bindir}/osgwidgetinput
%{_bindir}/osgwidgetlabel
%{_bindir}/osgwidgetmenu
%{_bindir}/osgwidgetmessagebox
%{_bindir}/osgwidgetnotebook
%{_bindir}/osgwidgetperformance
%{_bindir}/osgwidgetscrolled
%{_bindir}/osgwidgetshader
%{_bindir}/osgwidgetstyled
%{_bindir}/osgwidgettable
%{_bindir}/osgwidgetwindow
%{_bindir}/osgwindows
%{_datadir}/OpenSceneGraph

%files examples-SDL
%{_bindir}/osgviewerSDL

%files examples-fltk
%{_bindir}/osgviewerFLTK

%files examples-gtk
%{_bindir}/osgviewerGTK

%files -n OpenThreads
%doc AUTHORS.txt NEWS.txt README.md
%license LICENSE.txt
%{_libdir}/libOpenThreads.so.*

%files -n OpenThreads-devel
%doc %{_vpath_builddir}/doc/OpenThreadsReferenceDocs
%{_libdir}/pkgconfig/openthreads.pc
%{_libdir}/libOpenThreads.so
%{_includedir}/OpenThreads

%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE.txt
%{mingw32_bindir}/libOpenThreads.dll
%{mingw32_bindir}/libosg*.dll
%dir %{mingw32_bindir}/osgPlugins-%{version}/
%{mingw32_bindir}/osgPlugins-%{version}/*.dll
%{mingw32_libdir}/libOpenThreads.dll.a
%{mingw32_libdir}/libosg*.dll.a
%{mingw32_libdir}/pkgconfig/openscenegraph*.pc
%{mingw32_libdir}/pkgconfig/openthreads.pc
%{mingw32_includedir}/OpenThreads/
%{mingw32_includedir}/osg*/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{name}
%license LICENSE.txt
%{mingw64_bindir}/libOpenThreads.dll
%{mingw64_bindir}/libosg*.dll
%dir %{mingw64_bindir}/osgPlugins-%{version}/
%{mingw64_bindir}/osgPlugins-%{version}/*.dll
%{mingw64_libdir}/libOpenThreads.dll.a
%{mingw64_libdir}/libosg*.dll.a
%{mingw64_libdir}/pkgconfig/openscenegraph*.pc
%{mingw64_libdir}/pkgconfig/openthreads.pc
%{mingw64_includedir}/OpenThreads/
%{mingw64_includedir}/osg*/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Sandro Mani <manisandro@gmail.com> - 3.6.5-31
- Rebuild (openexr)

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 3.6.5-30
- Rebuild (gdal)

* Tue Nov 05 2024 Sandro Mani <manisandro@gmail.com> - 3.6.5-29
- Exclude osgdb_zip, it conflicts with plugin from osgearth

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Sandro Mani <manisandro@gmail.com> - 3.6.5-27
- Rebuild (openexr)

* Tue May 14 2024 Sandro Mani <manisandro@gmail.com> - 3.6.5-26
- Rebuild (gdal)

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 3.6.5-25
- Rebuilt for openexr 3.2.4

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Sandro Mani <manisandro@gmail.com> - 3.6.5-22
- Rebuild (jasper)

* Tue Nov 28 2023 Orion Poplawski <orion@nwra.com> - 3.6.5-21
- Rebuild for jasper 4.1

* Mon Nov 20 2023 Richard Shaw <hobbes1069@gmail.com> - 3.6.5-20
- Rebuild for Coin4.

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 3.6.5-19
- Rebuild (gdal)

* Mon Aug 14 2023 Sandro Mani <manisandro@gmail.com> - 3.6.5-18
- Rebuild (mingw-poppler)

* Mon Aug 14 2023 Sandro Mani <manisandro@gmail.com> - 3.6.5-17
- Rebuild (mingw-poppler)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 3.6.5-15
- Rebuild (gdal)

* Tue Feb 07 2023 Sandro Mani <manisandro@gmail.com> - 3.6.5-14
- Rebuild (mingw-poppler)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-12
- Rebuild due to wxGLCanvas ABI change

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 3.6.5-11
- Rebuild (gdal)

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 3.6.5-10
- Rebuild with wxWidgets 3.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Sandro Mani <manisandro@gmail.com> - 3.6.5-8
- Rebuild (jasper)

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 3.6.5-7
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.6.5-6
- Rebuild with mingw-gcc-12

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 3.6.5-5
- Make mingw subpackages noarch

* Mon Feb 21 2022 Sandro Mani <manisandro@gmail.com> - 3.6.5-4
- Add mingw subpackages

* Sun Feb 13 2022 Josef Ridky <jridky@redhat.com> - 3.6.5-3
- Rebuilt for libjasper.so.6

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Sandro Mani <manisandro@gmail.com> - 3.6.5-1
- Update to 3.6.5

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 3.4.1-33
- Rebuild (gdal)

* Sun Aug 22 2021 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-32
- Rebuild for OpenEXR/Imath 3.1.

* Wed Aug 11 2021 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-31
- Fix linking with OpenEXR/Imath 3.

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 3.4.1-30
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-29
- Port to OpenEXR 3.x

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Sandro Mani <manisandro@gmail.com> - 3.4.1-27
- Rebuild (libgta)

* Thu May 20 2021 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-26
- Rebuilding for libgta 1.2.1.

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 3.4.1-25
- Rebuild (gdal)

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 3.4.1-24
- Rebuild (gdal)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.4.1-22
- Rebuilt for Boost 1.75

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-21
- Rebuild for OpenEXR 2.5.3.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.1-19
- Rebuilt for gtkglext w/o pangox.
- Spec file cosmetics.
- Work-around %%cmake regressions.

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 3.4.1-18
- Rebuilt for Boost 1.73

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 3.4.1-17
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 3.4.1-16
- Rebuild (gdal)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.4.1-14
- Rebuild for poppler-0.84.0

* Wed Oct  9 2019 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-13
- Rebuild with Coin4.

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.4.1-12
- Rebuilt for new freeglut

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-10
- Rebuild for OpenEXR 2.3.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.4.1-8
- Rebuilt for Boost 1.69

* Sat Aug 04 2018 Scott Talbert <swt@techie.net> - 3.4.1-7
- Rebuild against wxWidgets 3.0 and patch to always use GTK X11 backend

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 3.4.1-5
- Rebuild (giflib)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 3.4.1-3
- Rebuilt for Boost 1.66

* Wed Oct 25 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.1-2
- Add 0006-Add-collada-dom-2.5.patch.
- Rebuild against collada-dom-2.5.

* Thu Sep 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.1-1
- Upgrade to 3.4.1.
- Rebase patches.
- Reflect Source0:-URL having changed.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.4.0-11
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 3.4.0-10
- Rebuilt for Boost 1.64

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.4.0-9
- rebuild (libvncserver)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-7
- Get rid of additional OpenSceneGraph-%%version directory.
- Tidy-up %%changelog.

* Thu Dec 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-6
- Add Collada plugin subpackage.
- Add OpenEXR plugin subpackage.
- Cleanup conditionals.
- BR: libcurl-devel instead of curl-devel.

* Sun Dec 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-5
- Rebuild for jasper-2.0.0.

* Thu Feb 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-4
- Add 0005-c-11-narrowing-hacks.patch (F24FTBFS on arm).
- Remove -pedantic from CMakeLists.txt.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-2
- Eliminate %%define.

* Fri Sep 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-1
- Upstream update to 3.4.0.
- Rebase patches.
- Rework package deps.

* Tue Aug 18 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.3-3
- Move osgqfonts into *-qt.
- Make CMakeModules/FindFLTK multilib-aware.
- Add BR: pkgconfig(*) for those packages, cmake checks for.
- Explicitly list all plugins.
- Spec file cosmetics.

* Mon Aug 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.3-2
- Reflect upstream having changed Source0:-URL.

* Sun Aug 16 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.3-1
- Update to 3.2.3.
- Rebase patches.

* Wed Aug 12 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.2-3
- Set %%Version to %%srcvers.
- BR: boost-devel.
- Add support for Coin3 and Inventor.

* Mon Aug 10 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.2-2
- Add 0004-Unset-DOT_FONTNAME.patch.

* Sat Aug 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2.
- Rebase patches.

* Wed Jun 24 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-7
- Add 0005-From-Jannik-Heller-Fix-for-Qt4-multi-threaded-crash..patch
  (Address RHBZ#1235030)
- Run doxygen -u on doxygen source-files.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.1-5
- Rebuild (gcc-5.0.1).
- Modernize spec.
- Add %%license.

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.1-4
- rebuild (fltk,gcc5)

* Thu Oct 30 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.1-3
- Add 0004-Applied-fix-to-Node-remove-Callback-NodeCallback-ins.patch
  (RHBZ #1158669).
- Rebase patches.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.1-1
- Upgrade to 3.2.1.
- Rebase patches.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.0-2
- Modernize spec.
- Preps for 3.2.1.

* Wed Aug 14 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.0-1
- Upstream update.
- Rebase patches.

* Tue Aug 13 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-18
- Fix %%changelog dates.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.0.1-15
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.0.1-14
- rebuild against new libjpeg

* Mon Sep 03 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-13
- BR: libvncserver-devel, ship osgvnc (RHBZ 853755).

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 17 2012 Marek Kasik <mkasik@redhat.com> - 3.0.1-11
- Rebuild (poppler-0.20.0)

* Mon May 07 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-10
- Append -pthread to CXXFLAGS (Fix FTBFS).

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-9
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.0.1-7
- Rebuild for new libpng

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-6
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 3.0.1-5
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-3
- Add BR: qtwebkit-devel.
- Add osgQtBrowser, osgQtWidgets to OpenSceneGraph-examples-qt.

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 3.0.1-2
- Rebuild (poppler-0.17.3)

* Wed Aug 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-1
- Upstream update.
- Remove OpenSceneGraph2* tags.
- Split out OpenSceneGraph-qt, OpenSceneGraph-qt-devel.
- Pass -Wno-dev to cmake.
- Append -pthread to CFLAGS.

* Sun Jul 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.5-3
- Reflect curl having silently broken their API.

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 2.8.5-2
- Rebuild (poppler-0.17.0)

* Tue Jun 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.5-1
- Upstream update.

* Mon May 30 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.4-2
- Reflect fltk-include paths having changed incompatibly.

* Wed Apr 27 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.4-1
- Upstream update.
- Rebase OpenSceneGraph-*.diff.
- Spec file cleanup.

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 2.8.3-10
- Rebuild (poppler-0.16.3)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-8
- rebuild (poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-7
- rebuild (poppler)

* Wed Dec 15 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.3-6
- Add %%{_fontdir} to OSG's font file search path.

* Sat Nov 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-5
- rebuilt (poppler)

* Thu Sep 30 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.3-4
- rebuild (libpoppler-glib.so.6).

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-3
- rebuild (poppler)

* Mon Jul 12 2010 Dan Horák <dan@danny.cz> - 2.8.3-2
- rebuilt against wxGTK-2.8.11-2

* Fri Jul 02 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.3-1
- Upstream update.
- Add osg-examples-gtk.

* Wed Aug 26 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.2-3
- Change Source0 URL (Upstream moved it once again).

* Tue Aug 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.2-2
- Spec file cleanup.

* Mon Aug 17 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.2-1
- Upstream update.
- Reflect upstream having changes Source0-URL.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.1-2
- Remove /usr/bin/osgfilecache from *-examples.
- Further spec cleanup.

* Wed Jun 24 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.8.1-1
- Upstream update.
- Reflect upstream having consolidated their Source0:-URL.
- Stop supporting OSG < 2.6.0.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Ralf Corsépius <rc040203@freenet.de> - 2.8.0-1
- Upgrade to OSG-2.8.0.
- Remove Obsolete: Producer hacks.

* Thu Aug 14 2008 Ralf Corsépius <rc040203@freenet.de> - 2.6.0-1
- Upgrade to OSG-2.6.0.

* Wed Aug 13 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-4
- Preps for 2.6.0.
- Reflect the Source0-URL having changed.
- Major spec-file overhaul.

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.0-3
- fix license tag

* Tue May 13 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-2
- Add Orion Poplawski's patch to fix building with cmake-2.6.0.

* Mon May 12 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-1
- Upstream update.
- Adjust patches to 2.4.0.

* Mon Feb 11 2008 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-5
- Add *-examples-SDL package.
- Add osgviewerSDL.
- Add *-examples-fltk package.
- Add osgviewerFLTK.
- Add *-examples-qt package.
- Move osgviewerQT to *-examples-qt package.

* Mon Feb 11 2008 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-4
- Rebuild for gcc43.
- OpenSceneGraph-2.2.0.diff: Add gcc43 hacks.

* Wed Nov 28 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-3
- Re-add apivers.
- Rebuild against doxygen-1.5.3-1 (BZ 343591).

* Fri Nov 02 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-2
- Add qt.

* Thu Nov 01 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-1
- Upstream upgrade.
- Reflect Source0-URL having changed once again.
- Reflect upstream packaging changes to spec.

* Sat Oct 20 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-8
- Reflect Source0-URL having changed.

* Thu Sep 27 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-7
- Let OpenSceneGraph-libs Obsoletes: Producer
- Let OpenSceneGraph-devel Obsoletes: Producer-devel.

* Wed Sep 26 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-6
- By public demand, add upstream's *.pcs.
- Add hacks to work around the worst bugs in *.pcs.
- Add OpenSceneGraph2-devel.
- Move ldconfig to *-libs.
- Abandon OpenThreads2.
- Remove obsolete applications.

* Wed Aug 22 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-5
- Prepare renaming package into OpenSceneGraph2.
- Split out run-time libs into *-libs subpackage.
- Rename pkgconfig files into *-2.pc.
- Reactivate ppc64.
- Mass rebuild.

* Sat Jun 30 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-4
- Cleanup CVS.
- Add OSG1_Producer define.

* Fri Jun 29 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-3
- Re-add (but don't ship) *.pc.
- Let OpenSceneGraph "Obsolete: Producer".
- Let OpenSceneGraph-devel "Obsolete: Producer-devel".

* Wed Jun 27 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-2
- Build docs.

* Fri Jun 22 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-1
- Upgrade to 2.0.

* Thu Oct 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2-1
- Upstream update.

* Thu Aug 24 2006 Ralf Corsépius <rc040203@freenet.de> - 1.1-1
- Upstream update.

* Sat Dec 10 2005 Ralf Corsépius <rc040203@freenet.de> - 1.0-1
- Upstream update.

* Tue Aug 02 2005 Ralf Corsepius <ralf@links2linux.de> - 0.9.9-1
- FE submission.

* Thu Jul 21 2005 Ralf Corsepius <ralf@links2linux.de> - 0.9.9-0
- Initial spec.
