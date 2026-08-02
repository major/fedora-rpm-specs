Summary: Chat with your friends on Signal
Name: flare-im
Version: 0.22.1
Release: %autorelease
URL: https://gitlab.com/schmiddi-on-mobile/flare
Source0: https://gitlab.com/schmiddi-on-mobile/flare/-/archive/%{version}/flare-%{version}.tar.bz2
# generated using vendor.sh
Source1: flare-%{version}-vendor.tar.bz2
Source2: vendor.toml
Source3: vendor.sh
# flare itself is AGPL-3.0-or-later. The rest are statically linked rust libraries based on cargo_license_summary output.
License: AGPL-3.0-or-later AND (MIT OR Apache-2.0) AND NCSA AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND AGPL-3.0-only AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (CC0-1.0 OR Apache-2.0) AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib
BuildRequires: blueprint-compiler
BuildRequires: cargo
BuildRequires: cargo-rpm-macros
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: meson
# required by libsqlite3-sys crate
BuildRequires: openssl-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libspelling-1)
BuildRequires: pkgconfig(gtksourceview-5)
# required by spqr crate
BuildRequires: protobuf-compiler
BuildRequires: rust
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}
# flare-the-game-engine uses the same binary path
Conflicts: flare

%description
Flare is an open-source, Rust-based Signal chat client designed for Linux
desktop and mobile environments using GTK4 and Libadwaita for an adaptive
interface. Developed by Schmiddi on Mobile, the project provides a native
experience with secure local storage via libsecret.

%prep
%autosetup -p1 -a 1 -n flare-%{version}
%cargo_prep -N
# include full configuration for vendored dependencies
cp -p %{S:2} .cargo/config.toml
sed -i -e '/\(gtk_update_icon_cache\|glib_compile_schemas\|update_desktop_database\)/s/true/false/' meson.build
# rename to valid glibc locale names
# https://sourceware.org/bugzilla/show_bug.cgi?id=30761
sed -i -e 's/zh_Hans/zh_CN/' -e 's/zh_Hant/zh_TW/' po/LINGUAS
mv po/zh_{Hans,CN}.po
mv po/zh_{Hant,TW}.po

%conf
%meson -Dprofile=default

%build
%meson_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest

%install
%meson_install
%find_lang flare

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/de.schmidhuberj.Flare.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/de.schmidhuberj.Flare.desktop

%files -f flare.lang
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc CHANGELOG.md NOTICE README.md
%{_bindir}/flare
%{_datadir}/applications/de.schmidhuberj.Flare.desktop
%{_datadir}/dbus-1/services/de.schmidhuberj.Flare.service
%{_datadir}/flare/
%{_datadir}/glib-2.0/schemas/de.schmidhuberj.Flare.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/de.schmidhuberj.Flare.svg
%{_datadir}/icons/hicolor/symbolic/apps/de.schmidhuberj.Flare-symbolic.svg
%{_metainfodir}/de.schmidhuberj.Flare.metainfo.xml

%changelog
%autochangelog
