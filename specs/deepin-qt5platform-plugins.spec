%global repo qt5platform-plugins
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$

Name:           deepin-qt5platform-plugins
Version:        5.7.5
Release:        %autorelease
Summary:        Qt platform integration plugins for Deepin Desktop Environment
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/qt5platform-plugins
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5XcbQpa)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5EdidSupport)
BuildRequires:  cmake(Qt5XkbCommonSupport)

BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(xkbcommon)

BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

Provides:       deepin-qt5dxcb-plugin = %{version}-%{release}
Provides:       deepin-qt5dxcb-plugin%{?_isa} = %{version}-%{release}
Obsoletes:      deepin-qt5dxcb-plugin < 5.0.21

%description
qt5platform-plugins is the Qt platform integration plugin for Deepin Desktop
Environment.

%prep
%autosetup -p1 -n %{repo}-%{version}

# https://github.com/linuxdeepin/developer-center/issues/7217
# remove wayland support
sed -i '/wayland/d' CMakeLists.txt

# remove redundant bundled code
rm -r xcb/{libqt5xcbqpa-dev,libqt6xcbqpa-dev}

%build
%cmake \
    -DQT_XCB_PRIVATE_HEADERS=%{_qt5_headerdir}/QtXcb \
    -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_qt5_plugindir}/platforms/libdxcb.so

%changelog
%autochangelog
