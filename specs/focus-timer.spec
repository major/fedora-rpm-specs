%global uuid pomodoro@arun.codito.in
%global forgeurl https://github.com/focustimerhq/FocusTimer

Version:        1.1.3

%global tag %{version}
%forgemeta

Name:           focus-timer
Release:        %autorelease
Summary:        A time-management app built around the Pomodoro Technique

# GPL-3.0-or-later for the application code; the bundled sounds in
# /usr/share/focus-timer/sounds are licensed separately (see data/sounds/CREDITS):
#   bell.ogg, loud-bell.ogg, brown-noise.ogg : CC-BY-3.0
#   metronome.ogg                            : CC-BY-4.0
#   clock.ogg                                : CC0-1.0
License:        GPL-3.0-or-later AND CC-BY-3.0 AND CC-BY-4.0 AND CC0-1.0
URL:            https://gnomepomodoro.org/
Source0:        %forgesource

BuildRequires:  appstream
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-controller-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(gtk4-x11)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wayland-client)

Requires:       hicolor-icon-theme
# For /usr/share/dbus-1/services ownership
Requires:       dbus-common
# For /usr/share/knotifications6 ownership
Requires:       kf6-knotifications

# Renamed upstream from gnome-pomodoro.
# Drop these in F47
Provides:       gnome-pomodoro = 1:%{version}-%{release}
Obsoletes:      gnome-pomodoro < 1:0.28.0-5

%description
Focus Timer (formerly gnome-pomodoro) is a time-management app built around the
Pomodoro Technique, helping you maintain focus and prevent burnout through
structured work and break intervals.

Key features:

- Customizable work session and break lengths
- Screen overlay during breaks
- System tray icon
- Hotkeys (global shortcuts)
- Daily, weekly, and monthly statistics
- Extensible via custom shell commands, D-Bus, and CLI
- GNOME Shell extension for deeper desktop integration:
  https://github.com/focustimerhq/gnome-shell-extension-focus-timer

%prep
%forgesetup

%build
%meson
%meson_build

%install
%meson_install
PATH="$PATH:%{buildroot}/%{_bindir}" help2man -N -n 'Time-management app built around the Pomodoro Technique' \
    %{name} > %{name}.1

# fix man page encoding and command line
iconv -f iso8859-1 -t utf-8 %{name}.1 > %{name}.1.new && mv -v %{name}.1.new %{name}.1
sed -i 's/io.github.focustimerhq.FocusTimer.*/focus-timer [OPTION...]/' %{name}.1
cat %{name}.1

install -Dm0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1


%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.github.focustimerhq.FocusTimer.desktop
appstreamcli validate --no-net %{buildroot}/%{_metainfodir}/io.github.focustimerhq.FocusTimer.metainfo.xml

%files -f %{name}.lang
%doc README.md NEWS data/sounds/CREDITS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{bash_completions_dir}/%{name}
%{_datadir}/applications/io.github.focustimerhq.FocusTimer.desktop
%{_datadir}/dbus-1/interfaces/io.github.focustimerhq.FocusTimer*.xml
%{_datadir}/dbus-1/services/io.github.focustimerhq.FocusTimer.service
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/io.github.focustimerhq.FocusTimer*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/io.github.focustimerhq.FocusTimer*
%{_datadir}/knotifications6/io.github.focustimerhq.FocusTimer.notifyrc
%{_metainfodir}/io.github.focustimerhq.FocusTimer.metainfo.xml

%changelog
%autochangelog
