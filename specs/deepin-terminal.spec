Name:           deepin-terminal
Version:        6.5.22
Release:        %autorelease
Summary:        Default terminal emulation application for Deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-terminal
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Dtk6Widget)

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(xcb-ewmh)

BuildRequires:  cmake(lxqt2-build-tools)
# required by lxqt2-build-tools
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  libicu-devel
BuildRequires:  pkgconfig(chardet)
BuildRequires:  uchardet-devel

Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
Deepin Terminal is an advanced terminal emulator with workspace , multiple
windows, remote management, quake mode and other features.

%prep
%autosetup -p1

sed -i 's|SHARED|STATIC|' 3rdparty/terminalwidget/CMakeLists.txt
sed -i 's|/lib|%{_libdir}|' cmake/translation-generate.cmake
sed -i 's|DDE;||' src/deepin-terminal.desktop

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_includedir}/terminalwidget6/ \
    %{buildroot}%{_libdir}/libterminalwidget6.a \
    %{buildroot}%{_libdir}/cmake/terminalwidget6/ \
    %{buildroot}%{_libdir}/pkgconfig/terminalwidget6.pc \
    %{buildroot}%{_datadir}/terminalwidget6/

# debuginfo generation fails with debugedit >= 5.1
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/GG4LQYBEKGWAGFSJ5PKTKJAOHLAB3A27/#QYIK5E642MDB4NGBXLRLLTMU7HAJOVV5
chmod u+w %{buildroot}%{_bindir}/deepin-terminal

%files
%doc README.md
%license LICENSE
%{_bindir}/deepin-terminal
%{_datadir}/applications/deepin-terminal.desktop
%dir %{_datadir}/deepin-terminal
%{_datadir}/deepin-terminal/translations/
%{_datadir}/deepin-manual/manual-assets/application/deepin-terminal/
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.terminal.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.terminal.json
%{_datadir}/dsg/configs/org.deepin.terminal/
%{_datadir}/icons/hicolor/scalable/apps/deepin-terminal.svg

%changelog
%autochangelog
