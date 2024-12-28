%global rdnn        dev.geopjr.Tuba

Name:           tuba
Version:        0.9.1
Release:        %autorelease
Summary:        Browse the Fediverse
License:        GPL-3.0-only
URL:            https://tuba.geopjr.dev/
Source:         https://github.com/GeopJr/Tuba/archive/v%{version}/Tuba-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

# optional for features
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(gstreamer-1.0)

# for desktop-file-validate command
BuildRequires:  desktop-file-utils
# for appstream-util command
BuildRequires:  libappstream-glib

# for ownership of icon parent directories
Requires:       hicolor-icon-theme


%description
Explore the federated social web with Tuba for GNOME. Stay connected to your
favorite communities, family and friends with support for popular Fediverse
platforms like Mastodon, GoToSocial, Akkoma & more!


%prep
%autosetup -n Tuba-%{version} -p 1


%build
%meson
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
%{_datadir}/glib-2.0/schemas/%{rdnn}.gschema.xml
%{_datadir}/gtksourceview-5/language-specs/fedi*.lang
%{_datadir}/gtksourceview-5/styles/fedi*.xml
%{_datadir}/icons/hicolor/*/apps/%{rdnn}*.svg
%{_metainfodir}/%{rdnn}.metainfo.xml


%changelog
%autochangelog
