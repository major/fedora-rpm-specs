Name:           accel-ppp
Version:        1.13.0
Release:        %autorelease
Summary:        High-performance VPN and broadband protocol server
License:        GPL-2.0-Only OR GPL-2.0-Or-Later OR MIT
URL:            https://accel-ppp.org/
Source:         https://github.com/accel-ppp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Use-PCRE2-instead-of-PCRE.patch
Patch1:		0002-Add-Fedora-CPack-option.patch
Patch2:		0003-Allow-building-in-source-directory-needed-for-EPEL8.patch
Patch3:		0004-Add-EPEL-10-CPack-option.patch
ExcludeArch:	%{ix86}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  systemd-rpm-macros

%description
accel-ppp is a Linux kernel-accelerated implementation of PPPoE, PPTP, L2TP
and other VPN and broadband protocols.

%prep
%autosetup -p1

%build
%if 0%{?rhel}
%cmake -DCMAKE_BUILD_TYPE=Release -DCPACK_TYPE=Centos%{rhel}
%endif
%if 0%{?fedora}
%cmake -DCMAKE_BUILD_TYPE=Release -DCPACK_TYPE=Fedora
%endif
%cmake_build

%install
%cmake_install

%post
%systemd_post accel-ppp.service

%preun
%systemd_preun accel-ppp.service

%postun
%systemd_postun accel-ppp.service

%files
%{_bindir}/accel-cmd
%{_bindir}/accel-pppd
%dir %{_datadir}/accel-ppp
%dir %{_datadir}/accel-ppp/l2tp
%{_datadir}/accel-ppp/l2tp/dictionary*
%dir %{_datadir}/accel-ppp/radius
%{_datadir}/accel-ppp/radius/dictionary*
%dir %{_libdir}/accel-ppp
%{_libdir}/accel-ppp/*
%{_mandir}/man1/accel-cmd.1.gz
%{_mandir}/man5/accel-ppp.conf.5.gz
%{_sysconfdir}/accel-ppp.conf.dist
%{_unitdir}/accel-ppp.service
%license COPYING

%changelog
%autochangelog
