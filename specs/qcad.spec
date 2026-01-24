%bcond_with qt6

%global _QCAD_DIR %{_libdir}/%{name}

%if %{with qt6}
%global _QT_PLUGINS %{_qt6_plugindir}
%bcond_without cmake
%else
%global _QT_PLUGINS %{_qt5_plugindir}
%bcond_with cmake
%endif

# Filter private libraries
%global __provides_exclude ^(%%(find %{buildroot}%{_libdir}/qcad -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/qcad -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
#

Name:    qcad
Version: 3.32.6.0
Release: %autorelease
Epoch:   1
Summary: Powerful 2D CAD system

## Main license: GPLv3
##
## 3rd parties licenses: 
## dxflib: GPLv2+.
#  See src/3rdparty/dxflib/gpl-2.0greater.txt
## opennurbs: Public domain (neither copyright nor copyleft apply).
#  See src/3rdparty/opennurbs/readme.txt
## spatialindexnavel:  MIT
#  See src/3rdparty/spatialindexnavel/COPYING
## stemmer: BSD 2-Clause License
#  See src/3rdparty/stemmer/bsd-2.txt
## Hershey fonts are released under the terms described in fonts/hershey.readme.
## Other fonts in directory 'fonts' are released as public domain (all copyright
## is waived) and BSD (3-clauses).

License: GPL-3.0-only AND GPL-2.0-or-later AND MIT AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Callaway-Public-Domain AND CC-BY-3.0 AND LicenseRef-Hershey
Source0: https://github.com/qcad/qcad/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: %{name}.appdata.xml
URL: https://www.qcad.org/

%if %{with qt6}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qttools-static
BuildRequires: qt6-qtwebengine
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qtscxml-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: glslang-devel
%else
BuildRequires: qt5-qtbase-devel >= 5.9.0
BuildRequires: qt5-rpm-macros >= 5.9.0
BuildRequires: qt5-qttools-devel >= 5.9.0
BuildRequires: qt5-qttools-static >= 5.9.0
BuildRequires: qt5-qtscript-devel >= 5.9.0
BuildRequires: qt5-qtsvg-devel >= 5.9.0
BuildRequires: qt5-qtxmlpatterns-devel >= 5.9.0
BuildRequires: qt5-qtdeclarative-devel >= 5.9.0
Requires:      qt5-qtsvg%{?_isa}
Requires:      qt5-qtscript%{?_isa}
Provides:      bundled(qtscriptgenerator)
%endif
BuildRequires: gcc-c++
BuildRequires: chrpath
%if %{with cmake}
BuildRequires: cmake
%endif
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXrender-devel
BuildRequires: libSM-devel
BuildRequires: fdupes
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: dbus-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: fontpackages-devel
BuildRequires: vlgothic-fonts
BuildRequires: dejavu-sans-fonts
BuildRequires: dejavu-sans-mono-fonts

Requires:      dejavu-sans-fonts
Requires:      dejavu-sans-mono-fonts
Requires:      hicolor-icon-theme
Requires:      vl-gothic-fonts


Provides:      bundled(dxflib) = 1.0.0
Provides:      bundled(opennurbs) = 201004095
Provides:      bundled(stemmer) = 1.0.0
# Unbundling this library may cause crashes of the software
Provides:      bundled(spatialindex) = 1.9.1
Provides:      bundled(spatialindexnavel) = 1.9.1

%description
QCAD is an application for computer aided drafting (CAD) in two dimensions (2D).
With QCAD you can create technical drawings such as plans for buildings,
interiors, mechanical parts or schematics and diagrams.
QCAD was designed with modularity, extensibility and portability in mind.
But what people notice most often about QCAD is its intuitive
user interface.
QCAD is an easy to use but powerful 2D CAD system for everyone.
You dont need any CAD experience to get started with QCAD immediately.

%prep
%setup -n %{name}-%{version} -q

rm -rf ../*-SPECPARTS

# Use Fedora Qt5 scripts
%if %{without qt6}
cp -a src/3rdparty/qt-labs-qtscriptgenerator-5.15.8 src/3rdparty/qt-labs-qtscriptgenerator-5.15.18
mv src/3rdparty/qt-labs-qtscriptgenerator-5.15.18/qt-labs-qtscriptgenerator-5.15.8.pro \
 src/3rdparty/qt-labs-qtscriptgenerator-5.15.18/qt-labs-qtscriptgenerator-5.15.18.pro
%endif


%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

%if %{with cmake}
export LDFLAGS="%{__global_ldflags} -Wl,-rpath -Wl,%{_QCAD_DIR}"
%cmake -DBUILD_QT6:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release \
       -DCMAKE_CFLAGS_RELEASE="%{build_cflags} %(pkg-config --cflags Qt6UiTools)" \
       -DCMAKE_CXXFLAGS_RELEASE="%{build_cxxflags} %(pkg-config --cflags Qt6UiTools)" \
       -DVulkan_GLSLC_EXECUTABLE:FILEPATH=%{_bindir}/glslang -DVulkan_GLSLANG_VALIDATOR_EXECUTABLE:FILEPATH=%{_bindir}/glslangValidator \
       -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%else
%{_qt5_qmake} -makefile CONFIG+=release %{name}.pro \
 QMAKE_CFLAGS_RELEASE+="%{_qt5_optflags} %(pkg-config --cflags Qt5UiTools)" \
 QMAKE_CXXFLAGS_RELEASE+="%{_qt5_optflags} %(pkg-config --cflags Qt5UiTools)" \
 QMAKE_LFLAGS+="%{_qt5_ldflags} -Wl,-rpath -Wl,%{_QCAD_DIR}" \
 LFLAGS+="%{_qt5_ldflags} -Wl,-rpath -Wl,%{_QCAD_DIR}"
%make_build
%endif

%install
%if %{with cmake}
%cmake_install
%else
mkdir -p %{buildroot}%{_QCAD_DIR}/ts
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mkdir -p %{buildroot}%{_QT_PLUGINS}/codecs
mkdir -p %{buildroot}%{_QT_PLUGINS}/script
mkdir -p %{buildroot}%{_QT_PLUGINS}/designer
mkdir -p %{buildroot}%{_QT_PLUGINS}/imageformats
mkdir -p %{buildroot}%{_QT_PLUGINS}/sqldrivers
mkdir -p %{buildroot}%{_QCAD_DIR}/plugins/codecs
mkdir -p %{buildroot}%{_QCAD_DIR}/plugins/designer
mkdir -p %{buildroot}%{_QCAD_DIR}/plugins/imageformats
mkdir -p %{buildroot}%{_QCAD_DIR}/plugins/sqldrivers
mkdir -p %{buildroot}%{_QCAD_DIR}/plugins/script
mkdir -p %{buildroot}%{_QCAD_DIR}/plugins/printsupport

## Install fonts
cp -a fonts %{buildroot}%{_QCAD_DIR}/

# Unbundle vlgothic-fonts
ln -sf %{_fontbasedir}/vl-gothic-fonts/VL-Gothic-Regular.ttf %{buildroot}%{_QCAD_DIR}/fonts/VL-Gothic-Regular.ttf

# Unbundle dejavu-sans-fonts
for i in `ls %{buildroot}%{_QCAD_DIR}/fonts/qt | grep DejaVuSans`; do
 ln -sf %{_fontbasedir}/dejavu-sans-fonts/$i %{buildroot}%{_QCAD_DIR}/fonts/qt/$i
done
for i in `ls %{buildroot}%{_QCAD_DIR}/fonts/qt | grep DejaVuSansMono`; do
 ln -sf %{_fontbasedir}/dejavu-sans-mono-fonts/$i %{buildroot}%{_QCAD_DIR}/fonts/qt/$i
done
##

cp -a patterns %{buildroot}%{_QCAD_DIR}/
cp -a themes %{buildroot}%{_QCAD_DIR}/
cp -a libraries %{buildroot}%{_QCAD_DIR}/
cp -a scripts %{buildroot}%{_QCAD_DIR}/
cp -a plugins %{buildroot}%{_QCAD_DIR}/
cp -a linetypes %{buildroot}%{_QCAD_DIR}/

# This file is required for Help's "Show Readme" menu choice
ln -sf %{_datadir}/doc/qcad/readme.txt %{buildroot}%{_QCAD_DIR}/readme.txt

install -pm 644 ts/qcad*.qm %{buildroot}%{_QCAD_DIR}/ts

ln -sf %{_QT_PLUGINS}/imageformats/libqgif.so %{buildroot}%{_QCAD_DIR}/plugins/imageformats/libqgif.so
ln -sf %{_QT_PLUGINS}/imageformats/libqico.so %{buildroot}%{_QCAD_DIR}/plugins/imageformats/libqico.so
ln -sf %{_QT_PLUGINS}/imageformats/libqjpeg.so %{buildroot}%{_QCAD_DIR}/plugins/imageformats/libqjpeg.so
ln -sf %{_QT_PLUGINS}/imageformats/libqsvg.so %{buildroot}%{_QCAD_DIR}/plugins/imageformats/libqsvg.so
ln -sf %{_QT_PLUGINS}/imageformats/libqtga.so %{buildroot}%{_QCAD_DIR}/plugins/imageformats/libqtga.so
ln -sf %{_QT_PLUGINS}/imageformats/libqtiff.so %{buildroot}%{_QCAD_DIR}/plugins/imageformats/libqtiff.so

ln -sf %{_QT_PLUGINS}/sqldrivers/libqsqlite.so %{buildroot}%{_QCAD_DIR}/plugins/sqldrivers/libqsqlite.so
ln -sf %{_QT_PLUGINS}/printsupport/libcupsprintersupport.so %{buildroot}%{_QCAD_DIR}/plugins/printsupport/libcupsprintersupport.so

install -pm 644 scripts/qcad_icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pm 755 release/*.so %{buildroot}%{_QCAD_DIR}
install -pm 755 release/%{name}-bin %{buildroot}%{_QCAD_DIR}

install -pm 644 qcad.1 %{buildroot}%{_mandir}/man1
install -pm 644 scripts/%{name}_icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

find %{buildroot}%{_QCAD_DIR} -name ".gitignore" -delete
find %{buildroot}%{_QCAD_DIR} -name "Makefile" -delete

pushd %{buildroot}%{_QCAD_DIR}
for i in `find . -type f \( -name "*.so*" -o -name "qcad-bin" \)`; do
  chmod -c 755 $i
  chrpath -r %{_QCAD_DIR} $i
done
popd
%endif

%fdupes -s %{buildroot}%{_QCAD_DIR}/libraries
%fdupes -s %{buildroot}%{_QCAD_DIR}/patterns
%fdupes -s %{buildroot}%{_QCAD_DIR}/scripts
%fdupes -s %{buildroot}%{_QCAD_DIR}/themes
# %%fdupes does not recognize any options other than '-s'
%{_bindir}/fdupes -H -nA %{buildroot}%{_QCAD_DIR}/plugins

cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/sh
env QT_QPA_PLATFORM=xcb %{_QCAD_DIR}/%{name}-bin "\$@"
EOF
chmod a+x %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install        \
 --add-category Graphics    \
 --add-category Engineering \
 --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc README.md readme.txt
%license LICENSE.txt gpl-3.0.txt gpl-3.0-exceptions.txt cc-by-3.0.txt fonts/hershey.readme
%license fonts/README.sazanami fonts/LICENSE_E.mplus fonts/osifont_license.txt
%license src/3rdparty/dxflib/gpl-2.0greater.txt
%license src/3rdparty/spatialindexnavel/COPYING
%license src/3rdparty/stemmer/bsd-2.txt
%{_bindir}/%{name}
%{_QCAD_DIR}/
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/*

%changelog
%autochangelog
