%global libcall_ui_commit 3a2044f8e7c45387954ed35d22c6b6309e6751d6

Name:       calls
Version:    50~rc.0
Release:    1%{?dist}
Summary:    A phone dialer and call handler

License:    GPL-3.0-or-later AND LGPL-2.1-or-later
URL:        https://gitlab.gnome.org/GNOME/calls
Source0:    https://gitlab.gnome.org/GNOME/calls/-/archive/v%{version_no_tilde _}/%{name}-v%{version_no_tilde _}.tar.gz
Source1:    https://gitlab.gnome.org/World/Phosh/libcall-ui/-/archive/%{libcall_ui_commit}/libcall-ui-%{libcall_ui_commit}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  dbus-daemon
BuildRequires:  pkgconfig(libcallaudio-0.1)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.76
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(libebook-contacts-1.2)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(libfeedback-0.0) >= 0.0.1
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gmobile) >= 0.3.0
BuildRequires:  gstreamer1-plugins-good-gtk
BuildRequires:  sofia-sip-glib-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  /usr/bin/xauth
BuildRequires:  libappstream-glib
BuildRequires:  python3-docutils
BuildRequires:  mobile-broadband-provider-info-devel

Requires:  hicolor-icon-theme
Requires:  mobile-broadband-provider-info

Recommends: feedbackd

Provides: gnome-calls = %{version}-%{release}
Provides: gnome-calls%{?_isa} = %{version}-%{release}

%description
A phone dialer and call handler.

%prep
%autosetup -a1 -p1 -n %{name}-v%{version_no_tilde _}

mv libcall-ui-%{libcall_ui_commit} subprojects/libcall-ui

%conf
%meson

%build
%meson_build

%install
%meson_install

# Remove call-ui translations
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/call-ui.mo

# We do not support the ofono backend
rm -rf %{buildroot}%{_libdir}/calls/plugins/provider/ofono/

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Calls.desktop

# Some tests are failing in the build environment, so we manually just run a handful for now.
LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test plugins
SH

%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/org.gnome.Calls-daemon.desktop
%{_userunitdir}/calls-daemon.service
%{_bindir}/gnome-%{name}

%dir %{_libdir}/calls/plugins/provider

%dir %{_libdir}/calls/plugins/provider/mm
%dir %{_libdir}/calls/plugins/provider/dummy
%dir %{_libdir}/calls/plugins/provider/sip

%{_libdir}/calls/plugins/provider/mm/libmm.so
%{_libdir}/calls/plugins/provider/mm/mm.plugin
%{_libdir}/calls/plugins/provider/dummy/dummy.plugin
%{_libdir}/calls/plugins/provider/dummy/libdummy.so
%{_libdir}/calls/plugins/provider/sip/libsip.so
%{_libdir}/calls/plugins/provider/sip/sip.plugin

%{_datadir}/dbus-1/services/org.gnome.Calls.service
%{_datadir}/glib-2.0/schemas/org.gnome.Calls.gschema.xml
%{_datadir}/applications/org.gnome.Calls.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Calls.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calls-symbolic.svg
%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml

%{_mandir}/man1/gnome-calls.1*

%doc README.md
%license COPYING

%changelog
%autochangelog
