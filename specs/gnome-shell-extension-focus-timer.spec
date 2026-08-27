%global extension   focus-timer
%global uuid        %{extension}@focustimerhq.github.io
%global forgeurl    https://github.com/focustimerhq/gnome-shell-extension-focus-timer

%global tag 3


Name:           gnome-shell-extension-%{extension}
Version:        %tag
Release:        %autorelease
Summary:        GNOME Shell integration for the Focus Timer app
License:        GPL-3.0-or-later
URL:            %forgeurl
BuildArch:      noarch

%forgemeta

Source0:        %forgesource

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  pkgconfig(gio-2.0)

Requires:       gnome-shell >= 45
Requires:       focus-timer
Requires:       glib2
Recommends:     gnome-extensions-app


%description
Focus Timer is an app based on the Pomodoro Technique that helps you break work
into intervals (typically 25 minutes), separated by short breaks. This builds
focus and prevents burnout.

Desktop Integration Features:

- Top bar indicator to quickly start, pause, and control your timer
- Notifications showing a live countdown of your session
- Screen overlay active during breaks, designed to be easy to dismiss
- Automatic Do-Not-Disturb mode to reduce interruptions while you focus
- Lock screen widget to check your timer without having to unlock



%prep
%forgesetup


%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md NEWS
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
