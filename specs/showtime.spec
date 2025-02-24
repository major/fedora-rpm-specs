%global glib2_version 2.79.0
%global gtk4_version 4.15.0
%global libadwaita_version 1.6~beta

%global interim_pkg_ver beta.1

Name:           showtime
Version:        48.0~20250201.%{interim_pkg_ver}

Release:        1%{?dist}
Summary:        Modern video player built using GTK4

License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/Showtime/

# Altered this macro a bit. We added a '.0' to the version. That needed to be removed from the download url.
%global tarball_version %(echo %{version} | tr '~' '.' | sed 's/\.0//')
%global major_version %(cut -d "." -f 1 <<<%{tarball_version})

# Modify this once the package is released
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-48.%{interim_pkg_ver}.tar.xz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  blueprint-compiler
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       gtk4 >= %{gtk4_version}
Requires:       libadwaita >= %{libadwaita_version}
Requires:       python3
Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugin-gtk4

%description
Play your favorite movies and video files without hassle. Showtime
features simple playback controls that fade out of your way when
you're watching, fullscreen, adjustable playback speed, multiple
language and subtitle tracks, and screenshots — everything you
need for a straightforward viewing experience.

%prep
%autosetup -p1 -n %{name}-48.%{interim_pkg_ver}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Showtime.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files  -f %{name}.lang
%doc README.md
%license COPYING
%{python3_sitelib}/showtime/
%{_bindir}/showtime
%{_datadir}/applications/org.gnome.Showtime.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Showtime.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Showtime.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Showtime-symbolic.svg
%{_metainfodir}/org.gnome.Showtime.metainfo.xml
%{_datadir}/showtime/

%changelog
* Sat Feb 22 2025 Steve Cossette <farchord@gmail.com> - 48.0~20250201.beta.1-1
- Update to 48.0-beta1

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 48.0~20241104.080500.5579430-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Neal Gompa <ngompa@fedoraproject.org> - 48.0~20241104.080500.5579430-2
- Make the package noarch

* Thu Nov 7 2024 Steve Cossette <farchord@gmail.com> - 48.0~20241104.080500.5579430-1
- Initial release
