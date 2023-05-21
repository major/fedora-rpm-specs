#define _version_suffix

Name:           spice-gtk
Version:        0.42
Release:        %autorelease
Summary:        A GTK+ widget for SPICE clients

License:        LGPL-2.1-or-later AND MIT AND MIT-open-group and BSD-3-Clause
URL:            https://www.spice-space.org/spice-gtk.html
#VCS:           git:git://anongit.freedesktop.org/spice/spice-gtk
Source0:        https://www.spice-space.org/download/gtk/%{name}-%{version}%{?_version_suffix}.tar.xz
#Source1:        https://www.spice-space.org/download/gtk/%{name}-%{version}%{?_version_suffix}.tar.xz.sig
#Source2:        victortoso-E37A484F.keyring

BuildRequires: git-core
BuildRequires: meson
BuildRequires: usbredir-devel >= 0.7.1
BuildRequires: libusb1-devel >= 1.0.21
BuildRequires: pixman-devel libjpeg-turbo-devel
BuildRequires: opus-devel
BuildRequires: zlib-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libcacard-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libacl-devel
%if ! 0%{?flatpak}
BuildRequires: polkit-devel
%endif
BuildRequires: gtk-doc
BuildRequires: vala
BuildRequires: usbutils
BuildRequires: libsoup3-devel
BuildRequires: libphodav-devel >= 3.0
BuildRequires: lz4-devel
BuildRequires: gtk3-devel
BuildRequires: json-glib-devel
BuildRequires: spice-protocol >= 0.14.1
BuildRequires: gstreamer1-devel >= 1.10 gstreamer1-plugins-base-devel >= 1.10
BuildRequires: python3-six
BuildRequires: python3-pyparsing
BuildRequires: openssl-devel
BuildRequires: gnupg2
BuildRequires: libcap-ng-devel
BuildRequires: wayland-protocols-devel

Obsoletes: spice-gtk-python < 0.32

Requires: spice-glib%{?_isa} = %{version}-%{release}

%description
Client libraries for SPICE desktop servers.

%package -n spice-glib
Summary: A GObject for communicating with Spice servers

%description -n spice-glib
spice-client-glib-2.0 is a SPICE client library for GLib2.

%package -n spice-glib-devel
Summary: Development files to build Glib2 applications with spice-glib-2.0
Requires: spice-glib%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel

%description -n spice-glib-devel
spice-client-glib-2.0 is a SPICE client library for GLib2.

Libraries, includes, etc. to compile with the spice-glib-2.0 libraries

%package -n spice-gtk3
Summary: A GTK3 widget for SPICE clients
Requires: spice-glib%{?_isa} = %{version}-%{release}

%description -n spice-gtk3
spice-client-glib-3.0 is a SPICE client library for Gtk3.

%package -n spice-gtk3-devel
Summary: Development files to build GTK3 applications with spice-gtk-3.0
Requires: spice-gtk3%{?_isa} = %{version}-%{release}
Requires: spice-glib-devel%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: gtk3-devel
Obsoletes: spice-gtk-devel < 0.32

%description -n spice-gtk3-devel
spice-client-gtk-3.0 provides a SPICE viewer widget for GTK3.

Libraries, includes, etc. to compile with the spice-gtk3 libraries

%package -n spice-gtk3-vala
Summary: Vala bindings for the spice-gtk-3.0 library
Requires: spice-gtk3%{?_isa} = %{version}-%{release}
Requires: spice-gtk3-devel%{?_isa} = %{version}-%{release}

%description -n spice-gtk3-vala
A module allowing use of the spice-gtk-3.0 widget from vala

%package tools
Summary: Spice-gtk tools
Requires: spice-gtk3%{?_isa} = %{version}-%{release}

%description tools
Simple clients for interacting with SPICE servers.
spicy is a client to a SPICE desktop server.
spicy-screenshot is a tool to capture screen-shots of a SPICE desktop.


%prep
#gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git_am


%build

# meson macro has --auto-features=enabled

%meson \
  -Dbuiltin-mjpeg=false \
%ifarch s390x # https://gitlab.freedesktop.org/spice/spice-gtk/issues/120
  -Dusbredir=disabled \
%endif
%if 0%{?flatpak}
  -Dpolkit=disabled
%else
  -Dusb-acl-helper-dir=%{_libexecdir}/spice-gtk-%{_arch}/
%endif

%meson_build


%check
%meson_test


%install
%meson_install


%find_lang %{name}

%ldconfig_scriptlets
%ldconfig_scriptlets -n spice-glib
%ldconfig_scriptlets -n spice-gtk3


%files
%doc AUTHORS
%doc COPYING
%doc README.md
%doc CHANGELOG.md
%{_mandir}/man1/spice-client.1*

%files -n spice-glib -f %{name}.lang
%{_libdir}/libspice-client-glib-2.0.so.*
%{_libdir}/girepository-1.0/SpiceClientGLib-2.0.typelib
%if ! 0%{?flatpak}
%dir %{_libexecdir}/spice-gtk-%{_arch}/
%attr(4755, root, root) %{_libexecdir}/spice-gtk-%{_arch}/spice-client-glib-usb-acl-helper
%{_datadir}/polkit-1/actions/org.spice-space.lowlevelusbaccess.policy
%endif

%files -n spice-glib-devel
%{_libdir}/libspice-client-glib-2.0.so
%{_includedir}/spice-client-glib-2.0
%{_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{_datadir}/gir-1.0/SpiceClientGLib-2.0.gir
%doc %{_datadir}/gtk-doc/html/*

%files -n spice-gtk3
%{_libdir}/libspice-client-gtk-3.0.so.*
%{_libdir}/girepository-1.0/SpiceClientGtk-3.0.typelib

%files -n spice-gtk3-devel
%{_libdir}/libspice-client-gtk-3.0.so
%{_includedir}/spice-client-gtk-3.0
%{_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{_datadir}/gir-1.0/SpiceClientGtk-3.0.gir

%files -n spice-gtk3-vala
%{_datadir}/vala/vapi/spice-client-glib-2.0.deps
%{_datadir}/vala/vapi/spice-client-glib-2.0.vapi
%{_datadir}/vala/vapi/spice-client-gtk-3.0.deps
%{_datadir}/vala/vapi/spice-client-gtk-3.0.vapi

%files tools
%{_bindir}/spicy
%{_bindir}/spicy-screenshot
%{_bindir}/spicy-stats

%changelog
%autochangelog
