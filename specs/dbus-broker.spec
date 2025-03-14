%global dbus_user_id 81

Name:                 dbus-broker
Version:              36
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

%description
dbus-broker is an implementation of a message bus as defined by the D-Bus
specification. Its aim is to provide high performance and reliability, while
keeping compatibility to the D-Bus reference implementation. It is exclusively
written for Linux systems, and makes use of many modern features provided by
recent Linux kernel releases.

%package tests
Summary:              Internal unit and reference tests of dbus-broker
Requires:             %{name}%{_isa} = %{version}-%{release}

%description tests
dbus-broker's unit and reference tests that can be used to verify the functionality
of the installed dbus-broker.

%prep
%autosetup -p1

# Create a sysusers.d config file
cat >dbus-broker.sysusers.conf <<EOF
u dbus %{dbus_user_id} 'System Message Bus' - -
EOF

%build
%meson -Dselinux=true -Daudit=true -Ddocs=true -Dtests=true -Dsystem-console-users=gdm -Dlinux-4-17=true
%meson_build

%install
%meson_install

install -m0644 -D dbus-broker.sysusers.conf %{buildroot}%{_sysusersdir}/dbus-broker.conf

%check
%meson_test

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
%{_sysusersdir}/dbus-broker.conf

%files tests
%{_prefix}/lib/dbus-broker/tests/

%changelog
%autochangelog
