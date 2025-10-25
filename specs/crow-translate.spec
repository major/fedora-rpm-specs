%ifnarch s390x
%bcond onnxruntime 1
%endif

%global appid org.kde.CrowTranslate

Name: crow-translate
Version: 4.0.2
Release: %autorelease
Summary: A simple and lightweight translator

# The entire source code is GPL-3.0-only except bundled libs:
# GPL-3.0-or-later: qonlinetranslator
# BSD-3-Clause:     qhotkey
#                   qtaskbarcontrol
#                   singleapplication
# MIT:              singleapplication
License: GPL-3.0-only AND GPL-3.0-or-later AND BSD-3-Clause AND MIT
URL: https://apps.kde.org/crowtranslate/
Source: https://download.kde.org/%{stable_kf6}/%{name}/%{version}/%{name}-%{version}.tar.gz

# https://invent.kde.org/office/crow-translate/-/merge_requests/770
Patch:  0001-Fix-Hebrew-on-Yandex-and-DuckDuckGo.patch
# https://invent.kde.org/office/crow-translate/-/merge_requests/771
Patch:  0002-cmake-fix-pkg-config-detection-of-onnxruntime.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: cmake >= 3.16
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: cmake(leptonica)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6StateMachine)
BuildRequires: cmake(Qt6TextToSpeech)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(KWayland)
BuildRequires: cmake(tesseract) >= 4.0
%if %{with onnxruntime}
BuildRequires: pkgconfig(libonnxruntime)
%endif

Requires: hicolor-icon-theme

Recommends: gstreamer-plugins-good

# Consider submodules in this repo as a way to avoid copy-pasting the code
# https://github.com/crow-translate/crow-translate/issues/615#issuecomment-1762779870
%if %{with onnxruntime}
Provides: bundled(espeak-ng)
%endif
Provides: bundled(qonlinetranslator)
Provides: bundled(qhotkey)
Provides: bundled(qtaskbarcontrol)
Provides: bundled(singleapplication)

%description
Crow Translate is a simple and lightweight translator written in C++ / Qt that
allows you to translate and speak text using Google, Yandex, Bing,
LibreTranslate and Lingva translate API. You may also be interested in my
library QOnlineTranslator used in this project.


%prep
%autosetup -N -n %{name}
dos2unix cmake/*.cmake src/*.cpp
%autopatch -p1
# Unbundle
#   * Used only on Windows
rm -r src/qgittag


%build
# https://github.com/crow-translate/crow-translate/issues/615#issuecomment-1762934229
# Statically link bundled modules
#   Problem: conflicting requests
#    - nothing provides libQTaskbarControl.so()(64bit) needed by crow-translate-2.10.10-1.fc39.x86_64
#    - nothing provides libqhotkey.so.1()(64bit) needed by crow-translate-2.10.10-1.fc39.x86_64
%{cmake_kf6} \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    %{!?with_onnxruntime:-DWITH_PIPER_TTS:BOOL=OFF}
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/crow
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%if %{with onnxruntime}
%{_datadir}/%{name}/
%endif
%{_metainfodir}/%{appid}.metainfo.xml


%changelog
%autochangelog
