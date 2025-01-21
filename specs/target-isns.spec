%define __cmake_in_source_build 1

Name:           target-isns
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        An iSNS client for the Linux LIO iSCSI target 
Version:        0.6.8
Release:        15%{?dist}
URL:            https://github.com/cvubrugier/target-isns
Source:         https://github.com/open-iscsi/target-isns/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-disable-stringop-overflow-and-stringop-truncation-er.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  cmake systemd-units
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
Target-isns is an Internet Storage Name Service (iSNS) client for the Linux
LIO iSCSI target. It allows registering LIO iSCSI targets with an iSNS server.

%prep
%setup -q
%patch -P0 -p1

%build
%cmake -DSUPPORT_SYSTEMD=ON .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -m 644 target-isns.service %{buildroot}%{_unitdir}

%post
%systemd_post target-isns.service

%preun
%systemd_preun target-isns.service

%postun
%systemd_postun_with_restart target-isns.service

%files
%{_bindir}/target-isns
%config(noreplace) %{_sysconfdir}/target-isns.conf
%{_mandir}/man8/target-isns.8.gz
%{_unitdir}/target-isns.service
%doc README.md
%license COPYING

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.8-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.8-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 0.6.8-4
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 25 2020 Maurizio Lombardi <mlombard@redhat.com> - 0.6.8-1
- Update to new upstream version 0.6.8

* Tue Mar 31 2020 Maurizio Lombardi <mlombard@redhat.com> - 0.6.7-1
- Update to new upstream version 0.6.7

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Tom Callaway <spot@fedoraproject.org> - 0.6.6-1
- update to 0.6.6

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Andy Grover <agrover@redhat.com> - 0.6.2-1
- New upstream version

* Fri Oct 16 2015 Andy Grover <agrover@redhat.com> - 0.5-2
- Initial Fedora packaging
