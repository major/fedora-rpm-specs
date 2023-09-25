%global uuid org.gabmus.%{name}

Name:           hydrapaper
Version:        3.3.2
Release:        %autorelease
Epoch:          1
Summary:        Set two different backgrounds for each monitor on GNOME

License:        GPL-3.0-or-later
URL:            https://gitlab.com/gabmus/HydraPaper
Source0:        %{url}/-/archive/%{version}/HydraPaper-%{version}.tar.gz
BuildArch:      noarch

# blueprint-compiler does not work on s390x:
# https://gitlab.gnome.org/jwestman/blueprint-compiler/-/issues/96
ExcludeArch:    s390x

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.58.0
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.3.1
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0.0

Requires:       dbus-common
Requires:       glib2
Requires:       gtk4 >= 4.3.1
Requires:       hicolor-icon-theme
Requires:       libadwaita >= 1.0.0
Requires:       python3-dbus
Requires:       python3-pillow

%description
GTK utility to set two different backgrounds for each monitor on GNOME (which
lacks this feature).

Wallpaper manager with multimonitor support.

HydraPaper officially supports the following desktop environments:

  - GNOME 3
  - MATE
  - Cinnamon
  - Budgie

Experimental support for the sway window manager/Wayland compositor is also
present.


%prep
%autosetup -n HydraPaper-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
%autochangelog
