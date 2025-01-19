Summary: An NFS traffic monitoring tool
Name: nfswatch
Version: 4.99.13
Release: 4%{?dist}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://nfswatch.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc libpcap-devel ncurses-devel libtirpc-devel

%description
Nfswatch is a command-line tool for monitoring NFS traffic.
Nfswatch can capture and analyze the NFS packets on a particular
network interface or on all interfaces.

Install nfswatch if you need a program to monitor NFS traffic.

%prep
%setup -q

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
make STRIP= MANSUF=8 DESTDIR=${RPM_BUILD_ROOT} install

%files
%doc	LICENSE README
%{_sbindir}/nfswatch
%{_sbindir}/nfslogsum
%{_mandir}/man8/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 4.99.13-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 21 2024 Christian Iseli <christian.iseli@epfl.ch> - 4.99.13-1
- Update to latest upstream version
- Address too many warning messages printed (bz 2263223)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Christian Iseli <Christian.Iseli@unil.ch> - 4.99.12-1
- Update to latest upstream version
- Fix FTBFS (bz 2113548)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Christian Iseli <Christian.Iseli@unil.ch> - 4.99.11-16
- Fix FTBFS (bz 1583309)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 23 2010 Christian Iseli <Christian.Iseli@licr.org> 4.99.11-1
 - new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 15 2009 Christian Iseli <Christian.Iseli@licr.org> 4.99.10-1
 - new upstream version
 - needs libpcap-devel

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.99.9-3
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Christian Iseli <Christian.Iseli@licr.org> 4.99.9-2
 - rebuild for BuildID

* Wed May 30 2007 Christian Iseli <Christian.Iseli@licr.org> 4.99.9-1
 - new upstream version

* Tue Mar 13 2007 Christian Iseli <Christian.Iseli@licr.org> 4.99.8-1
 - new upstream version
 - Set Source0 according to Packaging/SourceURL

* Tue Jan 30 2007 Christian Iseli <Christian.Iseli@licr.org> 4.99.7-1
 - new upstream version
 - use new Makefile's install
 - remove Prefix tag (useless according to rpmlint)

* Tue Sep 05 2006 Christian Iseli <Christian.Iseli@licr.org> 4.99.6-2
 - rebuild for FC 6

* Wed Jun 14 2006 Christian Iseli <Christian.Iseli@licr.org> 4.99.6-1
 - new upstream version

* Wed Feb 15 2006 Christian Iseli <Christian.Iseli@licr.org> 4.99.5-3
 - rebuild for FE 5

* Fri Dec 23 2005 Christian Iseli <Christian.Iseli@licr.org> 4.99.5-2
 - rebuild with gcc-4.1

* Tue Nov 29 2005 Christian Iseli <Christian.Iseli@licr.org> 4.99.5-1
 - new upstream version

* Tue Jul 12 2005 Christian Iseli <Christian.Iseli@licr.org> 4.99.4-1
 - new upstream version

* Wed Jun  1 2005 Christian Iseli <Christian.Iseli@licr.org> 4.99.2-3
 - rebuilt

* Mon May 09 2005 Christian Iseli <Christian.Iseli@licr.org> 4.99.2-2
 - rebuilt

* Fri Apr 22 2005 Christian Iseli <Christian.Iseli@licr.org> 4.99.2-1
 - new upstream version

* Fri Feb 25 2005 Christian Iseli <Christian.Iseli@licr.org> 4.99.1-1
 - new upstream version

* Sun Feb  6 2005 Christian Iseli <Christian.Iseli@licr.org> 4.99.0-1
 - Create spec file.
