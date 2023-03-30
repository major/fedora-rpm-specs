%global _QCAD_DIR %{_libdir}/%{name}
%global _QT_PLUGINS %{_qt5_plugindir}

# Filter private libraries
%global __provides_exclude ^(%%(find %{buildroot}%{_libdir}/qcad -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/qcad -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
#

Name:    qcad
Version: 3.28.0.0
Release: 1%{?dist}
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

License: GPLv3 and GPLv2+ and MIT and BSD and Public Domain and CC-BY and Hershey
Source0: https://github.com/qcad/qcad/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: %{name}.appdata.xml
URL: https://www.qcad.org/

BuildRequires: qt5-qtbase-devel >= 5.9.0
BuildRequires: qt5-rpm-macros >= 5.9.0
BuildRequires: qt5-qtwebkit-devel >= 5.9.0
BuildRequires: qt5-qttools-devel >= 5.9.0
BuildRequires: qt5-qttools-static >= 5.9.0
BuildRequires: qt5-qtscript-devel >= 5.9.0
BuildRequires: qt5-qtsvg-devel >= 5.9.0
BuildRequires: qt5-qtxmlpatterns-devel >= 5.9.0
Requires: qt5-designer >= 5.9.0
Requires: qt5-qtsvg
Provides: bundled(qtscriptgenerator) = 5.9.0
BuildRequires: gcc-c++, chrpath
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXrender-devel
BuildRequires: libSM-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: dbus-devel
BuildRequires: mesa-libGLU-devel
#BuildRequires: spatialindex-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: fontpackages-devel

Requires: hicolor-icon-theme
Requires: wise2
Requires: qgnomeplatform-qt5
Requires: vlgothic-fonts
Requires: dejavu-sans-fonts

Provides: bundled(dxflib) = 1.0.0
Provides: bundled(opennurbs) = 201004095
Provides: bundled(stemmer) = 1.0.0

## Unbundle spatialindex libraries
Patch0: %{name}-qt5-unbundle_libraries.patch

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
%autosetup -n %{name}-%{version} -p0

# Use Fedora Qt5 scripts
cp -a src/3rdparty/qt-labs-qtscriptgenerator-5.15.3 src/3rdparty/qt-labs-qtscriptgenerator-5.15.8
mv src/3rdparty/qt-labs-qtscriptgenerator-5.15.8/qt-labs-qtscriptgenerator-5.15.3.pro \
 src/3rdparty/qt-labs-qtscriptgenerator-5.15.8/qt-labs-qtscriptgenerator-5.15.8.pro

%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

%{_qt5_qmake} -makefile CONFIG+=release %{name}.pro \
 QMAKE_CFLAGS_RELEASE+="%{_qt5_optflags} %(pkg-config --cflags Qt5UiTools) -I$PWD/src/3rdparty/spatialindexnavel/include" \
 QMAKE_CXXFLAGS_RELEASE+="%{_qt5_optflags} %(pkg-config --cflags Qt5UiTools) -I$PWD/src/3rdparty/spatialindexnavel/include" \
 QMAKE_LFLAGS+="%{_qt5_ldflags} -Wl,-rpath -Wl,%{_QCAD_DIR}" \
 LFLAGS+="%{_qt5_ldflags} -Wl,-rpath -Wl,%{_QCAD_DIR}"
%make_build

%install

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
cp -a fonts %{buildroot}%{_QCAD_DIR}

# Unbundle vlgothic-fonts
ln -sf %{_fontbasedir}/vlgothic/VL-Gothic-Regular.ttf %{buildroot}%{_QCAD_DIR}/fonts/VL-Gothic-Regular.ttf

# Unbundle dejavu-sans-fonts
for i in `ls %{buildroot}%{_QCAD_DIR}/fonts/qt | grep DejaVuSans`; do
 ln -sf %{_fontbasedir}/dejavu/$i %{buildroot}%{_QCAD_DIR}/fonts/qt/$i
done
##

cp -a patterns %{buildroot}%{_QCAD_DIR}
cp -a themes %{buildroot}%{_QCAD_DIR}
cp -a libraries %{buildroot}%{_QCAD_DIR}
cp -a scripts %{buildroot}%{_QCAD_DIR}
cp -a plugins %{buildroot}%{_QCAD_DIR}
cp -a linetypes %{buildroot}%{_QCAD_DIR}

# This file is required for Help's "Show Readme" menu choice
cp -p readme.txt %{buildroot}%{_QCAD_DIR}

install -pm 644 ts/qcad*.qm %{buildroot}%{_QCAD_DIR}/ts
ln -sf %{_QT_PLUGINS}/codecs/libqcncodecs.so %{buildroot}%{_QCAD_DIR}/plugins/codecs/libqcncodecs.so
ln -sf %{_QT_PLUGINS}/codecs/libqjpcodecs.so %{buildroot}%{_QCAD_DIR}/plugins/codecs/libqjpcodecs.so
ln -sf %{_QT_PLUGINS}/codecs/libqkrcodecs.so %{buildroot}%{_QCAD_DIR}/plugins/codecs/libqkrcodecs.so
ln -sf %{_QT_PLUGINS}/codecs/libqtwcodecs.so %{buildroot}%{_QCAD_DIR}/plugins/codecs/libqtwcodecs.so

ln -sf %{_QT_PLUGINS}/designer/libqwebview.so %{buildroot}%{_QCAD_DIR}/plugins/designer/libqwebview.so

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
install -pm 644 readme.txt %{buildroot}%{_QCAD_DIR}

install -pm 644 qcad.1 %{buildroot}%{_mandir}/man1
install -pm 644 scripts/%{name}_icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

find %{buildroot}%{_QCAD_DIR} -name ".gitignore" -delete
find %{buildroot}%{_QCAD_DIR} -name "readme.txt" -delete
find %{buildroot}%{_QCAD_DIR} -name "Makefile" -delete

pushd %{buildroot}%{_QCAD_DIR}
for i in `find . -type f \( -name "*.so*" -o -name "qcad-bin" \)`; do
  chmod -c 755 $i
  chrpath -r %{_QCAD_DIR} $i
done
popd

cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/sh
export \
LD_LIBRARY_PATH=%{_QCAD_DIR}:%{_QCAD_DIR}/plugins/script \
QTLIB=%{_qt5_libdir} \
QTDIR=%{_qt5_libdir} \
QTINC=%{_qt5_headerdir} \
WISECONFIGDIR=%{_datadir}/wise2 \
%if 0%{?fedora} >= 31
QT_QPA_PLATFORM=xcb \
%endif
PATH=%{_libdir}:%{_QCAD_DIR}
%{_QCAD_DIR}/%{name}-bin "\$@"
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
%doc README.md
%license LICENSE.txt gpl-3.0.txt gpl-3.0-exceptions.txt cc-by-3.0.txt fonts/hershey.readme
%license fonts/README.sazanami fonts/LICENSE_E.mplus fonts/osifont_license.txt
%license src/3rdparty/dxflib/gpl-2.0greater.txt
%license src/3rdparty/spatialindexnavel/COPYING
%license src/3rdparty/stemmer/bsd-2.txt
%license src/3rdparty/opennurbs/readme.txt
%{_bindir}/%{name}
%{_QCAD_DIR}/
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/*

%changelog
* Tue Mar 28 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.28.0.0-1
- Release 3.28.0.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.27.9.0-1
- Release 3.27.9.0

* Thu Dec 08 2022 Marie Loise Nolden <loise@kde.org> - 3.27.8.0-2
- build with Qt 5.15.7

* Sat Oct 08 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.27.8.0-1
- Release 3.27.8.0

* Mon Oct 03 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.27.7.0-1
- Release 3.27.7.0

* Tue Aug 09 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.27.6.0-3
- Fix qt scripts

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.27.6.0-1
- Release 3.27.6.0

* Tue May 10 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.27.5.0-1
- Release 3.27.5.0

* Thu Apr 28 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.27.2.0-1
- Release 3.27.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.27.1.0-1
- Release 3.27.1.0

* Fri Dec 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.27.0.1-1
- Release 3.27.0.1

* Fri Sep 17 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.26.4.0-1
- Release 3.26.4.0

* Sat Aug 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.26.3.0-4
- Remove references to quazip

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 3.26.3.0-3
- Rebuild (quazip)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.3.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.26.3.0-1
- Release 3.26.2.3

* Thu Apr 15 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.26.2.0-1
- Release 3.26.2.0

* Mon Mar 08 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.26.1.0-1
- Release 3.26.1.0

* Wed Mar 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.26.0.1-2
- Filter private libraries

* Wed Mar 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.26.0.1-1
- Release 3.26.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.25.2.0-2
- Add make BR

* Fri Sep 04 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.25.2.0-1
- Release 3.25.2.0

* Mon Aug 31 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.25.1.0-1
- Release 3.25.1.0

* Thu Aug 20 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.25.0.0-1
- Release 3.25.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Jeff Law <law@redhat.com> - 3.24.3.0-3
- Disable LTO

* Sat Jun 20 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.24.3.0-2
- Modification to the desktop file (rhbz#1849265)

* Mon Apr 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.24.3.0-1
- Release 3.24.3.0

* Mon Mar 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.24.2.6-2
- Fix plugins macro

* Wed Feb 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.24.2.6-1
- Release 3.24.2.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.24.2.1-3
- Workaround for rhbz #1790550

* Wed Jan 15 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.24.2.1-2
- Fix desktop files

* Tue Jan 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.24.2.1-1
- Release 3.24.2.1
- Use bundled spatialindex-1.8.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.22.1.0-6
- Undo latest change

* Thu Jul 11 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.22.1.0-5
- Use relative symlinks to the system fonts

* Thu Jul 11 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.22.1.0-4
- Remove filtering of private libraries (rhbz #1728088)

* Tue Jul 09 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.22.1.0-3
- Do not remove rpaths (rhbz #1728088)

* Fri May 31 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.22.1.0-2
- Add Qt-5.11.3 scripts

* Thu May 30 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.22.1.0-1
- Update to 3.22.1.0
- Remove Qt4 condition
- Update patch

* Tue Feb 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.21.3.15-1
- Update to 3.21.3.15

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.21.3.2-1
- Update to 3.21.3.2

* Thu Jul 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.21.2.2-1
- Update to 3.21.2.2
- Appdata file modified
- Fix qt-5.9.6 scripts for Fedora 27

* Sun Jul 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.20.1.3-4
- Add script bindings for Qt 5.11.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.20.1.3-2
- Include readme.txt for Help menu

* Sun May 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.20.1.3-1
- Update to 3.20.1.3
- Unbunlde vlgothic-fonts and dejavu-sans-fonts

* Wed Apr 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.19.2.8-1
- Update to 3.19.2.8

* Sun Mar 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.19.2.3-2
- Build with Qt5 on fedora 26 too

* Sat Mar 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.19.2.3-1
- Update to 3.19.2.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.19.2.2-1
- Update to 3.19.2.2

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.19.1.0-3
- Remove obsolete scriptlets

* Sat Dec 23 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.19.1.0-2
- Appdata file moved into metainfo data directory

* Sat Nov 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.19.1.0-1
- Update to 3.19.1.0

* Thu Nov 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.19.0.0-1
- Update to 3.19.0.0

* Sat Oct 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.18.1.0-2
- printsupport/libcupsprintersupport.so file symlinked (bz#1499418)

* Thu Oct 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.18.1.0-1
- Update to 3.18.1.0

* Fri Sep 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.18.0.0-1
- Update to 3.18.0.0

* Fri Aug 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.17.3.6-1
- Update to 3.17.3.6
- Add script bindings for Qt 5.9.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.17.3.1-1
- Update to 3.17.3.1
- Fix licenses reported in the appdata file

* Sat Jul 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.17.3.0-1
- Update to 3.17.3.0

* Sun Jun 18 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.17.1.5-2.20170616git7f66d9
- Update to 3.17.1.5 -post release commit #7f66d9

* Sat Jun 17 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.17.1.5-1
- Update to 3.17.1.5
- Build qt4 version on fedora < 27

* Fri May 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.17.1.1-1
- Update to 3.17.1.1
- Built with Qt5 (5.9.0)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Mar 27 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.16.7.0-1
- Update to 3.16.7.0
- Fix detection of QCAD modules

* Sun Mar 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.16.5.0-2
- Add linetypes directory (bz#1429248)

* Fri Feb 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.16.5.0-1
- Update to 3.16.5.0

* Wed Jan 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.16.4.0-1
- Update to 3.16.4.0

* Sun Jan 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.16.3.0-2
- Add quazip as Requires package

* Wed Dec 28 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.16.3.0-1
- Update to 3.16.3.0

* Tue Dec 20 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.16.2.0-2
- Main directory moved under libdir directory
- Filtering of private libraries

* Tue Dec 20 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.16.2.0-1
- Return to QT4 (see comment)
- Update to 3.16.2.0

* Mon Dec 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.15.6.1-3
- Unbundle quazip libraries
- Rebuilt with QT5

* Sun Dec 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.15.6.1-2
- Unbundle spatialindex libraries

* Sun Dec 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.15.6.1-1
- Update to 3.15.6.1

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.0.5.0-14
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul  4 2010 Alain Portal <alain.portal AT univ-montp2 DOT fr> - 2.0.5.0-12
- Patch to add some missing caracters to the latin1 charset
- Patch to to fix a french mispelling
- Frenchify desktop and spec files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.5.0-9
- fix license tag

* Fri Feb 22 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.0.5.0-8
- patch to compile with GCC 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.5.0-7
- Autorebuild for GCC 4.3

* Wed Jan 23 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.0.5.0-6
- added patch to add arc type tangential to menu

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.0.5.0-5
- Rebuild for FE6

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.0.5.0-4
- Rebuild for Fedora Extras 5

* Thu Nov 24 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.0.5.0-3
- generate and include qm files

* Wed Nov 23 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.0.5.0
- New Version 2.0.5.0

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 2.0.4.0-5.fc4
- fix build on 64bit arches (#158650)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.0.4.0-4.fc4
- rebuild on all arches

* Tue Apr  5 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.0.4.0-3.fc4
- Add missing line in qcad-assistant.patch which prevents orphans.

* Mon Feb 14 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.0.4.0-2
- Remove /usr/bin/assistant (-> qt-devel) dependency, replace with
  patches to open a warning dialog in case of Qt Assistant error
  conditions. Add a related patch for the English manual which
  removes references to two missing images.

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.0.4.0-1
- Added documentation
- Fixed code for calling Qt Assistant: qcad-qass.patch

* Mon Nov 15 2004 Gerard Milmeister <gemi@bluewin.ch> - 2.0.4.0-0.fdr.2
- Added mime type to desktop file

* Fri Oct  1 2004 Gerard Milmeister <gemi@bluewin.ch> - 2.0.4.0-0.fdr.1
- New Version 2.0.4.0

* Sat Jun  5 2004 Gerard Milmeister <gemi@bluewin.ch> - 2.0.3.3-0.fdr.1
- New Version 2.0.3.3

* Sun Apr 25 2004 Gerard Milmeister <gemi@bluewin.ch> - 2.0.3.1-0.fdr.2
- Set QTDIR from qt.sh

* Sun Apr 11 2004 Gerard Milmeister <gemi@bluewin.ch> - 2.0.3.1-0.fdr.1
- New Version 2.0.3.1

* Sat Feb 28 2004 Gerard Milmeister <gemi@bluewin.ch> - 2.0.2.0-0.fdr.1
- New Version 2.0.2.0

* Fri Dec 12 2003 Gerard Milmeister <gemi@bluewin.ch> - 2.0.1.3-0.fdr.1
- New Version 2.0.1.3

* Wed Nov 26 2003 Gerard Milmeister <gemi@bluewin.ch> - 2.0.1.2-1.fdr.2
- Respect RPM_OPT_FLAGS

* Wed Nov 26 2003 Gerard Milmeister <gemi@bluewin.ch> - 2.0.1.2-0.fdr.1
- New Version 2.0.1.2

* Tue Oct 21 2003 Gerard Milmeister <gemi@bluewin.ch> - 2.0.1.1-1.fdr.1
- First Fedora release
