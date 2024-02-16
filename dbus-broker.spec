%global dbus_user_id 81

Name:                 dbus-broker
Version:              35
Release:              %autorelease
Summary:              Linux D-Bus Message Broker
License:              Apache-2.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND (Apache-2.0 OR LGPL-2.1-or-later)
URL:                  https://github.com/bus1/dbus-broker
Source0:              https://github.com/bus1/dbus-broker/releases/download/v%{version}/dbus-broker-%{version}.tar.xz
BuildRequires:        pkgconfig(audit)
BuildRequires:        pkgconfig(expat)
BuildRequires:        pkgconfig(dbus-1)
BuildRequires:        pkgconfig(libcap-ng)
BuildRequires:        pkgconfig(libselinux)
BuildRequires:        pkgconfig(libsystemd)
BuildRequires:        pkgconfig(systemd)
BuildRequires:        gcc
BuildRequires:        glibc-devel
BuildRequires:        meson
BuildRequires:        python3-docutils
Requires:             dbus-common
Requires(pre):        shadow-utils

%description
dbus-broker is an implementation of a message bus as defined by the D-Bus
specification. Its aim is to provide high performance and reliability, while
keeping compatibility to the D-Bus reference implementation. It is exclusively
written for Linux systems, and makes use of many modern features provided by
recent Linux kernel releases.

%prep
%autosetup -p1

%build
%meson -Dselinux=true -Daudit=true -Ddocs=true -Dsystem-console-users=gdm -Dlinux-4-17=true
%meson_build

%install
%meson_install

%check
%meson_test

%pre
# create dbus user and group
getent group dbus >/dev/null || groupadd -f -g %{dbus_user_id} -r dbus
if ! getent passwd dbus >/dev/null ; then
    if ! getent passwd %{dbus_user_id} >/dev/null ; then
      useradd -r -u %{dbus_user_id} -g %{dbus_user_id} -d '/' -s /sbin/nologin -c "System message bus" dbus
    else
      useradd -r -g %{dbus_user_id} -d '/' -s /sbin/nologin -c "System message bus" dbus
    fi
fi
exit 0

%post
%systemd_post dbus-broker.service
%systemd_user_post dbus-broker.service
%journal_catalog_update

%preun
%systemd_preun dbus-broker.service
%systemd_user_preun dbus-broker.service

%postun
%systemd_postun dbus-broker.service
%systemd_user_postun dbus-broker.service

%triggerpostun -- dbus-daemon
if [ $2 -eq 0 ] && [ -x /usr/bin/systemctl ] ; then
        # The `dbus-daemon` package used to provide the default D-Bus
        # implementation. We continue to make sure that if you uninstall it, we
        # re-evaluate whether to enable dbus-broker to replace it. If we didnt,
        # you might end up without any bus implementation active.
        systemctl --no-reload          preset dbus-broker.service || :
        systemctl --no-reload --global preset dbus-broker.service || :
fi

%files
%license AUTHORS
%license LICENSE
%{_bindir}/dbus-broker
%{_bindir}/dbus-broker-launch
%{_journalcatalogdir}/dbus-broker.catalog
%{_journalcatalogdir}/dbus-broker-launch.catalog
%{_mandir}/man1/dbus-broker.1*
%{_mandir}/man1/dbus-broker-launch.1*
%{_unitdir}/dbus-broker.service
%{_userunitdir}/dbus-broker.service

%changelog
%autochangelog
