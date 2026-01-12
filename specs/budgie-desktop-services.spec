Name:    budgie-desktop-services
Version: 1.0.0
Release: 1%{?dist}
Summary: Daemon responsible for enabling various features of Budgie Desktop

License: MPL-2.0
URL:     https://forge.moderndesktop.dev/BuddiesOfBudgie/budgie-desktop-services
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake(KWayland)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(toml11)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

%description
The future central hub and orchestrator for Budgie Desktop 
(with a focus on Budgie 11). Today, it primarily provides Wayland-native 
display configuration for Budgie 10.10; over time it will coordinate broader 
desktop logic for Budgie 11.

%prep
%autosetup -n %{name}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_bindir}/org.buddiesofbudgie.Services
%{_datadir}/dbus-1/system.d/org.buddiesofbudgie.Services.conf
%{_sysconfdir}/labwc/autostart

%changelog
* Sat Jan 10 2026 Joshua Strobl <joshua@buddiesofbudgie.org> - 1.0.0-1
- Update to 1.0.0 stable release

* Sun Nov 23 2025 Joshua Strobl <joshua@buddiesofbudgie.org> - 0.0.1-1
- Initial inclusion of budgie-desktop-services
