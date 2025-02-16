Version:        4.6.4

%global forgeurl https://github.com/cminyard/ser2net
%forgemeta

Name:           ser2net
Release:        %autorelease
Summary:        Proxy that allows TCP/UDP to serial port connections

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}.sysusers

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libgensio)
BuildRequires:  pkgconfig(libgensioosh)
BuildRequires:  pkgconfig(libgensiomdns)
# EL9 does not provide pkgconfig(pam) yet
%if 0%{?el9}
BuildRequires:  pam-devel
%else
BuildRequires:  pkgconfig(pam)
%endif
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  systemd-rpm-macros
%{?sysusers_requires_compat}

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
install -Dpm0644 %{name}.yaml %{buildroot}%{_sysconfdir}/%{name}/%{name}.yaml
install -Dpm0644 %{name}.service  %{buildroot}%{_unitdir}/%{name}.service
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_compat %{SOURCE1}

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
%{_sysusersdir}/%{name}.conf
%{_mandir}/man5/%{name}.yaml.5.gz
%{_mandir}/man8/%{name}.8.gz


%changelog
%autochangelog
