Name:           openiked
Version:        7.3
Release:        5%{?dist}
Summary:        A free Internet Key Exchange (IKEv2) implementation

License:        ISC
URL:            https://github.com/openiked/openiked-portable
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenIKED/openiked-%{version}.tar.gz
Source1:        openiked.service
Source2:        sysusers.conf
Source3:        openiked-keygen
Source4:        openiked-keygen.service
Source5:        openiked-keygen.target

BuildRequires:  cmake
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  byacc
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-devel

%description
OpenIKED is a free, permissively licensed Internet Key Exchange (IKEv2)
implementation, developed as part of the OpenBSD project. It is intended to be
a lean, secure and inter-operable daemon that allows for easy setup and
management of IPsec VPNs.

%prep
%autosetup

%build
%cmake -DWITH_SYSTEMD:BOOL=ON
%cmake_build

%install
%cmake_install
install -p -D -m644 %{SOURCE1} %{buildroot}%{_unitdir}/openiked.service
install -p -D -m644 %{SOURCE2} %{buildroot}%{_sysusersdir}/openiked.conf
install -p -D -m755 %{SOURCE3} %{buildroot}%{_libexecdir}/openiked/openiked-keygen
install -p -m644 %{SOURCE4} %{buildroot}%{_unitdir}/openiked-keygen.service
install -p -m644 %{SOURCE5} %{buildroot}%{_unitdir}/openiked-keygen.target

%check
%{__cmake_builddir}/regress/dh/dhtest
%{__cmake_builddir}/regress/parser/test_parser

%pre
%sysusers_create_compat %{SOURCE2}

%post
%systemd_post openiked.service

%preun
%systemd_preun openiked.service

%postun
%systemd_postun_with_restart openiked.service

%files
%license LICENSE
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/iked.conf
%{_sbindir}/iked
%{_sbindir}/ikectl
%{_mandir}/man5/iked.conf.5.*
%{_mandir}/man8/ikectl.8.*
%{_mandir}/man8/iked.8.*
%{_unitdir}/openiked.service
%{_sysusersdir}/openiked.conf
%{_sysconfdir}/iked/ca
%{_sysconfdir}/iked/certs
%{_sysconfdir}/iked/crls
%{_sysconfdir}/iked/pubkeys/ipv4
%{_sysconfdir}/iked/pubkeys/ipv6
%{_sysconfdir}/iked/pubkeys/fqdn
%{_sysconfdir}/iked/pubkeys/ufqdn
%{_sysconfdir}/ssl/ikeca.cnf
%{_sysconfdir}/ssl/ikex509v3.cnf
%attr(0700,root,root) %{_sysconfdir}/iked/private
%{_libexecdir}/openiked/openiked-keygen
%{_unitdir}/openiked-keygen.service
%{_unitdir}/openiked-keygen.target
%dir %{_sysconfdir}/iked/
%dir %{_libexecdir}/openiked/
%dir %{_sysconfdir}/iked/pubkeys


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Henrik Boeving <hargonix@gmail.com> 7.3-1
- Updated to new release 7.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Henrik Boeving <hargonix@gmail.com> 7.2-3
- fixed keygen script

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 01 2023 Henrik Boeving <hargonix@gmail.com> 7.2-1
- Updated to new release 7.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 06 2022 Henrik Boeving <hargonix@gmail.com> 7.1-1
- Updated to new release 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 04 2021 Henrik Boeving <hargonix@gmail.com> 7.0-1
- Updated to new release 7.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 6.9.0-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Henrik Boeving <hargonix@gmail.com> - 6.9.0-1
- initial packaging

