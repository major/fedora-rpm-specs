%global forgeurl https://github.com/hluk/CopyQ/
%global commit fa209998b981460003349194b5ba1237d9804ea8

Name:    copyq
Version: 13.0.0
Release: %autorelease
Summary: Advanced clipboard manager
License: GPL-3.0-or-later

%{forgemeta}

Url:     %{forgeurl}
Source0: %{forgesource}
Source1: %{name}.rpmlintrc

BuildRequires: cmake, extra-cmake-modules, gcc-c++
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils, git
BuildRequires: libXtst-devel, libXfixes-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-rpm-macros
BuildRequires: qt6-qtbase-devel, qt6-qtbase-private-devel
BuildRequires: qt6-qtsvg-devel, qt6-qtdeclarative-devel
BuildRequires: qt6-qttools-devel, kf6-kstatusnotifieritem-devel
BuildRequires: qwt-qt6-devel
BuildRequires: wayland-devel, qt6-qtwayland-devel

%description
CopyQ is advanced clipboard manager with searchable and editable history with
support for image formats, command line control and more.

%prep
%{forgesetup}
%autosetup -p1 -n %{archivename}

# drop upstream ASCII restricted cast define
sed -i '/DQT_RESTRICTED_CAST_FROM_ASCII/d' CMakeLists.txt

# Force the right private target and make sure CMake can find it
grep -Rl -F 'Qt::GuiPrivate' src | xargs sed -i 's/\bQt::GuiPrivate\b/Qt6::GuiPrivate/g'
grep -q 'find_package(Qt6GuiPrivate' CMakeLists.txt || \
  sed -i '/set(QT_DEFAULT_MAJOR_VERSION 6)/a find_package(Qt6GuiPrivate REQUIRED)' CMakeLists.txt

# Tests on Qt 6.10 need this explicit include
grep -q '^#include <QElapsedTimer>' src/tests/tests_scripts.cpp || \
  sed -i '1i #include <QElapsedTimer>' src/tests/tests_scripts.cpp

# (Optional, GCC15 nit) Make QLockFile init explicit
sed -i 's/QLockFile lockFile = lockFilePath();/QLockFile lockFile = QLockFile(lockFilePath());/' src/common/server.cpp

# Fail early if any Qt::GuiPrivate remains
if grep -R --line-number -F 'Qt::GuiPrivate' src ; then
  echo "ERROR: Qt::GuiPrivate still present after sed" >&2 ; exit 1
fi

%build
%cmake_kf6 \
  -Wno-dev \
  -DWITH_QT6:BOOL=ON \
  -DWITH_TESTS:BOOL=ON \
  -DPLUGIN_INSTALL_PREFIX=%{_libdir}/%{name}/plugins \
  -DTRANSLATION_INSTALL_PREFIX:PATH=%{_datadir}/%{name}/locale

%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/com.github.hluk.%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/com.github.hluk.%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS CHANGES.md HACKING README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/metainfo/com.github.hluk.%{name}.appdata.xml
%{_datadir}/applications/com.github.hluk.%{name}.desktop
%{_datadir}/bash-completion/completions/copyq
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/locale/
%{_datadir}/%{name}/themes/
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
