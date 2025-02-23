%global tarball_version %%(echo %{version} | tr '~' '.')

%if 0%{?rhel}
%global bundled_rust_deps 1
%endif

# djvulibre is not available in RHEL 10+
%bcond djvu %{undefined rhel}

# Filter out soname provides for plugins
%global __provides_exclude_from ^(%{_libdir}/papers/.*\\.so|%{_libdir}/nautilus/extensions-4/.*\\.so)$

Name:           papers
Version:        47.3
Release:        %autorelease
Summary:        View multipage documents

# papers itself is:
SourceLicense:  GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND libtiff
# ... and its crate dependencies are:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# GPL-2.0-or-later
# MIT
# MIT AND (MIT OR Apache-2.0)
# MIT OR Apache-2.0
# Unlicense OR MIT
# Zlib
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND Zlib AND libtiff AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (Unlicense OR MIT)
URL:            https://gitlab.gnome.org/GNOME/Incubator/papers
Source:         https://download.gnome.org/sources/papers/47/papers-%{tarball_version}.tar.xz
# To generate vendored cargo sources:
#   tar xf papers-%%{tarball_version}.tar.xz ; pushd papers-%%{tarball_version}/shell-rs ; \
#   cargo vendor && tar Jcvf ../../papers-%%{tarball_version}-vendor.tar.xz ../shell-rs/vendor/ ; popd
Source1:        papers-%{tarball_version}-vendor.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(dbus-1)
%if %{with djvu}
BuildRequires:  pkgconfig(ddjvuapi)
%endif
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-unix-print)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-previewer%{?_isa} = %{version}-%{release}
Requires:       %{name}-thumbnailer%{?_isa} = %{version}-%{release}

# For hicolor icon theme directories
Requires:       hicolor-icon-theme

%description
Papers is a document viewer for multiple document formats for GNOME.


%package        libs
Summary:        Libraries for the Papers document viewer

%description    libs
This package contains shared libraries needed for Papers.


%package        devel
Summary:        Support for developing backends for the Papers document viewer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files needed for Papers
backend development.


%package        nautilus
Summary:        Papers extension for nautilus
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       nautilus%{?_isa}
Supplements:    (nautilus and %{name})

%description    nautilus
This package contains the Papers extension for the Nautilus file manager.
It adds an additional tab called "Document" to the file properties dialog.


%package        previewer
Summary:        Papers previewer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    previewer
This package brings the Papers previewer independently from Papers.
It provides the printing preview for the GTK printing dialog.


%package        thumbnailer
Summary:        Papers thumbnailer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    thumbnailer
This package brings the Papers thumbnailer independently from Papers.


%prep
%autosetup -p1 -n papers-%{tarball_version} %{?bundled_rust_deps:-a1}

%if 0%{?bundled_rust_deps}
%cargo_prep -v shell-rs/vendor
%else
rm shell-rs/Cargo.lock
%cargo_prep
%endif


%if !0%{?bundled_rust_deps}
%generate_buildrequires
cd shell-rs
%cargo_generate_buildrequires -a -t
cd ~-
%endif


%build
%meson \
       -Ddjvu=%{?with_djvu:enabled}%{!?with_djvu:disabled} \
       -Dintrospection=disabled \
       -Dtests=false \
       %{nil}

%meson_build

cd shell-rs
%cargo_license_summary -a
%{cargo_license -a} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif
cd ~-


%install
%meson_install

# Remove unused symbolic link
rm $RPM_BUILD_ROOT%{_libdir}/libppsshell-4.0.so

%find_lang papers --with-gnome


%check
%meson_test

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop


%files -f papers.lang
%doc README.md
%license COPYING
%license shell-rs/LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license shell-rs/cargo-vendor.txt
%endif
%{_bindir}/papers
# internal library not used by other apps, which is why it is not in -libs
%{_libdir}/libppsshell-4.0.so.4{,.*}
%{_datadir}/applications/org.gnome.Papers.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Papers.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Papers.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Papers-symbolic.svg
%{_mandir}/man1/papers.1*
%{_metainfodir}/org.gnome.Papers.metainfo.xml

%files libs
%license COPYING
%{_libdir}/libppsdocument-4.0.so.5{,.*}
%{_libdir}/libppsview-4.0.so.4{,.*}
%{_libdir}/papers/
%{_metainfodir}/papers-comicsdocument.metainfo.xml
%if %{with djvu}
%{_metainfodir}/papers-djvudocument.metainfo.xml
%endif
%{_metainfodir}/papers-pdfdocument.metainfo.xml
%{_metainfodir}/papers-tiffdocument.metainfo.xml
%{_metainfodir}/papers-xpsdocument.metainfo.xml

%files devel
%{_includedir}/papers/
%{_libdir}/libppsdocument-4.0.so
%{_libdir}/libppsview-4.0.so
%{_libdir}/pkgconfig/papers-document-4.0.pc
%{_libdir}/pkgconfig/papers-view-4.0.pc

%files nautilus
%{_libdir}/nautilus/extensions-4/libpapers-document-properties.so

%files previewer
%{_bindir}/papers-previewer
%{_datadir}/applications/org.gnome.Papers-previewer.desktop
%{_mandir}/man1/papers-previewer.1*

%files thumbnailer
%{_bindir}/papers-thumbnailer
%{_datadir}/thumbnailers/
%{_mandir}/man1/papers-thumbnailer.1*


%changelog
%autochangelog
