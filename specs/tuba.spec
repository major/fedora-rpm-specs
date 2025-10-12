%global rdnn        dev.geopjr.Tuba

Name:           tuba
Version:        0.10.3
Release:        %autorelease
Summary:        Browse the Fediverse
License:        GPL-3.0-only
URL:            https://tuba.geopjr.dev/
Source:         https://github.com/GeopJr/Tuba/archive/v%{version}/Tuba-%{version}.tar.gz
# Fedora packaging guidelines require validating AppData files with
# appstream-util.  Upstream previously did this in their meson tests, but have
# switched to using appstreamcli instead.  This would probably be fine, except
# validation fails using this tool.  This patch reverts the upstream switch.
# https://github.com/GeopJr/Tuba/commit/e5a1528c27ef7b4411c1b322e61beea6dd430bf0
Patch:          0001-Revert-feat-meson-use-appstream-for-appdata-validation-1379.patch

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(clapper-0.0)
BuildRequires:  pkgconfig(clapper-gtk-0.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(gexiv2)

# for desktop-file-validate command
BuildRequires:  desktop-file-utils
# for appstream-util command
BuildRequires:  libappstream-glib

# for ownership of icon parent directories
Requires:       hicolor-icon-theme

# The flatpak previously bundled this but now relies on it being part of the
# platform/sdk.
# https://github.com/GeopJr/Tuba/pull/678
Recommends:     webp-pixbuf-loader


%description
Explore the federated social web with Tuba for GNOME. Stay connected to your
favorite communities, family and friends with support for popular Fediverse
platforms like Mastodon, GoToSocial, Akkoma & more!


%prep
%autosetup -n Tuba-%{version} -p 1


%build
# Build with the same options as the flatpak to ensure feature parity.
# https://github.com/flathub/dev.geopjr.Tuba/blob/master/dev.geopjr.Tuba.yaml
%meson \
    -Dclapper=enabled \
    -Dspelling=enabled \
    -Dgstreamer=enabled \
    -Din-app-browser=enabled \
    -Dgexiv2=enabled
%meson_build


%install
%meson_install
%find_lang %{rdnn}


%check
# The .desktop and .metainfo.xml files are validated during the test suite, so
# we don't need to run those validate commands separately.
%meson_test


%files -f %{rdnn}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{rdnn}
%{_mandir}/man1/%{rdnn}.1*
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/dbus-1/services/%{rdnn}.service
%{_datadir}/glib-2.0/schemas/%{rdnn}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{rdnn}*.svg
%{_metainfodir}/%{rdnn}.metainfo.xml


%changelog
%autochangelog
