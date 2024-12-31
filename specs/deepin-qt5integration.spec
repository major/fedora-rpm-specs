%global repo qt5integration
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\.so$

Name:           deepin-qt5integration
Version:        5.7.5
Release:        %autorelease
Summary:        Qt platform theme integration plugins for DDE
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/qt5integration
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5ThemeSupport)

# for Qt5::ThemeSupport
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires:  cmake(DtkWidget) >= %{version}

BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(x11)

Requires:       deepin-qt5platform-plugins%{?_isa}

%description
Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep
%autosetup -p1 -n %{repo}-%{version}

%build
%cmake -DENABLE_QT_XDG_ICON_LOADER=OFF -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_qt5_plugindir}/iconengines/libdicon.so
%{_qt5_plugindir}/iconengines/libdsvgicon.so
%{_qt5_plugindir}/imageformats/libdci.so
%{_qt5_plugindir}/imageformats/libdsvg.so
%{_qt5_plugindir}/platformthemes/libqdeepin.so
%{_qt5_plugindir}/styles/libchameleon.so

%changelog
%autochangelog
