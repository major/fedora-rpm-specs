Name:           scanssh
Summary:        Fast SSH server and open proxy scanner
Version:        2.1.2
Release:        19%{?dist}
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
URL:            http://github.com/ofalk/scanssh/wiki
Source0:        http://github.com/ofalk/%{name}/archive/%{version}.tar.gz
Patch0:         scanssh-2.1-hide.patch
# HACK: Do not drop user provided CFLAGS
Patch1:         scanssh-2.1.1-autotools.patch
Patch2:         scanssh-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  libdnet-devel
BuildRequires:  libevent-devel

%description
ScanSSH supports scanning a list of addresses and networks for open proxies,
SSH protocol servers, Web and SMTP servers. Where possible ScanSSH, displays
the version number of the running services. ScanSSH protocol scanner supports
random selection of IP addresses from large network ranges and is useful for
gathering statistics on the deployment of SSH protocol servers in a company
or the Internet as whole.

%prep
%setup -q %{name}-%{version}
%{?_with_hidescan:%patch0 -p1}
%patch -P1 -p1
%patch -P2 -p1

# Remove CFLAGS - They must not be overriden in Makefiles
sed -i -e '/^CFLAGS =.*$/d' Makefile*

# We are patching autotools-generated files.
# Avoid re-running the autotools
touch -r aclocal.m4 configure* Makefile*

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc README.md
%{_bindir}/scanssh
%{_mandir}/man1/scanssh*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.2-18
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Florian Weimer <fweimer@redhat.com> - 2.1.2-13
- C99 compatibility fixes

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 10:42:45 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.2-8
- Rebuilt for libevent 2.1.12

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 06 2018 Oliver Falk <oliver@linux-kernel.at> - 2.1.2-3
- Bump release for rebuilding against latest libdnet version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Oliver Falk <oliver@linux-kernel.at> - 2.1.2-1
- Update
- Rebuild for f28 (RHBZ#1573057)
- Cleanup spec

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.1-13
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.1-8
- Add scanssh-2.1.1-autotools.patch (Fix F23FTBFS, RHBZ#1239993).
- Remove redundant -Wall from CFLAGS (Already in %%optflags)

* Tue Jul 7 2015 Mosaab Alzoubi <moceap@hotmail.com> - 2.1.1-7
- Fix #1239993

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Christopher Meng <rpm@cicku.me> - 2.1.1-3
- SPEC cleanup.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Oliver Falk <oliver@linux-kernel.at> - 2.1.1-1
- Update to - hopefully fix BZ#926490

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 01 2011 Oliver Falk <oliver@linux-kernel.at> - 2.1-22
- Rebuild for new libevent/libdnet

* Sun Feb 13 2011 Oliver Falk <oliver@linux-kernel.at> - 2.1-21
- Rebuild for new libevent

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 30 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.1-17
- Rebuild for new libevent

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.1-16
- Bump-n-build for GCC 4.3

* Sat Jan 26 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.1-15
- Rebuild for new libevent.

* Tue Aug 21 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.1-14
- License correction

* Tue Aug 21 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.1-13
- Rebuild for BuildID

* Sun Mar 11 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.1-12
- Bump-n-build due to libevent upgrade (my own fault)

* Mon Feb 26 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.1-11
- Bump-n-build due to libevent upgrade

* Wed Nov 29 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.1-10
- Rebuild due to libpcap upgrade

* Wed Oct 04 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.1-9
- Bump-n-build

* Tue Sep 19 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> - 2.1-8
- I suppose I need to port this one to FC6 now, huh?

* Tue Sep 19 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> - 2.1-7
- Bump for FC6 rebuild

* Mon Nov 14 2005 Oliver Falk <oliver@linux-kernel.at> - 2.1-6
- Rebuild

* Thu Aug 11 2005 Oliver Falk <oliver@linux-kernel.at> - 2.1-5
- Make hidescan patch not applied by default, use
  --define 'with_hidescan 1' if you want it enabled

* Mon Aug 08 2005 Oliver Falk <oliver@linux-kernel.at> - 2.1-4
- Remove Requires, rpm will detect it automatically

* Mon Aug 08 2005 Oliver Falk <oliver@linux-kernel.at> - 2.1-3
- Integrate changes suggested by José Pedro Oliveira after
  first FE review

* Mon Jun 20 2005 Oliver Falk <oliver@linux-kernel.at> - 2.1-2
- Add patch to make us invisible/hide us. Don't let OpenSSH know
  that we scan it.

* Tue Jun 07 2005 Oliver Falk <oliver@linux-kernel.at> - 2.1-1
- Initial build for FC 4
