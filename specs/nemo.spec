%global upstream_version 6.7.3-unstable

Name:           nemo
Summary:        File manager for Cinnamon
Version:        6.7.3^unstable
Release:        1%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz
Source1:        nemo-fedora.gschema.override
Patch0:         fix_mount_action.patch

ExcludeArch:   %{ix86}

Requires:       redhat-menus
Requires:       gvfs-archive%{?_isa}
Requires:       gvfs-fuse%{?_isa}
Requires:       gvfs-goa%{?_isa}
Requires:       xapps%{?_isa} >= 2.2.0
# required for for gtk-stock fallback
Recommends:     xapp-symbolic-icons
Recommends:     cinnamon-translations >= 6.7.0
Recommends:     nemo-search-helpers
Recommends:     folder-color-switcher-nemo

BuildRequires:  meson
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
BuildRequires:  pkgconfig(libxml-2.0)
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

%description
Nemo is the file manager and graphical shell for the Cinnamon desktop
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote filesystems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the Cinnamon desktop.

%package extensions
Summary: Nemo extensions library
License:    LGPL-2.0-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description extensions
This package provides the libraries used by nemo extensions.

%package search-helpers
Summary: Nemo search helpers
License:    LGPL-2.0-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   exif
Requires:   ghostscript
Requires:   odt2txt
Requires:   poppler-utils
Requires:   python3-xlrd

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

%build
%meson \
  -D deprecated_warnings=false \
  -D gtk_doc=false \
  -D gtk_layer_shell=true \
  -D selinux=true
%meson_build

%install
%meson_install

install -D -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/glib-2.0/schemas/nemo-fedora.gschema.override

# Only autostart in cinnamon and budgie
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  --add-only-show-in "X-Cinnamon;Budgie" \
  %{buildroot}%{_datadir}/applications/nemo-autostart.desktop
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/{nemo,nemo-autorun-software}.desktop

# create extensions directoy
mkdir -p %{buildroot}%{_libdir}/nemo/extensions-3.0/

rm %{buildroot}%{_datadir}/nemo/search-helpers/id3.nemo_search_helper
rm %{buildroot}%{_datadir}/nemo/search-helpers/pdf2txt.nemo_search_helper

%ldconfig_scriptlets extensions

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
* Wed Jun 17 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.3^unstable-1
- Update to 6.7.3-unstable

* Sat May 23 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.2^unstable-2
- Drop some patches

* Sat May 23 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.2^unstable-1
- Update to 6.7.2-unstable

* Tue Apr 14 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-2
- Enable gtk_layer_shell

* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-1
- Update to 6.7.0-unstable

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Jan 11 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.3-2
- Fix mount action so it works compressed archives
- Add requires gvfs-archive

* Thu Jan 08 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.3-1
- Update to 6.6.3

* Tue Dec 16 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Wed Dec 10 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Feb 26 2025 Leigh Scott <leigh123linux@gmail.com> - 6.4.5-1
- Update to 6.4.5

* Sat Feb 08 2025 Leigh Scott <leigh123linux@gmail.com> - 6.4.4-1
- Update to 6.4.4

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 06 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.3-1
- Update to 6.4.3

* Mon Dec 02 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.1-1
- Update t0 6.4.1

* Wed Nov 27 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 6.2.8-2
- convert license to SPDX

* Tue Aug 13 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.8-1
- Update to 6.2.8

* Sat Jul 20 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.5-1
- Update to 6.2.5

* Wed Jul 17 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.4-1
- Update to 6.2.4

* Mon Jul 08 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Tue Jun 18 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Thu Jun 13 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.2-2
- Add buildrequires python3-packaging

* Fri Dec 29 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.2-1
- Update to 6.0.2 release

* Tue Dec 19 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.1-1
- Update to 6.0.1 release

* Sun Nov 19 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-1
- Update to 6.0.0 release
