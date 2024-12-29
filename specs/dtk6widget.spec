Name:           dtk6widget
Version:        6.0.25
Release:        %autorelease
Summary:        Deepin base graphical widgets library
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtk6widget
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

BuildRequires:  cmake(Dtk6Core) >= %{version}
BuildRequires:  cmake(Dtk6Gui) >= %{version}

BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)

BuildRequires:  doxygen

%description
Deepin Tool Kit Widget(DtkWidget) provides the base widgets on Deepin.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake -GNinja \
    -DQCH_INSTALL_DESTINATION=%{_qt6_docdir} \
    -DDTK_VERSION=%{version} \
%cmake_build

%install
%cmake_install
%find_lang dtkwidget --all-name --with-qt

%files -f dtkwidget.lang
%license LICENSE
%doc README.md
%{_libdir}/libdtk6widget.so.6*
%dir %{_libdir}/dtk6
%{_libdir}/dtk6/DWidget/

%files devel
%{_libdir}/libdtk6widget.so
%{_includedir}/dtk6/DWidget/
%{_libdir}/cmake/Dtk6Widget/
%{_libdir}/pkgconfig/dtk6widget.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
