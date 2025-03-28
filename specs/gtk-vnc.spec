# -*- rpm-spec -*-

# This spec file assumes you are building for Fedora 32 or newer,
# or for RHEL 8 or newer. It may need some tweaks for other distros.

%global tls_priority "@LIBVIRT,SYSTEM"
%global verdir %(echo ${version} | cut -d. -f1,2)

%global with_mingw 0

%if 0%{?fedora}
%global with_mingw 1
%endif

Summary: A GTK widget for VNC clients
Name: gtk-vnc
Version: 1.5.0
Release: %autorelease
License: LGPL-2.1-or-later
Source: https://download.gnome.org/sources/%{name}/%{verdir}/%{name}-%{version}.tar.xz
Patch: 0001-make-gtk-vnc-debug-work-with-new-glib.patch
Patch: 0002-Expand-log-message-to-include-log-domain-and-timesta.patch
URL: https://gitlab.gnome.org/GNOME/gtk-vnc
Requires: gvnc = %{version}-%{release}
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: gnutls-devel gmp-devel cyrus-sasl-devel zlib-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: vala
BuildRequires: pulseaudio-libs-devel
BuildRequires: perl-podlators
BuildRequires: meson
BuildRequires: gi-docgen

%if %{with_mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-cairo
BuildRequires: mingw32-gettext
BuildRequires: mingw32-gmp
BuildRequires: mingw32-gnutls
BuildRequires: mingw32-gtk3


BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-cairo
BuildRequires: mingw64-gettext
BuildRequires: mingw64-gmp
BuildRequires: mingw64-gnutls
BuildRequires: mingw64-gtk3
%endif

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%package -n gvnc
Summary: A GObject for VNC connections

%description -n gvnc
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

%package -n gvnc-devel
Summary: Libraries, includes, etc. to compile with the gvnc library
Requires: gvnc = %{version}-%{release}
Requires: pkgconfig

%description -n gvnc-devel
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

Libraries, includes, etc. to compile with the gvnc library

%package -n gvncpulse
Summary: A Pulse Audio bridge for VNC connections
Requires: gvnc = %{version}-%{release}

%description -n gvncpulse
gvncpulse is a bridge to the Pulse Audio system for VNC.
It allows VNC clients to play back audio on the local
system

%package -n gvncpulse-devel
Summary: Libraries, includes, etc. to compile with the gvncpulse library
Requires: gvncpulse = %{version}-%{release}
Requires: pkgconfig

%description -n gvncpulse-devel
gvncpulse is a bridge to the Pulse Audio system for VNC.
It allows VNC clients to play back audio on the local
system

Libraries, includes, etc. to compile with the gvnc library

%package -n gvnc-tools
Summary: Command line VNC tools
Requires: gvnc = %{version}-%{release}

%description -n gvnc-tools
Provides useful command line utilities for interacting with
VNC servers. Includes the gvnccapture program for capturing
screenshots of a VNC desktop

%package -n gtk-vnc2
Summary: A GTK3 widget for VNC clients
Requires: gvnc = %{version}-%{release}
Obsoletes: gtk-vnc < 1.0.0

%description -n gtk-vnc2
gtk-vnc is a VNC viewer widget for GTK3. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%package -n gtk-vnc2-devel
Summary: Development files to build GTK3 applications with gtk-vnc
Requires: gtk-vnc2 = %{version}-%{release}
Requires: pkgconfig
Requires: gtk3-devel
Obsoletes: gtk-vnc-devel < 1.0.0

%description -n gtk-vnc2-devel
gtk-vnc is a VNC viewer widget for GTK3. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

Libraries, includes, etc. to compile with the gtk-vnc library

%if %{with_mingw}
# Mingw32
%package -n mingw32-gvnc
Summary: MinGW Windows port of VNC GObject
BuildArch: noarch

%package -n mingw32-gvnc-tools
Summary: Command line VNC tools
BuildArch: noarch

%package -n mingw32-gtk-vnc2
Summary: A GTK3 widget for VNC clients
Requires: pkgconfig
Obsoletes: mingw32-gtk-vnc < 1.0.0
BuildArch: noarch

%description -n mingw32-gvnc
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

%description -n mingw32-gvnc-tools
Provides useful command line utilities for interacting with
VNC servers. Includes the gvnccapture program for capturing
screenshots of a VNC desktop

%description -n mingw32-gtk-vnc2
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

# Mingw64
%package -n mingw64-gvnc
Summary: MinGW Windows port of VNC GObject
BuildArch: noarch

%package -n mingw64-gvnc-tools
Summary: Command line VNC tools
BuildArch: noarch

%package -n mingw64-gtk-vnc2
Summary: A GTK3 widget for VNC clients
Requires: pkgconfig
Obsoletes: mingw64-gtk-vnc < 1.0.0
BuildArch: noarch

%description -n mingw64-gvnc
gvnc is a GObject for managing a VNC connection. It provides all the
infrastructure required to build a VNC client without having to deal
with the raw protocol itself.

%description -n mingw64-gvnc-tools
Provides useful command line utilities for interacting with
VNC servers. Includes the gvnccapture program for capturing
screenshots of a VNC desktop

%description -n mingw64-gtk-vnc2
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%{?mingw_debug_package}
%endif

%prep
%autosetup -n gtk-vnc-%{version} -p1

%build
%meson
%meson_build
chmod -x examples/*.pl examples/*.js examples/*.py

%if %{with_mingw}
%mingw_meson -Dintrospection=disabled -Dgi-docs=disabled
%mingw_ninja
%endif


%install
%meson_install

%find_lang %{name}

%if %{with_mingw}
export DESTDIR=%{buildroot}
%mingw_ninja install

rm -f $RPM_BUILD_ROOT%{mingw32_mandir}/man1/gvnccapture.1*
rm -f $RPM_BUILD_ROOT%{mingw64_mandir}/man1/gvnccapture.1*

%mingw_debug_install_post

%mingw_find_lang gtk-vnc
%endif

%check
%meson_test

%files -n gvnc -f %{name}.lang
%{_libdir}/libgvnc-1.0.so.*
%{_libdir}/girepository-1.0/GVnc-1.0.typelib
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/gvnc-1.0.deps
%{_datadir}/vala/vapi/gvnc-1.0.vapi

%files -n gvnc-devel
%{_libdir}/libgvnc-1.0.so
%dir %{_includedir}/gvnc-1.0/
%{_includedir}/gvnc-1.0/*.h
%{_libdir}/pkgconfig/gvnc-1.0.pc
%{_datadir}/gir-1.0/GVnc-1.0.gir
%{_datadir}/doc/gvnc/
%{_datadir}/doc/gvnc.toml

%files -n gvncpulse -f %{name}.lang
%{_libdir}/libgvncpulse-1.0.so.*
%{_libdir}/girepository-1.0/GVncPulse-1.0.typelib
%{_datadir}/vala/vapi/gvncpulse-1.0.deps
%{_datadir}/vala/vapi/gvncpulse-1.0.vapi

%files -n gvncpulse-devel
%{_libdir}/libgvncpulse-1.0.so
%dir %{_includedir}/gvncpulse-1.0/
%{_includedir}/gvncpulse-1.0/*.h
%{_libdir}/pkgconfig/gvncpulse-1.0.pc
%{_datadir}/gir-1.0/GVncPulse-1.0.gir

%files -n gvnc-tools
%doc AUTHORS
%doc ChangeLog
%doc ChangeLog-old
%doc NEWS
%doc README
%doc COPYING.LIB
%{_bindir}/gvnccapture
%{_mandir}/man1/gvnccapture.1*

%files -n gtk-vnc2
%{_libdir}/libgtk-vnc-2.0.so.*
%{_libdir}/girepository-1.0/GtkVnc-2.0.typelib
%{_datadir}/vala/vapi/gtk-vnc-2.0.deps
%{_datadir}/vala/vapi/gtk-vnc-2.0.vapi

%files -n gtk-vnc2-devel
%doc examples/gvncviewer.c
%doc examples/gvncviewer.js
%doc examples/gvncviewer.pl
%doc examples/gvncviewer.py
%{_libdir}/libgtk-vnc-2.0.so
%dir %{_includedir}/%{name}-2.0/
%{_includedir}/%{name}-2.0/*.h
%{_libdir}/pkgconfig/%{name}-2.0.pc
%{_datadir}/gir-1.0/GtkVnc-2.0.gir
%{_datadir}/doc/gtk-vnc/
%{_datadir}/doc/gtk-vnc.toml

%if %{with_mingw}
# Mingw32
%files -n mingw32-gvnc -f mingw32-gtk-vnc.lang
%doc AUTHORS
%doc ChangeLog
%doc ChangeLog-old
%doc NEWS
%doc README
%doc COPYING.LIB
%{mingw32_bindir}/libgvnc-1.0-0.dll
%{mingw32_libdir}/libgvnc-1.0.dll.a
%{mingw32_libdir}/pkgconfig/gvnc-1.0.pc
%{mingw32_includedir}/gvnc-1.0

%files -n mingw32-gtk-vnc2
%{mingw32_bindir}/libgtk-vnc-2.0-0.dll
%{mingw32_libdir}/libgtk-vnc-2.0.dll.a
%{mingw32_libdir}/pkgconfig/gtk-vnc-2.0.pc
%{mingw32_includedir}/gtk-vnc-2.0

%files -n mingw32-gvnc-tools
%{mingw32_bindir}/gvnccapture.exe

# Mingw64
%files -n mingw64-gvnc -f mingw64-gtk-vnc.lang
%doc AUTHORS
%doc ChangeLog
%doc ChangeLog-old
%doc NEWS
%doc README
%doc COPYING.LIB
%{mingw64_bindir}/libgvnc-1.0-0.dll
%{mingw64_libdir}/libgvnc-1.0.dll.a
%{mingw64_libdir}/pkgconfig/gvnc-1.0.pc
%{mingw64_includedir}/gvnc-1.0

%files -n mingw64-gtk-vnc2
%{mingw64_bindir}/libgtk-vnc-2.0-0.dll
%{mingw64_libdir}/libgtk-vnc-2.0.dll.a
%{mingw64_libdir}/pkgconfig/gtk-vnc-2.0.pc
%{mingw64_includedir}/gtk-vnc-2.0

%files -n mingw64-gvnc-tools
%{mingw64_bindir}/gvnccapture.exe
%endif

%changelog
%autochangelog
