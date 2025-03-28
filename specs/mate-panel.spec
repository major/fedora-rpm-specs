%global branch 1.28

Name:          mate-panel
Version:       %{branch}.4
Release:       %autorelease
Summary:       MATE Desktop panel and applets
#libs are LGPLv2+ applications GPLv2+
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Source1:       mate-panel_fedora-30.layout
Source2:       mate-panel_rhel.layout
Source3:       mate-panel_fedora-40.layout

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
#for fish
Recommends:    fortune-mod
# rhbz (#1007219)
Requires:      caja-schemas

BuildRequires: desktop-file-utils
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: gtk-layer-shell-devel
BuildRequires: libmateweather-devel
BuildRequires: libwnck3-devel
BuildRequires: libSM-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-menus-devel
BuildRequires: wayland-devel
BuildRequires: yelp-tools

%description
MATE Desktop panel applets

%package libs
Summary:     Shared libraries for mate-panel
License:     LGPLv2+
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description libs
Shared libraries for libmate-desktop

%package devel
Summary:     Development files for mate-panel
Requires:    %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-panel

%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build

#libexecdir needed for gnome conflicts
%configure                                        \
           --disable-static                       \
           --disable-schemas-compile              \
           --libexecdir=%{_libexecdir}/mate-panel \
           --enable-introspection                 \
           --disable-gtk-doc                      \
           --enable-x11                           \
           --enable-wayland                       \
           --with-in-process-applets=all

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

# https://bugzilla.redhat.com/show_bug.cgi?id=2273561
# refresh translation message catalogs
# workaround to avoid missing strftime l10n entries.
(
  cd po
  make mate-panel.pot-update
  make update-po
  for f in mate-panel.pot *.po
  do
    sed -i '/^#, /d' $f
  done
  make update-gmo
)

make %{?_smp_mflags} V=1


%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/mate-panel.desktop

%if 0%{?fedora} && 0%{?fedora} <= 39
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/mate-panel/layouts/fedora.layout
%endif
%if 0%{?fedora} && 0%{?fedora} >= 40
install -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/mate-panel/layouts/fedora.layout
%endif
%if 0%{?rhel}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/mate-panel/layouts/rhel.layout
%endif

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/mate-desktop-item-edit
%{_bindir}/mate-panel
%{_bindir}/mate-panel-test-applets
#%%{_libexecdir}/mate-panel
%{_datadir}/glib-2.0/schemas/org.mate.panel.*.xml
%{_datadir}/applications/mate-panel.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mate-panel
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.ClockAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.FishAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.NotificationAreaAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.WnckletFactory.service
%{_libdir}/mate-panel

%files libs
%doc COPYING.LIB
%{_libdir}/libmate-panel-applet-4.so.1*
%{_libdir}/girepository-1.0/MatePanelApplet-4.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/mate-panel-applet/
%{_libdir}/libmate-panel-applet-4.so
%{_includedir}/mate-panel-4.0
%{_libdir}/pkgconfig/libmatepanelapplet-4.0.pc
%{_datadir}/gir-1.0/MatePanelApplet-4.0.gir


%changelog
%autochangelog
