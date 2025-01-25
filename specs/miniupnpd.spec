Name:       miniupnpd
Version:    2.3.7
Release:    1%{?dist}
Summary:    Lightweight UPnP IGD & PCP/NAT-PMP daemon

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://miniupnp.tuxfamily.org/
Source0:    http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
Source1:    miniupnpd.service
Patch0:     miniupnpd-init-selinux.patch

BuildRequires:  gcc
%{?systemd_requires}
BuildRequires:  systemd
%if 0%{?with_iptables}
BuildRequires:  iptables-devel
%else
Buildrequires:  libmnl-devel
Buildrequires:  libnftnl-devel
%endif
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  procps-ng

# requires ENABLE_HTTPS to be set
#BuildRequires:  openssl-devel
#BuildRequires:  zlib-devel


%description
The MiniUPnP daemon is an UPnP IGD & PCP/NAT-PMP daemon for gateway routers.

UPnP IGD & PCP/NAT-PMP are used to improve internet connectivity for devices behind
a NAT router. Any peer to peer network application such as games, IM, etc. can
benefit from a NAT router supporting UPnP IGD & PCP/NAT-PMP.


%prep
%autosetup -p1


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
./configure \
 --ipv6 \
 --igd2 \
%if 0%{?with_iptables}
 --firewall=iptables
%else
 --firewall=nftables
%endif
sed -i 's/ OS_NAME.*$/ OS_NAME "Fedora"/' config.h
sed -i 's/ OS_VERSION.*$/ OS_VERSION "%{fedora}\/%%s"/' config.h
sed -i 's/ OS_URL.*$/ OS_URL "https:\/\/getfedora.org"/' config.h
sed -i 's/^CFLAGS.*$//g' Makefile
sed -i 's/^LDFLAGS.*$//g' Makefile
sed -i 's/        policy drop;/        policy accept;/' netfilter_nft/scripts/nft_init.sh
%make_build


%install
export STRIP="/bin/true"
%make_install

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

#Do not ship SysVinit script
rm -f %{buildroot}/etc/init.d/%{name}

#sbin migration for F42+
%if 0%{?fedora} >= 42
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}/usr/sbin/%{name} %{buildroot}%{_bindir}/%{name}
%endif


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc INSTALL README
%{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*.sh
%config(noreplace) %{_sysconfdir}/%{name}/miniupnpd.conf
%{_mandir}/man8/%{name}.8.gz
%{_unitdir}/%{name}.service


%changelog
* Thu Jan 23 2025 - Michael Cronenworth <mike@cchtml.com> - 2.3.7-1
- Version update

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.6-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 - Michael Cronenworth <mike@cchtml.com> - 2.3.6-1
- Version update

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 - Michael Cronenworth <mike@cchtml.com> - 2.3.4-1
- Version update

* Wed Jul 26 2023 - Michael Cronenworth <mike@cchtml.com> - 2.3.3-1
- Version update
- Fix reported fields (RHBZ#2161103)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 - Michael Cronenworth <mike@cchtml.com> - 2.3.1-1
- Version update

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 03 2022 - Michael Cronenworth <mike@cchtml.com> - 2.3.0-1
- Version update
- Default to nftables

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 - Michael Cronenworth <mike@cchtml.com> - 2.2.0-1
- Version update

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 2.1-7
- Patch CVEs (RHBZ#1714990,1715005,1715006,1715007)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 2.1-5
- Rebuilt (iptables)

* Sun Feb 03 2019 - Michael Cronenworth <mike@cchtml.com> - 2.1-4
- Upstream patch for kernel 5.0 changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 - Michael Cronenworth <mike@cchtml.com> - 2.1-1
- Initial release

