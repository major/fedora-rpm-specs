%global forgeurl https://github.com/contour-terminal/contour
Version:        0.6.1.7494
%forgemeta

Name:           contour-terminal
Release:        %autorelease
Summary:        Modern C++ Terminal Emulator
License:        Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

ExclusiveArch:  x86_64 aarch64

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  fmt-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  range-v3-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  libxcb-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libutempter-devel
BuildRequires:  pkgconfig(libssh2)

BuildRequires:  libunicode-devel
BuildRequires:  cmake(boxed-cpp)
BuildRequires:  cmake(reflection-cpp)

# provides tic
BuildRequires:  ncurses

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  catch-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Core5Compat)

Requires:       qt6-qt5compat
Requires:       hicolor-icon-theme
Requires:       kf6-kservice
Requires:       kf6-filesystem
Requires:       ncurses-term

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCONTOUR_TESTING=ON \

%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md
# already included in ncurses-term package
rm %{buildroot}%{_datadir}/terminfo/c/contour

%check
%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/contour
%{_datadir}/applications/*.desktop
%{_datadir}/kservices5/ServiceMenus/*.desktop
%dir %{_datadir}/contour
%dir %{_datadir}/contour/shell-integration
%{_datadir}/contour/shell-integration/shell-integration.bash
%{_datadir}/contour/shell-integration/shell-integration.fish
%{_datadir}/contour/shell-integration/shell-integration.tcsh
%{_datadir}/contour/shell-integration/shell-integration.zsh
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.xml

%changelog
%autochangelog
