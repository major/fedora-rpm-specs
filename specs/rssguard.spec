Name:           rssguard
Version:        4.8.3
Release:        %autorelease
Summary:        Simple yet powerful feed reader

# GPL-3.0-only: main program
# GPL-3.0-or-later: src/librssguard/network-web/webengine/networkurlinterceptor
# LGPL-2.1-only: src/librssguard-gmail/src/3rd-party/richtexteditor/
# LGPL-3.0-only: src/librssguard/miscellaneous/regexfactory
# LGPL-3.0-or-later: src/librssguard/3rd-party/mimesis
# AGPL-3.0-or-later: src/librssguard/network-web/oauth2service
# BSD-3-Clause: 
# - src/librssguard/network-web/googlesuggest.*
# - src/librssguard/3rd-party/sc
# MIT: src/librssguard/3rd-party/boolinq
# blessing: src/librssguard/3rd-party/sqlite/
License:        GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND BSD-3-Clause AND MIT AND AGPL-3.0-or-later AND blessing
URL:            https://github.com/martinrotter/rssguard
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Qt6WebEngine is only available on those architectures
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  cmake >= 3.14.0
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
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
BuildRequires:  pkgconfig(mpv)
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
%cmake -DREVISION_FROM_GIT=OFF \
       -DNO_UPDATE_CHECK=OFF
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
%{_datadir}/applications/io.github.martinrotter.rssguard.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.martinrotter.rssguard.png
%{_datadir}/metainfo/io.github.martinrotter.rssguard.metainfo.xml
%{_includedir}/lib%{name}/
%{_libdir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
