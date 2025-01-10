# niri isn't packaged in Fedora
%bcond niri_session 0
# we don't want to support hyprland
%bcond hyprland_session 0

Name:           lxqt-wayland-session
Version:        0.1.1
Release:        4%{?dist}
Summary:        Wayland session files for LXQt
# See "LICENSE" for a breakdown of license usage
License:        LGPL-2.1-only AND GPL-3.0-only AND MIT AND GPL-2.0-only AND BSD-3-Clause
URL:            https://lxqt-project.org/

Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         0001-adjust-labwc-pointer-speed.patch
BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  perl

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  cmake(lxqt)

BuildRequires:  cmake(KF6WindowSystem)

%description
Files needed for the LXQt Wayland Session: Wayland session start script,
its desktop entry for display managers and default configurations for
actually supported compositors.

%files
%doc README.md
%license COPYING.LESSER LICENSE
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/wayland
%dir %{_datadir}/lxqt/wayland/firstrun
%{_bindir}/startlxqtwayland
%{_datadir}/wayland-sessions/lxqt-wayland.desktop
%{_datadir}/lxqt/wayland/firstrun/autostart
%{_datadir}/lxqt/wallpapers/origami-dark-labwc.png

%dnl ------------------------------------------------------------------

%if %{with hyprland_session}
%package -n     lxqt-hyprland-session
Summary:        Session files for LXQt-Hyprland
License:        BSD-3-Clause
Requires:       %{name} = %{version}-%{release}
Requires:       hyprland
Supplements:    (%{name} and hyprland)

%description -n lxqt-hyprland-session
This package contains the files necessary to use Hyprland as the Wayland
compositor with LXQt.

%files -n lxqt-hyprland-session
%license LICENSE.BSD
%{_datadir}/lxqt/wayland/lxqt-hyprland.conf
%endif

%dnl ------------------------------------------------------------------

%if %{with niri_session}
%package -n     lxqt-niri-session
Summary:        Session files for LXQT-niri
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       niri
Supplements:    (%{name} and niri)

%description -n lxqt-niri-session
This package contains the files necessary to use niri as the Wayland compositor
for LXQt.

%files -n lxqt-niri-session
%license COPYING
%{_datadir}/lxqt/wayland/lxqt-niri.kdl
%endif

%dnl ------------------------------------------------------------------

%package -n     lxqt-river-session
Summary:        Session files for LXQt-river
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       river
Supplements:    (%{name} and river)

%description -n lxqt-river-session
This package contains the files necessary to use river as the Wayland
compositor with LXQt.

%files -n lxqt-river-session
%license COPYING
%{_datadir}/lxqt/wayland/lxqt-river-init

%dnl ------------------------------------------------------------------

%package -n     lxqt-sway-session
Summary:        Session files for LXQt-Sway
License:        MIT
Requires:       %{name} = %{version}-%{release}
Requires:       sway
Supplements:    (%{name} and sway)

%description -n lxqt-sway-session
This package contains the files necessary to use Sway as the Wayland compositor
with LXQt.

%files -n lxqt-sway-session
%license LICENSE.MIT
%{_datadir}/lxqt/wayland/lxqt-sway.config

%dnl ------------------------------------------------------------------

%package -n     lxqt-wayfire-session
Summary:        Session files for LXQt-wayfire
License:        MIT
Requires:       %{name} = %{version}-%{release}
Requires:       wayfire
Supplements:    (%{name} and wayfire)

%description -n lxqt-wayfire-session
This package contains the files necessary to use wayfire as the Wayland
compositor with LXQt.

%files -n lxqt-wayfire-session
%license LICENSE.MIT
%{_datadir}/lxqt/wayland/lxqt-wayfire.ini

%dnl ------------------------------------------------------------------

%package -n     lxqt-labwc-session
Summary:        Session files and theme for LXQt-labwc
License:        CC-BY-SA-4.0 AND GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       labwc >= 0.7.2
Requires:       swaybg
Requires:       swayidle
Requires:       swaylock
Supplements:    (%{name} and labwc)

%description -n lxqt-labwc-session
This package contains the openbox themes and other files necessary to use
labwc as the Wayland compositor with LXQt.

%files -n lxqt-labwc-session
%license LICENSE.GPLv2
%dir %{_datadir}/lxqt/wallpapers
%dir %{_datadir}/lxqt/wayland/labwc
%dir %{_datadir}/lxqt/graphics
%{_datadir}/themes/Vent/
%{_datadir}/themes/Vent-dark/
%{_datadir}/lxqt/wallpapers/origami-dark-labwc.png
%{_datadir}/lxqt/wayland/labwc/README
%{_datadir}/lxqt/wayland/labwc/autostart
%{_datadir}/lxqt/wayland/labwc/environment
%{_datadir}/lxqt/wayland/labwc/menu.xml
%{_datadir}/lxqt/wayland/labwc/rc.xml
%{_datadir}/lxqt/wayland/labwc/themerc
%{_datadir}/lxqt/wayland/labwc/themerc-override
%{_datadir}/lxqt/graphics/lxqt-labwc.png

%dnl ------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version} -S git_am

%build
%cmake
%cmake_build

%install
%cmake_install

%if ! %{with hyprland_session}
# Drop hyprland session files
rm -v %{buildroot}%{_datadir}/lxqt/wayland/lxqt-hyprland.conf
%endif

%if ! %{with niri_session}
# Drop niri session files
rm -v %{buildroot}%{_datadir}/lxqt/wayland/lxqt-niri.kdl
%endif


%changelog
* Wed Jan 08 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.1.1-4
- Add patch to adjust default pointer speed in labwc session

* Sun Dec 22 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.1.1-3
- Disable hyprland session option

* Tue Dec 17 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.1.1-2
- Disable niri session subpackage until niri is packaged (rhbz#2332801)

* Sun Dec 15 2024 Steve Cossette <farchord@gmail.com> - 0.1.1-1
- Initial
