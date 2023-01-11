%bcond_without  sddm
%global sway_ver 1.7

Name:           sway-config-fedora
Version:        0.1.1
Release:        %autorelease
Summary:        Fedora Sway Spin configuration for Sway

License:        MIT
URL:            https://gitlab.com/fedora/sigs/sway/sway-config-fedora
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

Requires:       sway >= %{sway_ver}
Provides:       sway-config = %{sway_ver}+%{version}-%{release}
Conflicts:      sway-config

# Lack of graphical drivers may hurt the common use case
Requires:       mesa-dri-drivers
# Logind needs polkit to create a graphical session
Requires:       polkit
# dmenu (as well as rxvt any many others) requires XWayland on Sway
Requires:       xorg-x11-server-Xwayland

# Install configs and scripts for better integration with systemd user session
Recommends:     sway-systemd
# Minimal installation doesn't include Qt Wayland backend
Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

### Collected from /etc/sway/config and 50-fedora.conf
Recommends: foot
Recommends: libnotify
Recommends: rofi-wayland
Requires: /usr/bin/pgrep
Requires: /usr/bin/pkill
Requires: desktop-backgrounds-compat
Requires: grimshot
Requires: light
Requires: lxqt-policykit
Requires: playerctl
Requires: pulseaudio-utils
Requires: swaybg
Requires: swayidle
Requires: swaylock
Requires: waybar

%description
%{summary}.

%if %{with sddm}
%package -n     sddm-wayland-sway
Summary:        Sway Wayland SDDM greeter configuration
Provides:       sddm-greeter-displayserver
Conflicts:      sddm-greeter-displayserver

Requires:       lxqt-themes-fedora
Requires:       sddm >= 0.19.0^git20221123.3e48649
Requires:       sway

%description -n sddm-wayland-sway
This package contains configuration and dependencies for SDDM
to use Sway for the greeter display server.
%endif


%prep
%autosetup -p1


%build
%make_build


%install
%make_install PREFIX='%{_prefix}' WITH_SDDM='%[%{with sddm}?"yes":"no"]'


%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/sway/config
%config(noreplace) %{_sysconfdir}/sway/environment
%dir %{_sysconfdir}/swaylock
%config(noreplace) %{_sysconfdir}/swaylock/config
%{_bindir}/start-sway
%{_datadir}/sway/config.d
%{_datadir}/sway/config.live.d
%{_datadir}/wayland-sessions/sway.desktop
%{_libexecdir}/sway

%if %{with sddm}
%files -n sddm-wayland-sway
%license LICENSE
%config(noreplace) %{_sysconfdir}/sway/sddm-greeter.config
%{_prefix}/lib/sddm/sddm.conf.d/wayland-sway.conf
%{_libexecdir}/sddm-compositor-sway
%endif

%changelog
%autochangelog
