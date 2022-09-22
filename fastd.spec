#%%global gitver 7dc53ab69e494b9bfb982f729d9f2c510b3629ec
#%%global gitshort %(r=%{gitver}; echo ${r:0:7})

%if 0%{?gitver:1}
  %global srcurl   https://github.com/NeoRaider/%{name}/archive/%{gitver}.tar.gz#/%{name}-%{gitver}.tar.gz
  %global setuppath %{name}-%{gitver}
%else
  %global srcurl   https://github.com/NeoRaider/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
  %global setuppath %{name}-%{version}
%endif


Name:           fastd
Version:        22
Release:        7%{?gitshort:.git%{gitshort}}%{?dist}
Summary:        Fast and secure tunneling daemon

License:        BSD
URL:            https://github.com/NeoRaider/fastd/wiki
Source0:        %{srcurl}

BuildRequires:  gcc
BuildRequires:  meson
%if 0%{?rhel} < 8
BuildRequires:  python-sphinx
%else
BuildRequires:  python3-sphinx
%endif

BuildRequires:  bison
BuildRequires:  json-c-devel
BuildRequires:  libcap-devel
BuildRequires:  libmnl-devel
BuildRequires:  libsodium-devel
BuildRequires:  libuecc-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     kmod(l2tp_core.ko)
Recommends:     kmod(l2tp_eth.ko)
Recommends:     kmod(l2tp_netlink.ko)
# Workaround for dnf pulling in kernel-debug-modules-extra over
# kernel-modules-extra to satisfy the kmod dependencies (rhbz#1192189)
Suggests:       kernel-modules-extra
%endif

%description
fastd is a secure tunneling daemon with some unique features:

 - Very small binary (about 100KB on OpenWRT in the default configuration,
   including all dependencies besides libc)
 - Exchangable crypto methods
 - Transport over UDP for simple usage behind NAT
 - Can run in 1:1 and 1:n scenarios
 - There are no server and client roles defined by the protocol, this is just
   defined by the usage.
 - Only one instance of the daemon is needed on each host to create a full mesh
   If no full mesh is established, a routing protocol is necessary to enable
   hosts that are not connected directly to reach each other

%prep
%autosetup -p1 -n %{setuppath}


%build
%ifnarch %{ix86} x86_64
  %meson \
    -Dcipher_salsa2012_xmm=disabled \
    -Dmac_ghash_pclmulqdq=disabled \
    -Dcipher_salsa20_xmm=disabled
%else
  %meson
%endif

%meson_build

# build documentation
pushd doc
  make text
popd

%install
%meson_install

install -Dpm 0644 doc/examples/fastd@.service $RPM_BUILD_ROOT/%{_unitdir}/%{name}@.service
install -Dpm 0644 doc/fastd.1 $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README.md doc/build/text/*
%license COPYRIGHT
%dir %{_sysconfdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_unitdir}/%{name}@.service
%{_bindir}/%{name}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 12 2022 Felix Kaechele <felix@kaechele.ca> - 22-6
- add conditionals for EL7 around Recommends and Suggests tags

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 22-4
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 22-2
- Rebuild for versioned symbols in json-c

* Sun Jun 27 2021 Felix Kaechele <felix@kaechele.ca> - 22-1
- update to 22
- add L2TP kmod recommends to enable L2TP offloading feature
- add git helper macros for easier prerelease testing

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 21-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Felix Kaechele <felix@kaechele.ca> - 21-2
- revert to legacy timestamp in changelog to make EL7 happy

* Fri Oct 23 2020 Felix Kaechele <felix@kaechele.ca> - 21-1
- update to 21
- fixes CVE-2020-27638

* Mon Oct 12 2020 Felix Kaechele <felix@kaechele.ca> - 20-3
- add conditional for sphinx on EL < 8

* Mon Oct 12 2020 Felix Kaechele <felix@kaechele.ca> - 20-2
- fix build on non x86 architectures

* Mon Oct 12 2020 Felix Kaechele <felix@kaechele.ca> - 20-1
- update to 20
- build system switched from cmake to meson
- drop OpenSSL patch (upstreamed)

* Thu Aug 13 2020 Felix Kaechele <heffer@fedoraproject.org> - 19-4
- update cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Felix Kaechele <heffer@fedoraproject.org> - 19-1
- update to v19
- change upstream and source URLs to GitHub
- enable LTO
- add OpenSSL linker fix patch

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 18-15
- Rebuild (json-c)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Felix Kaechele <heffer@fedoraproject.org> - 18-13
- fix build on F31: python-sphinx -> python3-sphinx

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 18-9
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 18-7
- Rebuilt for libjson-c.so.3

* Wed Oct 04 2017 Felix Kaechele <heffer@fedoraproject.org> - 18-6
- disable libsodium AES implementation, removed upstream

* Mon Oct 02 2017 Remi Collet <remi@fedoraproject.org> - 18-5
- rebuild for libsodium

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 30 2016 Felix Kaechele <heffer@fedoraproject.org> - 18-1
- update to version 18
- removed segfault patch
- changed Source URL to https

* Mon Mar 07 2016 Remi Collet <remi@fedoraproject.org> - 17-6
- rebuild for new libsodium soname

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 02 2016 Felix Kaechele <heffer@fedoraproject.org> - 17-4
- added patch to fix segfault

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Felix Kaechele <heffer@fedoraproject.org> - 17-2
- mark license file as %%license
- build docs with sphinx

* Tue Feb 10 2015 Felix Kaechele <heffer@fedoraproject.org> - 17-1
- update to version 17

* Tue Nov 25 2014 Felix Kaechele <heffer@fedoraproject.org> - 16-1
- update to version 16

* Sun Jul 13 2014 Felix Kaechele <heffer@fedoraproject.org> - 14-1
- update to v14

* Sat Mar 29 2014 Felix Kaechele <heffer@fedoraproject.org> - 12-1
- first package version
