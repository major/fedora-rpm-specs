Name:             3proxy
Version:          1.0.0
Release:          %autorelease

Summary:          Tiny but very powerful proxy
Summary(ru):      Маленький, но крайне мощный прокси-сервер

License:          BSD-3-Clause OR Apache-2.0 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Url:              https://3proxy.org/
Source0:          https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:          3proxy.cfg
Source3:          3proxy.service

BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    openssl-devel
BuildRequires:    pam-devel
BuildRequires:    pcre2-devel
BuildRequires:    systemd-rpm-macros

# I correct config path in man only. It is fully Fedora related.
Patch0:           3proxy-1.0.0-config-path.patch
# Adapt manpages to reflect renamed proxy binary
Patch1:           3proxy-1.0.0-manpage.patch

%description
%{name} -- light proxy server.
Universal proxy server with HTTP, HTTPS, SOCKS v4, SOCKS v4a, SOCKS v5, FTP,
POP3, UDP and TCP portmapping, access control, bandwith control, traffic
limitation and accounting based on username, client IP, target IP, day time,
day of week, etc.

%description -l ru
%{name} -- маленький прокси сервер.
Это универсальное решение поддерживающее HTTP, HTTPS, SOCKS v4, SOCKS v4a,
SOCKS v5, FTP, POP3, UDP и TCP проброс портов (portmapping), списки доступа
управление скоростью доступа, ограничением трафика и статистикоу, базирующейся
на имени пользователя, слиентском IP адресе, IP цели, времени дня, дня недели
и т.д.


%prep
%autosetup -p1

# To use "fedora" CFLAGS (exported)
sed -i -e "s/^CFLAGS [?]=\+/CFLAGS +=/" -e "s/^CFLAGS =/CFLAGS +=/" Makefile.Linux

%build
%set_build_flags
%make_build -f Makefile.Linux PREFIX=

%install
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man{5,8}
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_libdir}/%{name}

install -m755 -D bin/%{name} %{buildroot}%{_bindir}/%{name}
install -m755 -D bin/ftppr %{buildroot}%{_bindir}/ftppr
install -m755 -D bin/imapp %{buildroot}%{_bindir}/imapp
install -m755 -D bin/crypt %{buildroot}%{_bindir}/mycrypt
install -m755 -D bin/pop3p %{buildroot}%{_bindir}/pop3p
install -m755 -D bin/proxy %{buildroot}%{_bindir}/htproxy
install -m755 -D bin/smtpp %{buildroot}%{_bindir}/smtpp
install -m755 -D bin/socks %{buildroot}%{_bindir}/socks
install -m755 -D bin/tcppm %{buildroot}%{_bindir}/tcppm
install -m755 -D bin/tlspr %{buildroot}%{_bindir}/tlspr
install -m755 -D bin/udppm %{buildroot}%{_bindir}/udppm

install -m755 -D bin/*.ld.so %{buildroot}%{_libdir}/%{name}/

install -p -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.cfg
install -p -m644 -D %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service

for man in man/*.5 ; do
  install -p -m644 "$man" "%{buildroot}%{_mandir}/man5/"
done
for man in man/*.8 ; do
  install -p -m644 "$man" "%{buildroot}%{_mandir}/man8/"
done
echo ".so 3proxy_crypt.8" > %{buildroot}%{_mandir}/man8/mycrypt.8

%check
# Upstream does not provide an automated test suite.
# Smoke test the built binaries.
%{buildroot}%{_bindir}/mycrypt test password

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license copying
%doc README.md authors
%{_bindir}/%{name}
%{_bindir}/ftppr
%{_bindir}/htproxy
%{_bindir}/imapp
%{_bindir}/mycrypt
%{_bindir}/pop3p
%{_bindir}/smtpp
%{_bindir}/socks
%{_bindir}/tcppm
%{_bindir}/tlspr
%{_bindir}/udppm
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.ld.so
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%dir %{_localstatedir}/log/%{name}
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*
%{_unitdir}/%{name}.service

%changelog
%autochangelog
