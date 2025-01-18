# hardened build if not overriden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build}%{!?_hardened_build:0}
%global cflags_harden -fpie
%global ldflags_harden -pie -z relro -z now
%endif

Summary: An user-space IPIP encapsulation daemon for the ampr network
Name: amprd
Version: 3.0.1
Release: 9%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.yo2loj.ro/hamprojects/
BuildRequires: gcc
BuildRequires: dos2unix
BuildRequires: systemd
BuildRequires: make
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0: http://www.yo2loj.ro/hamprojects/%{name}-%{version}.tgz
Source1: amprd.service
Patch0: amprd-3.0-install-fix.patch

%description
An user-space IPIP encapsulation daemon with automatic RIPv2 multicast
processing and multiple tunnel support for the ampr network.
All RIPv2 processing, encapsulation, decapsulation and routing happens
inside the daemon and it offers one or more virtual TUN interfaces to
the system for your 44net traffic.

%prep
%autosetup -p1

dos2unix minGlue.h

%build
make %{?_smp_mflags} CFLAGS="%{optflags} %{?cflags_harden}" LDFLAGS="%{?__global_ldflags} %{?ldflags_harden}"

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

# Systemd
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# Examples
install -Dd %{buildroot}%{_datadir}/%{name}
install -Dpm 644 -t %{buildroot}%{_datadir}/%{name} startup_example.sh interfaces_example

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc COPYING README

%{_sbindir}/amprd
%config(noreplace) %{_sysconfdir}/amprd.conf
%{_datadir}/%{name}
%{_var}/lib/amprd
%{_unitdir}/amprd.service

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.1-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0.1-1
- New version
  Resolves: rhbz#2103065

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-1
- New version
  Resolves: rhbz#1705380

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-6
- Fixed FTBFS by adding gcc requirement
  Resolves: rhbz#1603377

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun  5 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-1
- New version
  Resolves: rhbz#1458458

* Mon Apr 10 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6-1
- New version
  Resolves: rhbz#1440339
  Updated install-fix patch

* Tue Apr  4 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5-1
- New version
  Resolves: rhbz#1438614
- Dropped pidfile and examples-noshebang patches (both upstreamed)
- Updated install-fix patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 29 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4-2
- Fixed ldflags_harden

* Tue Jul 29 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4-1
- Initial release
