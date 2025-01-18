%define _hardened_build 1

Name:           ahcpd
Version:        0.53
Release:        34%{?dist}
Summary:        Ad-hoc network configuration daemon

License:        MIT
URL:            http://www.pps.univ-paris-diderot.fr/~jch/software/ahcp/
Source0:        http://www.pps.univ-paris-diderot.fr/~jch/software/files/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
Source3:        %{name}.logrotate
BuildRequires: 	systemd gcc
BuildRequires: make

%description
AHCP is a configuration protocol that can replace DHCP on networks without 
transitive connectivity, such as mesh networks.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags}


%install
install -Dpm 755 ahcpd $RPM_BUILD_ROOT%{_sbindir}/ahcpd
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/ahcpd.conf
install -Dpm 644 ahcpd.man $RPM_BUILD_ROOT/%{_mandir}/man8/ahcpd.8
install -Dp -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/ahcpd
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/ahcpd/leases/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ahcp/
install -Dpm 755 ahcp-config.sh $RPM_BUILD_ROOT%{_sysconfdir}/ahcp/ahcp-config.sh


%post
%systemd_post ahcpd.service
  
%preun
%systemd_preun ahcpd.service

%postun
%systemd_postun ahcpd.service


%files
%doc CHANGES LICENCE README
%{_sbindir}/ahcpd
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/ahcpd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/ahcpd
%{_mandir}/man8/ahcpd.8.gz
%ghost %attr(0600,root,root) %{_localstatedir}/log/ahcpd.log
%config(noreplace) %{_sysconfdir}/ahcp/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.53-29
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.53-18
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jon Ciesla <limburgher@gmail.com> - 0.53-13
- systemd cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Jon Ciesla <limburgher@gmail.com> - 0.53-7
- Add ahcp-config.sh, BZ 1035710.

* Mon Aug 05 2013 Jon Ciesla <limburgher@gmail.com> - 0.53-6
- Add BuildRequires: systemd to fix FTBFS, BZ 991958.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Jon Ciesla <limburgher@gmail.com> - 0.53-4
- Add LDFLAGS to enable PIE, BZ 955446.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 27 2012 Jon Ciesla <limburgher@gmail.com> - 0.53-2
- Dropped unneeded parts for review.
- Added log, logrotate, state file, and default config.

* Tue Aug 21 2012 Jon Ciesla <limburgher@gmail.com> - 0.53-1
- Initial package.
