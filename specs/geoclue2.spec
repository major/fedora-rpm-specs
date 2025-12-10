Name:           geoclue2
Version:        2.7.2
Release:        %autorelease
Summary:        Geolocation service

License:        GPL-2.0-or-later
URL:            http://www.freedesktop.org/wiki/Software/GeoClue/
Source0:        https://gitlab.freedesktop.org/geoclue/geoclue/-/archive/%{version}/geoclue-%{version}.tar.bz2
Source1:        geoclue2.sysusers

# Backport from upstream
## Generated with: git format-patch -N --stdout 2.7.2...master > geoclue-2.7.2-git41-backports.patch
Patch0:         geoclue-2.7.2-git41-backports.patch

BuildRequires:  avahi-glib-devel
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  json-glib-devel
BuildRequires:  libsoup3-devel
BuildRequires:  meson
BuildRequires:  ModemManager-glib-devel
BuildRequires:  systemd, systemd-rpm-macros
BuildRequires:  vala
Requires:       dbus
%{?sysusers_requires_compat}

Obsoletes:      geoclue2-server < 2.1.8

Obsoletes:      geoclue < 0.12.99-10
Obsoletes:      geoclue-devel < 0.12.99-10
Obsoletes:      geoclue-gsmloc < 0.12.99-10
Obsoletes:      geoclue-gui < 0.12.99-10
Obsoletes:      geoclue-gypsy < 0.12.99-10

%description
Geoclue is a D-Bus service that provides location information. The primary goal
of the Geoclue project is to make creating location-aware applications as
simple as possible, while the secondary goal is to ensure that no application
can access location information without explicit permission from user.


%package        libs
Summary:        Geoclue client library
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
Recommends:     %{name} = %{version}-%{release}

%description    libs
The %{name}-libs package contains a convenience library to interact with
Geoclue service.


%package        devel
Summary:        Development files for %{name}
# /docs/*xml is GFDL-1.1-or-later
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GFDL-1.1-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains files for developing applications that
use %{name}.


%package        demos
Summary:        Demo applications for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     %{name} = %{version}-%{release}
BuildRequires:  libnotify-devel

%description    demos
The %{name}-demos package contains demo applications that use %{name}.


%prep
%autosetup -n geoclue-%{version} -S git_am


%conf
%meson \
       -Ddbus-srv-user=geoclue \
       -Ddefault-wifi-url="https://api.beacondb.net/v1/geolocate" \
       -Ddefault-wifi-submit-url="https://api.beacondb.net/v2/geosubmit" \
       %{nil}


%build
%meson_build


%install
%meson_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/geoclue2.conf

# Home directory for the 'geoclue' user
mkdir -p $RPM_BUILD_ROOT/var/lib/geoclue


%pre
%sysusers_create_compat %{SOURCE1}
exit 0

%post
%systemd_post geoclue.service

%preun
%systemd_preun geoclue.service

%postun
%systemd_postun_with_restart geoclue.service


%files
%license COPYING
%doc NEWS
%config %{_sysconfdir}/geoclue/
%dir %{_libexecdir}/geoclue-2.0
%dir %{_libexecdir}/geoclue-2.0/demos
%{_sysconfdir}/xdg/autostart/geoclue-demo-agent.desktop
%{_libexecdir}/geoclue
%{_datadir}/dbus-1/system.d/org.freedesktop.GeoClue2.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.GeoClue2.service
%{_datadir}/polkit-1/rules.d/org.freedesktop.GeoClue2.rules
%{_datadir}/applications/geoclue-demo-agent.desktop
%{_mandir}/man5/geoclue.5*
%{_unitdir}/geoclue.service
%{_libexecdir}/geoclue-2.0/demos/agent
%{_sysusersdir}/geoclue2.conf
%attr(755,geoclue,geoclue) %dir /var/lib/geoclue

%files libs
%license COPYING.LIB
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Geoclue-2.0.typelib
%{_libdir}/libgeoclue-2.so.0*

%files devel
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2*.xml
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Geoclue-2.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/geoclue/
%{_datadir}/gtk-doc/html/libgeoclue/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgeoclue-2.0.*
%{_includedir}/libgeoclue-2.0/
%{_libdir}/pkgconfig/geoclue-2.0.pc
%{_libdir}/pkgconfig/libgeoclue-2.0.pc
%{_libdir}/libgeoclue-2.so

%files demos
%{_libexecdir}/geoclue-2.0/demos/where-am-i
%{_datadir}/applications/geoclue-where-am-i.desktop


%changelog
%autochangelog
