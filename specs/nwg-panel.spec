%global forgeurl https://github.com/nwg-piotr/%{name}
%global sys_name nwg_panel

Name:       nwg-panel
Version:    0.10.15
%forgemeta
Release:    %autorelease
Summary:    GTK3-based panel for sway and Hyprland Wayland compositors
BuildArch:  noarch

License:    MIT
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros

Requires:   gtk-layer-shell
Requires:   gtk3
Requires:   python3-gobject
Requires:   python3-i3ipc
Requires:   python3-dasbus
Requires:   wlr-randr

Recommends: /usr/bin/pactl
Recommends: brightnessctl
Recommends: playerctl
Recommends: python3-psutil

%description
This application is a part of the nwg-shell project.

Nwg-panel is a GTK3-based panel for sway and Hyprland Wayland compositors.
The panel is equipped with a graphical configuration program that frees the
user from the need to manually edit configuration files.

%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{sys_name}

install -Dpm 0644 %{name}.svg -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -Dpm 0644 nwg-shell.svg -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -Dpm 0755 %{name}-config.desktop -t %{buildroot}%{_datadir}/applications/
install -Dpm 0644 %{name}.service -t %{buildroot}%{_userunitdir}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_bindir}/nwg-dwl-interface
%{_bindir}/nwg-processes
%{_datadir}/applications/%{name}-config.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_userunitdir}/%{name}.service


%changelog
%autochangelog
