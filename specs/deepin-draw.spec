Name:           deepin-draw
Version:        6.5.33
Release:        %autorelease
Summary:        A lightweight drawing tool for Linux Deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-draw
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)

BuildRequires:  desktop-file-utils

#Requires:       deepin-qt6integration
#Recommends:     deepin-manual

%description
A lightweight drawing tool for Linux Deepin.

%prep
%autosetup -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/deepin-draw
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/deepin-draw.desktop
%{_datadir}/mime/packages/deepin-draw.xml
%{_datadir}/deepin-manual/manual-assets/application/deepin-draw/
%{_datadir}/deepin-draw/
%{_datadir}/icons/deepin/apps/scalable/deepin-draw.svg
%{_datadir}/icons/hicolor/*/apps/*

%changelog
%autochangelog
