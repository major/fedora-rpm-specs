Name:		driverctl
Version:	0.121
Release:	%autorelease
Summary:	Device driver control utility

License:	LGPL-2.1-or-later
URL:		https://gitlab.com/driverctl/driverctl
BuildArch:	noarch

Source0:	https://gitlab.com/driverctl/driverctl/-/archive/%{version}/driverctl-%{version}.tar.bz2

# for udev macros
BuildRequires: systemd
BuildRequires: make
Requires(post,postun): %{_sbindir}/udevadm
Requires: coreutils udev

%description
driverctl is a tool for manipulating and inspecting the system
device driver choices.

Devices are normally assigned to their sole designated kernel driver
by default. However in some situations it may be desireable to
override that default, for example to try an older driver to
work around a regression in a driver or to try an experimental alternative
driver. Another common use-case is pass-through drivers and driver
stubs to allow userspace to drive the device, such as in case of
virtualization.

driverctl integrates with udev to support overriding
driver selection for both cold- and hotplugged devices from the
moment of discovery, but can also change already assigned drivers,
assuming they are not in use by the system. The driver overrides
created by driverctl are persistent across system reboots
by default.

%prep
%setup -q

%install
%make_install PREFIX=%{_prefix} SBINDIR=%{_sbindir}

%files
%license COPYING
%doc README TODO
%{_sbindir}/driverctl
%{_udevrulesdir}/*.rules
%{_udevrulesdir}/../vfio_name
%{_unitdir}/driverctl@.service
%dir %{_sysconfdir}/driverctl.d
%{_datadir}/bash-completion/
%{_mandir}/man8/driverctl.8*

%post
%udev_rules_update

%postun
%udev_rules_update

%changelog
%autochangelog
