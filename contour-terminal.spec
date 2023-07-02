%bcond_without qt6

Name:           contour-terminal
Version:        0.3.12.262
Release:        %autorelease
Summary:        Modern C++ Terminal Emulator

License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source0:        %{url}/archive/v%{version}/contour-%{version}.tar.gz
# fix build with fmt 10
Patch0:         https://github.com/contour-terminal/contour/commit/782fb7248d6fe643e7163bf57b0bcef50a81a8f7.patch

ExcludeArch:    s390x i686 ppc64le

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
BuildRequires:  libunicode-devel
BuildRequires:  libutempter-devel
# provides tic
BuildRequires:  ncurses
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%if %{?fedora} <= 37
BuildRequires:  catch-devel
%else
BuildRequires:  catch2-devel
%endif

%if %{with qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)
%else
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5X11Extras)
%endif

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
%if %{with qt6}
    -DCONTOUR_QT_VERSION=6 \
%else
    -DCONTOUR_QT_VERSION=5 \
%endif

%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/terminfo/c/contour-latest
ln -s contour %{buildroot}%{_datadir}/terminfo/c/contour-latest
rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md

%check
./%{_vpath_builddir}/src/crispy/crispy_test
./%{_vpath_builddir}/src/vtbackend/vtbackend_test

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
