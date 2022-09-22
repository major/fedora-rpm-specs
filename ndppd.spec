%global commit e01d67a864bbeeb8e15f35ad955aecafa52e4c3d

Name:           ndppd
Version:        0.2.5
Release:        %autorelease
Summary:        NDP Proxy Daemon

Group:          System Environment/Daemons
License:        GPLv3
URL:            https://github.com/DanielAdolfsson/ndppd
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/raw/%{commit}/%{name}.service
Source2:        %{name}.conf

BuildRequires:  gcc-c++
BuildRequires:  make
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif

%description
ndppd, or NDP Proxy Daemon, is a daemon that proxies NDP (Neighbor
Discovery Protocol) messages between interfaces.

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
%if 0%{?fedora} || 0%{?rhel} >= 8
%systemd_postun_with_restart ndppd.service
%else
/bin/systemctl --system daemon-reload &> /dev/null || :
%endif

%post
%if 0%{?fedora} || 0%{?rhel} >= 8
%systemd_post ndppd.service
%else
/bin/systemctl --system daemon-reload &> /dev/null || :
/bin/systemctl --system preset ndppd &> /dev/null || :
%endif

%preun
%if 0%{?fedora} || 0%{?rhel} >= 8
%systemd_preun ndppd.service
%endif

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
