%if 0%{?with_snapshot}
%global gitdate              20220915
%global portable_commit      3f638e16a67691a3f11d5e745e545df531af92c3
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       43b3801c4cc6d22976048c9d833346a4f42bee72
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif

Summary:        OpenBGPD Routing Daemon
Name:           openbgpd
Version:        8.8
Release:        1%{?with_snapshot:.git%{gitdate}}%{?dist}
# OpenBGPD itself is ISC but uses other source codes, breakdown:
# BSD-2-Clause: include/sys/tree.h
# BSD-3-Clause: compat/{fmt_scaled,setproctitle,sha2,vis}.c and include/{sha2_openbsd,util,vis,sys/queue}.h
# LicenseRef-Fedora-Public-Domain: include/{{endian,sha2,stdlib,string,unistd},net/if,netinet/{in,ip_ipsp}}.h
#                                  and include/sys/{_null,socket,time,types,wait}.h
#                                  and compat/{{explicit_bzero,getrtable}.c,chacha_private.h}
License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://www.openbgpd.org/
%if !0%{?with_snapshot}
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenBGPD/%{name}-%{version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/OpenBGPD/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/BA3DA14FEE657A6D7931C08EC755429BA6A969A8
%else
Source0:        https://github.com/openbgpd-portable/openbgpd-portable/archive/%{portable_commit}/%{name}-portable-%{version}-%{portable_shortcommit}.tar.gz
Source1:        https://github.com/openbgpd-portable/openbgpd-openbsd/archive/%{openbsd_commit}/%{name}-openbsd-%{version}-%{openbsd_shortcommit}.tar.gz
%endif
Source3:        openbgpd.service
Source4:        openbgpd.tmpfilesd
Source5:        openbgpd.sysusersd
# Adjust path of Validated ROA Payloads (VRP) for rpki-client
Patch0:         openbgpd-6.7p0-rpki-client.patch
%if !0%{?with_snapshot}
BuildRequires:  gnupg2
%else
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  bison
%endif
BuildRequires:  gcc
BuildRequires:  libmnl-devel >= 1.0.4
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
Recommends:     rpki-client
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
OpenBGPD is a free implementation of the Border Gateway Protocol (BGP),
Version 4. It allows ordinary machines to be used as routers exchanging
routes with other systems speaking the BGP protocol.

%prep
%if !0%{?with_snapshot}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%else
%setup -q -n %{name}-portable-%{portable_commit}
tar xfz %{SOURCE1}
mv -f %{name}-openbsd-%{openbsd_commit} openbsd
./autogen.sh
%endif
%patch -P0 -p1 -b .rpki-client
touch -c -r bgpd.conf{.rpki-client,}

%build
%configure --with-privsep-user=bgpd --disable-bgplgd
# Workaround until autoconf generated './configure' supports '--runstatedir=/run/bgpd' option
sed -e 's|^\(runstatedir =\).*|\1 %{_rundir}/bgpd|g' -i {.,compat,include,src/{bgpctl,bgpd,bgplgd}}/Makefile
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir}/empty,%{_rundir}}/bgpd/
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/bgpd.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post bgpd.service

%preun
%systemd_preun bgpd.service

%postun
%systemd_postun_with_restart bgpd.service

%files
%license LICENSE
%doc AUTHORS README.md
%config(noreplace) %attr(0640,root,bgpd) %{_sysconfdir}/bgpd.conf
%dir %attr(0750,root,bgpd) %{_sysconfdir}/bgpd/
%{_unitdir}/bgpd.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/bgpctl
%{_sbindir}/bgpd
%{_mandir}/man5/bgpd.conf.5*
%{_mandir}/man8/bgpctl.8*
%{_mandir}/man8/bgpd.8*
%dir %attr(0755,root,root) %{_rundir}/bgpd/
%dir %attr(0711,root,root) %{_localstatedir}/empty/bgpd/

%changelog
* Sun Feb 09 2025 Robert Scheck <robert@fedoraproject.org> 8.8-1
- Upgrade to 8.8 (#2344212)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Robert Scheck <robert@fedoraproject.org> 8.7-1
- Upgrade to 8.7 (#2332838)

* Sun Sep 22 2024 Robert Scheck <robert@fedoraproject.org> 8.6-1
- Upgrade to 8.6 (#2313604)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Robert Scheck <robert@fedoraproject.org> 8.5-1
- Upgrade to 8.5 (#2294650)

* Thu Mar 07 2024 Robert Scheck <robert@fedoraproject.org> 8.4-1
- Upgrade to 8.4 (#2268423)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 15 2023 Robert Scheck <robert@fedoraproject.org> 8.3-1
- Upgrade to 8.3 (#2243809)

* Tue Oct 03 2023 Robert Scheck <robert@fedoraproject.org> 8.2-1
- Upgrade to 8.2 (#2241730)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Robert Scheck <robert@fedoraproject.org> 8.1-1
- Upgrade to 8.1 (#2222359)

* Fri May 05 2023 Robert Scheck <robert@fedoraproject.org> 8.0-1
- Upgrade to 8.0

* Thu Mar 23 2023 Robert Scheck <robert@fedoraproject.org> 7.9-1
- Upgrade to 7.9 (#2181220)

* Sat Mar 18 2023 Robert Scheck <robert@fedoraproject.org> 7.8-1
- Upgrade to 7.8 (#2179395)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 06 2022 Robert Scheck <robert@fedoraproject.org> 7.7-1
- Upgrade to 7.7 (#2132808)

* Thu Sep 15 2022 Robert Scheck <robert@fedoraproject.org> 7.6-1
- Upgrade to 7.6 (#2127225)

* Fri Aug 05 2022 Robert Scheck <robert@fedoraproject.org> 7.5-1
- Upgrade to 7.5 (#2107606)

* Sun Jul 31 2022 Robert Scheck <robert@fedoraproject.org> 7.4-3
- Added sysusers.d file to achieve user() and group() provides

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Robert Scheck <robert@fedoraproject.org> 7.4-1
- Upgrade to 7.4 (#2096896)

* Wed Apr 13 2022 Robert Scheck <robert@fedoraproject.org> 7.3-1
- Upgrade to 7.3 (#2075138)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Robert Scheck <robert@fedoraproject.org> 7.2-1
- Upgrade to 7.2 (#2007210)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Robert Scheck <robert@fedoraproject.org> 7.1-1
- Upgrade to 7.1 (#1976160)

* Fri Jun 04 2021 Robert Scheck <robert@fedoraproject.org> 7.0-1
- Upgrade to 7.0 (#1968016)

* Fri Apr 30 2021 Robert Scheck <robert@fedoraproject.org> 6.9p0-1
- Upgrade to 6.9p0 (#1955524)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.8p1-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.8p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Robert Scheck <robert@fedoraproject.org> 6.8p1-1
- Upgrade to 6.8p1 (#1895063)

* Tue Oct 20 2020 Robert Scheck <robert@fedoraproject.org> 6.8p0-1
- Upgrade to 6.8p0 (#1889826)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7p0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-2
- Changes to match the Fedora Packaging Guidelines (#1835023 #c2)

* Tue May 19 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-1
- Upgrade to 6.7p0

* Wed May 13 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-0.1.git20200512
- Upgrade to 6.7p0 (GIT 20200512)

* Thu Apr 30 2020 Robert Scheck <robert@fedoraproject.org> 6.6p0-1
- Upgrade to 6.6p0 (#1835023)
- Initial spec file for Fedora and Red Hat Enterprise Linux
