%global _hardened_build 1

Name:           netbsd-iscsi
Version:        20111006
Release:        21%{?dist}
Summary:        User-space implementation of iSCSI target from NetBSD project

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://NetBSD.org/
Source0:        http://ftp.netbsd.org/pub/pkgsrc/distfiles/netbsd-iscsi-%{version}.tar.gz
Source1:        netbsd-iscsi.service
Source2:        netbsd-iscsi.sysconfig
Patch0:         netbsd-iscsi-20111006-linux.patch
Patch1:         netbsd-iscsi-20111006-utf8.patch
Patch2:         netbsd-iscsi-20111006-allocate.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  systemd
BuildRequires:  fuse-devel

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
NetBSD iSCSI is an iSCSI target following the iSCSI RFC 3720.  It is based
on the BSD-licensed Intel iSCSI reference model.  It has been tried and
tested with the Microsoft iSCSI initiator, version 1.06.


%prep
%setup -q
%patch -P0 -p1 -b .linux
%patch -P1 -p1 -b .utf8
%patch -P2 -p1 -b .allocate


%build
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
# We disable libscsi.so because it has a SONAME conflict with iscsi-initiator-utils
%configure --enable-shared=no
make %{?_smp_mflags} all


%install
%make_install

install -d %{buildroot}%{_sysconfdir}/sysconfig
install -pm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/netbsd-iscsi

install -d %{buildroot}%{_unitdir}
install -pm644 %{SOURCE1} %{buildroot}%{_unitdir}/netbsd-iscsi.service

# Example configuration
install -d %{buildroot}%{_sysconfdir}/iscsi
install -pm644 src/etc/targets %{buildroot}%{_sysconfdir}/iscsi


%post
%systemd_post netbsd-iscsi.service

%preun
%systemd_preun netbsd-iscsi.service

%postun
%systemd_postun_with_restart netbsd-iscsi.service


%files
%dir %{_sysconfdir}/iscsi
%config(noreplace) %{_sysconfdir}/iscsi/targets
%config(noreplace) %{_sysconfdir}/sysconfig/netbsd-iscsi
%{_unitdir}/netbsd-iscsi.service
%{_bindir}/iscsi-target
%{_bindir}/iscsi-initiator
%exclude %{_mandir}/man3/libiscsi.3*
%{_mandir}/man5/targets.5*
%{_mandir}/man8/iscsi-target.8*
%{_mandir}/man8/iscsi-initiator.8*
%exclude %{_libdir}/libiscsi.a
%exclude %{_libdir}/libiscsi.la
%doc doc/license doc/README doc/README_OSD
%doc doc/COMPATIBILITY doc/FAQ doc/PERFORMANCE


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 20111006-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  8 2022 Florian Weimer <fweimer@redhat.com> - 20111006-14
- Fix placement of #endif in netbsd-iscsi-20111006-allocate.patch.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20111006-10
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20111006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 20111006-1
- Update to the latest upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080207-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080207-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080207-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20080207-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep  2 2014 Lubomir Rintel <lkundrak@v3.sk> - 20080207-14
- Enable hardening (Dhiru Kholia, #955290)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Lubomir Rintel <lkundrak@v3.sk> - 20080207-11
- Fix environment file inclusion

* Tue May 27 2014 Lubomir Rintel <lkundrak@v3.sk> - 20080207-10
- Port to systemd (#914421)

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 20080207-9
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 3 2008 Lubomir Rintel <lkundrak@v3.sk> - 20080207-1
- Update to more recent upstream code
- Remove the silly prealocation code (#465533)

* Mon Jul 28 2008 Lubomir Rintel <lkundrak@v3.sk> 20071205-3
- Init script (thanks to Saturo Sato)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20071205-2
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Lubomir Kundrak <lkundrak@redhat.com> 20071205-1
- Initial package
