%global rdnn        dev.geopjr.Tuba

Name:           tuba
Version:        0.3.2
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
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libwebp)

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
%autosetup -n Tuba-%{version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{rdnn}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.appdata.xml


%files -f %{rdnn}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{rdnn}
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/glib-2.0/schemas/%{rdnn}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{rdnn}*.svg
%{_metainfodir}/%{rdnn}.appdata.xml


%changelog
%autochangelog
