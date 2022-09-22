%global repo qt5platform-plugins
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$
%global _enable_wayland 0

Name:           deepin-%{repo}
Version:        5.0.59.1
Release:        %autorelease
Summary:        Qt platform integration plugins for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dde-wayland-client)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  wayland-devel
# for libQt5EdidSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  make
Provides:       deepin-qt5dxcb-plugin = %{version}-%{release}
Provides:       deepin-qt5dxcb-plugin%{?_isa} = %{version}-%{release}
Obsoletes:      deepin-qt5dxcb-plugin < 5.0.21

%description
%{repo} is the
%{summary}.

%prep
%autosetup -p1 -n %{repo}-%{version}
rm -r xcb/libqt5xcbqpa-dev wayland/qtwayland-dev

sed -i 's|error(Not support Qt Version: .*)|INCLUDEPATH += %{_qt5_includedir}/QtXcb|' xcb/linux.pri
%if !%{_enable_wayland}
sed -i '/wayland/d' qt5platform-plugins.pro
%endif

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_qt5_plugindir}/platforms/libdxcb.so
%if %{_enable_wayland}
%{_qt5_plugindir}/platforms/libdwayland.so
%{_qt5_plugindir}/wayland-shell-integration/libkwayland-shell.so
%endif

%changelog
%autochangelog
