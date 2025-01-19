#%%global alphatag rc

Name: iperf
Version: 2.2.1
Release: 2%{?alphatag:.%{alphatag}}%{?dist}
Summary: Measurement tool for TCP/UDP bandwidth performance
License: BSD-3-Clause
URL: http://sourceforge.net/projects/iperf2
Source: http://sourceforge.net/projects/iperf2/files/%{name}-%{version}%{?alphatag:-%{alphatag}}.tar.gz
BuildRequires: gcc-c++
BuildRequires: make

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
various parameters and UDP characteristics. Iperf reports bandwidth, delay
jitter, datagram loss.

%prep
%autosetup -p1 -n %{name}-%{version}%{?alphatag:-%{alphatag}}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%make_install

%files
%doc AUTHORS ChangeLog COPYING README doc/*.gif doc/*.html
%{_bindir}/iperf
%{_mandir}/man*/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 07 2024 Gabriel Somlo <gsomlo@gmail.com> - 2.2.1-1
- update to 2.2.1 (#2324266)

* Sun Oct 20 2024 Gabriel Somlo <gsomlo@gmail.com> - 2.2.0-4
- fix SPDX license

* Fri Oct 18 2024 Gabriel Somlo <gsomlo@gmail.com> - 2.2.0-3
- backport upstream patch to fix buffer overflow (BZ #2297736)

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.0-2.1
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 11 2024 Gabriel Somlo <gsomlo@gmail.com> 2.2.0-1
- update to 2.2.0 (#2274431)
- re-apply debuginfo patch to configure script

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 16 2023 Gabriel Somlo <gsomlo@gmail.com> 2.1.9-1
- update to 2.1.9 (#2178491)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 20 2022 Gabriel Somlo <gsomlo@gmail.com> 2.1.8-1
- update to 2.1.8 (#2118053)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 18 2022 Gabriel Somlo <gsomlo@gmail.com> 2.1.7-1
- update to 2.1.7 (#2074223)

* Sat Feb 12 2022 Jeff Law <jeffreyalaw@gmail.com> - 2.1.6-3
- Re-enable LTO.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Gabriel Somlo <gsomlo@gmail.com> 2.1.6-1
- update to 2.1.6 (#2029026)

* Sun Dec 05 2021 Gabriel Somlo <gsomlo@gmail.com> 2.1.5-1
- update to 2.1.5 (#2029026)

* Tue Aug 31 2021 Gabriel Somlo <somlo at cmu.edu> 2.1.4-2
- reimplement debug info patch in configure script
- remove autoconf build dependency
- fix autoconf-2.71 related FTBFS (#1999454)

* Sat Aug 21 2021 Gabriel Somlo <somlo at cmu.edu> 2.1.4-1
- update to 2.1.4 (#1995352)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Gabriel Somlo <somlo at cmu.edu> 2.1.3-1
- update to 2.1.3 (#1982021)

* Sat Jun 26 2021 Gabriel Somlo <somlo at cmu.edu> 2.1.2-1
- update to 2.1.2 (#1976356)

* Fri Jun 25 2021 Gabriel Somlo <somlo at cmu.edu> 2.1.1-1
- update to 2.1.1 (#1975486)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-1.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Gabriel Somlo <somlo at cmu.edu> 2.1.0-0.rc1
- update to 2.1.0-rc1 (#1884104)

* Thu Dec 24 2020 Gabriel Somlo <somlo at cmu.edu> 2.0.13-6
- Disable LTO (#1910200)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Gabriel Somlo <somlo at cmu.edu> 2.0.13-1
- update to 2.0.13 (#1668455)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Gabriel Somlo <somlo at cmu.edu> 2.0.12-[2..4]
- restore specfile cleanup changes (#1599922)
- add buildrequires gcc-c++

* Tue Jul 03 2018 Gabriel Somlo <somlo at cmu.edu> 2.0.12-1
- update to 2.0.12 (#1595235)

* Fri May 25 2018 Gabriel Somlo <somlo at cmu.edu> 2.0.11-1
- update to 2.0.11 (#1582496)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Gabriel Somlo <somlo at cmu.edu> 2.0.10-1
- update to 2.0.10 (#1356228)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Gabriel Somlo <somlo at cmu.edu> 2.0.8-6
- math header include fix for gcc6 from git 2.0.9 release candidate (# 1307641)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Gabriel Somlo <somlo at cmu.edu> 2.0.8-1
- update to 2.0.8
- update source URL in spec file
- rebase debuginfo and bindfail fixup patches
- added patch to prevent error on installing manpage

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Gabriel Somlo <somlo at cmu.edu> 2.0.5-11
- patch to exit on port bind failure (#1047172, #1047569)

* Sun Dec 22 2013 Gabriel Somlo <somlo at cmu.edu> 2.0.5-10
- added patch to build with format security enabled (#1037132)

* Tue Aug 06 2013 Gabriel Somlo <somlo at cmu.edu> 2.0.5-9
- fix debuginfo regression (#925592)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Gabriel Somlo <somlo at cmu.edu> 2.0.5-7
- added autoconf step to support aarch64 (#925592)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Gabriel Somlo <somlo at cmu.edu> 2.0.5-3
- include man page with build (BZ 756794)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 21 2010 Gabriel Somlo <somlo at cmu.edu> 2.0.5-1
- update to 2.0.5

* Tue Dec 01 2009 Gabriel Somlo <somlo at cmu.edu> 2.0.4-4
- patched to current svn trunk to address performance issues (#506884)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Gabriel Somlo <somlo at cmu.edu> 2.0.4-1
- update to 2.0.4
- patch to avoid tcp/dualtest server from quitting (bugzilla #449796), also submitted to iperf sourceforge ticket tracker (#1983829)

* Sat Oct 27 2007 Gabriel Somlo <somlo at cmu.edu> 2.0.2-4
- replace usleep with sched_yield to avoid hogging CPU (bugzilla #355211)

* Mon Jan 29 2007 Gabriel Somlo <somlo at cmu.edu> 2.0.2-3
- patch to prevent removal of debug info by ville.sxytta(at)iki.fi

* Fri Sep 08 2006 Gabriel Somlo <somlo at cmu.edu> 2.0.2-2
- rebuilt for FC6MassRebuild

* Wed Apr 19 2006 Gabriel Somlo <somlo at cmu.edu> 2.0.2-1
- initial build for fedora extras (based on Dag Wieers SRPM)
- fixed license tag: BSD (U. of IL / NCSA), not GPL
