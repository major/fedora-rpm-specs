Summary:     Inotify cron system
Name:        incron
Version:     0.5.12
Release:     27%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:     GPL-2.0-only
URL:         https://github.com/ar-/incron
Source0:     https://github.com/ar-/%{name}/archive/%{version}.tar.gz
Source1:     incrond.service
Patch0:      incron-0.5.10-gcc.patch
Patch1:      incron-0.5.12-prevent-zombies.patch
# https://github.com/ar-/incron/pull/56
Patch2:      56.patch

BuildRequires: systemd
BuildRequires: gcc-c++
BuildRequires: make

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
This program is an "inotify cron" system.
It consists of a daemon and a table manipulator.
You can use it a similar way as the regular cron.
The difference is that the inotify cron handles
filesystem events rather than time periods.

%prep
%setup -q
%patch -P0 -p1 -b .gcc
%patch -P1 -p1
%patch -P2 -p1

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags} -std=c++14" LDFLAGS="%{__global_ldflags}"

%install
#install files manually since source Makefile tries to do it as root
install -D -p incrond %{buildroot}%{_sbindir}/incrond
install -D -p -m 4755 incrontab %{buildroot}%{_bindir}/incrontab
install -d %{buildroot}%{_localstatedir}/spool/%{name}
install -d %{buildroot}%{_sysconfdir}/%{name}.d
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/incrond.service
install -D -p -m 0644 incron.conf.example %{buildroot}%{_sysconfdir}/%{name}.conf

# install manpages
make install-man MANPATH="%{buildroot}%{_mandir}" INSTALL="install -D -p"

%post
%systemd_post incrond.service

%preun
%systemd_preun incrond.service

%postun
%systemd_postun_with_restart incrond.service

%files
%license COPYING LICENSE-GPL
%doc CHANGELOG README TODO
%attr(4755,root,root) %{_bindir}/incrontab
%{_sbindir}/incrond
%{_unitdir}/incrond.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/incrontab.1.gz
%{_mandir}/man5/incrontab.5.gz
%{_mandir}/man5/incron.conf.5.gz
%{_mandir}/man8/incrond.8.gz
%dir %{_localstatedir}/spool/%{name}
%dir %{_sysconfdir}/%{name}.d

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.12-26
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.12-17
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.5.12-15
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Kevin Fenzi <kevin@scrye.com> - 0.5.12-11
- Add patch for system-incrontabs multiplying.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Kevin Fenzi <kevin@scrye.com> - 0.5.12-9
- Add patch to prevent zombies from upstream post release commits. Fixes bug #1656939

* Tue Jul 17 2018 Kevin Fenzi <kevin@scrye.com> - 0.5.12-8
- Fix FTBFS by adding BuildRequires: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Orion Poplawski <orion@cora.nwra.com> - 0.5.12-4
- Do not install service file as executable
- Use %%license
- Cleanup spec

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Kevin Fenzi <kevin@scrye.com> - 0.5.12-1
- Update to 0.5.12

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.10-9
- Rebuilt for GCC 5 C++11 ABI change

* Wed Sep 10 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.5.10-8
- inotify_init is legacy syscall not supported on AArch64

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Kevin Fenzi <kevin@scrye.com> 0.5.10-5
- Add BuildRequires on systemd to make sure we have the _unitdir macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Kevin Fenzi <kevin@scrye.com> 0.5.10-3
- Add hardening flags. Fixes bug #965519

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Kevin Fenzi <kevin@scrye.com> 0.5.10-1
- Update to 0.5.10
- Add systemd macros for presets. Fixes bug #850158

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Jon Ciesla <limburgher@gmail.com> - 0.5.9-4
- Migrate to systemd, BZ 789688.
- gcc47 patch.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 21 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.5.9-1
- Upstream released new version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.5.8-1
- Upstream released new version
- GCC 4.4 fixes
- Drop GCC 4.3 patch, fixed upstream

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 09 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 0.5.7-1
- Sync with upstream

* Thu Mar 13 2007 <ruben@rubenkerkhof.com> 0.5.5-1
- Sync with upstream
* Mon Feb 12 2007 <ruben@rubenkerkhof.com> 0.5.4-1
- Update to new upstream version
- Upstream fixed permissions on pidfile
- New manpage for incron.conf
- Upstream fixed example conf file
* Sun Feb 04 2007 <ruben@rubenkerkhof.com> 0.5.1-1
- Updated to new upstream version
- Upstream fixed the incorrect encoding of the LICENSE-GPL file
* Sun Jan 27 2007 <ruben@rubenkerkhof.com> 0.5.0-1
- Updated to new upstream version
- Changed the service name in the scriptlets
- Added a configuration file
- Included GPL License
* Sat Jan 27 2007 <ruben@rubenkerkhof.com> 0.4.0-1
- First try at packaging it up
