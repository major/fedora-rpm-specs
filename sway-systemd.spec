Name:           sway-systemd
Version:        0.4.0
Release:        %autorelease
Summary:        Systemd integration for Sway session

License:        MIT
URL:            https://github.com/alebastr/sway-systemd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

Requires:       python3dist(dbus-next)
Requires:       python3dist(i3ipc)
Requires:       python3dist(psutil)
Requires:       python3dist(python-xlib)
Requires:       python3dist(tenacity)
Requires:       sway
Requires:       systemd
Recommends:     /usr/bin/dbus-update-activation-environment

%description
%{summary}.

The goal of this project is to provide a minimal set of configuration files
and scripts required for running Sway in a systemd environment.

This includes several areas of integration:
 - Propagate required variables to the systemd user session environment.
 - Define sway-session.target for starting user services.
 - Place GUI applications into a systemd scopes for systemd-oomd compatibility.

%prep
%autosetup


%build
%meson \
    -Dautoload-configs='cgroups'
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/sway/config.d/10-systemd-session.conf
%config(noreplace) %{_sysconfdir}/sway/config.d/10-systemd-cgroups.conf
%{_datadir}/%{name}/*.conf
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/assign-cgroups.py
%{_libexecdir}/%{name}/locale1-xkb-config
%{_libexecdir}/%{name}/session.sh
%{_libexecdir}/%{name}/wait-sni-ready
%{_userunitdir}/sway-session.target
%{_userunitdir}/sway-session-shutdown.target
%{_userunitdir}/sway-xdg-autostart.target


%changelog
%autochangelog
