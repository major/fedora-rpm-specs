%define rdnn        org.kde.drawy
%define commit      6387aa20ef967ee1a4f922009dfe1aaf13519574
%global shortcommit %{sub %{commit} 1 7}

Name:           drawy
Version:        1.0.0~^3.%{shortcommit}
Release:        %autorelease
Summary:        Your handy, infinite, brainstorming tool
# primary license: GPL-3.0-or-later
# src/resources/fonts/{FuzzyBubbles,Inter}.ttf: OFL-1.1
License:        GPL-3.0-or-later AND OFL-1.1
URL:            https://invent.kde.org/graphics/drawy
Source:         %{url}/-/archive/%{commit}/drawy-%{shortcommit}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  pkgconfig(libzstd)

# for desktop-file-validate command
BuildRequires:  desktop-file-utils
# for appstream-util command
BuildRequires:  libappstream-glib

# for ownership of icon parent directories
Requires:       hicolor-icon-theme


%description
Drawy is a work-in-progress infinite whiteboard tool written in Qt/C++, which
aims to be a native-desktop alternative to the amazing web-based Excalidraw.


%prep
%autosetup -n drawy-%{commit}


%conf
%cmake -DCMAKE_BUILD_TYPE=Release


%build
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml


%files -f %{name}.lang
%license LICENSES/GPL-3.0-or-later.txt LICENSES/OFL-1.1.txt
%{_bindir}/drawy
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{rdnn}.svg
%{_datadir}/qlogging-categories6/drawy.categories
%{_metainfodir}/%{rdnn}.metainfo.xml


%changelog
%autochangelog
