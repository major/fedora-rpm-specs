%global srcname Wildcard
%global app_id net.ffkkinos.Wildcard

%global commit 446f85fc82677a2c416aa63651608e0d1041d1ec
%global shortcommit %{sub %{commit} 1 8}

Name:           wildcard
Version:        0.3.5^1.%{shortcommit}
Release:        %autorelease
Summary:        Test your regular expressions

# Wildcard itself is GPL-3.0-or-later, the rest comes from the rust
# dependencies that end up statically linked into it:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
# See LICENSE.depndencies for the full breakdown
License:        %{shrink:
    GPL-3.0-or-later
    AND MIT
    AND Unicode-DFS-2016
    AND (Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
}
URL:            https://gitlab.gnome.org/World/Wildcard
Source:         %{url}/-/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  blueprint-compiler
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       dbus-common
Requires:       hicolor-icon-theme

%description
Wildcard gives you a nice and simple to use interface to test/practice regular
expressions.

%prep
%autosetup -C -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%meson
%meson_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}*.svg
%{_metainfodir}/%{app_id}.metainfo.xml

%changelog
%autochangelog
