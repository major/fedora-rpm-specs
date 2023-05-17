%global commit 3445aff746aee165da47c912e1a3f501e8cd3f57
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20230504

%global qt5_minver 5.15.0
%global kf5_minver 5.83.0
%global kp5_minver 5.27.5

Name:           xwaylandvideobridge
Version:        0~git%{commitdate}.%{shortcommit}
Release:        2%{?dist}
Summary:        Utility to allow streaming Wayland windows to X applications

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/system/xwaylandvideobridge
Source0:        %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules >= %{kf5_minver}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_minver}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_minver}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_minver}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_minver}
BuildRequires:  cmake(KF5I18n) >= %{kf5_minver}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_minver}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_minver}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_minver}
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  cmake(KPipeWire) >= %{kp5_minver}

Requires:       hicolor-icon-theme

# Requires at least KPipeWire 5.27.5
Requires:       kpipewire%{?_isa} >= %{kp5_minver}

%description
By design, X11 applications can't access window or screen contents
for wayland clients. This is fine in principle, but it breaks screen
sharing in tools like Discord, MS Teams, Skype, etc and more.

This tool allows us to share specific windows to X11 clients,
but within the control of the user at all times.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake_kf5 -GNinja
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%doc README.md
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml



%changelog
* Mon May 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20230504.3445aff-2
- Add dependency on hicolor-icon-theme

* Wed May 10 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20230504.3445aff-1
- Initial package
