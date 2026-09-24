%global upstream_version 6.7.8-unstable

Name:           nemo
Summary:        File manager for Cinnamon
Version:        6.7.8^unstable
Release:        %autorelease
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz
Source1:        nemo-fedora.gschema.override

ExcludeArch:   %{ix86}

BuildSystem:   meson
BuildOption(conf): -D deprecated_warnings=false
BuildOption(conf): -D gtk_doc=false
BuildOption(conf): -D gtk_layer_shell=true
BuildOption(conf): -D selinux=true
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  python3-gobject-base
BuildRequires:  python3-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(cinnamon-desktop) >= 6.7.0
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xapp) >= 2.2.0
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(pango)

# the main binary links against libnemo-extension.so
# don't depend on soname, rather on exact version
Requires:       %{name}-extensions%{?_isa} = %{version}-%{release}
Requires:       redhat-menus
Requires:       gvfs-fuse%{?_isa}
Recommends:     gvfs-goa%{?_isa}
Requires:       xapps%{?_isa} >= 2.2.0
# required by nemo-action-layout-editor
Requires:       libxmlb%{?_isa}
Requires:       python3-cairo
Requires:       python3-gobject
# required for gtk-stock fallback
Recommends:     xapp-symbolic-icons
Recommends:     cinnamon-translations >= 6.7.0
Recommends:     nemo-search-helpers
Recommends:     folder-color-switcher-nemo

%description
Nemo is the file manager and graphical shell for the Cinnamon desktop
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote filesystems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the Cinnamon desktop.

%package extensions
Summary: Nemo extensions library
License:    LGPL-2.0-or-later

%description extensions
This package provides the libraries used by nemo extensions.

%package search-helpers
Summary: Nemo search helpers
License:    GPL-2.0-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   exif
Requires:   ghostscript
Requires:   poppler-utils
Requires:   python3-xlrd
Recommends: catdoc
Recommends: unzip

%description search-helpers
This package provides the search helpers used by nemo.


%package devel
Summary: Support for developing nemo extensions
License:    LGPL-2.0-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-extensions%{?_isa} = %{version}-%{release}


%description devel
This package provides libraries and header files needed
for developing nemo extensions.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%install -a
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/glib-2.0/schemas/nemo-fedora.gschema.override

# Only autostart in cinnamon and budgie
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  --add-only-show-in "X-Cinnamon;Budgie" \
  %{buildroot}%{_datadir}/applications/nemo-autostart.desktop
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/{nemo,nemo-autorun-software}.desktop

# create extensions directory
mkdir -p %{buildroot}%{_libdir}/nemo/extensions-3.0/

rm %{buildroot}%{_datadir}/nemo/search-helpers/id3.nemo_search_helper
rm %{buildroot}%{_datadir}/nemo/search-helpers/pdf2txt.nemo_search_helper

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc AUTHORS NEWS
%license COPYING COPYING-DOCS
%{_bindir}/nemo
%{_bindir}/nemo-autorun-software
%{_bindir}/nemo-connect-server
%{_bindir}/nemo-desktop
%{_bindir}/nemo-action-layout-editor
%{_bindir}/nemo-open-with
%{_libexecdir}/nemo-*
%dir %{_datadir}/nemo/
%{_datadir}/nemo/action-info.md
%{_datadir}/nemo/nemo-action-layout-editor-resources.gresource
%{_datadir}/nemo/actions/
%{_datadir}/nemo/icons/
%{_datadir}/nemo/layout-editor/
%{_datadir}/nemo/script-info.md
%{_datadir}/applications/*
%{_datadir}/mime/packages/nemo.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/dbus-1/services/nemo*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/polkit-1/actions/org.nemo.root.policy
%{_datadir}/gtksourceview-*/language-specs/nemo_*.lang
%{_mandir}/man1/nemo*

%files extensions
%license COPYING.EXTENSIONS COPYING.LIB
%{_libdir}/libnemo-extension.so.*
%{_libdir}/nemo/
%{_libdir}/girepository-1.0/Nemo-3.0.typelib

%files search-helpers
%{_bindir}/nemo-epub2text
%{_bindir}/nemo-mso-to-txt
%{_bindir}/nemo-odf-to-txt
%{_bindir}/nemo-ppt-to-txt
%{_bindir}/nemo-xls-to-txt
%{_datadir}/nemo/search-helpers/

%files devel
%{_includedir}/nemo/
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

%changelog
%autochangelog