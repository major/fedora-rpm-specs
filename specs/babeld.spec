%define _hardened_build 1

Name:           babeld
Version:        1.13.1
Release:        5%{?dist}
Summary:        Ad-hoc network routing daemon

License:        MIT
URL:            http://www.pps.univ-paris-diderot.fr/~jch/software/babel/
Source0:        http://www.pps.univ-paris-diderot.fr/~jch/software/files/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
Source3:        %{name}.logrotate
BuildRequires:	systemd gcc
BuildRequires: make
Conflicts:      quagga

%description
Babel is a loop-avoiding distance-vector routing protocol roughly
based on HSDV and AODV, but with provisions for link cost estimation
and redistribution of routes from other routing protocols.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}


%install
install -Dpm 755 babeld $RPM_BUILD_ROOT%{_sbindir}/babeld
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/babeld.conf
install -Dpm 644 babeld.man $RPM_BUILD_ROOT/%{_mandir}/man8/babeld.8
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/
install -Dp -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/babeld

%post
%systemd_post babeld.service
  
%preun
%systemd_preun babeld.service

%postun
%systemd_postun_with_restart babeld.service


%files
%license LICENCE
%doc CHANGES README
%{_sbindir}/babeld
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/babeld.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/babeld
%{_mandir}/man8/babeld.8.*
%ghost %attr(0600,root,root) %{_localstatedir}/lib/babel-state
%ghost %attr(0600,root,root) %{_localstatedir}/log/babel.log


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.13.1-1
- 1.13.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.13-1
- 1.13

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.12.2-2
- migrated to SPDX license

* Tue Feb 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.12.2-1
- 1.12.2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.12.1-1
- 1.12.1

* Thu May 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.12-1
- 1.12

* Tue Apr 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.11-1
- 1.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.10-1
- 1.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.9.2-1
- 1.9.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.9.1-1
- 1.9.1

* Mon Aug 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.9.0-1
- 1.9.0

* Wed Jul 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.8.5-1
- 1.8.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.8.3-1
- 1.8.3

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.8.2-3
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.8.2-1
- 1.8.2

* Wed Apr 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.8.1-1
- 1.8.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jon Ciesla <limburgher@gmail.com> - 1.8.0-3
- systemd cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Jon Ciesla <limburgher@gmail.com> - 1.8.0-1
- 1.8.0, BZ 1402171

* Mon Feb 15 2016 Jon Ciesla <limburgher@gmail.com> - 1.7.1-1
- 1.7.1

* Thu Feb 04 2016 Jon Ciesla <limburgher@gmail.com> - 1.7.0-1
- 1.7.0, BZ 1304562.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Jon Ciesla <limburgher@gmail.com> - 1.6.3-1
- 1.6.3, BZ 1268162.

* Mon Aug 03 2015 Jon Ciesla <limburgher@gmail.com> - 1.6.2-1
- 1.6.2, BZ 1249255.

* Thu Jun 25 2015 Jon Ciesla <limburgher@gmail.com> - 1.6.1-1
- 1.6.1, BZ 1232520.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Jon Ciesla <limburgher@gmail.com> - 1.6.0-1
- 1.6.0, BZ 1211807.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 07 2014 Jon Ciesla <limburgher@gmail.com> - 1.5.1-1
- 1.5.1, BZ 1116566.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Jon Ciesla <limburgher@gmail.com> - 1.5.0-1
- 1.5.0, BZ 1100632.

* Mon Nov 18 2013 Jon Ciesla <limburgher@gmail.com> - 1.4.3-1
- 1.4.3, BZ 1031256.

* Mon Aug 05 2013 Jon Ciesla <limburgher@gmail.com> - 1.4.2-3
- Fix FTBFS.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Jon Ciesla <limburgher@gmail.com> - 1.4.2-1
- 1.4.2, BZ 975973.

* Tue May 28 2013 Jon Ciesla <limburgher@gmail.com> - 1.4.1-1
- 1.4.1, BZ 967786.

* Mon May 06 2013 Jon Ciesla <limburgher@gmail.com> - 1.4.0-1
- 1.4.0, BZ 959897.

* Fri May 03 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.6-1
- 1.3.6, BZ 959103.

* Mon Apr 15 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.5-1
- 1.3.5, BZ 952151.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 04 2012 Jon Ciesla <limburgher@gmail.com> - 1.3.4-3
- Conflict with quagga and it's babeld.

* Thu Aug 23 2012 Jon Ciesla <limburgher@gmail.com> - 1.3.4-2
- Dropped unneeded parts for review.
- Added log, logrotate, state file, and default config.

* Tue Aug 21 2012 Jon Ciesla <limburgher@gmail.com> - 1.3.4-1
- Initial package.
