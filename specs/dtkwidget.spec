Name:           dtkwidget
Version:        5.7.5
Release:        %autorelease
Summary:        Deepin tool kit widget modules
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires:  cmake(DtkCore) >= %{version}
BuildRequires:  cmake(DtkGui) >= %{version}

BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)

BuildRequires:  doxygen

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1

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
%{_libdir}/libdtkwidget.so.5*
%{_libdir}/dtk5/DWidget
%{_datadir}/dtk5/DWidget

%files devel
%{_includedir}/dtk5/DWidget/
%{_libdir}/cmake/DtkWidget/
%{_libdir}/pkgconfig/dtkwidget.pc
%{_libdir}/libdtkwidget.so
%{_qt5_docdir}/dtkwidget.qch
%{_qt5_archdatadir}/mkspecs/modules/*.pri

%changelog
%autochangelog
