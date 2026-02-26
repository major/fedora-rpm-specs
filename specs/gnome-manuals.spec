%global appname org.gnome.Manuals
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-manuals
Version:        50~rc
Release:        %autorelease
Summary:        Install, Browse, and Search developer documentation
License:        GPL-3.0-or-later

URL:            https://gitlab.gnome.org/GNOME/manuals
Source:         https://download.gnome.org/sources/manuals/50/manuals-%{tarball_version}.tar.xz

ExcludeArch:    %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  pkgconfig(libfoundry-1)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(webkitgtk-6.0)

Requires:       dbus-common
Requires:       hicolor-icon-theme

%description
Manuals is an extraction of the Documentation component of GNOME Builder
into a standalone application.

%prep
%autosetup -n manuals-%{tarball_version} -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang manuals

%check
desktop-file-validate \
    $RPM_BUILD_ROOT/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT/%{_datadir}/metainfo/%{appname}.metainfo.xml

%files -f manuals.lang
%{_bindir}/manuals
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}{,-symbolic}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
%autochangelog
