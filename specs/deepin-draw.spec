Name:           deepin-draw
Version:        6.5.8
Release:        %autorelease
Summary:        A lightweight drawing tool for Linux Deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-draw
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5LinguistTools)

BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkgui)

BuildRequires:  desktop-file-utils

Requires:       deepin-qt5integration
Recommends:     deepin-manual

%description
A lightweight drawing tool for Linux Deepin.

%prep
%autosetup -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
%find_lang deepin-draw --with-qt --all-name
rm %{buildroot}%{_datadir}/deepin-draw/translations/deepin-draw.qm

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f deepin-draw.lang
%doc README.md
%license LICENSE.txt
%{_bindir}/deepin-draw
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/deepin-draw.desktop
%{_datadir}/mime/packages/deepin-draw.xml
%{_datadir}/deepin-manual/manual-assets/application/deepin-draw/
%{_datadir}/icons/deepin/apps/scalable/deepin-draw.svg
%{_datadir}/icons/hicolor/*/apps/*

%changelog
%autochangelog
