Summary: Generate a readout of the current bandwidth use
Name: bwbar
Version: 1.2.3
Release: 39%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://www.kernel.org/pub/software/web/bwbar/bwbar-1.2.3.tar.bz2
Source1: bwbar.systemd
Source2: bwbar.8
Patch0: bwbar.daemon.patch
Patch1: bwbar.debian-010_directory_option.patch
Patch2: bwbar.debian-020_proc_net_2.6.x_fix.patch
Patch3: bwbar.zlib.h.patch
URL: http://www.kernel.org/pub/software/web/bwbar/
BuildRequires:  gcc
BuildRequires: libpng-devel systemd-units
BuildRequires: make
Requires(post): systemd-units, systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
bwbar is a small program that generates a text and a graphical readout
of the current bandwidth use.  It is currently for Linux only.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_mandir}/man8
%{__mkdir_p} $RPM_BUILD_ROOT%{_initrddir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__install} -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
%{__install} -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man8

%{__cat} >> $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/bwbar << END
#OPTIONS="eth0 100 -d /path/to/outdir"
END

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%triggerun -- %{name} < 1.2.3-11
/usr/bin/systemd-sysv-convert --save %{name} >/dev/null 2>&1 ||:
/bin/systemctl --no-reload enable %{name}.service >/dev/null 2>&1 ||:
/sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :


%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man8/*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.3-38
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-30
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 21 2012 Adrian Reber <adrian@lisas.de> - 1.2.3-13
- fix for "Introduce new systemd-rpm macros in bwbar spec file" (#850052)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 25 2012 Adrian Reber <adrian@lisas.de> - 1.2.3-11
- added systemd files
- almost remove '-D' daemon feature (not needed with systemd)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adrian Reber <adrian@lisas.de> - 1.2.3-9
- fix build failure with new libpng

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.3-8
- Rebuild for new libpng

* Thu Mar 31 2011 Adrian Reber <adrian@lisas.de> - 1.2.3-7
- fix patch (**** rejecting target file name with ".." component)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 01 2008 Adrian Reber <adrian@lisas.de> - 1.2.3-3
- recreated bwbar.daemon.patch to apply cleanly

* Fri Feb 15 2008 Adrian Reber <adrian@lisas.de> - 1.2.3-2
- rebuilt for gcc43

* Sat Aug 25 2007 Adrian Reber <adrian@lisas.de> - 1.2.3-1
- updated to 1.2.3
- adapted daemon patch
- fixed some rpmlint warnings/errors

* Mon Sep 11 2006 Adrian Reber <adrian@lisas.de> - 1.2.2-5
- rebuilt

* Wed Feb 13 2006 Adrian Reber <adrian@lisas.de> - 1.2.2-4
- rebuilt

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Jul 23 2004 Adrian Reber <adrian@lisas.de> - 0:1.2.2-0.fdr.2
- changed the daemon patch to use -D and --Daemon
- added a debian patch to specify an output directory
- added another debian patch
- added the man page (also from the debian package)

* Fri Jul 16 2004 Adrian Reber <adrian@lisas.de> - 0:1.2.2-0.fdr.1
- Initial RPM release.
