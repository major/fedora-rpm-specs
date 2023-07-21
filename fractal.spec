%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           fractal
Version:        5~beta1
Release:        2%{?dist}
Summary:        Matrix group messaging app

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/fractal
Source0:        https://gitlab.gnome.org/GNOME/fractal/-/package_files/366/download#/fractal-%{tarball_version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cargo
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


%install
%meson_install

%find_lang fractal


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop


%files -f fractal.lang
%license LICENSE
%doc README.md
%{_bindir}/fractal
%{_datadir}/applications/org.gnome.Fractal.desktop
%{_datadir}/fractal/
%{_datadir}/glib-2.0/schemas/org.gnome.Fractal.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Fractal.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Fractal-symbolic.svg
%{_datadir}/metainfo/org.gnome.Fractal.metainfo.xml


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5~beta1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Pete Walter <pwalter@fedoraproject.org> - 5~beta1-1
- First Fedora build
