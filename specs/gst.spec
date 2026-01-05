%global uuid    com.leinardi.%{name}

Name:           gst
Version:        0.7.7
Release:        %autorelease
Summary:        System utility designed to stress and monitoring various hardware components

License:        GPL-3.0-or-later
URL:            https://gitlab.com/leinardi/gst
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel

BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.56.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30

Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       lm_sensors
Requires:       python3-gobject >= 3.50.0
Requires:       python3-humanfriendly >= 10.0
Requires:       python3-injector >= 0.22.0
Requires:       python3-matplotlib-gtk3 >= 3.1.1
Requires:       python3-peewee >= 3.17.8
Requires:       python3-psutil >= 6.1.0
Requires:       python3-pyxdg >= 0.28
Requires:       python3-pyyaml >= 6.0.2
Requires:       python3-requests >= 2.32.3
Requires:       python3-reactivex >= 4.0.4

Recommends:     dmidecode
Recommends:     stress-ng

%description
GST is a GTK system utility designed to stress and monitor various hardware
components like CPU and RAM.

Features

- Run different CPU and memory stress tests
- Run multi and single core benchmark
- Show Processor information (name, cores, threads, family, model, stepping,
  flags,bugs, etc)
- Show Processor's cache information
- Show Motherboard information (vendor, model, bios version, bios date, etc)
- Show RAM information (size, speed, rank, manufacturer, part number, etc)
- Show CPU usage (core %, user %, load avg, etc)
- Show Memory usage
- Show CPU's physical's core clock (current, min, max)
- Show Hardware monitor (info provided by sys/class/hwmon)


%prep
%autosetup
sed -e '/meson_post_install/d' -i meson.build


%build
%meson
%meson_build


%install
%meson_install
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2x/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING.txt
%doc CHANGELOG.md README.md RELEASING.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
%autochangelog
