Name:           bijiben
Version:        40.1
Release:        %autorelease
Summary:        Simple Note Viewer

# Bijiben is GPLv3+ apart a few files "LGPLv2 or LGPLv3"
# And ligd is LGPLv2+
License:        GPL-3.0-or-later AND LGPL-3.0-only AND LGPL-2.0-or-later
Url:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/%{name}/40/%{name}-%{version}.tar.xz

Patch01:        meson-0.61-build.patch
Patch02:        webkitdep.patch

BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libecal-2.0) >= 3.45.1
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.45.1
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(webkit2gtk-4.1) >= 2.36
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  libappstream-glib-devel

Recommends:     gvfs-goa

# libgd is not meant to be installed as a system-wide shared library.
# It is just a way for GNOME applications to share widgets and other common
# code on an ad-hoc basis.
Provides: bundled(libgd)

%description
Simple note editor which emphasis on visuals : quickly write
notes, quickly find it back.


%prep
%autosetup -p1 -S gendiff


%build
%meson \
%if 0%{?flatpak}
  -Dprivate_store=true
%else
  -Dprivate_store=false
%endif

%meson_build


%install
%meson_install

# Creates the file for all locales
%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Notes.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Notes.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/bijiben
%{_datadir}/applications/org.gnome.Notes.desktop
%{_datadir}/bijiben/
%{_datadir}/dbus-1/services/org.gnome.Notes.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Notes.gschema.xml
# co-own these directories
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Notes-search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Notes.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Notes-symbolic.svg
%{_datadir}/metainfo/org.gnome.Notes.appdata.xml
%{_datadir}/mime/packages/org.gnome.Notes.xml
%{_libexecdir}/bijiben-shell-search-provider


%changelog
%autochangelog
