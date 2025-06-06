%global glib2_version 2.45.8
%global systemd_version 231

Summary:   Local caching server
Name:      passim
Version:   0.1.10
Release:   %autorelease
License:   LGPL-2.1-or-later
URL:       https://github.com/hughsie/%{name}
Source0:   https://github.com/hughsie/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: git-core
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gnutls-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libappstream-glib
BuildRequires: libsoup3-devel
BuildRequires: meson
BuildRequires: systemd-rpm-macros
BuildRequires: systemd >= %{systemd_version}

Recommends: avahi

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# Obsolete versions from before the subpackage split
Obsoletes: %{name} < 0.1.1-3

%description
Passim is a daemon that allows software to share files on your local network.

%package libs
Summary: Local caching server library
# Obsolete versions from before the subpackage split
Obsoletes: %{name} < 0.1.1-3

%description libs
libpassim is a library that allows software to share files on your local network
using the passimd daemon.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
rm %{buildroot}/var/lib/passim/data/*
%find_lang %{name}

%check
%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%post
%systemd_post passim.service

%preun
%systemd_preun passim.service

%postun
%systemd_postun_with_restart passim.service

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/passim
%config(noreplace)%{_sysconfdir}/passim.conf
%dir %{_datadir}/passim
%{_datadir}/passim/*.ico
%{_datadir}/passim/*.css
%{_datadir}/dbus-1/system.d/org.freedesktop.Passim.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Passim.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.Passim.service
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.Passim.svg
%{_datadir}/icons/hicolor/256x256/apps/org.freedesktop.Passim.png
%{_datadir}/metainfo/org.freedesktop.Passim.metainfo.xml
%{_libdir}/girepository-1.0/Passim-1.0.typelib
%{_libexecdir}/passimd
%{_mandir}/man1/passim.1*
%{_unitdir}/passim.service
/usr/lib/sysusers.d/passim.conf

%files libs
%license LICENSE
%{_libdir}/libpassim.so.1*

%files devel
%{_datadir}/gir-1.0/Passim-1.0.gir
%dir %{_includedir}/passim-1
%{_includedir}/passim-1/passim*.h
%{_libdir}/libpassim*.so
%{_libdir}/pkgconfig/passim.pc

%changelog
%autochangelog
