# Requires explicit trust in builder's keyring
%bcond_without SIGCHECK

Name: dhcpcd
Version: 9.4.1
Release: 4%{?dist}
Summary: A minimalistic network configuration daemon with DHCPv4, rdisc and DHCPv6 support
License: BSD
# Moved to github
# https://github.com/NetworkConfiguration/dhcpcd
URL: http://roy.marples.name/projects/%{name}/
Source0: http://roy.marples.name/downloads/%{name}/%{name}-%{version}.tar.xz
Source1: %{name}.service
Source2: %{name}@.service
Source3: http://roy.marples.name/downloads/%{name}/%{name}-%{version}.tar.xz.distinfo.asc
Source4: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xa785ed2755955d9e93ea59f6597f97ea9ad45549#/roy-marples.name.asc
Source5: systemd-sysusers.conf
BuildRequires: gcc
BuildRequires: systemd-rpm-macros
BuildRequires: chrony
BuildRequires: systemd-devel
BuildRequires: ypbind
BuildRequires: make
%if %{with SIGCHECK}
BuildRequires: gnupg2
%endif
%{?systemd_requires}
%description
The dhcpcd package provides a minimalistic network configuration daemon
that supports IPv4 and IPv6 configuration including configuration discovery
through NDP, DHCPv4 and DHCPv6 protocols.

%prep
%if %{with SIGCHECK}
GPGHOME="$(mktemp -d ./gpghome-XXXXXXX)"
gpg --homedir "$GPGHOME" --import %{SOURCE4}
gpg --homedir "$GPGHOME" --verify %{SOURCE3}
rm -rf "$GPGHOME"
%endif
(cd %{_sourcedir} && tr -d '\r' <%{SOURCE3} | sha256sum -c)
%autosetup

%build
%configure \
    --dbdir=/var/lib/%{name}
%make_build

%check
make test

%install
export BINMODE=755
%make_install
find %{buildroot} -name '*.la' -delete -print
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}@.service
install -d %{buildroot}%{_sharedstatedir}/%{_name}

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}/hooks/10-wpa_supplicant
%{_datadir}/%{name}/hooks/15-timezone
%{_datadir}/%{name}/hooks/29-lookup-hostname
%{_datadir}/%{name}/hooks/50-yp.conf
%{_libdir}/%{name}
%{_libexecdir}/%{name}-hooks
%{_libexecdir}/%{name}-run-hooks
%{_mandir}/man5/%{name}.conf.5.gz
%{_mandir}/man8/%{name}-run-hooks.8.gz
%{_mandir}/man8/%{name}.8.gz
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%defattr(0644,root,dhcpcd,0755)
%{_sharedstatedir}/%{name}

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Petr Menšík <pemensik@redhat.com> - 9.4.1-1
- Update to 9.4.1 (#2016639)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Petr Menšík <pemensik@redhat.com> - 9.4.0-2
- Reenable net device binding

* Fri Mar 19 2021 Petr Menšík <pemensik@redhat.com> - 9.4.0-1
- Update to 9.4.0

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.11.3-13
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 6.11.3-7
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 26 2016 Pavel Šimerda <psimerda@redhat.com> - 6.11.3-1
- New version 6.11.3

* Wed Aug 10 2016 Pavel Šimerda <psimerda@redhat.com> - 6.11.2-1
- New version 6.11.2

* Fri Feb 19 2016 Pavel Šimerda <psimerda@redhat.com> - 6.10.1-4
- initial version
