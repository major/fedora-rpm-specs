%global _hardened_build 1

Name:             bird
Version:          2.16.1
Release:          1%{?dist}
Summary:          BIRD Internet Routing Daemon

License:          GPL-2.0-or-later
URL:              https://bird.network.cz/
Source0:          https://bird.network.cz/download/bird-%{version}.tar.gz
Source1:          bird.service
Source2:          bird.tmpfilesd
Source3:          bird.sysusersd

BuildRequires:    flex
BuildRequires:    bison
BuildRequires:    ncurses-devel
BuildRequires:    readline-devel
BuildRequires:    sed
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    libssh-devel
BuildRequires:    systemd-rpm-macros
%{?systemd_requires}
%{?sysusers_requires_compat}

Obsoletes:        bird-sysvinit
Obsoletes:        bird6 < 2.0.2-1
Provides:         bird6 = %{version}-%{release}

%description
BIRD is a dynamic IP routing daemon supporting both, IPv4 and IPv6, Border
Gateway Protocol (BGPv4), Routing Information Protocol (RIPv2, RIPng), Open
Shortest Path First protocol (OSPFv2, OSPFv3), Babel Routing Protocol (Babel),
Bidirectional Forwarding Detection (BFD), IPv6 router advertisements, static
routes, inter-table protocol, command-line interface allowing on-line control
and inspection of the status of the daemon, soft reconfiguration as well as a
powerful language for route filtering.

%if 0%{!?_without_doc:1}
%package doc
Summary:          Documentation for BIRD Internet Routing Daemon
BuildRequires:    linuxdoc-tools sgml-common perl(FindBin)
BuildArch:        noarch

%description doc
Documentation for users and programmers of the BIRD Internet Routing Daemon.

BIRD is a dynamic IP routing daemon supporting both, IPv4 and IPv6, Border
Gateway Protocol (BGPv4), Routing Information Protocol (RIPv2, RIPng), Open
Shortest Path First protocol (OSPFv2, OSPFv3), Babel Routing Protocol (Babel),
Bidirectional Forwarding Detection (BFD), IPv6 router advertisements, static
routes, inter-table protocol, command-line interface allowing on-line control
and inspection of the status of the daemon, soft reconfiguration as well as a
powerful language for route filtering.
%endif

%prep
%setup -q

%build
%configure --runstatedir=%{_rundir}/bird
%make_build all %{!?_without_doc:docs}

%install
%make_install

install -d %{buildroot}{%{_localstatedir}/lib/bird,%{_rundir}/bird}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/bird.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/bird.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/bird.conf

%check
make test

%pre
%sysusers_create_compat %{SOURCE3}

%post
%systemd_post bird.service

%preun
%systemd_preun bird.service

%postun
%systemd_postun_with_restart bird.service

%files
%doc NEWS README
%attr(0640,root,bird) %config(noreplace) %{_sysconfdir}/bird.conf
%{_unitdir}/bird.service
%{_sysusersdir}/bird.conf
%{_tmpfilesdir}/bird.conf
%{_sbindir}/bird
%{_sbindir}/birdc
%{_sbindir}/birdcl
%dir %attr(0750,bird,bird) %{_localstatedir}/lib/bird
%dir %attr(0750,bird,bird) %{_rundir}/bird

%if 0%{!?_without_doc:1}
%files doc
%doc NEWS README
%doc doc/bird.conf.*
%doc obj/doc/bird*.html
%doc obj/doc/bird.pdf
%doc obj/doc/prog*.html
%doc obj/doc/prog.pdf
%endif

%changelog
* Sat Jan 11 2025 Robert Scheck <robert@fedoraproject.org> - 2.16.1-1
- Upgrade to 2.16.1

