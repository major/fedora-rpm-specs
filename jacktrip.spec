Name:           jacktrip
Version:        1.9.0
Release:        %autorelease
Summary:        A system for high-quality audio network performance over the Internet

License:        MIT and GPL-3.0-or-later and LGPL-3.0-only
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson, cmake, gcc-c++
BuildRequires:  python3-pyyaml, python3-jinja2
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(rtaudio)
BuildRequires:  help2man
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Requires:       qt5-qtquickcontrols2%{?_isa}
Requires:       qt5-qtsvg%{?_isa}
Obsoletes:      jacktrip-doc < 1.4.0

%description
JackTrip is a Linux and Mac OS X-based system used for multi-machine
network performance over the Internet. It supports any number of
channels (as many as the computer/network can handle) of
bidirectional, high quality, uncompressed audio signal steaming.

%prep
%autosetup -p1
rm -rf externals
mkdir -p externals/weakjack

%build
%meson -Drtaudio=enabled
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%check
%meson_test

%files
%doc README.md
%license LICENSE.md LICENSES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/org.jacktrip.JackTrip.desktop
%{_metainfodir}/org.jacktrip.JackTrip.metainfo.xml

%changelog
%autochangelog
