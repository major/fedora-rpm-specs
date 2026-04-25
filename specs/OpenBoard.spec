Name:          OpenBoard
Release:       %autorelease
Version:       1.7.7
Summary:       Interactive whiteboard application for use in a classroom setting
# most code is under GPLv3+, except:
# all jquery*.js: MIT
# resources/library/applications/Camera.wgt/cropper: MIT
# resources/library/applications/ColorPicker.wgt/js: MIT
# resources/library/applications/GeoInfo.wgt/js/tinyxmldom.js: LGPL-2.1-or-later
# resources/library/applications/Horloge.wgt/station-clock.js: Apache-2.0
# resources/library/applications/Html.wgt: MIT
# resources/library/applications/Latex2svg.wgt/js/MathJax: Apache-2.0
# resources/library/applications/OpenStreetMap.wgt/api/OpenLayers.js: BSD-2-Clause-Views AND MIT AND Apache-2.0 AND BSD-3-Clause
# resources/library/applications/QR-Code.wgt/js/qrcode.js: MIT
# resources/library/applications/Stopwatch.wgt/js/DD_roundies_0.0.2a.js: MIT
# resources/library/applications/Wikipedia.wgt/script/superfish.js: MIT
# resources/library/applications/Wiktionnairy.wgt/script/superfish.js: MIT
# resources/startupHints/js: MIT
# src/network/UBAutoSaver.{h,cpp}: LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only
# src/network/UBCookieJar.{h,cpp}: LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only
# src/singleapplication: MIT
# src/web/simplebrowser/WB*: LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only 
# src/web/simplebrowser/*: BSD-3-Clause
License:       GPL-3.0-or-later AND MIT AND LGPL-2.1-or-later AND Apache-2.0 AND BSD-2-Clause-Views AND BSD-3-Clause AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only)
URL:           https://openboard.ch/
# Source:        https://github.com/OpenBoard-org/OpenBoard/archive/v%%{version}/%%{name}-%%{version}.tar.gz
# upstream source contains non-free fonts and extensions
Source:        %{name}-%{version}-free.tar.gz
Source:        %{name}-mktarball.sh
Source:        ch.openboard.OpenBoard.appdata.xml
# Upstream uses only OpenBoard-specific fonts to make drawings portable
# https://github.com/OpenBoard-org/OpenBoard/issues/474
# Ensure system fonts are still available after unbundling included fonts
Patch:         %{name}-use-system-fonts.patch
# Disable software update check and hide the checkbox in Preferences, based on OpenSUSE patch:
# https://build.opensuse.org/projects/home:letsfindaway:experimental/packages/OpenBoard-Qt6/files/9117-disable-software-update.patch
Patch:         %{name}-disable-software-update.patch
BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6MultimediaWidgets)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6SvgWidgets)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(QuaZip-Qt6)
BuildRequires: cmake(zlib)
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(opengl)
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: qt6-srpm-macros
Provides: bundled(js-jquery) = 1.3.2
Provides: bundled(js-jquery) = 1.6.2
Provides: bundled(js-jquery) = 1.7.1
Provides: bundled(js-jquery) = 1.7.2
Provides: bundled(js-jquery) = 1.8.0
Provides: bundled(js-jquery) = 1.8.1
# Use system Andika New Basic instead of bundled obsolete Andika Basic
Requires: font(andikanewbasic)
# Use system Écolier court fonts
Requires: font(ecolier_court)
Requires: font(ecolier_lignes_court)
Requires: hicolor-icon-theme
Requires: shared-mime-info
# Qt6WebEngineWidgets is not available on x86 32bit and s390x
ExclusiveArch: %{qt6_qtwebengine_arches}

%description
OpenBoard is an open source cross-platform interactive white board
application designed primarily for use in schools. It was originally
forked from Open-Sankoré, which was itself based on Uniboard.

%prep
%autosetup -p1

%build
%cmake \
        -G Ninja \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_CXX_STANDARD=20 \

%cmake_build

%install
%cmake_install
# bundled urw fonts are unused
rm -rv %{buildroot}%{_datadir}/openboard/fonts

install -Dpm644 %{S:2} %{buildroot}%{_datadir}/metainfo/ch.openboard.OpenBoard.metainfo.xml

hardlink --content --verbose %{buildroot}

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ch.openboard.OpenBoard.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ch.openboard.OpenBoard.metainfo.xml

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/openboard
%{_datadir}/applications/ch.openboard.OpenBoard.desktop
%{_datadir}/mime/packages/ch.openboard.openboard-ubz.xml
%dir %{_datadir}/openboard
%{_datadir}/openboard/customizations
%dir %{_datadir}/openboard/i18n
%{_datadir}/openboard/library
%{_datadir}/openboard/startupHints
%{_datadir}/openboard/template
%{_iconsdir}/hicolor/scalable/apps/ch.openboard.OpenBoard.svg
%{_iconsdir}/hicolor/scalable/mimetypes/ch.openboard.application-ubz.svg
%{_metainfodir}/ch.openboard.OpenBoard.metainfo.xml
%{_sysconfdir}/openboard

%changelog
%autochangelog
