%global branch 1.28

Summary:       Shared code for mate-panel, mate-session, caja, etc
Name:          mate-desktop
# Automatically converted from old format: GPLv2+ and LGPLv2+ and MIT - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
Version:       %{branch}.2
Release:       %autorelease
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

# fedora specific settings
Source1:       mate-fedora-f34.gschema.override
Source2:       mate-rhel.gschema.override
Source3:       mate-mimeapps.list
Source4:       80-mate-compiz.preset

BuildRequires: dconf-devel
BuildRequires: desktop-file-utils
BuildRequires: gobject-introspection-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: startup-notification-devel
BuildRequires: gtk3-devel
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel
BuildRequires: cairo-gobject-devel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-configs = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} >= 34
Obsoletes: %{name}-systemd <= 1.26.0-5
%endif
Requires: redhat-menus
Requires: xdg-user-dirs-gtk
Requires: mate-control-center-filesystem
Requires: mate-panel
Requires: mate-notification-daemon
Requires: mate-user-guide
%if 0%{?fedora} && 0%{?fedora} >= 40
Requires: f40-backgrounds-mate
%endif
%if 0%{?fedora} && 0%{?fedora} == 39
Requires: f39-backgrounds-mate
%endif
%if 0%{?fedora} && 0%{?fedora} == 38
Requires: f38-backgrounds-mate
%endif

# Need this to pull in the right imsettings in groupinstalls
# See https://bugzilla.redhat.com/show_bug.cgi?id=1349743
Suggests:  imsettings-mate

%description
The mate-desktop package contains an internal library
(libmatedesktop) used to implement some portions of the MATE
desktop, and also some data files and other shared components of the
MATE user environment.

%package libs
Summary:   Shared libraries for libmate-desktop
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:   LicenseRef-Callaway-LGPLv2+

%description libs
Shared libraries for libmate-desktop

%package configs
Summary:    Configurations for Mate desktop
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} >= 40
Recommends: systemd-oomd-defaults
%endif
%if 0%{?fedora} && 0%{?fedora} <= 39
Recommends: earlyoom
%endif

%description configs
Configurations for Mate desktop

%package devel
Summary:    Libraries and headers for libmate-desktop
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for the MATE-internal private library
libmatedesktop.


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure                                                 \
     --enable-gtk-doc                                      \
     --disable-schemas-compile                             \
     --with-x                                              \
     --disable-static                                      \
     --with-pnp-ids-path="%{_datadir}/hwdata/pnp.ids"      \
     --enable-gtk-doc-html                                 \
     --enable-introspection=yes

make %{?_smp_mflags} V=1


%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'


desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-about.desktop

desktop-file-install                                         \
        --delete-original                                    \
        --dir=%{buildroot}%{_datadir}/applications           \
%{buildroot}%{_datadir}/applications/mate-color-select.desktop

%if 0%{?fedora} >= 34
install -D -m 0644 %SOURCE1 %{buildroot}%{_datadir}/glib-2.0/schemas/10_mate-fedora.gschema.override
%endif

%if 0%{?rhel}
install -D -m 0644 %SOURCE2 %{buildroot}%{_datadir}/glib-2.0/schemas/10_mate-rhel.gschema.override
%endif

mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %SOURCE3 %{buildroot}/%{_datadir}/applications/mate-mimeapps.list

%if 0%{?fedora} <= 39
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 644 %SOURCE4 %{buildroot}/%{_prefix}/lib/systemd/system-preset/80-mate-compiz.preset
%endif

%find_lang %{name} --with-gnome --all-name


%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_bindir}/mate-about
%{_bindir}/mate-color-select
%{_datadir}/applications/mate-about.desktop
%{_datadir}/applications/mate-color-select.desktop
%{_datadir}/mate-about
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-desktop-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/mate-desktop.svg
%{_mandir}/man1/*

%files libs -f %{name}.lang
%{_libdir}/libmate-desktop-2.so.*
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml
%{_libdir}/girepository-1.0/MateDesktop-2.0.typelib

%files configs
%if 0%{?fedora} <= 39
%{_prefix}/lib/systemd/system-preset/80-mate-compiz.preset
%endif
%if 0%{?fedora}
%{_datadir}/glib-2.0/schemas/10_mate-fedora.gschema.override
%endif
%{_datadir}/applications/mate-mimeapps.list
%{_datadir}/xdg-desktop-portal/mate-portals.conf
%if 0%{?rhel}
%{_datadir}/glib-2.0/schemas/10_mate-rhel.gschema.override
%endif

%files devel
%{_libdir}/libmate-desktop-2.so
%{_libdir}/pkgconfig/mate-desktop-2.0.pc
%{_includedir}/mate-desktop-2.0
%doc %{_datadir}/gtk-doc/html/mate-desktop
%{_datadir}/gir-1.0/MateDesktop-2.0.gir


%changelog
%autochangelog
