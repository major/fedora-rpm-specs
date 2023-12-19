%bcond	gnome		1
%bcond	gnome45		%[0%{?fedora} >= 39 || 0%{?rhel} >= 10]
%bcond	gnome_flashback	1
%bcond	mate		1
%bcond	xfce		1

Name:          workrave
Version:       1.10.52
Release:       %autorelease
Summary:       Program that assists in the recovery and prevention of RSI
# Based on older packages by Dag Wieers <dag@wieers.com> and Steve Ratcliffe
License:       GPL-3.0-or-later AND LGPL-2.0-or-later
URL:           https://workrave.org/
%global tag %(echo %{version} | sed -e 's/\\./_/g')
Source0:       https://github.com/rcaelers/workrave/archive/v%{tag}/%{name}-v%{tag}.tar.gz

Obsoletes:     %{name}-gtk2 < 1.10.37-1
Provides:      %{name}-gtk2 = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(glib-2.0) >= 2.28.0
BuildRequires: pkgconfig(gio-2.0) >= 2.26.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires: pkgconfig(sigc++-2.0) >= 2.2.4.2
BuildRequires: pkgconfig(glibmm-2.4) >= 2.28.0
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.0.0
BuildRequires: gobject-introspection-devel >= 0.6.7
BuildRequires: boost-devel
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-cheetah
BuildRequires: python3-jinja2
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libpulse) >= 0.9.15
BuildRequires: pkgconfig(libpulse-mainloop-glib) >= 0.9.15
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: autoconf, automake, libtool, autoconf-archive
BuildRequires: desktop-file-utils
%if %{with gnome_flashback}
BuildRequires: pkgconfig(libgnome-panel)
%endif
%if %{with gnome}
BuildRequires: pkgconfig(gtk4)
%endif
%if %{with xfce}
BuildRequires: pkgconfig(libxfce4panel-2.0) >= 4.12
%endif
%if %{with mate}
BuildRequires: pkgconfig(libmatepanelapplet-4.0)
%endif

Requires:      dbus-common
Recommends:    (%{name}-cinnamon if cinnamon)
Recommends:    (%{name}-gnome if gnome-shell)
Recommends:    (%{name}-gnome-flashback if gnome-panel)
Recommends:    (%{name}-mate if mate-panel)
Recommends:    (%{name}-xfce if xfce4-panel)
Recommends:    gstreamer1-plugins-base
Recommends:    gstreamer1-plugins-good
Obsoletes:     %{name}-devel < %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

%global _description Workrave is a program that assists in the recovery and prevention of\
Repetitive Strain Injury (RSI). The program frequently alerts you to\
take micro-pauses, rest breaks and restricts you to your daily limit.

%description
%{_description}

%package cinnamon
Requires:      %{name} = %{version}-%{release}
Summary:       Workrave applet for Cinnamon desktop

%description cinnamon
%{_description}

This package provides an applet for the Cinnamon desktop.

%package gnome
Requires:      %{name} = %{version}-%{release}
Summary:       Workrave applet for GNOME desktop

%description gnome
%{_description}

This package provides an applet for the GNOME desktop.

%package gnome-flashback
Requires:      %{name} = %{version}-%{release}
Summary:       Workrave applet for GNOME Flashback

%description gnome-flashback
%{_description}

This package provides an applet for the GNOME Flashback panel.

%package mate
Requires:      %{name} = %{version}-%{release}
Summary:       Workrave applet for MATE

%description mate
%{_description}

This package provides an applet for the MATE panel.

%package xfce
Requires:      %{name} = %{version}-%{release}
Summary:       Workrave applet for Xfce

%description xfce
%{_description}

This package provides an applet for the Xfce panel.


%prep
%autosetup -n workrave-%{tag} -p1
touch ChangeLog
# https://bugzilla.redhat.com/show_bug.cgi?id=304121
sed -i -e '/^DISTRIBUTION_HOME/s/\/$//' frontend/gtkmm/src/Makefile.*


# use versioned python command
%py3_shebang_fix libs/dbus/bin/dbusgen.py
sed -i 's/AC_CHECK_PROG(PYTHON, python, python)/AC_CHECK_PROG(PYTHON, python3, python3)/' configure.ac

%build
if [ ! -x configure ]; then
  ### Needed for snapshot releases.
  NOCONFIGURE=1 ./autogen.sh
fi

# gnome3 is flashback panel applet, not gnome-shell
%configure \
%if %{with gnome_flashback}
  --enable-gnome3 \
%else
  --disable-gnome3 \
%endif
%if %{with gnome45}
  --enable-gnome45 \
%endif
%if %{with mate}
  --enable-mate \
%else
  --disable-mate \
%endif
%if %{with xfce}
  --enable-xfce \
%else
  --disable-xfce \
%endif
  --disable-indicator \
  --disable-static --disable-xml

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete
# workrave does not provide a public API
rm -f %{buildroot}%{_datadir}/gir-1.0/*.gir
rm -f %{buildroot}%{_libdir}/*.so

%find_lang %{name}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README.md
%{_bindir}/workrave
%{_datadir}/workrave/
%{_datadir}/sounds/workrave/
%{_datadir}/icons/hicolor/16x16/apps/workrave.png
%{_datadir}/icons/hicolor/24x24/apps/workrave.png
%{_datadir}/icons/hicolor/32x32/apps/workrave.png
%{_datadir}/icons/hicolor/48x48/apps/workrave.png
%{_datadir}/icons/hicolor/64x64/apps/workrave.png
%{_datadir}/icons/hicolor/96x96/apps/workrave.png
%{_datadir}/icons/hicolor/128x128/apps/workrave.png
%{_datadir}/icons/hicolor/scalable/workrave-sheep.svg
%{_datadir}/icons/hicolor/scalable/apps/workrave.svg
%{_datadir}/metainfo/workrave.appdata.xml
%{_datadir}/applications/workrave.desktop
%{_datadir}/dbus-1/services/org.workrave.Workrave.service
%{_datadir}/glib-2.0/schemas/org.workrave.*.xml
# support library for gtk3 applets
%{_libdir}/girepository-1.0/Workrave-1.0.typelib
%{_libdir}/libworkrave-private-1.0.so.*

%files cinnamon
%dir %{_datadir}/cinnamon/
%dir %{_datadir}/cinnamon/applets/
%{_datadir}/cinnamon/applets/workrave@workrave.org/

%if %{with gnome}
%files gnome
%{_libdir}/girepository-1.0/Workrave-2.0.typelib
%{_libdir}/libworkrave-gtk4-private-1.0.so.*
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/extensions/
%{_datadir}/gnome-shell/extensions/workrave@workrave.org/
%endif

%if %{with gnome_flashback}
%files gnome-flashback
%{_libdir}/gnome-panel/modules/libworkrave-applet.so
%endif

%if %{with xfce}
%files xfce
%{_libdir}/xfce4/panel/plugins/libworkrave-plugin.so
%{_datadir}/xfce4/panel/plugins/workrave-xfce-applet.desktop
%endif

%if %{with mate}
%files mate
%{_libdir}/mate-applets/workrave-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.WorkraveAppletFactory.service
%{_datadir}/mate-panel/applets/org.workrave.WorkraveApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/workrave-menu.xml
%endif

%changelog
%autochangelog
