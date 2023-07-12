Version:        4.3.13

%global forgeurl https://github.com/cminyard/ser2net
%forgemeta

Name:           ser2net
Release:        %autorelease
Summary:        Proxy that allows TCP/UDP to serial port connections

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libgensio)
BuildRequires:  pkgconfig(libgensioosh)
BuildRequires:  pkgconfig(libgensiomdns)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  systemd-rpm-macros

%description
ser2net provides a way for a user to connect from a network connection to a 
serial port. It provides all the serial port setup, a configuration file to 
configure the ports, a control login for modifying port parameters, 
monitoring ports, and controlling ports.


%prep
%forgeautosetup


%build
autoreconf -f -i
%configure
%make_build


%install
%make_install
install -Dm0644 %{name}.yaml %{buildroot}%{_sysconfdir}/%{name}/%{name}.yaml
install -Dm0644 %{name}.service  %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license COPYING
%doc AUTHORS README.rst
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.yaml
%{_unitdir}/%{name}.service
%{_sbindir}/%{name}
%{_mandir}/man5/%{name}.yaml.5.gz
%{_mandir}/man8/%{name}.8.gz


%changelog
%autochangelog
