#define _version_suffix

%global with_mingw 0

%if 0%{?fedora}
%global with_mingw 1
%endif

Name:           spice-gtk
Version:        0.43
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
BuildRequires: libacl-devel
%if ! 0%{?flatpak}
BuildRequires: polkit-devel
%endif
BuildRequires: vala
BuildRequires: usbutils
BuildRequires: libsoup3-devel
BuildRequires: libphodav-devel >= 3.0
BuildRequires: lz4-devel
BuildRequires: gtk3-devel
BuildRequires: json-glib-devel
BuildRequires: spice-protocol >= 0.14.5
BuildRequires: gstreamer1-devel >= 1.10 gstreamer1-plugins-base-devel >= 1.10
BuildRequires: python3-six
BuildRequires: python3-pyparsing
BuildRequires: openssl-devel
BuildRequires: gnupg2
BuildRequires: libcap-ng-devel
BuildRequires: wayland-protocols-devel
BuildRequires: gi-docgen

%if %{with_mingw}
BuildRequires: mingw32-filesystem >= 104
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gtk3 >= 3.22
BuildRequires: mingw32-pixman
BuildRequires: mingw32-openssl
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-zlib
BuildRequires: mingw32-gstreamer1
BuildRequires: mingw32-gstreamer1-plugins-base
BuildRequires: mingw32-opus
BuildRequires: mingw32-spice-protocol >= 0.14.5
BuildRequires: mingw32-libusbx >= 1.0.21
BuildRequires: mingw32-usbredir >= 0.7.1
BuildRequires: mingw32-json-glib

BuildRequires: mingw64-filesystem >= 104
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-gtk3 >= 3.22
BuildRequires: mingw64-pixman
BuildRequires: mingw64-openssl
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-zlib
BuildRequires: mingw64-gstreamer1
BuildRequires: mingw64-gstreamer1-plugins-base
BuildRequires: mingw64-opus
BuildRequires: mingw64-spice-protocol >= 0.14.5
BuildRequires: mingw64-libusbx >= 1.0.21
BuildRequires: mingw64-usbredir >= 0.7.1
BuildRequires: mingw64-json-glib
%endif

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

%if %{with_mingw}
%package -n mingw32-spice-glib
Summary: GLib-based library to connect to SPICE servers
BuildArch: noarch
Requires: pkgconfig
Requires: mingw32-glib2
Requires: mingw32-spice-protocol

%description -n mingw32-spice-glib
A SPICE client library using GLib2.

%package -n mingw32-spice-gtk3
Summary: A GTK3 widget for SPICE clients
BuildArch: noarch
Requires: mingw32-spice-glib = %{version}-%{release}
Requires: mingw32-gtk3
Requires: pkgconfig
Obsoletes: mingw32-spice-gtk < 0.32
Obsoletes: mingw32-spice-gtk-static < 0.32-2

%description -n mingw32-spice-gtk3
Gtk+3 client libraries for SPICE desktop servers.

%package -n mingw64-spice-glib
Summary: GLib-based library to connect to SPICE servers
BuildArch: noarch
Requires: pkgconfig
Requires: mingw64-glib2
Requires: mingw64-spice-protocol

%description -n mingw64-spice-glib
A SPICE client library using GLib2.

%package -n mingw64-spice-gtk3
Summary: A GTK3 widget for SPICE clients
BuildArch: noarch
Requires: mingw64-spice-glib = %{version}-%{release}
Requires: mingw64-gtk3
Requires: pkgconfig
Obsoletes: mingw64-spice-gtk < 0.32
Obsoletes: mingw64-spice-gtk-static < 0.32-2

%description -n mingw64-spice-gtk3
Gtk+3 client libraries for SPICE desktop servers.

%{?mingw_debug_package}

%endif

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

%if %{with_mingw}
%mingw_meson \
  -Dbuiltin-mjpeg=false \
  -Dgtk_doc=disabled \
  -Dintrospection=disabled
%mingw_ninja
%endif


%check
%meson_test


%install
%meson_install

%if %{with_mingw}
%mingw_ninja_install
find %{buildroot}%{mingw32_mandir} %{buildroot}%{mingw64_mandir} -name "*.1" -delete 2>/dev/null ||:
%mingw_find_lang spice-gtk --all-name
%mingw_debug_install_post
%endif

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
%doc %{_datadir}/doc/SpiceClientGLib-2.0

%files -n spice-gtk3
%{_libdir}/libspice-client-gtk-3.0.so.*
%{_libdir}/girepository-1.0/SpiceClientGtk-3.0.typelib

%files -n spice-gtk3-devel
%{_libdir}/libspice-client-gtk-3.0.so
%{_includedir}/spice-client-gtk-3.0
%{_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{_datadir}/gir-1.0/SpiceClientGtk-3.0.gir
%doc %{_datadir}/doc/SpiceClientGtk-3.0

%files -n spice-gtk3-vala
%{_datadir}/vala/vapi/spice-client-glib-2.0.deps
%{_datadir}/vala/vapi/spice-client-glib-2.0.vapi
%{_datadir}/vala/vapi/spice-client-gtk-3.0.deps
%{_datadir}/vala/vapi/spice-client-gtk-3.0.vapi

%files tools
%{_bindir}/spicy
%{_bindir}/spicy-screenshot
%{_bindir}/spicy-stats

%if %{with_mingw}
%files -n mingw32-spice-glib -f mingw32-spice-gtk.lang
%doc AUTHORS
%doc COPYING
%doc README.md
%doc CHANGELOG.md
%{mingw32_bindir}/libspice-client-glib-2.0-8.dll
%{mingw32_bindir}/spicy-screenshot.exe
%{mingw32_bindir}/spicy-stats.exe
%{mingw32_libdir}/libspice-client-glib-2.0.dll.a
%{mingw32_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{mingw32_includedir}/spice-client-glib-2.0

%files -n mingw32-spice-gtk3
%{mingw32_bindir}/libspice-client-gtk-3.0-5.dll
%{mingw32_bindir}/spicy.exe
%{mingw32_libdir}/libspice-client-gtk-3.0.dll.a
%{mingw32_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{mingw32_includedir}/spice-client-gtk-3.0

%files -n mingw64-spice-glib -f mingw64-spice-gtk.lang
%doc AUTHORS
%doc COPYING
%doc README.md
%doc CHANGELOG.md
%{mingw64_bindir}/libspice-client-glib-2.0-8.dll
%{mingw64_bindir}/spicy-screenshot.exe
%{mingw64_bindir}/spicy-stats.exe
%{mingw64_libdir}/libspice-client-glib-2.0.dll.a
%{mingw64_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{mingw64_includedir}/spice-client-glib-2.0

%files -n mingw64-spice-gtk3
%{mingw64_bindir}/libspice-client-gtk-3.0-5.dll
%{mingw64_bindir}/spicy.exe
%{mingw64_libdir}/libspice-client-gtk-3.0.dll.a
%{mingw64_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{mingw64_includedir}/spice-client-gtk-3.0
%endif

%changelog
%autochangelog
