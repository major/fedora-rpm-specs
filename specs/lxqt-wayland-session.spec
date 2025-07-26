# we don't want to support hyprland
%bcond hyprland_session 0

Name:           lxqt-wayland-session
Version:        0.2.0
Release:        3%{?dist}
Summary:        Wayland session files for LXQt
# See "LICENSE" for a breakdown of license usage
License:        LGPL-2.1-only AND GPL-3.0-only AND MIT AND GPL-2.0-only AND BSD-3-Clause
URL:            https://lxqt-project.org/

Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        default-compositor-miriway

Patch0:         0001-configuration-changes-for-default-labwc-session.patch
Patch1:         0002-configuration-changes-for-default-wayfire-session.patch
Patch2:         0003-configuration-changes-for-default-niri-session.patch
Patch3:         0004-configuration-adds-miriway-session.patch
Patch4:         0005-configuration-changes-for-default-river-session.patch
Patch5:         0006-configuration-changes-for-default-sway-session.patch
BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  perl

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  cmake(lxqt)

BuildRequires:  cmake(KF6WindowSystem)

Requires:       desktop-backgrounds-compat
# Require the default compositor
Requires:       %{name}-default-compositor
# We prefer miriway
Suggests:       %{name}-default-compositor-miriway

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
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/startlxqtwayland.1.gz


%dnl ------------------------------------------------------------------
%package -n     %{name}-default-compositor-miriway
Summary:        Sets default compositor to miriway
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       lxqt-miriway-session = %{version}-%{release}
Provides:       %{name}-default-compositor
Conflicts:      %{name}-default-compositor

%description -n %{name}-default-compositor-miriway
Sets the default compositor to miriway, and provides the miriway session
setup

%files -n %{name}-default-compositor-miriway
%license COPYING
%{_datadir}/lxqt/wayland/default-compositor

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
%package -n     lxqt-miriway-session
Summary:        Session files for LXQt-miriway
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
# For flag to customize decoration preference
Requires:       miriway >= 24.11.1-1
# For mir fixes for LXQt
Requires:       mir-server-libs >= 2.19.3-3
Supplements:    (%{name} and miriway)

%description -n lxqt-miriway-session
This package contains the files necessary to use Miriway as the Wayland
compositor with LXQt

%files -n lxqt-miriway-session
%license COPYING
%attr(0755,root,root) %{_datadir}/lxqt/wayland/miriway/lxqt-miriway-wrapper
%{_datadir}/lxqt/wayland/miriway/miriway-shell.config

%dnl ------------------------------------------------------------------

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

%dnl ------------------------------------------------------------------

%package -n     lxqt-river-session
Summary:        Session files for LXQt-river
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       river
Recommends:     swaybg
Recommends:     jxl-pixbuf-loader
Supplements:    (%{name} and river)

%description -n lxqt-river-session
This package contains the files necessary to use river as the Wayland
compositor with LXQt.

%files -n lxqt-river-session
%license COPYING
%attr(0755,root,root) %{_datadir}/lxqt/wayland/lxqt-river-init

%dnl ------------------------------------------------------------------

%package -n     lxqt-sway-session
Summary:        Session files for LXQt-Sway
License:        MIT
Requires:       %{name} = %{version}-%{release}
Requires:       sway
Recommends:     swaybg
Recommends:     jxl-pixbuf-loader
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
Recommends:     swaybg
Recommends:     jxl-pixbuf-loader
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
Requires:       jxl-pixbuf-loader
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
cp -a %{SOURCE1} default-compositor-miriway

%build
%cmake
%cmake_build

%install
%cmake_install

install -m0644 default-compositor-miriway %{buildroot}%{_datadir}/lxqt/wayland/default-compositor

%if ! %{with hyprland_session}
# Drop hyprland session files
rm -v %{buildroot}%{_datadir}/lxqt/wayland/lxqt-hyprland.conf
%endif

%fdupes -s %{buildroot}%{_datadir}/themes/

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 20 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0-2
- Restore niri support

* Fri Apr 18 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.2.0-1
- 0.2.0

* Fri Mar 28 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.1.1-13
- Add LABWC_CONFIG_DIR env variable to labwc session

* Thu Mar 13 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.1-12
- Refresh miriway session patch with latest version of upstream submission

* Fri Feb 21 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.1-11
- Refresh miriway session patch with latest version of upstream submission

* Sun Feb 16 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.1-10
- Ensure the default compositor configuration is installed

* Sun Feb 16 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.1.1-9
- Adjusted session configs for new jxl wallpapers

* Sat Feb 15 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.1-8
- Refresh miriway session patch to match upstream submission

* Fri Feb 07 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.1.1-7
- Add patch to enable setting of default wayland compositor
- Added configuration file and subpackage for default session

* Tue Jan 21 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.1.1-6
- Added patches to adjust configurations in all sessions
- Added patch to enable miriway session

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.1.1-4
- Add patch to adjust default pointer speed in labwc session

* Sun Dec 22 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.1.1-3
- Disable hyprland session option

* Tue Dec 17 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.1.1-2
- Disable niri session subpackage until niri is packaged (rhbz#2332801)

* Sun Dec 15 2024 Steve Cossette <farchord@gmail.com> - 0.1.1-1
- Initial
