Name:           contour-terminal
Version:        0.4.1.6292
Release:        %autorelease
Summary:        Modern C++ Terminal Emulator

License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source0:        %{url}/archive/v%{version}/contour-%{version}.tar.gz

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

BuildRequires:  libunicode-devel >= 0.4.0
BuildRequires:  boxed-cpp-devel >= 1.1.0

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

Requires:       hicolor-icon-theme
Requires:       kf5-kservice
Requires:       kf5-filesystem
Requires:       ncurses-base

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
%autosetup -p1 -n contour-%{version}

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCONTOUR_TESTING=ON \
    -DCONTOUR_QT_VERSION=6 \

%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md

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
%{_datadir}/contour/shell-integration/shell-integration.fish
%{_datadir}/contour/shell-integration/shell-integration.tcsh
%{_datadir}/contour/shell-integration/shell-integration.zsh
%{_datadir}/terminfo/c/contour*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.xml

%changelog
%autochangelog
