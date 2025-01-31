%global commit 0a58a1fa639836be5d7fc8f8178f9988856e28a0
%global srcname Wildcard
%global app_id com.felipekinoshita.Wildcard

Name:           wildcard
Version:        0.3.3
Release:        %autorelease
Summary:        Test your regular expressions

# Wildcard itself is GPL-3.0-or-later, the rest comes from the rust
# dependencies that end up statically linked into it
# See LICENSE.depndencies for the full breakdown
License:        GPL-3.0-or-later AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
URL:            https://gitlab.gnome.org/World/Wildcard
Source:         %{url}/-/archive/v%{version}/%{srcname}-%{version}.tar.gz

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

Requires:       hicolor-icon-theme

%description
Wildcard gives you a nice and simple to use interface to test/practice regular
expressions.

%prep
%autosetup -p1 -n %{srcname}-v%{version}-%{commit}
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
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}*.svg
%{_metainfodir}/%{app_id}.metainfo.xml

%changelog
%autochangelog
