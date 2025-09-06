%global glib2_version 2.79.0
%global gtk4_version 4.15.0
%global libadwaita_version 1.6~beta
%global blueprint_compiler_version 0.18

Name:           showtime
Version:        49~rc

Release:        %autorelease
Summary:        Modern video player built using GTK4

License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/Showtime/

# Altered this macro a bit. We added a '.0' to the version. That needed to be removed from the download url.
%global tarball_version %(echo %{version} | tr '~' '.' | sed 's/\.0//')
%global major_version %(cut -d "." -f 1 <<<%{tarball_version})

Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  blueprint-compiler >= %{blueprint_compiler_version}
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
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugin-gtk4
Requires:       (gstreamer1-plugin-openh264 if openh264)

Recommends:     gstreamer1-plugins-good
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-ugly-free

%description
Play your favorite movies and video files without hassle. Showtime
features simple playback controls that fade out of your way when
you're watching, fullscreen, adjustable playback speed, multiple
language and subtitle tracks, and screenshots — everything you
need for a straightforward viewing experience.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

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
%{_datadir}/dbus-1/services/org.gnome.Showtime.service
%{_datadir}/glib-2.0/schemas/org.gnome.Showtime.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Showtime.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Showtime-symbolic.svg
%{_metainfodir}/org.gnome.Showtime.metainfo.xml
%{_datadir}/showtime/

%changelog
%autochangelog
