Name:           deepin-screensaver
Version:        6.5.4
Release:        %autorelease
Summary:        Screensaver Tool
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-screensaver
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb)

Requires:       xscreensaver-extras
Requires:       xscreensaver-gl-extras

%description
Deepin screensaver viewer and tools.

%prep
%autosetup -p1

sed -i 's|/lib|%{_libdir}|' cmake/translation-generate.cmake

sed -i 's|${qt_required_components}|${qt_required_components} GuiPrivate|' src/CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE.txt
%dir %{_sysconfdir}/deepin-screensaver
%dir %{_sysconfdir}/deepin-screensaver/deepin-custom-screensaver
%{_sysconfdir}/deepin-screensaver/deepin-custom-screensaver/deepin-custom-screensaver.desktop
%{_bindir}/deepin-screensaver-preview
%{_bindir}/deepin-screensaver
%{_datadir}/dbus-1/interfaces/com.deepin.ScreenSaver.xml
%{_datadir}/dbus-1/services/com.deepin.ScreenSaver.service
%{_datadir}/dconfig/overrides/org.deepin.screensaver/
%{_datadir}/deepin-custom-screensaver/
%{_datadir}/deepin-screensaver/
%{_datadir}/dsg/configs/org.deepin.screensaver/
%{_prefix}/lib/deepin-screensaver/

%changelog
%autochangelog
