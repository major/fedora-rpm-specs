# Qt-Color-Widgets and kdsingleapplication are linked statically within
# flameshot, the standard upstream build systemd does this via a git clone
# as part of the build process
%global qtcolor_commit 352bc8f99bf2174d5724ee70623427aa31ddc26a
%global qtcolor_url https://gitlab.com/mattbas/Qt-Color-Widgets

Name: flameshot
Version: 13.3.0
Release: %autorelease

# Main code: GPL-3.0-or-later
# Logo: LAL-1.3
# Button icons: Apache-2.0
# capture/capturewidget.cpp and capture/capturewidget.h: GPL-2.0-only
# regiongrabber.cpp: LGPL-3.0-or-later
# Qt-Color-Widgets: LGPL-3.0-only OR GPL-3.0-only
# More information: https://github.com/flameshot-org/flameshot#license
License: GPL-3.0-or-later AND Apache-2.0 AND GPL-2.0-only AND LGPL-3.0-or-later AND (LGPL-3.0-only OR GPL-3.0-only) AND LAL-1.3
Summary: Powerful and simple to use screenshot software
URL: https://github.com/flameshot-org/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{qtcolor_url}/-/archive/%{qtcolor_commit}/Qt-Color-Widgets-%{qtcolor_commit}.tar.gz

BuildRequires: cmake(KDSingleApplication-qt6)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build

Requires: grim
Requires: hicolor-icon-theme
Requires: qt6-qtsvg%{?_isa}

# XDG portals are required to take screenshots on Wayland:
# https://github.com/flameshot-org/flameshot/issues/1910
Recommends: xdg-desktop-portal%{?_isa}
Recommends: (xdg-desktop-portal-gnome%{?_isa} if gnome-shell%{?_isa})
Recommends: (xdg-desktop-portal-kde%{?_isa} if plasma-workspace-wayland%{?_isa})
Recommends: (xdg-desktop-portal-wlr%{?_isa} if wlroots%{?_isa})

Provides: bundled(qt-color-widgets) = 2.2.0

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep
%autosetup -p1
mkdir -p external/Qt-Color-Widgets
tar -xf %{SOURCE1} -C external/Qt-Color-Widgets --strip-components=1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_BUNDLED_KDSINGLEAPPLICATION:BOOL=OFF \
    -DUSE_WAYLAND_CLIPBOARD:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DUSE_LAUNCHER_ABSOLUTE_PATH:BOOL=OFF
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_includedir}/QtColorWidgets
rm -rf %{buildroot}%{_libdir}/cmake/QtColorWidgets
rm -f %{buildroot}%{_libdir}/libQtColorWidgets.*
rm -f %{buildroot}%{_libdir}/pkgconfig/QtColorWidgets.pc

%find_lang Internationalization --with-qt
%fdupes %{buildroot}%{_datadir}/icons

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f Internationalization.lang
%doc README.md
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.metainfo.xml
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/%{name}.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
