%global forgeurl https://github.com/xapp-project/velocitty
%global tag      %{version}
%forgemeta

Name:           velocitty
Version:        1.0.2
Release:        %autorelease
Summary:        Terminal emulator for Linux desktops

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildSystem:    meson
BuildRequires:  gettext
BuildRequires:  gtk4
BuildRequires:  python3-rpm-macros
BuildRequires:  desktop-file-utils

Requires:       gtk4
Requires:       hicolor-icon-theme
Requires:       libadwaita
Requires:       python3-gobject
Requires:       python3-setproctitle
Requires:       python3-xapp
Requires:       vte291-gtk4
Requires:       xapp-symbolic-icons


%description
Velocitty is a simple, intuitive terminal emulator for Linux desktops, written
in Python with GTK4, libadwaita and VTE. It is desktop-agnostic and aims to
need just enough configuration to feel at home, while making it easy to
identify, organise and restore tabs.

%prep
%forgesetup

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.x.velocitty.desktop

%files
%license LICENSES/*
%doc README.md
%{_bindir}/velocitty
%{python3_sitelib}/velocitty/
%{_datadir}/velocitty/
%{_datadir}/applications/org.x.velocitty.desktop
%{_datadir}/icons/hicolor/scalable/apps/velocitty.svg
%{_datadir}/glib-2.0/schemas/org.x.velocitty.gschema.xml

%changelog
%autochangelog