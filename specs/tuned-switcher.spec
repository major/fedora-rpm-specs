Name: tuned-switcher
Version: 0.9.1
Release: %autorelease

# Main code - GPL-3.0-or-later.
# Icon - Apache-2.0.
License: GPL-3.0-or-later AND Apache-2.0
Summary: Simple utility to manipulate the Tuned service
URL: https://github.com/xvitaly/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 43
ExcludeArch: %{ix86}
%endif

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build
BuildRequires: pandoc

Requires: hicolor-icon-theme
Requires: tuned

%description
Tuned Switcher is a simple utility for managing performance profiles using
the Tuned service.

Tuned is a daemon for monitoring and adaptive tuning of system devices.
In order to use this program, a daemon must be installed on your system.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DOCS:BOOL=OFF \
    -DBUILD_MANPAGE:BOOL=ON
%cmake_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%cmake_install
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc docs/*
%license COPYING licenses/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_metainfodir}/*.metainfo.xml
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
