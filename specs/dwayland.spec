Name:           dwayland
Version:        5.25.0
Release:        %autorelease
Summary:        Qt-style Client and Server library wrapper for the Wayland libraries
License:        (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:            https://github.com/linuxdeepin/dwayland
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         dwayland-5.25.0-unsigned-types.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires:  deepin-wayland-protocols-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  wayland-devel

Requires:       kf5-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
# fix error: XDG_RUNTIME_DIR is invalid or not set in the environment
mkdir tmp
export XDG_RUNTIME_DIR="$PWD/tmp"
SKIP_TESTS=
SKIP_TESTS+='kwayland-testWaylandSurface|'
SKIP_TESTS+='kwayland-testWindowmanagement|'
SKIP_TESTS+='kwayland-testXdgDecoration|'
SKIP_TESTS+='kwayland-testServerSideDecoration|'
SKIP_TESTS+='kwayland-testKeyboardShortcutsInhibitorInterface|'
%ctest -E $SKIP_TESTS

%files
%license LICENSES/*
%doc README.md
%{_kf5_datadir}/qlogging-categories5/*categories
%{_libdir}/libDWaylandClient.so.5*
%{_libdir}/libDWaylandServer.so.5*

%files devel
%{_libdir}/libDWaylandClient.so
%{_libdir}/libDWaylandServer.so
%{_includedir}/DWayland/
%{_includedir}/dwayland_version.h
%{_libdir}/cmake/DWayland/
%{_qt5_archdatadir}/mkspecs/modules/qt_DWaylandClient.pri

%changelog
%autochangelog
