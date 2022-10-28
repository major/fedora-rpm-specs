%global commit e01d67a864bbeeb8e15f35ad955aecafa52e4c3d

Name:           ndppd
Version:        0.2.5
Release:        %autorelease
Summary:        NDP Proxy Daemon

License:        GPL-3.0-or-later
URL:            https://github.com/DanielAdolfsson/ndppd
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/raw/%{commit}/%{name}.service
Source2:        %{name}.conf

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

%description
ndppd, or NDP Proxy Daemon, is a daemon that proxies neighbor discovery
messages. It listens for neighbor solicitations on a specified interface
and responds with neighbor advertisements - as described in RFC 4861
section 7.2.

%prep
%setup -q

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=/usr
install -Dpm0644 %SOURCE1 %{buildroot}%{_unitdir}/ndppd.service
install -Dpm0644 %SOURCE2 %{buildroot}%{_tmpfilesdir}/ndppd.conf
install -dm0755 %{buildroot}/run/%{name}
install -Dpm0644 ndppd.conf-dist %{buildroot}%{_sysconfdir}/ndppd.conf

%postun
%systemd_postun_with_restart %{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%license LICENSE
%doc ChangeLog README
%{_sbindir}/ndppd
%{_mandir}/man1/ndppd.1.gz
%{_mandir}/man5/ndppd.conf.5.gz
%{_tmpfilesdir}/ndppd.conf
%{_unitdir}/ndppd.service
%dir /run/%{name}
%config(noreplace) %{_sysconfdir}/ndppd.conf

%changelog
%autochangelog
