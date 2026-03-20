%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-robots
Version:        41.2
Release:        %autorelease
Summary:        GNOME Robots game

# * gnome-robots source code and data is GPL-3.0-or-later and GFDL-1.1-or-later
# * rust crate dependencies are:
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause OR Apache-2.0
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    GPL-3.0-or-later AND GFDL-1.1-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    LGPL-2.1-or-later AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown
URL:            https://wiki.gnome.org/Apps/Robots
Source0:        https://download.gnome.org/sources/%{name}/41/%{name}-%{tarball_version}.tar.xz
# Update dependencies to GNOME SDK 49
Patch0:         https://gitlab.gnome.org/GNOME/gnome-robots/-/merge_requests/39.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(gtk4)

Requires:       hicolor-icon-theme

%description
The classic game where you have to avoid a hoard of robots who are trying to
kill you. Each step you take brings them closer toward you. Fortunately they
aren't very smart and you also have a helpful teleportation gadget.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires


%build
%meson
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Robots.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Robots.metainfo.xml


%files -f %{name}.lang
%license COPYING
%license LICENSE.dependencies
%{_bindir}/gnome-robots
%{_datadir}/applications/org.gnome.Robots.desktop
%{_datadir}/dbus-1/services/org.gnome.Robots.service
%{_datadir}/glib-2.0/schemas/org.gnome.Robots.gschema.xml
%{_datadir}/gnome-robots
%{_datadir}/icons/hicolor/*/actions/teleport*.png
%{_datadir}/icons/hicolor/*/apps/org.gnome.Robots.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Robots-symbolic.svg
%{_datadir}/metainfo/org.gnome.Robots.metainfo.xml
%{_mandir}/man6/gnome-robots.6*


%changelog
%autochangelog
