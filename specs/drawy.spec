%define rdnn        io.github.prayag2.Drawy
%define commit      b12eca1ea772d8c5b458390a78f0ae6daec88e82
%global shortcommit %{sub %{commit} 1 7}

Name:           drawy
Version:        1.0.0~^2.%{shortcommit}
Release:        %autorelease
Summary:        Your handy, infinite, brainstorming tool
# primary license: GPL-3.0-or-later
# src/resources/fonts/{FuzzyBubbles,Inter}.ttf: OFL-1.1
License:        GPL-3.0-or-later AND OFL-1.1
URL:            https://github.com/Prayag2/drawy
Source:         %{url}/archive/%{commit}/drawy-%{shortcommit}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGLWidgets)

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


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml


%files
%license LICENSE
%{_bindir}/drawy
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{rdnn}.svg
%{_metainfodir}/%{rdnn}.metainfo.xml


%changelog
%autochangelog
