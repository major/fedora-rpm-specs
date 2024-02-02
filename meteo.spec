%global uuid    com.gitlab.bitseater.%{name}

Name:           meteo
Version:        0.9.9.3
Release:        %autorelease
Summary:        Forecast application using OpenWeatherMap API

License:        GPL-3.0-or-later
URL:            https://gitlab.com/bitseater/meteo
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme

%description
Know the forecast of the next hours & days.

Developed with Vala & Gtk, using OpenWeatherMap API.

Features:

- Current weather, with information about temperature, pressure, wind speed and
  direction, sunrise & sunset.
- Forecast for next 18 hours.
- Forecast for next five days.
- Choose your units (metric, imperial or british).
- Choose your city, with maps help.
- Awesome maps with weather info.
- System tray indicator.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%files -f %{uuid}.lang
%license COPYING
%doc README.md AUTHORS CREDITS.md CHANGELOG
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*
%{_metainfodir}/*.appdata.xml


%changelog
%autochangelog
