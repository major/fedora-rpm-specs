%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           gnome-robots
Version:        50.0
Release:        %autorelease
Summary:        GNOME Robots game

# * gnome-robots source code and data is GPL-3.0-or-later and GFDL-1.1-or-later
# * rust crate dependencies are:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    GPL-3.0-or-later AND GFDL-1.1-or-later AND
    ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception) AND
    MIT AND
    (MIT OR Apache-2.0) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown
URL:            https://wiki.gnome.org/Apps/Robots
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

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
