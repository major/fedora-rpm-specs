%global apiver 2.91

%global fmt_version 11.0.0
%global fribidi_version 1.0.0
%global glib2_version 2.72.0
%global gnutls_version 3.2.7
%global gtk3_version 3.24.22
%global gtk4_version 4.14.0
%global icu_uc_version 4.8
%global libsystemd_version 220
%global pango_version 1.22.0
%global pcre2_version 10.21
%global simdutf_version 7.2.1

Name:           vte291
Version:        0.81.0
Release:        %autorelease
Summary:        GTK terminal emulator library

# libvte-2.91.so is generated from LGPLv2+ and MIT sources
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND X11 AND CC-BY-4.0

URL:            https://wiki.gnome.org/Apps/Terminal/VTE
Source0:        https://download.gnome.org/sources/vte/0.81/vte-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/vte/-/merge_requests/2
Patch0:         0001-Only-use-fast_float-when-std-from_chars-is-insuffici.patch

BuildRequires:  pkgconfig(fmt) >= %{fmt_version}
BuildRequires:  pkgconfig(fribidi) >= %{fribidi_version}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnutls) >= %{gnutls_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(icu-uc) >= %{icu_uc_version}
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpcre2-8) >= %{pcre2_version}
BuildRequires:  pkgconfig(libsystemd) >= %{libsystemd_version}
BuildRequires:  pkgconfig(pango) >= %{pango_version}
BuildRequires:  pkgconfig(simdutf) >= %{simdutf_version}
BuildRequires:  fast_float-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala

Requires:       fribidi >= %{fribidi_version}
Requires:       glib2 >= %{glib2_version}
Requires:       gnutls%{?_isa} >= %{gnutls_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       libicu%{?_isa} >= %{icu_uc_version}
Requires:       pango >= %{pango_version}
Requires:       pcre2%{?_isa} >= %{pcre2_version}
Requires:       systemd-libs%{?_isa} >= %{libsystemd_version}
Requires:       vte-profile

Conflicts:      gnome-terminal < 3.20.1-2

%description
VTE is a library implementing a terminal emulator widget for GTK+. VTE
is mainly used in gnome-terminal, but can also be used to embed a
console/terminal in games, editors, IDEs, etc.

%package        gtk4
Summary:        GTK4 terminal emulator library

# libvte-2.91.so is generated from LGPLv2+ and MIT sources
License:        LGPL-3.0-or-later AND MIT AND X11

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gtk4
VTE is a library implementing a terminal emulator widget for GTK 4. VTE
is mainly used in gnome-terminal, but can also be used to embed a
console/terminal in games, editors, IDEs, etc.

%package        devel
Summary:        Development files for GTK+ 3 %{name}

# vte-2.91 is generated from GPLv3+ sources, while the public headers are
# LGPLv3+
License:        GPL-3.0-or-later AND LGPL-3.0-or-later

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing GTK+ 3 applications that use %{name}.

%package        gtk4-devel
Summary:        Development files for GTK 4 %{name}

# vte-2.91 is generated from GPLv3+ sources, while the public headers are
# LGPLv3+
License:        GPL-3.0-or-later AND LGPL-3.0-or-later

Requires:       %{name}-gtk4%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description gtk4-devel
The %{name}-gtk4-devel package contains libraries and header files for
developing GTK 4 applications that use %{name}.

# vte-profile is deliberately not noarch to avoid having to obsolete a noarch
# subpackage in the future when we get rid of the vte3 / vte291 split. Yum is
# notoriously bad when handling noarch obsoletes and insists on installing both
# of the multilib packages (i686 + x86_64) as the replacement.
%package -n     vte-profile
Summary:        Profile script for VTE terminal emulator library
License:        GPL-3.0-or-later
# vte.sh was previously part of the vte3 package
Conflicts:      vte3 < 0.36.1-3

%description -n vte-profile
The vte-profile package contains a profile.d script for the VTE terminal
emulator library.

%prep
%autosetup -p1 -n vte-%{version}
%if 0%{?flatpak}
# Install user units where systemd macros expect them
sed -i -e "/^vte_systemduserunitdir =/s|vte_prefix|'/usr'|" meson.build
%endif

%build
%meson --buildtype=plain -Ddocs=true -Dgtk3=true -Dgtk4=true
%meson_build

%install
%meson_install
rm %{buildroot}/%{_datadir}/applications/org.gnome.Vte.App.Gtk3.desktop
rm %{buildroot}/%{_datadir}/applications/org.gnome.Vte.App.Gtk4.desktop

%find_lang vte-%{apiver}

%files -f vte-%{apiver}.lang
%license COPYING.LGPL3
%license COPYING.XTERM
%doc README.md
%{_libdir}/libvte-%{apiver}.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Vte-2.91.typelib
%{_userunitdir}/vte-spawn-.scope.d
%{_datadir}/xdg-terminals/org.gnome.Vte.App.Gtk3.desktop
%{_datadir}/xdg-terminals/org.gnome.Vte.App.Gtk4.desktop
%dir %{_datadir}/vte-2.91
%dir %{_datadir}/vte-2.91/terminfo
%dir %{_datadir}/vte-2.91/terminfo/x
%{_datadir}/vte-2.91/terminfo/x/xterm-256color

%files gtk4
%{_libdir}/libvte-%{apiver}-gtk4.so.0*
%{_libdir}/girepository-1.0/Vte-3.91.typelib

%files devel
%license COPYING.GPL3
%{_bindir}/vte-%{apiver}
%{_includedir}/vte-%{apiver}/
%{_libdir}/libvte-%{apiver}.so
%{_libdir}/pkgconfig/vte-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Vte-2.91.gir
%{_datadir}/glade/
%doc %{_docdir}/vte-2.91/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/vte-2.91.deps
%{_datadir}/vala/vapi/vte-2.91.vapi

%files gtk4-devel
%{_bindir}/vte-%{apiver}-gtk4
%{_includedir}/vte-%{apiver}-gtk4/
%{_libdir}/libvte-%{apiver}-gtk4.so
%{_libdir}/pkgconfig/vte-%{apiver}-gtk4.pc
%{_datadir}/gir-1.0/Vte-3.91.gir
%doc %{_docdir}/vte-2.91-gtk4/
%{_datadir}/vala/vapi/vte-2.91-gtk4.deps
%{_datadir}/vala/vapi/vte-2.91-gtk4.vapi

%files -n vte-profile
%license COPYING.GPL3
%{_libexecdir}/vte-urlencode-cwd
%{_sysconfdir}/profile.d/vte.csh
%{_sysconfdir}/profile.d/vte.sh

%changelog
%autochangelog
