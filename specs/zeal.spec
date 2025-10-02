%global debug_package %{nil}

Name:           zeal
Version:        0.7.2
Release:        %autorelease
Summary:        Offline documentation browser inspired by Dash

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://zealdocs.org/
Source:         https://github.com/zealdocs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-apply-websettings.patch
Patch1:         zeal-fix-build-against-qt-6-10.patch

ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  cmake(Qt6Core) >= 6.2.0
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6Network)

BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
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
  -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.zealdocs.zeal.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.zealdocs.zeal.appdata.xml


%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/org.zealdocs.zeal.desktop
%{_metainfodir}/org.zealdocs.zeal.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
%autochangelog
