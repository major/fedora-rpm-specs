Name:           cambalache
Version:        0.99.8
Release:        %autorelease
Summary:        User interface maker

# Most files under LGPL-2.1-only

# GNU General Public License v2.0 or later
# cambalache/app/cambalache.css
# cambalache/cambalache.css

# GNU General Public License, Version 2
# tools/cmb_catalog_gen/cmb-catalog-gen.in
# tools/cmb_catalog_gen/cmb_catalog_db.py
# tools/cmb_catalog_gen/cmb_catalog_utils.c
# tools/cmb_catalog_gen/cmb_catalog_utils.h
# tools/cmb_catalog_gen/cmb_gir_data.py
# tools/cmb_init_dev.py
# tools/db-codegen.py
# tools/update-supporters.py

License:        LGPL-2.1-only AND GPL-2.0-only AND GPL-2.0-or-later
URL:            https://gitlab.gnome.org/jpu/cambalache
Source:         %{url}/-/archive/%{version}/cambalache-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  pkgconfig(casilda-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pygobject-3.0)

BuildRequires:  gtksourceview5-devel
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pytest
BuildRequires:  webkitgtk6.0-devel
BuildRequires:  webkit2gtk4.1-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:  cambalache-data
Requires:  hicolor-icon-theme
# Needed for ownership of %%{_datadir}/gir-1.0
Requires:  gobject-introspection-devel%{?_isa}
# Needed at runtime
Requires:  libadwaita
Requires:  pkgconfig(casilda-1.0)
Requires:  python3-gobject-base
Requires:  python3-lxml
Requires:  gtksourceview5-devel
Requires:  webkitgtk6.0-devel
Requires:  webkit2gtk4.1-devel

%description
Cambalache is a RAD tool for Gtk 4 and 3 with a clear MVC design and data model
first philosophy. This translates to a wide feature coverage with minimal/none
developer intervention for basic support.

%package data
Summary: Shared data files for Cambalache
BuildArch: noarch

%description data
Common data files used across all architectures.

%prep
%autosetup -n cambalache-%{version}


%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
# Starting the application requires a display, so tests cannot at present be run, nor can anything
# that starts the application
# https://gitlab.gnome.org/jpu/cambalache/-/issues/271
desktop-file-validate %{buildroot}/%{_datadir}/applications/ar.xjuan.Cambalache.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/ar.xjuan.Cambalache.metainfo.xml

%files -f %{name}.lang
%license COPYING
%license COPYING.GPL
%doc README.md
%doc CHANGELOG.md
%doc SUPPORTERS.md
%{_bindir}/cambalache
%{_bindir}/cmb-catalog-gen
%{_datadir}/applications/ar.xjuan.Cambalache.desktop
%{_datadir}/gir-1.0/CambalachePrivate-3.0.gir
%{_datadir}/gir-1.0/CambalachePrivate-4.0.gir
%{_datadir}/gir-1.0/CmbCatalogUtils-3.0.gir
%{_datadir}/gir-1.0/CmbCatalogUtils-4.0.gir
%{_datadir}/glib-2.0/schemas/ar.xjuan.Cambalache.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/ar.xjuan.Cambalache.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/ar.xjuan.Cambalache.mime.svg
%{_datadir}/icons/hicolor/symbolic/apps/ar.xjuan.Cambalache-symbolic.svg
%{_metainfodir}/ar.xjuan.Cambalache.metainfo.xml
# These should likely be added to filesystem package
%dir %{_datadir}/mime
%dir %{_datadir}/mime/packages
%{_datadir}/mime/packages/ar.xjuan.Cambalache.mime.xml
%{python3_sitelib}/cambalache/
%{python3_sitelib}/cmb_catalog_gen/
%dir %{_libdir}/cambalache
%{_libdir}/cambalache/CambalachePrivate-3.0.typelib
%{_libdir}/cambalache/CambalachePrivate-4.0.typelib
%{_libdir}/cambalache/libcambalacheprivate-3.so
%{_libdir}/cambalache/libcambalacheprivate-4.so
%dir %{_libdir}/cmb_catalog_gen
%{_libdir}/cmb_catalog_gen/CmbCatalogUtils-3.0.typelib
%{_libdir}/cmb_catalog_gen/CmbCatalogUtils-4.0.typelib
%{_libdir}/cmb_catalog_gen/libcmbcatalogutils-3.so
%{_libdir}/cmb_catalog_gen/libcmbcatalogutils-4.so

%files data
%license COPYING
%license COPYING.GPL
%dir %{_datadir}/cambalache
%{_datadir}/cambalache/*.gresource
%dir %{_datadir}/cambalache/catalogs
%{_datadir}/cambalache/catalogs/*.xml

%changelog
%autochangelog
