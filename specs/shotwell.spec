# Not enabled by default for now - see rhbz#2190013
%bcond_with facedetect

Name:           shotwell
Version:        33~alpha
Release:        %autorelease
Summary:        A photo organizer for the GNOME desktop

%global tarball_version %%(echo %{version} | tr '~' '.')

# LGPLv2+ for the code
# CC-BY-SA for some of the icons
License:        LGPL-2.1-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Shotwell
Source0:        https://download.gnome.org/sources/shotwell/%{tarball_version}/shotwell-%{tarball_version}.tar.xz

BuildRequires:  cmake
BuildRequires:  vala
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib >= 0.7.3
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-ui-3)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.22
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gexiv2) >= 0.11.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.40
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgphoto2) >= 2.5.0
BuildRequires:  pkgconfig(libportal-gtk3) >= 0.5
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.1) >= 2.26
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libportal-gtk4)
%if %{with facedetect}
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  gcc-c++
%endif

# to fix symlinks
BuildRequires:  symlinks fakechroot

# provides the icon directories
Requires:       hicolor-icon-theme

%description
Shotwell is an easy-to-use, fast photo organizer designed for the GNOME
desktop.  It allows you to import photos from your camera or disk, organize
them by date and subject matter, even ratings.  It also offers basic photo
editing, like crop, red-eye correction, color adjustments, and straighten.
Shotwell's non-destructive photo editor does not alter your master photos,
making it easy to experiment and correct errors.


%prep
%autosetup -n shotwell-%{tarball_version} -p1


%build
%meson \
  -Dinstall_apport_hook=false \
%if %{with facedetect}
  -Dface_detection=true \
  -Dface_detection_helper=true \
  -Dface_detection_helper_bus=session \
%endif
  %{nil}

%meson_build


%install
%meson_install

pushd %{buildroot}
fakechroot -- symlinks -C -cvr %{_datadir}/help
popd

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shotwell.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shotwell-Viewer.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Shotwell.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc README.md NEWS THANKS AUTHORS
%{_bindir}/shotwell
%{_libdir}/shotwell/
%{_libdir}/libshotwell-authenticator.so.*
%exclude %{_libdir}/libshotwell-authenticator.so
%{_libdir}/libshotwell-plugin-common.so.*
%exclude %{_libdir}/libshotwell-plugin-common.so
%{_libdir}/libshotwell-plugin-dev-1.0.so.*
%exclude %{_libdir}/libshotwell-plugin-dev-1.0.so
%{_libexecdir}/shotwell/
%{_datadir}/applications/org.gnome.Shotwell.desktop
%{_datadir}/applications/org.gnome.Shotwell.Auth.desktop
%{_datadir}/applications/org.gnome.Shotwell-Viewer.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Shotwell.png
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Shotwell.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Shotwell-symbolic.svg
%{_metainfodir}/org.gnome.Shotwell.appdata.xml
%{_mandir}/man1/shotwell.1*
%if %{with facedetect}
%{_datadir}/dbus-1/services/org.gnome.Shotwell.Faces1.service
%{_datadir}/shotwell/facedetect
%endif


%changelog
%autochangelog
