Name:           rssguard
Version:        4.5.1
Release:        %autorelease
Summary:        Simple yet powerful feed reader

# GPL-3.0-or-later: main program
# LGPL-3.0-or-later: src/librssguard/3rd-party/mimesis
# BSD-3-Clause: src/librssguard/network-web/googlesuggest.*
# BSD-4-Clause: src/librssguard/3rd-party/sc
# MIT: src/librssguard/3rd-party/boolinq
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND BSD-4-Clause AND MIT
URL:            https://github.com/martinrotter/rssguard
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Qt5WebEngine is only available on those architectures
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(libsqlite3x)
Requires:       hicolor-icon-theme

Provides:       bundled(boolinq) = 3.0.1-1
Provides:       bundled(mimesis)
Provides:       bundled(simplecrypt) = 3.1-1

%description
RSS Guard is simple, light and easy-to-use RSS/ATOM feed aggregator developed
using Qt framework which supports online feed synchronization.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i 's/\r$//' README.md

%build
%cmake -DBUILD_WITH_QT6=1
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.rssguard.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.rssguard.metainfo.xml

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_includedir}/lib%{name}/
%{_libdir}/lib%{name}.so
%{_datadir}/applications/io.github.martinrotter.rssguard.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.martinrotter.rssguard.png
%{_datadir}/metainfo/io.github.martinrotter.rssguard.metainfo.xml

%changelog
%autochangelog
