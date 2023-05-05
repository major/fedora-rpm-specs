%global libcall_ui_commit 6798b38d4d66d069751151b3e9a202c6de8d7f3c

Name:		calls
Version:	45~alpha.0
Release:	2%{?dist}
Summary:	A phone dialer and call handler

License:	GPLv3+ and MIT
URL:		https://gitlab.gnome.org/GNOME/calls
Source0:	https://gitlab.gnome.org/GNOME/calls/-/archive/v45_alpha.0/%{name}-v45_alpha.0.tar.gz
Source1:	https://gitlab.gnome.org/World/Phosh/libcall-ui/-/archive/%{libcall_ui_commit}/libcall-ui-%{libcall_ui_commit}.tar.gz
Patch0:		calls-c99.patch

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:  dbus-daemon

BuildRequires:	pkgconfig(libcallaudio-0.1)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libhandy-1) >= 1.0.0
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(gom-1.0)
BuildRequires:	pkgconfig(libebook-contacts-1.2)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(mm-glib)
BuildRequires:	pkgconfig(libfeedback-0.0) >= 0.0.1
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	gstreamer1-plugins-good-gtk
BuildRequires:	sofia-sip-glib-devel

BuildRequires:	desktop-file-utils
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	/usr/bin/xauth
BuildRequires:	libappstream-glib
BuildRequires:  python3-docutils

Requires: hicolor-icon-theme

%description
A phone dialer and call handler.

%prep
%setup -a1 -q -n %{name}-v45_alpha.0
%patch -P 0 -p1

mv libcall-ui-%{libcall_ui_commit}/* subprojects/libcall-ui/

%build
%meson
%meson_build


%install
%meson_install

# Remove call-ui translations
rm %{buildroot}%{_datadir}/locale/ca/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pt_BR/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ro/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/uk/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fa/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fur/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/nl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pt/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sv/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/gl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/it/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fi/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/he/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ka/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/oc/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/tr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/el/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/hr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/cs/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/eu/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/hi/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/hu/LC_MESSAGES/call-ui.mo

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
* Wed May 03 2023 Florian Weimer <fweimer@redhat.com> - 45~alpha.0-2
- Port to C99

%autochangelog
