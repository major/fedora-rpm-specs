Name:           dtkgui
Version:        5.7.5
Release:        %autorelease
Summary:        Deepin dtkgui
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkgui
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires:  cmake(DtkCore) >= %{version}
#BuildRequires:  cmake(DtkBuildHelper) >= %{version}
BuildRequires:  dtkcommon-devel >= %{version}
BuildRequires:  cmake(TreelandProtocols)

BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(wayland-client)

BuildRequires:  doxygen

%description
Dtkgui is the GUI module for DDE look and feel.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup

%build
%cmake -GNinja \
    -DDTK_VERSION=%{version} \
    -DQCH_INSTALL_DESTINATION=%{_qt5_docdir}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libdtkgui.so.5*
%{_libexecdir}/dtk5/DGui/

%files devel
%{_includedir}/dtk5/DGui/
%{_libdir}/pkgconfig/dtkgui.pc
%{_libdir}/cmake/DtkGui/
%{_libdir}/libdtkgui.so
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtkgui.pri
%{_qt5_docdir}/dtkgui.qch

%changelog
%autochangelog
