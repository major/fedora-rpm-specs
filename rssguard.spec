Name:           rssguard
Version:        4.2.3
Release:        %autorelease
Summary:        Simple yet powerful feed reader

# GPL-3.0-or-later: main program
# BSD-3-Clause:  src/network-web/librssguard/googlesuggest.*
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://github.com/martinrotter/rssguard
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Qt5WebEngine is only available on those architectures
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  qt5-linguist
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
RSS Guard is simple, light and easy-to-use RSS/ATOM feed aggregator developed
using Qt framework which supports online feed synchronization.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i 's/\r$//' README.md

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.github.rssguard.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/com.github.rssguard.appdata.xml

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_includedir}/lib%{name}/
%{_libdir}/lib%{name}.so
%{_datadir}/applications/com.github.rssguard.desktop
%{_datadir}/icons/hicolor/*/apps/rssguard.png
%{_datadir}/metainfo/com.github.rssguard.appdata.xml

%changelog
%autochangelog
