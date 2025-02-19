%bcond  initialsetup %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%bcond  sddm 1
%global sway_ver 1.8
%global bg_format %[ 0%{?fedora} >= 42 ? "jxl" : "png" ]

Name:           sway-config-fedora
Version:        0.4.3
Release:        %autorelease
Summary:        Fedora Sway Spin configuration for Sway

SourceLicense:  MIT AND CC-BY-SA-3.0
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
Recommends:     sway-systemd >= 0.3.0
# Minimal installation doesn't include Qt Wayland backend
Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

### Collected from /etc/sway/config and 50-fedora.conf
Recommends: foot
Recommends: libnotify
Recommends: rofi-wayland
Recommends: xdg-user-dirs
Requires: /usr/bin/pgrep
Requires: /usr/bin/pkill
Requires: brightnessctl >= 0.5.1-11
Requires: desktop-backgrounds-compat
Requires: grimshot
%if "%{bg_format}" == "jxl"
Requires: jxl-pixbuf-loader
%endif
Requires: lxqt-policykit
Requires: playerctl
Requires: pulseaudio-utils
Requires: swaybg
Requires: swayidle
Requires: swaylock
Requires: waybar

%description
%{summary}.

%if %{with initialsetup}
%package -n     initial-setup-gui-wayland-sway
Summary:        Sway Wayland Initial Setup GUI configuration
Provides:       firstboot(gui-backend)
Conflicts:      firstboot(gui-backend)

Requires:       xorg-x11-server-Xwayland
Requires:       initial-setup-gui >= 0.3.99
Requires:       sway >= %{sway_ver}
Supplements:    (initial-setup-gui and sway)

%description -n initial-setup-gui-wayland-sway
This package contains configuration and dependencies for
Anaconda Initial Setup to use Sway for the display server.
%endif

%if %{with sddm}
%package -n     sddm-wayland-sway
Summary:        Sway Wayland SDDM greeter configuration
License:        MIT AND CC-BY-SA-3.0

Provides:       sddm-greeter-displayserver
Conflicts:      sddm-greeter-displayserver

Requires:       desktop-backgrounds-compat
%if "%{bg_format}" == "jxl"
Requires:       kf6-kimageformats
%endif
Requires:       sddm >= 0.20.0
Requires:       sway >= %{sway_ver}

%description -n sddm-wayland-sway
This package contains configuration and dependencies for SDDM
to use Sway for the greeter display server.
%endif


%prep
%autosetup -p1


%build
%make_build \
    PREFIX='%{_prefix}' \
    BACKGROUND='%{_datadir}/backgrounds/default.%{bg_format}'


%install
%make_install \
    PREFIX='%{_prefix}' \
    WITH_INITIALSETUP='%[%{with initialsetup}?"yes":"no"]' \
    WITH_SDDM='%[%{with sddm}?"yes":"no"]'


%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/sway/config
%config(noreplace) %{_sysconfdir}/sway/environment
%dir %{_sysconfdir}/swaylock
%config(noreplace) %{_sysconfdir}/swaylock/config
%{_bindir}/start-sway
%{_datadir}/sway/config.d
%{_datadir}/sway/config.live.d
%{_datadir}/sway/live
%{_datadir}/wayland-sessions/sway.desktop
%{_libexecdir}/sway

%if %{with initialsetup}
%files -n initial-setup-gui-wayland-sway
%license LICENSE
%{_libexecdir}/initial-setup/run-gui-backend
%endif

%if %{with sddm}
%files -n sddm-wayland-sway
%license LICENSE
%license %{_datadir}/sddm/themes/03-sway-fedora/LICENSE
%config(noreplace) %{_sysconfdir}/sway/sddm-greeter.config
%{_datadir}/sddm/themes/03-sway-fedora/
%{_libexecdir}/sddm-compositor-sway
%{_prefix}/lib/sddm/sddm.conf.d/wayland-sway.conf
%endif

%changelog
%autochangelog
