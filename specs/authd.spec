%global _hardened_build 1

Summary: A RFC 1413 ident protocol daemon
Name: authd
Version: 1.4.4
Release: 18%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/InfrastructureServices/authd
Obsoletes: pidentd < 3.2
Provides: pidentd = 3.2
Requires(post): openssl
Source0: https://github.com/InfrastructureServices/authd/releases/download/v1.4.4/authd-1.4.4.tar.gz
Source1: auth.socket
Source2: auth@.service
BuildRequires:  gcc
BuildRequires: openssl-devel gettext help2man systemd-units
BuildRequires: make
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
authd is a small and fast RFC 1413 ident protocol daemon
with both xinetd server and interactive modes that
supports IPv6 and IPv4 as well as the more popular features
of pidentd.

%prep
%autosetup

%build
make prefix=%{_prefix} CFLAGS="%{optflags}" \
        LDFLAGS="-lcrypto %{build_ldflags}"


%install
%make_install datadir=%{buildroot}/%{_datadir} \
	sbindir=%{buildroot}/%{_sbindir}

install -d %{buildroot}%{_unitdir}/
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/

install -d %{buildroot}%{_sysconfdir}/
touch %{buildroot}%{_sysconfdir}/ident.key

install -d %{buildroot}/%{_mandir}/man1/
help2man -N -v -V %{buildroot}/%{_sbindir}/in.authd -o \
         %{buildroot}/%{_mandir}/man1/in.authd.1

%find_lang %{name}

%post
/usr/sbin/adduser -s /sbin/nologin -u 98 -r -d '/' ident 2>/dev/null || true
/usr/bin/openssl rand -base64 -out %{_sysconfdir}/ident.key 32
echo CHANGE THE LINE ABOVE TO A PASSPHRASE >> %{_sysconfdir}/ident.key
/bin/chown ident:ident %{_sysconfdir}/ident.key
chmod o-rw %{_sysconfdir}/ident.key
%systemd_post auth.socket

%postun
%systemd_postun_with_restart auth.socket

%preun
%systemd_preun auth.socket

%files -f authd.lang
%license COPYING
%verify(not md5 size mtime user group) %config(noreplace) %attr(640,root,root) %{_sysconfdir}/ident.key
%doc COPYING README.html rfc1413.txt
%{_sbindir}/in.authd
%{_mandir}/*/*
%{_unitdir}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.4-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.4.4-9
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.4-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Pavel Zhukov <pzhukov@redhat.com> - 1.4.4-2
- hardened build with fedora specific flags

* Tue Feb 12 2019 Pavel Zhukov <pzhukov@redhat.com> - 1.4.4-1
- New release (v1.4.4)
- New upstream URL

