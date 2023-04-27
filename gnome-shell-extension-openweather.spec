%global shortname openweather
%global uuid %{shortname}-extension@jenslody.de

Name:           gnome-shell-extension-%{shortname}
Version:        121
Release:        %autorelease
Summary:        Display weather information for any location on Earth
BuildArch:      noarch

License:        GPLv3+
URL:            https://gitlab.com/skrewball/openweather
Source0:        %{url}/-/archive/v%{version}/%{shortname}-v%{version}.tar.gz

BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  make
# The version of gnome-common in CentOS7 is only 3.7.4
BuildRequires:  gnome-common >= 3.7.4

Requires:       gnome-shell >= 43

%description
OpenWeather (%uuid) is a simple extension for
displaying weather conditions and forecasts for any location on Earth in the
GNOME Shell. It provides support for multiple locations with editable names
using coordinates to store the locations, a beautiful layout, and more.
Weather data is fetched from OpenWeatherMap including 3 hour forecasts for up
to 5 days.

After completing installation, restart GNOME Shell (Alt+F2, r, Enter) and
enable the extension through the gnome-extensions app or via terminal:

  $ gnome-shell-extension-tool -e %uuid


%prep
%autosetup -n %{shortname}-v%{version} -p1


%build
%make_build


%install
%make_install
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
%autochangelog
