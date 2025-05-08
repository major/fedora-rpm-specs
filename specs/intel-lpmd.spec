%global daemon_name intel_lpmd

Name:		intel-lpmd
Version:	0.0.9
Release:	%autorelease
Summary:	Intel Low Power Mode Daemon

License:	GPL-2.0-or-later
URL:		https://github.com/intel/intel-lpmd
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:	x86_64

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	libnl3-devel
BuildRequires:	libxml2-devel
BuildRequires:	libtool
BuildRequires:	upower-devel
BuildRequires:	systemd-devel
BuildRequires:	systemd-units

%description
Intel Low Power Model Daemon is a Linux daemon used to optimize active idle
power. It selects a set of most power efficient CPUs based on configuration
file or CPU topology. Based on system utilization and other hints, it puts
the system into Low Power Mode by activating the power efficient CPUs and
disabling the rest, and restoring the system from Low Power Mode by activating
all CPUs.

%prep
%autosetup -p1

# fedora path fix
sed -i -e "s|etc|usr/share|" configure.ac

%build
aclocal --install
gtkdocize --copy --flavour no-tmpl
autoreconf --install --verbose
%configure --disable-werror
%make_build

%install
%make_install
install -D -p -m 644 src/%{daemon_name}_dbus_interface.xml %{buildroot}/%{_datadir}/dbus-1/interfaces/org.freedesktop.%{daemon_name}.xml

%post
%systemd_post %{daemon_name}.service

%preun
%systemd_preun %{daemon_name}.service

%postun
%systemd_postun_with_restart %{daemon_name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/%{daemon_name}_control
%{_sbindir}/%{daemon_name}
%dir %{_sysconfdir}/%{daemon_name}
%config(noreplace) %{_sysconfdir}/%{daemon_name}/%{daemon_name}_config.xml
%config(noreplace) %{_sysconfdir}/%{daemon_name}/%{daemon_name}_config_F6_M170.xml
%config(noreplace) %{_sysconfdir}/%{daemon_name}/%{daemon_name}_config_F6_M189.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.%{daemon_name}.xml
%{_datadir}/dbus-1/system.d/org.freedesktop.%{daemon_name}.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.%{daemon_name}.service
%{_unitdir}/%{daemon_name}.service
%{_mandir}/man5/%{daemon_name}_config.xml.5*
%{_mandir}/man8/%{daemon_name}.8*
%{_mandir}/man8/%{daemon_name}_control.8*

%changelog
%autochangelog
