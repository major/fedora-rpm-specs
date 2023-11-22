%global sdbus_version 1.3.0

Name:           xdg-desktop-portal-hyprland
Version:        1.2.5
Release:        %autorelease
Summary:        xdg-desktop-portal backend for hyprland

# xdg-desktop-portal-hyprland: BSD-3-Clause
# protocols/wlr-foreign-toplevel-management-unstable-v1.xml: HPND-sell-variant
# sdbus-cpp: LGPL-2.1-or-later WITH Qt-LGPL-exception-1.1
%if %{fedora} < 40
License:        BSD-3-Clause AND HPND-sell-variant AND LGPL-2.1-or-later WITH Qt-LGPL-exception-1.1
%else
License:        BSD-3-Clause AND HPND-sell-variant
%endif
URL:            https://github.com/hyprwm/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/Kistler-Group/sdbus-cpp/archive/v%{sdbus_version}/sdbus-%{sdbus_version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(Qt6Widgets)
%if %{fedora} >= 40
BuildRequires:  pkgconfig(sdbus-c++)
%endif
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

Requires:       dbus-common
Requires:       dbus
# required for Screenshot portal implementation
Requires:       grim
Requires:       xdg-desktop-portal
# required for hyprland-share-picker
Requires:       slurp
Requires:       qt6-qtwayland

Enhances:       hyprland
Supplements:    hyprland

%if %{fedora} < 40
Provides:       bundled(sdbus-cpp) = %{sdbus_version}
%endif

%description
%{summary}.


%prep
%autosetup
%if %{fedora} < 40
tar -xf %{SOURCE1} -C subprojects/sdbus-cpp --strip=1
%endif


%build
%if %{fedora} < 40
pushd subprojects/sdbus-cpp
%cmake -G Ninja \
    -DCMAKE_INSTALL_PREFIX=%{_builddir}/sdbus \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=OFF
%cmake_build
cmake --install %{_vpath_builddir}
popd
export PKG_CONFIG_PATH=%{_builddir}/sdbus/%{_lib}/pkgconfig
%endif
%meson
%meson_build


%install
%meson_install


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%license LICENSE
%doc README.md contrib/config.sample
%{_bindir}/hyprland-share-picker
%{_libexecdir}/%{name}
%{_datadir}/xdg-desktop-portal/portals/hyprland.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.hyprland.service
%{_userunitdir}/%{name}.service


%changelog
%autochangelog
