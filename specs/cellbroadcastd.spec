%global gvdb_commit 4758f6fb7f889e074e13df3f914328f3eecb1fd3

Name:     cellbroadcastd
Version:  0.0.2
Release:  %autorelease
Summary:  DBus service for cellular broadcast messages
License:  GPL-3.0-or-later AND LGPL-2.1-or-later
URL:      https://gitlab.freedesktop.org/devrtz/%{name}
Source0:  %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:  https://gitlab.gnome.org/GNOME/gvdb/-/archive/%{gvdb_commit}/gvdb-%{gvdb_commit}.tar.gz

ExcludeArch:  %{ix86}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= 2.76
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.76
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gmobile) >= 0.4.0
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  pkgconfig(mm-glib) >= 1.24.0
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros

Requires:  hicolor-icon-theme
Requires:  libcellbroadcast%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
cellbroadcastd provides DBus daemon that manages cell broadcast messages via
ModemManager. It provides a storage for them and allows configuring channels
for the modem to watch out for.

%package -n libcellbroadcast
Summary:   Library to ease usage from applications

%description -n libcellbroadcast
Library to ease usage from applications.

%package -n libcellbroadcast-devel
Summary:   Development headers for libcellbroadcastd
Requires:  libcellbroadcast%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libcellbroadcast-devel
Development headers for libcellbroadcast.

%prep
%autosetup -n %{name}-v%{version}
mkdir subprojects/gvdb
tar -xf %{S:1} -C subprojects/gvdb --strip-components 1

%conf
%meson -Dsystemd_user_unit_dir="%{_userunitdir}"

%build
%meson_build

%install
%meson_install
rm %{buildroot}%{_libdir}/libcellbroadcast-0.0.a

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.freedesktop.cbd.desktop
dbus-run-session sh <<'SH'
%meson_test
SH

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service
%systemd_user_postun_with_reload %{name}.service
%systemd_user_postun %{name}.service

%files
%doc README.md
%license COPYING
%{_bindir}/cbcli
%{_datadir}/applications/org.freedesktop.cbd.desktop
%{_datadir}/dbus-1/interfaces/org.freedesktop.cbd.xml
%{_datadir}/dbus-1/services/org.freedesktop.cbd.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.cbd.enums.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.cbd.gschema.xml
%{_libexecdir}/cellbroadcastd
%{_userunitdir}/cellbroadcastd.service

%files -n libcellbroadcast
%{_libdir}/libcellbroadcast-0.0.so.0

%files -n libcellbroadcast-devel
%{_includedir}/libcellbroadcast-0.0/
%{_libdir}/libcellbroadcast-0.0.so
%{_libdir}/pkgconfig/libcellbroadcast-0.0.pc

%changelog
%autochangelog
