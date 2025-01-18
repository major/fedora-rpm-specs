# hardened build if not overriden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build}%{!?_hardened_build:0}
%global cflags_harden -fpie
%global ldflags_harden -pie -z relro -z now
%endif

Summary: Routing daemon for the ampr network
Name: ampr-ripd
Version: 2.4.1
Release: 10%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.yo2loj.ro/hamprojects/
BuildRequires: gcc, dos2unix, systemd
BuildRequires: make
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0: http://www.yo2loj.ro/hamprojects/%{name}-%{version}.tgz
Source1: ampr-ripd.service
# upstream notified
Source2: COPYING
Patch0: ampr-ripd-2.4.1-install-fix.patch
Patch1: ampr-ripd-2.1.1-examples-noshebang.patch
Patch2: ampr-ripd-2.4.1-pidfile.patch

%description
Routing daemon written in C similar to Hessu's rip44d including optional
resending of RIPv2 broadcasts for router injection.

%prep
%setup -q
%patch -P0 -p1 -b .install-fix
%patch -P1 -p1 -b .examples-noshebang
%patch -P2 -p1 -b .pidfile
cp %{SOURCE2} .

%build
make %{?_smp_mflags} CFLAGS="%{optflags} %{?cflags_harden}" LDFLAGS="%{?__global_ldflags} %{?ldflags_harden}"

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

# Systemd
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# Examples
install -Dd %{buildroot}%{_datadir}/%{name}/examples
install -Dpm 644 -t %{buildroot}%{_datadir}/%{name}/examples examples/ampr-run.sh examples/find_pass.sh \
  examples/interfaces

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc COPYING manual.txt

%{_sbindir}/ampr-ripd
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_unitdir}/%{name}.service

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.1-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.1-1
- New version
  Resolves: rhbz#2030369

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3-10
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3-3
- Fixed FTBFS by adding gcc requirement
  Resolves: rhbz#1603375

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun  5 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3-1
- New version
  Resolves: rhbz#1458559
- De-fuzzified patches

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2-1
- New version
  Resolves: rhbz#1457007

* Mon May 29 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.1-1
- New version
  Resolves: rhbz#1456303
- Updated patches

* Mon May 22 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0-1
- New version
  Resolves: rhbz#1452948

* Thu Apr 20 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.16.3-1
- New version
  Resolves: rhbz#1443785

* Mon Apr 10 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.16.2-1
- New version
  Resolves: rhbz#1440340
- Updated pidfile patch

* Tue Apr  4 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.16-1
- New version
  Resolves: rhbz#1438615
- Updated patches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.15-1
- New version
  Resolves: rhbz#1378260
- Updated / de-fuzzified patches

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.13-1
- New version
  Resolves: rhbz#1166335
- Updated pidfile patch

* Mon Sep  8 2014 Jan Synáček <jsynacek@redhat.com> - 1.11-2
- Make debuginfo available (#1139051)

* Tue Jul 22 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11-1
- Initial release
