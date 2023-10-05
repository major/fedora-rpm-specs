Name:             rtkit
Version:          0.11
# -b is needed because of https://pagure.io/fedora-infra/rpmautospec/issue/228
# Remove if the version is ever bumped (or rpmautospec fixed).
Release:          %autorelease -b17
Summary:          Realtime Policy and Watchdog Daemon
# The daemon itself is GPLv3+, the reference implementation for the client MIT
# The LICENSE file incorrectly states that the client is under BSD.
License:          GPL-3.0-or-later AND MIT
URL:              http://git.0pointer.net/rtkit.git/
Requires:         dbus
Requires:         polkit
BuildRequires:    make
BuildRequires:    systemd-devel
BuildRequires:    systemd-rpm-macros
BuildRequires:    dbus-devel >= 1.2
BuildRequires:    libcap-devel
BuildRequires:    polkit-devel
BuildRequires:    autoconf automake libtool
%{?sysusers_requires_compat}
Source0:          http://0pointer.de/public/%{name}-%{version}.tar.xz
Source1:          rtkit.sysusers
Patch:            rtkit-mq_getattr.patch
Patch:            0001-SECURITY-Pass-uid-of-caller-to-polkit.patch
Patch:            rtkit-controlgroup.patch

# Temporarily disable -Werror=format-security since it breaks the build
Patch:            format-security.patch

Patch:            0001-Fix-borked-error-check.patch
Patch:            0001-systemd-update-sd-daemon.-ch.patch
Patch:            0002-Remove-bundled-copy-of-sd-daemon.-ch.patch

Patch:            remove-debug-messages.patch

%description
RealtimeKit is a D-Bus system service that changes the
scheduling policy of user processes/threads to SCHED_RR (i.e. realtime
scheduling mode) on request. It is intended to be used as a secure
mechanism to allow real-time scheduling to be used by normal user
processes.

%prep
%autosetup -p1

%build
autoreconf -fvi
%configure --with-systemdsystemunitdir=%{_unitdir}
%make_build
./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml

%install
%make_install
install -Dm0644 org.freedesktop.RealtimeKit1.xml %{buildroot}%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/rtkit.conf

%pre
%sysusers_create_compat %{SOURCE1}

%post
%systemd_post rtkit-daemon.service
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :

%preun
%systemd_preun rtkit-daemon.service

%postun
%systemd_postun_with_restart rtkit-daemon.service

%files
%doc README GPL LICENSE rtkit.c rtkit.h
%attr(0755,root,root) %{_sbindir}/rtkitctl
%attr(0755,root,root) %{_libexecdir}/rtkit-daemon
%{_datadir}/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
%{_prefix}/lib/systemd/system/rtkit-daemon.service
%{_mandir}/man8/*
%{_sysusersdir}/rtkit.conf

%changelog
%autochangelog
