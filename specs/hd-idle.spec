Name:           hd-idle
Version:        1.05
Release:        %autorelease
Summary:        Spin down idle [USB] hard disks
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://hd-idle.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Source1:        %{name}.service
Source2:        %{name}.default
Patch0:         %{name}-systemd-nodaemon.diff
Patch1:         %{name}-fix-sbin.diff
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd

%description
hd-idle is a utility program for spinning-down external disks after a period
of idle time. Since most external IDE disk enclosures don't support setting
the IDE idle timer, a program like hd-idle is required to spin down idle disks
automatically.

A word of caution: hard disks don't like spinning up too often. Laptop disks
are more robust in this respect than desktop disks but if you set your disks
to spin down after a few seconds you may damage the disk over time due to the
stress the spin-up causes on the spindle motor and bearings. It seems that
manufacturers recommend a minimum idle time of 3-5 minutes, the default in
hd-idle is 10 minutes.

One more word of caution: hd-idle will spin down any disk accessible via the
SCSI layer (USB, IEEE1394, ...) but it will not work with real SCSI disks
because they don't spin up automatically. Thus it's not called scsi-idle and
I don't recommend using it on a real SCSI system unless you have a kernel
patch that automatically starts the SCSI disks after receiving a sense buffer
indicating the disk has been stopped. Without such a patch, real SCSI disks
won't start again and you can as well pull the plug.


%prep
%autosetup -n %{name} -p1
sed -i 's/install -D -g root -o root/install -D/' Makefile

%build
%set_build_flags
%make_build

%install
%make_install
# Remove executable bit from manual page
find "%{buildroot}%{_mandir}" -executable -type f -exec chmod -x {} \;
install -dpm 0755 %{buildroot}%{_unitdir}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/*.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
%autochangelog
