Name:           dtkwidget
Version:        5.6.12
Release:        %autorelease
Summary:        Deepin tool kit widget modules
# migrated to SPDX
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  %{_bindir}/doxygen
BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  dtkgui-devel
BuildRequires:  dtkcore-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5UiPlugin)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  cups-devel
BuildRequires:  gtest-devel

# libQt5Gui.so.5(Qt_5.10.1_PRIVATE_API)(64bit) needed by dtkwidget-2.0.6.1-1.fc29.x86_64
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  make


%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcore-devel%{?_isa}
Requires:       dtkgui-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DHUNTER_ENABLED=OFF \
       -DLINUXNAME="fedora" \
       -DNOTPACKAGE=OFF \
       -DBUILD_DOCS=ON \
       -DQCH_INSTALL_DESTINATION=%{_qt5_docdir}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_libdir}/dtk5/DWidget
%{_datadir}/dtk5/DWidget
%{_datadir}/dsg/

%files devel
%{_includedir}/dtk5/DWidget
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/DtkWidget/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_qt5_docdir}/%{name}.qch

%changelog
%autochangelog
