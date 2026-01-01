%global po_package %{name}-3.0

Name:           gnome-applets
Version:        3.58.0
Release:        %autorelease
Summary:        Small applications for the GNOME Flashback panel

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GnomeApplets
Source:         https://download.gnome.org/sources/%{name}/3.58/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake >= 1.16.4
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libSM-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  yelp-tools

BuildRequires:  pkgconfig(adwaita-icon-theme) >= 3.14.0
BuildRequires:  pkgconfig(dbus-1) >= 1.1.2
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.74
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(gucharmap-2.90) >= 2.33.0
BuildRequires:  pkgconfig(gweather4) >= 3.91
BuildRequires:  pkgconfig(libgnome-panel) >= 3.41.1
BuildRequires:  pkgconfig(libgtop-2.0) >= 2.11.92
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libwnck-3.0) >= 43.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(upower-glib) >= 0.9.4
BuildRequires:  pkgconfig(x11)
%ifnarch s390 s390x sparc64 i686
BuildRequires:  kernel-tools-devel
%endif

Requires:       gnome-panel >= 3.41.1
Requires:       hicolor-icon-theme

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Gnome Applets component is part of the GnomeFlashback project. It currently
provides the following applets:

- Accessibility applet (accessx-status)
- Battery status (battstat)
- A symbol table (charpick)
- A system monitor for cpu, memory and network usage information (cpufreq)
- A drive mount applet (drivemount)
- Geyes, a funny applet that shows a pair of eyes which follow the cursor
  (geyes)
- A weather applet (gweather)
- A command execution and macro plugin (mini-commander)
- A sound applet (deprecated and replaced by libsound-applet in GnomeFlashback
  (mixer)
- A model lights plugin for modems (modemlights)
- A multi load plugin (multiload)
- A notes applets (stickynotes)
- A trash applet (trashapplet)
- A window picker applet that shows open applications as icons. This saves a lot
  of screen space and is very useful if many applications are open.
  (windowpicker)


%prep
%autosetup -p1
autoreconf -fiv


%build
%configure                      \
    --disable-scrollkeeper      \
    --disable-static            \
    --enable-gtk-doc            \
    --enable-mini-commander     \
    --enable-suid=no            \
    --with-cpufreq-lib=cpupower \
    --without-hal               \
    %{nil}
%make_build


%install
%make_install
%find_lang %{po_package} --all-name

# drop non-XKB support files
rm -rf %{buildroot}%{_datadir}/xmodmap


%files -f %{po_package}.lang
%license COPYING COPYING-DOCS
%doc README.md AUTHORS NEWS
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_libdir}/gnome-panel/modules/org.gnome.%{name}.so
%{_datadir}/glib-2.0/schemas/*.enums.xml
%ifnarch s390 s390x i686
%{_bindir}/cpufreq-selector
%{_datadir}/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%{_datadir}/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%{_datadir}/polkit-1/actions/org.gnome.cpufreqselector.policy
%endif

# Don't make it as separate noarch package since it builds differently on 's390x'
# arch and we got build error here
%{_datadir}/help/


%changelog
%autochangelog
