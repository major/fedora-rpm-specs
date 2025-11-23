%define commit      4fec01b234a6aa909059a750ec654cc6a3136970
%global shortcommit %{sub %{commit} 1 7}

Name:           drawy
Version:        1.0.0~^1.%{shortcommit}
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

for size in 16 32 256 512; do
    install -D -p -m 644 assets/logo-$size.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/drawy.png
done
install -D -p -m 644 assets/logo.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/drawy.svg

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    deploy/appimage/AppDir/usr/share/applications/drawy.desktop


%files
%license LICENSE
%{_bindir}/drawy
%{_datadir}/applications/drawy.desktop
%{_datadir}/icons/hicolor/*/apps/drawy.*


%changelog
%autochangelog
