Name:           zeal
Version:        0.9.1
Release:        %autorelease
Summary:        Offline documentation browser inspired by Dash

License:        GPL-3.0-or-later
URL:            https://zealdocs.org/
Source:         https://github.com/zealdocs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  cmake(Qt6Core) >= 6.5.1
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(tomlplusplus)
BuildRequires:  cmake(httplib)

BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
Zeal is a simple offline documentation browser inspired by Dash.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
# turn off shared libs building:
# - it's only used from Zeal itself
# - build scripts not configured to install the lib
%cmake_qt6 \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DZEAL_FEATURE_UPDATE_CHECK:BOOL=OFF
%cmake_build


%install
%cmake_install


%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/org.zealdocs.zeal.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.zealdocs.zeal.appdata.xml


%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/org.zealdocs.zeal.desktop
%{_metainfodir}/org.zealdocs.zeal.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-tray.svg


%changelog
%autochangelog
