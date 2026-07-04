%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$

Name:           sushi
Version:        51~alpha
Release:        %autorelease
Summary:        A quick previewer for Nautilus

# data/org.gnome.NautilusPreviewer.appdata.xml.in.in is CC0-1.0
# the files in src/libsushi/ are combination of:
#      LGPL-2.0-or-later
#      LGPL-2.1-or-later WITH GStreamer-exception-2005
License:        GPL-2.0-or-later WITH GStreamer-exception-2008 AND CC0-1.0 AND (LGPL-2.0-or-later AND LGPL-2.1-or-later WITH GStreamer-exception-2005)
URL:            https://gitlab.gnome.org/GNOME/sushi
Source0:        https://download.gnome.org/sources/%{name}/%{gnome_major_version}/%{name}-%{gnome_tarball_version}.tar.xz

%gnome_check_version

# papers does not build for ix86, thus disable for it too
ExcludeArch:    %{ix86}

BuildRequires:  blueprint-compiler
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gjs-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(glycin-gtk4-2)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(papers-document-4.0)
BuildRequires:  pkgconfig(webkitgtk-6.0)

Obsoletes:      sushi-devel < 0.5.1

Requires: gtksourceview5
Recommends: webkitgtk6.0

#Description from upstream's README.
%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop
file manager.


%prep
%autosetup -p1 -n %{name}-%{gnome_tarball_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS NEWS README.md TODO
%license COPYING
%{_bindir}/sushi
%{_libexecdir}/org.gnome.NautilusPreviewer
%{_libdir}/sushi/
%{_datadir}/dbus-1/services/org.gnome.NautilusPreviewer.service
%{_metainfodir}/org.gnome.NautilusPreviewer.metainfo.xml
%{_datadir}/sushi/


%changelog
%autochangelog
