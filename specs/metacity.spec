Name: metacity
Version: 3.58.1
Release: %autorelease
Summary: Unobtrusive window manager
URL: https://wiki.gnome.org/Projects/Metacity
Source0: https://download.gnome.org/sources/metacity/3.58/metacity-%{version}.tar.xz

License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT-open-group

BuildRequires: autoconf, automake, gettext-devel, libtool, gnome-common
BuildRequires: desktop-file-utils
BuildRequires: itstool
BuildRequires: make
BuildRequires: vulkan-devel
BuildRequires: yelp-tools

BuildRequires: pkgconfig(gio-2.0) >= 2.67.3
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= 42.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.24.6
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xpresent)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xres) >= 1.2

Requires: gsettings-desktop-schemas
Requires: startup-notification

# http://bugzilla.redhat.com/605675
Provides: firstboot(windowmanager) = metacity

%description
Metacity is a window manager that integrates nicely with the GNOME desktop.
It strives to be quiet, small, stable, get on with its job, and stay out of
your attention.


%package devel
Summary: Development files for metacity
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the files needed for compiling programs using the
metacity-private library. Note that you are not supposed to write programs
using the metacity-private library, since it is a private API. This package
exists purely for technical reasons.


%prep
%autosetup -p1
# force regeneration
rm -f src/org.gnome.%{name}.gschema.valid


%build
# Always rerun configure for now
rm -f configure
(if ! test -x configure; then autoreconf -i -f; fi;
 %configure --disable-static --disable-schemas-compile)

SHOULD_HAVE_DEFINED="HAVE_SM HAVE_XINERAMA HAVE_RANDR"

for I in $SHOULD_HAVE_DEFINED; do
  if ! grep -q "define $I" config.h; then
    echo "$I was not defined in config.h"
    grep "$I" config.h
    exit 1
  else
    echo "$I was defined as it should have been"
    grep "$I" config.h
  fi
done

%make_build


%install
%make_install

%find_lang %{name} --all-name --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS HACKING rationales.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-message
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/gnome-control-center/keybindings/*
%{_libdir}/lib*.so.*
%{_libexecdir}/%{name}-dialog
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-message.1*
%{_datadir}/applications/%{name}.desktop
%{_userunitdir}/%{name}.service

%files devel
%{_bindir}/%{name}-theme-viewer
%{_includedir}/%{name}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/%{name}-theme-viewer.1*


%changelog
%autochangelog
