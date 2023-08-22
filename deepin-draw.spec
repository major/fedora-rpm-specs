Name:           deepin-draw
Version:        6.0.6
Release:        %autorelease
Summary:        A lightweight drawing tool for Linux Deepin
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-draw
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires:  gcc-c++
BuildRequires:  freeimage-devel
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  make
Requires:       deepin-notifications
Requires:       deepin-qt5integration
Recommends:     deepin-manual

%description
A lightweight drawing tool for Linux Deepin.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/deepin-manual/
%{_datadir}/icons/deepin/
%{_datadir}/icons/hicolor/*/apps/*

%changelog
%autochangelog
