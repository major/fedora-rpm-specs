%global forgeurl https://github.com/darkk/redsocks
%global tag      release-%{version}
%global distprefix %{nil} 
%forgemeta

Name:           redsocks
Version:        0.5
Release:        %autorelease
Summary:        SOCKS and HTTP proxy redirector
# Majority of software is under Apache-2.0.
# base64.c/h is under LGPL-2.1-or-later
# md5.c/h is under Zlib
License:        Apache-2.0 AND LGPL-2.1-or-later AND Zlib
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        redsocks.conf
Source2:        redsocks.service
Source3:        redsocks.sysconfig
Source4:        redsocks.sysuser
Source5:        Apache-2.0.txt
Source6:        LGPL-2.1-or-later.txt
Source7:        Zlib.txt

# Proposed upstream: https://github.com/darkk/redsocks/pull/50
Patch0:         setgroups-before-setuid.patch
# Proposed upstream: https://github.com/darkk/redsocks/pull/123
Patch1:         libevent-2.1-compat.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  systemd-rpm-macros

%description
This tool allows you to redirect any TCP connection to SOCKS or HTTPS
proxy using your firewall, so redirection is system-wide.

%prep
%forgeautosetup -p1

%build
%make_build

%install
install -Dpm 755 redsocks %{buildroot}%{_bindir}/redsocks
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/redsocks.conf
install -dm  755 %{buildroot}%{_unitdir}
install -pm  644 %{SOURCE2} %{buildroot}%{_unitdir}
install -Ddm 755 %{buildroot}%{_sysconfdir}/sysconfig
install -pm  644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/redsocks
install -Dpm 644 %{SOURCE4} %{buildroot}%{_sysusersdir}/redsocks.conf
install -pm  644 %{SOURCE5} Apache-2.0.txt
install -pm  644 %{SOURCE6} LGPL-2.1-or-later.txt
install -pm  644 %{SOURCE7} Zlib.txt
install -Ddm 755 %{buildroot}%{_mandir}/man8
install -pm  644 debian/redsocks.8 %{buildroot}%{_mandir}/man8

%pre 
%sysusers_create_compat %{SOURCE3}

%post
%systemd_post redsocks.service

%preun
%systemd_preun redsocks.service

%postun
%systemd_postun_with_restart redsocks.service

%files
%license Apache-2.0.txt LGPL-2.1-or-later.txt Zlib.txt
%doc README README.html 
%{_mandir}/man8/%{name}.8*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysconfdir}/sysconfig/redsocks
%{_sysusersdir}/redsocks.conf

%changelog
%autochangelog
