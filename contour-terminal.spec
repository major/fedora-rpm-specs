Name:           contour-terminal
Version:        0.4.3.6442
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
BuildRequires:  cmake(boxed-cpp)

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
Requires:       kf5-kservice
Requires:       kf5-filesystem
Requires:       ncurses-term

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

- Available on all 4 major platforms, Linux, macOS, FreeBSD, Windows.
- GPU-accelerated rendering.
- Font ligatures support (such as in Fira Code).
- Unicode: Emoji support (-: 🌈 💝 😛 👪 - including ZWJ, VS15, VS16 emoji :-)
- Unicode: Grapheme cluster support
- Bold and italic fonts
- High-DPI support.
- Vertical Line Markers (quickly jump to markers in your history!)
- Vi-like input modes for improved selection and copy'n'paste experience and Vi-like scrolloff feature.
- Blurred behind transparent background support for Windows 10 and above as well as the KDE and GNOME desktop environment on Linux.
- Blurrable Background image support.
- Runtime configuration reload
- 256-color and Truecolor support
- Key binding customization
- Color Schemes
- Profiles (grouped customization of: color scheme, login shell, and related behaviours)
- Synchronized rendering (via SM ? 2026 / RM ? 2026)
- Text reflow (configurable via SM ? 2028 / RM ? 2028)
- Clickable hyperlinks via OSC 8
- Clipboard setting via OSC 52
- Sixel inline images
- Terminal page buffer capture VT extension to quickly extract contents.
- Builtin Fira Code inspired progress bar support.
- Read-only mode, protecting against accidental user-input to the running application, such as Ctrl+C.
- VT320 Host-programmable and Indicator status line support.

%prep
%autosetup -p1 -n contour-%{version}

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
%{_datadir}/contour/shell-integration/shell-integration.fish
%{_datadir}/contour/shell-integration/shell-integration.tcsh
%{_datadir}/contour/shell-integration/shell-integration.zsh
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.xml

%changelog
%autochangelog
