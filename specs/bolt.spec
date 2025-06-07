Name:          bolt
Version:       0.9.9
Release:       %autorelease
Summary:       Thunderbolt device manager
License:       LGPL-2.1-or-later
URL:           https://gitlab.freedesktop.org/bolt/bolt
Source0:       %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:        0001-test-test-unix-skip-unix-domain-socket-test.patch

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: libudev-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(systemd)
BuildRequires: polkit-devel
BuildRequires: systemd
%{?systemd_requires}

# for the integration test (optional)
%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires: python3-gobject-base
BuildRequires: python3-dbus
BuildRequires: python3-dbusmock
BuildRequires: umockdev-devel
%endif

%description
bolt is a system daemon to manage Thunderbolt devices via a D-BUS
API. Thunderbolt 3 introduced different security modes that require
devices to be authorized before they can be used. The D-Bus API can be
used to list devices, enroll them (authorize and store them in the
local database) and forget them again (remove previously enrolled
devices). It also emits signals if new devices are connected (or
removed). During enrollment devices can be set to be automatically
authorized as soon as they are connected.  A command line tool, called
boltctl, can be used to control the daemon and perform all the above
mentioned tasks.

%package tests
Summary: Test files for bolt
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
Test files for bolt

%prep
%autosetup -p1

%build
sed -i "s/WatchdogSec=3min/#WatchdogSec=3min/g" data/bolt.service.in
%meson -Ddb-name=boltd -Dinstall-tests=true
%meson_build

%check
%meson_test

%install
%meson_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/boltctl
%{_libexecdir}/boltd
%{_unitdir}/%{name}.service
%{_udevrulesdir}/*-%{name}.rules
%{_datadir}/dbus-1/system.d/org.freedesktop.bolt.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.bolt.xml
%{_datadir}/polkit-1/actions/org.freedesktop.bolt.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.bolt.rules
%{_datadir}/dbus-1/system-services/org.freedesktop.bolt.service
%{_mandir}/man1/boltctl.1*
%{_mandir}/man8/boltd.8*
%ghost %dir %{_localstatedir}/lib/boltd

%files tests
%{_libexecdir}/installed-tests/bolt

%changelog
%autochangelog
