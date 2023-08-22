Name:           deepin-editor
Version:        6.0.10
Release:        %autorelease
Summary:        Simple editor for Linux Deepin
# SPDX migration
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  freeimage-devel
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(DFrameworkdbus)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  enca-devel
BuildRequires:  uchardet-devel
BuildRequires:  libchardet-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  libicu-devel

Requires:       deepin-notifications
Requires:       deepin-qt5integration
Recommends:     deepin-manual

%description
%{summary}.

%prep
%autosetup -p1

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
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
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/deepin-manual/
%{_datadir}/dsg/

%changelog
%autochangelog