* Sat Dec 07 2024 Robert Scheck <robert@fedoraproject.org> - 2.16-1
- Upgrade to 2.16 (#2330977)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 23 2024 Robert Scheck <robert@fedoraproject.org> - 2.15.1-1
- Upgrade to 2.15.1 (#2270927)

* Sun Mar 10 2024 Robert Scheck <robert@fedoraproject.org> - 2.15-1
- Upgrade to 2.15 (#2268900)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 08 2023 Robert Scheck <robert@fedoraproject.org> - 2.14-1
- Upgrade to 2.14 (#2242616)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 Robert Scheck <robert@fedoraproject.org> - 2.13.1-1
- Upgrade to 2.13.1 (#2190169)

* Sun Apr 23 2023 Robert Scheck <robert@fedoraproject.org> - 2.13-1
- Upgrade to 2.13 (#2188938)

* Tue Jan 24 2023 Robert Scheck <robert@fedoraproject.org> - 2.0.12-1
- Upgrade to 2.0.12 (#2163423)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Robert Scheck <robert@fedoraproject.org> - 2.0.11-1
- Upgrade to 2.0.11 (#2152447)

* Sat Jul 30 2022 Robert Scheck <robert@fedoraproject.org> - 2.0.10-3
- Added sysusers.d file to achieve user() and group() provides

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Robert Scheck <robert@fedoraproject.org> - 2.0.10-1
- Upgrade to 2.0.10 (#2101352)

* Thu Mar 17 2022 Robert Scheck <robert@fedoraproject.org> - 2.0.9-2
- Added patch to fix bug in babel iface reconfiguration (#2064465)

* Sun Feb 20 2022 Robert Scheck <robert@fedoraproject.org> - 2.0.9-1
- Upgrade to 2.0.9 (#2056249)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 21 2021 Robert Scheck <robert@fedoraproject.org> - 2.0.8-1
- Upgrade to 2.0.8 (#1941375)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.7-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Robert Scheck <robert@fedoraproject.org> - 2.0.7-3
- Added patch to declare variable as extern in header file

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Robert Scheck <robert@fedoraproject.org> - 2.0.7-1
- Upgrade to 2.0.7 (#1762260)

* Wed Sep 11 2019 Robert Scheck <robert@fedoraproject.org> - 2.0.6-1
- Upgrade to 2.0.6 (#1751031, #1751349)

* Mon Aug 05 2019 Robert Scheck <robert@fedoraproject.org> - 2.0.5-1
- Upgrade to 2.0.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Robert Scheck <robert@fedoraproject.org> - 2.0.4-1
- Upgrade to 2.0.4 (#1684317)
- Build require libssh-devel for RPKI-RTR protocol

* Sat Mar 30 2019 Robert Scheck <robert@fedoraproject.org> - 2.0.3-1
- Upgrade to 2.0.3

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-8
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Robert Scheck <robert@fedoraproject.org> - 2.0.2-6
- More modernizations and cleanups of spec file (#1653088 #c1)

* Sun Nov 25 2018 Robert Scheck <robert@fedoraproject.org> - 2.0.2-5
- Modernization and cleanup of spec file
- Ship PDF and HTML documentation rather SGML documentation
- Ensure /etc/bird.conf can be only read by BIRD user

* Tue Nov 20 2018 Stanislav Kozina <skozina@redhat.com> - 2.0.2-4
- Fix bird6 Provides and Obsoletes (#1524385 #c11)

* Mon Nov 19 2018 Stanislav Kozina <skozina@redhat.com> - 2.0.2-3
- Obsolete bird6 and make bird-doc noarch package

* Mon Nov 12 2018 Stanislav Kozina <skozina@redhat.com> - 2.0.2-2
- Run bird under bird user and group rather than root (#1397574)

* Mon Nov 12 2018 Stanislav Kozina <skozina@redhat.com> - 2.0.2-1
- update to 2.0.2 (#1524385)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Michal Sekletar <msekleta@redhat.com> - 1.6.3-7
- add gcc to BuildRequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.6.3-2
- Rebuild for readline 7.x

* Sat Dec 31 2016 Robert Scheck <robert@fedoraproject.org> - 1.6.3-1
- update to 1.6.3 (#1378434)

* Thu May 05 2016 Stanislav Kozina <skozina@redhat.com> - 1.6.0-1
- update to 1.6.0 (#1331895)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Michal Sekletar <msekleta@redhat.com> - 1.5.0-1
- update to 1.5.0 (#1214701)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Michal Sekletar <msekleta@redhat.com> - 1.4.5-1
- update to 1.4.5 (#1150449)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Michal Sekletar <msekleta@redhat.com> - 1.4.4-1
- update to 1.4.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Michal Sekletar <msekleta@redhat.com> - 1.4.3-1
- update to 1.4.3

* Tue Dec 03 2013 Michal Sekletar <msekleta@redhat.com> - 1.4.0-1
- update to 1.4.0

* Thu Oct 17 2013 Michal Sekletar <msekleta@redhat.com> - 1.3.11-1
- update to 1.3.11
- add systemd to BuildRequires
- change scriptlet Requires to systemd
- drop rpm triggers used for migration from sysv to systemd
- drop sysvinit subpackages
- use macroized systemd scriptlets
- specfile cleanup
- enable hardened build
- modernize systemd service file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Stanislav Kozina <stanislav.kozina@gmail.com> 1.3.10-1
- updated to latest upstream 1.3.10

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Stanislav Kozina <skozina@redhat.com> 1.3.7-1
- updated to latest upstream 1.3.7

* Wed Jan 11 2012 Jiri Skala <jskala@redhat.com> 1.3.5-1
- updated to latest upstream 1.3.5

* Wed Nov 23 2011 Jiri Skala <jskala@redhat.com> 1.3.4-2
- initscripts moved to subpackage

* Mon Oct 10 2011 Jiri Skala <jskala@redhat.com> 1.3.4-1
- updated to latest upstream 1.3.4

* Mon Sep 12 2011 Jiri Skala <jskala@redhat.com> 1.3.3-1
- updated to latest upstream 1.3.3

* Mon Jul 11 2011 Jiri Skala <jskala@redhat.com> 1.3.2-1
- updated to latest upstream 1.3.2

* Wed May 11 2011 Bill Nottingham <notting@redhat.com>  1.3.1-2
- fix systemd scriptlets for upgrade (#703234)

* Wed May 04 2011 Jan Görig <jgorig@redhat.com> 1.3.1-1
- New upstream bugfix release

* Thu Mar 31 2011 Jan Görig <jgorig@redhat.com> 1.3.0-1
- New upstream release - iBGP improved, IPv6 RA added, many changes and bufixes
- Updated systemd unit files configuration

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 11 2010 Jan Görig <jgorig@redhat.com> 1.2.5-2
- Move from SysVInit to systemd

* Mon Oct 11 2010 Jan Görig <jgorig@redhat.com> 1.2.5-1
- New upstream release

* Tue Oct 5 2010 Jan Görig <jgorig@redhat.com> 1.2.4-1
- Initial release
