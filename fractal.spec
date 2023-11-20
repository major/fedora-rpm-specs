%global tarball_version %%(echo %{version} | tr '~' '.')

# errors out on vendor/ulid/src/lib.rs
%global __brp_mangle_shebangs_exclude_from /usr/src/debug/.*\.rs

Name:           fractal
Version:        5~rc1
Release:        1%{?dist}
Summary:        Matrix group messaging app

# fractal itself is GPL-3.0-or-later. The rest are statically linked rust libraries based on cargo_license_summary output.
License:        GPL-3.0-or-later AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND GPL-3.0-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND MPL-2.0+ AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://gitlab.gnome.org/GNOME/fractal
Source0:        https://gitlab.gnome.org/GNOME/fractal/-/package_files/473/download#/fractal-%{tarball_version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-play-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(shumate-1.0)
BuildRequires:  pkgconfig(xdg-desktop-portal)
# for check
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%description
Fractal is a Matrix messaging app for GNOME written in Rust. Its interface is
optimized for collaboration in large groups, such as free software projects.


%prep
%autosetup -n fractal-%{tarball_version} -p1

sed -i -e '/\(gtk_update_icon_cache\|glib_compile_schemas\|update_desktop_database\)/s/true/false/' meson.build


%build
%meson
%meson_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%install
%meson_install

%find_lang fractal


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop


%files -f fractal.lang
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/fractal
%{_datadir}/applications/org.gnome.Fractal.desktop
%{_datadir}/fractal/
%{_datadir}/glib-2.0/schemas/org.gnome.Fractal.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Fractal.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Fractal-symbolic.svg
%{_datadir}/metainfo/org.gnome.Fractal.metainfo.xml


%changelog
* Fri Nov 17 2023 Pete Walter <pwalter@fedoraproject.org> - 5~rc1-1
- Update to 5.rc1

* Thu Aug 17 2023 Pete Walter <pwalter@fedoraproject.org> - 5~beta2-1
- Update to 5.beta2

* Tue Aug 15 2023 Pete Walter <pwalter@fedoraproject.org> - 5~beta1-3
- Include statically linked rust library licenses in the license tag (rhbz#2223224)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5~beta1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Pete Walter <pwalter@fedoraproject.org> - 5~beta1-1
- First Fedora build
