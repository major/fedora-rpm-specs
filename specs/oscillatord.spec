Name:           oscillatord
Version:        3.9.0
Release:        %autorelease
Summary:        Daemon for disciplining an oscillator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/Orolia2s/oscillatord
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gpsd-devel
BuildRequires:  json-c-devel
BuildRequires:  liboscillator-disciplining-devel >= %{version}
BuildRequires:  pps-tools-devel
BuildRequires:  sed
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  ubloxcfg-devel >= 1.16-1.20260223git499048b

Requires: liboscillator-disciplining = %{version}
Requires: ubloxcfg >= 1.16-1.20260223git499048b

%description
The oscillatord daemon takes input from a PHC clock, reporting once per second,
the phase error between an oscillator and a reference GNSS receiver. For an
example of such a device, please see the ptp_ocp kernel driver.

The phase error read is then used as an input to the disciplining-minipod
library which will compute a setpoint, used by oscillatord to control an
oscillator and discipline it to the 1PPS from a GNSS receiver. Oscillatord also
sets PHC'stime at start up, using Output from a GNSS receiver.

To communicate with GNSS receiver's serial it uses ubloxcfg

%prep
%autosetup
# Drop hardcoded CFLAGS
sed -e 's/-O0//g' -i CMakeLists.txt

%build
%cmake -DBUILD_UTILS=1
%cmake_build

%install
%cmake_install

# install default config
install -Dpm0644 example_configurations/%{name}_default.conf \
    %{buildroot}%{_sysconfdir}/%{name}.conf

%post
%systemd_post oscillatord.service

%preun
%systemd_preun oscillatord.service

%postun
%systemd_postun_with_restart oscillatord.service

%files
%license LICENSE
%doc README.md example_configurations
%{_bindir}/*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%exclude %{_unitdir}/%{name}@.service

%changelog
%autochangelog
