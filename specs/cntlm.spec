%global _hardened_build 1

Summary:          Fast NTLM authentication proxy with tunneling
Name:             cntlm
Version:          0.92.3
Release:          31%{?dist}
License:          GPL-2.0-or-later

URL:              http://cntlm.sourceforge.net/
Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:          cntlm.tmpfiles
Source2:          cntlm.service
# Don't override global CFLAGS/LDFLAGS and don't strip installed binaries
Patch0:           cntlm_makefile.patch
Patch1: cntlm-c99.patch

BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    systemd
%{?systemd_requires}


%description
Cntlm is a fast and efficient NTLM proxy, with support for TCP/IP tunneling,
authenticated connection caching, ACLs, proper daemon logging and behavior
and much more. It has up to ten times faster responses than similar NTLM
proxies, while using by orders or magnitude less RAM and CPU. Manual page
contains detailed information.


%prep
%autosetup -p1

# Create a sysusers.d config file
cat >cntlm.sysusers.conf <<EOF
u cntlm - '%{name} daemon' %{_localstatedir}/run/%{name} -
EOF


%build
%configure
%make_build SYSCONFDIR=%{_sysconfdir}


%install
make BINDIR=%{buildroot}%{_sbindir} MANDIR=%{buildroot}%{_mandir} SYSCONFDIR=%{buildroot}%{_sysconfdir} install

install -D -m 0644 rpm/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cntlmd
install -D -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

install -D -d -m 0755 %{buildroot}/run/%{name}/

install -m0644 -D cntlm.sysusers.conf %{buildroot}%{_sysusersdir}/cntlm.conf




%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README COPYRIGHT
%license LICENSE
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/cntlmd
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%attr(755, %{name}, %{name}) %dir /run/%{name}/
%{_sysusersdir}/cntlm.conf


%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.92.3-31
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Florian Weimer <fweimer@redhat.com> - 0.92.3-25
- Fix C99 compatibility issues

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.92.3-20
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-5
- Set correct permissions on /run/cntlm/

* Thu Dec 12 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-4
- Really create /run/cntlm/ on install

* Wed Oct 23 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-3
- Install /run/cntlm, change /var/run -> /run

* Mon Aug 26 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-2
- Fix debuginfo package empty (rhbz#1001302)

* Thu Aug 22 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-1
- Update to 0.92.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan  4 2012 Matt Domsch <mdomsch@fedoraproject.org> - 0.92-2
- convert to systemd (BZ771504), with unit file by Jóhann B. Guðmundsson

* Mon Dec  5 2011 Matt Domsch <mdomsch@fedoraproject.org> - 0.92-1
- update to new bugfix release (BZ760164)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-8
- add /etc/tmpfiles.d/cntlm.conf to create /var/run/cntlm/ (BZ656561)

* Mon Nov  8 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-7
- install NetworkManager dispatcher script, fixes BZ650079

* Mon Sep 27 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-6
- set SYSCONFDIR during build.  Fixes BZ637767

* Wed Sep  1 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-5
- add define for _initddir, needed on el5

* Thu Aug 26 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-4
- initscript: use pidfile to killproc

* Wed Aug 25 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-3
- additional fixes per package review

* Tue Aug 24 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-2
- updated spec to match Fedora packaging guidelines

* Fri Jul 27 2007 Radislav Vrnata <vrnata at gedas.cz>
- added support for SuSE Linux

* Fri Jul 27 2007 Radislav Vrnata <vrnata at gedas.cz>
- fixed pre, post, preun, postun macros bugs affecting upgrade process

* Wed May 30 2007 Since 0.28 maintained by <dave@awk.cz>


* Mon May 28 2007 Radislav Vrnata <vrnata at gedas.cz>
- Version 0.27
- First release
