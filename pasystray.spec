Name:           pasystray
Version:        0.8.1
Release:        %autorelease
Summary:        PulseAudio system tray
License:        LGPL-2.1-or-later
URL:            https://github.com/christophgysin/pasystray

Source0:        https://github.com/christophgysin/pasystray/archive/%{version}/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1471192
# https://bugzilla.redhat.com/show_bug.cgi?id=2035305
Patch1:         pasystray-0.8.0-wayland.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  desktop-file-utils

%if 0%{?fedora}
Suggests:       paman
Suggests:       pavucontrol
Suggests:       pavumeter
#Suggests:       paprefs
#Suggests:       pulseaudio-qpaeq
%endif

%description
A replacement for the deprecated padevchooser.
pasystray allows setting the default PulseAudio source/sink and moving streams
on the fly between sources/sinks without restarting the client applications.

%prep
%autosetup -p1

%build
autoreconf -i
%configure
%make_build

%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
%autochangelog
